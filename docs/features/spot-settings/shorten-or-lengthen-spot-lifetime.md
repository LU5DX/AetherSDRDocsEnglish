# Shorten or lengthen spot lifetime

Use this page to control how long DX spots remain visible on the panadapter before fading away. A shorter lifetime keeps the display uncluttered; a longer one lets you track spots across extended operating sessions.

## Before you start

- AetherSDR must be running. A radio connection is not required to change this setting.
- The Spot Settings dialog must be accessible from the panadapter context menu or the Spots overlay.

## Steps

1. Right-click the panadapter (or the Spots overlay) to open the context menu, then select the option that opens **Spot Settings**.
2. Locate the **Spot Lifetime:** row.
3. Drag the slider left to shorten the lifetime or right to lengthen it. The label to the right of the slider updates immediately to show the current value in seconds, minutes, or hours.
4. Release the slider. The new value is saved automatically.

## What each control does

| Control | Description | Default | Range | Setting key |
|---|---|---|---|---|
| **Spot Lifetime:** slider | Sets how long spots remain on the panadapter before fading. The slider uses a non-linear scale: positions at the left cover 10–55 seconds (in 5-second steps), the middle covers 5–55 minutes (in 5-minute steps), and the right covers 1–24 hours (in 1-hour steps). The label shows the current value formatted as seconds (`sec`), minutes (`mins`), or hours (`hrs`), with 24 hours displayed as `1 day`. | 30 min | 10 sec – 24 hr | `SpotsLifetime` (`DxClusterSpotLifetimeSec` internally, in seconds) |

## Tips

- The slider snaps to predefined steps, not arbitrary values. The finest resolution is 5 seconds at the low end and 1 hour at the high end.
- If you upgraded from an earlier version of AetherSDR, the application migrates your old per-minute lifetime value to the new per-second key automatically on first launch.
- Setting a very long lifetime (several hours) can result in a crowded panadapter on busy bands. Use the **Clear All Spots** button in the same dialog to flush accumulated spots immediately.

## Troubleshooting

- **Spots disappear sooner than the configured lifetime** — Verify that **Spots:** is set to **Enabled** in the same dialog. If the `IsSpotsEnabled` setting is toggled off and back on, spots already displayed may restart their lifetime counter.
- **Slider jumps past the value you want** — The scale is non-linear. Move slowly near the transition points (around 55 seconds and 55 minutes) where the step size changes.

## Related

- [Spot Settings overview](overview.md)
- [Turn spots on or off](turn-spots-on-or-off.md)
- [Clear every spot from the panadapter](clear-every-spot-from-the-panadapter.md)
- [Change spot density and vertical position](change-spot-density-and-vertical-position.md)
