# Turn spots on or off

DX spots from cluster sources appear as overlays on the panadapter. This page explains how to enable or disable that display using the master spot toggle in the Spot Settings dialog.

## Before you start

- A panadapter must be visible in the main window.
- Spot sources (DX cluster, RBN, etc.) should be configured via `Settings > SpotHub...` if you want live spots to appear once you enable the overlay.

## Steps

1. Right-click anywhere on the panadapter to open the context menu.
2. Select the spot overlay option to open the **Spot Settings** dialog.
3. Locate the **Spots:** toggle button at the top of the dialog.
4. Click the button to toggle between **Enabled** and **Disabled**.
   - The button displays "Enabled" when toggled on. The checked state (highlighted background) indicates the active status.
   - When **Enabled**, DX spots are drawn on the panadapter.
   - When **Disabled**, no spots are drawn. The setting is saved immediately; no additional confirmation is needed.

## What each control does

| Label                            | Kind          | Default   | Setting key                              |
|----------------------------------|---------------|-----------|------------------------------------------|
| **Spots:**                       | Toggle button | Enabled   | `IsSpotsEnabled`                         |
| **Memories:**                    | Toggle button | Disabled  | `IsMemorySpotsEnabled`                   |
| **Levels:**                      | Slider        | 3         | `SpotsMaxLevel`                          |
| **Position:**                    | Slider        | 50        | `SpotsStartingHeightPercentage`          |
| **Font Size:**                   | Slider        | 16        | `SpotFontSize`                           |
| **Spot Lifetime:**               | Slider        | —         | `DxClusterSpotLifetimeSec`               |
| **Override Colors:**             | Toggle button | Disabled  | `IsSpotsOverrideColorsEnabled`           |
| Spot text color picker           | Button        | `#FFFF00` | `SpotsOverrideColor`                     |
| **Override Background: Enabled** | Toggle button | Enabled   | `IsSpotsOverrideBackgroundColorsEnabled` |
| **Override Background: Auto**    | Toggle button | Enabled   | `IsSpotsOverrideToAutoBackgroundColorEnabled` |
| Spot background color picker     | Button        | `#000000` | `SpotsOverrideBgColor`                   |
| **Background Opacity:**          | Slider        | 48        | `SpotsBackgroundOpacity`                 |
| **Spot Lines:**                  | Toggle button | Enabled   | `IsSpotsLinesEnabled`                    |
| **Clear All Spots**              | Button        | —         | —                                        |

The **Total Spots:** indicator at the bottom of the dialog shows how many live spots are currently tracked.

### Control details

**Spot Lines:** draws a vertical line from the spectrum baseline up to each spot label. Disable this during contests to reduce visual clutter. This control was added in v0.9.7 (issue #2349).

**Spot Lifetime:** uses a non-linear scale ranging from 10 seconds to 24 hours. The value is stored in seconds in `DxClusterSpotLifetimeSec`. On first read, any value previously saved under the old minutes-based key `DxClusterSpotLifetime` is automatically migrated.

### Setting key changes in v0.9.7

Several setting keys were renamed. If you reference these keys in scripts or external configuration tools, update them accordingly.

| Control             | Old key                        | New key                          |
|---------------------|--------------------------------|----------------------------------|
| **Memories:**       | `IsMemoriesShownOnPanadapter`  | `IsMemorySpotsEnabled`           |
| **Levels:**         | `SpotsStackLevels`             | `SpotsMaxLevel`                  |
| **Position:**       | `SpotsPosition`                | `SpotsStartingHeightPercentage`  |
| **Font Size:**      | `SpotsFontSize`                | `SpotFontSize`                   |
| **Spot Lifetime:**  | `SpotsLifetime`                | `DxClusterSpotLifetimeSec`       |
| **Background Opacity:** | `SpotsOverrideBgOpacity`   | `SpotsBackgroundOpacity`         |

## Tips

- Toggling **Spots:** to **Disabled** does not clear buffered spots. When you re-enable it, spots that have not yet expired will reappear.
- Toggle buttons in the Spot Settings dialog now always display "Enabled" as their text label. The checked state (highlighted background) indicates whether the feature is active.
- The **Spot Lifetime:** slider uses a non-linear scale: fine steps in seconds at the low end, then minutes, then hours up to 24 hours.
- Disable **Spot Lines:** during contests to keep the panadapter uncluttered while retaining spot labels.
- The Spot Settings dialog now follows the current theme. Title labels and the Total Spots indicator use the theme's primary text color for consistent appearance across different theme profiles.

## Related

- [Spot Settings overview](overview.md)
- [Overlay memory channels on the panadapter](overlay-memory-channels-on-the-panadapter.md)
- [Change spot density and vertical position](change-spot-density-and-vertical-position.md)
- [Enlarge or shrink the spot font](enlarge-or-shrink-the-spot-font.md)
- [Shorten or lengthen spot lifetime](shorten-or-lengthen-spot-lifetime.md)
- [Force a single spot text color](force-a-single-spot-text-color.md)
- [Pick a custom background color for spots](pick-a-custom-background-color-for-spots.md)
- [Adjust spot background opacity](adjust-spot-background-opacity.md)
- [Clear every spot from the panadapter](clear-every-spot-from-the-panadapter.md)