# Drag a filter cutoff guide line to set the TX or RX filter edge

The Aetherial Parametric EQ (TX / RX) displays dashed yellow vertical guide lines marking the active TX filter low/high cutoffs or the RX slice passband edges. In the floating editor you can drag either guide line horizontally to update the radio's filter setting in real time.

## Before you start

- Open the floating EQ editor for the path you want to adjust. Double-click the EQ stage in the CHAIN widget (TX or RX side) to open the frameless editor titled **Aetherial Parametric EQ — TX** or **— RX**.
- Confirm the filter guide lines are visible in the analyzer area — they appear as faint dashed yellow vertical lines. If no filter is set, the lines are hidden (stored frequency is 0 Hz).

## Steps

1. In the floating editor, locate the **Analyzer / curve area** — the main display showing the EQ response curve, FFT overlay, and the dashed yellow filter guide lines.
2. Click and drag either dashed yellow guide line horizontally to the desired cutoff frequency. The radio's TX filter cutoff (TX path) or the active RX slice passband edge (RX path) updates in real time as you drag.

## What each control does

| Control | Behavior |
|---|---|
| **Analyzer / curve area** | Displays the summed EQ response, live FFT analyzer with filled-gradient overlay, a peak-hold trace, and dashed yellow vertical guide lines at the active filter cutoff frequencies. In the floating editor, grab either dashed yellow line and drag horizontally to set the TX filter cutoff (TX path) or the RX slice passband edge (RX path) in real time. |
| **Filter passband guide lines** | TX path: marks the radio's current TX filter low/high cutoffs. RX path: marks the active slice's passband edges. Updated automatically whenever the filter changes. Dragging either line emits `cutoffsDragRequested` and applies the change immediately. Hidden when the stored frequency is 0 Hz. |

## Tips

- The guide lines are draggable **only in the floating editor** — the docked applet tile is view-only.
- Watch the guide lines relative to your EQ bands to confirm that key boosts or cuts fall inside the transmit or receive passband.
- The guide lines update automatically whenever the filter changes from another part of the UI, so you can also use them as a passive reference while adjusting other settings.

## Related

- [aetherial-parametric-eq.md](aetherial-parametric-eq.md)
- [set-tx-filter-cutoff.md](set-tx-filter-cutoff.md)
- [set-rx-slice-passband.md](set-rx-slice-passband.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
