# Change spot density and vertical position

Use the Spot Settings dialog to control how many vertical rows of spots appear on the panadapter and where those rows sit relative to the display height.

## Before you start

- AetherSDR must be running. A radio connection is not required to adjust these settings.
- Open the Spot Settings dialog by right-clicking the spots overlay or panadapter to access the context menu.

## Steps

1. Right-click the panadapter to open the context menu, then select the option to open **Spot Settings**.
2. Locate the **Levels:** slider. Drag it left or right to set the number of vertical stacking rows used to display spots. The current value appears to the right of the slider.
3. Locate the **Position:** slider. Drag it left or right to set the vertical position of the spot rows on the panadapter. The current value appears to the right of the slider.
4. Changes take effect immediately. Close the dialog when finished.

## What each control does

| Control | What it does | Default | Range | Setting key |
|---|---|---|---|---|
| **Levels:** | Sets the number of vertical stacking rows for spots. More rows allow denser spot display without overlap. | 3 | 1–10 | `SpotsStackLevels` |
| **Position:** | Sets the vertical position of the spot band on the panadapter, expressed as a percentage of display height. Lower values move spots toward the top; higher values move them toward the bottom. | 50 | 0–100 | `SpotsPosition` |

## Tips

- If spots are crowding each other, increase **Levels:** to give them more rows to spread across.
- If spots are obscuring signals of interest, adjust **Position:** to move the entire spot band away from the busy part of the display.
- The **Spots:** master toggle must be set to **Enabled** for spots to appear regardless of these settings.

## Troubleshooting

- **Spots do not appear after adjusting Levels: or Position:** — Confirm the **Spots:** toggle shows **Enabled**. If it shows **Disabled**, click it to enable spot display.

## Related

- [Turn spots on or off](turn-spots-on-or-off.md)
- [Enlarge or shrink the spot font](enlarge-or-shrink-the-spot-font.md)
- [Shorten or lengthen spot lifetime](shorten-or-lengthen-spot-lifetime.md)
- [Spot Settings overview](overview.md)
