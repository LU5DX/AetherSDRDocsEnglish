# Spot Settings overview

The Spot Settings dialog controls how DX spots and memory channels appear on the panadapter — including whether they are shown at all, how dense and large they are, how long they persist, and how their text and background are colored. Open it from the panadapter context menu or the Spots overlay.

## Before you start

- No radio connection is required to change these settings.
- Spots must be fed from a configured DX cluster or other source via `Settings > SpotHub...` before any spots will appear on the panadapter.

## How it works

When spots are enabled, AetherSDR receives spot data from connected sources (DX cluster, RBN, WSJTX, and others) and renders each spot as a labeled marker on the panadapter at the corresponding frequency. The Spot Settings dialog gives you control over every visual aspect of that rendering.

The **Total Spots:** indicator at the top of the dialog shows a live count of spots currently being tracked, regardless of whether the display is enabled.

Settings are saved immediately when you change a control. No Apply or OK button is needed.

## What each control does

| Label | Kind | Default | Persisted key | What it does |
|---|---|---|---|---|
| Spots: | Toggle button | Enabled | `IsSpotsEnabled` | Master on/off for DX spot display on the panadapter. |
| Memories: | Toggle button | Disabled | `IsMemoriesShownOnPanadapter` | Shows radio memory channels as spot-like markers on the panadapter. |
| Levels: | Slider | 3 | `SpotsStackLevels` | Number of vertical stacking rows used when spots crowd the same frequency area. Range: 1–10. |
| Position: | Slider | 50 | `SpotsPosition` | Vertical position of the spot row on the panadapter, as a percentage from top to bottom. Range: 0–100. |
| Font Size: | Slider | 16 | `SpotsFontSize` | Text size for spot labels. Range: 8–32. |
| Spot Lifetime: | Slider | 30 min | `SpotsLifetime` | How long a spot remains on the panadapter before expiring. The slider uses a non-linear scale: 10–55 seconds in 5-second steps, 5–55 minutes in 5-minute steps, then 1–24 hours in 1-hour steps. |
| Override Colors: | Toggle button | Disabled | `IsSpotsOverrideColorsEnabled` | When enabled, forces all spot text to a single color instead of per-source colors. |
| Spot text color picker | Button | #FFFF00 | `SpotsOverrideColor` | Opens a color picker to select the override text color. Active only when Override Colors: is Enabled. |
| Override Background: Enabled | Toggle button | Enabled | `IsSpotsOverrideBackgroundColorsEnabled` | Draws a filled background behind each spot label for legibility. |
| Override Background: Auto | Toggle button | Enabled | `IsSpotsOverrideToAutoBackgroundColorEnabled` | When enabled, automatically selects a background color to contrast with the spot text. When disabled, uses the manually chosen background color. |
| Spot background color picker | Button | #000000 | `SpotsOverrideBgColor` | Opens a color picker to select a fixed background color. Used when Override Background: Auto is disabled. |
| Background Opacity: | Slider | 48 | `SpotsOverrideBgOpacity` | Alpha transparency of the spot background. Range: 0 (fully transparent) to 100 (fully opaque). |
| Clear All Spots | Button | — | — | Immediately removes all spots from the panadapter. Does not affect incoming spot sources. |

## Tips

- Set Override Background: Auto to Enabled when you have many spot sources with different colors — the automatic contrast selection keeps labels readable regardless of the underlying spectrum color.
- If spots from different sources stack on top of each other, increase Levels: to spread them across more rows.
- The Spot Lifetime: slider snaps to named intervals (for example, "10 sec", "5 mins", "1 hr"). The display label updates as you drag.
- Turning Spots: to Disabled stops rendering on the panadapter but does not disconnect your DX cluster sources; the Total Spots: count continues to increment.

## Troubleshooting

- **No spots appear even though Spots: shows Enabled** — Check that at least one spot source is configured and connected in `Settings > SpotHub...`. The Total Spots: count will read 0 if no data is arriving.
- **Spot labels are unreadable against the panadapter background** — Enable Override Background: Enabled and Override Background: Auto, or lower the Background Opacity: slider to reduce the background density.
- **All spots disappear shortly after appearing** — Spot Lifetime: may be set very low. Open Spot Settings and drag the Spot Lifetime: slider to a higher value such as 30 mins.

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
