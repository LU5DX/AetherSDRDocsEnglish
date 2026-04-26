# Enlarge or shrink the spot font

Use this page to increase or decrease the text size of DX spots displayed on the panadapter. A larger font makes callsigns easier to read at a glance; a smaller font reduces clutter when many spots are visible.

## Before you start

- AetherSDR must be running. A radio connection is not required to change this setting.
- The Spot Settings dialog must be accessible from the panadapter context menu or Spots overlay.

## Steps

1. Right-click the panadapter (or the Spots overlay) to open the context menu, then select the option that opens the Spot Settings dialog.
2. Locate the **Font Size:** row.
3. Drag the slider left to decrease the font size or right to increase it. The current value displays to the right of the slider.
4. Release the slider. The change is saved immediately to `SpotsFontSize` and takes effect on the panadapter without closing the dialog.

## What each control does

| Control | Description | Default | Range | Setting key |
|---|---|---|---|---|
| **Font Size:** slider | Sets the text size of spot labels on the panadapter. | 16 | 8–32 (points) | `SpotsFontSize` |

## Tips

- A font size of 16 pt is the default. Values at the lower end of the range (8–10 pt) are useful when the **Levels:** slider is set high and many stacking rows of spots are visible.
- Changing the font size does not affect the **Background Opacity:** or spot position. Adjust **Position:** and **Levels:** separately if resized text overlaps other panadapter elements.

## Related

- [Spot Settings overview](overview.md)
- [Change spot density and vertical position](change-spot-density-and-vertical-position.md)
- [Shorten or lengthen spot lifetime](shorten-or-lengthen-spot-lifetime.md)
- [Turn spots on or off](turn-spots-on-or-off.md)
