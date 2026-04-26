# Compressor overview

The client-side compressor is a TX dynamic-range processor built into AetherSDR's audio chain. It reduces peak levels before transmission, letting you increase average power without over-driving the signal.

## Before you start

- The COMPRESSOR tile is part of the PooDoo Audio (TXDSP) processing chain. It stays hidden until the Compressor stage is enabled — bypass it off via the CHAIN widget or the floating editor to make the tile visible.
- No radio connection is required to configure the compressor.

## How it works

The compressor monitors the level of your TX audio in real time. When the signal exceeds the threshold you set, the compressor reduces gain at the ratio you specify. Attack and release times control how quickly it clamps down and lets go. Make-up gain compensates for the overall level lost to compression.

The COMPRESSOR applet gives you a compact view of all of this at once:

- The **Transfer curve** shows the static input/output gain relationship as a curve. A live ball moves along the curve to show where the current envelope level sits. This view is read-only in the applet; the curve is editable in the floating editor.
- The **Gain-reduction bar** is a horizontal amber strip that fills from the right. It shows how much attenuation the compressor is currently applying, up to a maximum of 20 dB. A tick mark at −6 dB indicates a typical working amount of gain reduction. The meter refreshes at approximately 30 Hz with smoothed ballistics.

Two controls that affect whether the compressor is active — enable/bypass and the knee and limiter settings — are not in the applet itself. Bypass is controlled from the CHAIN widget (single-click) or the floating editor. Knee and limiter settings are only available in the floating editor.

## What each control does

| Control | Default | Valid range | Persisted setting | Behavior |
|---|---|---|---|---|
| Thresh | −18.0 dB | −60.0 to 0.0 dB | `ClientCompTxThresholdDb` | Sets the input level above which compression begins. Lower values compress more of the signal. |
| Ratio | 3.0 | 1.0 to 20.0 | `ClientCompTxRatio` | Sets how aggressively peaks are held once the threshold is crossed. Displayed as X.XX:1. Uses logarithmic knob mapping. |
| Attack | 20.0 ms | 0.1 to 300.0 ms | `ClientCompTxAttackMs` | Sets how quickly the compressor responds after the signal crosses the threshold. Uses exponential knob mapping. |
| Release | 200 ms | 5 to 2000 ms | `ClientCompTxReleaseMs` | Sets how quickly gain returns after the signal drops back below the threshold. Uses exponential knob mapping. |
| Makeup | 0.0 dB | −12.0 to +24.0 dB | `ClientCompTxMakeupDb` | Adds back gain lost to compression. Positive values display with an explicit + sign. |
| `ClientCompTxEnabled` | — | on/off | `ClientCompTxEnabled` | Whether the compressor stage is active or bypassed. Controlled from the CHAIN widget or floating editor, not from the applet directly. |
| `ClientCompTxKneeDb` | — | — | `ClientCompTxKneeDb` | Knee width. Only accessible in the floating editor. |
| `ClientCompTxLimEnabled` | — | on/off | `ClientCompTxLimEnabled` | Enables the output limiter. Only accessible in the floating editor. |
| `ClientCompTxLimCeilingDb` | — | — | `ClientCompTxLimCeilingDb` | Limiter ceiling level. Only accessible in the floating editor. |

## Tips

- Watch the gain-reduction bar while speaking at your normal voice level. Aim to keep the amber fill working mostly to the left of the −6 dB tick mark for a natural-sounding result.
- The Transfer curve ball gives you a quick visual check that the threshold is set appropriately — if the ball never moves off the resting position, the threshold may be set too high for your signal level.
- Knee width and limiter settings are only available in the floating editor. Double-click the Comp stage in the CHAIN widget to open it.

## Related

- [Adjust compressor threshold](adjust-compressor-threshold.md)
- [Set compression ratio for voice](set-compression-ratio-for-voice.md)
- [Tune attack / release for a natural-sounding squeeze](tune-attack-release-for-a-natural-sounding-squeeze.md)
- [Apply make-up gain after compression](apply-make-up-gain-after-compression.md)
- [Watch live gain reduction while speaking](watch-live-gain-reduction-while-speaking.md)
- [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md)
- [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md)
