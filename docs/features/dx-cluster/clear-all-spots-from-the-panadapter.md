# Clear all spots from the panadapter

Remove every spot currently shown on the panadapter in one action. Use this when the display is cluttered and you want to start fresh without disconnecting any spot sources.

## Before you start

- At least one spot source (DX cluster, RBN, WSJT-X, SpotCollector, POTA, or FreeDV) must have delivered spots, otherwise there is nothing to clear.
- Spots continue arriving from any connected or running source immediately after clearing, so sources remain active.

## Steps

1. Open `Settings > SpotHub...`.
2. Click the `Display` tab.
3. Click `Clear All Spots`.

All spots are removed from the panadapter and the spot list instantly. Connected sources are not disconnected and will continue delivering new spots.

## Tips

- To remove spots band by band rather than all at once, use the `Spot List` tab. Check or uncheck individual bands under `Bands:` to hide spots for a specific band without discarding them permanently.
- To clear only the spot list table, go to the `Spot List` tab and click `Clear`. This empties the table display but the effect on the panadapter overlay follows the same live spot data.
- If spots reappear immediately and you want a clean slate for longer, reduce `Spot Lifetime:` on the `Display` tab (`SpotsLifetime`) or disconnect the relevant source before clearing.

## Related

- [SpotHub overview](overview.md)
- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
- [Tune to a spot by double-clicking the spot list](tune-to-a-spot-by-double-clicking-the-spot-list.md)
