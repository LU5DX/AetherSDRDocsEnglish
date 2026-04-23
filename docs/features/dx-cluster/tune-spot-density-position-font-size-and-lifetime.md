# Tune spot density, position, font size and lifetime

Use the Display tab in SpotHub to control how many spot labels appear on the panadapter, where they sit vertically, how large the text is, and how long each spot stays visible before fading.

## Before you start

- Open AetherSDR and ensure at least one spot source is configured (DX cluster, RBN, WSJT-X, POTA, SpotCollector, or FreeDV).
- Spots must be enabled: the `IsSpotsEnabled` toggle must be on (default: Enabled).

## Steps

1. Click `Settings > SpotHub...` to open the SpotHub dialog.
2. Click the **Display** tab.
3. Confirm the **Spots:** toggle shows **Enabled**. If it does not, click it to enable the spot overlay.
4. To let AetherSDR automatically adjust spot density as you zoom the panadapter, click **Auto Mode:** to enable it. Skip steps 5 and 6 if you use Auto Mode.
5. To set density manually, drag the **Levels:** slider to choose the number of vertical stacking rows for spots.
6. Drag the **Position:** slider to move the spot row block up or down on the panadapter.
7. Drag the **Font Size:** slider to increase or decrease the spot label text size.
8. Drag the **Spot Lifetime:** slider to set how many seconds a spot remains visible before it fades.

## What each control does

| Control | What it does | Persisted key |
|---|---|---|
| **Spots:** | Master toggle for the spot overlay. Default: Enabled. | `IsSpotsEnabled` |
| **Auto Mode:** | Automatically adjusts spot density based on panadapter zoom level. | `SpotsAutoMode` |
| **Levels:** | Number of vertical stacking rows used when spots cluster at nearby frequencies. | `SpotsStackLevels` |
| **Position:** | Vertical position of the spot overlay on the panadapter. | `SpotsPosition` |
| **Font Size:** | Size of the text used for spot labels. | `SpotsFontSize` |
| **Spot Lifetime:** | Seconds a spot remains on the panadapter before being removed. | `SpotsLifetime` |

## Tips

- When **Auto Mode:** is enabled, the **Levels:** slider has no effect. Disable **Auto Mode:** first if you want manual control over stacking density.
- The WSJT-X source has its own separate spot lifetime setting (**Spot Life:** on the WSJT-X tab), stored as `WsjtxSpotLife`. Adjusting **Spot Lifetime:** on the Display tab does not affect WSJT-X spots.
- If the panadapter looks cluttered at a busy contest frequency, reduce **Levels:** or shorten **Spot Lifetime:** rather than disabling spots entirely.

## Related

- [SpotHub overview](overview.md)
- [Pick colors for each spot source](pick-colors-for-each-spot-source.md)
- [Start WSJT-X UDP listener and filter for CQ, POTA or calls to me](start-wsjt-x-udp-listener-and-filter-for-cq-pota-or-calls-to-me.md)
- [Tune to a spot by double-clicking the spot list](tune-to-a-spot-by-double-clicking-the-spot-list.md)
- [Clear all spots from the panadapter](clear-all-spots-from-the-panadapter.md)
