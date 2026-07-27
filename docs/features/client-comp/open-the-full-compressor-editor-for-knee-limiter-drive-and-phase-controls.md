# Open the full Compressor editor for knee, limiter, Drive, and Phase controls

The compact Compressor applet (shown when you enable the COMP stage in the CHAIN widget) gives you five tuning knobs — Thresh, Ratio, Attack, Release, and Makeup — plus a transfer curve indicator and a horizontal gain-reduction meter (20 dB max). To access Knee, Limiter, Drive, and Phase controls, you need to open the floating StripCompPanel editor by double-clicking the COMP tile in the CHAIN widget.

## Before you start

- The COMP stage (TX side: "Aetherial Compressor", RX side: "Aetherial AGC-C") must be enabled in the CHAIN widget. If the tile is dimmed (bypassed), see [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md) to enable it first.
- The COMP tile must be visible in the CHAIN widget inside the Aetherial Audio (TXDSP) parent container.

## Steps

1. Locate the **COMP** stage tile in the CHAIN widget (TX or RX side).
2. **Double-click** the COMP tile.

   The floating editor opens with the title **"Aetherial Compressor — TX"** or **"— RX"**, depending on which side you double-clicked. It is a frameless panel with an 18 px gradient title bar, a grip glyph, and min/max/close controls.

3. In the editor, you will see:
   - **Left column**: the transfer curve (interactive, not view-only), Knee knob (soft-knee transition width), and Make-up knob.
   - **Right column (TX only)**: Drive knob (0–18 dB pre-comp gain with linked auto-makeup), Phase knob (0–6 all-pass stages), and a **Limiter** section with an **Enable** button and a Ceiling knob (sets the hard ceiling level).
   - **Right column (RX only)**: a **Limiter** section with an **Enable** button and a Ceiling knob.

4. Adjust any control. Changes take effect immediately — there is no separate "Apply" button.

5. Close the editor by clicking the **X** on the title bar, or minimize it (middle button) to keep it alive but out of the way.

## What each control does

| Label | Function | Default | Valid range |
|---|---|---|---|
| **Knee** (only in editor) | Soft-knee transition width. Adds a gradual onset of compression at the threshold point instead of an abrupt hard-knee switch. | — (see `ClientCompTxKneeDb`) | — (see `ClientCompTxKneeDb`) |
| **Limiter Enable** (only in editor) | Enables a hard-knee brickwall limiter that prevents peaks from exceeding the Ceiling value. Toggle button (checked = on). Persisted as `ClientCompTxLimEnabled` (TX) or `ClientCompRxLimEnabled` (RX). | Off | — |
| **Limiter Ceiling** (only in editor) | Absolute peak ceiling (dB) that the limiter enforces. Persisted as `ClientCompTxLimCeilingDb` (TX) or `ClientCompRxLimCeilingDb` (RX). | — | — |
| **Drive** (TX only, only in editor) | Pre-compression gain boost with linked auto-makeup. Pushes more signal across the threshold so the compressor engages harder, and simultaneously adds equal gain at the output so average RMS lifts alongside peaks rather than dropping. Pair with Phase to keep peaks clean. Persisted as `ClientCompTxDriveDb`. | 0.0 dB | 0.0 to 18.0 dB |
| **Phase** (TX only, only in editor) | Number of cascaded all-pass filter stages (0 = off). Each stage adds 12 dB/oct of phase rotation at staggered frequencies (300/700/1500/2500 Hz, plus optional 1000/2000 Hz). Symmetrizes asymmetric voice peaks before compression to reduce peak-to-average-power ratio (PAPR). Broadcast default is 4 stages. Persisted as `ClientCompTxPhaseRotatorStages`. | 0 stages (labeled "Off") | 0 to 6 stages |

## Tips

- The five knobs shown in the compact applet (Thresh, Ratio, Attack, Release, Makeup) and the Knee knob in the editor control the same underlying compressor parameters — the editor simply exposes them in a single panel alongside the advanced controls.
- The editor's transfer curve is interactive: you can drag the threshold point and the ratio angle directly on the curve graphic rather than turning knobs.
- Changes made in the editor are immediately reflected back in the compact applet's knobs and gain-reduction meter.
- The editor remembers its last position and size via `StripCompPanelGeometry`. If you want to reset it, you can clear that setting from the config file.
- The compact applet's theme adapts to the current color scheme. The transfer curve background, grid lines, axis labels, curve color, envelope ball glow, and ball core all use theme colors from the `color` palette.
- The gain-reduction meter and envelope ball animation refresh continuously while the compressor is active — the animation timer stops when the meter settles but continues repainting while the envelope ball is moving, ensuring the ball glides along the transfer curve without stutter.

## Related

- [Adjust compressor threshold (TX or RX side)](adjust-compressor-threshold-tx-or-rx-side.md)
- [Apply make-up gain after compression](apply-make-up-gain-after-compression.md)
- [Drive the compressor harder with pre-comp gain for PAPR reduction](drive-the-compressor-harder-with-pre-comp-gain-for-papr-reduction.md)
- [Rotate voice phase symmetry with the Phase rotator (0–6 stages)](rotate-voice-phase-symmetry-with-the-phase-rotator-0-6-stages.md)
- [Tune attack / release for a natural-sounding squeeze](tune-attack-release-for-a-natural-sounding-squeeze.md)
- [Watch live gain reduction while speaking or listening](watch-live-gain-reduction-while-speaking-or-listening.md)