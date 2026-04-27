# Adjust spot background opacity

Use this page to control how transparent or opaque the background behind spot labels appears on the panadapter. Reducing opacity lets the spectrum show through; increasing it makes spot text easier to read against busy signals.

## Before you start

- Open the Spot Settings dialog by right-clicking the spots overlay on the panadapter.
- Confirm that "Override Background: Enabled" is active (the button shows "Enabled"). The opacity slider has no visible effect if the background is disabled.

## Steps

1. In the Spot Settings dialog, locate the **Background Opacity:** row.
2. Drag the slider left to decrease opacity (more transparent) or right to increase it (more opaque).
3. The numeric readout next to the slider updates immediately to reflect the current value.
4. Close the dialog. The change is saved automatically to `SpotsOverrideBgOpacity`.

## What each control does

| Control | Default | Valid range | Setting key |
|---|---|---|---|
| **Background Opacity:** slider | 48 | 0 – 100 | `SpotsOverrideBgOpacity` |
| **Override Background: Enabled** toggle | Enabled | Enabled / Disabled | `IsSpotsOverrideBackgroundColorsEnabled` |
| **Override Background: Auto** toggle | Enabled | Enabled / Disabled | `IsSpotsOverrideToAutoBackgroundColorEnabled` |
| Spot background color picker | `#000000` | Any color | `SpotsOverrideBgColor` |

## Tips

- A value of 0 makes the background fully transparent; spot text will still appear but with no backing fill.
- A value of 100 makes the background fully opaque. This can obscure weak signals beneath a spot label.
- When "Override Background: Auto" is Enabled, AetherSDR picks the background color automatically for contrast. The opacity slider still applies on top of that auto-selected color.
- If you want a specific background color, disable "Override Background: Auto" first, then use the spot background color picker to choose a color before adjusting opacity.

## Troubleshooting

- **Moving the slider has no effect** — Confirm "Override Background: Enabled" is showing "Enabled". If it shows "Disabled", click it to enable the background and then adjust the slider.

## Related

- [Spot Settings overview](overview.md)
- [Pick a custom background color for spots](pick-a-custom-background-color-for-spots.md)
- [Force a single spot text color](force-a-single-spot-text-color.md)
- [Turn spots on or off](turn-spots-on-or-off.md)
