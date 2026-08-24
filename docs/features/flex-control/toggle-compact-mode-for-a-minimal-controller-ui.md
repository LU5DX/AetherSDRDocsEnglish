# AetherControl / FlexControl Dialog

The AetherControl dialog configures the FlexControl hardware controller and provides a virtual tuning wheel for the active slice. It includes wheel tuning, push-button action mapping, five auxiliary buttons with single- and double-tap actions, compact mode, and automatic reconnection for the physical device.

## Opening the dialog

Open the AetherControl dialog: `Settings > AetherControl…`

## What each control does

| Control | Default | Valid range | Setting key |
|---------|---------|-------------|-------------|
| Wheel (indicator) | — | — | — |
| Physical (indicator) | — | — | — |
| Compact (toggle button) | Off | — | `FlexControlCompactMode` |
| External Spin (toggle button) | Off | — | — |
| Reverse (toggle button) | Off | — | — |
| Push (action) (combo box) | — | — | `FlexControlButtonAction_*` |
| Double-tap (action) (combo box) | — | — | — |
| Wheel Tightness (slider) | 45 | 0–100 | `FlexControlVirtualWheel` (nested JSON, looseness field) |
| Mouse Sensitivity (slider) | 50 | 0–100 | `FlexControlVirtualWheel` (nested JSON, sensitivity field) |
| Aux buttons 1–5 (push button) | — | — | — |
| Aux single-tap combo (combo box) | — | — | — |
| Aux double-tap combo (combo box) | — | — | — |

## Virtual wheel

- **Wheel** — Rotate with mouse or touch to tune the active slice. Shows the frequency and mode readout.
- **Reverse** — Click to reverse the wheel tuning direction.
- **Wheel Tightness** — Adjusts virtual wheel coasting drag; 0 = tight (fast stop), 100 = loose (long coast). Primarily affects trackpads; does not affect the physical FlexControl. The slider is labeled with **Tight** and **Loose** endpoints.
- **Mouse Sensitivity** — Adjusts how much captured mouse or trackpad movement turns the virtual wheel. Midpoint (50) yields 1.0x scale. The slider is labeled with **Less** and **More** endpoints. Pointer deltas are clamped to 15° (π/12) per event to avoid jitter, and the anchor re-centers when the pointer crosses the wheel's center dead-zone without computing a delta.

## Physical FlexControl

- **Physical** — Shows the physical FlexControl connection state and port name. Use **Detect** and **Close** buttons to manage the physical device.
- The physical device reconnects automatically if it is unplugged and reinserted, or if the port becomes unavailable. Retry intervals start at 2 seconds and back off to a maximum of 30 seconds for persistent failures. The port is re-detected on each retry in case a USB re-enumeration assigned a different COM port.

## Compact mode

1. Click **Compact** to hide the auxiliary buttons and their action combo boxes, leaving only the wheel and frequency/mode readout.
2. Click **Compact** again to restore the full view.

## External spin

Click **External Spin** to enable spin-wheel tuning gestures from the panadapter. Dragging on the panadapter then triggers spin-wheel tuning.

## Action mapping

- **Push (action)** — Assigns an action to pushing the wheel (single tap).
- **Double-tap (action)** — Assigns an action to double-tapping the wheel.
- **Aux buttons 1–5** — Five configurable auxiliary buttons. Each has a **single-tap** and **double-tap** action combo box. The active button is indicated by an aux dot label.

## Available wheel actions

The following actions can be assigned to wheel presses and auxiliary button taps:

| Action ID | Display Name |
|-----------|--------------|
| ModeCycle | Mode Cycle |
| StepZoom | Step Zoom |
| ZoomReset | Zoom Reset |
| BandUp | Band Up |
| BandDown | Band Down |
| WheelRit | RIT (Receive Incremental Tuning) |
| WheelXit | XIT (Transmit Incremental Tuning) |
| WheelVolume | Master Volume |
| WheelSliceAudio | Slice Audio Volume |
| WheelHeadphoneVolume | Headphone Volume |
| WheelAgcT | AGCT (Automatic Gain Control Threshold) |
| WheelApf | APF (Audio Peaking Filter) |

**Note:** The **Slice Audio Volume** action (WheelSliceAudio) adjusts the audio volume of the active slice independently from the master and headphone volumes.

## Window sizing behavior (v26.7.4)

The AetherControl dialog uses a scrollable layout. When compact mode is off, the window ensures the full controller is available even on short or DPI-scaled screens. The content area scrolls vertically when its intrinsic height exceeds the available screen height. The minimum window width tracks the content's minimum width to prevent horizontal clipping.

## Related

- [AetherControl / FlexControl overview](overview.md)
- [Configure the AetherControl / FlexControl hardware controller](configure-the-aethercontrol-flexcontrol-hardware-controller.md)
- [Use the virtual wheel to tune the active slice](use-the-virtual-wheel-to-tune-the-active-slice.md)