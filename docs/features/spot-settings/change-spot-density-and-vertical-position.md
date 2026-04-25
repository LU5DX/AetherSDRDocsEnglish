# Change spot density and vertical position

Use Spot Settings to control how many vertical rows of spots appear on the panadapter and where on the panadapter they sit.

## Before you start

- Open a panadapter. Spot Settings is accessed from the panadapter context menu, not the main menu.
- Spots must be enabled. If the `IsSpotsEnabled` setting is off, spots will not appear regardless of density or position. See [Turn spots on or off](turn-spots-on-or-off.md).

## Steps

1. Right-click anywhere on the panadapter to open the context menu.
2. Select the spot overlay option to open the **Spot Settings** dialog.
3. To change spot density, drag the **Levels:** slider. Higher values add more vertical stacking rows, allowing more spots to appear simultaneously without overlapping. The range is 1–10; the default is 3.
4. To change vertical position, drag the **Position:** slider. The value is a percentage of the panadapter height from the top, ranging from 0 to 100; the default is 50.
5. Changes take effect immediately. Close the dialog when done.

## What each control does

| Control | What it does | Default | Range | Setting key |
|---|---|---|---|---|
| **Levels:** | Number of vertical stacking rows for spots. More rows allow denser spot display without overlap. | 3 | 1–10 | `SpotsStackLevels` |
| **Position:** | Vertical position of the spot band on the panadapter, as a percentage of panadapter height. | 50 | 0–100 | `SpotsPosition` |

## Tips

- If spots crowd together and overlap, increase **Levels:** to give them more rows to stack into.
- If spots obscure signals of interest, move them up or down with **Position:** until they sit in a clear area of the panadapter.
- The **Levels:** and **Position:** sliders display their current numeric value to the right of the slider as you drag.

## Related

- [Turn spots on or off](turn-spots-on-or-off.md)
- [Enlarge or shrink the spot font](enlarge-or-shrink-the-spot-font.md)
- [Shorten or lengthen spot lifetime](shorten-or-lengthen-spot-lifetime.md)
- [Overlay memory channels on the panadapter](overlay-memory-channels-on-the-panadapter.md)
