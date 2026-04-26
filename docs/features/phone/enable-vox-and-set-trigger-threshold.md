# Enable VOX and set trigger threshold

VOX (voice-operated transmit) lets the radio switch to transmit automatically when it detects audio, without pressing PTT. This page explains how to turn VOX on and set the level at which it triggers.

## Before you start

- AetherSDR must be connected to the radio. VOX controls are sent directly to the FLEX-8600 and require an active connection.
- The Phone applet must be visible in the Applet Panel. If it is not, click the PHNE tray button on the right sidebar.

## Steps

1. Open the Phone applet by clicking the PHNE tray button on the right sidebar.
2. Click VOX to enable voice-operated transmit. The button lights green when active.
3. Adjust the VOX level slider to set the trigger threshold. Higher values require a louder audio signal before the radio transmits. Valid range: 0–100.
4. Speak at your normal operating level and watch for unintended keying or missed triggers. Adjust the VOX level slider up or down as needed until the radio keys reliably on your voice and not on background noise.

## What each control does

| Control | Kind | What it does | Default | Range | Setting key |
|---|---|---|---|---|---|
| VOX | Toggle button | Enables or disables voice-operated transmit | — | On / Off | — |
| VOX level | Slider | Sets the audio threshold at which VOX activates | — | 0–100 | — |
| Delay | Slider | Sets how long the radio stays in transmit after audio stops (hang time) | — | 0–100 | — |

## Tips

- If the radio stays keyed after you stop talking, reduce the Delay slider. See [Tune VOX hang time](tune-vox-hang-time.md) for detail.
- If background noise triggers VOX, raise the VOX level slider until the noise no longer activates transmit.
- The numeric value next to each slider updates in real time as you drag.

## Troubleshooting

- **VOX keys the radio on room noise** — Raise the VOX level slider until the threshold is above the noise floor.
- **VOX does not trigger when you speak** — Lower the VOX level slider. If it is already near 0 and the radio still does not key, verify your microphone and audio input are configured correctly in `Settings > Radio Setup...`.
- **Radio stays in transmit after speech ends** — Lower the Delay slider. See [Tune VOX hang time](tune-vox-hang-time.md).

## Related

- [Tune VOX hang time](tune-vox-hang-time.md)
- [Phone overview](overview.md)
