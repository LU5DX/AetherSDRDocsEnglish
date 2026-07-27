# Tune Attack / Release for a Natural-Sounding Squeeze

The Attack and Release knobs control how quickly the compressor clamps down on loud transients and how quickly it lets go afterward. Dialing these in is what separates a transparent, natural-sounding squeeze from an audible pumping artifact.

## Before you start

- The Aetherial Compressor (TX) or Aetherial AGC-C (RX) applet must be visible. The tile is hidden until its stage is enabled via the CHAIN widget. See [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md) if the tile is not showing.
- When a compressor stage is bypassed, the entire tile renders at reduced opacity (approximately 55% of full brightness). This is a visual indicator only and does not affect your knob settings.
- Decide whether you are tuning the TX path ("Aetherial Compressor" sub-container) or the RX path ("Aetherial AGC-C" sub-container). Both have independent Attack and Release knobs with the same ranges and behavior.

## Steps

1. Locate the five-knob row at the bottom of the compressor tile. The knobs are labeled **Thresh**, **Ratio**, **Attack**, **Release**, and **Makeup**, left to right.
2. Watch the gain-reduction bar (the amber horizontal strip above the knob row) while speaking into the microphone (TX) or while audio plays (RX). The strip fills from the right; a tick mark indicates 6 dB of reduction.
3. Turn the **Attack** knob to set how quickly the compressor responds after the input crosses the threshold. Turn left for a faster clamp (more transient control), right for a slower onset (more transient pass-through).
4. Turn the **Release** knob to set how quickly gain recovers after the input drops back below the threshold. Turn left for a faster release (tighter sound), right for a slower release (smoother, less pumping).
5. Observe the live envelope ball on the transfer curve above the knob row. A ball that races up and snaps back on every syllable suggests Release is too fast. A ball that never returns to rest suggests Release is too slow.
6. Repeat steps 3–5 until the gain-reduction bar sits near the −6 dB tick during normal speech peaks and the sound feels even without pumping.

## What each control does

| Knob    | Default  | Valid range     |
|---------|----------|-----------------|
| Attack  | 20.0 ms  | 0.1 to 300.0 ms |
| Release | 200 ms   | 5 to 2000 ms    |
| Drive   | 0.0 dB   | 0.0 to 18.0 dB  |
| Phase   | 0 stages | 0 to 6 stages   |

**Attack** — Exponential knob mapping. Values below 10 ms display as `X.X ms`; values at 10 ms and above display as `X ms`. Shorter attack times clamp peaks faster but can dull consonants. Longer attack times let transients through before compression engages.

**Release** — Exponential knob mapping. Displayed as `X ms`. Shorter release times let gain return quickly between syllables; if too short, the compressor audibly pumps. Longer release times produce a smoother, more sustained gain reduction but can reduce intelligibility if set too long.

**Drive** — Pre-comp gain boost with linked auto-makeup. Pushes more signal across the threshold so the compressor engages harder, and simultaneously adds equal gain at the output so average RMS lifts alongside peaks rather than dropping. Pair with Phase to keep peaks clean. Displayed in the floating StripCompPanel only (right column). Label shows as '+X.X dB'.

**Phase** — Number of cascaded all-pass sections (0 = off). Each stage adds 12 dB/oct of phase rotation at staggered frequencies (300/700/1500/2500 Hz, plus optional 1000/2000 Hz). Symmetrizes asymmetric voice peaks before compression to reduce PAPR. Displayed in the floating StripCompPanel only (right column). Label 'Off' when 0, 'N stg' when active. Tooltip: 'Pre-comp phase rotator (#2887). All-pass cascade that symmetrizes asymmetric voice peaks before compression. 0 = off, 4 = broadcast default.'

## Using the inline value editor

When you click a knob's numeric value label, it transforms into an editable text field. This allows precise numerical entry without dragging the knob.

1. Click the numeric value below any knob (Thresh, Ratio, Attack, Release, or Makeup). The value text becomes a highlighted input field with a cyan border.
2. Type the desired value. Supported formats include:
   - Simple numbers: `150`
   - Numbers with units: `150 ms`
   - Comma-decimal locale format: `12,5`
   - Values with a minus sign: `−18`
