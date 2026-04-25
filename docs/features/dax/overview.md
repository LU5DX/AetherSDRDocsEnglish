# DAX Audio overview

The DAX (Digital Audio eXchange) applet bridges audio between your FLEX-8600 and other software on your computer. Use it to route received slice audio into digital mode programs such as WSJT-X or fldigi, and to send audio from those programs back to the radio for transmission.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The DAX applet requires an active radio connection.
- The DAX applet is hidden by default. Click the **DAX** tray button on the right sidebar to show it.

## How it works

DAX provides four independent RX audio channels and one TX audio channel. Each RX channel can be assigned to a slice on the radio; the applet shows which slice (if any) is currently routed to each channel. The TX channel carries audio from your computer to the radio and is driven by whichever slice currently holds TX privileges.

Each channel has a combined meter and gain slider. The meter shows the post-fader level — the smoothed RMS signal multiplied by the current gain — so the bar reflects actual output level. Drag the slider thumb to set the gain for that channel; the value is saved immediately.

The master **Enable** button starts or stops the entire DAX audio bridge. Toggling it also updates the `AutoStartDAX` setting, which controls whether DAX starts automatically when AetherSDR launches. You can also set autostart from `Settings > Autostart DAX with AetherSDR`.

## What each control does

| Control | What it does | Default | Range | Setting key |
|---|---|---|---|---|
| **Enable** | Starts or stops the DAX audio bridge. Master switch for all RX and TX streams. | Off | On / Off | `AutoStartDAX` |
| **DAX 1** gain+meter | Sets RX gain for DAX channel 1 and displays its post-fader level. | 0.5 | 0.0 – 1.0 | `DaxRxGain1` |
| **DAX 2** gain+meter | Sets RX gain for DAX channel 2 and displays its post-fader level. | 0.5 | 0.0 – 1.0 | `DaxRxGain2` |
| **DAX 3** gain+meter | Sets RX gain for DAX channel 3 and displays its post-fader level. | 0.5 | 0.0 – 1.0 | `DaxRxGain3` |
| **DAX 4** gain+meter | Sets RX gain for DAX channel 4 and displays its post-fader level. | 0.5 | 0.0 – 1.0 | `DaxRxGain4` |
| **TX** gain+meter | Sets gain for the DAX TX stream and displays its post-fader level. | 0.5 | 0.0 – 1.0 | `DaxTxGain` |
| Slice-assignment indicator (per RX channel) | Shows which slice is routed to this DAX channel. Displays `—` when unassigned, or `Slice A` through `Slice H` when assigned. | — | `—` or `Slice A–H` | — |
| TX slice indicator | Shows which slice currently holds TX privileges and drives the DAX TX stream. Displays `—` when no TX slice is active. | — | `—` or `Slice A–H` | — |

## Tips

- Gain changes are saved immediately to persistent settings. You do not need to click a separate save or apply button.
- The meter uses asymmetric smoothing: the level bar rises quickly on a new signal (fast attack) and falls slowly when the signal drops (slow decay), consistent with other metering surfaces in AetherSDR.

## Related

- [Enable DAX to route slice audio to WSJT-X / FLDigi / other digital software](enable-dax-to-route-slice-audio-to-wsjt-x-fldigi-other-digital-software.md)
- [Autostart DAX on launch](autostart-dax-on-launch.md)
- [Set DAX RX gain per channel](set-dax-rx-gain-per-channel.md)
- [Set DAX TX gain](set-dax-tx-gain.md)
- [See which slice is currently using each DAX channel](see-which-slice-is-currently-using-each-dax-channel.md)
- [Identify which slice is the TX slice](identify-which-slice-is-the-tx-slice.md)
- [Setting up digital modes (FT8, WSJT-X, fldigi)](../../operating/digital-modes/digital-modes-setup.md)
