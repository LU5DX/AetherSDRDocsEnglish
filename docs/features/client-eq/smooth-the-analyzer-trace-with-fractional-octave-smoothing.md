# Smooth the analyzer trace with fractional-octave smoothing

The Aetherial Parametric EQ includes a live FFT analyzer overlay on the curve display. Use the **Smoothing** combo box in the floating editor to apply fractional-octave smoothing to that trace, making it easier to read broad spectral trends without altering any EQ math or audio processing.

## Before you start

- Open the floating EQ editor for the TX or RX path by double-clicking the EQ stage in the CHAIN widget. The **Smoothing** control is available in the floating editor only — it does not appear in the docked applet tile.
- Confirm audio is passing through the path so the analyzer trace is active.

## Steps

1. In the floating editor header strip, locate the **Smoothing** combo box (default: **Off (1/96)**).
2. Select the desired smoothing fraction: **1/24**, **1/12**, **1/6**, or **1/3**. A lower fraction number produces a smoother curve; **1/3** gives the most smoothing. To return to full resolution, select **Off (1/96)**.

The analyzer trace updates immediately. EQ band math and audio output are not affected.

## What each control does

| Control | Behavior |
|---|---|
| **Smoothing** | Applies fractional-octave smoothing to the analyzer trace display. **Off (1/96)** = full resolution; **1/24**, **1/12**, **1/6**, **1/3** = progressively smoother curve. Affects the visual FFT display only — EQ math and audio processing are unchanged. Shared between the TX and RX editor instances. Persisted as `ClientEqSmoothingFraction`. |

## Tips

- Use **1/3** octave smoothing when you want to judge broad tonal balance and ignore fine spectral detail; use **1/24** or **Off** when hunting for narrow resonances or peaks.
- The **Smoothing** setting is shared between the TX and RX editors — changing it in one editor also changes it in the other.
- To reliably spot transient peaks at full resolution, keep **Smoothing** at **Off (1/96)** and use the **Peak Hold** button in the editor header strip to freeze the peak-hold trace instead.

## Related

- [Use peak hold to capture transient levels](peak-hold.md)
- [Select a filter family for HP/LP bands](filter-family.md)
- [Adjust post-EQ output gain](output-fader.md)
<!-- docmesh:llm version=v0.9.5.1 date=2026-05-04 -->
