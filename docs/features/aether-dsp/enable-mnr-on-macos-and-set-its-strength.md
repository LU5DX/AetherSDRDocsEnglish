# Enable MNR on macOS and set its strength

MNR is an MMSE-Wiener noise reduction engine available only on macOS. Use this page to turn it on and adjust how aggressively it suppresses noise.

## Before you start

- AetherSDR must be running on macOS. The "Enable MNR (macOS only)" checkbox has no effect on Linux or Windows.
- No radio connection is required to change these settings.

## Steps

1. Click `Settings > AetherDSP Settings...`.
2. Click the **MNR** tab.
3. Check **Enable MNR (macOS only)** to activate the engine.
4. Drag the **Strength** slider to the desired level. Lower values apply mild noise reduction; higher values apply maximum suppression.

## What each control does

| Control | Description | Default | Valid range | Setting key |
|---|---|---|---|---|
| Enable MNR (macOS only) | Enables MMSE-Wiener noise reduction with asymmetric gain smoothing. Initial state is read from the audio engine at dialog open. | — | On / Off | `MnrEnabled` |
| Strength | Adjusts MNR aggressiveness. 0 is mild; 100 is maximum. Persisted internally as a normalized value (0.00–1.00). | 100 | 0–100 | `MnrStrength` |

## Tips

- If you want noise reduction that works across all platforms, consider NR2 or NR4 instead. MNR is macOS-only and will not be active on Linux or Windows regardless of the saved `MnrEnabled` value.
- Changes take effect immediately — there is no Apply or OK button to press.

## Related

- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
- [Tune NR2 reduction depth and voice threshold](tune-nr2-reduction-depth-and-voice-threshold.md)
- [Adjust NR4 reduction amount in dB](adjust-nr4-reduction-amount-in-db.md)
- [AetherDSP Settings overview](overview.md)
