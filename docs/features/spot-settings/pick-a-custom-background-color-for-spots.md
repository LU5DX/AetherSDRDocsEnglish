# Pick a custom background color for spots

This page explains how to set a specific background color that appears behind spot labels on the panadapter, instead of letting AetherSDR choose the color automatically.

## Before you start

- Open the Spot Settings dialog by right-clicking on the panadapter and selecting it from the spots overlay context menu.
- Confirm that the `IsSpotsOverrideBackgroundColorsEnabled` toggle is active — the background color picker has no effect if background override is off.

## Steps

1. In the Spot Settings dialog, locate the **Override Background:** row.
2. Confirm the **Enabled** toggle button shows **Enabled**. If it shows **Disabled**, click it to enable background overrides. This controls `IsSpotsOverrideBackgroundColorsEnabled`.
3. Click the **Auto** toggle button so it shows **Disabled**. While **Auto** is enabled, AetherSDR picks the background color automatically and ignores your custom color. Disabling it activates `IsSpotsOverrideToAutoBackgroundColorEnabled` = False.
4. Click the small color swatch button to the right of **Auto**. This is the spot background color picker and opens a color chooser dialog.
5. Select your desired color in the color dialog and confirm the selection.
6. The swatch updates to show the chosen color. The value is saved immediately to `SpotsOverrideBgColor`.

## What each control does

| Control | What it does | Default | Setting key |
|---|---|---|---|
| **Override Background: Enabled** toggle | Draws a background behind spot text. When **Disabled**, no background is drawn and all background controls are inactive. | Enabled | `IsSpotsOverrideBackgroundColorsEnabled` |
| **Override Background: Auto** toggle | When **Enabled**, AetherSDR automatically selects a contrasting background color and ignores the custom color picker. Set to **Disabled** to use your chosen color. | Enabled | `IsSpotsOverrideToAutoBackgroundColorEnabled` |
| Spot background color picker | Opens a color dialog to choose the custom background color. Active only when **Auto** is **Disabled**. | `#000000` | `SpotsOverrideBgColor` |
| **Background Opacity:** slider | Controls the transparency of the spot background. Range 0–100; default 48. | 48 | `SpotsOverrideBgOpacity` |

## Tips

- The custom color set here only takes effect when both **Enabled** is active and **Auto** is **Disabled**. If spots still show automatic background colors after picking a color, check that **Auto** reads **Disabled**.
- To fine-tune how visible the background is without changing the color, adjust the **Background Opacity:** slider after setting your color. See [Adjust spot background opacity](adjust-spot-background-opacity.md).

## Troubleshooting

- **Background color does not change after picking a new color** — Check that **Override Background:** shows **Enabled** and that the **Auto** toggle shows **Disabled**. If **Auto** is **Enabled**, the custom color is ignored.
- **No background appears at all** — The **Enabled** toggle under **Override Background:** is set to **Disabled**. Click it so it reads **Enabled**.

## Related

- [Adjust spot background opacity](adjust-spot-background-opacity.md)
- [Force a single spot text color](force-a-single-spot-text-color.md)
- [Turn spots on or off](turn-spots-on-or-off.md)
- [Spot Settings overview](overview.md)
