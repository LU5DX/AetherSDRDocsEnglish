# Pick a custom background color for spots

This page explains how to set a specific background color for DX spot labels on the panadapter. Use this when you want a fixed color rather than the automatic contrast-based color that AetherSDR selects by default.

## Before you start

- Open the Spot Settings dialog by right-clicking the spots overlay on the panadapter.
- Confirm that `IsSpotsOverrideBackgroundColorsEnabled` is active — the "Override Background: Enabled" toggle must be on, or the background color has no effect.

## Steps

1. In the Spot Settings dialog, locate the **Override Background:** row.
2. Click the **Enabled** toggle button so it shows "Enabled". This activates the spot background and persists `IsSpotsOverrideBackgroundColorsEnabled`.
3. Click the **Auto** toggle button so it shows "Disabled". While Auto is enabled, AetherSDR ignores your custom color and picks one automatically for contrast. Turning it off allows your chosen color to take effect. This persists `IsSpotsOverrideToAutoBackgroundColorEnabled`.
4. Click the small color swatch button to the right of **Auto**. The system color picker opens.
5. Choose your desired color and confirm. AetherSDR applies the color immediately and saves it as `SpotsOverrideBgColor`.
6. Adjust the **Background Opacity:** slider if you want the background more or less transparent. The default value is 48. This persists `SpotsOverrideBgOpacity`.

## What each control does

| Control | Behavior | Default | Setting key |
|---|---|---|---|
| **Override Background: Enabled** toggle | Draws a colored background behind spot text. | Enabled | `IsSpotsOverrideBackgroundColorsEnabled` |
| **Override Background: Auto** toggle | When enabled, AetherSDR automatically picks a background color for contrast. Disable this to use your custom color. | Enabled | `IsSpotsOverrideToAutoBackgroundColorEnabled` |
| Spot background color picker (swatch button) | Opens the color picker dialog to set a fixed background color. | `#000000` | `SpotsOverrideBgColor` |
| **Background Opacity:** slider | Sets the transparency of the spot background. Range: 0–100. | 48 | `SpotsOverrideBgOpacity` |

## Tips

- If your chosen color does not appear after picking it, check that **Override Background: Auto** is set to "Disabled". Auto mode overrides the manual color selection.
- A low opacity value (closer to 0) makes the background nearly transparent. If spot text becomes hard to read, increase the **Background Opacity:** slider value.

## Troubleshooting

- **Custom color is ignored and the background color keeps changing** — The **Override Background: Auto** toggle is still "Enabled". Click it to disable Auto mode, then your color from `SpotsOverrideBgColor` will be used.
- **Background does not appear at all** — The **Override Background: Enabled** toggle is set to "Disabled". Click it to enable it.
- **Background appears but is invisible** — The **Background Opacity:** slider may be set to 0. Increase it.

## Related

- [Adjust spot background opacity](adjust-spot-background-opacity.md)
- [Force a single spot text color](force-a-single-spot-text-color.md)
- [Turn spots on or off](turn-spots-on-or-off.md)
- [Spot Settings overview](overview.md)
