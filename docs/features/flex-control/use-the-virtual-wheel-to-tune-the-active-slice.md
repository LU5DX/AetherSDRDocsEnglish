# Use the virtual wheel to tune the active slice

Use the on-screen virtual tuning wheel in the AetherControl dialog to change the frequency of the currently active slice with mouse or trackpad gestures, simulating the feel of a physical rotary controller.

## Before you start

- Open the AetherControl dialog: `Settings > AetherControl...`

## Steps

1. In the AetherControl dialog, locate the **Wheel** control at the top. It shows the current slice frequency and mode.
2. Click and drag in a circular motion around the wheel to tune. Drag clockwise to increase frequency, counter-clockwise to decrease.
3. (Optional) To reverse the tuning direction, click **Reverse**.
4. (Optional) To enable panadapter-based tuning, click **External Spin**. When enabled, dragging on the panadapter also triggers spin-wheel tuning.

## What each control does

| Control | Default | Range | Setting key |
|---|---|---|---|
| **Wheel** | — | — | None (renders current slice) |
| **Reverse** | Off | On/Off | `FlexControlInvertDir` |
| **External Spin** | Off | On/Off | `FlexControlVirtualExternalSpin` |
| **Wheel Tightness** | 45 | 0–100 (0 = tight, 100 = loose) | `FlexControlVirtualWheel` (nested JSON `looseness` field) |
| **Mouse Sensitivity** | 50 | 0–100 (0 = less, 100 = more) | `FlexControlVirtualWheel` (nested JSON `sensitivity` field) |

## Tips

- The virtual wheel responds to circular mouse or trackpad drags. Single-event pointer deltas are clamped to 15° (π/12 radians) per event to reduce jitter.
- When your pointer crosses through the center dead zone, the anchor resets. The next movement starts a new tuning gesture without computing a delta.
- **Wheel Tightness** and **Mouse Sensitivity** are stored together in a single JSON object under `FlexControlVirtualWheel`. In earlier versions, Wheel Tightness was stored separately as `FlexControlVirtualWheelLooseness`; this is auto-migrated on first read.
- The wheel shows the slice frequency in Hz and the current mode (e.g., USB, CW, AM).

## Related

- [Adjust mouse sensitivity for the virtual wheel](adjust-mouse-sensitivity-for-the-virtual-wheel.md)
- [Adjust wheel tightness (coasting feel)](adjust-wheel-tightness-coasting-feel.md)
- [Toggle Reverse to invert tuning direction](toggle-reverse-to-invert-tuning-direction.md)
- [Toggle Auto Spin for external frequency change animation](toggle-auto-spin-for-external-frequency-change-animation.md)
