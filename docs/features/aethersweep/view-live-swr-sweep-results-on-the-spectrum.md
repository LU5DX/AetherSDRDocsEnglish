# View live SWR sweep results on the spectrum

The Spectrum / Waterfall widget renders live FFT data for each panadapter and plots AetherSweep SWR scan results directly on the spectrum line. No separate window is needed — sweep data appears overlaid as soon as a scan completes.

## Before you start

- Connect to a radio and open at least one Panadapter applet.
- Run an AetherSweep SWR scan over the frequency range you want to inspect.

## Steps

1. Open a Panadapter applet. The Spectrum / Waterfall widget is always visible inside it.
2. Start or replay an AetherSweep SWR scan. Results are plotted directly on the spectrum as the sweep data arrives — no additional controls to activate.

## What each control does

| Control | Behavior |
|---|---|
| Waterfall colour scheme | Changes the gradient palette used to map signal intensity to waterfall colour. Options: Default (0), Grayscale (1), Blue-Green (2), Fire (3), Plasma (4). Setting is persisted per panadapter. |

## Tips

- If the SWR overlay is hard to read against a bright spectrum, switch the **Waterfall colour scheme** to **Grayscale** to reduce background colour noise and make the sweep trace stand out.
- Scroll the spectrum to zoom into the swept frequency range for a more detailed view of the SWR curve.

## Related

- [panadapter-applet.md](panadapter-applet.md)
- [aethersweep-swr-scan.md](aethersweep-swr-scan.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
