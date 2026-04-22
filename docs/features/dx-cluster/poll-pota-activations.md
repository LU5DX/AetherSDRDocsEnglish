# Poll POTA activations

AetherSDR can periodically fetch current Parks on the Air (POTA) activations from `api.pota.app` and display them as spots on your panadapter. Use this to find active park operators without running a separate application.

## Before you start

- AetherSDR must be running. A radio connection is not required to configure POTA polling.
- Your machine must have outbound HTTP access to `api.pota.app`.
- Confirm that the spot overlay is enabled (`IsSpotsEnabled` set to Enabled) so spots appear on the panadapter.

## Steps

1. Open `Settings > SpotHub...`.
2. Click the **POTA** tab.
3. Review the **Server:** indicator — it shows `api.pota.app (HTTP polling)` and is not editable.
4. Set **Poll Interval:** to the number of seconds between polls. This value is saved as `PotaPollInterval`.
5. Click **Start**. The status indicator changes to **Polling**.
6. Watch the **POTA Activations** console for incoming activation data.
7. To change the color of POTA spots on the panadapter, click **Spot Color:** and choose a color. The choice is saved as `PotaSpotColor`.
8. To have polling start automatically every time AetherSDR launches, click **Auto-start on startup** so it is active. This is saved as `PotaAutoStart`.
9. To stop polling, click **Stop**.

## What each control does

| Control | Description | Default | Setting key |
|---|---|---|---|
| **Server:** | Read-only indicator showing the fixed POTA endpoint. | `api.pota.app (HTTP polling)` | — |
| **Poll Interval:** | Seconds between successive polls of the POTA API. | — | `PotaPollInterval` |
| **Start / Stop** | Starts or stops POTA polling. Status changes between **Polling** and **Stopped**. | — | — |
| **Auto-start on startup** | Automatically starts polling when AetherSDR launches. | — | `PotaAutoStart` |
| **POTA Activations** | Read-only console showing the raw activation feed received from the API. | — | — |
| **Spot Color:** | Opens a color picker to set the panadapter spot color for POTA spots. | — | `PotaSpotColor` |

## Tips

- The **POTA Activations** console loads the last 500 lines from the session log when the SpotHub dialog opens, so recent activations are visible immediately without waiting for the next poll.
- Double-click any POTA spot in the **Spot List** tab to tune directly to that activation's frequency.

## Troubleshooting

- **Status stays Stopped after clicking Start** — Check that your machine has a working internet connection and that outbound HTTP to `api.pota.app` is not blocked by a firewall.
- **No spots appear on the panadapter** — Confirm the master spot overlay is enabled: open the **Display** tab in SpotHub and verify **Spots:** is set to Enabled (`IsSpotsEnabled`).

## Related

- [SpotHub overview](overview.md)
- [Tune to a spot by double-clicking the spot list](tune-to-a-spot-by-double-clicking-the-spot-list.md)
- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
- [Pick colors for each spot source](pick-colors-for-each-spot-source.md)
- [Start WSJT-X UDP listener and filter for CQ, POTA or calls to me](start-wsjt-x-udp-listener-and-filter-for-cq-pota-or-calls-to-me.md)
