# Set DAX TX gain

Adjust the TX gain slider in the DAX Audio applet to control the output level of the DAX transmit stream sent from your computer audio to the radio. This is useful when your digital mode software's audio output is too loud or too quiet relative to the radio's expected input level.

## Before you start

- Connect to a FLEX-8600 radio. The DAX applet requires an active radio connection.
- Open the DAX applet by clicking the DAX tray button on the right sidebar. The applet is hidden by default.
- DAX must be enabled. If the Enable button is not lit, click Enable to start the DAX audio bridge.

## Steps

1. Click the DAX tray button on the right sidebar to open the DAX Audio applet.
2. Locate the TX row at the bottom of the applet. It shows a label "TX:", a slice assignment indicator, and a combined meter/slider.
3. Drag the thumb on the TX gain+meter slider left to decrease gain or right to increase gain. The valid range is 0.0 to 1.0.
4. Release the mouse button. The new value is saved immediately to `DaxTxGain`.

## What each control does

| Control | Default | Valid range | Setting key | Behavior |
|---|---|---|---|---|
| TX gain+meter slider | 0.5 | 0.0–1.0 | `DaxTxGain` | Sets the gain for the DAX TX stream. The meter bar behind the slider shows the current output level post-fader. |
| TX assignment indicator | — | — or Slice A–H | *(none)* | Shows which slice currently holds TX privileges and drives the DAX TX stream. |

## Tips

- The meter bar behind the slider shows the post-fader level — that is, the incoming audio level multiplied by the current gain setting. A bar that stays near the right edge at your current gain suggests the gain is too high; reduce it to avoid clipping.
- The gain value persists across sessions. You do not need to re-enter it after restarting AetherSDR.

## Troubleshooting

- **TX meter shows no activity** — The TX slice may not be assigned yet. Check the TX assignment indicator. If it shows "—", no slice currently holds TX privileges. See [Identify which slice is the TX slice](identify-which-slice-is-the-tx-slice.md).
- **Slider position resets on reopen** — If DAX was not enabled when you set the gain, the setting still saves, but confirm Enable is active so the bridge is running and the value takes effect.

## Related

- [DAX Audio overview](overview.md)
- [Enable DAX to route slice audio to WSJT-X / FLDigi / other digital software](enable-dax-to-route-slice-audio-to-wsjt-x-fldigi-other-digital-software.md)
- [Set DAX RX gain per channel](set-dax-rx-gain-per-channel.md)
- [Identify which slice is the TX slice](identify-which-slice-is-the-tx-slice.md)
- [Autostart DAX on launch](autostart-dax-on-launch.md)
