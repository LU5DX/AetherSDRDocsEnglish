# Shorten or lengthen spot lifetime

Use this page to control how long DX spots remain visible on the panadapter before they expire. A shorter lifetime keeps the display uncluttered; a longer lifetime is useful during slow band conditions when spots arrive infrequently.

## Before you start

- The Spot Settings dialog is not in the main menu. You must open it from the panadapter context menu or the spots overlay.
- Spots must be enabled (`IsSpotsEnabled`) for the lifetime setting to have any visible effect.

## Steps

1. Right-click the panadapter (or click the spots overlay) to open the **Spot Settings** dialog.
2. Locate the **Spot Lifetime:** slider.
3. Drag the slider left to shorten the lifetime or right to lengthen it. The label to the right of the slider updates immediately, showing the current value in seconds, minutes, or hours (for example, `30 secs`, `5 mins`, `1 hr`).
4. Release the slider. The new value is saved automatically.

## What each control does

| Control | Behavior | Default | Persisted key |
|---|---|---|---|
| **Spot Lifetime:** slider | Sets how long a spot remains on the panadapter before it disappears. The scale is non-linear: the left portion steps through 10–55 seconds in 5-second increments, the middle portion steps through 5–55 minutes in 5-minute increments, and the right portion steps through 1–24 hours in 1-hour increments. | 30 minutes | `SpotsLifetime` |

## Tips

- The slider display label rounds to the nearest step value, so you cannot enter an arbitrary number of seconds — use the nearest step.
- If you previously configured spot lifetime in an older version of AetherSDR that stored the value in minutes, the dialog migrates that value to seconds automatically on first open.
- At the far right of the slider range, the label reads `1 day` (24 hours), which is the maximum lifetime.

## Related

- [Spot Settings overview](overview.md)
- [Turn spots on or off](turn-spots-on-or-off.md)
- [Clear every spot from the panadapter](clear-every-spot-from-the-panadapter.md)
