# Aetherial Compressor (TX) / Aetherial AGC-C (RX)

Client-side dynamic-range compressor. The applet instantiates one TX-bound copy ("Aetherial Compressor") and one RX-bound copy ("Aetherial AGC-C") with fully independent state. Both show the static transfer curve with a live "ball" riding on the current envelope, a horizontal gain-reduction meter (20 dB max), and five tuning knobs — Thresh, Ratio, Attack, Release, Makeup — so you can tame voice peaks (TX) or audio peaks (RX) without opening the floating editor. The floating StripCompPanel (double-click the CHAIN widget COMP tile) adds Knee, Ceiling, Makeup, a Limiter enable/disable button, a pre-comp Drive knob (0–18 dB) with auto-makeup gain linked to Drive (RMS lifts alongside peaks), and a Phase Rotator knob (0–6 all-pass stages at staggered 300/700/1500/2500 Hz with optional 1000/2000 Hz, broadcast default 4) for peak-to-average-power-ratio (PAPR) reduction.

## Controls in the compact applet tile

| Control | Kind | Default | Valid range | Setting key | Behavior |
|---------|------|---------|-------------|-------------|----------|
| Transfer curve | indicator | — | — | — | Compact-mode ClientCompCurveWidget. Draws the input/output transfer curve plus a live ball showing the current envelope level. View-only in the applet; editable in the floating ClientCompEditor. |
| Gain-reduction bar | meter | — | 0 to 20 dB GR | — | Horizontal amber strip, right-filled. Scale maxes at 20 dB reduction; a tick at -6 dB marks a typical working amount. Polled at ~30 Hz from `ClientComp::gainReductionDb()`; MeterSmoother ballistics (125 Hz animation, 30 ms attack / 180 ms release) make the fill read identically across all metering surfaces. |
| Thresh | knob | -18.0 dB | -60.0 to 0.0 dB | `ClientCompTxThresholdDb` | Linear mapping. Sets the level above which compression starts. Label formatted as "-18.0 dB". |
| Ratio | knob | 3.0 | 1.0 to 20.0 | `ClientCompTxRatio` | Logarithmic mapping (1 * 20^n). Sets how hard peaks are held once threshold is crossed. Label formatted as "X.XX:1". |
| Attack | knob | 20.0 ms | 0.1 to 300.0 ms | `ClientCompTxAttackMs` | Exponential mapping (0.1 * 3000^n). Sets how quickly the compressor clamps down after the threshold is crossed. Label formatted "X.X ms" below 10, "X ms" above. |
| Release | knob | 200 ms | 5 to 2000 ms | `ClientCompTxReleaseMs` | Exponential mapping (5 * 400^n). Sets how quickly gain returns after the input drops back below threshold. Label formatted "X ms". |
| Makeup | knob | 0.0 dB | -12.0 to 24.0 dB | `ClientCompTxMakeupDb` | Linear mapping. Adds back gain lost to compression. Label shows explicit "+" sign for positive values. |

## Indicators

| Indicator | States | Meaning |
|-----------|--------|---------|
| Envelope ball | resting at threshold line, moving along curve | Live input level plotted against the static transfer curve. |
| Gain-reduction strip | empty, amber fill, -6 dB tick | Amount of dynamic attenuation currently applied by the compressor. |

## Drive the compressor harder with pre-comp gain for PAPR reduction (auto-makeup linked)

Use the Drive knob to push more signal into the compressor before the threshold, then automatically get that gain back at the output. This lets you run the compressor harder — increasing peak-to-average-power-ratio (PAPR) reduction — while keeping your average RMS level unchanged so you don't have to re-adjust your Makeup knob.

### Before you start

- Confirm the TX compressor is enabled (click the compressor tile in the CHAIN widget so it shows as active, not dimmed).
- Open the floating StripCompPanel by double-clicking the COMP tile in the TX side of the CHAIN widget.

### Steps

1. Locate the Drive knob on the right column of the floating StripCompPanel (labelled as `+X.X dB`).
2. Turn Drive clockwise from its default `0.0 dB` (range: `0.0` to `18.0 dB`). Each dB of Drive pushes more signal above the threshold, so the compressor clamps down harder on peaks.
3. Optionally pair Drive with the Phase Rotator knob (also on the right column).

The compressor's gain-reduction meter and the live ball on the transfer curve will show more activity as Drive increases. The auto-makeup ensures your output level doesn't drop as compression increases, so your Makeup knob remains a clean post-everything trim.

## Controls in the floating StripCompPanel (double-click COMP tile)

| Control | Kind | Default | Valid range | Setting key | Behavior |
|---------|------|---------|-------------|-------------|----------|
| Drive | knob | 0.0 dB | 0.0 to 18.0 dB | `ClientCompTxDriveDb` | Pre-comp gain boost with linked auto-makeup. Pushes more signal across the threshold so the compressor engages harder, and simultaneously adds equal gain at the output so average RMS lifts alongside peaks rather than dropping. Label shows as "+X.X dB". Tooltip explains #2887 PAPR reduction pairing. Auto-makeup matches the broadcast-Optimod model — Drive pushes more material into the curve AND adds equal gain back, so the user's fixed Makeup stays a clean post-everything trim knob. |
| Phase | knob | 0 stages | 0 to 6 stages | `ClientCompTxPhaseRotatorStages` | Number of cascaded all-pass sections (0 = off). Each stage adds 12 dB/oct of phase rotation at staggered frequencies (300/700/1500/2500 Hz, plus optional 1000/2000 Hz). Symmetrizes asymmetric voice peaks before compression to reduce PAPR. Label "Off" when 0, "N stg" when active. Tooltip: "Pre-comp phase rotator (#2887). All-pass cascade that symmetrizes asymmetric voice peaks before compression. 0 = off, 4 = broadcast default." Default centres (300/700/1500/2500 Hz with optional 1000/2000 Hz) cover the speech formant range without bunching. |

## What each control does

| Control | Default | Valid range |
|---------|---------|-------------|
| Drive | `0.0 dB` | `0.0` to `18.0 dB` |
| Phase | `0 stages` | `0` to `6 stages` |
| Thresh | `-18.0 dB` | `-60.0` to `0.0 dB` |
| Ratio | `3.0` | `1.0` to `20.0` |
| Attack | `20.0 ms` | `0.1` to `300.0 ms` |
| Release | `200 ms` | `5` to `2000 ms` |
| Makeup | `0.0 dB` | `-12.0` to `24.0 dB` |

## Tips

- Drive is designed to be used *before* you touch Makeup. With auto-makeup active, you can increase Drive to get harder compression without losing average level.
- The Phase Rotator's default broadcast setting is 4 stages. Start there and listen for cleaner, more symmetrical peaks.
- The Drive knob is only available in the floating StripCompPanel — it does not appear in the compact applet tile.

## Related

- [Open the full Compressor editor for knee, limiter, Drive, and Phase controls](open-the-full-compressor-editor-for-knee-limiter-drive-and-phase-controls.md)
- [Rotate voice phase symmetry with the Phase rotator (0–6 stages at staggered frequencies)](rotate-voice-phase-symmetry-with-the-phase-rotator-0-6-stages-at-staggered-frequencies.md)
- [Adjust compressor threshold (TX or RX side)](adjust-compressor-threshold-tx-or-rx-side.md)
- [Apply make-up gain after compression](apply-make-up-gain-after-compression.md)