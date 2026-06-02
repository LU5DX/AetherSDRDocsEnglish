# Change spot density and vertical position

Use the Spot Settings dialog to control how many vertical rows of spots appear on the panadapter and where those rows sit relative to the spectrum display.

## Before you start

- Open a panadapter. Spots do not need to be actively receiving, but the panadapter must be visible.
- The **Spots:** toggle must be set to **Enabled** for changes to be visible. See [Turn spots on or off](turn-spots-on-or-off.md).

## Steps

1. Right-click the panadapter (or the spots overlay) to open the context menu, then select the option that opens the Spot Settings dialog.
2. The **Spot Settings** window opens.
3. To change density — the number of vertical stacking rows — drag the **Levels:** slider. The current value displays to the right of the slider. Valid range: 1–10.
4. To change vertical position — where the stack of rows sits on the panadapter — drag the **Position:** slider. The current value (0–100) displays to the right of the slider. Lower values move spots toward the top; higher values move them toward the bottom.
5. To show or hide the vertical lines drawn from the spectrum baseline up to each spot label, click the **Spot Lines:** toggle. The toggle reads **Enabled** or **Disabled**. See [What each control does](#what-each-control-does) below.
6. Changes take effect immediately. Close the dialog when finished.

## What each control does

| Control | Behavior | Default |
|---|---|---|
| **Spots:** toggle | Master toggle for DX spot display. Setting key: `IsSpotsEnabled`. | Enabled |
| **Memories:** toggle | Toggles memory channel overlays on the panadapter. Setting key: `IsMemorySpotsEnabled`. | Disabled |
| **Levels:** slider | Sets the number of vertical stacking rows available for spots. More rows reduce overlap when many spots are present on the same frequency range. Setting key: `SpotsMaxLevel`. | 3 |
| **Position:** slider | Sets the vertical starting position of the spot stack as a percentage of the panadapter height. Setting key: `SpotsStartingHeightPercentage`. | 50 |
| **Font Size:** slider | Sets the spot text size in points. Setting key: `SpotFontSize`. | 16 |
| **Spot Lifetime:** slider | How long spots remain before fading. Non-linear scale from 10 seconds to 24 hours. Stored in seconds. Setting key: `DxClusterSpotLifetimeSec`. | 10 sec |
| **Override Colors:** toggle | Forces a single text color for all spots. Setting key: `IsSpotsOverrideColorsEnabled`. | Disabled |
| **Spot text color picker** button | Opens a color dialog to pick the text color. Setting key: `SpotsOverrideColor`. | #FFFF00 |
| **Override Background: Enabled** toggle | Draws a background under spot text. Setting key: `IsSpotsOverrideBackgroundColorsEnabled`. | Enabled |
| **Override Background: Auto** toggle | Auto-picks background color for contrast. Setting key: `IsSpotsOverrideToAutoBackgroundColorEnabled`. | Enabled |
| **Spot background color picker** button | Opens a color dialog for background color. Setting key: `SpotsOverrideBgColor`. | #000000 |
| **Background Opacity:** slider | Alpha of spot background (0 = transparent, 100 = opaque). Setting key: `SpotsBackgroundOpacity`. | 48 |
| **Spot Lines:** toggle | Draws vertical lines from the spectrum baseline up to each spot label. Disable during contests to reduce visual clutter. Setting key: `IsSpotsLinesEnabled`. | Enabled |
| **Clear All Spots** button | Clears all spots from the panadapter. | N/A |

## Tips

- If spots overlap heavily, increase **Levels:** to give them more rows to stack into.
- If spots cover signal traces you need to see, lower the **Position:** value to push the stack toward the top of the panadapter, or raise it to move spots toward the bottom.
- During contests, disable **Spot Lines:** to reduce visual clutter without turning off spot labels entirely.
- The **Total Spots:** indicator in the dialog shows how many live spots are currently tracked, which helps you judge how many levels are needed.
- Use the **Clear All Spots** button to quickly remove all spots from the panadapter without changing any settings.

## Related

- [Turn spots on or off](turn-spots-on-or-off.md)
- [Enlarge or shrink the spot font](enlarge-or-shrink-the-spot-font.md)
- [Shorten or lengthen spot lifetime](shorten-or-lengthen-spot-lifetime.md)
- [Clear every spot from the panadapter](clear-every-spot-from-the-panadapter.md)