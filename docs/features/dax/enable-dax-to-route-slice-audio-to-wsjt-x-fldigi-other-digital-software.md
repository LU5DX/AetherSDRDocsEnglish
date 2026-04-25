# Enable DAX to route slice audio to WSJT-X / FLDigi / other digital software

DAX (Digital Audio eXchange) creates audio streams between AetherSDR and other applications on your computer. Enable it so that software such as WSJT-X or FLDigi can receive audio from a radio slice and transmit audio back through it.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. DAX requires an active radio connection.
- At least one slice must exist and be assigned to a DAX channel in the radio's configuration before audio will flow.
- Your digital mode software must be configured to use the DAX virtual audio device. See [Setting up digital modes (FT8, WSJT-X, fldigi)](../../operating/digital-modes/digital-modes-setup.md) for that side of the setup.

## Steps

1. Click the `DAX` tray button on the right sidebar to open the DAX Audio applet. The applet is hidden by default.
2. Click `Enable`. The button turns green when DAX is active. AetherSDR saves this state as `AutoStartDAX`.
3. Check the slice-assignment indicator next to each DAX channel (for example, `Slice A`). A dash (`—`) means no slice is routed to that channel. Assign a slice to a DAX channel from within the radio's slice settings if needed.
4. Drag the gain+meter slider for the DAX channel your digital software will use to set the RX audio level. The default is `0.5` (mid-scale). Adjust until the level meter shows signal without clipping.
5. If your digital software will transmit through DAX, drag the `TX` gain+meter slider to set the transmit audio level. The default is also `0.5`.
6. In your digital mode software (WSJT-X, FLDigi, etc.), select the DAX virtual audio device as the input (RX) and output (TX) sound card.

## What each control does

| Control | What it does | Default | Range | Setting key |
|---|---|---|---|---|
| `Enable` | Starts the DAX audio bridge. All RX and TX streams depend on this being active. | Off | On / Off | `AutoStartDAX` |
| `DAX 1` gain+meter | Sets RX audio gain for DAX channel 1. Drag to adjust; meter shows live level. | 0.5 | 0.0 – 1.0 | `DaxRxGain1` |
| `DAX 2` gain+meter | Sets RX audio gain for DAX channel 2. | 0.5 | 0.0 – 1.0 | `DaxRxGain2` |
| `DAX 3` gain+meter | Sets RX audio gain for DAX channel 3. | 0.5 | 0.0 – 1.0 | `DaxRxGain3` |
| `DAX 4` gain+meter | Sets RX audio gain for DAX channel 4. | 0.5 | 0.0 – 1.0 | `DaxRxGain4` |
| `TX` gain+meter | Sets the transmit audio level for the DAX TX stream. | 0.5 | 0.0 – 1.0 | `DaxTxGain` |
| Slice-assignment indicator (per channel) | Shows which slice is routed to this DAX channel (`—` if none, or `Slice A` through `Slice H`). | `—` | — | — |

## Tips

- To have DAX start automatically every time AetherSDR launches, enable `Settings > Autostart DAX with AetherSDR` instead of clicking `Enable` each session.
- The level meter in each gain+meter widget shows post-fader level — it reflects the actual output level after the gain slider is applied. Use it to judge whether your digital software is receiving adequate signal.
- The `TX` indicator shows which slice currently holds TX privileges. If it reads `—`, no slice is designated as the TX slice and DAX TX audio will not be routed.

## Troubleshooting

- **`Enable` button is present but the DAX applet shows no meter activity** — Confirm a slice is assigned to the DAX channel you are using. The slice-assignment indicator must show a slice letter, not `—`.
- **Digital software receives no audio** — Verify that the DAX virtual audio device is selected as the input device in your digital software. DAX must be enabled in AetherSDR before the virtual device becomes active.
- **TX audio is not reaching the radio** — Check that the `TX` indicator shows a slice letter. If it reads `—`, no TX slice is assigned. Also confirm your digital software is using the DAX virtual audio device as its output.

## Related

- [DAX Audio overview](overview.md)
- [Autostart DAX on launch](autostart-dax-on-launch.md)
- [Set DAX RX gain per channel](set-dax-rx-gain-per-channel.md)
- [Set DAX TX gain](set-dax-tx-gain.md)
- [See which slice is currently using each DAX channel](see-which-slice-is-currently-using-each-dax-channel.md)
- [Identify which slice is the TX slice](identify-which-slice-is-the-tx-slice.md)
- [Setting up digital modes (FT8, WSJT-X, fldigi)](../../operating/digital-modes/digital-modes-setup.md)
