# Configure the AetherControl / FlexControl hardware controller

Configure a physical FlexControl or the virtual AetherControl wheel for tuning and button actions. The dialog lets you manage connection, wheel behavior, and button mappings for both hardware and virtual controllers.

## Before you start

- A physical FlexControl connected by USB (for hardware use)
- For virtual use only, no hardware is needed

## Steps

1. Open **Settings > AetherControl...**
2. To connect a physical FlexControl, click **Detect** in the Physical section. The dialog scans serial ports and connects automatically. If detection fails, click **Close** and try again.
3. To use the virtual wheel, double-click and drag around the Wheel indicator to tune the active slice. Double-click again to release capture, or press Escape.
4. Adjust the **Wheel Tightness** slider to set coasting drag (0 = tight, 100 = loose). Default: 45.
5. Adjust the **Mouse Sensitivity** slider to scale captured pointer movement (0 = less, 100 = more). Default: 50.
6. Toggle **Compact** to hide auxiliary buttons and show only the wheel and frequency readout.
7. Toggle **External Spin** to enable panadapter drag-initiated spin-wheel tuning.
8. Toggle **Reverse** to invert the wheel tuning direction.
9. Configure the wheel Push action: select an action from the **Push** combo box.
10. Configure the wheel Double-tap action: select an action from the **Double-tap** combo box.
11. To configure auxiliary buttons, click an aux button (labeled with dots). Then select actions from the **Aux single-tap combo** and **Aux double-tap combo** that appear.

## What each control does

| Control | Default | Valid range | Setting key | Behavior |
|---------|---------|-------------|-------------|----------|
| Wheel | — | — | — | Virtual wheel: double-click to capture, then rotate with mouse/touch to tune the active slice. Double-click again or press Escape to release. Shows frequency and mode readout. |
| Physical | — | — | `FlexControlPort`, `FlexControlOpen`, `FlexControlAutoDetect` | Shows physical FlexControl connection state and port name. Detect/Close buttons manage the device. Automatically restores LED state after device reset. |
| Compact | — | — | `FlexControlCompactMode` | Hides auxiliary buttons; shows only wheel and frequency. |
| External Spin | — | — | `FlexControlVirtualExternalSpin` | Enables panadapter drag-triggered spin-wheel tuning. |
| Reverse | — | — | `FlexControlInvertDir` | Reverses wheel tuning direction. |
| Push | — | — | `FlexControlButtonAction_*` | Action assigned to single-tapping the wheel. |
| Double-tap | — | — | stored per-button | Action assigned to double-tapping the wheel. |
| Wheel Tightness | 45 | 0–100 | `FlexControlVirtualWheel` (looseness field) | Adjusts virtual wheel coasting drag. 0 = tight (fast stop), 100 = loose (long coast). |
| Mouse Sensitivity | 50 | 0–100 | `FlexControlVirtualWheel` (sensitivity field) | Scales captured pointer movement. 50 = 1.0x scale. De-jitter clamps single-event pointer deltas to 15°. Lazy re-anchoring: when pointer crosses through centre dead-zone, next movement re-anchors without computing a delta. |
| Aux buttons (1–5) | — | 5 buttons | — | Click to select; then configure single- and double-tap actions. |
| Aux single-tap combo | — | — | `FlexControlBtn1Action0`–`FlexControlBtn4Action0` | Action for single-tapping the selected aux button. |
| Aux double-tap combo | — | — | `FlexControlBtn1Action1`–`FlexControlBtn4Action1` | Action for double-tapping the selected aux button. |

## Tips

- The **Wheel Tightness** and **Mouse Sensitivity** sliders only affect the virtual wheel (trackpad/pointer use), not a physical FlexControl.
- Pre-built action IDs include: `Tune Slice`, `Band Zoom`, `Segment Zoom`, `RIT`, `XIT`, `Master Volume`, `Headphone Volume`, `AGCT`, `APF`, `Clear RIT`, `Clear XIT`, `Toggle APF`, `Change Active Slice`, `Split Active Slice`, `MOX`, `RF Power`, `CW Speed`, `Step Up`, `Step Down`, `Toggle Tune`, `Toggle Mute`, `Toggle Lock`, `Previous Slice`, `Toggle AGC`, `Slice AF Up`, `Slice AF Down`, `None`, and CWX macros 1–12.
- Settings are saved automatically when you adjust controls in this dialog.
- The virtual wheel now uses double-click to capture and release, providing a more intuitive experience than the previous click-to-capture / Escape-to-release model. Escape still works as a secondary release path.
- The FlexControl dialog automatically restores LED state on the physical device when it receives a hardware reset command, ensuring the Aux LEDs match the application's active wheel-mode button.

## Troubleshooting

- **Physical FlexControl not detected** — Ensure the device is plugged into a USB port. Click **Detect** again. If still not found, try a different USB cable or port.
- **Virtual wheel tuning feels sluggish** — Increase **Mouse Sensitivity** and decrease **Wheel Tightness** for quicker response.
- **Aux LEDs on physical FlexControl don't match** — This is now handled automatically. The dialog restores LED state after device resets, correcting any mismatch that could occur during power-on sequences.

## Related

- [AetherControl / FlexControl overview](overview.md)
- [Use the virtual wheel to tune the active slice](use-the-virtual-wheel-to-tune-the-active-slice.md)
- [Configure single- and double-tap actions for the PUSH button](configure-single-and-double-tap-actions-for-the-push-button.md)
- [Set up aux buttons with single- and double-tap actions](set-up-aux-buttons-with-single-and-double-tap-actions.md)
- [Adjust wheel tightness (coasting feel)](adjust-wheel-tightness-coasting-feel.md)
- [Adjust mouse sensitivity for the virtual wheel](adjust-mouse-sensitivity-for-the-virtual-wheel.md)
- [Toggle compact mode for a minimal controller UI](toggle-compact-mode-for-a-minimal-controller-ui.md)
- [Toggle Auto Spin for external frequency change animation](toggle-auto-spin-for-external-frequency-change-animation.md)
- [Toggle Reverse to invert tuning direction](toggle-reverse-to-invert-tuning-direction.md)
- [Map push-button and double-tap actions to the wheel](map-push-button-and-double-tap-actions-to-the-wheel.md)