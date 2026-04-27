# Force a single spot text color

Override the per-spot colors assigned by your DX cluster source and render all spot labels in one chosen color instead. Useful when the default colors clash with your panadapter theme or are hard to read.

## Before you start

- Spots must be enabled. If the `IsSpotsEnabled` toggle reads "Disabled", enable it first — see [Turn spots on or off](turn-spots-on-or-off.md).
- Open the Spot Settings dialog by right-clicking the spots overlay on the panadapter.

## Steps

1. In the Spot Settings dialog, locate the **Override Colors:** row.
2. Click the toggle button so it reads **Enabled**. This persists as `IsSpotsOverrideColorsEnabled`.
3. Click the color swatch button immediately to the right of **Enabled**. A color picker dialog opens.
4. Select the color you want for all spot text labels, then click **OK**.
5. The swatch updates to show your chosen color. All spots on the panadapter immediately render in that color. The chosen value is persisted as `SpotsOverrideColor`.

To revert to per-spot colors, click the **Override Colors:** toggle again so it reads **Disabled**.

## What each control does

| Control | Default | Persisted key | Behavior |
|---|---|---|---|
| **Override Colors:** toggle | Disabled | `IsSpotsOverrideColorsEnabled` | When Enabled, forces all spot text to a single color instead of source-assigned colors. |
| Spot text color picker (swatch button) | `#FFFF00` | `SpotsOverrideColor` | Opens the color picker dialog. The selected color is applied to all spot labels when Override Colors is Enabled. |

## Tips

- The color picker only takes effect while **Override Colors:** reads **Enabled**. You can pre-select a color while the toggle is still Disabled; it will apply the next time you enable the override.
- If spot text is still hard to read after setting the color, adjust the background contrast using the **Override Background:** controls — see [Pick a custom background color for spots](pick-a-custom-background-color-for-spots.md) and [Adjust spot background opacity](adjust-spot-background-opacity.md).

## Related

- [Turn spots on or off](turn-spots-on-or-off.md)
- [Pick a custom background color for spots](pick-a-custom-background-color-for-spots.md)
- [Adjust spot background opacity](adjust-spot-background-opacity.md)
