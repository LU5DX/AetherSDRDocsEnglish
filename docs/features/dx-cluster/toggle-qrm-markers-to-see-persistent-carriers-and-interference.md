# Toggle QRM markers to see persistent carriers and interference

Turn on QRM markers to highlight persistent narrow carriers and wideband interference on the panadapter, making it easier to avoid or investigate signals that may be constant noise sources.

## Steps

1. Open **Settings > SpotHub...**.
2. Click the **Display** tab.
3. In the **QRM (Signal History)** row, click the toggle button to enable it (default: Disabled). Red markers appear on the panadapter for signals classified as QRM.

To disable QRM markers, click the toggle again.

## What each control does

| Control | Setting key | Default | Behavior |
|---------|-------------|---------|----------|
| **QRM (Signal History)** | `SHistoryQrmEnabled` | Disabled | Master toggle for red QRM markers on the panadapter. |
| **QRM Gate** (slider) | `SHistoryQrmGateS` | 6 s | How long a narrow carrier or wideband signal must persist before being classified as QRM. Range: 3–30 s. Double-click the slider knob to reset to the default value of 6 s. |
| **Edge Threshold** (slider) | `SHistorySoftEdgeDb` | 3.0 dB | Threshold above noise floor for the slope edge walk that refines the S-History carrier-side edge. Range: 1.0–10.0 dB. Lower = closer to carrier but more noise-sensitive. Double-click the slider knob to reset to the default value of 3.0 dB. |
| **QRM color swatch** | `SHistoryColorQrm` | #FF0000 | Opens a color picker to change the QRM marker color. |

## Tips

- QRM markers are independent from Signal History voice markers (the `SHistoryMarkersEnabled` toggle). You can enable one, both, or neither.
- Use the **QRM Gate** slider to ignore brief transmissions and only mark signals that persist long enough to be interference.
- Double-click any slider knob in the Signal History section to instantly reset it to its factory default value.
- The SpotHub dialog now uses theme-aware colors instead of hardcoded values. Status labels change color based on the active theme: accent color when connected, label color when disconnected, and danger color on error.

## Related

- [Toggle Signal History voice markers on the panadapter](toggle-signal-history-voice-markers-on-the-panadapter)
- [Adjust S-History marker lifetime, QRM gate and edge threshold](adjust-s-history-marker-lifetime-qrm-gate-and-edge-threshold)
- [Pick custom colors for voice signal and QRM markers](pick-custom-colors-for-voice-signal-and-qrm-markers)