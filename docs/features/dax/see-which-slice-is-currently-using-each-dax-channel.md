# See which slice is using each DAX channel

The DAX Audio applet shows a slice-assignment indicator next to each DAX channel so you can confirm at a glance which slice is routed where without leaving the main window.

## Before you start

- AetherSDR must be connected to the radio. The slice-assignment indicators require a live radio connection.
- At least one slice must have a DAX channel assigned. If no slices are assigned, all indicators show `—`.
- AetherSDR v26.5.2.1 or later renders slice letters with rich text formatting for improved visibility.

## Steps

1. Click the **DAX** tray button on the right sidebar to open the DAX Audio applet.
2. Look at the status label to the right of each channel label (**DAX 1:**, **DAX 2:**, **DAX 3:**, **DAX 4:**).
3. Read the indicator for each channel. It shows either `—` (no slice assigned) or `Slice A` through `Slice H` (the letter of the slice currently routed to that channel). In v26.5.2.1, the slice letter may be displayed using rich text formatting for better legibility.
4. To see which slice is driving the DAX TX stream, read the status label on the **TX:** row. It follows the same format: `—` or `Slice A` through `Slice H`.

## What each control does

| Control | Kind | Default | Range | Setting key | Behavior |
|---|---|---|---|---|---|
| **DAX Enable** | Toggle button | Off | — | `AutoStartDAX` | Starts the DAX audio bridge; emits `daxToggled`. |
| **DAX 1 gain+meter** | Meter/slider | 0.5 | 0.0–1.0 | `DaxRxGain1` | Drag to set RX gain on DAX channel 1. |
| **DAX 2 gain+meter** | Meter/slider | 0.5 | 0.0–1.0 | `DaxRxGain2` | Drag to set RX gain on DAX channel 2. |
| **DAX 3 gain+meter** | Meter/slider | 0.5 | 0.0–1.0 | `DaxRxGain3` | Drag to set RX gain on DAX channel 3. |
| **DAX 4 gain+meter** | Meter/slider | 0.5 | 0.0–1.0 | `DaxRxGain4` | Drag to set RX gain on DAX channel 4. |
| **TX gain+meter** | Meter/slider | 0.5 | 0.0–1.0 | `DaxTxGain` | Drag to set TX gain on the DAX TX stream. |

| Indicator | Location | Possible values | Persisted setting |
|---|---|---|---|
| Slice-assignment status (per channel) | Right of **DAX 1:** – **DAX 4:** labels | `—` or `Slice A`–`Slice H` | None |
| TX assignment status | Right of **TX:** label | `—` or `Slice A`–`Slice H` | None |

These indicators are read-only. They update automatically when a slice's DAX channel assignment changes. Slice-to-channel assignment is configured on the slice itself, not in this applet.

## Tips

- The indicators update in real time. If you change a slice's DAX channel assignment on the radio or in another part of the UI, the applet reflects the change immediately without requiring a manual refresh.
- A channel showing `—` means no slice is currently assigned to it; audio will not flow on that channel.
- Starting with v26.5.2.1, slice letters in the status indicators may use rich text formatting. This is an internal change; you do not need to adjust any settings to see the indicators correctly.
- The DAX Audio applet uses theme styling (class `applet/dax`). If you customize your application theme, the applet's appearance may vary to match the rest of the UI.
- Accessibility labels have been added for the RX gain sliders (as "DAX RX 1 gain", "DAX RX 2 gain", "DAX RX 3 gain", "DAX RX 4 gain") and the TX gain slider (as "DAX TX gain") to improve compatibility with screen-reader software.

## Related

- [DAX Audio overview](overview.md)
- [Enable DAX to route slice audio to WSJT-X / FLDigi / other digital software](enable-dax-to-route-slice-audio-to-wsjt-x-fldigi-other-digital-software.md)
- [Identify which slice is the TX slice](identify-which-slice-is-the-tx-slice.md)
- [Set DAX RX gain per channel](set-dax-rx-gain-per-channel.md)