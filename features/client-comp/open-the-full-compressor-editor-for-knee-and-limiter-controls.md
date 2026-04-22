# Open the Full Compressor Editor for Knee and Limiter Controls

The COMPRESSOR applet exposes five knobs for everyday adjustments, but the knee (`ClientCompTxKneeDb`) and limiter (`ClientCompTxLimEnabled`, `ClientCompTxLimCeilingDb`) controls are only available in the floating Compressor editor. Open the editor when you need to shape the transition zone or add a hard ceiling to your TX audio.

## Before you start

- The COMPRESSOR sub-container must be visible inside the PooDoo Audio (TXDSP) parent container.
- The Compressor stage must be enabled (bypass off) via the CHAIN widget; the COMPRESSOR tile stays hidden while bypassed.

## Steps

1. Locate the CHAIN widget inside the PooDoo Audio (TXDSP) container.
2. Double-click the **Comp** stage in the CHAIN widget. The floating Compressor editor opens.

Alternatively:

2. Right-click the **COMPRESSOR** sub-container titlebar and choose the float or pop-out option from the context menu. This surfaces the full editor in a separate window.

## What each control does

The floating editor adds the following controls not present in the applet:

| Control | Default | Valid range | Setting key |
|---|---|---|---|
| Knee | — | — | `ClientCompTxKneeDb` |
| Limiter enable | — | On / Off | `ClientCompTxLimEnabled` |
| Limiter ceiling | — | — | `ClientCompTxLimCeilingDb` |

The editor also mirrors the five knobs available in the applet:

| Control | Default | Valid range | Setting key |
|---|---|---|---|
| Thresh | −18.0 dB | −60.0 to 0.0 dB | `ClientCompTxThresholdDb` |
| Ratio | 3.0 | 1.0 to 20.0 | `ClientCompTxRatio` |
| Attack | 20.0 ms | 0.1 to 300.0 ms | `ClientCompTxAttackMs` |
| Release | 200 ms | 5 to 2000 ms | `ClientCompTxReleaseMs` |
| Makeup | 0.0 dB | −12.0 to 24.0 dB | `ClientCompTxMakeupDb` |

Changes made in the editor and in the applet knobs stay in sync.

## Tips

- The transfer curve in the applet is view-only. The floating editor provides the interactive version of the same curve, where knee adjustments are reflected visually in real time.
- The CHAIN widget single-click bypasses the compressor; double-click opens the editor. Do not single-click when you intend to open the editor.

## Related

- [Compressor overview](overview.md)
- [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md)
- [Adjust compressor threshold](adjust-compressor-threshold.md)
- [Set compression ratio for voice](set-compression-ratio-for-voice.md)
- [Tune attack / release for a natural-sounding squeeze](tune-attack-release-for-a-natural-sounding-squeeze.md)
- [Apply make-up gain after compression](apply-make-up-gain-after-compression.md)
- [Watch live gain reduction while speaking](watch-live-gain-reduction-while-speaking.md)
