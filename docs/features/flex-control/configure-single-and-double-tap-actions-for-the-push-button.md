# Configure the AetherControl / FlexControl hardware controller

Configure the virtual or physical FlexControl rotary controller in AetherSDR. The AetherControl dialog provides a virtual tuning wheel with circular mouse/touch tuning, push-button action mapping, five auxiliary buttons with single- and double-tap actions, compact mode, external spin animation on frequency changes, and automatic reconnection for the physical device.

## Before you start

- Open the AetherControl dialog: `Settings > AetherControl...`
- Connect a physical FlexControl device via USB (optional). When connected, the dialog shows the port name and connection state.

## Configure the virtual wheel

1. **Wheel**: Rotate the virtual wheel with mouse or touch to tune the active slice. The frequency and mode readout appear on the wheel face.
2. **Tightness**: Adjust the **Wheel Tightness** slider (0–100). 0 = tight (fast stop), 100 = loose (long coast). This affects the virtual wheel only, not a physical FlexControl.
3. **Mouse Sensitivity**: Adjust the **Mouse Sensitivity** slider (0–100). Midpoint (50) yields 1.0x scale. Higher values make small pointer movements turn the wheel more. Affects virtual wheel only.
4. **Reverse**: Click **Reverse** to reverse the wheel tuning direction.

## Configure push-button actions

1. **Push (action)**: Select an action from the combo box for single-tap of the wheel.
2. **Double-tap (action)**: Select an action from the combo box for double-tap of the wheel.

See Configure single- and double-tap actions for the PUSH button for the full list of available actions.

## Configure auxiliary buttons

1. Click an **Aux button** (1–5) to select it. The button shows a dot indicator when selected.
2. For the selected aux button, configure:
   - **Aux single-tap combo**: Assigns an action to single-tapping the selected aux button.
   - **Aux double-tap combo**: Assigns an action to double-tapping the selected aux button.
3. Repeat for each aux button as needed.

## Manage physical device

1. The **Physical** indicator shows the connection state and port name of a physical FlexControl device.
2. Click **Detect** to scan for a connected physical FlexControl.
3. Click **Close** to disconnect the physical device.

### Automatic reconnection

The physical FlexControl device now reconnects automatically when the USB connection is lost and restored:

- When the device disconnects (USB cable pulled, device unplugged, or port error), AetherSDR retries the connection every 2 seconds.
- If the device remains absent, the retry interval backs off, doubling each attempt up to a maximum of 30 seconds.
- On each retry, AetherSDR re-detects the port rather than reusing the old name, so a USB re-enumeration that assigns a new COM port still reconnects correctly.
- When the device returns, the connection is restored automatically; no manual action is needed.
- If you close the connection manually with **Close**, retrying stops.

## Compact mode

1. Click **Compact** to toggle compact mode. When enabled, auxiliary buttons are hidden and only the wheel and frequency display remain visible.
2. The dialog automatically resizes to fit the content. On short or DPI-scaled screens, a scroll bar appears to keep the full controller accessible.
3. Click **Compact** again to return to the full view.

## External spin

1. Click **External Spin** to enable external spin wheel tuning. When enabled, dragging on the panadapter triggers spin-wheel tuning gestures.

## What each control does

| Control | Behavior | Setting key |
|---|---|---|
| **Wheel** indicator | Virtual tuning wheel with frequency/mode readout. Rotate with mouse or touch. | None |
| **Physical** indicator | Shows physical FlexControl connection state and port name. Detect/Close buttons manage the device. | None |
| **Compact** toggle | Toggles compact mode: hides auxiliary buttons, shows only wheel and frequency. | None |
| **External Spin** toggle | Enables external spin wheel tuning from panadapter drags. | None |
| **Reverse** toggle | Reverses wheel tuning direction. | None |
| **Push (action)** combo | Assigns action to single tap of wheel. | `FlexControlButtonAction_*` |
| **Double-tap (action)** combo | Assigns action to double-tap of wheel. | (stored alongside single-tap) |
| **Wheel Tightness** slider | Adjusts virtual wheel coasting drag (0–100). 0 = tight, 100 = loose. | `FlexControlVirtualWheel` (nested JSON, looseness field) |
| **Mouse Sensitivity** slider | Adjusts pointer-to-wheel movement scale (0–100). 50 = 1.0x. | `FlexControlVirtualWheel` (nested JSON, sensitivity field) |
| **Aux buttons** (1–5) | Five configurable auxiliary buttons with dot indicator for active selection. | None |
| **Aux single-tap combo** | Assigns action to single-tap of selected aux button. | None |
| **Aux double-tap combo** | Assigns action to double-tap of selected aux button. | None |

