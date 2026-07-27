# Spot Settings overview

The Spot Settings dialog controls how DX spots and memory channels appear on the panadapter — including whether they are shown at all, how densely they stack, how long they persist, and how their text and backgrounds are colored. Open it from the panadapter context menu or the spots overlay.

## Before you start

- A radio connection is not required to adjust spot settings; changes take effect whenever spots are next displayed.
- Spots must be fed from a configured DX cluster or other source (see `Settings > SpotHub...`) before any spots will appear on the panadapter.

## How it works

The Spot Settings dialog is a standalone window. It groups controls into three areas: visibility and layout, lifetime, and color overrides. All changes are saved immediately when you interact with a control. The dialog automatically follows the current theme for colors and styling.

The **Total Spots:** indicator at the bottom of the dialog shows the count of live spots currently being tracked.

Toggle buttons display either "Enabled" or "Disabled" text that updates to match the current state, with a colored background (green for enabled, red/amber for disabled).

## What each control does

| Label | Kind | Default | Behavior | Notes |
|---|---|---|---|---|
| Spots: | Toggle button | Enabled | Master toggle for DX spot display. Button text changes to "Enabled" or "Disabled" based on state. | — |
| Memories: | Toggle button | Disabled | Toggles memory channel overlays on panadapter. Button text changes to "Enabled" or "Disabled" based on state. | Setting key changed from `IsMemoriesShownOnPanadapter` in v0.9.7. |
| Levels: | Slider (1–10) | 3 | Vertical stacking rows for spots. | Setting key changed from `SpotsStackLevels` in v0.9.7. |
| Position: | Slider (0–100) | 50 | Vertical position on panadapter as a percentage. | Setting key changed from `SpotsPosition` in v0.9.7. |
| Font Size: | Slider (8–32) | 16 | Spot text size in points. | Setting key changed from `SpotsFontSize` in v0.9.7. |
| Spot Lifetime: | Slider (10 sec – 24 hrs, non-linear) | — | How long spots remain before fading. | Stored in seconds (`DxClusterSpotLifetimeSec`). Setting key changed from `SpotsLifetime` in v0.9.7. Migrates old minutes-based `DxClusterSpotLifetime` key on first read. |
| Override Colors: | Toggle button | Disabled | Forces a single text color for all spots. Button text changes to "Enabled" or "Disabled" based on state. | — |
| Spot text color picker | Push button | `#FFFF00` | Opens a color dialog to pick spot text color. | — |
| Override Background: Enabled | Toggle button | Enabled | Draws a background under spot text. Button text changes to "Enabled" or "Disabled" based on state. | — |
| Override Background: Auto | Toggle button | Enabled | Auto-picks background color for contrast. The button text stays "Auto"; its background color changes to indicate state. | — |
| Spot background color picker | Push button | `#000000` | Opens a color dialog to pick spot background color. | — |
| Background Opacity: | Slider (0–100) | 48 | Alpha of spot background (0 = transparent, 100 = opaque). | Setting key changed from `SpotsOverrideBgOpacity` in v0.9.7. |
| Spot Lines: | Toggle button | Enabled | Draws vertical lines from the spectrum baseline up to each spot label. Disable during contests to reduce visual clutter. Button text changes to "Enabled" or "Disabled" based on state. | New in v0.9.7 (#2349). |
| Clear All Spots | Push button | — | Clears all spots from the panadapter. | — |

## Tips

- Toggle buttons display either "Enabled" or "Disabled" text that updates to match the current state, with a green background when enabled and red/amber when disabled.
- The Spot Lifetime slider is non-linear. Small movements at the low end of the slider adjust lifetime in seconds; larger movements progress through minutes and then hours up to 24 hours.
- Enabling Override Background: Auto while Override Background: Enabled is on lets AetherSDR choose contrasting background colors automatically. Disable Auto to apply your manually picked color from the spot background color picker instead.
- Enabling Memories: shows your radio's stored memory channels as spot-style overlays, which is useful for quickly identifying activity on channels you have saved.
- Disable Spot Lines: during contests or when the panadapter is crowded to reduce visual clutter. The spot labels remain visible; only the vertical lines are hidden.
- The Spot Settings dialog automatically follows the current theme. Text and background colors for dialog elements update when you switch themes.

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