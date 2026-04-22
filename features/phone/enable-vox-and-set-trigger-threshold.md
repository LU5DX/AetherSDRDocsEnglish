# Enable VOX and set trigger threshold

Use the Phone applet to turn on voice-operated transmit (VOX) and adjust how sensitive it is to your audio. VOX automatically keys the transmitter when you speak, removing the need to press a PTT button.

## Before you start

- AetherSDR must be connected to the radio. VOX controls are sent directly to the FLEX-8600 and require an active connection.
- The Phone applet must be visible. If it is not, click the PHNE tray button in the right sidebar to show it.

## Steps

1. Open the Phone applet by clicking the PHNE tray button in the right sidebar.
2. Click the **VOX** toggle button to enable voice-operated transmit. The button lights green when active.
3. Adjust the **VOX level** slider to set the activation threshold. Move it right to require a stronger audio signal before the radio keys; move it left to make it more sensitive. The valid range is 0–100. The current value is shown as a number to the right of the slider.

## What each control does

| Control | Kind | Valid range | Default | Behavior |
|---|---|---|---|---|
| VOX | Toggle button | On / Off | Off | Enables or disables voice-operated transmit. |
| VOX level | Slider | 0–100 | — | Sets the audio level required to activate the transmitter. Higher values require louder audio. |

## Tips

- After setting the threshold, watch the transmit indicator while speaking at your normal operating level. If the radio keys on background noise, increase the **VOX level** value. If it fails to key on speech, decrease it.
- VOX hang time (how long the radio stays in transmit after you stop speaking) is controlled separately by the **Delay** slider. See [Tune VOX hang time](tune-vox-hang-time.md).

## Troubleshooting

- **VOX does not key the radio even when speaking loudly** — The **VOX level** threshold may be set too high. Move the slider toward 0 to reduce the required activation level.
- **VOX keys on background noise or room sound** — The **VOX level** threshold is too low. Move the slider toward 100 until ambient noise no longer triggers the transmitter.

## Related

- [Tune VOX hang time](tune-vox-hang-time.md)
- [Phone overview](overview.md)
- [Set the TX audio low-cut frequency](set-the-tx-audio-low-cut-frequency.md)
- [Set the TX audio high-cut frequency](set-the-tx-audio-high-cut-frequency.md)
