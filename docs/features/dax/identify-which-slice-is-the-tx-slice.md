# Identify which slice is the TX slice

The DAX Applet shows a live TX assignment indicator that tells you which slice currently holds TX privileges. Use this when you need to confirm the transmit slice before operating digital modes or checking DAX TX audio routing.

## Before you start

- AetherSDR must be connected to the radio. The TX assignment indicator requires an active radio connection.
- The DAX Applet must be visible. It is hidden by default.

## Steps

1. Click the **DAX** tray button on the right sidebar to open the DAX Applet.
2. Look at the **TX:** row at the bottom of the applet.
3. Read the status indicator to the right of the **TX:** label. It shows either `—` (no TX slice assigned) or a slice letter `A` through `H` (the slice currently holding TX privileges). The slice letter is rendered in a colored box matching the slice's color.

## What each control does

| Control | Description | Default | Valid states | Setting key |
|---|---|---|---|---|
| DAX Enable | Toggle button that starts the DAX audio bridge. Master switch for all DAX RX and TX streams. Button label toggles between "Enabled" and "Disabled". | off | on/off | `AutoStartDAX` |
| DAX 1 gain+meter | Combined meter and slider for RX gain on DAX channel 1. Drag to adjust gain. | 0.5 | 0.0–1.0 | `DaxRxGain1` |
| DAX 2 gain+meter | Combined meter and slider for RX gain on DAX channel 2. Drag to adjust gain. | 0.5 | 0.0–1.0 | `DaxRxGain2` |
| DAX 3 gain+meter | Combined meter and slider for RX gain on DAX channel 3. Drag to adjust gain. | 0.5 | 0.0–1.0 | `DaxRxGain3` |
| DAX 4 gain+meter | Combined meter and slider for RX gain on DAX channel 4. Drag to adjust gain. | 0.5 | 0.0–1.0 | `DaxRxGain4` |
| TX gain+meter | Combined meter and slider for the DAX TX stream. Drag to adjust gain. | 0.5 | 0.0–1.0 | `DaxTxGain` |
| DAX 1 assignment indicator | Shows which slice (if any) is currently routed to DAX channel 1. | `—` | `—` or `Slice A`–`Slice H` | none |
| DAX 2 assignment indicator | Shows which slice (if any) is currently routed to DAX channel 2. | `—` | `—` or `Slice A`–`Slice H` | none |
| DAX 3 assignment indicator | Shows which slice (if any) is currently routed to DAX channel 3. | `—` | `—` or `Slice A`–`Slice H` | none |
| DAX 4 assignment indicator | Shows which slice (if any) is currently routed to DAX channel 4. | `—` | `—` or `Slice A`–`Slice H` | none |
| TX assignment indicator | Shows which slice currently has TX privileges. Updates automatically when TX is moved between slices. Slice letter is displayed in a colored box matching the slice's color. | `—` | `—` or colored slice letter `A`–`H` | none |

## Tips

- The TX indicator updates in real time. If you transfer TX to another slice on the radio, the indicator changes immediately without any manual refresh.
- The RX rows above the TX row show per-channel DAX assignments (`DAX 1:` through `DAX 4:`). These indicate which slice is routed to each DAX RX channel and are separate from the TX assignment.
- The slice letter in the TX indicator is rendered as rich text, allowing the colored box display when the radio is connected.
- On Linux with PipeWire, a native `pw_stream` source path replaces the previous PulseAudio client, reducing DAX RX latency from approximately 400 ms to approximately 200 ms.
- Each gain slider and meter has an accessible name for screen reader support: `DAX RX 1 gain` through `DAX RX 4 gain` for the receive channels, and `DAX TX gain` for the transmit channel.
- On Windows, the DAX Applet shows only a notice that no built-in DAX driver is shipped with AetherSDR. The enable button, gain sliders, and meters are not displayed. Use TCI or SmartSDR DAX instead. See **Help > Configuring Data Modes** for setup instructions.

## Related

- [See which slice is currently using each DAX channel](see-which-slice-is-currently-using-each-dax-channel.md)
- [Enable DAX to route slice audio to WSJT-X / FLDigi / other digital software](enable-dax-to-route-slice-audio-to-wsjt-x-fldigi-other-digital-software.md)
- [DAX Audio overview](overview.md)