# Overlay memory channels on the panadapter

Memory channels stored on your FLEX-8600 can be displayed as spot-like overlays directly on the panadapter. This lets you see saved frequencies in context while you browse the band.

## Before you start

- AetherSDR must be running. A radio connection is not required to configure this setting.
- Open the Spot Settings dialog by right-clicking on the panadapter's spots overlay area to access the context menu.

## Steps

1. Right-click the panadapter spots overlay to open the context menu, then select the option that opens **Spot Settings**.
2. Locate the **Memories:** row in the dialog.
3. Click the toggle button next to **Memories:**. It changes from **Disabled** to **Enabled**.
4. Close the dialog. Memory channels now appear as overlays on the panadapter.

To hide memory overlays, click the **Memories:** toggle again so it reads **Disabled**.

## What each control does

| Control | Default | Behavior | Setting key |
|---|---|---|---|
| **Memories:** toggle | Disabled | Turns memory channel overlays on or off on the panadapter. | `IsMemoriesShownOnPanadapter` |
| **Spots:** toggle | Enabled | Master toggle for all spot and memory overlay display. If this is **Disabled**, memory overlays will not appear regardless of the **Memories:** setting. | `IsSpotsEnabled` |
| **Levels:** slider | 3 | Number of vertical stacking rows used for overlays. Range: 1–10. | `SpotsStackLevels` |
| **Position:** slider | 50 | Vertical position of overlays on the panadapter. Range: 0–100. | `SpotsPosition` |
| **Font Size:** slider | 16 | Text size for overlay labels. Range: 8–32. | `SpotsFontSize` |
| **Spot Lifetime:** slider | 30 min | How long spots remain before fading. Non-linear scale: 10–55 sec, then 5–55 min, then 1–24 hr. | `SpotsLifetime` |
| **Override Colors:** toggle | Disabled | Forces a single text color for all overlays. | `IsSpotsOverrideColorsEnabled` |
| Spot text color picker | #FFFF00 | Opens a color picker to select the override text color. Active only when **Override Colors:** is **Enabled**. | `SpotsOverrideColor` |
| **Override Background: Enabled** toggle | Enabled | Draws a background behind overlay text. | `IsSpotsOverrideBackgroundColorsEnabled` |
| **Override Background: Auto** toggle | Enabled | Automatically selects a background color for contrast. | `IsSpotsOverrideToAutoBackgroundColorEnabled` |
| Spot background color picker | #000000 | Opens a color picker to select the background color manually. | `SpotsOverrideBgColor` |
| **Background Opacity:** slider | 48 | Alpha (transparency) of the overlay background. Range: 0–100. | `SpotsOverrideBgOpacity` |
| **Clear All Spots** | — | Removes all current spots from the panadapter immediately. Does not affect memory overlays stored on the radio. | — |

## Tips

- Memory overlays share the same position, font size, stacking, and color settings as DX spots. Adjust **Levels:** and **Position:** to prevent overlaps if you have many memories on a band.
- If no overlays appear after enabling **Memories:**, confirm that **Spots:** is also set to **Enabled**. The **Spots:** toggle is the master switch for all overlay display.

## Troubleshooting

- **Memories: is Enabled but nothing appears on the panadapter** — Check that **Spots:** is also **Enabled**. Overlays will not render if the master **Spots:** toggle is **Disabled**.
- **Memory overlays are present but unreadable** — Increase **Font Size:** or enable **Override Background: Enabled** so text has a contrasting background.

## Related

- [Turn spots on or off](turn-spots-on-or-off.md)
- [Change spot density and vertical position](change-spot-density-and-vertical-position.md)
- [Enlarge or shrink the spot font](enlarge-or-shrink-the-spot-font.md)
- [Force a single spot text color](force-a-single-spot-text-color.md)
- [Pick a custom background color for spots](pick-a-custom-background-color-for-spots.md)
- [Adjust spot background opacity](adjust-spot-background-opacity.md)
- [Shorten or lengthen spot lifetime](shorten-or-lengthen-spot-lifetime.md)
