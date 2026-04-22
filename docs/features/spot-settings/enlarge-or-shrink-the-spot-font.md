# Enlarge or shrink the spot font

Use this page to increase or decrease the text size of DX spots displayed on the panadapter. A larger font makes callsigns easier to read at a glance; a smaller font reduces clutter when the band is busy.

## Before you start

- AetherSDR must be running. A radio connection is not required to change this setting.
- Open the Spot Settings dialog by right-clicking the spots overlay on any panadapter.

## Steps

1. In the Spot Settings dialog, locate the **Font Size:** row.
2. Drag the **Font Size:** slider left to decrease the font size or right to increase it.
3. Read the current value in the number display to the right of the slider.
4. Close the dialog when finished. The change takes effect immediately and is saved automatically.

## What each control does

| Control | Description | Default | Valid range | Setting key |
|---|---|---|---|---|
| **Font Size:** slider | Sets the text size of spot labels on the panadapter. | 16 | 8 – 32 (pt) | `SpotsFontSize` |

## Tips

- The value shown next to the slider reflects the current font size in points. The panadapter updates in real time as you drag, so you can judge the result without closing the dialog.
- If spots overlap at larger font sizes, reduce the number of stacking rows with the **Levels:** slider, or adjust the **Position:** slider to give spots more vertical room. See [Change spot density and vertical position](change-spot-density-and-vertical-position.md).

## Related

- [Change spot density and vertical position](change-spot-density-and-vertical-position.md)
- [Turn spots on or off](turn-spots-on-or-off.md)
- [Spot Settings overview](overview.md)
