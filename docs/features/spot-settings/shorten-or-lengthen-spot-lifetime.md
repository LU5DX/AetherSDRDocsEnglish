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

| Control | Behavior | Default | Range | Setting key |
|---|---|---|---|---|
| **Spot Lifetime:** slider | Sets how long a spot remains on the panadapter before it fades. The scale is non-linear: the lower portion steps in 5-second increments (10 sec – 55 sec), the middle portion steps in 5-minute increments (5 min – 55 min), and the upper portion steps in 1-hour increments (1 hr – 24 hrs / 1 day). | 30 min | 10 sec – 24 hrs | `SpotsLifetime` |

## Tips

- The slider uses a non-linear scale. Small movements near the left end adjust lifetime by seconds; movements near the right end adjust by hours. Position the slider carefully when targeting a specific value.
- The displayed label rounds to the nearest step: values under 60 seconds show as `sec`, values under 1 hour show as `min` or `mins`, and values of 1 hour or more show as `hr`, `hrs`, or `1 day`.

## Troubleshooting

- **Old spots still appear after reducing lifetime** — Existing spots that arrived before the change will expire based on the previous setting. New spots will use the updated lifetime. Click **Clear All Spots** to remove existing spots immediately.

## Related

- [Spot Settings overview](overview.md)
- [Turn spots on or off](turn-spots-on-or-off.md)
- [Clear every spot from the panadapter](clear-every-spot-from-the-panadapter.md)
