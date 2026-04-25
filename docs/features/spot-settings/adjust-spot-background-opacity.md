# Adjust spot background opacity

Use this page to control how transparent or opaque the background fill behind spot labels appears on the panadapter. A lower value makes the background nearly invisible; a higher value makes it solid and easier to read against a busy spectrum display.

## Before you start

- Open the Spot Settings dialog by right-clicking on the panadapter spots overlay and selecting it from the context menu.
- Confirm that "Override Background:" is set to **Enabled**. The opacity slider has no visible effect if the background is disabled.

## Steps

1. In the Spot Settings dialog, locate the **Override Background:** row and confirm the **Enabled** toggle shows "Enabled". If it shows "Disabled", click it to enable it.
2. Locate the **Background Opacity:** slider.
3. Drag the slider left to decrease opacity (more transparent) or right to increase it (more opaque).
4. The numeric readout beside the slider updates immediately to show the current value.
5. The panadapter updates in real time. No confirmation step is required.

The value is saved automatically to `SpotsOverrideBgOpacity`.

## What each control does

| Control | Default | Range | Setting key | Behavior |
|---|---|---|---|---|
| **Override Background: Enabled** | Enabled | Enabled / Disabled | `IsSpotsOverrideBackgroundColorsEnabled` | Draws a background fill under spot text. Opacity has no effect when this is Disabled. |
| **Override Background: Auto** | Enabled | Enabled / Disabled | `IsSpotsOverrideToAutoBackgroundColorEnabled` | When Enabled, the background color is chosen automatically for contrast. When Disabled, the color set by the background color picker is used instead. |
| **Background Opacity:** | 48 | 0 – 100 | `SpotsOverrideBgOpacity` | Sets the alpha of the spot background fill. 0 is fully transparent; 100 is fully opaque. |

## Tips

- The default opacity of 48 provides a semi-transparent background that remains readable without obscuring the spectrum beneath.
- If **Override Background: Auto** is Enabled, the background color is chosen automatically for contrast with the spot text. To use a specific color at your chosen opacity, set **Override Background: Auto** to "Disabled" and use the background color picker instead.

## Troubleshooting

- **Changing the slider has no effect on the panadapter** — Confirm that **Override Background: Enabled** shows "Enabled". If the background override is off, no background is drawn and opacity has nothing to affect.
- **Background is invisible even at opacity 100** — Confirm that **Spots:** is set to "Enabled". If the master spots toggle is off, no spots or their backgrounds are rendered. See [Turn spots on or off](turn-spots-on-or-off.md).

## Related

- [Pick a custom background color for spots](pick-a-custom-background-color-for-spots.md)
- [Force a single spot text color](force-a-single-spot-text-color.md)
- [Turn spots on or off](turn-spots-on-or-off.md)
- [Spot Settings overview](overview.md)
