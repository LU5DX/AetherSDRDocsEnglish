# Tune Attack / Release for a Natural-Sounding Squeeze

The Attack and Release knobs control how quickly the compressor clamps down on loud transients and how quickly it lets go afterward. Dialing these in is what separates a transparent, natural-sounding squeeze from an audible pumping artifact.

## Before you start

- The Aetherial Compressor (TX) or Aetherial AGC-C (RX) applet must be visible. The tile is hidden until its stage is enabled via the CHAIN widget. See [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md) if the tile is not showing.
- Decide whether you are tuning the TX path ("Aetherial Compressor" sub-container) or the RX path ("Aetherial AGC-C" sub-container). Both have independent Attack and Release knobs with the same ranges and behavior.

## Steps

1. Locate the five-knob row at the bottom of the compressor tile. The knobs are labeled Thresh, Ratio, Attack, Release, and Makeup, left to right.
2. Watch the gain-reduction bar (the amber horizontal strip above the knob row) while speaking into the microphone (TX) or while audio plays (RX). The strip fills from the right; a tick mark indicates 6 dB of reduction.
3. Turn the **Attack** knob to set how quickly the compressor responds after the input crosses the threshold. Turn left for a faster clamp (more transient control), right for a slower onset (more transient pass-through).
4. Turn the **Release** knob to set how quickly gain recovers after the input drops back below the threshold. Turn left for a faster release (tighter sound), right for a slower release (smoother, less pumping).
5. Observe the live envelope ball on the transfer curve above the knob row. A ball that races up and snaps back on every syllable suggests Release is too fast. A ball that never returns to rest suggests Release is too slow.
6. Repeat steps 3–5 until the gain-reduction bar sits near the −6 dB tick during normal speech peaks and the sound feels even without pumping.

## What each control does

| Knob | Default | Valid range | Persisted key (TX / RX) |
|---|---|---|---|
| Attack | 20.0 ms | 0.1 to 300.0 ms | `ClientCompTxAttackMs` / `ClientCompRxAttackMs` |
| Release | 200 ms | 5 to 2000 ms | `ClientCompTxReleaseMs` / `ClientCompRxReleaseMs` |

**Attack** — Exponential knob mapping. Values below 10 ms display as `X.X ms`; values at 10 ms and above display as `X ms`. Shorter attack times clamp peaks faster but can dull consonants. Longer attack times let transients through before compression engages.

**Release** — Exponential knob mapping. Displayed as `X ms`. Shorter release times let gain return quickly between syllables; if too short, the compressor audibly pumps. Longer release times produce a smoother, more sustained gain reduction but can reduce intelligibility if set too long.

## Tips

- The gain-reduction bar refreshes at approximately 30 Hz with smoothed ballistics, so it reflects the averaged envelope rather than instantaneous peaks. Trust your ears alongside the meter.
- A starting point that works for most SSB voice: Attack 10–20 ms, Release 150–300 ms. Adjust from there based on the gain-reduction bar behavior.
- Double-click the COMP stage in the CHAIN widget to open the full editor, which also exposes the Knee and Limiter controls. Knee softening can reduce the need for extremely precise attack timing. See [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md).
- Both Attack and Release are saved immediately when you move a knob; no explicit save step is needed.

## Troubleshooting

- **Audible pumping or breathing on every syllable** — Release is too fast. Increase the Release value. Try 200–500 ms as a starting range.
- **Gain never fully recovers between words; everything sounds squashed** — Release is too slow, or Ratio is too high. Decrease Release and check that Ratio is not set above 6:1 for normal voice work.
- **Loud transients still clip even with a fast Attack** — Attack cannot be set to 0 ms; the minimum is 0.1 ms. If clipping persists, enable the limiter in the full editor. See [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md).
- **Knob value resets unexpectedly** — Another source (such as a profile load) may have overwritten `ClientCompTxAttackMs` or `ClientCompTxReleaseMs`. Retune and the new value will persist immediately.

## Related

- [Aetherial Compressor (TX) / Aetherial AGC-C (RX) overview](overview.md)
- [Adjust compressor threshold (TX or RX side)](adjust-compressor-threshold-tx-or-rx-side.md)
- [Set compression ratio for voice (TX) or for received audio (RX AGC-C)](set-compression-ratio-for-voice-tx-or-for-received-audio-rx-agc-c.md)
- [Apply make-up gain after compression](apply-make-up-gain-after-compression.md)
- [Watch live gain reduction while speaking or listening](watch-live-gain-reduction-while-speaking-or-listening.md)
- [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md)
