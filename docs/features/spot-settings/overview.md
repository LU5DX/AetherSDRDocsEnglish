# Spot Settings overview

The Spot Settings dialog controls how DX spots and memory channels appear on the panadapter — including whether they are shown at all, how many rows they occupy, where they sit vertically, how long they persist, and what colors they use. Open it from the panadapter context menu or the spots overlay; it does not require an active radio connection.

## How it works

AetherSDR draws DX spots as labeled markers directly on the panadapter display. Each spot is placed at its spotted frequency and stacked vertically when multiple spots fall close together. The dialog groups its controls into four areas: visibility toggles, layout, lifetime, and color.

**Visibility** — The `IsSpotsEnabled` master toggle must be on for any spots to appear. The `IsMemoriesShownOnPanadapter` toggle independently controls whether radio memory channels are rendered in the same overlay.

**Layout** — `SpotsStackLevels` sets how many vertical rows are available when spots crowd the same frequency. `SpotsPosition` sets the baseline height as a percentage from the bottom of the panadapter. `SpotsFontSize` controls the text size of spot labels.

**Lifetime** — `SpotsLifetime` determines how long a spot remains visible before it fades. The slider uses a non-linear scale: it steps through seconds (10–55 s), then minutes (5–55 min), then hours (1–24 hr), displaying a formatted label such as "15 mins" or "2 hrs".

**Color** — By default, spots are drawn using colors assigned by the spot source. `IsSpotsOverrideColorsEnabled` replaces all spot text with a single chosen color (`SpotsOverrideColor`, default `#FFFF00`). Background rendering is controlled by `IsSpotsOverrideBackgroundColorsEnabled` (default on) with `IsSpotsOverrideToAutoBackgroundColorEnabled` (default on) selecting a contrast color automatically. When auto mode is off, `SpotsOverrideBgColor` (default `#000000`) is used. `SpotsOverrideBgOpacity` sets the background alpha on a 0–100 scale (default 48).

The **Total Spots:** indicator at the bottom of the dialog shows how many spots are currently tracked.

## What each control does

| Label | Kind | Default | Setting key | Behavior |
|---|---|---|---|---|
| Spots: | Toggle button | Enabled | `IsSpotsEnabled` | Master on/off for the DX spot overlay. |
| Memories: | Toggle button | Disabled | `IsMemoriesShownOnPanadapter` | Shows radio memory channels as spot-like markers on the panadapter. |
| Levels: | Slider | 3 | `SpotsStackLevels` | Number of vertical stacking rows; range 1–10. |
| Position: | Slider | 50 | `SpotsPosition` | Baseline height of the spot row as a percentage (0–100) from the bottom. |
| Font Size: | Slider | 16 | `SpotsFontSize` | Spot label text size in points; range 8–32. |
| Spot Lifetime: | Slider | 30 min | `SpotsLifetime` | How long a spot is displayed; non-linear scale from 10 sec to 24 hr. |
| Override Colors: | Toggle button | Disabled | `IsSpotsOverrideColorsEnabled` | Forces all spot text to a single color instead of source-assigned colors. |
| Spot text color picker | Button | `#FFFF00` | `SpotsOverrideColor` | Opens a color picker to choose the override text color. Active only when Override Colors is Enabled. |
| Override Background: Enabled | Toggle button | Enabled | `IsSpotsOverrideBackgroundColorsEnabled` | Draws a filled background behind each spot label. |
| Override Background: Auto | Toggle button | Enabled | `IsSpotsOverrideToAutoBackgroundColorEnabled` | Automatically selects a background color to contrast with the text. When off, uses the manually chosen background color. |
| Spot background color picker | Button | `#000000` | `SpotsOverrideBgColor` | Opens a color picker to choose the background color. Used when Auto is off. |
| Background Opacity: | Slider | 48 | `SpotsOverrideBgOpacity` | Alpha of the spot background; range 0–100. |
| Clear All Spots | Button | — | — | Immediately removes all spots from the panadapter. This action is not undoable. |

## Tips

- If spots from different sources use colors that clash with your panadapter theme, enable Override Colors and pick a single readable color rather than adjusting each source individually.
- Set Override Background: Auto on whenever you change the text override color; AetherSDR will pick a contrasting background automatically.
- The Spot Lifetime slider snaps to defined steps. There is no arbitrary seconds entry; choose the nearest step available.
- Reducing Levels to 1 makes the overlay compact but causes spots at close frequencies to overlap rather than stack.

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
