# Compressor overview

The client-side TX compressor in AetherSDR reduces dynamic range in your transmitted audio before it reaches the radio. Use it to tame voice peaks, maintain consistent average power, and reduce the chance of splatter on SSB.

## Before you start

- The Compressor stage must be enabled (bypass off) via the CHAIN widget or the floating editor before the COMPRESSOR applet tile becomes visible.
- No radio connection is required to adjust compressor settings.

## How it works

The compressor runs entirely on the client side — it processes audio in AetherSDR before the signal is sent to the FLEX-8600. It applies a standard gain-reduction model: when the input level crosses the threshold, the compressor attenuates the signal according to the ratio you set. Attack and release times control how quickly the compressor clamps down and recovers. Makeup gain lets you restore the average level lost to compression.

The **COMPRESSOR** applet tile lives inside the PooDoo Audio (TXDSP) parent container. It shows a transfer curve with a live envelope indicator and a horizontal gain-reduction meter so you can watch compression in real time while transmitting.

To access knee and limiter controls (`ClientCompTxKneeDb`, `ClientCompTxLimEnabled`, `ClientCompTxLimCeilingDb`), open the floating editor by double-clicking the Comp stage in the CHAIN widget.

## What each control does

| Control | Description | Default | Range | Setting key |
|---|---|---|---|---|
| Transfer curve | Draws the static input/output transfer curve. A live ball moves along the curve to show the current envelope level. View-only in the applet; editable in the floating editor. | — | — | — |
| Gain-reduction bar | Horizontal amber strip, right-filled. Shows how much attenuation is currently applied. A tick marks the −6 dB point as a typical working reference. Scale maxes at 20 dB reduction. | — | 0–20 dB GR | — |
| Thresh | Level above which compression starts. | −18.0 dB | −60.0 to 0.0 dB | `ClientCompTxThresholdDb` |
| Ratio | How aggressively peaks are held once the threshold is crossed. Displayed as X.XX:1. | 3.0 | 1.0 to 20.0 | `ClientCompTxRatio` |
| Attack | How quickly the compressor clamps down after the input crosses the threshold. | 20.0 ms | 0.1 to 300.0 ms | `ClientCompTxAttackMs` |
| Release | How quickly gain returns after the input drops back below the threshold. | 200 ms | 5 to 2000 ms | `ClientCompTxReleaseMs` |
| Makeup | Adds back gain lost to compression. Positive values are shown with an explicit `+` sign. | 0.0 dB | −12.0 to 24.0 dB | `ClientCompTxMakeupDb` |

The following settings are available only in the floating editor:

| Setting key | Purpose |
|---|---|
| `ClientCompTxEnabled` | Enables or bypasses the compressor stage. |
| `ClientCompTxKneeDb` | Softens the transition into compression around the threshold. |
| `ClientCompTxLimEnabled` | Enables the output limiter. |
| `ClientCompTxLimCeilingDb` | Sets the hard ceiling the limiter enforces. |

## Tips

- The gain-reduction bar is refreshed at approximately 30 Hz. Watch it while speaking to judge whether your settings are working before you transmit on-air.
- The −6 dB tick on the gain-reduction bar is a useful reference: consistent reduction in that region generally produces natural-sounding compression on SSB voice.
- The five knobs in the applet tile are sufficient for most adjustments. Open the floating editor only when you need to tune the knee or enable the limiter.
- Right-click the COMPRESSOR sub-container titlebar to float, pop-out, or hide the applet tile.

## Related

- [Adjust compressor threshold](adjust-compressor-threshold.md)
- [Set compression ratio for voice](set-compression-ratio-for-voice.md)
- [Tune attack / release for a natural-sounding squeeze](tune-attack-release-for-a-natural-sounding-squeeze.md)
- [Apply make-up gain after compression](apply-make-up-gain-after-compression.md)
- [Watch live gain reduction while speaking](watch-live-gain-reduction-while-speaking.md)
- [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md)
- [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md)
