# Adjust S-History marker lifetime, QRM gate and edge threshold

Fine-tune how Signal History markers behave on the panadapter — how long they live, how persistently a signal must hold to be flagged as QRM, and how aggressively the marker edge snaps to the carrier.

## Before you start

- Open SpotHub: `Settings > SpotHub...`
- Click the **Display** tab.

## Steps

1. Under **Signal History**, adjust **Marker Lifetime:** by dragging the slider. Inactive markers are removed after this many seconds (range 15–300 sec, default 60). Left double-click the slider to reset to 60.

2. Adjust **QRM Gate:** — the seconds a narrow carrier or wideband signal must persist before the system classifies it as QRM (range 3–30 sec, default 6). Left double-click the slider to reset to 6.

3. Adjust **Edge Threshold:** — the dB level above the noise floor for the slope-edge walk that refines a marker’s carrier-side edge. A lower value hugs the carrier more tightly but is more noise-sensitive (range 1.0–10.0 dB, default 3.0). Left double-click the slider to reset to 3.0.

4. Optionally enable **Snap to Step:** in the Signal History section to round click-to-tune to the nearest active slice step size.

## What each control does

| Control | Label on slider | Default | Valid range | Setting key | Notes |
|---|---|---|---|---|---|
| **Marker Lifetime:** | `15 sec` – `300 sec` | 60 | 15–300 sec | `SHistoryLifetimeS` | Left double-click resets to 60 |
| **QRM Gate:** | `3 sec` – `30 sec` | 6 | 3–30 sec | `SHistoryQrmGateS` | Left double-click resets to 6 |
| **Edge Threshold:** | `1.0 dB` – `10.0 dB` | 3.0 | 1.0–10.0 dB | `SHistorySoftEdgeDb` | Left double-click resets to 3.0 |
| **Snap to Step:** | toggle button | Disabled | Enabled / Disabled | `SHistorySnapToStep` | |

## Tips

- **Marker Lifetime** controls voice-bandwidth signal markers (gold by default). QRM markers (red by default) also follow this lifetime — they are not separately timed.
- To see Signal History markers on the panadapter in the first place, enable **Signals** and/or **QRM** under the top toggle row in the Display tab. Their persisted keys are `SHistoryMarkersEnabled` and `SHistoryQrmEnabled`.
- Turning on **Snap to Step** hides the small carrier offset that can appear when clicking an S-History marker; the tune frequency snaps to the next multiple of the active slice’s step size.
- Left double-clicking any slider resets it to its default value, providing a quick way to restore factory behavior without dragging.

## Troubleshooting

- **Markers disappear too quickly** — Increase **Marker Lifetime:** to a higher value. Left double-click the slider to reset to the 60-second default.
- **QRM markers appear on weak signals that aren’t really interference** — Raise **QRM Gate:** so the system requires a longer hold time before classifying the signal as QRM. Left double-click the slider to reset to the 6-second default.
- **Marker edges wobble or jump** — Increase **Edge Threshold:** slightly (e.g., from 3.0 to 4.0 dB) to reduce noise sensitivity. Left double-click the slider to reset to the 3.0 dB default.

## Related

- [Toggle Signal History voice markers on the panadapter](toggle-signal-history-voice-markers-on-the-panadapter.md)
- [Toggle QRM markers to see persistent carriers and interference](toggle-qrm-markers-to-see-persistent-carriers-and-interference.md)
- [Pick custom colors for voice signal and QRM markers](pick-custom-colors-for-voice-signal-and-qrm-markers.md)
- [Enable Snap to Step for precise S-History tuning](enable-snap-to-step-for-precise-s-history-tuning.md)
- Add startup commands for DX cluster connection