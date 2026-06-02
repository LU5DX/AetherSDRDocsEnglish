# Use the virtual wheel to tune the active slice

Use the on-screen virtual tuning wheel in the AetherControl dialog to change the frequency of the currently active slice with mouse or trackpad gestures, simulating the feel of a physical rotary controller.

## Before you start

- Open the AetherControl dialog: `Settings > AetherControl...`

## Steps

1. In the AetherControl dialog, locate the **Wheel** control at the top. It shows the current slice frequency and mode.
2. Double-click the wheel to capture mouse input for circular tuning. The wheel becomes active for tuning gestures.
3. Drag in a circular motion around the wheel to tune. Drag clockwise to increase frequency, counter-clockwise to decrease.
4. To release the mouse capture, double-click the wheel again. Press Escape as a secondary release path.
5. (Optional) To reverse the tuning direction, click **Reverse**.
6. (Optional) To enable panadapter-based tuning, click **External Spin**. When enabled, dragging on the panadapter also triggers spin-wheel tuning.

## What each control does

| Control | Default | Range | Setting key |
|---|---|---|---|
| **Wheel** | — | — | None (renders current slice) |
| **Physical** | — | — | None (shows connection state) |
| **Compact** | Off | On/Off | None |
| **External Spin** | Off | On/Off | `FlexControlVirtualExternalSpin` |
| **Reverse** | Off | On/Off | `FlexControlInvertDir` |
| **Push (action)** | — | — | `FlexControlButtonAction_*` |
| **Double-tap (action)** | — | — | None |
| **Wheel Tightness** | 45 | 0–100 (0 = tight, 100 = loose) | `FlexControlVirtualWheel` (nested JSON `looseness` field) |
| **Mouse Sensitivity** | 50 | 0–100 (0 = less, 100 = more) | `FlexControlVirtualWheel` (nested JSON `sensitivity` field) |
| **Aux buttons 1–5** | — | 5 buttons | None |

## Auxiliary buttons

The dialog provides five configurable auxiliary buttons (labeled with aux dots to indicate active selection). Each button has:

- **Aux single-tap combo**: Assigns an action to single-tapping the selected aux button.
- **Aux double-tap combo**: Assigns an action to double-tapping the selected aux button.

These settings are stored per aux button.

## Tips

- Mouse capture has been simplified to a single double-click toggle: double-click to capture, double-click again to release. This replaces the previous click-to-capture, Escape-to-release behavior for a cleaner user experience.
- The virtual wheel responds to circular mouse or trackpad drags. Single-event pointer deltas are clamped to 15° (π/12 radians) per event to reduce jitter.
- When your pointer crosses through the center dead zone, the anchor resets. The next movement starts a new tuning gesture without computing a delta.
- **Wheel Tightness** and **Mouse Sensitivity** are stored together in a single JSON object under `FlexControlVirtualWheel`. In earlier versions, Wheel Tightness was stored separately as `FlexControlVirtualWheelLooseness`; this is auto-migrated on first read.
- The wheel shows the slice frequency in Hz and the current mode (e.g., USB, CW, AM).
- Click **Compact** to toggle compact mode, which hides auxiliary buttons and shows only the wheel and frequency for a minimal UI.
- The **Physical** indicator shows physical FlexControl connection state and port name. Use the Detect/Close buttons to manage the physical device.

## Related

- [Adjust mouse sensitivity for the virtual wheel](adjust-mouse-sensitivity-for-the-virtual-wheel.md)
- [Adjust wheel tightness (coasting feel)](adjust-wheel-tightness-coasting-feel.md)
- [Toggle Reverse to invert tuning direction](toggle-reverse-to-invert-tuning-direction.md)
- [Toggle Auto Spin for external frequency change animation](toggle-auto-spin-for-external-frequency-change-animation.md)