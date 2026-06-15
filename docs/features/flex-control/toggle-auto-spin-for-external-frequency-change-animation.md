# Toggle Auto Spin for external frequency change animation

Enable or disable the automatic virtual wheel spin animation that plays when an external source changes the slice frequency, such as clicking on the panadapter or using CAT commands.

## Before you start

- Open the AetherControl dialog via **Settings > AetherControl...**

## Steps

1. Click **External Spin** to toggle the animation on or off.

When enabled, dragging on the panadapter or changing frequency from an external source triggers a spin-wheel tuning gesture animation on the virtual wheel. When disabled, frequency changes happen immediately without animation.

## What each control does

| Control | Label | Behavior |
|---------|-------|----------|
| Toggle button | External Spin | Enables or disables the spin animation on the virtual wheel when frequency changes originate from outside the wheel. Setting key: `FlexControlVirtualExternalSpin` |
| Toggle button | Reverse | Reverses the wheel tuning direction. |
| Toggle button | Compact | Toggles compact mode: hides auxiliary buttons, shows only the wheel and frequency for a minimal UI. |
| Slider | Wheel Tightness | Adjusts virtual wheel coasting drag; 0 = tight (fast stop), 100 = loose (long coast). Primarily for trackpads; does not affect physical FlexControl. Setting key: `FlexControlVirtualWheel` (nested JSON, looseness field). |
| Slider | Mouse Sensitivity | Adjusts how much captured mouse/trackpad movement turns the virtual wheel. Midpoint (50) yields 1.0x scale. Primarily for trackpads; does not affect physical FlexControl. Setting key: `FlexControlVirtualWheel` (nested JSON, sensitivity field). |
| Combo box | Push (action) | Assigns an action to pushing the wheel (single tap). Options include mode cycle, step zoom, zoom reset, band up/down, RIT, XIT, Master Volume, Slice Audio Volume, Headphone Volume, AGCT, APF, and more. Setting key: `FlexControlButtonAction_*`. |
| Combo box | Double-tap (action) | Assigns an action to double-tapping the wheel. |
| Push button | Aux buttons (1-5) | Five configurable auxiliary buttons; labeled with aux dots to indicate active selection. |
| Combo box | Aux single-tap combo | Assigns an action to single-tapping the selected aux button. |
| Combo box | Aux double-tap combo | Assigns an action to double-tapping the selected aux button. |

## Indicators

| Indicator | Meaning |
|-----------|---------|
| Wheel | Virtual FlexControl wheel showing frequency and mode readout of the active slice. Rotate with mouse or touch to tune. |
| Physical | Shows physical FlexControl connection state and port name. Use Detect/Close buttons to manage the physical device. |

## Wheel action options

The following actions can be assigned to wheel push, double-tap, or aux button taps:

| Action ID | Description |
|-----------|-------------|
| WheelRit | RIT (Receive Incremental Tuning) |
| WheelXit | XIT (Transmit Incremental Tuning) |
| WheelVolume | Master Volume |
| WheelSliceAudio | Slice Audio Volume |
| WheelHeadphoneVolume | Headphone Volume |
| WheelAgcT | AGCT (Automatic Gain Control Threshold) |
| WheelApf | APF (Audio Peaking Filter) |

## Related

- [Use the virtual wheel to tune the active slice](use-the-virtual-wheel-to-tune-the-active-slice.md)
- [Configure the AetherControl / FlexControl hardware controller](configure-the-aethercontrol-flexcontrol-hardware-controller.md)