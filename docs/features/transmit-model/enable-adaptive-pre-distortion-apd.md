# Enable adaptive pre-distortion (APD)

The Transmit Model exposes an APD toggle that instructs the radio to apply adaptive pre-distortion to the transmit signal, reducing distortion at higher power levels.

## Before you start

- Confirm your radio reports `apd configurable=1`. The APD row is hidden automatically on radios that do not support this feature.

## Steps

1. Open the TX applet.
2. Click the **APD** toggle button to enable adaptive pre-distortion. The button activates when APD is on; click it again to disable.

## What each control does

| Control | Behavior | Notes |
|---|---|---|
| **APD** | Enables or disables adaptive pre-distortion on the radio. Hidden on radios that do not report `apd configurable=1`. |  |
## Tips

- APD works on the transmitted signal in real time. You do not need to retune or reload a TX profile after toggling it.
- If the **APD** row is not visible, your radio firmware does not support adaptive pre-distortion; no action is needed.

## Related

- [Transmit overview](transmit-overview.md)
- [Enable ATU](enable-atu.md)
- [Set RF power](set-rf-power.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
