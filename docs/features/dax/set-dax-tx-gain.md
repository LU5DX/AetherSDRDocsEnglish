# DAX Audio Applet (v26.8.4)

The DAX Audio applet provides a per-channel RX audio bridge and a single TX audio stream for digital mode operation. It displays live audio meters and gain sliders for DAX channels 1–8 and the TX stream, along with slice-assignment indicators.

> **Windows note:** AetherSDR does not ship a built-in DAX audio driver on Windows. On Windows, the applet displays an informational note only; all controls are inert. Use TCI or FlexRadio's SmartSDR DAX drivers instead. See Help → Configuring Data Modes for setup instructions.

## Enabling DAX Audio

1. Click the `DAX` tray button on the right sidebar to open the DAX Audio applet.
2. Click `Enable` to start the DAX audio bridge. The setting persists as `AutoStartDAX`.
3. Once enabled, all DAX RX and TX streams become active.
4. The button label updates to `Enabled` when the bridge is active and `Disabled` when inactive.

## Setting DAX RX gain per channel

Adjust the gain for each DAX receive channel (1–8) to control the audio level sent to connected software. Rows for channels above your radio's slice capacity are hidden automatically.

### Steps

1. In the DAX Audio applet, locate the row for the desired channel (`DAX 1` through `DAX 8`).
2. Drag the thumb on the combined meter/slider left or right to decrease or increase RX gain.
3. The value saves immediately and persists as `DaxRxGain1` through `DaxRxGain8`.

## Setting DAX TX gain

Adjust the DAX TX gain slider to control how much audio from your transmit slice is sent through the DAX TX stream to connected software.

### Steps

1. In the DAX Audio applet, locate the `TX:` row at the bottom.
2. Drag the thumb on the `TX gain+meter` slider left or right to decrease or increase TX gain.
3. The value saves immediately and persists as `DaxTxGain`.

## What each control does

| Control                   | Default | Range |
|---------------------------|---------|-------|
| `Enable` button           | off     | on/off|
| `DAX 1 gain+meter` slider | 0.5     | 0.0 – 1.0 |
| `DAX 2 gain+meter` slider | 0.5     | 0.0 – 1.0 |
| `DAX 3 gain+meter` slider | 0.5     | 0.0 – 1.0 |
| `DAX 4 gain+meter` slider | 0.5     | 0.0 – 1.0 |
| `DAX 5 gain+meter` slider | 0.5     | 0.0 – 1.0 |
| `DAX 6 gain+meter` slider | 0.5     | 0.0 – 1.0 |
| `DAX 7 gain+meter` slider | 0.5     | 0.0 – 1.0 |
| `DAX 8 gain+meter` slider | 0.5     | 0.0 – 1.0 |
| `TX gain+meter` slider    | 0.5     | 0.0 – 1.0 |
| `DAX 5 gain+meter`        | Combined meter/slider; drag to set RX gain on DAX channel 5. | Visible only when the connected radio supports at least 5 slices. |
| `DAX 6 gain+meter`        | Combined meter/slider; drag to set RX gain on DAX channel 6. | Visible only when the connected radio supports at least 6 slices. |
| `DAX 7 gain+meter`        | Combined meter/slider; drag to set RX gain on DAX channel 7. | Visible only when the connected radio supports at least 7 slices. |
| `DAX 8 gain+meter`        | Combined meter/slider; drag to set RX gain on DAX channel 8. | Visible only on an 8-slice-capable radio. |
| Windows note              | On Windows builds the applet shows only the note `No built-in DAX driver on Windows. Use TCI, or SmartSDR DAX.` (#4112). | Windows has no built-in DAX bridge (no kernel-mode audio driver); all other controls are omitted and their setters are null-guarded. |

Rows for DAX channels above the connected radio's slice capacity are hidden automatically, so a small radio doesn't show dead gain sliders. For example, a 2-slice radio (like the FLEX-6300) shows only DAX 1–2, while an 8-slice radio (FLEX-6700) shows all eight channels.

## Slice-assignment indicators

| Indicator | States | Meaning |
|---|---|---|
| `DAX 1..8 assignment` | — or Slice A–H | The slice currently assigned to this DAX channel |
| `TX assignment` | — or Slice A–H | The slice currently holding TX privileges (drives DAX TX) |

The slice letters in the assignment indicators render in rich text format, providing improved visual clarity when slice labels contain HTML entities (issue #2606).

## Accessibility

Each DAX RX gain slider and the TX gain slider has an accessible name. Screen readers announce `DAX RX 1 gain` through `DAX RX 8 gain` for the receive channel sliders, and `DAX TX gain` for the transmit gain slider. The DAX Enable button has an accessible name of `DAX enable` and an accessible description of `Enable or disable DAX digital audio routing`.

## Tips

- The meter bars reflect post-fader level: they show the actual output level after your gain setting is applied. Moving a slider gives immediate visual feedback even before you transmit.
- RX meter levels are exponentially smoothed (fast attack, slow decay) to give responsive yet stable readings.
- A gain of 0.5 is the default starting point. If your digital mode software reports overdriven or weak audio, adjust from there in small increments.
- On Linux, DAX RX latency has been reduced from approximately 400 ms to approximately 200 ms using a native PipeWire `pw_stream` source path, replacing the previous PulseAudio client.

## Related

- [DAX Audio overview](overview.md)
- [Enable DAX to route slice audio to WSJT-X / FLDigi / other digital software](enable-dax-to-route-slice-audio-to-wsjt-x-fldigi-other-digital-software.md)
- [Identify which slice is the TX slice](identify-which-slice-is-the-tx-slice.md)
- [Setting up digital modes (FT8, WSJT-X, fldigi)](../../operating/digital-modes/digital-modes-setup.md)