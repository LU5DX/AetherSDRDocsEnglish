# Watch live gain reduction while speaking

The Compressor applet displays a horizontal gain-reduction bar and a live envelope ball on the transfer curve so you can see exactly how much the compressor is working while you transmit. Use these indicators to confirm your settings are producing the intended amount of compression without having to guess from audio alone.

## Before you start

- The COMPRESSOR applet must be visible. It appears inside the PooDoo Audio (TXDSP) parent container only when the Compressor stage is enabled (not bypassed) via the CHAIN widget.
- An audio engine must be connected; the meter does not animate without an active audio path.

## Steps

1. Locate the COMPRESSOR sub-container inside the PooDoo Audio (TXDSP) panel.
2. Speak into your microphone at a normal voice level.
3. Watch the **Gain-reduction bar** — the amber strip directly below the transfer curve. It fills from the right as the compressor reduces gain. A tick mark at the −6 dB position gives a reference for a typical working amount.
4. Watch the **Transfer curve** for the envelope ball. The ball moves along the static curve to show your current input level relative to the threshold.
5. Adjust the **Thresh** or **Ratio** knobs until the gain-reduction bar settles in a range that suits your operating style. The bar refreshes approximately 30 times per second with smoothed ballistics.

## What each control does

| Control | Kind | Default | Valid range | Persisted key |
|---|---|---|---|---|
| Transfer curve | Indicator | — | — | — |
| Gain-reduction bar | Meter | — | 0 to 20 dB GR | — |
| Thresh | Knob | −18.0 dB | −60.0 to 0.0 dB | `ClientCompTxThresholdDb` |
| Ratio | Knob | 3.0 | 1.0 to 20.0 | `ClientCompTxRatio` |
| Attack | Knob | 20.0 ms | 0.1 to 300.0 ms | `ClientCompTxAttackMs` |
| Release | Knob | 200 ms | 5 to 2000 ms | `ClientCompTxReleaseMs` |
| Makeup | Knob | +0.0 dB | −12.0 to 24.0 dB | `ClientCompTxMakeupDb` |

**Transfer curve** — View-only in the applet. Draws the static input/output curve. The envelope ball rides on the curve at your current input level.

**Gain-reduction bar** — Horizontal amber strip, right-filled. Empty means no compression is occurring. The fill grows toward the left as gain reduction increases. The scale maxes at 20 dB; the tick marks the −6 dB point.

**Thresh** — Level above which compression begins. Lower values engage the compressor earlier. Displayed as a value in dB (for example, `−18.0 dB`).

**Ratio** — How aggressively peaks are held once the threshold is crossed. Displayed as `X.XX:1`. Higher ratios produce a harder, more limiting character.

**Attack** — How quickly the compressor clamps down after the input crosses the threshold. Displayed as `X.X ms` below 10 ms, `X ms` above.

**Release** — How quickly gain returns after the input drops back below the threshold. Displayed in ms.

**Makeup** — Gain added after compression to recover lost loudness. Displayed with an explicit `+` sign for positive values.

## Tips

- The gain-reduction bar tick at −6 dB is a practical reference point. For most voice operation, keeping the average fill near or below that tick produces natural-sounding compression.
- If the bar is pinned at 20 dB continuously, the threshold is too low or the ratio is too high for your mic level. Raise **Thresh** or lower **Ratio** until the bar breathes with your speech.
- The envelope ball on the transfer curve shows whether you are operating in the linear, knee, or compressed region of the curve — useful when fine-tuning knee settings in the full editor.
- Knee and limiter controls (`ClientCompTxKneeDb`, `ClientCompTxLimEnabled`, `ClientCompTxLimCeilingDb`) are not accessible from the applet knobs. Open the full editor to reach them.

## Troubleshooting

- **Gain-reduction bar shows nothing while speaking** — The Compressor stage may be bypassed. Check the CHAIN widget and ensure the Compressor stage is enabled. If the stage is bypassed, the applet hides itself and the meter does not run.
- **Ball on the transfer curve does not move** — The audio engine is not receiving microphone input. Verify your audio input device is selected and the TX audio path is active.

## Related

- [Compressor overview](overview.md)
- [Adjust compressor threshold](adjust-compressor-threshold.md)
- [Set compression ratio for voice](set-compression-ratio-for-voice.md)
- [Tune attack / release for a natural-sounding squeeze](tune-attack-release-for-a-natural-sounding-squeeze.md)
- [Apply make-up gain after compression](apply-make-up-gain-after-compression.md)
- [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md)
- [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md)
