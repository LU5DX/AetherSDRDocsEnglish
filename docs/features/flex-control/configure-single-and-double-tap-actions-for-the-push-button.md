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