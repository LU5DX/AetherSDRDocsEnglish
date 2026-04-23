# DAX Audio overview

The DAX (Digital Audio eXchange) applet bridges audio between AetherSDR and other software on your computer — digital mode programs such as WSJT-X or fldigi, logging software, or any application that reads from or writes to a virtual audio device. It provides per-channel RX gain control for four independent receive streams plus a single TX stream, with live level metering on each.

## Before you start

- AetherSDR must be connected to a Flex radio. The DAX applet requires an active radio connection.
- The DAX applet is hidden by default. Click the **DAX** tray button on the right sidebar to show it.

## How it works

When you click **Enable**, AetherSDR starts the DAX audio bridge. The radio streams audio for each assigned slice over the bridge; your operating software connects to the resulting virtual audio devices to receive or send audio.

There are four independent RX channels (DAX 1–4). Each channel carries audio from whichever slice is assigned to it. The slice assignment is made on the radio or slice, not inside this applet — the applet shows the current assignment as a read-only indicator. The single TX channel carries transmit audio from whichever slice currently holds TX privileges.

Each RX channel and the TX channel has a combined level meter and gain slider. The meter bar shows the real-time audio level (post-fader, so moving the slider gives immediate visual feedback). Drag the thumb on the slider to adjust gain. Gain values are saved immediately and restored on next launch.

You can also enable DAX automatically every time AetherSDR starts via `Settings > Autostart DAX with AetherSDR`. This writes the same `AutoStartDAX` setting as the **Enable** button.

## What each control does

| Control | What it does | Default | Range | Setting key |
|---|---|---|---|---|
| **Enable** | Starts or stops the DAX audio bridge. Master switch for all RX and TX streams. | Off | On / Off | `AutoStartDAX` |
| **DAX 1** gain+meter | Sets RX gain and shows level for DAX channel 1. | 0.5 | 0.0–1.0 | `DaxRxGain1` |
| **DAX 2** gain+meter | Sets RX gain and shows level for DAX channel 2. | 0.5 | 0.0–1.0 | `DaxRxGain2` |
| **DAX 3** gain+meter | Sets RX gain and shows level for DAX channel 3. | 0.5 | 0.0–1.0 | `DaxRxGain3` |
| **DAX 4** gain+meter | Sets RX gain and shows level for DAX channel 4. | 0.5 | 0.0–1.0 | `DaxRxGain4` |
| **TX** gain+meter | Sets TX gain and shows level for the DAX TX stream. | 0.5 | 0.0–1.0 | `DaxTxGain` |
| Slice assignment indicator (per RX channel) | Shows which slice is routed to this DAX channel. Displays `—` if no slice is assigned, or `Slice A`–`Slice H` when assigned. Read-only. | — | `—` or `Slice A`–`Slice H` | — |
| TX assignment indicator | Shows which slice currently holds TX privileges and drives the DAX TX stream. Read-only. | — | `—` or `Slice A`–`Slice H` | — |

## Tips

- Gain changes take effect immediately and persist across restarts. You do not need to click a separate save control.
- The level meter bar color shifts from blue to yellow to red as the level increases, giving a quick visual warning of clipping before it affects your audio software.
- If you want DAX running every session without manually clicking **Enable**, use `Settings > Autostart DAX with AetherSDR` instead. Both controls write `AutoStartDAX`.

## Troubleshooting

- **The DAX applet is not visible** — Click the **DAX** tray button on the right sidebar. The applet is hidden by default and must be toggled into view.
- **Slice assignment shows `—` for all channels** — No slice has been assigned to a DAX channel on the radio. Assign a DAX channel to a slice from the slice controls. The applet reflects the assignment automatically once made.
- **TX indicator shows `—`** — No slice currently holds TX privileges, or the radio is not connected.

## Related

- [Enable DAX to route slice audio to WSJT-X / FLDigi / other digital software](enable-dax-to-route-slice-audio-to-wsjt-x-fldigi-other-digital-software.md)
- [Autostart DAX on launch](autostart-dax-on-launch.md)
- [Set DAX RX gain per channel](set-dax-rx-gain-per-channel.md)
- [Set DAX TX gain](set-dax-tx-gain.md)
- [See which slice is currently using each DAX channel](see-which-slice-is-currently-using-each-dax-channel.md)
- [Identify which slice is the TX slice](identify-which-slice-is-the-tx-slice.md)
- [Setting up digital modes (FT8, WSJT-X, fldigi)](../../operating/digital-modes/digital-modes-setup.md)
