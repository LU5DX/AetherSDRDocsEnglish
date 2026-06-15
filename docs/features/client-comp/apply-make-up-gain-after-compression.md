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

| Control     | Default  | Valid range       |
|-------------|----------|-------------------|
| Thresh      | -18.0 dB | -60.0 to 0.0 dB   |
| Ratio       | 3.0      | 1.0 to 20.0       |
| Attack      | 20.0 ms  | 0.1 to 300.0 ms   |
| Release     | 200 ms   | 5 to 2000 ms      |
| Makeup (TX) | 0.0 dB   | -12.0 to +24.0 dB |
| Makeup (RX) | 0.0 dB   | -12.0 to +24.0 dB |
| Drive       | 0.0 dB   | 0.0 to 18.0 dB    |
| Phase       | 0 stages | 0 to 6 stages     |

The **Makeup** knob uses a linear mapping. It adds a fixed amount of gain after the compressor stage. It does not affect the threshold, ratio, or any other compressor parameter.

The **Drive** and **Phase** knobs are available in the floating StripCompPanel only (double-click the CHAIN widget COMP tile). **Drive** adds pre-comp gain boost with linked auto-makeup, pushing more signal across the threshold while simultaneously adding equal gain at the output. This lifts average RMS alongside peaks rather than dropping it. **Phase** controls the number of cascaded all-pass sections (0 to 6 stages) for peak-to-average-power-ratio (PAPR) reduction. Each stage adds 12 dB/oct of phase rotation at staggered frequencies (300/700/1500/2500 Hz, plus optional 1000/2000 Hz) to symmetrize asymmetric voice peaks before compression. The default of 4 stages is the broadcast-Optimod standard.

## Tips

- Watch the gain-reduction bar while transmitting or listening. If the bar regularly sits at or beyond the `-6 dB` tick, you are applying significant compression; consider adding make-up gain in the `+4.0` to `+10.0 dB` range to recover loudness.
- Make-up gain is applied before the limiter stage (if enabled). If you add a large make-up value and the output clips, enable the limiter and set an appropriate ceiling. See [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md).
- The TX and RX sides store their make-up values independently. Adjusting one does not affect the other.
- The transfer curve in the applet now uses a cached text label system that adapts to compact mode. When the applet is in compact mode, axis labels use a smaller 7-pixel font instead of 9 pixels. The labels themselves remain the same — they show the major tick values (for example, -60, -40, -20, 0) along the axes.
- Inline editing also works on the Thresh, Ratio, Attack, and Release knobs. Click any knob's value label to type a precise numeric value. Press **Enter** or tab away to commit, or press **Escape** to cancel and revert.
- The transfer curve, grid lines, and envelope ball colors now follow the active application theme. The curve uses the theme accent color, grid lines use background colors, the ball glow uses the warning accent, and the ball core uses the primary text color. This ensures the compressor display adapts to your chosen color scheme.
- The gain-reduction meter (slider fill) also uses the theme slider foreground color, giving a consistent amber appearance that matches the overall visual theme.
- The envelope ball animation now uses a precise timer with improved rendering. When the compression envelope settles, the animation timer stops to save resources, and a single repaint ensures the display remains accurate. This means the ball may appear to jump to its final position rather than fading smoothly when compression stops.

## Troubleshooting

- **Makeup knob has no audible effect** — The compressor stage is likely bypassed. The applet tile will appear dimmed (roughly 55 % opacity) when bypassed. Re-enable it via the CHAIN widget so the compressor is in the signal path. See [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md).
- **Output is louder but peaks are clipping** — The make-up value combined with your signal level is exceeding headroom. Reduce **Makeup**, or open the full editor and enable the limiter with a suitable ceiling. See [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md).
- **Inline editor accepts a value but the knob doesn't change** — The entered value may be outside the valid range. Values are clamped silently; check the knob label to confirm the resulting value. If the knob behaves unexpectedly, try entering a simpler number (for example `6` instead of `6.0`).

## Related

- [Aetherial Compressor (TX) / Aetherial AGC-C (RX) overview](overview.md)
- [Watch live gain reduction while speaking or listening](watch-live-gain-reduction-while-speaking-or-listening.md)
- [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md)
- [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md)