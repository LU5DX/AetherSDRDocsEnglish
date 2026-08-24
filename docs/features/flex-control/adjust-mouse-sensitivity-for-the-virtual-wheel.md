# AetherControl / FlexControl Dialog

The AetherControl dialog provides configuration for both the physical FlexControl hardware and the virtual tuning wheel. It includes a virtual wheel display, auxiliary button configuration, and tuning sensitivity settings.

## Opening the dialog

- Select `Settings > AetherControl...`

## Virtual wheel display

The virtual wheel shows the currently active slice, its frequency, and mode. You can rotate it with mouse or touch to tune the active slice.

## Physical FlexControl

The dialog shows the physical FlexControl connection state and port name. Use the **Detect** and **Close** buttons to manage the physical device.

If the connection to a physical FlexControl is lost — for example, the USB cable is unplugged — AetherSDR automatically retries the connection. Retries start after 2 seconds and back off to a maximum interval of 30 seconds until the device is detected again. The driver re-detects the port name on each retry, so a device that re-enumerates on a different COM port is reconnected correctly. The failure is logged once per outage rather than on every retry.

## Compact mode

Toggle **Compact** to hide the auxiliary buttons and show only the wheel and frequency readout for a minimal UI.

## External spin

Enable **External Spin** to allow drag gestures on the panadapter to trigger spin-wheel tuning behavior.

## Reverse direction

Enable **Reverse** to reverse the wheel tuning direction.

## Wheel actions

Assign actions to pushing or double-tapping the wheel:

| Control | Description |
|---------|-------------|
| **Push (action)** | Select an action for a single tap on the wheel |
| **Double-tap (action)** | Select an action for a double-tap on the wheel |

Available wheel actions:

| Action ID | Display Name |
|-----------|--------------|
| `WheelRit` | RIT (Receive Incremental Tuning) |
| `WheelXit` | XIT (Transmit Incremental Tuning) |
| `WheelVolume` | Master Volume |
| `WheelSliceAudio` | Slice Audio Volume |
| `WheelHeadphoneVolume` | Headphone Volume |
| `WheelAgcT` | AGCT (Automatic Gain Control Threshold) |
| `WheelApf` | APF (Audio Peaking Filter) |

**WheelSlice Audio** controls the audio volume of the currently active slice, separate from the master volume control. Legacy settings using `WheelMasterAf` are automatically recognized as equivalent to `WheelVolume`.

## Auxiliary buttons

Configure five auxiliary buttons, each with separate single-tap and double-tap actions:

1. Click one of the five **Aux** buttons (labeled with dots) to select it.
2. In the **Aux single-tap combo**, select the action for a single tap.
3. In the **Aux double-tap combo**, select the action for a double-tap.

Each aux button remembers its own assignments independently. The selected aux button is indicated by the dot state next to its label.

## Wheel Tightness slider

Adjusts virtual wheel coasting drag:

| Control | Default | Range | Setting Key |
|---------|---------|-------|-------------|
| Wheel Tightness slider | 45 | 0–100 | `FlexControlVirtualWheel` (nested JSON, `looseness` field) |

- **Tight** (left, value 0): fast stop after you release the wheel.
- **Loose** (right, value 100): long coast after you release the wheel.
- Primarily affects trackpad usage; does not affect a physical FlexControl.
- Formerly stored under legacy flat key `FlexControlVirtualWheelLooseness`; auto-migrated on first read.

## Mouse Sensitivity slider

Adjusts how much pointer movement turns the virtual wheel:

| Control | Default | Range | Setting Key |
|---------|---------|-------|-------------|
| Mouse Sensitivity slider | 50 | 0–100 | `FlexControlVirtualWheel` (nested JSON, `sensitivity` field) |

- **Less** (left, value 0): requires more pointer movement.
- **More** (right, value 100): requires less pointer movement.
- Midpoint (50) yields 1.0x scaling.
- Single-event pointer deltas are clamped to 15° (π/12 radians) to reduce jitter.
- Lazy re-anchoring prevents unwanted jumps when the pointer crosses through the wheel's center dead-zone.
- Affects only the virtual wheel; does not change behavior of a physical FlexControl.

### Tips

- If using a trackpad, try starting Mouse Sensitivity at value 65 and adjust from there.
- Use the companion **Wheel Tightness** slider to control coasting feel.

## Capture/release behavior

- **Double-click** the virtual wheel to capture mouse input for circular tuning.
- **Double-click** again to release capture.
- Press **Escape** as a secondary release path.
- Single-clicking no longer captures or releases the wheel.

## Window sizing

The AetherControl dialog adapts to your screen size. When opened in non-compact mode on a shorter display, the content area scrolls vertically so all controls remain accessible. The dialog never opens taller than the available workspace height.