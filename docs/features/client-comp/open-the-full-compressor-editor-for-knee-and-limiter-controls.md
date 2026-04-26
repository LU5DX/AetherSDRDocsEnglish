# Open the Full Compressor Editor for Knee and Limiter Controls

The COMPRESSOR applet exposes five knobs for everyday adjustments. Two controls — soft-knee width (`ClientCompTxKneeDb`) and the output limiter (`ClientCompTxLimEnabled`, `ClientCompTxLimCeilingDb`) — are only available in the floating Compressor editor. Open the editor when you need to shape the compression curve at the threshold or add a hard ceiling to your TX signal.

## Before you start

- The Compressor stage must be present in the PooDoo Audio (TXDSP) chain. If you have not added it yet, see [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md).
- The COMPRESSOR sub-container must be visible in the applet panel. It stays hidden while the Compressor stage is bypassed.

## Steps

1. Locate the CHAIN widget inside the PooDoo Audio (TXDSP) container.
2. Double-click the **Comp** stage in the CHAIN widget. The floating Compressor editor opens.

Alternatively:

1. Right-click the **COMPRESSOR** sub-container titlebar.
2. Select the option to open or float the editor from the context menu.

## What each control does

The floating Compressor editor exposes all compressor parameters, including the two not available in the applet.

| Control | Default | Valid range | Setting key |
|---|---|---|---|
| Thresh | −18.0 dB | −60.0 to 0.0 dB | `ClientCompTxThresholdDb` |
| Ratio | 3.0 | 1.0 to 20.0 | `ClientCompTxRatio` |
| Attack | 20.0 ms | 0.1 to 300.0 ms | `ClientCompTxAttackMs` |
| Release | 200 ms | 5 to 2000 ms | `ClientCompTxReleaseMs` |
| Makeup | 0.0 dB | −12.0 to 24.0 dB | `ClientCompTxMakeupDb` |
| Knee | — | — | `ClientCompTxKneeDb` |
| Limiter enabled | — | on / off | `ClientCompTxLimEnabled` |
| Limiter ceiling | — | — | `ClientCompTxLimCeilingDb` |

The transfer curve widget in the editor is interactive, unlike the view-only version in the applet. Changes to knee, threshold, and ratio are reflected on the curve immediately.

## Tips

- Knob and curve changes made in the floating editor are reflected in real time on the applet's transfer curve and gain-reduction bar, so you can watch metering in the applet while editing parameters in the floating window.
- The five knobs in the COMPRESSOR applet (Thresh, Ratio, Attack, Release, Makeup) are kept in sync with the editor. Adjusting either location updates the other.

## Related

- [Compressor overview](overview.md)
- [Adjust compressor threshold](adjust-compressor-threshold.md)
- [Set compression ratio for voice](set-compression-ratio-for-voice.md)
- [Tune attack / release for a natural-sounding squeeze](tune-attack-release-for-a-natural-sounding-squeeze.md)
- [Apply make-up gain after compression](apply-make-up-gain-after-compression.md)
- [Watch live gain reduction while speaking](watch-live-gain-reduction-while-speaking.md)
- [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md)
