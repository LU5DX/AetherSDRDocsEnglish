# Pick a custom background color for spots

Set a specific background color that appears behind spot labels on the panadapter. Use this when the automatic color contrast is not suitable for your display or operating conditions.

## Before you start

- Open the Spot Settings dialog by right-clicking the spots overlay on a panadapter.
- Confirm that "Override Background: Enabled" is active (button reads "Enabled"). The background color picker has no effect when the background is disabled.
- Disable "Override Background: Auto" if you want your chosen color to take effect. When "Auto" is active, AetherSDR selects the background color automatically and ignores the manual color picker.

## Steps

1. Right-click the spots overlay on the panadapter and open Spot Settings.
2. Locate the **Override Background:** row.
3. If the "Enabled" button shows "Disabled", click it so it reads "Enabled". This persists to `IsSpotsOverrideBackgroundColorsEnabled`.
4. If the "Auto" button shows "Enabled", click it so it reads "Disabled". This persists to `IsSpotsOverrideToAutoBackgroundColorEnabled`. While "Auto" is active, the manual color picker is overridden.
5. Click the small color swatch button to the right of "Auto". This opens the system color dialog titled "Spot Background Color".
6. Select your desired color and confirm the selection.
7. The swatch updates immediately and the panadapter background behind spot labels changes to the chosen color. The value is persisted to `SpotsOverrideBgColor`.

## What each control does

| Label | Kind | Default | Notes |
|---|---|---|---|
| Override Background: Enabled | Toggle button | Enabled | Persists to `IsSpotsOverrideBackgroundColorsEnabled`. |
| Override Background: Auto | Toggle button | Enabled | Persists to `IsSpotsOverrideToAutoBackgroundColorEnabled`. When enabled, the manual color picker is ignored. |
| Spot background color picker | Push button (swatch) | `#000000` | Opens a color dialog. Persists to `SpotsOverrideBgColor`. |
| Background Opacity: | Slider (0–100) | 48 | Alpha of spot background. 0 = fully transparent, 100 = fully opaque. Persists to `SpotsBackgroundOpacity`. Setting key changed from `SpotsOverrideBgOpacity` in v0.9.7. |
| Spot Lines: | Toggle button | Enabled | Draws vertical lines from the spectrum baseline up to each spot label. Disable during contests to reduce visual clutter. Persists to `IsSpotsLinesEnabled`. New in v0.9.7. |

## Tips

- Setting opacity to 0 makes the background fully transparent regardless of the color chosen. If the background disappears after picking a color, check the "Background Opacity:" slider.
- "Override Background: Auto" defaults to "Enabled", so a freshly opened dialog will ignore any manual color until you disable "Auto".
- "Spot Lines:" defaults to "Enabled". If vertical lines from the spectrum baseline to spot labels are adding clutter during a contest, click the toggle so it reads "Disabled". This persists to `IsSpotsLinesEnabled`.

## Troubleshooting

- **Color picker has no visible effect on the panadapter** — Confirm "Override Background: Enabled" reads "Enabled" and "Override Background: Auto" reads "Disabled". Both conditions must be met for a manual background color to display.
- **Background is invisible despite correct toggle states** — Check the "Background Opacity:" slider. If it is at 0, the background is fully transparent. See [Adjust spot background opacity](adjust-spot-background-opacity.md).
- **Spot lines are not visible** — Confirm "Spot Lines:" reads "Enabled". The toggle persists to `IsSpotsLinesEnabled`. This control was added in v0.9.7; if you are running an earlier version, the setting is not available.

## Related

- [Adjust spot background opacity](adjust-spot-background-opacity.md)
- [Force a single spot text color](force-a-single-spot-text-color.md)
- [Turn spots on or off](turn-spots-on-or-off.md)
- [Spot Settings overview](overview.md)