# Pick custom colors for voice signal and QRM markers

Signal History markers distinguish between detected voice-width signals (gold) and persistent QRM carriers (red). You can change these colors to suit your panadapter theme or personal preference.

## Before you start

- AetherSDR must be connected to a radio.
- The Display tab in SpotHub is open (`Settings > SpotHub... > Display`).

## Steps

1. Click **Settings** > **SpotHub...** to open the SpotHub dialog.
2. Click the **Display** tab.
3. In the **Signal History** section on the right, locate the **Signals** and **QRM** color swatches.
4. Click the **Signals** color swatch (gold `#FFC800` by default, setting key `SHistoryColorSignals`).
5. Select a new color in the color picker and click **OK**.
6. Click the **QRM** color swatch (red `#FF0000` by default, setting key `SHistoryColorQrm`).
7. Select a new color in the color picker and click **OK**.

Changes apply immediately to all visible Signal History and QRM markers on the panadapter.

## What each control does

| Control | Default | Valid range | Setting key |
|---|---|---|---|
| **Signals** color swatch (Signal History) | `#FFC800` | Any QColor | `SHistoryColorSignals` |
| **QRM** color swatch (Signal History) | `#FF0000` | Any QColor | `SHistoryColorQrm` |

## Related

- [Toggle Signal History voice markers on the panadapter](toggle-signal-history-voice-markers-on-the-panadapter.md)
- [Toggle QRM markers to see persistent carriers and interference](toggle-qrm-markers-to-see-persistent-carriers-and-interference.md)
- [Adjust S-History marker lifetime, QRM gate and edge threshold](adjust-s-history-marker-lifetime-qrm-gate-and-edge-threshold.md)
