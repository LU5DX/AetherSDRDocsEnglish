# Enable DAX to route slice audio to WSJT-X / FLDigi / other digital software

DAX (Digital Audio eXchange) creates virtual audio streams between AetherSDR and other software running on the same machine. Enable it when you want WSJT-X, FLDigi, or any other digital mode program to receive audio from a radio slice or send audio back to the radio. The applet shows per-channel RX meters and gain sliders for DAX channels 1-8 plus a single TX meter.

## Before you start

- AetherSDR must be connected to your FLEX-8600 radio. DAX requires an active radio connection.
- Each slice you want to route must have a DAX channel assigned in the radio's slice settings. The DAX applet shows which slices are already assigned.
- On Linux, PipeWire must be running. On macOS, the system audio subsystem handles routing automatically.
- On Windows, AetherSDR does not include a built-in DAX audio driver. DAX audio on Windows requires FlexRadio's SmartSDR DAX drivers or TCI.
- The DAX applet shows only as many RX channel rows as the connected radio supports slices. A 6300 shows 2 channels; a 6600 shows 4; a 6700 shows all 8 (#4854).

## Steps

1. Click the **DAX** tray button on the right sidebar to open the DAX Audio applet. The applet is hidden by default.
2. On macOS and Linux, click **Enable** (labeled **Disabled** when off). The button changes to **Enabled** and turns green when DAX is active. AetherSDR saves this state as `AutoStartDAX`.
3. On Windows, the DAX applet shows a note "No built-in DAX driver on Windows. Use TCI, or SmartSDR DAX." The Enable button and all meters are not available. Proceed with your existing SmartSDR DAX drivers.
4. Check the slice-assignment indicators next to each DAX channel label (for example, **DAX 1:**, **DAX 2:**). Each indicator shows either `—` (no slice assigned) or `Slice A` through `Slice H`. Confirm the channel you want is showing the correct slice.
5. In your digital mode software (WSJT-X, FLDigi, etc.), select the corresponding DAX virtual audio device as the input (and output for TX) audio device. See [Setting up digital modes (FT8, WSJT-X, fldigi)](../../operating/digital-modes/digital-modes-setup.md) for per-application steps.
6. Transmit a test audio tone from your digital software and watch the **TX** meter in the applet. Adjust the **TX gain+meter** slider so the level stays below clipping.
7. Receive a signal and watch the **DAX 1–8 gain+meter** slider for the channel you assigned. Adjust the slider to set a comfortable level for your software's audio input.

## What each control does

| Control                    | Description                                                                                                                                            | Default                                                                                                                              |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Enable                     | Master toggle. Starts or stops all DAX audio streams. On macOS/Linux only. On Windows, the button is not available.                                    | Disabled                                                                                                                             |
| DAX 1 gain+meter           | Combined level meter and gain slider for DAX channel 1. Drag to adjust RX gain sent to software on that channel. Uses accessible name "DAX RX 1 gain". | 0.5                                                                                                                                  |
| DAX 2 gain+meter           | Same as DAX 1, for channel 2. Uses accessible name "DAX RX 2 gain".                                                                                    | 0.5                                                                                                                                  |
| DAX 3 gain+meter           | Same as DAX 1, for channel 3. Uses accessible name "DAX RX 3 gain".                                                                                    | 0.5                                                                                                                                  |
| DAX 4 gain+meter           | Same as DAX 1, for channel 4. Uses accessible name "DAX RX 4 gain".                                                                                    | 0.5                                                                                                                                  |
| DAX 5 gain+meter           | Same as DAX 1, for channel 5. Uses accessible name "DAX RX 5 gain". Visible only when the connected radio supports at least 5 slices.                  | 0.5                                                                                                                                  |
| DAX 6 gain+meter           | Same as DAX 1, for channel 6. Uses accessible name "DAX RX 6 gain". Visible only when the connected radio supports at least 6 slices.                  | 0.5                                                                                                                                  |
| DAX 7 gain+meter           | Same as DAX 1, for channel 7. Uses accessible name "DAX RX 7 gain". Visible only when the connected radio supports at least 7 slices.                  | 0.5                                                                                                                                  |
| DAX 8 gain+meter           | Same as DAX 1, for channel 8. Uses accessible name "DAX RX 8 gain". Visible only on an 8-slice-capable radio.                                         | 0.5                                                                                                                                  |
| TX gain+meter              | Combined level meter and gain slider for the DAX TX stream (audio from your digital software to the radio). Uses accessible name "DAX TX gain".        | 0.5                                                                                                                                  |
| Slice-assignment indicator (per channel) | Read-only. Shows which slice (A–H) is routed to each DAX channel, or `—` if none. Slice letters render in rich text for improved readability.          | `—`                                                                                                                                  |
| Windows note               | On Windows builds the applet shows only the note 'No built-in DAX driver on Windows. Use TCI, or SmartSDR DAX.' (#4112).                               | Windows has no built-in DAX bridge (no kernel-mode audio driver); all other controls are omitted and their setters are null-guarded. |

## Tips

- To start DAX automatically every time AetherSDR launches, check `Settings > Autostart DAX with AetherSDR` in the menu. This writes the same `AutoStartDAX` setting that the **Enable** button controls.
- The TX indicator next to the **TX** label shows which slice currently holds TX privileges. If it shows `—`, no slice is set as the TX slice, and DAX TX audio will not reach the radio. Slice letters render in rich text for improved readability.
- The gain sliders are post-fader: the meter bar reflects the level after your gain adjustment, so what you see is what the receiving application gets.
- RX meter levels are exponentially smoothed with fast attack and slow decay, so peaks are visible but needle jitter is reduced.
- Rows above the connected radio's slice capacity are hidden, so a small radio does not show dead gain sliders.
- On Linux (v26.6.1+), DAX RX latency is approximately 200 ms, reduced from approximately 400 ms in earlier versions, through native PipeWire streaming.
- On Windows, see `Help > Configuring Data Modes` for details on setting up audio routing with external DAX drivers.

## Troubleshooting

- **DAX channels show `—` and no audio passes** — No slice has a DAX channel assigned. Assign a DAX channel to the slice using the slice controls on the panadapter, then confirm the indicator in the applet updates to `Slice A` (or the appropriate letter).
- **Enable button does not stay checked after restarting AetherSDR** — `AutoStartDAX` was not saved. Enable the setting through `Settings > Autostart DAX with AetherSDR` so it is applied at launch.
- **Digital software receives no audio despite DAX being enabled** — Confirm the correct DAX virtual device is selected as the audio input in your digital mode software. The device name depends on your operating system and audio subsystem. On Windows, ensure SmartSDR DAX drivers are installed.
- **TX meter is active but the radio is not transmitting** — Confirm the TX slice indicator shows a valid slice. If it shows `—`, no slice holds TX privileges. See [Identify which slice is the TX slice](identify-which-slice-is-the-tx-slice.md).
- **DAX Enable button and meters are not visible on Windows** — This is expected behavior. AetherSDR does not include built-in DAX audio drivers for Windows. Use FlexRadio's SmartSDR DAX drivers or TCI for DAX audio on Windows. See `Help > Configuring Data Modes`.
- **Fewer DAX rows appear than expected** — The applet hides rows above the connected radio's slice capacity. A 6300 shows 2 channels, a 6600 shows 4, and a 6700 shows all 8.

## Related

- [DAX Audio overview](overview.md)
- [Autostart DAX on launch](autostart-dax-on-launch.md)
- [Set DAX RX gain per channel](set-dax-rx-gain-per-channel.md)
- [Set DAX TX gain](set-dax-tx-gain.md)
- [See which slice is currently using each DAX channel](see-which-slice-is-currently-using-each-dax-channel.md)
- [Identify which slice is the TX slice](identify-which-slice-is-the-tx-slice.md)
- [Setting up digital modes (FT8, WSJT-X, fldigi)](../../operating/digital-modes/digital-modes-setup.md)