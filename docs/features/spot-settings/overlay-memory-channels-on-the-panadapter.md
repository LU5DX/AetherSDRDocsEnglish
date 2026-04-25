# Overlay memory channels on the panadapter

Memory channels stored in your radio can be displayed as spot-like labels directly on the panadapter. This lets you see at a glance which memory frequencies fall within your current view.

## Before you start

- AetherSDR must be running. A radio connection is not required to change these settings.
- Open the Spot Settings dialog by right-clicking the panadapter and selecting the Spots overlay option from the context menu.

## Steps

1. Right-click anywhere on the panadapter to open the context menu, then open the Spot Settings dialog.
2. Locate the **Memories:** row.
3. Click the toggle button next to **Memories:** so it reads **Enabled**. The default state is **Disabled**.
4. Memory channel labels will appear on the panadapter immediately. Close the dialog when finished.

To hide memory overlays again, click the **Memories:** toggle so it reads **Disabled**.

## What each control does

| Label | Kind | Default | Setting key | Behavior |
|---|---|---|---|---|
| Spots: | Toggle button | Enabled | `IsSpotsEnabled` | Master toggle for all spot and memory overlays. Memories will not appear if this is Disabled. |
| Memories: | Toggle button | Disabled | `IsMemoriesShownOnPanadapter` | Shows radio memory channels as labels on the panadapter. |
| Levels: | Slider | 3 | `SpotsStackLevels` | Number of vertical stacking rows used when labels overlap. Range: 1–10. |
| Position: | Slider | 50 | `SpotsPosition` | Vertical position of labels on the panadapter. Range: 0–100. |
| Font Size: | Slider | 16 | `SpotsFontSize` | Text size of labels. Range: 8–32. |
| Spot Lifetime: | Slider | 30 min | `SpotsLifetime` | How long spots remain visible before fading. Non-linear scale from 10 seconds to 24 hours. |
| Override Colors: | Toggle button | Disabled | `IsSpotsOverrideColorsEnabled` | Forces all spot and memory labels to use a single text color. |
| Spot text color picker | Button | `#FFFF00` | `SpotsOverrideColor` | Opens a color picker to choose the override text color. |
| Override Background: Enabled | Toggle button | Enabled | `IsSpotsOverrideBackgroundColorsEnabled` | Draws a background fill behind label text. |
| Override Background: Auto | Toggle button | Enabled | `IsSpotsOverrideToAutoBackgroundColorEnabled` | Automatically selects a background color for readability contrast. |
| Spot background color picker | Button | `#000000` | `SpotsOverrideBgColor` | Opens a color picker to choose the background color when Auto is Disabled. |
| Background Opacity: | Slider | 48 | `SpotsOverrideBgOpacity` | Alpha level of the label background. Range: 0–100. |
| Clear All Spots | Button | — | — | Removes all current spots from the panadapter. Does not affect memories. |

## Tips

- Memory labels share the same position, font size, stacking, and color settings as DX spots. Adjust those controls to change the appearance of both.
- If no memory labels appear after enabling **Memories:**, confirm that the **Spots:** toggle is also set to **Enabled**. The master **Spots:** toggle controls both.
- The **Override Background: Auto** mode is enabled by default and picks a contrasting background automatically. Disable it to use the manual background color picker instead.

## Related

- [Spot Settings overview](overview.md)
- [Turn spots on or off](turn-spots-on-or-off.md)
- [Change spot density and vertical position](change-spot-density-and-vertical-position.md)
- [Enlarge or shrink the spot font](enlarge-or-shrink-the-spot-font.md)
- [Force a single spot text color](force-a-single-spot-text-color.md)
- [Pick a custom background color for spots](pick-a-custom-background-color-for-spots.md)
- [Adjust spot background opacity](adjust-spot-background-opacity.md)
