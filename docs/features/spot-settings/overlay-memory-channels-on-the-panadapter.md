# Overlay memory channels on the panadapter

Memory channels stored in your FLEX-8600 can be displayed as spot-like markers on the panadapter, making it easy to see saved frequencies in context with live signals. This page explains how to turn that overlay on and adjust it alongside other spot settings.

## Before you start

- AetherSDR must be running. A radio connection is not required to change these settings.
- Open the Spot Settings dialog by right-clicking the panadapter and selecting the Spots overlay option from the context menu.

## Steps

1. Right-click anywhere on the panadapter to open the context menu, then open the Spot Settings dialog.
2. Locate the **Memories:** row.
3. Click the toggle button next to **Memories:**. It reads "Disabled" by default. Click it once to change it to "Enabled".
4. Memory channels now appear as overlays on the panadapter. Click the toggle again to return to "Disabled" if you want to hide them.

## What each control does

| Control | What it does | Default | Setting key |
|---|---|---|---|
| **Spots:** toggle | Master on/off for all spot and memory overlays. Memories will not appear if this is off. | Enabled | `IsSpotsEnabled` |
| **Memories:** toggle | Shows or hides memory channel markers on the panadapter. | Disabled | `IsMemoriesShownOnPanadapter` |
| **Levels:** slider | Number of vertical stacking rows used when spots or memories overlap. Range: 1–10. | 3 | `SpotsStackLevels` |
| **Position:** slider | Vertical position of the overlay band on the panadapter, as a percentage from top. Range: 0–100. | 50 | `SpotsPosition` |
| **Font Size:** slider | Text size for spot and memory labels. Range: 8–32. | 16 | `SpotsFontSize` |
| **Spot Lifetime:** slider | How long spots remain before fading. Non-linear scale: 10–55 seconds, then 5–55 minutes, then 1–24 hours. | 30 min | `SpotsLifetime` |
| **Override Colors:** toggle | Forces a single text color for all spots and memories instead of source-assigned colors. | Disabled | `IsSpotsOverrideColorsEnabled` |
| Spot text color picker | Opens a color picker to choose the override text color. Default: `#FFFF00`. | `#FFFF00` | `SpotsOverrideColor` |
| **Override Background: Enabled** toggle | Draws a colored background behind spot and memory text. | Enabled | `IsSpotsOverrideBackgroundColorsEnabled` |
| **Override Background: Auto** toggle | Automatically selects a background color for contrast rather than using the manual color. | Enabled | `IsSpotsOverrideToAutoBackgroundColorEnabled` |
| Spot background color picker | Opens a color picker for the manual background color. Default: `#000000`. | `#000000` | `SpotsOverrideBgColor` |
| **Background Opacity:** slider | Sets the transparency of the spot background. Range: 0–100. | 48 | `SpotsOverrideBgOpacity` |
| **Clear All Spots** | Removes all spots from the panadapter immediately. Does not affect memories. | — | — |

## Tips

- Memory overlays share the same position, font, stacking, and color settings as DX spots. Adjust **Levels:** and **Position:** to prevent memory markers from obscuring signal peaks.
- If memory markers are not visible even after enabling **Memories:**, confirm that the **Spots:** toggle is also set to "Enabled". The Spots master toggle controls all overlay rendering.
- The **Override Background: Auto** toggle is active by default and selects contrast-appropriate background colors automatically. Disable it only if you want to set a specific background color with the background color picker.

## Troubleshooting

- **Memories: shows "Enabled" but no markers appear on the panadapter** — Check that the **Spots:** toggle is set to "Enabled". The master spots toggle must be on for any overlay, including memories, to render.
- **Memory markers overlap and are hard to read** — Increase the **Levels:** slider value to give the renderer more stacking rows, or adjust **Position:** to move the overlay to a less crowded area of the panadapter.

## Related

- [Spot Settings overview](overview.md)
- [Turn spots on or off](turn-spots-on-or-off.md)
- [Change spot density and vertical position](change-spot-density-and-vertical-position.md)
- [Enlarge or shrink the spot font](enlarge-or-shrink-the-spot-font.md)
- [Shorten or lengthen spot lifetime](shorten-or-lengthen-spot-lifetime.md)
- [Force a single spot text color](force-a-single-spot-text-color.md)
- [Pick a custom background color for spots](pick-a-custom-background-color-for-spots.md)
- [Adjust spot background opacity](adjust-spot-background-opacity.md)
