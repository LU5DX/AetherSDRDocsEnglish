# Adjust spot background opacity

Use this page to control how transparent or opaque the background behind spot labels appears on the panadapter. Reducing opacity lets the spectrum show through; increasing it makes spot text easier to read against busy signals.

## Before you start

- Open the Spot Settings dialog by right-clicking the spots overlay on the panadapter.
- Confirm that "Override Background: Enabled" toggle shows "Enabled" text and green background. The opacity slider has no visible effect if the background is disabled.

## Steps

1. In the Spot Settings dialog, locate the **Background Opacity:** row.
2. Drag the slider left to decrease opacity (more transparent) or right to increase it (more opaque).
3. The numeric readout next to the slider updates immediately to reflect the current value.
4. Close the dialog. The change is saved automatically to `SpotsBackgroundOpacity`.

## What each control does

| Control | Default | Valid range |
|---|---|---|
| **Background Opacity:** slider | 48 | 0 – 100 |
| **Override Background:** toggle | Enabled | Enabled / Disabled |
| **Override Background: Auto** toggle | Enabled | Enabled / Disabled |
| Spot background color picker | `#000000` | Any color |
| **Spots:** toggle | Enabled | Enabled / Disabled |
| **Memories:** toggle | Disabled | Enabled / Disabled |
| **Levels:** slider | 3 | 1 – 10 |
| **Position:** slider | 50 | 0 – 100 |
| **Font Size:** slider | 16 | 8 – 32 |
| **Spot Lifetime:** slider | Varies | 10 sec – 24 hrs (non-linear steps) |
| **Override Colors:** toggle | Disabled | Enabled / Disabled |
| Spot text color picker | `#FFFF00` | Any color |
| **Spot Lines:** toggle | Enabled | Enabled / Disabled |
| **Clear All Spots** button | N/A | N/A |

## Tips

- A value of 0 makes the background fully transparent; spot text will still appear but with no backing fill.
- A value of 100 makes the background fully opaque. This can obscure weak signals beneath a spot label.
- When "Override Background: Auto" is Enabled, AetherSDR picks the background color automatically for contrast. The opacity slider still applies on top of that auto-selected color.
- If you want a specific background color, disable "Override Background: Auto" first, then use the spot background color picker to choose a color before adjusting opacity.
- The **Spot Lines:** toggle controls whether vertical lines are drawn from the spectrum baseline up to each spot label. This setting is stored in `IsSpotsLinesEnabled`. Disable it during contests to reduce visual clutter.
- Toggle buttons display "Enabled" or "Disabled" text and use green/red background color indicators to show state.

## Troubleshooting

- **Moving the slider has no effect** — Confirm "Override Background:" toggle shows "Enabled" with green background. If it shows "Disabled" with red background, click it to enable the background and then adjust the slider.
- **Toggle buttons show the wrong state** — Each toggle button updates its text automatically when clicked. If the text doesn't match the background color, close and reopen the Spot Settings dialog to refresh.

## Related

- [Spot Settings overview](overview.md)
- [Pick a custom background color for spots](pick-a-custom-background-color-for-spots.md)
- [Force a single spot text color](force-a-single-spot-text-color.md)
- [Turn spots on or off](turn-spots-on-or-off.md)