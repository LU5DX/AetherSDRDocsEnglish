# Enable MNR on macOS and set its strength

MNR is AetherSDR's MMSE-Wiener noise reduction engine, available on macOS only. This page shows how to turn it on and adjust how aggressively it suppresses noise.

## Before you start

- AetherSDR must be running on macOS. The "Enable MNR (macOS only)" checkbox is present on all platforms but MNR processing is macOS-exclusive.
- No radio connection is required to open AetherDSP Settings.

## Steps

1. Click `Settings > AetherDSP Settings...`.
2. In the **AetherDSP Settings** dialog, click the **MNR** tab.
3. Check **Enable MNR (macOS only)** to activate the engine.
4. Drag the **Strength** slider to set aggressiveness. The default is 100 (maximum). Lower values reduce suppression.

## What each control does

| Control | Kind | Default | Valid range | Setting key |
|---|---|---|---|---|
| Enable MNR (macOS only) | Checkbox | *(read from audio engine at launch)* | On / Off | `MnrEnabled` |
| Strength | Slider | 100 | 0–100 | `MnrStrength` |

**Strength** is persisted internally as a normalized value of 0.00–1.00. The slider displays it on a 0–100 scale. A value of 0 applies minimal noise reduction; 100 applies maximum suppression.

## Tips

- Changes to **Strength** take effect immediately without restarting AetherSDR or reconnecting to the radio.
- If you want a lighter touch, set **Strength** to a value between 30 and 60 to reduce noise while preserving more speech naturalness.

## Troubleshooting

- **"Enable MNR (macOS only)" checkbox is visible but has no effect** — MNR processing is macOS-only. If you are running AetherSDR on Linux or Windows, the checkbox will appear but the engine will not activate.

## Related

- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
- [Tune NR2 reduction depth and voice threshold](tune-nr2-reduction-depth-and-voice-threshold.md)
- [Adjust NR4 reduction amount in dB](adjust-nr4-reduction-amount-in-db.md)
- [Set DeepFilterNet3 attenuation limit for strong or weak signals](set-deepfilternet3-attenuation-limit-for-strong-or-weak-signals.md)
