# Map push-button and double-tap actions to the wheel

Configure what happens when you push (single-tap) or double-tap the physical FlexControl wheel or the virtual wheel in the AetherControl dialog.

## Before you start

- Open the AetherControl dialog: **Settings > AetherControl...**
- If using a physical FlexControl, ensure it is connected (see [Configure the AetherControl / FlexControl hardware controller](configure-the-aethercontrol-flexcontrol-hardware-controller.md)).

## Steps

1. In the AetherControl dialog, locate the **Push (action)** combo box near the wheel display.
2. Click the combo box and select an action from the list.
3. In the **Double-tap (action)** combo box directly below, select a second action.
4. Close the dialog. The new actions take effect immediately.

## What each control does

| Control | Default | Setting key | Behavior |
|---------|---------|-------------|----------|
| Push (action) combo box | – | `FlexControlButtonAction_*` | Selects the action triggered by a single push of the wheel. Options include: Tune Slice, Band Zoom, Segment Zoom, RIT, XIT, Master Volume, Slice Audio Volume, Headphone Volume, AGCT, APF, Clear RIT, Clear XIT, Toggle APF, Change Active Slice, Split Active Slice, MOX, RF Power, CW Speed, CWX Macros 1-12, Step Up, Step Down, Toggle Tune, Toggle Mute, Toggle Lock, Previous Slice, Toggle AGC, Slice AF Up, Slice AF Down, and None. |
| Double-tap (action) combo box | – | – | Selects the action triggered by two quick pushes of the wheel. Same action options as Push. |

Both combo boxes share the same list of available actions. See the source snippet for the complete list of `FlexActionDef` entries, which include all labels shown above.

## Related

- [Configure single- and double-tap actions for the PUSH button](configure-single-and-double-tap-actions-for-the-push-button.md)

# Configure the AetherControl / FlexControl hardware controller

Configure the virtual AetherControl wheel and manage a physical FlexControl device.

## Before you start

- Open the AetherControl dialog: **Settings > AetherControl...**

## Steps

1. In the AetherControl dialog, the **Wheel** indicator shows the virtual tuning wheel. Double-click it to capture mouse input for circular tuning. Double-click again to release. Press Escape as a secondary release path.
2. The **Physical** indicator shows the connection state of a physical FlexControl. Click **Detect** to find the device, or **Close** to disconnect.
3. Use the **Compact** toggle button to switch to a minimal UI that shows only the wheel and frequency readout.
4. Enable **External Spin** to allow dragging on the panadapter to trigger spin-wheel tuning gestures.
5. Enable **Reverse** to reverse the wheel tuning direction.
6. Adjust **Wheel Tightness** with the slider to control virtual wheel coasting drag. 0 = tight (fast stop), 100 = loose (long coast). Primarily affects trackpad behavior.
7. Adjust **Mouse Sensitivity** with the slider to control how much captured mouse/trackpad movement turns the virtual wheel. Midpoint (50) yields 1.0x scale. Primarily affects trackpad behavior.
8. Configure the **Aux buttons (1-5)** by clicking a button to select it, then:
   - Select a single-tap action from the **Aux single-tap combo**.
   - Select a double-tap action from the **Aux double-tap combo**.
   The button's active state is indicated by an aux dot.

## What each control does

| Control | Default | Setting key | Behavior |
|---------|---------|-------------|----------|
| Wheel indicator | – | – | Virtual FlexControl wheel. Double-click to capture mouse/touch input; double-click again to release. Shows frequency and mode readout. |
| Physical indicator | – | – | Shows physical FlexControl connection state and port name. Detect/Close buttons manage the device. |
| Compact toggle | – | – | Toggles compact mode: hides auxiliary buttons, shows only the wheel and frequency for a minimal UI. |
| External Spin toggle | – | – | Enables external spin wheel tuning: dragging on the panadapter triggers spin-wheel tuning gestures. |
| Reverse toggle | – | – | Reverses the wheel tuning direction. |
| Push (action) combo box | – | `FlexControlButtonAction_*` | Selects the action triggered by a single push of the wheel. Options include: Tune Slice, Band Zoom, Segment Zoom, RIT, XIT, Master Volume, Slice Audio Volume, Headphone Volume, AGCT, APF, Clear RIT, Clear XIT, Toggle APF, Change Active Slice, Split Active Slice, MOX, RF Power, CW Speed, CWX Macros 1-12, Step Up, Step Down, Toggle Tune, Toggle Mute, Toggle Lock, Previous Slice, Toggle AGC, Slice AF Up, Slice AF Down, and None. |
| Double-tap (action) combo box | – | – | Selects the action triggered by two quick pushes of the wheel. Same action options as Push. |
| Wheel Tightness slider | 45 | `FlexControlVirtualWheel` (nested JSON, looseness field) | Adjusts virtual wheel coasting drag; 0 = tight (fast stop), 100 = loose (long coast). Primarily for trackpads; does not affect physical FlexControl. |
| Mouse Sensitivity slider | 50 | `FlexControlVirtualWheel` (nested JSON, sensitivity field) | Adjusts how much captured mouse/trackpad movement turns the virtual wheel. Midpoint (50) yields 1.0x scale. Primarily for trackpads; does not affect physical FlexControl. |
| Aux buttons (1-5) | – | – | Five configurable auxiliary buttons; each has a single-tap and double-tap action combo box. Labeled with aux dots to indicate active selection. |
| Aux single-tap combo | – | – | Assigns an action to single-tapping the selected aux button. Per-aux-button setting. |
| Aux double-tap combo | – | – | Assigns an action to double-tapping the selected aux button. Per-aux-button setting. |

## Indicators

| Indicator | Meaning |
|-----------|---------|
| Slice / Frequency / Mode readout | Shows which slice is bound, its current frequency, and mode. |

## Notes on window sizing

The AetherControl dialog uses a scroll area for its content when not in compact mode. The full controller may be taller than your screen; the content area scrolls vertically as needed. The dialog will not open taller than the available screen workspace (accounting for taskbars). The minimum non-compact width is 430 pixels; the dialog cannot be resized narrower than its content requires.

## Notes on physical FlexControl

When a physical FlexControl device is connected and sends a reset command (e.g. `F0304;`), AetherSDR automatically re-issues the cached LED state to restore the hardware's indicator lights to match the application's active wheel-mode button. This fixes a race condition where the device's power-on reset could otherwise clear the LEDs before AetherSDR had a chance to program them.

## Theme support

The FlexControl dialog uses theme-aware colors for sliders. The groove background uses `color.slider.background`, the filled portion and handle border use `color.accent.success`, and the handle uses `color.slider.handle`. These colors update automatically when switching between Default Dark and Default Light themes.

## Related

- [Map push-button and double-tap actions to the wheel](map-push-button-and-double-tap-actions-to-the-wheel.md)
- [Configure single- and double-tap actions for the PUSH button](configure-single-and-double-tap-actions-for-the-push-button.md)