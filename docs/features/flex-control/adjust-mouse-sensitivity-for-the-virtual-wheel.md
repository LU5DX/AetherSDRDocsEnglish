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

# Assign actions to the wheel push and double-tap

Configure what happens when you push or double-tap the virtual wheel in the AetherControl dialog.

## Before you start

- Open the AetherControl dialog: `Settings > AetherControl...`
- The virtual wheel must be active.

## Steps

1. In the **Push (action)** combo box, select an action for a single tap on the wheel.
2. In the **Double-tap (action)** combo box, select an action for a double-tap on the wheel.

## Available wheel actions

The following actions can be assigned to wheel push or double-tap:

| Action ID | Display Name |
|-----------|--------------|
| `WheelRit` | RIT (Receive Incremental Tuning) |
| `WheelXit` | XIT (Transmit Incremental Tuning) |
| `WheelVolume` | Master Volume |
| `WheelSliceAudio` | Slice Audio Volume |
| `WheelHeadphoneVolume` | Headphone Volume |
| `WheelAgcT` | AGCT (Automatic Gain Control Threshold) |
| `WheelApf` | APF (Audio Peaking Filter) |

- **WheelSlice Audio** controls the audio volume of the currently active slice. This is separate from the master volume control.
- Legacy settings using `WheelMasterAf` are automatically recognized as equivalent to `WheelVolume`.

# Configure auxiliary buttons

The five auxiliary buttons on the virtual FlexControl can each have separate single-tap and double-tap actions.

## Before you start

- Open the AetherControl dialog: `Settings > AetherControl...`

## Steps

1. Click one of the five **Aux** buttons (labeled with dots) to select it.
2. In the **Aux single-tap combo**, select the action for a single tap.
3. In the **Aux double-tap combo**, select the action for a double-tap.

## Tips

- Each aux button remembers its own single-tap and double-tap assignments independently.
- The selected aux button is indicated by the dot state next to its label.