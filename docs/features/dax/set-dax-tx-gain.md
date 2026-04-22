# Set DAX TX gain

Adjust the TX gain slider in the DAX Audio applet to control the level of the transmit audio stream sent from your computer to the radio. Setting this correctly prevents over- or under-driving the DAX TX path when using digital mode software.

## Before you start

- AetherSDR must be connected to the radio. The DAX Audio applet requires an active radio connection.
- DAX must be enabled. Click Enable in the DAX Audio applet if it is not already active.

## Steps

1. Click the DAX tray button on the right sidebar to open the DAX Audio applet.
2. Locate the **TX:** row at the bottom of the applet. The combined meter and slider shows the current TX gain position and live TX audio level.
3. Drag the slider thumb left to decrease TX gain or right to increase it. The valid range is 0.0 to 1.0. The default is 0.5.
4. Release the slider. The value is saved immediately to `DaxTxGain` and takes effect without restarting.

## What each control does

| Control | Default | Range | Setting key | Behavior |
|---|---|---|---|---|
| TX gain+meter | 0.5 | 0.0–1.0 | `DaxTxGain` | Drag to set the TX stream gain. The meter behind the thumb shows the live transmit level post-fader. |
| TX assignment indicator | — | — or Slice A–H | — | Shows which slice currently holds TX privileges and drives the DAX TX stream. Read-only. |
| Enable | off | on/off | `AutoStartDAX` | Master switch for all DAX streams including TX. TX gain has no effect while DAX is disabled. |

## Tips

- The meter fill behind the slider reflects the post-fader level — the raw input level multiplied by the current gain — so you can see the effective TX output level as you drag.
- If the TX assignment indicator shows —, no slice currently holds TX privileges. Ensure your transmit slice is selected on the radio before adjusting TX gain.

## Troubleshooting

- **TX meter shows no activity** — DAX TX audio only flows while the radio is transmitting or a digital mode application is sending audio to the DAX TX device. Check that your software (WSJT-X, fldigi, etc.) is routed to the correct DAX TX audio device.
- **TX gain resets after restart** — Verify `AutoStartDAX` is enabled so the DAX bridge starts on launch and restores the saved `DaxTxGain` value. See [Autostart DAX on launch](autostart-dax-on-launch.md).

## Related

- [DAX Audio overview](overview.md)
- [Enable DAX to route slice audio to WSJT-X / FLDigi / other digital software](enable-dax-to-route-slice-audio-to-wsjt-x-fldigi-other-digital-software.md)
- [Set DAX RX gain per channel](set-dax-rx-gain-per-channel.md)
- [Identify which slice is the TX slice](identify-which-slice-is-the-tx-slice.md)
- [Autostart DAX on launch](autostart-dax-on-launch.md)
