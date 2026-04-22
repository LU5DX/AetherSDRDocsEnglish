# Overlay memory channels on the panadapter

Memory channels stored in the radio can be displayed as spot-like markers directly on the panadapter. This makes it easy to see which of your saved frequencies fall within the current view without switching to a separate memory list.

## Before you start

- AetherSDR must be running. A radio connection is not required to change these settings.
- Open the Spot Settings dialog by right-clicking the panadapter spots overlay to access the context menu.

## Steps

1. Right-click the panadapter to open the context menu, then select the Spot Settings option to open the **Spot Settings** dialog.
2. Locate the **Memories:** row.
3. Click the toggle button next to **Memories:**. The button changes from **Disabled** to **Enabled** and memory channels immediately appear as overlays on the panadapter.

To hide memory overlays, click the toggle again so it reads **Disabled**.

## What each control does

| Label | Kind | Default | Persisted key | Behavior |
|---|---|---|---|---|
| **Spots:** | Toggle button | Enabled | `IsSpotsEnabled` | Master toggle for all spot and memory overlays. Memories will not appear if this is Disabled, regardless of the Memories: setting. |
| **Memories:** | Toggle button | Disabled | `IsMemoriesShownOnPanadapter` | Shows or hides radio memory channels as panadapter overlays. |
| **Levels:** | Slider | 3 | `SpotsStackLevels` | Number of vertical stacking rows used when overlays crowd together. Range: 1–10. |
| **Position:** | Slider | 50 | `SpotsPosition` | Vertical position of the overlay band on the panadapter, expressed as a percentage of panel height. Range: 0–100. |
| **Font Size:** | Slider | 16 | `SpotsFontSize` | Text size for overlay labels. Range: 8–32. |
| **Spot Lifetime:** | Slider | 30 min | `SpotsLifetime` | How long a spot marker remains visible before fading. Non-linear scale: 10–55 sec, then 5–55 min, then 1–24 hr. |
| **Override Colors:** | Toggle button | Disabled | `IsSpotsOverrideColorsEnabled` | Forces all overlay text to a single color instead of source-assigned colors. |
| Spot text color picker | Push button | `#FFFF00` | `SpotsOverrideColor` | Opens a color picker to choose the override text color. Active only when **Override Colors:** is Enabled. |
| **Override Background: Enabled** | Toggle button | Enabled | `IsSpotsOverrideBackgroundColorsEnabled` | Draws a filled background behind each overlay label. |
| **Override Background: Auto** | Toggle button | Enabled | `IsSpotsOverrideToAutoBackgroundColorEnabled` | Automatically selects a background color for contrast. When Disabled, the manually chosen background color is used. |
| Spot background color picker | Push button | `#000000` | `SpotsOverrideBgColor` | Opens a color picker to choose the background color. Active when **Override Background: Auto** is Disabled. |
| **Background Opacity:** | Slider | 48 | `SpotsOverrideBgOpacity` | Alpha level of the overlay background. Range: 0–100. |
| **Clear All Spots** | Push button | — | — | Removes all current spot markers from the panadapter. Does not affect memory overlays. |

## Tips

- The **Spots:** master toggle must be Enabled for memory overlays to appear. If you enable **Memories:** but see nothing, check that **Spots:** is also set to Enabled.
- Memory overlays share the same position, font size, and color settings as DX spots. Adjust **Levels:** and **Position:** to avoid overlapping your signal trace.
- If memory labels are difficult to read against the panadapter background, enable **Override Colors:** and use the text color picker to choose a high-contrast color.

## Related

- [Spot Settings overview](overview.md)
- [Turn spots on or off](turn-spots-on-or-off.md)
- [Change spot density and vertical position](change-spot-density-and-vertical-position.md)
- [Enlarge or shrink the spot font](enlarge-or-shrink-the-spot-font.md)
- [Force a single spot text color](force-a-single-spot-text-color.md)
- [Pick a custom background color for spots](pick-a-custom-background-color-for-spots.md)
- [Adjust spot background opacity](adjust-spot-background-opacity.md)
