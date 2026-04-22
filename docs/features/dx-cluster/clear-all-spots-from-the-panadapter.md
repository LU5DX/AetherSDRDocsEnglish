# Clear all spots from the panadapter

Remove every spot currently tracked by AetherSDR from the panadapter in one action. Use this when the display is cluttered after a band change or after toggling spot sources.

## Before you start

- At least one spot source (DX cluster, RBN, WSJT-X, SpotCollector, POTA, or FreeDV) must have delivered spots for there to be anything to clear.
- The SpotHub dialog must be accessible via the menu (no radio connection required).

## Steps

1. Click `Settings > SpotHub...` to open the SpotHub dialog.
2. Click the `Spot List` tab.
3. Click `Clear All Spots`.

All spots are immediately removed from the panadapter and from the spot table. Connected sources continue running and will populate new spots as they arrive.

## Tips

- `Clear All Spots` removes spots from the live tracking list across all sources at once. It does not disconnect any source or change any display settings.
- If you want to remove spots only from the table view without affecting the panadapter overlay, use the `Clear` button on the `Spot List` tab instead. That button empties the table display only.
- To stop new spots from appearing on the panadapter without disconnecting your sources, toggle `Spots:` to disabled on the `Display` tab (`IsSpotsEnabled`).

## Related

- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
- [Tune to a spot by double-clicking the spot list](tune-to-a-spot-by-double-clicking-the-spot-list.md)
- [SpotHub overview](overview.md)
