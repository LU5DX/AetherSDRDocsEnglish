# Enable MNR on macOS and set its strength

MNR is AetherSDR's macOS-native MMSE-Wiener noise reduction engine with asymmetric gain smoothing. Use this page to turn it on and adjust how aggressively it suppresses noise.

## Before you start

- AetherSDR must be running on macOS. MNR is a macOS-only engine; the control is present but has no effect on other platforms.
- No radio connection is required to change these settings.

## Steps

1. Click `Settings > AetherDSP Settings...`.
2. In the AetherDSP Settings dialog, click the **MNR** tab.
3. Check **Enable MNR (macOS only)** to turn the engine on.
4. Drag the **Strength** slider to the desired level. The range is 0–100; 0 is mild reduction and 100 is maximum.

## What each control does

| Control | Description | Default | Range | Setting key |
|---|---|---|---|---|
| **Enable MNR (macOS only)** | Enables MMSE-Wiener noise reduction with asymmetric gain smoothing. | Read from audio engine at startup | On / Off | `MnrEnabled` |
| **Strength** | Adjusts MNR aggressiveness. | 100 | 0–100 | `MnrStrength` |

`MnrStrength` is persisted as a normalized value of 0.00–1.00 regardless of the slider's 0–100 display scale.

## Tips

- Start with **Strength** at 100 and reduce it if you notice speech artifacts or an unnatural sound. Lower values trade some noise suppression for more natural audio.

## Troubleshooting

- **Enable MNR (macOS only) has no effect** — MNR is a macOS-only engine. On Linux or Windows the checkbox is visible but the engine does not run.
- **Settings do not persist after restart** — Verify that AetherSDR has write access to its settings storage. Both `MnrEnabled` and `MnrStrength` are persisted automatically when you change them.

## Related

- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
- [AetherDSP Settings overview](overview.md)
- [Tune NR2 reduction depth and voice threshold](tune-nr2-reduction-depth-and-voice-threshold.md)
