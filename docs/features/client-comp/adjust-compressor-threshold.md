# Adjust Compressor Threshold

Set the level at which the TX compressor begins acting on your signal. Lowering the threshold causes compression to engage earlier and more often; raising it reserves compression for only the loudest peaks.

## Before you start

- The Compressor stage must be enabled (not bypassed) in the CHAIN widget. If the COMPRESSOR tile is hidden, enable the stage there first — see [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md).
- The COMPRESSOR sub-container must be visible inside the PooDoo Audio (TXDSP) parent container.

## Steps

1. Locate the COMPRESSOR sub-container in the applet panel.
2. Find the **Thresh** knob — the leftmost knob in the five-knob row beneath the transfer curve.
3. Click and drag the **Thresh** knob to set the threshold level. Drag up to raise the threshold; drag down to lower it. The knob label updates in real time and shows the value in dB (for example, `-18.0 dB`).
4. Watch the gain-reduction bar while speaking. The amber strip should fill from the right when your signal crosses the threshold. A typical working amount of gain reduction lands near the `-6 dB` tick mark.
5. Release the knob. The new value is saved automatically to `ClientCompTxThresholdDb`.

## What each control does

| Control | Default | Valid range | Persisted key | Description |
|---|---|---|---|---|
| Thresh | -18.0 dB | -60.0 to 0.0 dB | `ClientCompTxThresholdDb` | Level above which compression starts. Linear mapping. |
| Ratio | 3.0 | 1.0 to 20.0 | `ClientCompTxRatio` | How hard peaks are held once the threshold is crossed. Logarithmic mapping. Label shows as `X.XX:1`. |
| Attack | 20.0 ms | 0.1 to 300.0 ms | `ClientCompTxAttackMs` | How quickly the compressor clamps down after the threshold is crossed. Exponential mapping. |
| Release | 200 ms | 5 to 2000 ms | `ClientCompTxReleaseMs` | How quickly gain returns after the signal drops back below threshold. Exponential mapping. |
| Makeup | 0.0 dB | -12.0 to 24.0 dB | `ClientCompTxMakeupDb` | Adds back gain lost to compression. Positive values shown with an explicit `+` sign. |
| Transfer curve | — | — | — | View-only. Draws the static input/output curve plus a live ball showing the current envelope level. |
| Gain-reduction bar | — | 0 to 20 dB GR | — | Horizontal amber strip, right-filled. Tick at -6 dB marks a typical working amount. Refreshed at approximately 30 Hz. |

## Tips

- Start with the default threshold of `-18.0 dB` and lower it gradually while speaking at your normal voice level until the gain-reduction bar shows consistent but moderate activity.
- The live ball on the transfer curve tracks your current envelope against the static curve. Use it to see exactly where your voice level sits relative to the threshold knee.
- If compression is engaging but the overall level sounds lower, increase the **Makeup** knob to compensate — see [Apply make-up gain after compression](apply-make-up-gain-after-compression.md).
- For knee and limiter settings that the applet does not expose, open the full editor — see [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md).

## Troubleshooting

- **Gain-reduction bar shows no activity while transmitting** — The Compressor stage may be bypassed, or your input level is not reaching the threshold. Check that the stage is active in the CHAIN widget, then lower the **Thresh** knob until the bar begins to show amber fill.
- **Gain-reduction bar pegs at maximum (20 dB) immediately** — The threshold is set too low for your input level. Raise the **Thresh** knob toward 0 dB until the bar reads a moderate amount.
- **Knob returns to a different value than you set** — Another source (the floating editor, or a profile load) may have written a conflicting value to `ClientCompTxThresholdDb`. Check the floating editor for the current value.

## Related

- [Compressor overview](overview.md)
- [Set compression ratio for voice](set-compression-ratio-for-voice.md)
- [Tune attack / release for a natural-sounding squeeze](tune-attack-release-for-a-natural-sounding-squeeze.md)
- [Apply make-up gain after compression](apply-make-up-gain-after-compression.md)
- [Watch live gain reduction while speaking](watch-live-gain-reduction-while-speaking.md)
- [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md)
- [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md)
