# Tune to a spot by double-clicking the spot list

The Spot List in SpotHub displays all live spots from every connected source in a single sortable table. Double-clicking any row tunes the active slice receiver to that spot's frequency.

## Before you start

- At least one spot source must be active and delivering spots (DX cluster, RBN, WSJT-X, SpotCollector, POTA, or FreeDV). See [Connect to a DX cluster](../../getting-started/setup/connect-to-a-dx-cluster.md) if you have not set one up yet.
- The `IsSpotsEnabled` setting must be on if you also want spots visible on the panadapter, but it is not required to use the spot list for tuning.
- A radio must be connected and at least one slice receiver must be open.

## Steps

1. Open `Settings > SpotHub...`.
2. Click the **Spot List** tab.
3. Optionally, check or uncheck the **Bands:** checkboxes to restrict the table to the bands you care about.
4. Click a column header (for example, **Freq (kHz)** or **Band**) to sort the table by that column.
5. Double-click any row in the spot table.

The active slice receiver tunes to the frequency shown in the **Freq (kHz)** column of that row.

## What each control does

| Control | Description | Setting key |
|---|---|---|
| **Bands:** checkboxes | Per-band toggles. Hiding a band removes those rows from the table view; it does not delete the spots. | — |
| **Clear** | Empties the spot list for all sources immediately. | — |
| Spot table | Sortable table of all live spots. Columns: Time, Freq (kHz), DX Call, Mode, Comment, Spotter, Band, Source. Double-click a row to tune. | — |

## Tips

- The table is sortable by every column. Sorting by **Band** then scanning **Freq (kHz)** is a fast way to find activity on a specific band.
- Newest spots appear at the top of the unsorted table; the most recent spot for a given DX call is prepended when it arrives.
- The table holds a finite number of spots. Older spots are dropped from the bottom as new ones arrive. Use the **Bands:** filters to reduce clutter if the list fills quickly.
- Use the **Spot Lifetime:** slider on the **Display** tab (`SpotsLifetime`) to control how long spots remain visible on the panadapter after you have tuned away.

## Troubleshooting

- **Table is empty** — No spot source is connected or running. Check the **Cluster**, **RBN**, **WSJT-X**, **SpotCollector**, **POTA**, or **FreeDV** tabs and confirm the status indicator shows Connected, Listening, or Polling.
- **Double-click does nothing** — No radio is connected. Connect to a FLEX-8600 first via `Settings > Connect to Radio...`.
- **A band's spots are not visible** — The corresponding **Bands:** checkbox is unchecked. Re-check it to restore that band in the table.

## Related

- [SpotHub overview](overview.md)
- [Connect to a DX cluster](../../getting-started/setup/connect-to-a-dx-cluster.md)
- [Connect to the Reverse Beacon Network](../../getting-started/setup/connect-to-the-reverse-beacon-network.md)
- [Start WSJT-X UDP listener and filter for CQ, POTA or calls to me](start-wsjt-x-udp-listener-and-filter-for-cq-pota-or-calls-to-me.md)
- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
- [Clear all spots from the panadapter](clear-all-spots-from-the-panadapter.md)