3. Press **Enter** or click anywhere outside the editor to commit the value. The knob updates immediately.
4. Press **Escape** to cancel editing and revert to the previous value.

The inline editor is enabled by default for all five knobs. It cannot be disabled in the applet view.

## Tips

- The gain-reduction bar refreshes at approximately 30 Hz with smoothed ballistics, so it reflects the averaged envelope rather than instantaneous peaks. Trust your ears alongside the meter.
- The transfer curve display caches axis labels for performance. Labels rebuild automatically when you toggle compact mode (e.g., when switching between the applet tile and the floating editor). This ensures the font size (9 px in full mode, 7 px in compact mode) always matches the current display without any visual lag.
- The compressor animation timer uses precise timing and runs repaints continuously for accurate visual feedback. The envelope ball and gain-reduction bar update smoothly at every animation tick regardless of settling state.
- A starting point that works for most SSB voice: Attack 10–20 ms, Release 150–300 ms. Adjust from there based on the gain-reduction bar behavior.
- If the tile appears dimmed, the compressor stage is currently bypassed. Re-enable it via the CHAIN widget before evaluating knob settings.
- Double-click the COMP stage in the CHAIN widget to open the full editor, which also exposes the **Knee**, **Limiter**, **Drive**, and **Phase** controls. Knee softening can reduce the need for extremely precise attack timing. See [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md).
- Both Attack and Release are saved immediately when you move a knob; no explicit save step is needed.
- Use the inline value editor for repeatable, exact values. For example, type `12.5` for Attack instead of dragging to approximate.

## Troubleshooting

- **Audible pumping or breathing on every syllable** — Release is too fast. Increase the Release value. Try 200–500 ms as a starting range.
- **Gain never fully recovers between words; everything sounds squashed** — Release is too slow, or Ratio is too high. Decrease Release and check that Ratio is not set above 6:1 for normal voice work.
- **Loud transients still clip even with a fast Attack** — Attack cannot be set to 0 ms; the minimum is 0.1 ms. If clipping persists, enable the limiter in the full editor. See [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md).
- **The tile is dimmed and the compressor does not seem to be doing anything** — The stage is bypassed. Enable it via the CHAIN widget. The tile returns to full brightness when the stage is active.
- **Knob value resets unexpectedly** — Another source (such as a profile load) may have overwritten `ClientCompTxAttackMs` or `ClientCompTxReleaseMs`. Retune and the new value will persist immediately.
- **Inline editor value is rejected** — The input must be a valid number in the knob's valid range. If the value is outside the range, it is clamped automatically. Non-numeric characters (other than decimal separators, sign, and comma) cause the edit to be ignored.

## Theme support

The compressor applet and its transfer curve widget now respect the current AetherSDR theme. Colors for the following elements are drawn from theme variables rather than hard-coded values:

| Element | Theme variable |
|---------|----------------|
| Widget background | `color.background.0` |
| Grid lines | `color.background.1` |
| Axis labels | `color.text.label` |
| Unity (identity) line | `color.background.1` |
| Transfer curve | `color.accent.dim` |
| Envelope ball glow | `color.accent.warning` |
| Envelope ball core | `color.text.primary` |

The gain-reduction slider fill uses the theme color `color.slider.foreground` applied at the `applet/comp` scope via the ThemeManager.

## Related

- [Aetherial Compressor (TX) / Aetherial AGC-C (RX) overview](overview.md)
- [Adjust compressor threshold (TX or RX side)](adjust-compressor-threshold-tx-or-rx-side.md)
- [Set compression ratio for voice (TX) or for received audio (RX AGC-C)](set-compression-ratio-for-voice-tx-or-for-received-audio-rx-agc-c.md)
- [Apply make-up gain after compression](apply-make-up-gain-after-compression.md)
- [Watch live gain reduction while speaking or listening](watch-live-gain-reduction-while-speaking-or-listening.md)
- [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md)