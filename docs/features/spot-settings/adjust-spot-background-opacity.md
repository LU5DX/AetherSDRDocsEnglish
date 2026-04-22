# Adjust spot background opacity

Use the **Background Opacity:** slider to control how transparent or opaque the background box drawn behind each spot label appears on the panadapter.

## Before you start

- Open the Spot Settings dialog by right-clicking the spots overlay on any panadapter.
- Confirm that **Override Background:** **Enabled** is active (its toggle must show "Enabled"). The opacity slider has no visible effect if background drawing is off.

## Steps

1. In the Spot Settings dialog, locate the **Background Opacity:** row near the bottom of the controls.
2. Drag the slider left to decrease opacity (more transparent) or right to increase it (more opaque).
3. The numeric readout next to the slider updates immediately. The panadapter reflects the change in real time.
4. Close the dialog when finished. The value is saved automatically to `SpotsOverrideBgOpacity`.

## What each control does

| Control | Default | Valid range | Setting key |
|---|---|---|---|
| **Background Opacity:** slider | 48 | 0 – 100 | `SpotsOverrideBgOpacity` |
| **Override Background:** **Enabled** toggle | Enabled | Enabled / Disabled | `IsSpotsOverrideBackgroundColorsEnabled` |
| **Override Background:** **Auto** toggle | Enabled | Enabled / Disabled | `IsSpotsOverrideToAutoBackgroundColorEnabled` |
| Spot background color picker | `#000000` | Any color | `SpotsOverrideBgColor` |

## Tips

- A value of 0 makes the background fully transparent; spot text remains visible but has no backing box. A value of 100 makes the background fully opaque.
- If **Override Background:** **Auto** is enabled, AetherSDR chooses the background color automatically for contrast. The manual color picker and opacity slider still apply.

## Troubleshooting

- **Changing the slider has no effect on the panadapter** — Check that **Override Background:** **Enabled** shows "Enabled". If it shows "Disabled", click it once to enable background drawing, then adjust the slider.
- **Spots are not visible at all** — Confirm that the **Spots:** toggle shows "Enabled". See [Turn spots on or off](turn-spots-on-or-off.md).

## Related

- [Pick a custom background color for spots](pick-a-custom-background-color-for-spots.md)
- [Force a single spot text color](force-a-single-spot-text-color.md)
- [Turn spots on or off](turn-spots-on-or-off.md)
- [Spot Settings overview](overview.md)
