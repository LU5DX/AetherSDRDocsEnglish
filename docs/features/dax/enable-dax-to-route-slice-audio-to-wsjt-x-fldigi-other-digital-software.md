# Enable DAX to Route Slice Audio to WSJT-X / FLDigi / Other Digital Software

DAX (Digital Audio eXchange) bridges audio between the FLEX-8600 and other software running on your computer. Enabling it creates virtual audio channels that programs like WSJT-X, FLDigi, and similar digital mode applications can use as their sound device.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. DAX requires an active radio connection.
- The applet panel must be visible. If it is not, click `View > Applet Panel` to show it.
- In your digital mode software, have the audio device settings open so you can select the DAX channel once it is active.

## Steps

1. Click the **DAX** tray button on the right sidebar to open the DAX Audio applet.
2. Click **Enable** to start the DAX audio bridge. The button turns green when active, and the setting is saved as `AutoStartDAX`.
3. In your radio, assign a slice to a DAX channel. The slice-assignment indicator next to each channel row updates to show the assigned slice (for example, `Slice A`). A `—` means no slice is assigned to that channel.
4. In your digital mode software, select the DAX RX channel that matches the assigned channel as your audio input device (for example, DAX IQ 1 or DAX Audio 1, depending on your OS and driver).
5. If your digital mode software transmits audio, select the corresponding DAX TX channel as your audio output device.
6. Drag the gain slider on the channel row to adjust the RX level for that channel. The default is `0.5` (mid-range). The meter behind the slider shows the live signal level.
7. If transmitting via DAX, drag the **TX** gain slider to set the transmit audio level. The default is also `0.5`.

## What each control does

| Control | Default | Valid range | Persisted setting | Behavior |
|---|---|---|---|---|
| Enable | Off | On / Off | `AutoStartDAX` | Master switch. Starts the DAX audio bridge for all RX and TX streams. |
| DAX 1 gain+meter | 0.5 | 0.0 – 1.0 | `DaxRxGain1` | Drag to set RX gain on DAX channel 1. Meter shows live level post-fader. |
| DAX 2 gain+meter | 0.5 | 0.0 – 1.0 | `DaxRxGain2` | Drag to set RX gain on DAX channel 2. |
| DAX 3 gain+meter | 0.5 | 0.0 – 1.0 | `DaxRxGain3` | Drag to set RX gain on DAX channel 3. |
| DAX 4 gain+meter | 0.5 | 0.0 – 1.0 | `DaxRxGain4` | Drag to set RX gain on DAX channel 4. |
| TX gain+meter | 0.5 | 0.0 – 1.0 | `DaxTxGain` | Drag to set TX stream gain. Meter shows live transmit level post-fader. |
| Slice-assignment indicator | — | `—` or `Slice A`–`Slice H` | _(none)_ | Shows which slice is routed to each DAX channel. Read-only. |

## Tips

- To have DAX start automatically every time AetherSDR launches, enable `Settings > Autostart DAX with AetherSDR` instead of clicking **Enable** manually each session.
- The TX status indicator shows which slice currently holds TX privileges. Only that slice drives the DAX TX stream.
- If a channel's meter is active but your digital software receives no audio, confirm the slice-assignment indicator shows a slice name rather than `—`.

## Troubleshooting

- **Enable button is present but does nothing visible** — DAX requires an active radio connection. Confirm AetherSDR is connected to the radio before clicking **Enable**.
- **Slice-assignment indicator shows `—` for all channels** — No slice has been assigned to a DAX channel in the radio. Use the radio's slice controls to assign a DAX channel number to the slice you want to decode.
- **Digital software receives no audio despite a slice being assigned** — Check that your software's audio input device matches the correct DAX channel number shown in the applet. Also confirm the RX gain slider is above `0.0`.

## Related

- [DAX Audio overview](overview.md)
- [Autostart DAX on launch](autostart-dax-on-launch.md)
- [Set DAX RX gain per channel](set-dax-rx-gain-per-channel.md)
- [Set DAX TX gain](set-dax-tx-gain.md)
- [See which slice is currently using each DAX channel](see-which-slice-is-currently-using-each-dax-channel.md)
- [Identify which slice is the TX slice](identify-which-slice-is-the-tx-slice.md)
- [Setting up digital modes (FT8, WSJT-X, fldigi)](../../operating/digital-modes/digital-modes-setup.md)
