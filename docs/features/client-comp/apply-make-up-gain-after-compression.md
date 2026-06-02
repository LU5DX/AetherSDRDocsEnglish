# Apply make-up gain after compression

Make-up gain compensates for the overall level lost when the compressor reduces peaks. Adjust the Makeup knob on the TX or RX side so that compressed audio comes out at a consistent, useful level.

## Before you start

- The Aetherial Compressor (TX) or Aetherial AGC-C (RX) applet must be visible. Each tile stays hidden until its stage is enabled via the CHAIN widget.
- The compressor must be enabled (not bypassed) on the side you want to adjust. Make-up gain has no audible effect when the compressor is bypassed. When a stage is bypassed, the entire applet tile dims to approximately 55 % opacity as a visual indicator that the compressor is out of the signal path.

## Steps

1. Locate the "Aetherial Compressor" tile (TX side) or "Aetherial AGC-C" tile (RX side) in the Aetherial Audio (TXDSP) parent container.
2. Find the **Makeup** knob — the rightmost knob in the five-knob row at the bottom of the applet.
3. Turn the **Makeup** knob to the desired value. Positive values are displayed with an explicit `+` sign (for example, `+6.0 dB`); negative values display without one (for example, `-3.0 dB`). To type a value directly, click the knob's value label — a small inline editor appears with a cyan border. Type the desired number (for example `6.0`) and press **Enter** or click elsewhere to commit. The knob snaps to the entered value, clamped to the valid range.
4. Watch the gain-reduction bar while speaking (TX) or listening (RX). A good starting point is to add make-up gain equal to roughly half the gain reduction shown on the bar.

## What each control does

| Control     | Default  | Valid range     | Behavior                                                                                                                                                                                                                                                                                                                    |
|-------------|----------|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Thresh      | -18.0 dB | -60.0 to 0.0 dB | Linear mapping. Sets the level above which compression starts. Label formatted as '-18.0 dB'.                                                                                                                                                                                                                               |
| Ratio       | 3.0      | 1.0 to 20.0     | Logarithmic mapping (1 * 20^n). Sets how hard peaks are held once threshold is crossed. Label formatted as 'X.XX:1'.                                                                                                                                                                                                        |
| Attack      | 20.0 ms  | 0.1 to 300.0 ms | Exponential mapping (0.1 * 3000^n). Sets how quickly the compressor clamps down after the threshold is crossed. Label formatted 'X.X ms' below 10, 'X ms' above.                                                                                                                                                           |
| Release     | 200 ms   | 5 to 2000 ms    | Exponential mapping (5 * 400^n). Sets how quickly gain returns after the input drops back below threshold. Label formatted 'X ms'.                                                                                                                                                                                          |
| Makeup (TX) | 0.0 dB   | -12.0 to +24.0 dB | Linear mapping. Adds back gain lost to compression. Label shows explicit '+' sign for positive values.                                                                                                                                                                                                                      |
| Makeup (RX) | 0.0 dB   | -12.0 to +24.0 dB | Linear mapping. Adds back gain lost to compression. Label shows explicit '+' sign for positive values.                                                                                                                                                                                                                      |
| Drive       | 0.0 dB   | 0.0 to 18.0 dB | Pre-comp gain boost with linked auto-makeup. Pushes more signal across the threshold so the compressor engages harder, and simultaneously adds equal gain at the output so average RMS lifts alongside peaks rather than dropping. Pair with Phase to keep peaks clean. Displayed in the floating StripCompPanel only (right column). Label shows as '+X.X dB'. Tooltip explains #2887 PAPR reduction pairing. Auto-makeup matches the broadcast-Optimod model — Drive pushes more material into the curve AND adds equal gain back, so the user's fixed Makeup stays a clean post-everything trim knob. |
| Phase       | 0 stages | 0 to 6 stages  | Number of cascaded all-pass sections (0 = off). Each stage adds 12 dB/oct of phase rotation at staggered frequencies (300/700/1500/2500 Hz, plus optional 1000/2000 Hz). Symmetrizes asymmetric voice peaks before compression to reduce PAPR. Displayed in the floating StripCompPanel only (right column). Label 'Off' when 0, 'N stg' when active. Tooltip: 'Pre-comp phase rotator (#2887). All-pass cascade that symmetrizes asymmetric voice peaks before compression. 0 = off, 4 = broadcast default.' Default centres (300/700/1500/2500 Hz with optional 1000/2000 Hz) cover the speech formant range without bunching. |

The **Makeup** knob uses a linear mapping. It adds a fixed amount of gain after the compressor stage. It does not affect the threshold, ratio, or any other compressor parameter.

## Tips

- Watch the gain-reduction bar while transmitting or listening. If the bar regularly sits at or beyond the `-6 dB` tick, you are applying significant compression; consider adding make-up gain in the `+4.0` to `+10.0 dB` range to recover loudness.
- Make-up gain is applied before the limiter stage (if enabled). If you add a large make-up value and the output clips, enable the limiter and set an appropriate ceiling. See [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md).
- The TX and RX sides store their make-up values independently. Adjusting one does not affect the other.
- The transfer curve in the applet now uses a cached text label system that adapts to compact mode. When the applet is in compact mode, axis labels use a smaller 7-pixel font instead of 9 pixels. The labels themselves remain the same — they show the major tick values (for example, -60, -40, -20, 0) along the axes.
- Inline editing also works on the Thresh, Ratio, Attack, and Release knobs. Click any knob's value label to type a precise numeric value. Press **Enter** or tab away to commit, or press **Escape** to cancel and revert.
- The transfer curve, grid lines, and envelope ball colors now follow the active application theme. The curve uses the theme accent color, grid lines use background colors, the ball glow uses the warning accent, and the ball core uses the primary text color. This ensures the compressor display adapts to your chosen color scheme.
- The gain-reduction meter (slider fill) also uses the theme slider foreground color, giving a consistent amber appearance that matches the overall visual theme.

## Troubleshooting

- **Makeup knob has no audible effect** — The compressor stage is likely bypassed. The applet tile will appear dimmed (roughly 55 % opacity) when bypassed. Re-enable it via the CHAIN widget so the compressor is in the signal path. See [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md).
- **Output is louder but peaks are clipping** — The make-up value combined with your signal level is exceeding headroom. Reduce **Makeup**, or open the full editor and enable the limiter with a suitable ceiling. See [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md).
- **Inline editor accepts a value but the knob doesn't change** — The entered value may be outside the valid range. Values are clamped silently; check the knob label to confirm the resulting value. If the knob behaves unexpectedly, try entering a simpler number (for example `6` instead of `6.0`).

## Related

- [Aetherial Compressor (TX) / Aetherial AGC-C (RX) overview](overview.md)
- [Watch live gain reduction while speaking or listening](watch-live-gain-reduction-while-speaking-or-listening.md)
- [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md)
- [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md)