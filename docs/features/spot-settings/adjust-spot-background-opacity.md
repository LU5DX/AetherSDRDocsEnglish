# Adjust spot background opacity

Use the **Background Opacity:** slider to control how transparent or opaque the background fill behind spot labels appears on the panadapter.

## Before you start

- Open the Spot Settings dialog by right-clicking the spots overlay on the panadapter.
- Confirm that "Override Background: Enabled" is active (the button reads "Enabled"). If it is not, the opacity slider has no visible effect.

## Steps

1. In the Spot Settings dialog, locate the "Override Background:" row.
2. Confirm the "Enabled" toggle button is checked (showing "Enabled"). If not, click "Enabled" to activate it.
3. Locate the "Background Opacity:" slider near the bottom of the dialog.
4. Drag the slider left to reduce opacity (more transparent) or right to increase it (more opaque).
5. The numeric label beside the slider updates immediately. The panadapter reflects the change in real time.

## What each control does

| Control | Default | Valid range | Setting key |
|---|---|---|---|
| "Override Background: Enabled" toggle | Enabled | Enabled / Disabled | `IsSpotsOverrideBackgroundColorsEnabled` |
| "Override Background: Auto" toggle | Enabled | Enabled / Disabled | `IsSpotsOverrideToAutoBackgroundColorEnabled` |
| "Background Opacity:" slider | 48 | 0 – 100 | `SpotsOverrideBgOpacity` |

## Tips

- A value of 0 makes the background fully transparent; spot text still appears but with no fill behind it.
- A value of 100 makes the background fully opaque. This can obscure the spectrum trace under dense spot clusters, so a mid-range value such as the default (48) is usually a practical starting point.
- The "Override Background: Auto" button, when "Enabled", lets AetherSDR choose the background color automatically for contrast. To use a fixed color instead, click "Auto" so it shows "Disabled", then use the spot background color picker. See [Pick a custom background color for spots](pick-a-custom-background-color-for-spots.md).

## Troubleshooting

- **Slider moves but panadapter background does not change** — Check that "Override Background: Enabled" shows "Enabled". If `IsSpotsEnabled` is also disabled (the "Spots:" toggle shows "Disabled"), no spot elements render at all. See [Turn spots on or off](turn-spots-on-or-off.md).

## Related

- [Pick a custom background color for spots](pick-a-custom-background-color-for-spots.md)
- [Force a single spot text color](force-a-single-spot-text-color.md)
- [Turn spots on or off](turn-spots-on-or-off.md)
- [Spot Settings overview](overview.md)
