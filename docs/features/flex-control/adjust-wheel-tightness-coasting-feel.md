# Adjust wheel tightness (coasting feel)

Configure how long the virtual tuning wheel continues to spin (coast) after you stop moving your mouse or trackpad. A tighter setting stops faster; a looser setting coasts longer.

## Before you start

- Open the AetherControl dialog: `Settings > AetherControl...`

## Steps

1. Find the **Wheel Tightness** slider in the dialog.
2. Drag the slider to your preferred coasting feel:
   - **0** (Tight) — wheel stops almost immediately when you stop moving.
   - **100** (Loose) — wheel coasts for a long time after you stop.
   - **45** — default value.
3. Close the dialog. Changes are saved automatically.

> **Note:** This setting affects only the virtual wheel (mouse/trackpad tuning). It does not affect a physical FlexControl hardware device.

## What each control does

| Control | Default | Range | Setting key | Behavior |
|---------|---------|-------|-------------|----------|
| Wheel Tightness slider | 45 | 0–100 | `FlexControlVirtualWheel` (nested JSON, `looseness` field) | Adjusts virtual wheel coasting drag. 0 = tight (fast stop), 100 = loose (long coast). |

## Related

- [Adjust mouse sensitivity for the virtual wheel](adjust-mouse-sensitivity-for-the-virtual-wheel.md)
- [Use the virtual wheel to tune the active slice](use-the-virtual-wheel-to-tune-the-active-slice.md)
