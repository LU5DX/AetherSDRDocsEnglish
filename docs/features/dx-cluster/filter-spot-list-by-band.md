# Filter spot list by band

The Spot List tab in SpotHub shows a unified table of all live spots from every connected source. Use the per-band checkboxes to hide or show spots for specific amateur bands.

## Steps

1. Open SpotHub: **Settings > SpotHub...**
2. Click the **Spot List** tab.
3. Under **Bands:**, check or uncheck the checkbox for each band you want to show or hide in the spot table.

## What each control does

| Control | Behavior | Notes |
|---|---|---|
| **Bands:** (per-band checkboxes) | Each checkbox toggles visibility of spots for that band in the spot table. Available bands: 160m, 80m, 60m, 40m, 30m, 20m, 17m, 15m, 12m, 10m, 6m. All checkboxes default to checked (all bands visible). |  |
| **Spot table** | Sortable table of spots from all sources. Displays only spots whose band is currently checked. Double-click a row to tune to that frequency. |  |
| **Clear** | Empties the current spot list immediately. |  |
## Tips

- Band filter settings persist across sessions. Each band is saved individually (e.g. `SpotBandFilter_40m`, `SpotBandFilter_20m`).
- 2m spots (from FreeDV) are always visible in the table regardless of filter state — there is no 2m checkbox.
- The table holds at most 500 spots. Uncheck rarely-used bands to reduce clutter when many sources are active.
- Filters affect only the Spot List table. Spots on the panadapter are controlled separately from the **Display** tab.

## Related

- [spothub-display-tab.md](spothub-display-tab.md)
- [spothub-overview.md](spothub-overview.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
