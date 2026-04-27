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
   - When **Enabled**, DX spots are drawn on the panadapter.
   - When **Disabled**, no spots are drawn. The setting is saved immediately; no additional confirmation is needed.

## What each control does

| Label | Kind | Default | Persisted key | Behavior |
|---|---|---|---|---|
| **Spots:** | Toggle button | Enabled | `IsSpotsEnabled` | Master on/off switch for DX spot display on the panadapter. |
| **Memories:** | Toggle button | Disabled | `IsMemoriesShownOnPanadapter` | Shows radio memory channels as spot-like markers on the panadapter. |
| **Levels:** | Slider | 3 | `SpotsStackLevels` | Number of vertical stacking rows used when spots overlap. Range: 1–10. |
| **Position:** | Slider | 50 | `SpotsPosition` | Vertical position of the spot band on the panadapter. Range: 0–100. |
| **Font Size:** | Slider | 16 | `SpotsFontSize` | Text size for spot labels. Range: 8–32. |
| **Spot Lifetime:** | Slider | 30 min | `SpotsLifetime` | How long a spot remains visible before expiring. Steps range from 10 seconds to 24 hours. |
| **Override Colors:** | Toggle button | Disabled | `IsSpotsOverrideColorsEnabled` | Forces all spot text to a single chosen color instead of source-assigned colors. |
| Spot text color picker | Button | `#FFFF00` | `SpotsOverrideColor` | Opens a color picker to select the override text color. Active only when **Override Colors:** is **Enabled**. |
| **Override Background: Enabled** | Toggle button | Enabled | `IsSpotsOverrideBackgroundColorsEnabled` | Draws a filled background behind each spot label. |
| **Override Background: Auto** | Toggle button | Enabled | `IsSpotsOverrideToAutoBackgroundColorEnabled` | Automatically selects a background color for contrast rather than using the manually chosen color. |
| Spot background color picker | Button | `#000000` | `SpotsOverrideBgColor` | Opens a color picker for the manual background color. Used when **Override Background: Auto** is **Disabled**. |
| **Background Opacity:** | Slider | 48 | `SpotsOverrideBgOpacity` | Alpha level of the spot background. Range: 0–100. |
| **Clear All Spots** | Button | — | — | Immediately removes all spots from the panadapter. Does not affect the enabled/disabled state. |

The **Total Spots:** indicator at the bottom of the dialog shows how many live spots are currently tracked.

## Tips

- Toggling **Spots:** to **Disabled** does not clear buffered spots. When you re-enable it, spots that have not yet expired will reappear.
- The **Spot Lifetime:** slider uses a non-linear scale: fine steps in seconds at the low end, then minutes, then hours up to 24 hours.

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
