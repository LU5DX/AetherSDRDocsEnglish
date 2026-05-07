# Smooth the analyzer trace with fractional-octave smoothing

The Aetherial Parametric EQ analyzer trace can be smoothed using fractional-octave averaging, making broad spectral trends easier to read. Smoothing affects the visual FFT display only — EQ math and audio processing are unchanged.

## Before you start

- Open the floating EQ editor by double-clicking the EQ stage in the CHAIN widget (TX or RX side). The **Smoothing** control is available in the floating editor only, not the docked applet tile.

## Steps

1. In the floating editor header strip, locate the **Smoothing** combo box.
2. Select a fraction from the drop-down: **1/3** gives the most smoothing; **1/6**, **1/12**, and **1/24** give progressively less; **Off (1/96)** disables smoothing entirely.

The analyzer trace updates immediately. To remove smoothing, set **Smoothing** back to **Off (1/96)**.

## What each control does

| Control | Behavior |
|---|---|
| **Smoothing** | Applies fractional-octave smoothing to the analyzer trace display. Lower fractions produce a smoother curve. Affects the visual FFT display only — EQ math and audio processing are unchanged. Default: **Off (1/96)**. Options: Off (1/96) \| 1/24 \| 1/12 \| 1/6 \| 1/3. Persisted as `ClientEqSmoothingFraction`. Shared between TX and RX editor instances. |

## Tips

- The **Smoothing** setting is shared between the TX and RX editor instances — changing it in one editor changes it in the other.
- Use **1/3** when scanning for broad resonances or room modes; switch to **Off (1/96)** when you need to resolve narrow peaks precisely.
- Pair **Smoothing** with the **Peak Hold** button (in the same editor header strip) to capture transient peaks on a smoothed trace.

## Related

- [peak-hold-analyzer-trace.md](peak-hold-analyzer-trace.md)
- [parametric-eq-overview.md](parametric-eq-overview.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
