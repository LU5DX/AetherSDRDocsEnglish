# DAX Audio Applet (v26.7.4)

The DAX Audio applet provides a per-channel RX audio bridge and a single TX audio stream for digital mode operation. It displays live audio meters and gain sliders for DAX channels 1–4 and the TX stream, along with slice-assignment indicators.

> **Windows note:** AetherSDR does not ship a built-in DAX audio driver on Windows. On Windows, the applet displays an informational note only; all controls are inert. Use TCI or FlexRadio's SmartSDR DAX drivers instead. See Help → Configuring Data Modes for setup instructions.

## Enabling DAX Audio

1. Click the `DAX` tray button on the right sidebar to open the DAX Audio applet.
2. Click `Enable` to start the DAX audio bridge. The setting persists as `AutoStartDAX`.
3. Once enabled, all DAX RX and TX streams become active.
4. The button label updates to `Enabled` when the bridge is active and `Disabled` when inactive.

## Setting DAX RX gain per channel

Adjust the gain for each DAX receive channel (1–4) to control the audio level sent to connected software.

### Steps

1. In the DAX Audio applet, locate the row for the desired channel (`DAX 1` through `DAX 4`).
2. Drag the thumb on the combined meter/slider left or right to decrease or increase RX gain.
3. The value saves immediately and persists as `DaxRxGain1` through `DaxRxGain4`.

## Setting DAX TX gain

Adjust the DAX TX gain slider to control how much audio from your transmit slice is sent through the DAX TX stream to connected software.

### Steps

1. In the DAX Audio applet, locate the `TX:` row at the bottom.
2. Drag the thumb on the `TX gain+meter` slider left or right to decrease or increase TX gain.
3. The value saves immediately and persists as `DaxTxGain`.

## What each control does

| Control | Default | Range | Persisted key |
|---|---|---|---|
| `Enable` button | off | on/off | `AutoStartDAX` |
| `DAX 1 gain+meter` slider | 0.5 | 0.0 – 1.0 | `DaxRxGain1` |
| `DAX 2 gain+meter` slider | 0.5 | 0.0 – 1.0 | `DaxRxGain2` |
| `DAX 3 gain+meter` slider | 0.5 | 0.0 – 1.0 | `DaxRxGain3` |
| `DAX 4 gain+meter` slider | 0.5 | 0.0 – 1.0 | `DaxRxGain4` |
| `TX gain+meter` slider | 0.5 | 0.0 – 1.0 | `DaxTxGain` |

## Slice-assignment indicators

| Indicator | States | Meaning |
|---|---|---|
| `DAX 1..4 assignment` | — or Slice A–H | The slice currently assigned to this DAX channel |
| `TX assignment` | — or Slice A–H | The slice currently holding TX privileges (drives DAX TX) |

The slice letters in the assignment indicators render in rich text format, providing improved visual clarity when slice labels contain HTML entities (issue #2606).

## Accessibility

Each DAX RX gain slider and the TX gain slider has an accessible name. Screen readers announce `DAX RX 1 gain` through `DAX RX 4 gain` for the receive channel sliders, and `DAX TX gain` for the transmit gain slider. The DAX Enable button has an accessible name of `DAX enable` and an accessible description of `Enable or disable DAX digital audio routing`.

## Tips

- The meter bars reflect post-fader level: they show the actual output level after your gain setting is applied. Moving a slider gives immediate visual feedback even before you transmit.
- A gain of 0.5 is the default starting point. If your digital mode software reports overdriven or weak audio, adjust from there in small increments.
- On Linux, DAX RX latency has been reduced from approximately 400 ms to approximately 200 ms using a native PipeWire `pw_stream` source path, replacing the previous PulseAudio client.

## Related

- [DAX Audio overview](overview.md)
- [Enable DAX to route slice audio to WSJT-X / FLDigi / other digital software](enable-dax-to-route-slice-audio-to-wsjt-x-fldigi-other-digital-software.md)
- [Identify which slice is the TX slice](identify-which-slice-is-the-tx-slice.md)
- [Setting up digital modes (FT8, WSJT-X, fldigi)](../../operating/digital-modes/digital-modes-setup.md)