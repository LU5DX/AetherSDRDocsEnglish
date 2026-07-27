# Toggle compact mode for a minimal controller UI

This page walks you through switching the AetherControl dialog to compact mode, which hides the auxiliary buttons and shows only the virtual wheel and frequency readout for a streamlined appearance.

## Before you start

- Open the AetherControl dialog: `Settings > AetherControl…`

## Steps

1. In the AetherControl dialog, locate the **Compact** toggle button.
2. Click **Compact** to enable compact mode. The auxiliary buttons and their action combo boxes will be hidden, leaving only the wheel and frequency/mode readout.
3. To exit compact mode, click **Compact** again to restore the full view.

## What each control does

| Control | Default | Valid range | Setting key |
|---------|---------|-------------|-------------|
| Compact (toggle button) | Off | — | `FlexControlCompactMode` |
| Wheel (indicator) | — | — | — |
| Physical (indicator) | — | — | — |
| External Spin (toggle button) | Off | — | — |
| Reverse (toggle button) | Off | — | — |
| Push (action) (combo box) | — | — | `FlexControlButtonAction_*` |
| Double-tap (action) (combo box) | — | — | — |
| Wheel Tightness (slider) | 45 | 0–100 | `FlexControlVirtualWheel` (nested JSON, looseness field) |
| Mouse Sensitivity (slider) | 50 | 0–100 | `FlexControlVirtualWheel` (nested JSON, sensitivity field) |
| Aux buttons 1–5 (push button) | — | — | — |
| Aux single-tap combo (combo box) | — | — | — |
| Aux double-tap combo (combo box) | — | — | — |

## Available wheel actions (for Push, Double-tap, and Aux button actions)

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

The AetherControl dialog now uses a scrollable layout. When compact mode is off, the window ensures the full controller is available even on short or DPI-scaled screens. The content area scrolls vertically when its intrinsic height exceeds the available screen height. The minimum window width tracks the content's minimum width to prevent horizontal clipping.

## Related

- [AetherControl / FlexControl overview](overview.md)
- [Configure the AetherControl / FlexControl hardware controller](configure-the-aethercontrol-flexcontrol-hardware-controller.md)
- [Use the virtual wheel to tune the active slice](use-the-virtual-wheel-to-tune-the-active-slice.md)