## Indicators

| Indicator | Meaning |
|---|---|
| Slice / Frequency / Mode readout | Shows which slice is bound, its current frequency, and mode. |
| Physical status | Shows connection state and port name of the physical FlexControl device. |

## Tips

- The virtual wheel supports circular mouse/touch tuning: double-click the wheel to capture, then rotate your finger or mouse in a circular motion. Press Escape to release.
- **Wheel Tightness** and **Mouse Sensitivity** primarily affect trackpads and do not affect a physical FlexControl device.
- In compact mode, the dialog resizes to a minimal size. If the content exceeds the available screen height, the dialog scrolls vertically.
- Changes are saved automatically when you close the dialog.
- If the physical FlexControl disconnects and reconnects, AetherSDR restores the connection automatically within a few seconds.

## Related

- Configure single- and double-tap actions for the PUSH button

---

# Configure single- and double-tap actions for the PUSH button

Configure what happens when you tap or double-tap the wheel (PUSH button) in the AetherControl dialog. This lets you quickly change frequency step, switch bands, toggle functions, or run CWX macros without reaching for the mouse.

## Before you start

- Open the AetherControl dialog: `Settings > AetherControl...`

## Steps

1. Locate the **Push (action)** combo box. This sets the single-tap action.
2. Click the combo box and select the desired action from the list.
3. Locate the **Double-tap (action)** combo box directly below. This sets the double-tap action.
4. Click the combo box and select the desired action from the list.
5. Close the dialog. Changes are saved automatically.

## What each control does

| Control | Behavior | Setting key |
|---|---|---|
| **Push (action)** combo box | Assigns an action to a single tap (push) of the wheel. | `FlexControlButtonAction_*` |
| **Double-tap (action)** combo box | Assigns an action to a double-tap of the wheel. | (stored alongside single-tap in same settings structure) |

Available actions for both combo boxes include:

| ID | Label |
|---|---|
| `None` | None |
| `WheelFrequency` | Tune Slice |
| `BandZoom` | Band Zoom |
| `SegmentZoom` | Segment Zoom |
| `WheelRit` | RIT (Receive Incremental Tuning) |
| `WheelXit` | XIT (Transmit Incremental Tuning) |
| `WheelVolume` | Master Volume |
| `WheelSliceAudio` | Slice Audio Volume |
| `WheelHeadphoneVolume` | Headphone Volume |
| `WheelAgcT` | AGCT (Automatic Gain Control Threshold) |
| `WheelApf` | APF (Audio Peaking Filter) |
| `ClearRit` | Clear RIT |
| `ClearXit` | Clear XIT |
| `ToggleApf` | Toggle APF |
| `NextSlice` | Change Active Slice |
| `SplitActiveSlice` | Split Active Slice |
| `ToggleMox` | MOX |
| `WheelPower` | RF Power |
| `WheelCwSpeed` | CW Speed |
| `CwxF1` through `CwxF12` | CWX Macro 1 through 12 |
| `StepUp` | Step Up |
| `StepDown` | Step Down |
| `ToggleTune` | Toggle Tune |
| `ToggleMute` | Toggle Mute |
| `ToggleLock` | Toggle Lock |
| `PrevSlice` | Previous Slice |
| `ToggleAgc` | Toggle AGC |
| `VolumeUp` | Slice AF Up |
| `VolumeDown` | Slice AF Down |

### New in v26.6.3

- **Slice Audio Volume** (`WheelSliceAudio`): Adjusts the audio volume of the active slice independently from the master volume. This action was added to the available action list in v26.6.3.

## Tips

- Use a wheel action (Tune Slice, Master Volume, etc.) for single-tap and a one-shot action (Step Up, Band Zoom, etc.) for double-tap for complementary behavior.
- The double-tap guard time is 230 ms. Tap twice within that window to trigger the double-tap action.
- Double-click the virtual wheel to capture or release circular tuning using the mouse or trackpad. Press Escape as an alternative release. The capture hint label at the bottom of the dialog now reads "Double-click the knob to capture circular tuning."

## Related

- [Map push-button and double-tap actions to the wheel](map-push-button-and-double-tap-actions-to-the-wheel.md)
- [Configure the AetherControl / FlexControl hardware controller](configure-the-aethercontrol-flexcontrol-hardware-controller.md)