# Enable adaptive pre-distortion (APD)

The Transmit Model controls adaptive pre-distortion (APD) on the connected radio. APD reduces transmit signal distortion by pre-correcting the waveform before it reaches the power amplifier.

## Before you start

- Confirm your radio reports `apd configurable=1`. The APD control is hidden on radios that do not support this feature.

## Steps

1. Open the TX applet.
2. Click the **APD** toggle button to enable adaptive pre-distortion. The button turns active when APD is on; click it again to disable.

## What each control does

| Control | Behavior |
|---|---|
| **APD** | Enables or disables adaptive pre-distortion on the radio. Hidden on radios that do not report `apd configurable=1`. |

## Tips

- APD state is not persisted across sessions — re-enable it after each connection if you use it regularly.
- If the APD button is not visible in the TX applet, your radio does not support adaptive pre-distortion.

## Related

- [transmit-model.md](transmit-model.md)
- [tune-antenna.md](tune-antenna.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
