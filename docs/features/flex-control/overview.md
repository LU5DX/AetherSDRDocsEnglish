# AetherControl / FlexControl overview

AetherControl is a dedicated configuration dialog for the FlexControl hardware rotary controller and its on-screen virtual equivalent. Use it to tune the active slice, assign actions to physical or virtual buttons, and adjust the feel of the virtual wheel.

## Before you start

- A radio connection is **not required** to configure the dialog — settings are persisted and take effect when a radio becomes available.

## How it works

The AetherControl dialog provides a virtual tuning wheel and configuration panel for both the physical FlexControl device and the on-screen virtual wheel.

**Virtual wheel** — A circular control rendered on screen that you rotate with mouse or touch gestures. It shows the active slice, frequency, and mode readout. Movement is translated into tuning steps based on Mouse Sensitivity and Wheel Tightness settings. Double-click the knob to capture mouse input for circular tuning; double-click again to release. Press Escape as a secondary release path.

**Physical FlexControl** — When a genuine FlexControl hardware controller is connected via serial port, the dialog shows its connection state and port name. Use the Detect and Close buttons to manage the physical device. When connected, the physical wheel and buttons operate in parallel with the virtual wheel. If the device resets (e.g., on power-up), AetherSDR automatically re-issues the cached LED state so the hardware matches the application's active wheel-mode button.

**Button actions** — The wheel itself has a push (single-tap) and double-tap action assignment. Five auxiliary buttons each support their own single-tap and double-tap actions. The available actions include tuning, mode cycling, zoom control, RIT/XIT, volume, AGC threshold, APF, CWX macros, slice management, and MOX.

**Compact mode** — Hides the auxiliary buttons, showing only the wheel and frequency readout for a minimal interface. Toggled via the Compact button.

**External Spin** — Enables a wheel-spin gesture when dragging on the panadapter outside this dialog. Frequency changes from external sources (e.g., clicking the panadapter) trigger a brief wheel rotation animation.

**Reverse** — Inverts the direction that wheel rotation moves frequency: clockwise tunes down instead of up (or vice versa).

**Wheel Tightness** — Slider (0–100, default 45) that controls how much the virtual wheel coasts after you release it. 0 = stops immediately (tight); 100 = continues spinning for a long time (loose). Stored in `FlexControlVirtualWheel` (JSON, `looseness` field). Primarily affects trackpad input; does not change physical FlexControl behavior.

**Mouse Sensitivity** — Slider (0–100, default 50) that scales how much pointer movement is required to turn the virtual wheel. Midpoint (50) is 1.0× scale. 0 = less movement needed; 100 = more movement needed. Stored in `FlexControlVirtualWheel` (JSON, `sensitivity` field). Primarily affects trackpad input; does not change physical FlexControl behavior.

**Auxiliary buttons (1–5)** — Five configurable buttons, each with its own single-tap and double-tap action combo box. The buttons show active selection via aux dots.

**Configurable actions** — The following actions are available for any button assignment:

| Action ID | Label |
|-----------|-------|
| WheelFrequency | Tune Slice |
| BandZoom | Band Zoom |
| SegmentZoom | Segment Zoom |
| WheelRit | RIT (Receive Incremental Tuning) |
| WheelXit | XIT (Transmit Incremental Tuning) |
| WheelVolume | Master Volume |
| WheelHeadphoneVolume | Headphone Volume |
| WheelAgcT | AGCT (Automatic Gain Control Threshold) |
| WheelApf | APF (Audio Peaking Filter) |
| ClearRit | Clear RIT |
| ClearXit | Clear XIT |
| ToggleApf | Toggle APF |
| NextSlice | Change Active Slice |
| SplitActiveSlice | Split Active Slice |
| ToggleMox | MOX |
| WheelPower | RF Power |
| WheelCwSpeed | CW Speed |
| CwxF1–CwxF12 | CWX Macro 1–12 |
| StepUp | Step Up |
| StepDown | Step Down |
| ToggleTune | Toggle Tune |
| ToggleMute | Toggle Mute |
| ToggleLock | Toggle Lock |
| PrevSlice | Previous Slice |
| ToggleAgc | Toggle AGC |
| VolumeUp | Slice AF Up |
| VolumeDown | Slice AF Down |
| None | None |

## Tips

- The Wheel Tightness and Mouse Sensitivity sliders are designed primarily for trackpad users. A physical FlexControl's mechanical detents are unaffected.
- The virtual wheel uses de-jitter logic that clamps single-event pointer movements to 15° (π/12 radians) to prevent sudden jumps.
- Double-click the virtual knob to capture mouse input, and double-click again to release. This replaces the previous single-click capture behavior that required Escape to release.
- If the physical FlexControl resets, AetherSDR automatically restores the correct LED state for the active wheel-mode button.

## Related

- [Configure the AetherControl / FlexControl hardware controller](configure-the-aethercontrol-flexcontrol-hardware-controller.md)
- [Use the virtual wheel to tune the active slice](use-the-virtual-wheel-to-tune-the-active-slice.md)
- [Configure single- and double-tap actions for the PUSH button](configure-single-and-double-tap-actions-for-the-push-button.md)
- [Set up aux buttons with single- and double-tap actions](set-up-aux-buttons-with-single-and-double-tap-actions.md)
- [Adjust wheel tightness (coasting feel)](adjust-wheel-tightness-coasting-feel.md)
- [Adjust mouse sensitivity for the virtual wheel](adjust-mouse-sensitivity-for-the-virtual-wheel.md)
- [Toggle compact mode for a minimal controller UI](toggle-compact-mode-for-a-minimal-controller-ui.md)
- [Toggle Auto Spin for external frequency change animation](toggle-auto-spin-for-external-frequency-change-animation.md)
- [Toggle Reverse to invert tuning direction](toggle-reverse-to-invert-tuning-direction.md)
- [Map push-button and double-tap actions to the wheel](map-push-button-and-double-tap-actions-to-the-wheel.md)