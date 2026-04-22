# Poll POTA activations

AetherSDR can periodically fetch current Parks on the Air (POTA) activations from `api.pota.app` and display them as spots on the panadapter. This lets you see active POTA operators across all bands without a separate browser or app.

## Before you start

- AetherSDR must have an active internet connection to reach `api.pota.app`.
- Spot display on the panadapter requires `IsSpotsEnabled` to be on. Check `Settings > SpotHub...` > Display tab > **Spots:** is set to **Enabled**.

## Steps

1. Open `Settings > SpotHub...`.
2. Click the **POTA** tab.
3. Review the **Server:** indicator — it shows `api.pota.app (HTTP polling)` and cannot be changed.
4. Set **Poll Interval:** to the number of seconds between polls (stored as `PotaPollInterval`).
5. Click **Start**. The status indicator changes to **Polling**.
6. Watch the **POTA Activations** console for incoming activation data. Spots appear on the panadapter once received.
7. To choose a spot color, click **Spot Color:** and pick a color from the dialog (stored as `PotaSpotColor`).
8. To start polling automatically every time AetherSDR launches, click **Auto-start on startup** so it is active (stored as `PotaAutoStart`).

## What each control does

| Control | Description | Setting key |
|---|---|---|
| **Server:** | Read-only indicator showing the fixed endpoint `api.pota.app (HTTP polling)`. | — |
| **Poll Interval:** | Seconds between HTTP polls to `api.pota.app`. | `PotaPollInterval` |
| **Start / Stop** | Starts or stops POTA polling. Status shows **Polling** when active, **Stopped** when inactive. | — |
| **Auto-start on startup** | When active, polling begins automatically at launch. | `PotaAutoStart` |
| **POTA Activations** | Read-only console showing the raw activation feed received from each poll. | — |
| **Spot Color:** | Opens a color picker for POTA spots on the panadapter. | `PotaSpotColor` |

## Tips

- If you want to tune directly to a POTA activation, switch to the **Spot List** tab and double-click the row. See [Tune to a spot by double-clicking the spot list](tune-to-a-spot-by-double-clicking-the-spot-list.md).
- POTA spots respect the global spot display settings (lifetime, position, font size, stacking). Adjust those on the **Display** tab or see [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md).

## Troubleshooting

- **Status stays Stopped after clicking Start** — Verify your system has a working internet connection and can reach `api.pota.app` on port 443.
- **No spots appear on the panadapter despite Polling status** — Check that **Spots:** on the **Display** tab is set to **Enabled** (`IsSpotsEnabled`). Also confirm that no active POTA stations happen to fall outside the currently visible panadapter range.
- **Spots disappear quickly** — The global **Spot Lifetime:** slider on the **Display** tab controls how long any spot remains visible. Increase it to keep POTA spots on screen longer (`SpotsLifetime`).

## Related

- [SpotHub overview](overview.md)
- [Tune to a spot by double-clicking the spot list](tune-to-a-spot-by-double-clicking-the-spot-list.md)
- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
- [Pick colors for each spot source](pick-colors-for-each-spot-source.md)
- [Clear all spots from the panadapter](clear-all-spots-from-the-panadapter.md)
