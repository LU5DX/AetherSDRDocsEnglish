# Change spot density and vertical position

Use the Spot Settings dialog to control how many stacking rows of spots appear on the panadapter and where on the vertical axis those rows sit.

## Before you start

- AetherSDR must be running. A radio connection is not required to change these settings.
- Spots must be visible on the panadapter. If they are not, see [Turn spots on or off](turn-spots-on-or-off.md).

## Steps

1. Right-click the spots overlay on the panadapter to open the panadapter context menu, then select the option that opens **Spot Settings**.
2. Locate the **Levels:** slider. Drag it left to reduce the number of vertical stacking rows; drag it right to increase them. The current value appears to the right of the slider. Valid range: 1–10.
3. Locate the **Position:** slider. Drag it left to move the spot rows toward the top of the panadapter; drag it right to move them toward the bottom. The current value is a percentage (0–100) shown to the right of the slider.
4. Close the dialog. Changes take effect immediately and are saved automatically.

## What each control does

| Control | What it does | Default | Range | Setting key |
|---|---|---|---|---|
| **Levels:** | Sets the number of vertical stacking rows used when spots overlap at similar frequencies. | 3 | 1–10 | `SpotsStackLevels` |
| **Position:** | Sets the vertical position of the spot rows as a percentage of the panadapter height. | 50 | 0–100 | `SpotsPosition` |

## Tips

- If spots overlap and call signs are unreadable, increase **Levels:** to give them more rows to stack into.
- If spots obscure signal activity you want to watch, move **Position:** toward 0 to push the rows toward the top of the panadapter.
- The **Total Spots:** indicator in the dialog shows how many spots are currently tracked, which can help you judge how many levels you need.

## Related

- [Turn spots on or off](turn-spots-on-or-off.md)
- [Enlarge or shrink the spot font](enlarge-or-shrink-the-spot-font.md)
- [Shorten or lengthen spot lifetime](shorten-or-lengthen-spot-lifetime.md)
- [Overlay memory channels on the panadapter](overlay-memory-channels-on-the-panadapter.md)
