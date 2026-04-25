# Shorten or lengthen spot lifetime

Adjust how long DX spots remain visible on the panadapter before they fade away. A shorter lifetime keeps the display uncluttered; a longer lifetime lets you see spots that arrived minutes or hours ago.

## Before you start

- AetherSDR must be running. A radio connection is not required to change this setting.
- The Spot Settings dialog must be accessible from the panadapter context menu or Spots overlay.

## Steps

1. Right-click the panadapter (or click the Spots overlay) to open the **Spot Settings** dialog.
2. Locate the **Spot Lifetime:** row.
3. Drag the slider left to decrease lifetime or right to increase it. The label to the right of the slider updates immediately, showing the current value in seconds, minutes, hours, or days.
4. Release the slider. The new value is saved automatically to `SpotsLifetime` (`DxClusterSpotLifetimeSec`).

## What each control does

| Control | Behavior | Default | Valid range | Setting key |
|---|---|---|---|---|
| **Spot Lifetime:** slider | Sets how long a spot stays on the panadapter before fading. The scale is non-linear: it steps through 10–55 sec (in 5 sec steps), then 5–55 min (in 5 min steps), then 1–24 hr (in 1 hr steps), ending at 1 day. | 30 min | 10 sec – 24 hr (1 day) | `SpotsLifetime` / `DxClusterSpotLifetimeSec` |

## Tips

- The slider display label uses human-readable units: values below 60 seconds show as `sec`, values below one hour show as `min` or `mins`, and values of one hour or more show as `hr` or `hrs`. 24 hours displays as `1 day`.
- If you upgraded from an older AetherSDR version, the setting is migrated automatically from the old minutes-based key to the current seconds-based key. No manual action is needed.

## Related

- [Spot Settings overview](overview.md)
- [Turn spots on or off](turn-spots-on-or-off.md)
- [Clear every spot from the panadapter](clear-every-spot-from-the-panadapter.md)
- [Change spot density and vertical position](change-spot-density-and-vertical-position.md)
