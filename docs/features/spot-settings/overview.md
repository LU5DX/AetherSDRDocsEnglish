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

| Label                        | Kind                                                                                                    | Default                        |
|------------------------------|---------------------------------------------------------------------------------------------------------|--------------------------------|
| Spots:                       | Toggle button                                                                                           | Enabled                        |
| Memories:                    | Toggle button                                                                                           | Disabled                       |
| Kiwi DX:                     | Toggle button                                                                                           | Disabled                       |
| Levels:                      | Slider (1–10)                                                                                           | 3                              |
| Position:                    | Slider (0–100)                                                                                          | 50                             |
| Font Size:                   | Slider (8–32)                                                                                           | 16                             |
| Spot Lifetime:               | Slider (10 sec – 24 hrs, non-linear)                                                                    | —                              |
| Override Colors:             | Toggle button                                                                                           | Disabled                       |
| Spot text color picker       | Push button                                                                                             | `#FFFF00`                      |
| Override Background: Enabled | Toggle button                                                                                           | Enabled                        |
| Override Background: Auto    | Toggle button                                                                                           | Enabled                        |
| Spot background color picker | Push button                                                                                             | `#000000`                      |
| Background Opacity:          | Slider (0–100)                                                                                          | 48                             |
| Spot Lines:                  | Toggle button                                                                                           | Enabled                        |
| Clear All Spots              | Push button                                                                                             | —                              |

### Spots:  

Master toggle for DX spot display. When Enabled, spots from the configured DX cluster source are drawn on the panadapter.

### Memories:  

Toggles memory channel overlays on the panadapter. When Enabled, your radio's stored memory channels appear as spot-style overlays for quickly identifying activity on saved channels.

### Kiwi DX:  

New in v26.8.4. Overlays KiwiSDR Community DX database spots (beacons, utilities, time signals) on the band plan strip. Default is Disabled. This setting is stored in `ShowKiwiDxSpots`.

### Levels:  

Vertical stacking rows for spots. Range is 1–10; default is 3. Higher values allow more spots to stack vertically before overlapping.

### Position:  

Vertical position of the spot text on the panadapter, expressed as a percentage. Range is 0–100; default is 50 (middle of the panadapter).

### Font Size:  

Spot text size in points. Range is 8–32; default is 16.

### Spot Lifetime:  

How long spots remain on the panadapter before fading. The slider is non-linear: small movements at the low end adjust lifetime in seconds; larger movements progress through minutes and then hours. Range is 10 seconds to 24 hours.

### Override Colors:  

Forces a single text color for all spots. When Enabled, the color you pick with the Spot text color picker is used for every spot regardless of the source.

### Spot text color picker  

Opens a color dialog to pick the text color used when Override Colors is Enabled. Default is `#FFFF00` (yellow).

### Override Background: Enabled  

Draws a background under spot text. When Enabled, spot text is drawn with a contrasting background for readability.

### Override Background: Auto  

Automatically picks a contrasting background color for spot text. When Enabled, the manually picked color is ignored. When Disabled, the color from the Spot background color picker is used instead.

### Spot background color picker  

Opens a color dialog to pick the background color used when Override Background: Enabled is on and Override Background: Auto is off. Default is `#000000` (black).

### Background Opacity:  

Alpha of the spot background. Range is 0–100; default is 48. At 0 the background is completely transparent; at 100 it is fully opaque.

### Spot Lines:  

Draws vertical lines from the spectrum baseline up to each spot label. Disable during contests or when the panadapter is crowded to reduce visual clutter; the spot labels remain visible and only the vertical lines are hidden.

### Clear All Spots  

Clears all spots from the panadapter immediately.

## Tips

- Toggle buttons display either "Enabled" or "Disabled" text that updates to match the current state, with a green background when enabled and red/amber when disabled.
- Enabling Kiwi DX: overlays spots from the KiwiSDR Community DX database, which includes beacons, utilities, and time signals that are not typically in DX cluster feeds.
- The Spot Lifetime slider is non-linear. Small movements at the low end of the slider adjust lifetime in seconds; larger movements progress through minutes and then hours up to 24 hours.
- Enabling Override Background: Auto while Override Background: Enabled is on lets AetherSDR choose contrasting background colors automatically. Disable Auto to apply your manually picked color from the spot background color picker instead.
- Enabling Memories: shows your radio's stored memory channels as spot-style overlays, which is useful for quickly identifying activity on channels you have saved.
- Disable Spot Lines: during contests or when the panadapter is crowded to reduce visual clutter. The spot labels remain visible; only the vertical lines are hidden.
- The Spot Settings dialog automatically follows the current theme. Text and background colors for dialog elements update when you switch themes.

## Related

- [Turn spots on or off](turn-spots-on-or-off.md)
- [Overlay memory channels on the panadapter](overlay-memory-channels-on-the-panadapter.md)
- [Overlay KiwiSDR Community DX spots](overlay-kiwisdr-community-dx-spots.md)
- [Change spot density and vertical position](change-spot-density-and-vertical-position.md)
- [Enlarge or shrink the spot font](enlarge-or-shrink-the-spot-font.md)
- [Shorten or lengthen spot lifetime](shorten-or-lengthen-spot-lifetime.md)
- [Force a single spot text color](force-a-single-spot-text-color.md)
- [Pick a custom background color for spots](pick-a-custom-background-color-for-spots.md)
- [Adjust spot background opacity](adjust-spot-background-opacity.md)
- [Clear every spot from the panadapter](clear-every-spot-from-the-panadapter.md)