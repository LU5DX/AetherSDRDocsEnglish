# Tune to a Spot by Double-Clicking the Spot List

The Spot List tab in SpotHub shows every live spot from all active sources in a single sortable table. Double-clicking a row tunes the active VFO to that spot's frequency.

## Before you start

- At least one spot source (DX Cluster, RBN, WSJT-X, SpotCollector, POTA, or FreeDV) must be connected and receiving spots.
- The radio must be connected to AetherSDR.

## Steps

1. Open `Settings > SpotHub...`.
2. Click the "Spot List" tab.
3. Optionally, use the "Bands:" checkboxes to filter the table by band. Uncheck any bands you do not want to see.
4. Click a column header to sort the table by that column. Columns are: Time, Freq (kHz), DX Call, Mode, Comment, Spotter, Band, Source.
5. Double-click any row in the spot table. AetherSDR tunes the active VFO to the frequency shown in that row.

## What each control does

| Control | Behavior | Setting key |
|---|---|---|
| Bands: | Per-band checkboxes. Uncheck a band to hide its spots from the table. | — |
| Clear | Removes all spots currently shown in the table. | — |
| Spot table | Sortable table of all live spots. Double-click a row to tune. Columns: Time, Freq (kHz), DX Call, Mode, Comment, Spotter, Band, Source. | — |

## Tips

- Sort by "Freq (kHz)" to find spots near your current frequency.
- Sort by "Band" to group all spots on a given band together before double-clicking.
- Spots are added newest-first; the table holds a maximum of the most recent spots across all sources.
- Hiding bands with the "Bands:" checkboxes affects only the Spot List view, not the panadapter overlay.

## Related

- [SpotHub overview](overview.md)
- [Connect to a DX cluster](../../getting-started/setup/connect-to-a-dx-cluster.md)
- [Connect to the Reverse Beacon Network](../../getting-started/setup/connect-to-the-reverse-beacon-network.md)
- [Start WSJT-X UDP listener and filter for CQ, POTA or calls to me](start-wsjt-x-udp-listener-and-filter-for-cq-pota-or-calls-to-me.md)
- [Poll POTA activations](poll-pota-activations.md)
- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
