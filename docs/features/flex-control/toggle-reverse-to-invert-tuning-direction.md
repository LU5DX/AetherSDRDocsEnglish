# AetherControl / FlexControl Configuration

This page describes the AetherControl / FlexControl dialog, which configures the hardware rotary controller and the virtual on-screen tuning wheel.

## Opening the dialog

1. Open the **Settings** menu.
2. Click **AetherControl...**.

## Physical FlexControl connection

The **Physical** indicator shows whether a FlexControl device is connected and which serial port it uses.

- Click **Detect** to scan for a connected FlexControl.
- Click **Close** to disconnect the physical device.

If the physical device is unplugged, AetherSDR automatically retries the connection. The retry interval starts at 2 seconds and backs off to a maximum of 30 seconds if the device does not reappear. When the device is reconnected, it may be assigned a different serial port; AetherSDR re-detects the port automatically.

## Virtual wheel

The **Wheel** is a virtual rotary control. Rotate it with your mouse or trackpad to tune the active slice. It shows the current frequency and mode readout.

| Control | Label | Behavior | Setting key |
|---------|-------|----------|-------------|
| Indicator | **Wheel** | Virtual rotary control for tuning the active slice. Shows frequency and mode. | — |
| Toggle button | **Compact** | Hides the auxiliary buttons and shows only the wheel and frequency for a minimal UI. | — |
| Toggle button | **External Spin** | Enables spin-wheel tuning gestures when dragging on the panadapter. | — |
| Toggle button | **Reverse** | Reverses the wheel tuning direction. | `FlexControlInvertDir` |
| Slider | **Wheel Tightness** | Adjusts virtual wheel coasting drag. 0 = tight (fast stop), 100 = loose (long coast). Primarily for trackpads; does not affect the physical FlexControl. | `FlexControlVirtualWheel` (nested JSON, `looseness` field) |
| Slider | **Mouse Sensitivity** | Adjusts how much captured mouse/trackpad movement turns the virtual wheel. Midpoint (50) yields 1.0x scale. Primarily for trackpads; does not affect the physical FlexControl. | `FlexControlVirtualWheel` (nested JSON, `sensitivity` field) |

### Wheel Tightness notes

- The **Wheel Tightness** slider replaces the old *Spin Sensitivity* slider (v26.5.3).
- The setting is stored as part of a nested JSON object under `FlexControlVirtualWheel`. Earlier flat key `FlexControlVirtualWheelLooseness` is auto-migrated on read.

### Mouse Sensitivity notes

- Introduced in v26.5.3.
- Pointer deltas are clamped to 15° (π/12) per event to avoid jumps.
- Lazy re-anchoring: when the pointer crosses the centre dead-zone, the anchor is dropped; the next movement re-anchors without computing a delta.

## Wheel actions

Assign actions to pushing and double-tapping the wheel.

| Control | Label | Behavior | Setting key |
|---------|-------|----------|-------------|
| Combo box | **Push (action)** | Assigns an action to pushing the wheel (single tap). Options include mode cycle, step zoom, zoom reset, band up/down, and more. | `FlexControlButtonAction_*` |
| Combo box | **Double-tap (action)** | Assigns an action to double-tapping the wheel. | — |

## Auxiliary buttons

Five configurable auxiliary buttons (1–5) sit below the wheel. Each button has its own single-tap and double-tap action.

1. Click an aux button to select it. The button is highlighted with an aux dot.
2. Choose the **Aux single-tap** action from the combo box.
3. Choose the **Aux double-tap** action from the combo box.

| Control | Label | Behavior | Setting key |
|---------|-------|----------|-------------|
| Push button group | **Aux buttons (1-5)** | Five configurable buttons, each with single-tap and double-tap actions. | — |
| Combo box | **Aux single-tap** | Assigns an action to single-tapping the selected aux button. | — |
| Combo box | **Aux double-tap** | Assigns an action to double-tapping the selected aux button. | — |

## Related

- Reverse tuning direction on the AetherControl
- [Use the virtual wheel to tune the active slice](use-the-virtual-wheel-to-tune-the-active-slice.md)
- [Adjust mouse sensitivity for the virtual wheel](adjust-mouse-sensitivity-for-the-virtual-wheel.md)
- Adjust wheel tightness for the virtual wheel