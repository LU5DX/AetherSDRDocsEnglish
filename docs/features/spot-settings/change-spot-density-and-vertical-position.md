# Change spot density and vertical position

Use the Spot Settings dialog to control how many vertical rows of spots appear on the panadapter and where those rows sit relative to the spectrum display.

## Before you start

- Open a panadapter. Spots do not need to be actively receiving, but the panadapter must be visible.
- The "Spots:" toggle must be set to "Enabled" for changes to be visible. See [Turn spots on or off](turn-spots-on-or-off.md).

## Steps

1. Right-click the panadapter (or the spots overlay) to open the context menu, then select the option that opens the Spot Settings dialog.
2. The **Spot Settings** window opens.
3. To change density — the number of vertical stacking rows — drag the **Levels:** slider. The current value displays to the right of the slider. Valid range: 1–10.
4. To change vertical position — where the stack of rows sits on the panadapter — drag the **Position:** slider. The current value (0–100) displays to the right of the slider. Lower values move spots toward the top; higher values move them toward the bottom.
5. Changes take effect immediately. Close the dialog when finished.

## What each control does

| Control | Behavior | Default | Range | Setting key |
|---|---|---|---|---|
| **Levels:** slider | Sets the number of vertical stacking rows available for spots. More rows reduce overlap when many spots are present on the same frequency range. | 3 | 1–10 | `SpotsStackLevels` |
| **Position:** slider | Sets the vertical starting position of the spot stack as a percentage of the panadapter height. | 50 | 0–100 | `SpotsPosition` |

## Tips

- If spots overlap heavily, increase **Levels:** to give them more rows to stack into.
- If spots cover signal traces you need to see, lower the **Position:** value to push the stack toward the top of the panadapter, or raise it to move spots toward the bottom.
- The **Total Spots:** indicator in the dialog shows how many live spots are currently tracked, which helps you judge how many levels are needed.

## Related

- [Turn spots on or off](turn-spots-on-or-off.md)
- [Enlarge or shrink the spot font](enlarge-or-shrink-the-spot-font.md)
- [Shorten or lengthen spot lifetime](shorten-or-lengthen-spot-lifetime.md)
- [Clear every spot from the panadapter](clear-every-spot-from-the-panadapter.md)
