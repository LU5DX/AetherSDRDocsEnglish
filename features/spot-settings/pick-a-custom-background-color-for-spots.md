# Pick a custom background color for spots

This page explains how to set a specific background color for spot labels on the panadapter. Use this when you want consistent, manually chosen background colors rather than the automatic contrast-based selection.

## Before you start

- Open the Spot Settings dialog by right-clicking the spots overlay on the panadapter.
- Confirm that `IsSpotsOverrideBackgroundColorsEnabled` is active — the "Override Background: Enabled" button must be checked. If it is not, the background color picker has no effect.
- Disable automatic background color selection: the "Override Background: Auto" button must be unchecked. While Auto is active, AetherSDR ignores the manually chosen color.

## Steps

1. Right-click the spots overlay on the panadapter and open Spot Settings.
2. Locate the **Override Background:** row.
3. If the "Enabled" button shows as unchecked, click it so it reads "Enabled".
4. If the "Auto" button shows as checked, click it so it reads unchecked. This disables automatic color selection and enables the manual color picker.
5. Click the small color swatch button (the square to the right of "Auto") to open the color picker.
6. Select your desired background color in the color dialog and confirm. The swatch updates immediately and the color is saved to `SpotsOverrideBgColor`.

## What each control does

| Control | Default | Persisted setting | Behavior |
|---|---|---|---|
| Override Background: Enabled | Enabled | `IsSpotsOverrideBackgroundColorsEnabled` | Draws a background behind spot label text. Must be enabled for any background color setting to apply. |
| Override Background: Auto | Enabled | `IsSpotsOverrideToAutoBackgroundColorEnabled` | When enabled, AetherSDR picks a background color automatically for contrast. Disable this to use a manually chosen color. |
| Spot background color picker | `#000000` | `SpotsOverrideBgColor` | Opens the color picker dialog. The selected color is used as the spot background when Auto is off. |
| Background Opacity: | 48 | `SpotsOverrideBgOpacity` | Controls the transparency of the spot background, from 0 (fully transparent) to 100 (fully opaque). |

## Tips

- If you change the background color but spots still show the automatic color, check that "Override Background: Auto" is unchecked. Auto takes precedence over the manual color.
- The background color and opacity are independent. After choosing a color, adjust the **Background Opacity:** slider to control how strongly it renders over the panadapter.

## Troubleshooting

- **Color picker opens but changes have no visible effect** — "Override Background: Auto" is still checked. Uncheck it so the manual color in `SpotsOverrideBgColor` is used.
- **No background appears behind spot text at all** — "Override Background: Enabled" is unchecked. Click it so it reads "Enabled".
- **Background is invisible despite correct color and Enabled state** — The **Background Opacity:** slider may be set to 0. Raise it above 0.

## Related

- [Adjust spot background opacity](adjust-spot-background-opacity.md)
- [Force a single spot text color](force-a-single-spot-text-color.md)
- [Turn spots on or off](turn-spots-on-or-off.md)
- [Spot Settings overview](overview.md)
