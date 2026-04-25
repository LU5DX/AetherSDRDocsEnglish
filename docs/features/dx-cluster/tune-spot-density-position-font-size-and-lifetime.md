# Tune spot density, position, font size and lifetime

The Display tab in SpotHub controls how spot labels appear on the panadapter: how many stack vertically, where they sit, how large the text is, and how long each spot lives before it fades. Adjust these settings to reduce clutter on a busy band or make spots more readable on a small screen.

## Before you start

- AetherSDR must be running. A radio connection is not required to change these settings.
- At least one spot source (DX cluster, RBN, WSJT-X, SpotCollector, POTA, or FreeDV) should be active so you can see the effect of your changes in real time.
- The master spot overlay must be on. On the Display tab, confirm `IsSpotsEnabled` is active (the "Spots:" toggle reads Enabled).

## Steps

1. Open `Settings > SpotHub...`.
2. Click the **Display** tab.
3. Confirm **Spots:** is set to Enabled. If it is not, click it to enable the overlay.
4. To control how many spots stack vertically before they start overlapping, drag the **Levels:** slider. Higher values allow more rows of spot labels.
5. To move the spot labels up or down on the panadapter, drag the **Position:** slider.
6. To change the text size of spot labels, drag the **Font Size:** slider.
7. To set how long a spot remains visible before it disappears, drag the **Spot Lifetime:** slider. The value is in seconds.
8. If you want AetherSDR to automatically adjust spot density based on the current panadapter zoom level, click **Auto Mode:** to enable it. When Auto Mode is on, the **Levels:** slider has no effect.
9. Close the dialog. Changes take effect immediately.

## What each control does

| Control | Setting key | Behavior | Default | Range/Units |
|---|---|---|---|---|
| **Spots:** | `IsSpotsEnabled` | Master toggle for the spot overlay on the panadapter. | Enabled | On / Off |
| **Auto Mode:** | `SpotsAutoMode` | Automatically adjusts spot density based on zoom level. Overrides Levels. | — | On / Off |
| **Levels:** | `SpotsStackLevels` | Number of vertical stacking rows for spot labels. | — | Slider |
| **Position:** | `SpotsPosition` | Vertical position of the spot label band on the panadapter. | — | Slider |
| **Font Size:** | `SpotsFontSize` | Size of the text in each spot label. | — | Slider |
| **Spot Lifetime:** | `SpotsLifetime` | Seconds a spot label remains visible before fading. | — | Seconds (slider) |

## Tips

- If spot labels overlap badly on a crowded band, increase **Levels:** to add more stacking rows, or decrease **Spot Lifetime:** so old spots clear sooner.
- **Auto Mode:** is useful when you switch between zoomed-in and zoomed-out views frequently. Disable it if you want manual control over density.
- WSJT-X spots have their own per-source lifetime setting (**Spot Life:** on the WSJT-X tab, stored as `WsjtxSpotLife`). The **Spot Lifetime:** slider on the Display tab applies to all other sources.

## Troubleshooting

- **Spot labels are not visible at all** — Check that **Spots:** on the Display tab is set to Enabled (`IsSpotsEnabled`). Also confirm at least one spot source is connected and receiving spots.
- **Changing Levels: has no effect** — **Auto Mode:** is likely enabled. Click **Auto Mode:** to disable it, then adjust **Levels:** manually.

## Related

- [SpotHub overview](overview.md)
- [Pick colors for each spot source](pick-colors-for-each-spot-source.md)
- [Clear all spots from the panadapter](clear-all-spots-from-the-panadapter.md)
- [Start WSJT-X UDP listener and filter for CQ, POTA or calls to me](start-wsjt-x-udp-listener-and-filter-for-cq-pota-or-calls-to-me.md)
