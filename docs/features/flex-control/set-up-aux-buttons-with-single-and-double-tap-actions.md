# AetherControl / FlexControl

Configure the AetherControl / FlexControl hardware rotary controller, including virtual wheel tuning, push-button action mapping, and five auxiliary buttons with single- and double-tap actions.

## Before you start

- Open the AetherControl dialog: `Settings > AetherControl...`
- Familiarise yourself with the [overview](overview.md) of the controller

## What each control does

| Control | Description | Setting keys |
|---|---|---|
| Wheel | Virtual FlexControl wheel: rotate with mouse/touch to tune the active slice. Shows frequency and mode readout. Double-click to capture circular tuning; double-click again to release. Press Escape as a secondary release path. | None |
| Physical | Shows physical FlexControl connection state and port name. Detect/Close buttons to manage the physical device. | None |
| Compact | Toggles compact mode: hides auxiliary buttons, shows only the wheel and frequency for a minimal UI. The content area scrolls if the dialog height exceeds the available screen workspace. | None |
| External Spin | Enables external spin wheel tuning: dragging on the panadapter triggers spin-wheel tuning gestures. | None |
| Reverse | Reverses the wheel tuning direction. | None |
| Push (action) | Assigns an action to pushing the wheel (single tap). Options include mode cycle, step zoom, zoom reset, band up/down, and more. | `FlexControlButtonAction_*` |
| Double-tap (action) | Assigns an action to double-tapping the wheel. | None |
| Wheel Tightness | Adjusts virtual wheel coasting drag; 0 = tight (fast stop), 100 = loose (long coast). Primarily for trackpads; does not affect physical FlexControl. Stored as part of a nested JSON object under `FlexControlVirtualWheel`. Formerly stored under legacy flat key `FlexControlVirtualWheelLooseness`; auto-migrated on read. | `FlexControlVirtualWheel` (nested JSON, looseness field) |
| Mouse Sensitivity | Adjusts how much captured mouse/trackpad movement turns the virtual wheel. Midpoint (50) yields 1.0x scale. Primarily for trackpads; does not affect physical FlexControl. De-jitter clamps single-event pointer deltas to 15° (π/12). Lazy re-anchoring: when pointer crosses through centre dead-zone, anchor is dropped; next movement re-anchors without computing a delta. | `FlexControlVirtualWheel` (nested JSON, sensitivity field) |
| Aux buttons (1–5) | Select an auxiliary button to configure. The active button is shown with a green dot. | None |
| Aux single-tap combo | Assigns an action to a single tap of the selected aux button. | `FlexControlBtn1Action0` – `FlexControlBtn4Action0` |
| Aux double-tap combo | Assigns an action to a double tap of the selected aux button. | `FlexControlBtn1Action1` – `FlexControlBtn4Action1` |

## Configure aux button actions

1. Click one of the five numbered auxiliary buttons to select it. The selected button is highlighted in green.
2. In the single-tap combo box below the aux buttons, select an action for a single tap.
3. In the double-tap combo box below the aux buttons, select an action for a double tap.
4. Repeat for each auxiliary button you want to configure.

## Available actions

Tune Slice, Band Zoom, Segment Zoom, RIT, XIT, Master Volume, **Slice Audio Volume**, Headphone Volume, AGCT, APF, Clear RIT, Clear XIT, Toggle APF, Change Active Slice, Split Active Slice, MOX, RF Power, CW Speed, CWX Macro 1–12, Step Up, Step Down, Toggle Tune, Toggle Mute, Toggle Lock, Previous Slice, Toggle AGC, Slice AF Up, Slice AF Down, None.

## Physical device reconnection

The dialog automatically reconnects if the physical FlexControl device disconnects and re-appears on the system:

- When the device is unplugged or the USB connection drops, the dialog logs the error once and begins retrying.
- Retries start at 2-second intervals and back off exponentially up to 30 seconds.
- On each retry, the port is re-detected rather than reusing the old name, so a USB re-enumeration that assigns a different COM port is handled automatically.
- When a physical FlexControl device sends an init/reset command (e.g. `F0304;`), the dialog automatically re-issues the LED state to ensure hardware matches the application's active wheel-mode button.
- If the device is still present but wedged (fails to open), the dialog retries rather than reporting a false connection.

## Tips

- A double-tap must be completed within 230 ms of the first tap. If you tap too slowly, the action fires as two single taps.
- Actions that are continuous controls (Tune Slice, Master Volume, etc.) latch the aux button into a tuning mode. One-shot actions (Step Up, Toggle MOX, macros) execute immediately and do not latch.
- The virtual wheel uses double-click to capture and release circular tuning mode. Single-click does not change capture state.
- Slice Audio Volume allows you to adjust the audio volume of the active slice independently using the wheel, without affecting the master volume or other slices.
- The dialog uses a scroll area for non-compact mode. If your screen height is limited or you use high DPI scaling, the content scrolls vertically so the full controller remains accessible. The window cannot be resized taller than the available screen workspace.

## Related

- [Configure single- and double-tap actions for the PUSH button](configure-single-and-double-tap-actions-for-the-push-button.md)
- [Map push-button and double-tap actions to the wheel](map-push-button-and-double-tap-actions-to-the-wheel.md)
- [Use the virtual wheel to tune the active slice](use-the-virtual-wheel-to-tune-the-active-slice.md)