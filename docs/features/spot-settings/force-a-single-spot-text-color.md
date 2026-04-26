# Force a single spot text color

By default, AetherSDR colors each DX spot according to its source or mode. This page explains how to override that behavior and display all spot text in one color of your choosing.

## Before you start

- Spots must be enabled. If the "Spots:" toggle shows "Disabled", see [Turn spots on or off](turn-spots-on-or-off.md) first.
- Open the Spot Settings dialog by right-clicking the spots overlay on the panadapter.

## Steps

1. In the Spot Settings dialog, locate the "Override Colors:" row.
2. Click the toggle button so it reads "Enabled". This activates `IsSpotsOverrideColorsEnabled` and forces all spot text to a single color.
3. Click the small color swatch button immediately to the right of the "Enabled" toggle. A color picker dialog opens.
4. Select the color you want and confirm. The swatch updates to reflect your choice, and all spot text on the panadapter changes immediately.

## What each control does

| Control | What it does | Default | Setting key |
|---|---|---|---|
| Override Colors: toggle | Enables or disables single-color override for all spot text. | Disabled | `IsSpotsOverrideColorsEnabled` |
| Spot text color picker | Opens the color picker dialog to select the override text color. | `#FFFF00` | `SpotsOverrideColor` |

## Tips

- The color you pick is saved immediately. There is no separate Save button.
- If you want high contrast, choose a color that differs from your panadapter background. Yellow (`#FFFF00`) is the default because it reads clearly on dark backgrounds.
- The override applies to all spots regardless of their source (DX cluster, RBN, WSJTX, etc.).

## Troubleshooting

- **Toggle shows "Enabled" but spot colors have not changed** — Confirm that "Spots:" is set to "Enabled" in the same dialog. If spots are disabled, the override has no visible effect.
- **Color picker closes without changing the swatch** — You dismissed the dialog without confirming a color. Click the swatch button again and select a color before closing.

## Related

- [Turn spots on or off](turn-spots-on-or-off.md)
- [Pick a custom background color for spots](pick-a-custom-background-color-for-spots.md)
- [Adjust spot background opacity](adjust-spot-background-opacity.md)
- [Enlarge or shrink the spot font](enlarge-or-shrink-the-spot-font.md)
