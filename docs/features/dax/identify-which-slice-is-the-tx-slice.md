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

| Control                    | Description                                                                                                                                                                  | Default                                                                                                                              |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| DAX Enable                 | Starts the DAX audio bridge; emits daxToggled.                                                                                                                               | Button label is 'Enable'/'Disabled'; master switch for all DAX RX and TX streams. Not built on Windows (#4112).                      |
| DAX 1 gain+meter           | Combined meter and slider for RX gain on DAX channel 1. Drag to adjust gain.                                                                                                 | 0.5                                                                                                                                  |
| DAX 2 gain+meter           | Combined meter and slider for RX gain on DAX channel 2. Drag to adjust gain.                                                                                                 | 0.5                                                                                                                                  |
| DAX 3 gain+meter           | Combined meter and slider for RX gain on DAX channel 3. Drag to adjust gain.                                                                                                 | 0.5                                                                                                                                  |
| DAX 4 gain+meter           | Combined meter and slider for RX gain on DAX channel 4. Drag to adjust gain.                                                                                                 | 0.5                                                                                                                                  |
| DAX 5 gain+meter           | Combined meter and slider for RX gain on DAX channel 5. Drag to adjust gain.                                                                                                 | 0.5                                                                                                                                  |
| DAX 6 gain+meter           | Combined meter and slider for RX gain on DAX channel 6. Drag to adjust gain.                                                                                                 | 0.5                                                                                                                                  |
| DAX 7 gain+meter           | Combined meter and slider for RX gain on DAX channel 7. Drag to adjust gain.                                                                                                 | 0.5                                                                                                                                  |
| DAX 8 gain+meter           | Combined meter and slider for RX gain on DAX channel 8. Drag to adjust gain.                                                                                                 | 0.5                                                                                                                                  |
| TX gain+meter              | Combined meter and slider for the DAX TX stream. Drag to adjust gain.                                                                                                        | 0.5                                                                                                                                  |
| DAX 1 assignment indicator | Shows which slice (if any) is currently routed to DAX channel 1.                                                                                                             | `—`                                                                                                                                  |
| DAX 2 assignment indicator | Shows which slice (if any) is currently routed to DAX channel 2.                                                                                                             | `—`                                                                                                                                  |
| DAX 3 assignment indicator | Shows which slice (if any) is currently routed to DAX channel 3.                                                                                                             | `—`                                                                                                                                  |
| DAX 4 assignment indicator | Shows which slice (if any) is currently routed to DAX channel 4.                                                                                                             | `—`                                                                                                                                  |
| DAX 5 assignment indicator | Shows which slice (if any) is currently routed to DAX channel 5.                                                                                                             | `—`                                                                                                                                  |
| DAX 6 assignment indicator | Shows which slice (if any) is currently routed to DAX channel 6.                                                                                                             | `—`                                                                                                                                  |
| DAX 7 assignment indicator | Shows which slice (if any) is currently routed to DAX channel 7.                                                                                                             | `—`                                                                                                                                  |
| DAX 8 assignment indicator | Shows which slice (if any) is currently routed to DAX channel 8.                                                                                                             | `—`                                                                                                                                  |
| TX assignment indicator    | Shows which slice currently has TX privileges. Updates automatically when TX is moved between slices. Slice letter is displayed in a colored box matching the slice's color. | `—`                                                                                                                                  |
| Windows note               | On Windows builds the applet shows only the note 'No built-in DAX driver on Windows. Use TCI, or SmartSDR DAX.' (#4112).                                                     | Windows has no built-in DAX bridge (no kernel-mode audio driver); all other controls are omitted and their setters are null-guarded. |

## Tips

- The TX indicator updates in real time. If you transfer TX to another slice on the radio, the indicator changes immediately without any manual refresh.
- The RX rows above the TX row show per-channel DAX assignments (`DAX 1:` through `DAX 8:`). These indicate which slice is routed to each DAX RX channel and are separate from the TX assignment.
- The slice letter in the TX indicator is rendered as rich text, allowing the colored box display when the radio is connected.
- On Linux with PipeWire, a native `pw_stream` source path replaces the previous PulseAudio client, reducing DAX RX latency from approximately 400 ms to approximately 200 ms.
- Each gain slider and meter has an accessible name for screen reader support: `DAX RX 1 gain` through `DAX RX 8 gain` for the receive channels, and `DAX TX gain` for the transmit channel.
- On Windows, the DAX Applet shows only a notice that no built-in DAX driver is shipped with AetherSDR. The enable button, gain sliders, and meters are not displayed. Use TCI or SmartSDR DAX instead. See **Help > Configuring Data Modes** for setup instructions.
- RX rows above the connected radio's slice capacity are hidden, so a radio with fewer slices (for example, a 2-slice FLEX-6300 or 4-slice FLEX-6600) does not show dead gain sliders that would route nowhere. The channel allocation is always 8 internally; the rows are merely hidden to match the radio's capabilities.

## Related

- [See which slice is currently using each DAX channel](see-which-slice-is-currently-using-each-dax-channel.md)
- [Enable DAX to route slice audio to WSJT-X / FLDigi / other digital software](enable-dax-to-route-slice-audio-to-wsjt-x-fldigi-other-digital-software.md)
- [DAX Audio overview](overview.md)