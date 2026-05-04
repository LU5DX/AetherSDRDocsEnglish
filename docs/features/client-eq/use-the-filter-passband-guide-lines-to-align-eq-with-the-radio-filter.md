# Use the filter passband guide lines to align EQ with the radio filter

The EQ curve area displays dashed yellow vertical guide lines marking the radio's active TX filter low/high cutoffs (TX path) or the RX slice passband edges (RX path), so you can see at a glance which EQ bands fall inside or outside the transmit or receive passband. In the floating editor you can also drag either guide line horizontally to move the radio filter cutoff in real time.

## Before you start

- Enable the matching EQ stage via the CHAIN widget or the floating editor so the docked tile is visible.
- Open the **Aetherial TX EQ** or **Aetherial RX EQ** sub-container inside the Aetherial Audio (TXDSP) parent container.

## Steps

1. Look at the **Analyzer / curve area** in the docked tile. Two dashed yellow vertical lines mark the active TX filter low/high cutoffs (TX path) or the RX slice passband edges (RX path). EQ bands whose center or corner frequencies fall between the lines are inside the passband; bands outside the lines are attenuated or cut by the radio filter.

2. To move a filter cutoff, double-click the EQ stage in the CHAIN widget to open the floating editor, then grab either dashed yellow guide line and drag it horizontally. The radio's TX filter cutoff or RX slice passband edge updates in real time as you drag. Release when the line aligns with the desired EQ band.

## What each control does

| Control | Behavior |
|---|---|
| **Analyzer / curve area** | Shows the summed EQ response, a live FFT analyzer with gradient fill, a peak-hold trace that decays ~10 dB/sec, and dashed yellow vertical guide lines at the active TX filter low/high cutoffs (TX path) or RX slice passband edges (RX path). Guide lines update automatically when the filter changes. View-only in the docked applet; guide lines are draggable in the floating editor. |
| **Peak Hold** | When checked, the per-bin peak-hold trace stops decaying — every frequency's highest observed level is held until toggled off. Located in the floating editor header strip. Amber background when checked; default is unchecked. |
| **Smoothing** | Applies fractional-octave smoothing to the analyzer trace display (Off / 1/24 / 1/12 / 1/6 / 1/3). Affects the visual FFT display only — EQ math and audio processing are unchanged. Default: Off (1/96). |
| **Filter family** | Selects the HP/LP cascade mathematics: Butterworth (maximally flat), Chebyshev (steeper rolloff, 1 dB ripple), Bessel (linear phase), or Elliptic (steepest transition, ripple in both bands). Applies only to HP and LP filter types. Default: Butterworth. |
| **Output Fader** | Sets post-EQ master gain from −36.0 to +12.0 dB. Drag to set; scroll wheel adjusts in 0.5 dB steps; double-click resets to 0 dB. The level bar shows smoothed post-EQ peak in real time. Located in the floating editor only. |
| **Reset** | Resets all bands to the default 10-band template, restores the default band count, and resets Filter family to Butterworth. Saves immediately. |

## Tips

- Use **Peak Hold** while tuning to freeze the analyzer trace at maximum observed levels — this makes it easy to identify resonances that extend outside the filter passband guide lines before you cut them.
- Apply **Smoothing** (1/6 or 1/3) if the FFT trace is noisy, to make it easier to see the broad shape of the signal relative to the guide lines.
- The guide lines update automatically whenever the radio filter changes — you do not need to reopen the editor.
- Dragging a guide line in the floating editor updates the radio filter cutoff directly; you do not need to use the radio's filter controls separately.

## Related

- [Aetherial Parametric EQ overview](aetherial-parametric-eq.md)
- [Set post-EQ output gain with the Output Fader](eq-output-fader.md)
- [Freeze the analyzer peak-hold trace](eq-peak-hold.md)
<!-- docmesh:llm version=v0.9.5.1 date=2026-05-04 -->
