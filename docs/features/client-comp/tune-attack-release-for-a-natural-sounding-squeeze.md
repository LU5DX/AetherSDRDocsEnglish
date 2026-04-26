# Tune Attack / Release for a Natural-Sounding Squeeze

Adjust the Attack and Release knobs in the Compressor applet to control how quickly the compressor responds to voice peaks and recovers between syllables. Getting these two values right prevents the compressor from pumping on fast transients or clamping so slowly that peaks escape.

## Before you start

- The Compressor stage must be enabled (bypass off). If the COMPRESSOR tile is hidden, enable the stage via the CHAIN widget or double-click the Comp stage in the CHAIN widget to open the floating editor and enable it there. See [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md).
- The COMPRESSOR sub-container must be visible inside the PooDoo Audio (TXDSP) parent container.
- You need an audio source (microphone) active so the gain-reduction bar gives live feedback while you adjust.

## Steps

1. Locate the COMPRESSOR sub-container in the PooDoo Audio (TXDSP) parent container.
2. Find the Attack knob in the five-knob row at the bottom of the applet.
3. Rotate Attack to set how quickly the compressor clamps down after the signal crosses the threshold. The default is 20.0 ms. For voice, start there and increase toward 50–80 ms if consonants sound dulled, or decrease toward 5–10 ms if peaks are escaping.
4. Find the Release knob immediately to the right of Attack.
5. Rotate Release to set how quickly gain returns after the signal drops back below the threshold. The default is 200 ms. Increase Release if you hear pumping or breathing between words; decrease it if the compressor holds down the level too long between syllables.
6. Speak into the microphone at a normal level and watch the Gain-reduction bar. The amber fill should move fluidly with your speech. The tick mark on the bar indicates 6 dB of reduction, which is a typical working amount. If the bar is surging and relaxing in an audible rhythm, the Release is too short for your speaking rate.
7. Once the gain-reduction bar moves smoothly without pumping, your attack and release settings are working together correctly.

## What each control does

| Control | Default | Valid range | Setting key |
|---|---|---|---|
| Attack | 20.0 ms | 0.1 to 300.0 ms | `ClientCompTxAttackMs` |
| Release | 200 ms | 5 to 2000 ms | `ClientCompTxReleaseMs` |
| Gain-reduction bar | — | 0 to 20 dB GR | — |

**Attack** — Sets how quickly the compressor clamps down after the input crosses the threshold. Uses exponential knob mapping; the label shows values below 10 ms as `X.X ms` and values at or above 10 ms as `X ms`.

**Release** — Sets how quickly gain returns after the input drops below the threshold. Uses exponential knob mapping; the label shows values as `X ms`.

**Gain-reduction bar** — A horizontal amber strip that fills from the right. Maxes at 20 dB of reduction. A tick marks the 6 dB point. Use this as your primary visual reference while adjusting attack and release.

## Tips

- The Gain-reduction bar updates at approximately 30 Hz with smoothed ballistics, so small rapid changes in your voice will appear slightly averaged. Judge pumping by ear, not solely by the meter.
- Attack and Release interact with Ratio and Thresh. If you change the threshold or ratio significantly, re-check attack and release. See [Adjust compressor threshold](adjust-compressor-threshold.md) and [Set compression ratio for voice](set-compression-ratio-for-voice.md).
- For a slow, transparent squeeze on voice, try Attack around 30–50 ms and Release around 300–500 ms. For tighter peak control, try Attack around 5–10 ms and Release around 100–150 ms.
- The transfer curve and its live envelope ball show the static input/output relationship but do not animate attack and release timing directly. Use the Gain-reduction bar for dynamic feedback.

## Troubleshooting

- **Audible pumping or breathing between words** — Release is too short. Increase Release until the level recovers smoothly between syllables rather than snapping back.
- **Fast transients or consonants sound squashed** — Attack is too short. Increase Attack to let the initial transient through before the compressor engages.
- **Compressor does not react at all to peaks** — Attack may be at or near its maximum (300.0 ms). Decrease Attack. Also confirm the compressor stage is enabled and that the threshold is set below your typical input level. See [Adjust compressor threshold](adjust-compressor-threshold.md).
- **Gain-reduction bar is pinned at maximum** — The compressor is applying its full 20 dB of reduction. The Release is likely too long relative to your speaking rate, or Ratio and Thresh together are too aggressive. Reduce Release, then re-check Thresh and Ratio.

## Related

- [Watch live gain reduction while speaking](watch-live-gain-reduction-while-speaking.md)
- [Adjust compressor threshold](adjust-compressor-threshold.md)
- [Set compression ratio for voice](set-compression-ratio-for-voice.md)
- [Apply make-up gain after compression](apply-make-up-gain-after-compression.md)
- [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md)
