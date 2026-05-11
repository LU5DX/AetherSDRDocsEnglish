# Toggle Signal History voice markers on the panadapter

Enable gold markers on the panadapter that show detected voice-width signals, helping you visually identify active voice transmissions.

## Before you start

- AetherSDR must be running (no radio connection required for this setting).

## Steps

1. Open **Settings > SpotHub...**.
2. Click the **Display** tab.
3. Click **Signals** (labeled "Signal History") to toggle it to the checked/on state.

The gold markers now appear on the panadapter at frequencies where AetherSDR has detected voice-width signals. Click a marker with the cursor to tune your active slice to that frequency.

## What each control does

| Control | Default | Valid range | Setting key |
|---|---|---|---|
| **Signals** (toggle button, labeled "Signal History" in the Display tab) | Disabled | On / Off | `SHistoryMarkersEnabled` |

This toggle has a dual path — it can also be activated from **View > Signal History Markers** in the main menu.

## Tips

- The gold markers appear only while the signal is active. Use the **Marker Lifetime** slider on the same Display tab to control how long an inactive marker remains visible (default 60 seconds).
- To remove all markers (and all spots) from the panadapter at once, click **Clear All** on the Display tab.

## Related

- [Toggle QRM markers to see persistent carriers and interference](toggle-qrm-markers-to-see-persistent-carriers-and-interference.md)
- [Adjust S-History marker lifetime, QRM gate and edge threshold](adjust-s-history-marker-lifetime-qrm-gate-and-edge-threshold.md)
- [Pick custom colors for voice signal and QRM markers](pick-custom-colors-for-voice-signal-and-qrm-markers.md)
- [Enable Snap to Step for precise S-History tuning](enable-snap-to-step-for-precise-s-history-tuning.md)
