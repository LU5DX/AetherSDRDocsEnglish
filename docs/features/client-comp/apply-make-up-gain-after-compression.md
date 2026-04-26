# Apply make-up gain after compression

Make-up gain compensates for the overall level lost when the compressor reduces peaks. Adjust the Makeup knob on the TX or RX side so that compressed audio comes out at a consistent, useful level.

## Before you start

- The Aetherial Compressor (TX) or Aetherial AGC-C (RX) applet must be visible. Each tile stays hidden until its stage is enabled via the CHAIN widget.
- The compressor must be enabled (not bypassed) on the side you want to adjust. Make-up gain has no audible effect when the compressor is bypassed.

## Steps

1. Locate the "Aetherial Compressor" tile (TX side) or "Aetherial AGC-C" tile (RX side) in the Aetherial Audio (TXDSP) parent container.
2. Find the **Makeup** knob — the rightmost knob in the five-knob row at the bottom of the applet.
3. Turn the **Makeup** knob to the desired value. Positive values are displayed with an explicit `+` sign (for example, `+6.0 dB`); negative values display without one (for example, `-3.0 dB`).
4. Watch the gain-reduction bar while speaking (TX) or listening (RX). A good starting point is to add make-up gain equal to roughly half the gain reduction shown on the bar.

## What each control does

| Control | Default | Valid range | Persisted setting key |
|---------|---------|-------------|-----------------------|
| Makeup (TX) | `0.0 dB` | `-12.0` to `+24.0 dB` | `ClientCompTxMakeupDb` |
| Makeup (RX) | `0.0 dB` | `-12.0` to `+24.0 dB` | `ClientCompRxMakeupDb` |

The **Makeup** knob uses a linear mapping. It adds a fixed amount of gain after the compressor stage. It does not affect the threshold, ratio, or any other compressor parameter.

## Tips

- Watch the gain-reduction bar while transmitting or listening. If the bar regularly sits at or beyond the `-6 dB` tick, you are applying significant compression; consider adding make-up gain in the `+4.0` to `+10.0 dB` range to recover loudness.
- Make-up gain is applied before the limiter stage (if enabled). If you add a large make-up value and the output clips, enable the limiter and set an appropriate ceiling. See [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md).
- The TX and RX sides store their make-up values independently. Adjusting one does not affect the other.

## Troubleshooting

- **Makeup knob has no audible effect** — The compressor stage is likely bypassed. Re-enable it via the CHAIN widget so the compressor is in the signal path. See [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md).
- **Output is louder but peaks are clipping** — The make-up value combined with your signal level is exceeding headroom. Reduce **Makeup**, or open the full editor and enable the limiter with a suitable ceiling. See [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md).

## Related

- [Aetherial Compressor (TX) / Aetherial AGC-C (RX) overview](overview.md)
- [Watch live gain reduction while speaking or listening](watch-live-gain-reduction-while-speaking-or-listening.md)
- [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md)
- [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md)
