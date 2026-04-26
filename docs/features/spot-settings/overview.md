# Spot Settings overview

The Spot Settings dialog controls how DX spots and memory channels appear on the panadapter — including whether they are shown at all, how many rows they occupy, where they sit vertically, how long they persist, and how their text and backgrounds are colored.

## Before you start

- A panadapter must be open. The Spot Settings dialog is not accessible from the main menu.
- To receive live DX spots, configure at least one spot source via `Settings > SpotHub...`.

## How it works

Open the dialog by right-clicking the spots overlay on the panadapter and selecting the spot settings option from the context menu. The dialog is titled "Spot Settings" and requires no radio connection to operate — all changes are saved immediately to persisted settings.

A **Total Spots:** indicator at the top of the dialog shows the count of live spots currently tracked.

The controls divide into four areas:

**Visibility and density** — whether spots and memories are drawn at all, how many stacking rows are used, and where on the panadapter they sit.

**Appearance** — font size and how long each spot remains visible before it fades.

**Text color** — an optional override that forces every spot to use a single color instead of the source-assigned color.

**Background** — a configurable background drawn behind spot text, with automatic contrast mode, manual color selection, and opacity control.

Clicking `Clear All Spots` removes every spot from the panadapter immediately. This action is not persisted; spots will reappear as new ones arrive from the configured sources.

## What each control does

| Label | Kind | Default | Setting key | Behavior |
|---|---|---|---|---|
| Spots: | Toggle button | Enabled | `IsSpotsEnabled` | Master toggle for DX spot display. |
| Memories: | Toggle button | Disabled | `IsMemoriesShownOnPanadapter` | Shows radio memory channels as spot-like markers on the panadapter. |
| Levels: | Slider | 3 | `SpotsStackLevels` | Sets the number of vertical stacking rows for spots (range: 1–10). |
| Position: | Slider | 50 | `SpotsPosition` | Sets the vertical position of the spot band on the panadapter as a percentage from the top (range: 0–100). |
| Font Size: | Slider | 16 | `SpotsFontSize` | Sets the spot label text size in points (range: 8–32). |
| Spot Lifetime: | Slider | 30 min | `SpotsLifetime` | Sets how long a spot remains visible before fading. The slider uses a non-linear scale: 10–55 seconds in 5-second steps, then 5–55 minutes in 5-minute steps, then 1–24 hours in 1-hour steps. |
| Override Colors: | Toggle button | Disabled | `IsSpotsOverrideColorsEnabled` | When enabled, all spot text is drawn in the color selected by the spot text color picker instead of each spot's source-assigned color. |
| Spot text color picker | Color button | `#FFFF00` | `SpotsOverrideColor` | Opens a color chooser for the override text color. Active only when Override Colors: is Enabled. |
| Override Background: Enabled | Toggle button | Enabled | `IsSpotsOverrideBackgroundColorsEnabled` | Draws a filled background behind each spot label. |
| Override Background: Auto | Toggle button | Enabled | `IsSpotsOverrideToAutoBackgroundColorEnabled` | When enabled, AetherSDR selects the background color automatically for contrast. When disabled, the manually chosen background color is used. |
| Spot background color picker | Color button | `#000000` | `SpotsOverrideBgColor` | Opens a color chooser for the manual background color. Used when Override Background: Auto is disabled. |
| Background Opacity: | Slider | 48 | `SpotsOverrideBgOpacity` | Sets the transparency of the spot background (range: 0–100, where 0 is fully transparent and 100 is fully opaque). |
| Clear All Spots | Button | — | — | Immediately removes all spots from the panadapter. Not persisted. |

## Tips

- If spots are hard to read against a busy panadapter, enable Override Background: Enabled and increase Background Opacity: to improve contrast without changing spot colors.
- The Spot Lifetime: slider snaps to predefined steps. The current value is shown as a formatted label (for example, "30 mins" or "2 hrs") next to the slider.
- Levels: and Position: interact: increasing Levels: expands the spot band downward from the Position: anchor point. Adjust Position: first, then tune Levels:.

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
