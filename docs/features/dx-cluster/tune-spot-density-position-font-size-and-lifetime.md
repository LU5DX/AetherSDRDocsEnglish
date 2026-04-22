# Tune spot density, position, font size and lifetime

The Display tab in SpotHub controls how spots appear on the panadapter: how many stack vertically, where they sit, how large the text is, and how long they stay visible before fading. Adjust these settings to reduce clutter or improve readability on your screen.

## Before you start

- Open AetherSDR and confirm at least one spot source is active (DX cluster, RBN, WSJT-X, POTA, SpotCollector, or FreeDV).
- Confirm the spot overlay is not disabled — `IsSpotsEnabled` must be on (see the Spots toggle below).

## Steps

1. Open `Settings > SpotHub...`.
2. Click the **Display** tab.
3. Confirm **Spots:** is set to Enabled. If it shows Disabled, click it to toggle it on.
4. To let AetherSDR automatically adjust density as you zoom, click **Auto Mode:** to enable it. Skip steps 5–6 if you use Auto Mode.
5. To set density manually, drag the **Levels:** slider to the number of vertical stacking rows you want.
6. Drag the **Position:** slider to move the spot row up or down on the panadapter.
7. Drag the **Font Size:** slider to increase or decrease the spot label text size.
8. Drag the **Spot Lifetime:** slider to set how many seconds a spot remains visible before it fades.

## What each control does

| Control | Behavior | Setting key |
|---|---|---|
| **Spots:** | Master toggle for the panadapter spot overlay. Default: Enabled. | `IsSpotsEnabled` |
| **Auto Mode:** | Automatically adjusts spot density based on the current zoom level. | `SpotsAutoMode` |
| **Levels:** | Number of vertical stacking rows used when spots overlap at the same frequency. | `SpotsStackLevels` |
| **Position:** | Vertical position of the spot row on the panadapter. | `SpotsPosition` |
| **Font Size:** | Size of the text label drawn on each spot. | `SpotsFontSize` |
| **Spot Lifetime:** | Seconds a spot remains on the panadapter before it is removed. | `SpotsLifetime` |

Note: The **Display** tab also contains color override and DXCC coloring controls not covered here. See the related pages below.

## Tips

- When **Auto Mode:** is enabled, the **Levels:** slider has no effect. Disable **Auto Mode:** first if you want manual control over stacking density.
- If the panadapter looks crowded at wide zoom, reduce **Levels:** or increase **Spot Lifetime:** only as high as your spot rate requires. A shorter lifetime also reduces clutter when spot rate is high.
- WSJT-X spots have their own independent lifetime set via **Spot Life:** on the **WSJT-X** tab, stored in `WsjtxSpotLife`. The **Spot Lifetime:** slider on the Display tab applies to all other sources.

## Troubleshooting

- **No spots visible on the panadapter despite active connections** — Check that **Spots:** on the Display tab is Enabled (`IsSpotsEnabled`). Also confirm the correct band is visible in the panadapter and that spots exist for that band in the **Spot List** tab.
- **Spots disappear almost immediately** — The **Spot Lifetime:** slider is set very low. Drag it to the right to increase lifetime.
- **Spots all stack in one row regardless of the Levels: setting** — **Auto Mode:** is enabled and overriding the manual Levels value. Click **Auto Mode:** to disable it, then adjust **Levels:**.

## Related

- [SpotHub overview](overview.md)
- [Pick colors for each spot source](pick-colors-for-each-spot-source.md)
- [Enable DXCC coloring from an ADIF log](enable-dxcc-coloring-from-an-adif-log.md)
- [Clear all spots from the panadapter](clear-all-spots-from-the-panadapter.md)
- [Start WSJT-X UDP listener and filter for CQ, POTA or calls to me](start-wsjt-x-udp-listener-and-filter-for-cq-pota-or-calls-to-me.md)
