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
| Mouse Sensitivity slider | 50 | 0–100 | `FlexControlVirtualWheel` (nested JSON, `sensitivity` field) | Adjusts how much captured mouse/trackpad movement turns the virtual wheel. Midpoint (50) yields 1.0x scale. Primarily for trackpads; does not affect physical FlexControl. |

## Related

- [Adjust mouse sensitivity for the virtual wheel](adjust-mouse-sensitivity-for-the-virtual-wheel.md)
- [Use the virtual wheel to tune the active slice](use-the-virtual-wheel-to-tune-the-active-slice.md)

---

# Slice Audio Volume wheel action

The **Slice Audio Volume** action lets you adjust the audio volume of the active slice using the AetherControl wheel.

## Before you start

- Open the AetherControl dialog: `Settings > AetherControl...`

## Steps

1. In the dialog, locate the **Push (action)** or **Double-tap (action)** combo box, or one of the **Aux** single-tap or double-tap combo boxes.
2. Click the combo box and select **Slice Audio Volume** from the list.
3. Close the dialog. Changes are saved automatically.

When you press the assigned button or trigger the double-tap, the tuning wheel switches to control the slice audio volume. Turning the wheel clockwise increases the volume; counter-clockwise decreases it.

> **Note:** This action was added in AetherSDR v26.6.3.

---

# Scroll area and compact mode behavior

The AetherControl dialog includes a scroll area that ensures all controls remain accessible even on short or DPI-scaled screens.

## Before you start

- Open the AetherControl dialog: `Settings > AetherControl...`

## How it works

- The dialog uses an internal scroll area (`QScrollArea`) to contain all AetherControl configuration controls.
- When not in compact mode, the dialog has a minimum height of 610 pixels and a minimum width of 430 pixels.
- If the screen's available height is smaller than the content's natural size, the dialog height is clamped to fit the workspace, and the content becomes scrollable.
- The horizontal scrollbar is always hidden; the minimum width ensures no horizontal clipping.
- In compact mode (use the **Compact** toggle button), the dialog shrinks to show only the wheel and frequency readout. Auxiliary buttons are hidden.

## Compact mode

Click **Compact** in the AetherControl dialog header. The dialog immediately resizes to its minimal size. Click **Compact** again to restore the full control layout.

## Screen fit

The dialog automatically checks the screen's available height (excluding taskbars and docks) when entering non-compact mode. It never opens taller than the workspace, and the content scrolls vertically if needed. This prevents the dialog from exceeding the display even with many aux buttons or high DPI scaling.

> **Note:** This scroll area behavior was added in AetherSDR v26.7.4 to address issues #3662 and #4365.

---

# Physical FlexControl connection recovery

AetherSDR automatically retries connecting to the physical FlexControl hardware device when the connection is lost or the device is temporarily unavailable.

## How it works

- When a connection attempt fails, AetherSDR keeps retrying instead of giving up immediately.
- Retries start at 2-second intervals and gradually back off to a maximum of 30 seconds between attempts.
- The device port is re-detected on each retry, so a USB re-enumeration that assigns a different port name is handled automatically.
- If the device is unplugged and replugged, AetherSDR reconnects on the new port without requiring manual intervention.
- The **Physical** indicator in the AetherControl dialog shows the current connection state.

## When this applies

- The device is unplugged and reconnected.
- The USB port is re-enumerated by the operating system.
- Another process temporarily holds the port.
- The device is mid-enumeration when AetherSDR starts.

> **Note:** Automatic reconnection was added in AetherSDR v26.8.4 to address issue #4574.

---

# AetherControl dialog controls reference

| Control | Kind | Default | Range | Setting key | Behavior |
|---------|------|---------|-------|-------------|----------|
| **Wheel** | indicator | — | — | — | Virtual FlexControl wheel: rotate with mouse/touch to tune the active slice. Shows frequency and mode readout. |
| **Physical** | indicator | — | — | — | Shows physical FlexControl connection state and port name. Detect/Close buttons to manage the physical device. |
| **Compact** | toggle button | — | — | — | Toggles compact mode: hides auxiliary buttons, shows only the wheel and frequency for a minimal UI. |
| **External Spin** | toggle button | — | — | — | Enables external spin wheel tuning: dragging on the panadapter triggers spin-wheel tuning gestures. |
| **Reverse** | toggle button | — | — | — | Reverses the wheel tuning direction. |
| **Push (action)** | combo box | — | — | `FlexControlButtonAction_*` | Assigns an action to pushing the wheel (single tap). Options include mode cycle, step zoom, zoom reset, band up/down, and more. |
| **Double-tap (action)** | combo box | — | — | — | Assigns an action to double-tapping the wheel. |
| **Wheel Tightness** | slider | 45 | 0–100 | `FlexControlVirtualWheel` (nested JSON, looseness field) | Adjusts virtual wheel coasting drag; 0 = tight (fast stop), 100 = loose (long coast). Primarily for trackpads; does not affect physical FlexControl. |
| **Mouse Sensitivity** | slider | 50 | 0–100 | `FlexControlVirtualWheel` (nested JSON, sensitivity field) | Adjusts how much captured mouse/trackpad movement turns the virtual wheel. Midpoint (50) yields 1.0x scale. Primarily for trackpads; does not affect physical FlexControl. |
| **Aux buttons (1-5)** | push button | — | 5 buttons | — | Five configurable auxiliary buttons; each has a single-tap and double-tap action combo box. |
| **Aux single-tap combo** | combo box | — | — | — | Assigns an action to single-tapping the selected aux button. |
| **Aux double-tap combo** | combo box | — | — | — | Assigns an action to double-tapping the selected aux button. |