# Use the filter passband guide lines to align EQ with the radio filter

The Aetherial Parametric EQ (TX / RX) displays dashed yellow vertical guide lines on the analyzer marking the radio's active filter cutoff frequencies. Use these lines to see immediately which EQ bands fall inside or outside the transmit or receive passband, and drag the lines to adjust the radio filter without leaving the EQ editor.

## Before you start

- Enable the matching EQ stage via the CHAIN widget or by double-clicking the EQ stage in the CHAIN widget to open the floating editor.
- Confirm the radio filter is set to the desired mode — the guide lines reflect the current filter automatically.

## Steps

1. Open the floating EQ editor by double-clicking the EQ stage in the CHAIN widget (TX or RX side). The **Analyzer / curve area** displays two dashed yellow vertical lines at the active TX filter low/high cutoffs (TX path) or the RX slice passband edges (RX path).
2. Compare the position of your EQ bands against the guide lines. Bands between the two lines are inside the passband; bands outside are attenuated by the radio filter.
3. To adjust the radio filter directly from the editor, grab either dashed yellow line and drag it horizontally. The radio's TX filter cutoff or RX slice passband edge updates in real time as you drag.
4. Optional — enable **Peak Hold** to freeze the analyzer trace while you tune, so you can see the highest level reached at each frequency without the trace decaying.
5. Optional — change **Smoothing** to reduce visual noise in the FFT trace and make the relationship between EQ bands and the passband edges easier to read.

## What each control does

| Control | Behavior |
|---|---|
| **Analyzer / curve area** | Shows the summed EQ response, live FFT analyzer with filled-gradient overlay, a peak-hold trace that decays ~10 dB/sec, and dashed yellow vertical guide lines at the active TX filter low/high cutoffs (TX path) or RX slice passband edges (RX path). Guide lines update automatically when the filter changes. In the floating editor, drag either guide line horizontally to set the radio's TX filter cutoff or RX slice passband edge in real time. |
| **Peak Hold** | When checked, the per-bin peak-hold trace stops decaying — every frequency's highest observed level is held until toggled off. Amber background when checked. Default: unchecked. |
| **Smoothing** | Applies fractional-octave smoothing to the FFT analyzer display only. Options: Off (1/96) / 1/24 / 1/12 / 1/6 / 1/3. Lower fractions produce a smoother trace. Does not affect EQ math or audio processing. Default: Off (1/96). |
| **Filter family** | Selects the HP/LP cascade mathematics used by the EQ. Options: Butterworth / Chebyshev / Bessel / Elliptic. Applies only to HP and LP filter types. Default: Butterworth. |
| **Output Fader** | Sets post-EQ master gain from −36 to +12 dB. Drag to set; scroll wheel adjusts in 0.5 dB steps; double-click resets to 0 dB. The level bar shows smoothed post-EQ peak in real time. Default: 0 dB. |
| **Reset** | Resets all bands to the default 10-band template, restores the default band count, and resets the filter family to Butterworth. Saves immediately. |

## Tips

- If the guide lines are not visible, the radio filter cutoff frequency may be stored as 0 Hz — check that the radio is connected and a filter is actively selected on the TX or RX slice.
- Use **Peak Hold** while transmitting or receiving to capture the loudest moments, then compare the frozen trace against the guide lines to spot energy that the radio filter will cut.
- The guide lines are path-specific: the TX EQ editor shows TX filter cutoffs; the RX EQ editor shows the active RX slice passband edges. Opening both editors side by side lets you align each independently.
- Dragging the guide lines is only available in the floating editor, not in the docked applet tile.

## Related

- [aetherial-parametric-eq.md](aetherial-parametric-eq.md)
- [chain-widget.md](chain-widget.md)
- [tx-filter-settings.md](tx-filter-settings.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
