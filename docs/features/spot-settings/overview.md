# Spot Settings overview

The Spot Settings dialog controls how DX spots and memory channels appear on the panadapter — including whether they are shown at all, how densely they stack, how long they persist, and how their text and backgrounds are colored. Open it from the panadapter context menu or the spots overlay.

## Before you start

- A radio connection is not required to adjust spot settings; changes take effect whenever spots are next displayed.
- Spots must be fed from a configured DX cluster or other source (see `Settings > SpotHub...`) before any spots will appear on the panadapter.

## How it works

The Spot Settings dialog is a standalone window. It groups controls into three areas: visibility and layout, lifetime, and color overrides. All changes are saved immediately when you interact with a control.

The **Total Spots:** indicator at the bottom of the dialog shows the count of live spots currently being tracked.

## What each control does

| Label | Kind | Default | Setting key | Behavior |
|---|---|---|---|---|
| Spots: | Toggle button | Enabled | `IsSpotsEnabled` | Master toggle for DX spot display on the panadapter. |
| Memories: | Toggle button | Disabled | `IsMemoriesShownOnPanadapter` | Overlays radio memory channels on the panadapter as spot-like markers. |
| Levels: | Slider | 3 | `SpotsStackLevels` | Sets the number of vertical stacking rows used when spots are close in frequency. Range: 1–10. |
| Position: | Slider | 50 | `SpotsPosition` | Sets the vertical position of the spot row on the panadapter as a percentage from top. Range: 0–100. |
| Font Size: | Slider | 16 | `SpotsFontSize` | Controls spot label text size. Range: 8–32. |
| Spot Lifetime: | Slider | 30 min | `SpotsLifetime` | How long a spot remains visible before expiring. Uses a non-linear scale: 10–55 seconds in 5-second steps, then 5–55 minutes in 5-minute steps, then 1–24 hours in 1-hour steps. |
| Override Colors: | Toggle button | Disabled | `IsSpotsOverrideColorsEnabled` | When enabled, forces all spot text to use the single color chosen by the spot text color picker, instead of per-source colors. |
| Spot text color picker | Push button | `#FFFF00` | `SpotsOverrideColor` | Opens a color dialog to choose the override text color. Only applied when Override Colors: is Enabled. |
| Override Background: Enabled | Toggle button | Enabled | `IsSpotsOverrideBackgroundColorsEnabled` | Draws a filled background behind each spot label to improve legibility. |
| Override Background: Auto | Toggle button | Enabled | `IsSpotsOverrideToAutoBackgroundColorEnabled` | When enabled, automatically selects a background color for contrast rather than using the manually chosen color. |
| Spot background color picker | Push button | `#000000` | `SpotsOverrideBgColor` | Opens a color dialog to choose the background color. Used only when Override Background: Auto is disabled. |
| Background Opacity: | Slider | 48 | `SpotsOverrideBgOpacity` | Sets the transparency of the spot background. Range: 0–100. |
| Clear All Spots | Push button | — | — | Removes all current spots from the panadapter immediately. This action is not undoable. |

## Tips

- The Spot Lifetime slider is non-linear. Small movements at the low end of the slider adjust lifetime in seconds; larger movements progress through minutes and then hours up to 24 hours.
- Enabling Override Background: Auto while Override Background: Enabled is on lets AetherSDR choose contrasting background colors automatically. Disable Auto to apply your manually picked color from the spot background color picker instead.
- Enabling Memories: shows your radio's stored memory channels as spot-style overlays, which is useful for quickly identifying activity on channels you have saved.

## Related

- [Turn spots on or off](turn-spots-on-or-off.md)
- [Overlay memory channels on the panadapter](overlay-memory-channels-on-the-panadapter.md)
- [Change spot density and vertical position](change-spot-density-and-vertical-position.md)
- [Enlarge or shrink the spot font](enlarge-or-shrink-the-spot-font.md)
- [Shorten or lengthen spot lifetime](shorten-or-lengthen-spot-lifetime.md)
- [Force a single spot text color](force-a-single-spot-text-color.md)
- [Pick a custom background color for spots](pick-a-custom-background-color-for-spots.md)
- [Adjust spot background opacity](adjust-spot-background-opacity.md)
- [Clear every spot from the panadapter](clear-every-spot-from-the-panadapter.md)
