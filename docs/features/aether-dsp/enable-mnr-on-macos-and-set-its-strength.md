# Enable MNR on macOS and set its strength

MNR is AetherSDR's MMSE-Wiener noise reduction engine, available on macOS only. This page shows how to turn it on and adjust how aggressively it suppresses noise.

## Before you start

- AetherSDR must be running on macOS. The "Enable MNR (macOS only)" checkbox is present only on macOS builds.
- No radio connection is required to adjust these settings.

## Steps

1. Click `Settings > AetherDSP Settings...`.
2. In the **AetherDSP Settings** dialog, click the **MNR** tab.
3. Check **Enable MNR (macOS only)** to activate the engine.
4. Drag the **Strength** slider to set aggressiveness. 0 is the mildest setting; 100 is maximum noise reduction.

## What each control does

| Control | Kind | Default | Valid range | Setting key |
|---|---|---|---|---|
| Enable MNR (macOS only) | Checkbox | *(read from audio engine at startup)* | On / Off | `MnrEnabled` |
| Strength | Slider | 100 | 0–100 | `MnrStrength` |

`MnrStrength` is persisted internally as a normalized value between 0.00 and 1.00.

## Tips

- Start with **Strength** at 100 and reduce it if you notice speech artifacts or a hollow sound. Lower values trade noise suppression for more natural voice reproduction.
- Because MNR's initial enabled state is read live from the audio engine at dialog open time, the checkbox reflects the current engine state rather than a fixed saved default.

## Troubleshooting

- **The MNR tab is visible but "Enable MNR (macOS only)" has no effect** — confirm you are running AetherSDR on macOS. The checkbox label explicitly notes macOS-only availability; on other platforms the engine is not active regardless of this setting.

## Related

- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
- [AetherDSP Settings overview](overview.md)
- [Tune NR2 reduction depth and voice threshold](tune-nr2-reduction-depth-and-voice-threshold.md)
