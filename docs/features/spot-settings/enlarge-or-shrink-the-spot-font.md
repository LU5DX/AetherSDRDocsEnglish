# Enlarge or shrink the spot font

Use this page to make spot callsign text larger or smaller on the panadapter. Adjusting the font size helps when spots are hard to read at a distance or when they overlap other display elements.

## Before you start

- AetherSDR must be running. A radio connection is not required to change this setting.
- The Spot Settings dialog must be accessible from the panadapter. If spots are not visible, confirm that the `IsSpotsEnabled` toggle is set to Enabled — see [Turn spots on or off](turn-spots-on-or-off.md).

## Steps

1. Right-click anywhere on the panadapter to open the context menu.
2. Select the spots overlay option to open the **Spot Settings** dialog.
3. Locate the **Font Size:** row.
4. Drag the slider left to decrease the font size or right to increase it. The current value in points is shown to the right of the slider.
5. Release the slider. The change takes effect immediately and is saved automatically.

## What each control does

| Control | Description | Default | Valid range | Setting key |
|---|---|---|---|---|
| **Font Size:** | Sets the text size of spot callsigns and labels rendered on the panadapter. | 16 | 8 – 32 (points) | `SpotsFontSize` |

## Tips

- A font size of 16 is the default. Values toward 8 reduce clutter when many spots are visible; values toward 32 help when viewing the panadapter from a distance.
- Font size applies to all spots simultaneously. There is no per-spot size override.

## Related

- [Change spot density and vertical position](change-spot-density-and-vertical-position.md)
- [Turn spots on or off](turn-spots-on-or-off.md)
- [Shorten or lengthen spot lifetime](shorten-or-lengthen-spot-lifetime.md)
