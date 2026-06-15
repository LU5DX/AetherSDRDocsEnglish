# Pick a custom background color for spots

Set a specific background color that appears behind spot labels on the panadapter. Use this when the automatic color contrast is not suitable for your display or operating conditions.

## Before you start

- Open the Spot Settings dialog by right-clicking the spots overlay on a panadapter.
- Confirm that "Override Background: Enabled" is active (button shows "Enabled"). The background color picker has no effect when the background is disabled.
- Disable "Override Background: Auto" if you want your chosen color to take effect. When "Auto" is active, AetherSDR selects the background color automatically and ignores the manual color picker.

## Steps

1. Right-click the spots overlay on the panadapter and open Spot Settings.
2. Locate the **Override Background:** row.
3. If the "Enabled" button shows a red/disabled state, click it so it shows a green/enabled state. This persists to `IsSpotsOverrideBackgroundColorsEnabled`.
4. If the "Auto" button shows a green/enabled state, click it so it shows a red/disabled state. This persists to `IsSpotsOverrideToAutoBackgroundColorEnabled`. While "Auto" is active, the manual color picker is overridden.
5. Click the small color swatch button to the right of "Auto". This opens the system color dialog titled "Spot Background Color".
6. Select your desired color and confirm the selection.
7. The swatch updates immediately and the panadapter background behind spot labels changes to the chosen color. The value is persisted to `SpotsOverrideBgColor`.

## What each control does

| Label | Kind | Default | Notes |
|---|---|---|---|
| Spots: | Toggle button | Enabled | Master toggle for DX spot display. Persists to `IsSpotsEnabled`. The button label always shows "Enabled" regardless of state; the checked state is indicated by color (green = enabled, red = disabled). |
| Memories: | Toggle button | Disabled | Toggles memory channel overlays on panadapter. Setting key changed from `IsMemoriesShownOnPanadapter` in v0.9.7. Persists to `IsMemorySpotsEnabled`. The button label always shows "Enabled" regardless of state. |
| Levels: | Slider (1–10) | 3 | Vertical stacking rows for spots. Setting key changed from `SpotsStackLevels` in v0.9.7. Persists to `SpotsMaxLevel`. |
| Position: | Slider (0–100) | 50 | Vertical position on panadapter as a percentage. Setting key changed from `SpotsPosition` in v0.9.7. Persists to `SpotsStartingHeightPercentage`. |
| Font Size: | Slider (8–32) | 16 | Spot text size in points. Setting key changed from `SpotsFontSize` in v0.9.7. Persists to `SpotFontSize`. |
| Spot Lifetime: | Slider (non-linear steps) | (varies) | How long spots remain before fading. Non-linear scale from 10 seconds to 24 hours. Stored in seconds. Setting key changed from `SpotsLifetime` in v0.9.7. Migrates old minutes-based `DxClusterSpotLifetime` key on first read. Persists to `DxClusterSpotLifetimeSec`. |
| Override Colors: | Toggle button | Disabled | Forces a single text color for all spots. Persists to `IsSpotsOverrideColorsEnabled`. The button label always shows "Enabled" regardless of state. |
| Spot text color picker | Push button (swatch) | `#FFFF00` | Opens a color dialog for text color. Persists to `SpotsOverrideColor`. |
| Override Background: Enabled | Toggle button | Enabled | Draws a background under spot text. Persists to `IsSpotsOverrideBackgroundColorsEnabled`. The button label always shows "Enabled" regardless of state. |
| Override Background: Auto | Toggle button | Enabled | Auto-picks background color for contrast. When enabled, the manual color picker is ignored. Persists to `IsSpotsOverrideToAutoBackgroundColorEnabled`. The button label always shows "Enabled" regardless of state. |
| Spot background color picker | Push button (swatch) | `#000000` | Opens a color dialog for background color. Persists to `SpotsOverrideBgColor`. |
| Background Opacity: | Slider (0–100) | 48 | Alpha of spot background. 0 = fully transparent, 100 = fully opaque. Setting key changed from `SpotsOverrideBgOpacity` in v0.9.7. Persists to `SpotsBackgroundOpacity`. |
| Spot Lines: | Toggle button | Enabled | Draws vertical lines from the spectrum baseline up to each spot label. Disable during contests to reduce visual clutter. New in v0.9.7 (#2349). Persists to `IsSpotsLinesEnabled`. The button label always shows "Enabled" regardless of state. |
| Clear All Spots | Push button | — | Clears all spots from the panadapter. |

## Indicators

| Label | Meaning |
|---|---|
| Total Spots: | Shows count of live spots currently tracked. |

## Tips

- Setting opacity to 0 makes the background fully transparent regardless of the color chosen. If the background disappears after picking a color, check the "Background Opacity:" slider.
- "Override Background: Auto" defaults to "Enabled", so a freshly opened dialog will ignore any manual color until you disable "Auto".
- "Spot Lines:" defaults to "Enabled". If vertical lines from the spectrum baseline to spot labels are adding clutter during a contest, click the toggle so it shows a red/disabled state. This persists to `IsSpotsLinesEnabled`.

## Troubleshooting

- **Color picker has no visible effect on the panadapter** — Confirm "Override Background: Enabled" shows green/enabled and "Override Background: Auto" shows red/disabled. Both conditions must be met for a manual background color to display.
- **Background is invisible despite correct toggle states** — Check the "Background Opacity:" slider. If it is at 0, the background is fully transparent. See [Adjust spot background opacity](adjust-spot-background-opacity.md).
- **Spot lines are not visible** — Confirm "Spot Lines:" shows green/enabled. The toggle persists to `IsSpotsLinesEnabled`. This control was added in v0.9.7; if you are running an earlier version, the setting is not available.

## Related

- [Adjust spot background opacity](adjust-spot-background-opacity.md)
- [Force a single spot text color](force-a-single-spot-text-color.md)
- [Turn spots on or off](turn-spots-on-or-off.md)
- [Spot Settings overview](overview.md)