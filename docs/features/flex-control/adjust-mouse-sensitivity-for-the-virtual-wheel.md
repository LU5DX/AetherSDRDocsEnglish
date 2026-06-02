# Adjust mouse sensitivity for the virtual wheel

Change how much mouse or trackpad movement is required to turn the virtual tuning wheel. Higher sensitivity means less physical movement per frequency change.

## Before you start

- The AetherControl dialog must be open: `Settings > AetherControl...`
- The virtual wheel is available regardless of whether a physical FlexControl is connected.

## Steps

1. Open `Settings > AetherControl...`.
2. In the **Wheel Tightness / Mouse Sensitivity** section, locate the **Mouse Sensitivity** slider.
3. Drag the slider to your desired value:
   - **Less** (left, value 0): requires more pointer movement to turn the wheel.
   - **More** (right, value 100): requires less pointer movement to turn the wheel.
4. Test the feel by rotating your finger or stylus around the virtual wheel widget.
5. Close the dialog to save the setting.

## What each control does

| Control | Default | Valid range | Setting key |
|---------|---------|-------------|-------------|
| Mouse Sensitivity slider | 50 | 0–100 | `FlexControlVirtualWheel` (nested JSON, `sensitivity` field) |

- Midpoint (50) yields 1.0x scaling of pointer movement.
- Values below 50 reduce sensitivity (more movement needed).
- Values above 50 increase sensitivity (less movement needed).
- Affects only the virtual wheel; does not change behavior of a physical FlexControl.
- Single-event pointer deltas are clamped to 15° (π/12 radians) to reduce jitter.
- Lazy re-anchoring prevents unwanted jumps when the pointer crosses through the wheel’s center dead-zone.

## Capture/release behavior

- **Double-click** the virtual wheel to capture mouse input for circular tuning.
- **Double-click** again to release capture.
- Press **Escape** as a secondary release path.
- Single-clicking no longer captures or releases the wheel. This change provides a cleaner user experience than the previous asymmetry of click-to-capture with Escape-to-release.

## Tips

- If using a trackpad, try starting at value 65 and adjust from there.
- The companion **Wheel Tightness** slider controls coasting feel (how long the wheel keeps spinning after you stop moving). See [Adjust wheel tightness (coasting feel)](adjust-wheel-tightness-coasting-feel.md).

## Related

- [Adjust wheel tightness (coasting feel)](adjust-wheel-tightness-coasting-feel.md)
- [Use the virtual wheel to tune the active slice](use-the-virtual-wheel-to-tune-the-active-slice.md)