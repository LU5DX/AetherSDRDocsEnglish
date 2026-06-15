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

| Control                                 | What it does                                                                                                             | Default   |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------|-----------|
| **Spots:** toggle                       | Master on/off for all spot and memory overlays. Memories will not appear if this is off.                                 | Enabled   |
| **Memories:** toggle                    | Shows or hides memory channel markers on the panadapter.                                                                 | Disabled  |
| **Levels:** slider                      | Number of vertical stacking rows used when spots or memories overlap. Range: 1–10.                                       | 3         |
| **Position:** slider                    | Vertical position of the overlay band on the panadapter, as a percentage from top. Range: 0–100.                         | 50        |
| **Font Size:** slider                   | Text size for spot and memory labels. Range: 8–32.                                                                       | 16        |
| **Spot Lifetime:** slider               | How long spots remain before fading. Non-linear scale: 10 seconds to 24 hours.                                           | —         |
| **Override Colors:** toggle             | Forces a single text color for all spots and memories instead of source-assigned colors.                                 | Disabled  |
| Spot text color picker                  | Opens a color picker to choose the override text color. Default: `#FFFF00`.                                              | `#FFFF00` |
| **Override Background: Enabled** toggle | Draws a colored background behind spot and memory text.                                                                  | Enabled   |
| **Override Background: Auto** toggle    | Automatically selects a background color for contrast rather than using the manual color.                                | Enabled   |
| Spot background color picker            | Opens a color picker for the manual background color. Default: `#000000`.                                                | `#000000` |
| **Background Opacity:** slider          | Sets the transparency of the spot background. Range: 0–100.                                                              | 48        |
| **Spot Lines:** toggle                  | Draws vertical lines from the spectrum baseline up to each spot label. Disable during contests to reduce visual clutter. | Enabled   |
| **Clear All Spots**                     | Removes all spots from the panadapter immediately. Does not affect memories.                                             | —         |

### Total Spots indicator

The **Total Spots:** label at the bottom of the dialog shows the count of live spots currently being tracked. It updates automatically as spots arrive or expire.

## Tips

- Memory overlays share the same position, font, stacking, and color settings as DX spots. Adjust **Levels:** and **Position:** to prevent memory markers from obscuring signal peaks.
- If memory markers are not visible even after enabling **Memories:**, confirm that the **Spots:** toggle is also set to "Enabled". The Spots master toggle controls all overlay rendering.
- The **Override Background: Auto** toggle is active by default and selects contrast-appropriate background colors automatically. Disable it only if you want to set a specific background color with the background color picker.
- During a contest, disable **Spot Lines:** to reduce visual clutter on the panadapter without hiding spot labels.
- The Spot Settings dialog now uses the active theme colors for its title and the Total Spots label, matching the appearance of other AetherSDR dialogs.
- The toggle buttons no longer change their displayed text when toggled. Instead, they indicate their state solely through their checked/unchecked appearance (colored red when disabled, default when enabled). The label next to each toggle remains constant.

## Troubleshooting

- **Memories: shows "Enabled" but no markers appear on the panadapter** — Check that the **Spots:** toggle is set to "Enabled". The master spots toggle must be on for any overlay, including memories, to render.
- **Memory markers overlap and are hard to read** — Increase the **Levels:** slider value to give the renderer more stacking rows, or adjust **Position:** to move the overlay to a less crowded area of the panadapter.
- **The dialog text looks different from before** — The Spot Settings dialog now applies the current theme. No functionality has changed; only visual styling was updated.

## Related

- [Spot Settings overview](overview.md)
- [Turn spots on or off](turn-spots-on-or-off.md)
- [Change spot density and vertical position](change-spot-density-and-vertical-position.md)
- [Enlarge or shrink the spot font](enlarge-or-shrink-the-spot-font.md)
- [Shorten or lengthen spot lifetime](shorten-or-lengthen-spot-lifetime.md)
- [Force a single spot text color](force-a-single-spot-text-color.md)
- [Pick a custom background color for spots](pick-a-custom-background-color-for-spots.md)
- [Adjust spot background opacity](adjust-spot-background-opacity.md)