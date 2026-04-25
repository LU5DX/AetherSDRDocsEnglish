# Poll POTA activations

AetherSDR can periodically fetch current Parks on the Air (POTA) activations from `api.pota.app` and display them as spots on your panadapter. This lets you find active POTA operators without a separate web browser or cluster feed.

## Before you start

- AetherSDR must be running. A radio connection is not required to configure this feature.
- Outbound HTTP access to `api.pota.app` must not be blocked by a firewall.

## Steps

1. Click `Settings > SpotHub...` to open the SpotHub dialog.
2. Click the **POTA** tab.
3. Review the **Server:** indicator, which shows `api.pota.app (HTTP polling)`. This endpoint is fixed and cannot be changed.
4. Set **Poll Interval:** to the number of seconds between each poll. This value is persisted as `PotaPollInterval`.
5. Click **Start** to begin polling. The status indicator changes to **Polling** when active. Click **Stop** to halt polling at any time.
6. To change the color used for POTA spots on the panadapter, click **Spot Color:**. Select a color from the picker. This is persisted as `PotaSpotColor`.
7. To start polling automatically each time AetherSDR launches, click **Auto-start on startup** so it is active. This is persisted as `PotaAutoStart`.
8. Monitor incoming activations in the **POTA Activations** console on the same tab.

## What each control does

| Control | Kind | Behavior | Setting key |
|---|---|---|---|
| **Server:** | Indicator | Shows the fixed polling endpoint: `api.pota.app (HTTP polling)`. Not configurable. | — |
| **Poll Interval:** | Spinbox | Seconds between POTA API polls. | `PotaPollInterval` |
| **Start / Stop** | Push button | Starts or stops POTA polling. | — |
| **Auto-start on startup** | Toggle button | Automatically starts POTA polling when AetherSDR launches. | `PotaAutoStart` |
| **POTA Activations** | Text field | Read-only console showing the activation feed. | — |
| **Spot Color:** | Push button | Opens a color picker for POTA spots on the panadapter. | `PotaSpotColor` |

## Tips

- POTA spots appear in the unified **Spot List** tab alongside spots from other sources. The **Source** column identifies them.
- Double-clicking a POTA spot row in the Spot List tunes your radio to that frequency. See [Tune to a spot by double-clicking the spot list](tune-to-a-spot-by-double-clicking-the-spot-list.md).
- If spots are not visible on the panadapter, confirm that the **Spots:** master toggle on the **Display** tab is set to **Enabled** (`IsSpotsEnabled`).

## Troubleshooting

- **Status stays at Stopped after clicking Start** — The application cannot reach `api.pota.app`. Check your internet connection and confirm no firewall or proxy is blocking outbound HTTP.
- **No spots appear on the panadapter despite Polling status** — Verify that **Spots:** on the **Display** tab is **Enabled**. Also check that the current band is not filtered out in the **Spot List** tab's **Bands:** checkboxes.
- **POTA Activations console is empty** — There may be no active POTA activations at this time, or the poll has not yet completed. Wait for the next poll interval to elapse.

## Related

- [SpotHub overview](overview.md)
- [Tune to a spot by double-clicking the spot list](tune-to-a-spot-by-double-clicking-the-spot-list.md)
- [Pick colors for each spot source](pick-colors-for-each-spot-source.md)
- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
- [Clear all spots from the panadapter](clear-all-spots-from-the-panadapter.md)
