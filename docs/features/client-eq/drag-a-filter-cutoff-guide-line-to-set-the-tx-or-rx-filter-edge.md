# Drag a filter cutoff guide line to set the TX or RX filter edge

Open the floating EQ editor to drag either dashed yellow filter guide line horizontally and set the radio's TX filter cutoff or the active RX slice passband edge in real time.

## Before you start

- The floating EQ editor must be open. Double-click the EQ stage in the CHAIN widget (TX or RX side) to open it.
- At least one filter guide line must be visible in the curve area — guide lines appear as dashed yellow vertical lines only when a non-zero cutoff frequency has been set on the active path.

## Steps

1. In the floating **Aetherial Parametric EQ — TX** or **— RX** editor, locate the dashed yellow vertical line(s) in the **Analyzer / curve area** that mark the filter edge you want to move.
2. Click and drag either dashed yellow guide line horizontally to the target frequency. Release to confirm — the radio's TX filter cutoff (TX path) or the active RX slice passband edge (RX path) updates in real time.

## What each control does

| Control | Behavior |
|---|---|
| **Analyzer / curve area** | Displays the summed EQ response, live FFT analyzer with filled-gradient overlay, a peak-hold trace that decays ~10 dB/sec, and dashed yellow vertical guide lines at the active filter cutoff frequencies. In the floating editor, grab either guide line and drag horizontally to update the TX filter cutoff or the RX slice passband edge in real time. |
| **Peak Hold** | When checked, the per-bin peak-hold trace stops decaying and holds every frequency's highest observed level until toggled off. Background turns amber when active. |
| **Filter family** | Selects the HP/LP cascade mathematics applied to the filter: **Butterworth** (maximally flat passband), **Chebyshev** (steeper rolloff with 1 dB passband ripple), **Bessel** (linear phase, gentler rolloff), or **Elliptic** (steepest transition with ripple in both bands). Default: Butterworth. |
| **Smoothing** | Applies fractional-octave smoothing to the analyzer trace display (Off / 1/24 / 1/12 / 1/6 / 1/3). Affects the visual FFT display only — EQ math and audio processing are unchanged. Default: Off (1/96). |
| **Reset** | Resets all bands to the default 10-band template, restores the default band count, and resets the filter family to Butterworth. Saves immediately. |
| **Output Fader** | Vertical combined fader + level meter on the right edge of the floating editor. Drag to set post-EQ master gain (−36 to +12 dB); scroll wheel adjusts in 0.5 dB steps; double-click resets to 0 dB. Default: 0 dB. |

## Tips

- Dragging is only available in the **floating editor** — the docked applet tile shows the guide lines as view-only indicators.
- The guide lines update automatically whenever the filter changes externally (e.g. via the radio's filter controls), so the position you see always reflects the current radio state before you drag.
- Use the guide lines alongside the **Analyzer / curve area** to verify that your EQ shaping falls within the active passband — EQ energy outside the cutoffs is filtered out by the radio.

## Related

- [Aetherial Parametric EQ overview](client-eq-overview.md)
- [Set the TX or RX filter family](set-filter-family.md)
- [Freeze the analyzer peak-hold trace](freeze-peak-hold.md)
<!-- docmesh:llm version=v0.9.5.1 date=2026-05-04 -->
