# Enable MNR on macOS and set its strength

MNR (MMSE-Wiener noise reduction with asymmetric gain smoothing) is a macOS-only noise reduction engine built into AetherSDR's audio pipeline. This page explains how to turn it on and adjust how aggressively it suppresses noise.

## Before you start

- You must be running AetherSDR on macOS. The "Enable MNR (macOS only)" checkbox has no effect on Linux or Windows.
- A radio connection is not required to change these settings.

## Steps

1. Click `Settings > AetherDSP Settings...` to open the AetherDSP Settings dialog.
2. Click the **MNR** tab.
3. Check **Enable MNR (macOS only)** to activate the engine.
4. Drag the **Strength** slider to set how aggressively MNR suppresses noise. The default is 100 (maximum). Move it left to reduce aggressiveness and preserve more of the original audio character.

## What each control does

| Control | Kind | Default | Valid range | Setting key |
|---|---|---|---|---|
| Enable MNR (macOS only) | Checkbox | *(read from audio engine at startup)* | On / Off | `MnrEnabled` |
| Strength | Slider | 100 | 0–100 | `MnrStrength` |

**Enable MNR (macOS only)** — Enables MMSE-Wiener noise reduction with asymmetric gain smoothing. The initial checked state reflects the live state of the audio engine when the dialog opens.

**Strength** — Controls MNR aggressiveness. 0 is mild suppression; 100 is maximum suppression. The value is persisted internally as a normalized 0.00–1.00 figure.

## Tips

- Start with **Strength** near 100 and reduce it if you notice the signal sounding hollow or over-processed. Voices become smoother as you lower aggressiveness.
- Because the initial state of **Enable MNR (macOS only)** is read live from the audio engine, it may differ from what you last saved if the engine state changed at startup.

## Related

- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
- [AetherDSP Settings overview](overview.md)
- [Tune NR2 reduction depth and voice threshold](tune-nr2-reduction-depth-and-voice-threshold.md)
- [Adjust NR4 reduction amount in dB](adjust-nr4-reduction-amount-in-db.md)
