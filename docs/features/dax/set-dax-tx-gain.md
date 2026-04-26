# Set DAX TX gain

Adjust the DAX TX gain slider to control the level of audio sent from your computer to the radio's transmit chain over the DAX audio bridge.

## Before you start

- AetherSDR must be connected to the radio. The DAX applet requires an active radio connection.
- DAX must be enabled. Click Enable in the DAX Audio applet to start the DAX bridge before adjusting TX gain.

## Steps

1. Click the **DAX** tray button on the right sidebar to open the DAX Audio applet.
2. If the Enable button is not already lit, click **Enable** to start the DAX bridge.
3. Locate the **TX:** row at the bottom of the applet. The combined meter and slider shows the current TX gain and live TX audio level.
4. Drag the slider thumb left to reduce TX gain or right to increase it. The setting is saved immediately as `DaxTxGain`.

## What each control does

| Control | Description | Default | Valid range | Setting key |
|---|---|---|---|---|
| Enable | Starts the DAX audio bridge. Must be active for TX audio to flow. | Off | On / Off | `AutoStartDAX` |
| TX gain+meter | Combined level meter and gain slider for the DAX TX stream. Drag the thumb to set gain. The meter bar reflects the post-fader output level. | 0.5 | 0.0 – 1.0 | `DaxTxGain` |
| TX assignment indicator | Shows which slice currently holds TX privileges and drives the DAX TX stream. Displays `—` when no TX slice is assigned, or `Slice A` through `Slice H`. | — | — / Slice A–H | — |

## Tips

- The meter bar in the TX row reflects post-fader level — it scales with the gain thumb position, so you get immediate visual feedback as you drag.
- The gain value is persisted as soon as you release the slider. Restarting AetherSDR restores the saved value.
- Check the TX assignment indicator in the TX row to confirm the expected slice is driving DAX TX before transmitting.

## Troubleshooting

- **TX meter shows no activity during transmit** — Verify Enable is active (button lit green). Confirm your digital mode software is sending audio to the correct DAX TX device. Check the TX assignment indicator to ensure a slice is assigned.
- **Gain resets to 0.5 after restart** — If `DaxTxGain` is absent from saved settings, AetherSDR falls back to the default of 0.5. Make a small adjustment and release the slider to force a save.

## Related

- [DAX Audio overview](overview.md)
- [Enable DAX to route slice audio to WSJT-X / FLDigi / other digital software](enable-dax-to-route-slice-audio-to-wsjt-x-fldigi-other-digital-software.md)
- [Set DAX RX gain per channel](set-dax-rx-gain-per-channel.md)
- [Identify which slice is the TX slice](identify-which-slice-is-the-tx-slice.md)
- [Autostart DAX on launch](autostart-dax-on-launch.md)
