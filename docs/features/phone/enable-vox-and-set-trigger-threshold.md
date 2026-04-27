# Enable VOX and set trigger threshold

VOX (voice-operated transmit) automatically keys the transmitter when your audio exceeds a set level, so you do not need to press PTT during phone operation. This page explains how to enable VOX and adjust its activation threshold in the Phone applet.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. VOX controls are inactive without a radio connection.
- The Phone applet must be visible in the Applet Panel. If it is not, click the PHNE tray button on the right sidebar.

## Steps

1. Open the Phone applet by clicking the PHNE tray button on the right sidebar.
2. Click VOX to enable voice-operated transmit. The button lights green when active.
3. Adjust the VOX level slider to set the activation threshold. Move it right to require a stronger audio signal before the radio keys; move it left to key on quieter audio. Valid range: 0–100.

## What each control does

| Control | Kind | What it does | Default | Range | Persisted key |
|---|---|---|---|---|---|
| VOX | Toggle button | Enables or disables voice-operated transmit | — | On / Off | — |
| VOX level | Slider | Sets the audio threshold required to activate transmit | — | 0–100 | — |
| Delay | Slider | Sets the hang time before the radio returns to receive after audio drops below the threshold | — | 0–100 | — |

## Tips

- If the radio keys up unintentionally on background noise, increase the VOX level slider value.
- If VOX drops out mid-syllable, increase the Delay slider to extend the hang time before the radio returns to receive.

## Troubleshooting

- **Radio does not key when you speak** — VOX level may be set too high. Lower the VOX level slider value so quieter audio triggers transmit.
- **Radio stays in transmit too long after you stop speaking** — Decrease the Delay slider value to shorten the hang time.

## Related

- [Tune VOX hang time](tune-vox-hang-time.md)
- [Phone overview](overview.md)
