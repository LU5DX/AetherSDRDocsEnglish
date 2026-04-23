# Poll POTA activations

AetherSDR can periodically fetch current Parks on the Air activations from `api.pota.app` and display them as spots on the panadapter. This lets you see active POTA operators without manually checking the POTA website.

## Before you start

- AetherSDR must have an active internet connection to reach `api.pota.app`.
- Spots must be enabled. Open `Settings > SpotHub...`, go to the **Display** tab, and confirm **Spots:** is set to Enabled.

## Steps

1. Open `Settings > SpotHub...`.
2. Click the **POTA** tab.
3. Review the **Server:** indicator — it shows `api.pota.app (HTTP polling)` and is fixed; no server entry is required.
4. Set **Poll Interval:** to the number of seconds between polls. This value is saved as `PotaPollInterval`.
5. Click **Start** to begin polling. The status indicator changes to **Polling**.
6. Watch the **POTA Activations** console for incoming activation data.
7. To change the color used for POTA spots on the panadapter, click **Spot Color:** to open the color picker. The chosen color is saved as `PotaSpotColor`.
8. To have POTA polling start automatically every time AetherSDR launches, enable **Auto-start on startup**. This is saved as `PotaAutoStart`.

## What each control does

| Control | Description | Persisted setting |
|---|---|---|
| **Server:** | Read-only indicator showing the fixed endpoint (`api.pota.app (HTTP polling)`). | — |
| **Poll Interval:** | Seconds between HTTP polls to the POTA API. | `PotaPollInterval` |
| **Start / Stop** | Starts or stops POTA polling. Status shows **Polling** when active, **Stopped** when inactive. | — |
| **Auto-start on startup** | Automatically starts POTA polling when AetherSDR launches. | `PotaAutoStart` |
| **POTA Activations** | Read-only console showing the raw activation feed as it arrives. | — |
| **Spot Color:** | Opens a color picker for the color used to render POTA spots on the panadapter. | `PotaSpotColor` |

## Tips

- POTA spots appear in the unified **Spot List** tab alongside spots from other sources. The **Source** column identifies them.
- Double-clicking a row in the **Spot List** tab tunes your radio to that spot's frequency. See [Tune to a spot by double-clicking the spot list](tune-to-a-spot-by-double-clicking-the-spot-list.md).
- To filter POTA CQ calls arriving via WSJT-X FT8 decodes instead of HTTP polling, see [Start WSJT-X UDP listener and filter for CQ, POTA or calls to me](start-wsjt-x-udp-listener-and-filter-for-cq-pota-or-calls-to-me.md).

## Troubleshooting

- **Status stays Stopped after clicking Start** — Confirm AetherSDR has outbound internet access to `api.pota.app` on port 443. A firewall or proxy may be blocking the connection.
- **No spots appear on the panadapter despite Polling status** — Check that the master spot overlay is enabled: **Display** tab, **Spots:** must be Enabled (`IsSpotsEnabled`). Also confirm **Spot Lifetime:** on the **Display** tab is set high enough for spots to remain visible between polls.
- **Spots appear but in the wrong color** — Click **Spot Color:** on the **POTA** tab to reassign the color. If **Override Colors:** is enabled on the **Display** tab, it overrides all per-source colors globally.

## Related

- [SpotHub overview](overview.md)
- [Tune to a spot by double-clicking the spot list](tune-to-a-spot-by-double-clicking-the-spot-list.md)
- [Start WSJT-X UDP listener and filter for CQ, POTA or calls to me](start-wsjt-x-udp-listener-and-filter-for-cq-pota-or-calls-to-me.md)
- [Pick colors for each spot source](pick-colors-for-each-spot-source.md)
- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
- [Clear all spots from the panadapter](clear-all-spots-from-the-panadapter.md)
