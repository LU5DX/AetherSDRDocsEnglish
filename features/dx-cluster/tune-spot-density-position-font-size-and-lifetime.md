# Tune spot density, position, font size and lifetime

The Display tab in SpotHub controls how spots appear on the panadapter: how many stack vertically, where they sit, how large the text is, and how long each spot stays visible before fading. Adjust these settings to reduce clutter or to make spots easier to read at a glance.

## Before you start

- AetherSDR must be running. A radio connection is not required to adjust display settings.
- At least one spot source (DX cluster, RBN, WSJT-X, SpotCollector, POTA, or FreeDV) should be configured so you can see the effect of your changes live.
- The spot overlay must be enabled (`IsSpotsEnabled` set to Enabled) for spots to appear on the panadapter at all.

## Steps

1. Open `Settings > SpotHub...`.
2. Click the **Display** tab.
3. Confirm **Spots:** is set to Enabled. If not, click it to enable the overlay.
4. To control how many vertical rows spots can occupy, drag the **Levels:** slider. More levels allow more spots to stack without overlapping; fewer levels keep the overlay compact.
5. To let AetherSDR automatically adjust stacking density based on the current panadapter zoom level, click **Auto Mode:** to enable it. When Auto Mode is on, the **Levels:** slider has no effect.
6. To move the entire spot overlay up or down on the panadapter, drag the **Position:** slider.
7. To change the size of spot callsign text, drag the **Font Size:** slider.
8. To change how long a spot remains visible before it disappears, drag the **Spot Lifetime:** slider. The value is in seconds.

## What each control does

| Control | What it does | Persisted setting |
|---|---|---|
| **Spots:** | Master toggle for the spot overlay on the panadapter. Default: Enabled. | `IsSpotsEnabled` |
| **Auto Mode:** | When enabled, AetherSDR adjusts stacking density automatically based on zoom. Overrides **Levels:**. | `SpotsAutoMode` |
| **Levels:** | Number of vertical stacking rows for spots. Has no effect while Auto Mode is on. | `SpotsStackLevels` |
| **Position:** | Vertical position of the spot overlay on the panadapter. | `SpotsPosition` |
| **Font Size:** | Size of the callsign text drawn on each spot marker. | `SpotsFontSize` |
| **Spot Lifetime:** | Seconds a spot remains visible on the panadapter before fading. | `SpotsLifetime` |

## Tips

- If spots overlap each other at your usual zoom level, increase **Levels:** or enable **Auto Mode:** so AetherSDR can find the best stacking depth for the current view.
- If the overlay obscures signal detail, reduce **Levels:** to one or two rows and use **Position:** to push spots toward the top or bottom edge of the panadapter.
- WSJT-X has its own per-source lifetime control (**Spot Life:** on the WSJT-X tab, persisted as `WsjtxSpotLife`). The **Spot Lifetime:** slider on the Display tab applies to all other sources.

## Troubleshooting

- **Spots are connected but nothing appears on the panadapter** — Check that **Spots:** on the Display tab shows Enabled. If it is disabled, click it to turn the overlay on.
- **Changing Levels: has no visible effect** — **Auto Mode:** is likely enabled. Click **Auto Mode:** to disable it, then adjust **Levels:**.

## Related

- [SpotHub overview](overview.md)
- [Pick colors for each spot source](pick-colors-for-each-spot-source.md)
- [Clear all spots from the panadapter](clear-all-spots-from-the-panadapter.md)
- [Enable DXCC coloring from an ADIF log](enable-dxcc-coloring-from-an-adif-log.md)
