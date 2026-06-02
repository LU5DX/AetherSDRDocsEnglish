# Shorten or lengthen spot lifetime

Use the **Spot Lifetime:** slider in Spot Settings to control how long DX spots remain visible on the panadapter before they expire.

## Before you start

- Spots must be displayed on the panadapter. If spots are not visible, confirm the **Spots:** toggle shows "Enabled" in Spot Settings.
- Open Spot Settings by right-clicking the spots overlay on the panadapter.

## Steps

1. Right-click the spots overlay on the panadapter to open the **Spot Settings** dialog.
2. Locate the **Spot Lifetime:** row.
3. Drag the slider left to shorten the lifetime or right to lengthen it. The label to the right of the slider updates immediately, showing the current value in seconds, minutes, or hours (for example, `30 secs`, `15 mins`, `2 hrs`).
4. Release the slider. The new value is saved automatically.

## What each control does

| Control                       | Behavior                                                                                                                                                                                                                                                                                               | Default |
|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| **Spots:** toggle button      | Master toggle for DX spot display. Click to toggle between Enabled and Disabled. Saved to `IsSpotsEnabled`.                                                                                                                                                                                            | Enabled |
| **Memories:** toggle button   | Toggles memory channel overlays on the panadapter. Click to toggle between Enabled and Disabled. Saved to `IsMemorySpotsEnabled`. Setting key changed from `IsMemoriesShownOnPanadapter` in v0.9.7.                                                                                                     | Disabled |
| **Levels:** slider            | Sets the number of vertical stacking rows for spots. Drag to set from 1 to 10. The default is 3. Saved to `SpotsMaxLevel`. Setting key changed from `SpotsStackLevels` in v0.9.7.                                                                                                                       | 3       |
| **Position:** slider          | Sets the vertical position of spots on the panadapter as a percentage. Drag left to move spots down, right to move them up. Range is 0 to 100. The default is 50. Saved to `SpotsStartingHeightPercentage`. Setting key changed from `SpotsPosition` in v0.9.7.                                         | 50      |
| **Font Size:** slider         | Sets the spot text size in points. Drag to set from 8 to 32. The default is 16. Saved to `SpotFontSize`. Setting key changed from `SpotsFontSize` in v0.9.7.                                                                                                                                           | 16      |
| **Spot Lifetime:** slider     | Sets how long a spot remains on the panadapter before it fades. The scale is non-linear: the lower portion steps in 5-second increments (10 sec – 55 sec), the middle portion steps in 5-minute increments (5 min – 55 min), and the upper portion steps in 1-hour increments (1 hr – 24 hrs / 1 day). | 30 min  |
| **Override Colors:** toggle button | Forces a single text color for all spots. Click to toggle between Enabled and Disabled. Saved to `IsSpotsOverrideColorsEnabled`.                                                                                                                                                                    | Disabled |
| **Spot text color picker**    | Opens a color dialog to pick the text color when Override Colors is enabled. The default is bright yellow (#FFFF00). Saved to `SpotsOverrideColor`.                                                                                                                                                    | #FFFF00 |
| **Override Background: Enabled** toggle button | Draws a background under spot text. Click to toggle between Enabled and Disabled. Saved to `IsSpotsOverrideBackgroundColorsEnabled`.                                                                                                                                                     | Enabled |
| **Override Background: Auto** toggle button | Auto-picks background color for contrast. Click to toggle between Enabled and Disabled. Saved to `IsSpotsOverrideToAutoBackgroundColorEnabled`.                                                                                                                                             | Enabled |
| **Spot background color picker** | Opens a color dialog to pick the background color when Override Background is enabled and Auto is disabled. The default is black (#000000). Saved to `SpotsOverrideBgColor`.                                                                                                                            | #000000 |
| **Background Opacity:** slider | Sets the alpha of the spot background. 0 is fully transparent, 100 is fully opaque. The default is 48. Saved to `SpotsBackgroundOpacity`. Setting key changed from `SpotsOverrideBgOpacity` in v0.9.7.                                                                                                | 48      |
| **Spot Lines:** toggle button | Draws vertical lines from the spectrum baseline up to each spot label. Click to toggle between Enabled and Disabled. Disable during contests to reduce visual clutter. Saved to `IsSpotsLinesEnabled`. Added in v0.9.7 (#2349).                                                                         | Enabled |
| **Clear All Spots** button    | Clears all spots from the panadapter immediately.                                                                                                                                                                                                                                                      | —       |

**Indicator:**

| Indicator        | Meaning                                                   |
|------------------|-----------------------------------------------------------|
| **Total Spots:** | Shows the count of live spots currently being tracked.    |

## Tips

- The slider uses a non-linear scale. Small movements near the left end adjust lifetime by seconds; movements near the right end adjust by hours. Position the slider carefully when targeting a specific value.
- The displayed label rounds to the nearest step: values under 60 seconds show as `sec`, values under 1 hour show as `min` or `mins`, and values of 1 hour or more show as `hr`, `hrs`, or `1 day`.
- If vertical lines make the panadapter feel cluttered during a contest, click **Spot Lines:** to set it to Disabled. The change takes effect immediately and is saved automatically.
- Use the **Override Colors** and **Override Background** toggles to customize spot readability against different panadapter backgrounds.

## Troubleshooting

- **Old spots still appear after reducing lifetime** — Existing spots that arrived before the change will expire based on the previous setting. New spots will use the updated lifetime. Click **Clear All Spots** to remove existing spots immediately.

## Related

- [Spot Settings overview](overview.md)
- [Turn spots on or off](turn-spots-on-or-off.md)
- [Clear every spot from the panadapter](clear-every-spot-from-the-panadapter.md)