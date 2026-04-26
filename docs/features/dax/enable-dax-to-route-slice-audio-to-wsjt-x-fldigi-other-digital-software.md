# Enable DAX to Route Slice Audio to WSJT-X / FLDigi / Other Digital Software

DAX (Digital Audio eXchange) creates audio bridges between AetherSDR and other software running on your computer. Enabling it lets programs like WSJT-X and fldigi receive slice audio and transmit audio back through the radio.

## Before you start

- AetherSDR must be connected to the radio. DAX requires an active radio connection.
- Your digital software (WSJT-X, fldigi, etc.) must be configured to use the DAX audio devices. See [Setting up digital modes (FT8, WSJT-X, fldigi)](../../operating/digital-modes/digital-modes-setup.md) for that side of the configuration.
- Identify which slice you want to route. Each DAX channel carries audio from one slice.

## Steps

1. Click the `DAX` tray button on the right sidebar to open the DAX Audio applet. If the applet panel is not visible, enable it with `View > Applet Panel`.
2. Click `Enable` to start the DAX audio bridge. The button turns green when active. This persists as `AutoStartDAX`.
3. Check the slice-assignment indicator next to each DAX channel (labeled `DAX 1:` through `DAX 4:`). A value of `—` means no slice is routed to that channel. A value such as `Slice A` means that slice's audio is flowing through the channel.
4. In your radio's slice controls, assign the desired slice to the DAX channel your digital software is listening on. The indicator updates automatically when the assignment takes effect.
5. In your digital software, select the corresponding DAX RX audio device as the input and the DAX TX audio device as the output.
6. Drag the gain+meter slider for the relevant DAX channel (for example, `DAX 1:`) to adjust the RX audio level delivered to your software. The default is `0.5`. Valid range is `0.0`–`1.0`, persisted as `DaxRxGain1` through `DaxRxGain4`.
7. If your digital software transmits audio, drag the `TX:` gain+meter slider to adjust the transmit level. The default is `0.5`. Valid range is `0.0`–`1.0`, persisted as `DaxTxGain`.

## What each control does

| Control | What it does | Default | Range | Setting key |
|---|---|---|---|---|
| `Enable` | Starts or stops the DAX audio bridge. Master switch for all RX and TX streams. | Off | On / Off | `AutoStartDAX` |
| `DAX 1:` gain+meter | Sets RX audio gain for DAX channel 1 and shows the live level. | 0.5 | 0.0–1.0 | `DaxRxGain1` |
| `DAX 2:` gain+meter | Sets RX audio gain for DAX channel 2 and shows the live level. | 0.5 | 0.0–1.0 | `DaxRxGain2` |
| `DAX 3:` gain+meter | Sets RX audio gain for DAX channel 3 and shows the live level. | 0.5 | 0.0–1.0 | `DaxRxGain3` |
| `DAX 4:` gain+meter | Sets RX audio gain for DAX channel 4 and shows the live level. | 0.5 | 0.0–1.0 | `DaxRxGain4` |
| `TX:` gain+meter | Sets the TX audio gain for the DAX transmit stream and shows the live level. | 0.5 | 0.0–1.0 | `DaxTxGain` |
| Slice-assignment indicator (per channel) | Shows which slice is currently routed to each DAX channel (`—` or `Slice A`–`Slice H`). Read-only. | `—` | — | — |

## Tips

- To have DAX start automatically every time AetherSDR launches, check `Settings > Autostart DAX with AetherSDR`. This sets `AutoStartDAX` without requiring you to open the applet each session.
- The level meter behind each slider shows post-fader level — the bar reflects the actual output level after the gain is applied, so what you see is what your digital software receives.
- The `TX:` indicator shows which slice currently holds TX privileges. If it shows `—`, no slice is set as the TX slice and transmit audio will not flow.

## Troubleshooting

- **`Enable` button is unresponsive or grayed out** — DAX requires an active radio connection. Confirm AetherSDR is connected to the FLEX-8600 before enabling DAX.
- **Slice-assignment indicator shows `—` after enabling DAX** — The slice has not been assigned to a DAX channel in the radio's slice settings. Assign the slice to a DAX channel from the slice controls.
- **Digital software receives no audio despite DAX being enabled** — Confirm the digital software's audio input device is set to the correct DAX RX channel matching the channel shown in the applet. Also check that the RX gain slider is above `0.0`.
- **TX audio is not being transmitted** — Check that the `TX:` indicator shows the expected slice rather than `—`. If it shows `—`, no slice holds TX privileges; see [Identify which slice is the TX slice](identify-which-slice-is-the-tx-slice.md).

## Related

- [DAX Audio overview](overview.md)
- [Autostart DAX on launch](autostart-dax-on-launch.md)
- [Set DAX RX gain per channel](set-dax-rx-gain-per-channel.md)
- [Set DAX TX gain](set-dax-tx-gain.md)
- [See which slice is currently using each DAX channel](see-which-slice-is-currently-using-each-dax-channel.md)
- [Identify which slice is the TX slice](identify-which-slice-is-the-tx-slice.md)
- [Setting up digital modes (FT8, WSJT-X, fldigi)](../../operating/digital-modes/digital-modes-setup.md)
