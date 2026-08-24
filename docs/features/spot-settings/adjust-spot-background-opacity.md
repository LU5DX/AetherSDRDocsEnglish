# Spot settings

Use this page to control how DX spots and memories render on the panadapter. You can toggle their visibility, adjust stacking density and position, set the font size, control how long spots stay on screen, and override their colors.

## Before you start

- Open the Spot Settings dialog by right-clicking the spots overlay on the panadapter.

## What each control does

| Control                              | Default   | Valid range                        | Setting key                                  |
|--------------------------------------|-----------|------------------------------------|----------------------------------------------|
| **Spots:** toggle                    | Enabled   | Enabled / Disabled                 | `IsSpotsEnabled`                             |
| **Memories:** toggle                 | Disabled  | Enabled / Disabled                 | `IsMemorySpotsEnabled`                       |
| **Kiwi DX:** toggle                  | Disabled  | Enabled / Disabled                 | `ShowKiwiDxSpots`                            |
| **Levels:** slider                   | 3         | 1 – 10                             | `SpotsMaxLevel`                              |
| **Position:** slider                 | 50        | 0 – 100                            | `SpotsStartingHeightPercentage`              |
| **Font Size:** slider                | 16        | 8 – 32                             | `SpotFontSize`                               |
| **Spot Lifetime:** slider            | Varies    | 10 sec – 24 hrs (non-linear steps) | `DxClusterSpotLifetimeSec`                  |
| **Override Colors:** toggle          | Disabled  | Enabled / Disabled                 | `IsSpotsOverrideColorsEnabled`               |
| Spot text color picker               | `#FFFF00` | Any color                          | `SpotsOverrideColor`                         |
| **Override Background:** toggle      | Enabled   | Enabled / Disabled                 | `IsSpotsOverrideBackgroundColorsEnabled`     |
| **Override Background: Auto** toggle | Enabled   | Enabled / Disabled                 | `IsSpotsOverrideToAutoBackgroundColorEnabled`|
| Spot background color picker         | `#000000` | Any color                          | `SpotsOverrideBgColor`                       |
| **Background Opacity:** slider       | 48        | 0 – 100                            | `SpotsBackgroundOpacity`                     |
| **Spot Lines:** toggle               | Enabled   | Enabled / Disabled                 | `IsSpotsLinesEnabled`                        |
| **Clear All Spots** button           | N/A       | N/A                                | N/A                                          |

## Using the toggles

Toggle buttons display "Enabled" or "Disabled" text and use green/red background color indicators to show state.

1. Click **Spots:** to show or hide DX spots on the panadapter.
2. Click **Memories:** to show or hide memory channel overlays.
3. Click **Kiwi DX:** to overlay KiwiSDR Community DX database spots (beacons, utilities, time signals) on the band plan strip.
4. Click **Override Colors:** to force a single text color for all spots, then use the spot text color picker to choose the color.
5. Click **Override Background:** to draw a background under spot text.
6. Click **Override Background: Auto** to auto-pick the background color for contrast.
7. Click **Spot Lines:** to draw vertical lines from the spectrum baseline up to each spot label. Disable during contests to reduce visual clutter.
8. Click **Clear All Spots** to clear all spots from the panadapter.

## Adjusting sliders

1. Drag the **Levels:** slider to set how many vertical stacking rows spots can use.
2. Drag the **Position:** slider to set the vertical position of spots on the panadapter as a percentage.
3. Drag the **Font Size:** slider to set spot text size in points.
4. Drag the **Spot Lifetime:** slider to set how long spots remain before fading. The scale is non-linear, from 10 seconds to 24 hours.
5. Drag the **Background Opacity:** slider to set the alpha of the spot background. 0 is fully transparent, 100 is fully opaque.

## Picking colors

1. Click the spot text color picker to open a color dialog and choose the text color for spots.
2. Click the spot background color picker to open a color dialog and choose the background color for spot text.

## Tips

- When "Override Background: Auto" is Enabled, AetherSDR picks the background color automatically for contrast. The opacity slider still applies on top of that auto-selected color.
- If you want a specific background color, disable "Override Background: Auto" first, then use the spot background color picker to choose a color before adjusting opacity.
- A background opacity of 0 makes the background fully transparent; spot text will still appear but with no backing fill.
- A background opacity of 100 makes the background fully opaque. This can obscure weak signals beneath a spot label.
- Settings are saved automatically when you change them. Close the dialog to dismiss it.

## Troubleshooting

- **Moving the Background Opacity slider has no effect** — Confirm **Override Background:** toggle shows "Enabled" with green background. If it shows "Disabled" with red background, click it to enable the background and then adjust the slider.
- **Toggle buttons show the wrong state** — Each toggle button updates its text automatically when clicked. If the text doesn't match the background color, close and reopen the Spot Settings dialog to refresh.

## Related

- [Turn spots on or off](turn-spots-on-or-off.md)
- [Force a single spot text color](force-a-single-spot-text-color.md)
- [Pick a custom background color for spots](pick-a-custom-background-color-for-spots.md)
- [Adjust spot background opacity](adjust-spot-background-opacity.md)