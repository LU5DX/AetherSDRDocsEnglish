# Align the client-side EQ guide lines with the TX audio filter edges

The TransmitModel tracks the TX audio filter edges and fires a dedicated signal whenever the low or high cutoff changes, allowing EQ applets to redraw their guide lines to match. Use the **Low Cut** and **High Cut** controls to set the filter boundaries; the EQ guide lines update automatically.

## Steps

1. In the TX panel, set **Low Cut** to the desired low-frequency cutoff in Hz. Step buttons snap to the nearest 50 Hz multiple; the default is 50 Hz.
2. Set **High Cut** to the desired high-frequency cutoff in Hz. Step buttons snap to the nearest 50 Hz multiple; the default is 3300 Hz.

The EQ applet guide lines reposition immediately after each change to reflect the current filter edges.

## What each control does

| Control | Behavior | Notes |
|---|---|---|
| **Low Cut** | Sets the TX audio low-frequency cutoff in Hz. Step buttons snap to the nearest 50 Hz multiple. Both `filter_low` and `filter_high` are always sent together when this value changes. Default: 50 Hz. Valid range: 0–10000 Hz. |  |
| **High Cut** | Sets the TX audio high-frequency cutoff in Hz. Step buttons snap to the nearest 50 Hz multiple. Both `filter_low` and `filter_high` are always sent together when this value changes. Default: 3300 Hz. Valid range: 0–10000 Hz. |  |
## Tips

- Both filter edges are sent to the radio as a pair every time either value changes, so adjusting one control also re-confirms the other. Set both to your target values before transmitting to avoid intermediate filter states.
- The EQ guide lines update client-side as soon as the TransmitModel fires its filter-change signal; no additional action is required to synchronize the display.

## Related

- [transmit-model.md](transmit-model.md)
- [tx-audio-settings.md](tx-audio-settings.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
