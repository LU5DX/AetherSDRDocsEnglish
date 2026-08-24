# DAX Audio applet

The DAX Audio applet shows per-channel RX meters and gain sliders for DAX 1-8 plus a single TX meter, with a master Enable toggle that persists as `AutoStartDAX`. It also displays slice-assignment indicators so you can confirm at a glance which slice is routed where without leaving the main window.

## Before you start

- AetherSDR must be connected to the radio. The slice-assignment indicators require a live radio connection.
- At least one slice must have a DAX channel assigned. If no slices are assigned, all indicators show `—`.
- AetherSDR v26.5.2.1 or later renders slice letters with rich text formatting for improved visibility.
- Rows above the connected radio's slice capacity are hidden. A 6300/6400 (2 slices) shows 2 DAX RX rows; a 6600/8600 (4 slices) shows 4; an 8-slice-capable radio shows all 8.
- RX meter levels are exponentially smoothed (fast attack, slow decay).

## Platform-specific behavior

### Windows
On Windows, AetherSDR does not include a built-in DAX audio bridge. The DAX Enable button, per-channel meters, gain sliders, and slice-assignment indicators are not functional because the necessary kernel-mode audio driver is only shipped on macOS and Linux. Instead, the applet shows only the notice:

> No built-in DAX driver on Windows. Use TCI, or SmartSDR DAX.

To set up DAX on Windows, use FlexRadio's own SmartSDR DAX drivers. For guidance, see **Help > Configuring Data Modes**.

### macOS and Linux
On macOS and Linux, the full DAX Audio applet is available. In v0.9.7 (Linux), DAX RX latency drops from approximately 400 ms to approximately 200 ms via a native PipeWire `pw_stream` source path, replacing the previous PulseAudio client.

## Steps

1. Click the **DAX** tray button on the right sidebar to open the DAX Audio applet.
2. On macOS or Linux, to enable DAX audio routing:
   - Click **DAX Enable**. The button text changes from "Disabled" to "Enabled".
   - AetherSDR saves the setting as `AutoStartDAX` in application settings. The DAX audio bridge starts and emits `daxToggled`.
3. Look at the status label to the right of each channel label (**DAX 1:**, **DAX 2:**, **DAX 3:**, **DAX 4:**, **DAX 5:**, **DAX 6:**, **DAX 7:**, **DAX 8:**).
4. Read the indicator for each channel. It shows either `—` (no slice assigned) or `Slice A` through `Slice H` (the letter of the slice currently routed to that channel). In v26.5.2.1, the slice letter may be displayed using rich text formatting for better legibility.
5. To see which slice is driving the DAX TX stream, read the status label on the **TX:** row. It follows the same format: `—` or `Slice A` through `Slice H`.
6. To adjust RX gain on a DAX channel, drag the meter/slider for that channel. The gain value persists in application settings (`DaxRxGain1` through `DaxRxGain8`).
7. To adjust TX gain on the DAX TX stream, drag the **TX gain+meter** slider. The gain value persists as `DaxTxGain`.
8. To disable DAX audio routing, click **DAX Enable** again. The button text changes from "Enabled" back to "Disabled".

## What each control does

| Control                               | Kind                                                                                                                     | Default                                                                                                                              |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| **DAX Enable**                        | Toggle button                                                                                                            | Off                                                                                                                                  |
| **DAX 1 gain+meter**                  | Meter/slider                                                                                                             | 0.5                                                                                                                                  |
| **DAX 2 gain+meter**                  | Meter/slider                                                                                                             | 0.5                                                                                                                                  |
| **DAX 3 gain+meter**                  | Meter/slider                                                                                                             | 0.5                                                                                                                                  |
| **DAX 4 gain+meter**                  | Meter/slider                                                                                                             | 0.5                                                                                                                                  |
| **DAX 5 gain+meter**                  | Meter/slider                                                                                                             | 0.5                                                                                                                                  |
| **DAX 6 gain+meter**                  | Meter/slider                                                                                                             | 0.5                                                                                                                                  |
| **DAX 7 gain+meter**                  | Meter/slider                                                                                                             | 0.5                                                                                                                                  |
| **DAX 8 gain+meter**                  | Meter/slider                                                                                                             | 0.5                                                                                                                                  |
| **TX gain+meter**                     | Meter/slider                                                                                                             | 0.5                                                                                                                                  |
| Indicator                             | Location                                                                                                                 | Possible values                                                                                                                      |
| ---                                   | ---                                                                                                                      | ---                                                                                                                                  |
| Slice-assignment status (per channel) | Shows which slice is currently routed to each DAX channel.                                                               | Slice letters render as rich text identifiers.                                                                                       |
| TX assignment status                  | Right of **TX:** label                                                                                                   | `—` or `Slice A`–`Slice H`                                                                                                           |
| DAX 5 gain+meter                      | Combined meter/slider; drag to set RX gain on DAX channel 5.                                                             | Visible only when the connected radio supports at least 5 slices.                                                                    |
| DAX 6 gain+meter                      | Combined meter/slider; drag to set RX gain on DAX channel 6.                                                             | Visible only when the connected radio supports at least 6 slices.                                                                    |
| DAX 7 gain+meter                      | Combined meter/slider; drag to set RX gain on DAX channel 7.                                                             | Visible only when the connected radio supports at least 7 slices.                                                                    |
| DAX 8 gain+meter                      | Combined meter/slider; drag to set RX gain on DAX channel 8.                                                             | Visible only on an 8-slice-capable radio.                                                                                            |
| Windows note                          | On Windows builds the applet shows only the note 'No built-in DAX driver on Windows. Use TCI, or SmartSDR DAX.' (#4112). | Windows has no built-in DAX bridge (no kernel-mode audio driver); all other controls are omitted and their setters are null-guarded. |

These indicators are read-only. They update automatically when a slice's DAX channel assignment changes. Slice-to-channel assignment is configured on the slice itself, not in this applet.

## Tips

- The indicators update in real time. If you change a slice's DAX channel assignment on the radio or in another part of the UI, the applet reflects the change immediately without requiring a manual refresh.
- A channel showing `—` means no slice is currently assigned to it; audio will not flow on that channel.
- Starting with v26.5.2.1, slice letters in the status indicators may use rich text formatting. This is an internal change; you do not need to adjust any settings to see the indicators correctly.
- The DAX Audio applet uses theme styling (class `applet/dax`). If you customize your application theme, the applet's appearance may vary to match the rest of the UI.
- Accessibility labels have been added: the DAX Enable button is labeled "DAX enable" with description "Enable or disable DAX digital audio routing", and the RX gain sliders are labeled "DAX RX 1 gain" through "DAX RX 4 gain" and the TX gain slider as "DAX TX gain" to improve compatibility with screen-reader software.

## Related

- [DAX Audio overview](overview.md)
- [Enable DAX to route slice audio to WSJT-X / FLDigi / other digital software](enable-dax-to-route-slice-audio-to-wsjt-x-fldigi-other-digital-software.md)
- [Identify which slice is the TX slice](identify-which-slice-is-the-tx-slice.md)
- [Set DAX RX gain per channel](set-dax-rx-gain-per-channel.md)