# Turn spots on or off

DX spots appear as overlays on the panadapter. This page explains how to enable or disable the spot display entirely, and describes all controls in the Spot Settings dialog.

## Before you start

- Open a panadapter. The Spot Settings dialog is not available from the main menu.
- Spots require an active SpotHub source to display. See `Settings > SpotHub...` to configure your DX cluster or other spot feeds.

## Steps

1. Right-click on the panadapter to open the context menu.
2. Select the Spots overlay option to open the **Spot Settings** dialog.
3. Click the toggle button next to **Spots:** to switch between **Enabled** and **Disabled**.
4. Close the dialog. The change takes effect immediately.

## What each control does

| Label | Kind | Default | Setting key | Behavior |
|---|---|---|---|---|
| **Spots:** | Toggle button | Enabled | `IsSpotsEnabled` | Master toggle for DX spot display on the panadapter. |
| **Memories:** | Toggle button | Disabled | `IsMemoriesShownOnPanadapter` | Shows radio memory channels as spot-like overlays on the panadapter. |
| **Levels:** | Slider | 3 | `SpotsStackLevels` | Number of vertical stacking rows used when multiple spots are near the same frequency. Range: 1–10. |
| **Position:** | Slider | 50 | `SpotsPosition` | Vertical position of the spot overlay on the panadapter, as a percentage from top. Range: 0–100. |
| **Font Size:** | Slider | 16 | `SpotsFontSize` | Text size for spot labels. Range: 8–32. |
| **Spot Lifetime:** | Slider | 30 min | `SpotsLifetime` | How long a spot remains visible before expiring. Uses a non-linear scale: 10–55 seconds, then 5–55 minutes, then 1–24 hours. |
| **Override Colors:** | Toggle button | Disabled | `IsSpotsOverrideColorsEnabled` | Forces all spot text to use a single color instead of source-assigned colors. |
| Spot text color picker | Push button | #FFFF00 | `SpotsOverrideColor` | Opens a color picker to select the override text color. Active only when **Override Colors:** is Enabled. |
| **Override Background: Enabled** | Toggle button | Enabled | `IsSpotsOverrideBackgroundColorsEnabled` | Draws a colored background behind each spot label. |
| **Override Background: Auto** | Toggle button | Enabled | `IsSpotsOverrideToAutoBackgroundColorEnabled` | Automatically selects a background color to contrast with the spot text color. |
| Spot background color picker | Push button | #000000 | `SpotsOverrideBgColor` | Opens a color picker to select the background color. Used when **Override Background: Auto** is Disabled. |
| **Background Opacity:** | Slider | 48 | `SpotsOverrideBgOpacity` | Alpha (transparency) of the spot background. Range: 0–100. |
| **Clear All Spots** | Push button | — | — | Removes all current spots from the panadapter immediately. Does not affect the enabled state. |

The **Total Spots:** indicator at the top of the dialog shows the count of live spots currently tracked.

## Tips

- Disabling **Spots:** hides the overlay but does not disconnect your SpotHub sources. Spots continue to accumulate in the background; re-enabling restores the current feed.
- If spots are visually crowded, increase **Levels:** to spread them across more vertical rows, or decrease **Spot Lifetime:** to expire older spots sooner.
- **Override Background: Auto** overrides the background color picker. To use a custom background color, disable **Override Background: Auto** first, then use the spot background color picker.

## Troubleshooting

- **Spots toggle is Enabled but no spots appear on the panadapter** — No spot feed may be configured or connected. Open `Settings > SpotHub...` and verify at least one source is active and connected.
- **Spot Lifetime slider resets on restart** — The dialog migrates from an older minutes-based setting to a seconds-based setting on first load. If you set the lifetime before upgrading, open Spot Settings and re-set the **Spot Lifetime:** slider, then close the dialog to save.

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
