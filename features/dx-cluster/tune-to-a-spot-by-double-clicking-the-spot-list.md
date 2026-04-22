# Tune to a spot by double-clicking the spot list

The Spot List tab in SpotHub shows a unified, sortable table of all live spots from every connected source. Double-clicking a row tunes the active receiver to that spot's frequency.

## Before you start

- At least one spot source must be active and delivering spots (DX cluster, RBN, WSJT-X, SpotCollector, POTA, or FreeDV). See the related pages below for setup instructions.
- The radio must be connected to AetherSDR.

## Steps

1. Open `Settings > SpotHub...`.
2. Click the `Spot List` tab.
3. Optionally, use the `Bands:` checkboxes to limit which bands appear in the table. Uncheck any band you do not want to see.
4. Click a column header to sort the table — for example, click `Freq (kHz)` to sort by frequency or `DX Call` to sort alphabetically.
5. Locate the spot you want to work.
6. Double-click that row. AetherSDR tunes the active receiver to the frequency shown in the `Freq (kHz)` column.

## What each control does

| Control | Behavior | Setting key |
|---|---|---|
| `Bands:` checkboxes | Per-band toggles. Unchecking a band hides its spots from the table. Does not affect panadapter display. | — |
| `Clear` | Empties the spot list immediately. | — |
| Spot table | Sortable table with columns: Time, Freq (kHz), DX Call, Mode, Comment, Spotter, Band, Source. Double-click any row to tune. | — |

## Tips

- Sort by `Time` (descending) to see the most recently received spots at the top. New spots are prepended, so the default sort already places them first.
- Sort by `Band` to compare activity across bands before deciding where to operate.
- If you expect spots but the table is empty, check that the band in question is not filtered out by the `Bands:` checkboxes.

## Troubleshooting

- **Double-clicking a row does nothing** — Verify the radio is connected. The tune action requires an active radio connection even though SpotHub itself does not.
- **Table is empty despite a connected source** — Confirm the source is shown as Connected, Listening, or Polling on its tab. Also confirm that the relevant band checkboxes are checked.
- **A spot's band column is blank** — The spot frequency falls outside the recognized amateur band edges. The row still appears and double-clicking it still tunes.

## Related

- [SpotHub overview](overview.md)
- [Connect to a DX cluster](../../getting-started/setup/connect-to-a-dx-cluster.md)
- [Connect to the Reverse Beacon Network](../../getting-started/setup/connect-to-the-reverse-beacon-network.md)
- [Start WSJT-X UDP listener and filter for CQ, POTA or calls to me](start-wsjt-x-udp-listener-and-filter-for-cq-pota-or-calls-to-me.md)
- [Poll POTA activations](poll-pota-activations.md)
- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
