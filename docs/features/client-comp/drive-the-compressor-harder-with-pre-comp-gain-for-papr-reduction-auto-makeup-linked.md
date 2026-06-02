# Drive the compressor harder with pre-comp gain for PAPR reduction (auto-makeup linked)

Use the Drive knob to push more signal into the compressor before the threshold, then automatically get that gain back at the output. This lets you run the compressor harder — increasing peak-to-average-power-ratio (PAPR) reduction — while keeping your average RMS level unchanged so you don't have to re-adjust your Makeup knob.

## Before you start

- Confirm the TX compressor is enabled (click the compressor tile in the CHAIN widget so it shows as active, not dimmed).
- Open the floating StripCompPanel by double-clicking the COMP tile in the TX side of the CHAIN widget.

## Steps

1. Locate the Drive knob on the right column of the floating StripCompPanel (labelled as `+X.X dB`).
2. Turn Drive clockwise from its default `0.0 dB` (range: `0.0` to `18.0 dB`). Each dB of Drive pushes more signal above the threshold, so the compressor clamps down harder on peaks.
3. Optionally pair Drive with the Phase Rotator knob (also on the right column) — see the related task for configuring phase rotation to further reduce PAPR.

The compressor’s gain-reduction meter and the live ball on the transfer curve will show more activity as Drive increases. The auto-makeup ensures your output level doesn’t drop as compression increases, so your Makeup knob remains a clean post-everything trim.

## What each control does

| Control | Default | Valid range | Setting key | Behavior |
|---|---|---|---|---|
| Drive | `0.0 dB` | `0.0` to `18.0 dB` | `ClientCompTxDriveDb` | Pre-comp gain boost with linked auto-makeup. Pushes more signal into the compressor and simultaneously adds equal gain at the output, so average RMS lifts alongside peaks rather than dropping. |
| Phase | `0 stages` | `0` to `6 stages` | `ClientCompTxPhaseRotatorStages` | Number of cascaded all-pass sections (0 = off). Symmetrizes asymmetric voice peaks before compression to reduce PAPR. Label shows "Off" when 0, "N stg" when active. |

## Tips

- Drive is designed to be used *before* you touch Makeup. With auto-makeup active, you can increase Drive to get harder compression without losing average level.
- The Phase Rotator’s default broadcast setting is 4 stages. Start there and listen for cleaner, more symmetrical peaks.
- The Drive knob is only available in the floating StripCompPanel — it does not appear in the compact applet tile.

## Related

- [Open the full Compressor editor for knee, limiter, Drive, and Phase controls](open-the-full-compressor-editor-for-knee-limiter-drive-and-phase-controls.md)
- [Rotate voice phase symmetry with the Phase rotator (0–6 stages at staggered frequencies)](rotate-voice-phase-symmetry-with-the-phase-rotator-0-6-stages-at-staggered-frequencies.md)
- [Adjust compressor threshold (TX or RX side)](adjust-compressor-threshold-tx-or-rx-side.md)
- [Apply make-up gain after compression](apply-make-up-gain-after-compression.md)
