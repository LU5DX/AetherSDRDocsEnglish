# Tune to a spot by double-clicking the spot list

The Spot List tab in SpotHub shows a unified, sortable table of all live spots from every active source. Double-clicking a row tunes your radio's active slice to that spot's frequency.

## Before you start

- At least one spot source must be connected and delivering spots (DX cluster, RBN, WSJT-X, SpotCollector, POTA, or FreeDV).
- Your radio must be connected to AetherSDR.
- `IsSpotsEnabled` must be on if you also want to see spots on the panadapter, but it is not required for the spot list itself.

## Steps

1. Open `Settings > SpotHub...`.
2. Click the **Spot List** tab.
3. Optionally, use the **Bands:** checkboxes to hide bands you are not interested in. Unchecking a band removes those rows from the table.
4. Optionally, click any column header to sort the table. Columns are: Time, Freq (kHz), DX Call, Mode, Comment, Spotter, Band, Source.
5. Double-click the row for the spot you want. The active slice tunes to that frequency.

## What each control does

| Control | Behavior | Setting key |
|---|---|---|
| **Bands:** checkboxes | One checkbox per band (160m, 80m, 60m, 40m, 30m, 20m, 17m, 15m, 12m, 10m, 6m, 2m). Unchecking a band hides its spots from the table. | — |
| **Clear** | Empties the current spot list. | — |
| Spot table | Sortable table of all live spots. Double-click a row to tune. Columns: Time, Freq (kHz), DX Call, Mode, Comment, Spotter, Band, Source. | — |

## Tips

- Click the **Freq (kHz)** column header to sort by frequency, making it easier to find spots near your current operating frequency.
- Click the **Band** column header to group all spots on the same band together.
- New spots are prepended at the top of the table. If the list grows unwieldy, click **Clear** to remove all current entries without disconnecting any source.

## Related

- [SpotHub overview](overview.md)
- [Connect to a DX cluster](../../getting-started/setup/connect-to-a-dx-cluster.md)
- [Connect to the Reverse Beacon Network](../../getting-started/setup/connect-to-the-reverse-beacon-network.md)
- [Start WSJT-X UDP listener and filter for CQ, POTA or calls to me](start-wsjt-x-udp-listener-and-filter-for-cq-pota-or-calls-to-me.md)
- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
