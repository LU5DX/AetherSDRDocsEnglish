# Remembers confirmation so the dialog does not show on subsequent sweeps

After you confirm the operator responsibility disclaimer and tick “Remember my answer”, AetherSDR persists that confirmation so the Antenna SWR Sweep – License Confirmation dialog is skipped on all future sweeps for the current station.

## Before you start

- You must have already started an Antenna SWR Sweep at least once (see [Confirm operator responsibility before running the antenna SWR sweep](confirm-operator-responsibility-before-running-the-antenna-swr-sweep.md)).
- The persisted setting is per-station (stored under the current station name in the settings file).

## Steps

1. When the “Antenna SWR Sweep — License Confirmation” dialog appears, read the operator responsibility disclaimer.
2. Check the **Remember my answer** checkbox.
3. Click **I am licensed to use this feature**.

The dialog sets the `SwrSweepLicenseConfirmed` key to `True` in AppSettings. On subsequent sweeps, the `.confirm()` helper reads this key and returns `true` immediately without showing the dialog.

## What each control does

| Control | Default | Persisted key | Behavior |
|---|---|---|---|
| **Remember my answer** checkbox | Unchecked | `SwrSweepLicenseConfirmed` | When checked, persists the confirmation to AppSettings so the dialog is skipped on subsequent sweeps. |
| **I am licensed to use this feature** button | — | — | Accepts the disclaimer and proceeds to the SWR sweep. Default button (highlighted with a blue border). |
| **Cancel** button | — | — | Rejects the disclaimer and aborts the sweep. The sweep will not start. |

## Tips

- The dialog also skips if you have a saved settings file from a previous session where you already checked **Remember my answer** — the key persists across application restarts.
- To make the dialog reappear, delete or manually edit the `SwrSweepLicenseConfirmed` line in your AetherSDR settings file (`~/.config/AetherSDR/AetherSDR.settings` on Linux/macOS).

## Related

- [Antenna SWR Sweep — License Confirmation overview](overview.md)
- [Confirm operator responsibility before running the antenna SWR sweep](confirm-operator-responsibility-before-running-the-antenna-swr-sweep.md)
