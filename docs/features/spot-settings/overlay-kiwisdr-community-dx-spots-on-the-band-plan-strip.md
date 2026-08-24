# Overlay KiwiSDR Community DX spots on the band plan strip

Overlay KiwiSDR Community DX database spots (beacons, utilities, time signals) on the panadapter band plan strip.

## Before you start

- AetherSDR connected to a FLEX-8600 radio. This feature does not require a radio connection to configure, but the spots display on the panadapter.

## Steps

1. Open the Spot Settings dialog from the panadapter context menu.
2. Find the **Kiwi DX:** row.
3. Click **Disabled** to change it to **Enabled**.
4. Adjust **Levels:**, **Position:**, **Font Size:**, **Spot Lifetime:**, and color settings as desired.

## What each control does

| Control | Default | Valid range | Setting key |
|---|---|---|---|
| **Kiwi DX:** toggle | Disabled | Enabled / Disabled | `ShowKiwiDxSpots` |
| **Levels:** slider | 3 | 1–10 | `SpotsMaxLevel` |
| **Position:** slider | 50 | 0–100 | `SpotsStartingHeightPercentage` |
| **Font Size:** slider | 16 | 8–32 | `SpotFontSize` |
| **Spot Lifetime:** slider | 30 min | 10 sec – 24 hrs (non-linear steps) | `DxClusterSpotLifetimeSec` |
| **Override Colors:** toggle | Disabled | Enabled / Disabled | `IsSpotsOverrideColorsEnabled` |
| Spot text color picker | #FFFF00 | Any color | `SpotsOverrideColor` |
| **Override Background:** toggle | Enabled | Enabled / Disabled | `IsSpotsOverrideBackgroundColorsEnabled` |
| **Override Background:** **Auto** toggle | Enabled | Enabled / Disabled | `IsSpotsOverrideToAutoBackgroundColorEnabled` |
| Spot background color picker | #000000 | Any color | `SpotsOverrideBgColor` |
| **Background Opacity:** slider | 48 | 0–100 | `SpotsBackgroundOpacity` |
| **Spot Lines:** toggle | Enabled | Enabled / Disabled | `IsSpotsLinesEnabled` |

## Tips

- Kiwi DX spots appear on the band plan strip independent of DX cluster spots, so you can see community-sourced beacons and utilities alongside your live DX cluster feed.
- Set **Spot Lines:** to **Disabled** during contests to reduce visual clutter.

## Related

- [Turn spots on or off](turn-spots-on-or-off.md)
- [Overlay memory channels on the panadapter](overlay-memory-channels-on-the-panadapter.md)
- [Change spot density and vertical position](change-spot-density-and-vertical-position.md)
- [Enlarge or shrink the spot font](enlarge-or-shrink-the-spot-font.md)
- [Shorten or lengthen spot lifetime](shorten-or-lengthen-spot-lifetime.md)
- [Force a single spot text color](force-a-single-spot-text-color.md)
- [Pick a custom background color for spots](pick-a-custom-background-color-for-spots.md)
- [Adjust spot background opacity](adjust-spot-background-opacity.md)
- [Toggle vertical spot lines for contest or casual operating](../dx-cluster/toggle-vertical-spot-lines-for-contest-or-casual-operating.md)
- [Clear every spot from the panadapter](clear-every-spot-from-the-panadapter.md)
- [Spot Settings overview](overview.md)
