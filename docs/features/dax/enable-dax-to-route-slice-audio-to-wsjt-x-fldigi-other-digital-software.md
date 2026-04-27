# Enable DAX to route slice audio to WSJT-X / FLDigi / other digital software

DAX (Digital Audio eXchange) creates virtual audio streams between AetherSDR and other software running on the same machine. Enable it when you want WSJT-X, FLDigi, or any other digital mode program to receive audio from a radio slice or send audio back to the radio.

## Before you start

- AetherSDR must be connected to your FLEX-8600 radio. DAX requires an active radio connection.
- Each slice you want to route must have a DAX channel assigned in the radio's slice settings. The DAX applet shows which slices are already assigned.
- On Linux, PipeWire must be running. On macOS, the system audio subsystem handles routing automatically.

## Steps

1. Click the **DAX** tray button on the right sidebar to open the DAX Audio applet. The applet is hidden by default.
2. Click **Enable**. The button turns green when DAX is active. AetherSDR saves this state as `AutoStartDAX`.
3. Check the slice-assignment indicators next to each DAX channel label (for example, **DAX 1:**, **DAX 2:**). Each indicator shows either `—` (no slice assigned) or `Slice A` through `Slice H`. Confirm the channel you want is showing the correct slice.
4. In your digital mode software (WSJT-X, FLDigi, etc.), select the corresponding DAX virtual audio device as the input (and output for TX) audio device. See [Setting up digital modes (FT8, WSJT-X, fldigi)](../../operating/digital-modes/digital-modes-setup.md) for per-application steps.
5. Transmit a test audio tone from your digital software and watch the **TX** meter in the applet. Adjust the **TX gain+meter** slider so the level stays below clipping.
6. Receive a signal and watch the **DAX 1–4 gain+meter** slider for the channel you assigned. Adjust the slider to set a comfortable level for your software's audio input.

## What each control does

| Control | Description | Default | Range | Setting key |
|---|---|---|---|---|
| Enable | Master toggle. Starts or stops all DAX audio streams. | Off | On / Off | `AutoStartDAX` |
| DAX 1 gain+meter | Combined level meter and gain slider for DAX channel 1. Drag to adjust RX gain sent to software on that channel. | 0.5 | 0.0–1.0 | `DaxRxGain1` |
| DAX 2 gain+meter | Same as DAX 1, for channel 2. | 0.5 | 0.0–1.0 | `DaxRxGain2` |
| DAX 3 gain+meter | Same as DAX 1, for channel 3. | 0.5 | 0.0–1.0 | `DaxRxGain3` |
| DAX 4 gain+meter | Same as DAX 1, for channel 4. | 0.5 | 0.0–1.0 | `DaxRxGain4` |
| TX gain+meter | Combined level meter and gain slider for the DAX TX stream (audio from your digital software to the radio). | 0.5 | 0.0–1.0 | `DaxTxGain` |
| Slice-assignment indicator | Read-only. Shows which slice (A–H) is routed to each DAX channel, or `—` if none. | `—` | `—` or `Slice A`–`Slice H` | — |

## Tips

- To start DAX automatically every time AetherSDR launches, check `Settings > Autostart DAX with AetherSDR` in the menu. This writes the same `AutoStartDAX` setting that the **Enable** button controls.
- The TX indicator next to the **TX** label shows which slice currently holds TX privileges. If it shows `—`, no slice is set as the TX slice, and DAX TX audio will not reach the radio.
- The gain sliders are post-fader: the meter bar reflects the level after your gain adjustment, so what you see is what the receiving application gets.

## Troubleshooting

- **DAX channels show `—` and no audio passes** — No slice has a DAX channel assigned. Assign a DAX channel to the slice using the slice controls on the panadapter, then confirm the indicator in the applet updates to `Slice A` (or the appropriate letter).
- **Enable button does not stay checked after restarting AetherSDR** — `AutoStartDAX` was not saved. Enable the setting through `Settings > Autostart DAX with AetherSDR` so it is applied at launch.
- **Digital software receives no audio despite DAX being enabled** — Confirm the correct DAX virtual device is selected as the audio input in your digital mode software. The device name depends on your operating system and audio subsystem.
- **TX meter is active but the radio is not transmitting** — Confirm the TX slice indicator shows a valid slice. If it shows `—`, no slice holds TX privileges. See [Identify which slice is the TX slice](identify-which-slice-is-the-tx-slice.md).

## Related

- [DAX Audio overview](overview.md)
- [Autostart DAX on launch](autostart-dax-on-launch.md)
- [Set DAX RX gain per channel](set-dax-rx-gain-per-channel.md)
- [Set DAX TX gain](set-dax-tx-gain.md)
- [See which slice is currently using each DAX channel](see-which-slice-is-currently-using-each-dax-channel.md)
- [Identify which slice is the TX slice](identify-which-slice-is-the-tx-slice.md)
- [Setting up digital modes (FT8, WSJT-X, fldigi)](../../operating/digital-modes/digital-modes-setup.md)
