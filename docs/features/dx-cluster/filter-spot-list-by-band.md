# Filter spot list by band

The Spot List tab in SpotHub shows a unified table of all live spots from every connected source. Use the per-band checkboxes to hide bands you are not interested in, keeping the table focused on the frequencies you care about.

## Steps

1. Open SpotHub: go to **Settings > SpotHub...** and click the **Spot List** tab.
2. Under **Bands:**, uncheck any band you want to hide from the table. Check it again to restore those spots.

## What each control does

| Control | Behavior |
|---|---|
| **Bands:** (checkboxes) | One checkbox per band: 160m, 80m, 60m, 40m, 30m, 20m, 17m, 15m, 12m, 10m, 6m. Unchecking a band hides all spots on that band from the spot table. Each band's state is saved individually (setting keys `SpotBandFilter_160m`, `SpotBandFilter_80m`, etc.). |
| **Spot table** | Sortable table showing spots that pass the active band filters. Double-click a row to tune to that frequency. Newest spots appear at the top; the table holds at most 500 spots. |
| **Clear** | Removes all spots from the current list regardless of band filter state. |

## Tips

- All band checkboxes default to checked (all bands visible). Uncheck only the bands you want to suppress — you do not need to change anything else.
- 2m spots (from FreeDV) bypass the band filter and are always visible in the table; there is no 2m checkbox.
- Band filter state is persisted between sessions, so your selection survives an application restart.
- The band filter affects only the Spot List table. Spot labels on the panadapter are controlled separately via the **Display** tab.

## Related

- [SpotHub overview](spothub.md)
- [Display spots on the panadapter](display-spots-panadapter.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
