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

| Control                   | Kind          | Behavior                                                                                 |
|---------------------------|---------------|------------------------------------------------------------------------------------------|
| **Server:**               | Indicator     | Shows the fixed polling endpoint: `api.pota.app (HTTP polling)`. Not configurable.       |
| **Poll Interval:**        | Spinbox       | Seconds between POTA API polls. Persisted as `PotaPollInterval`.                         |
| **Start / Stop**          | Push button   | Starts or stops POTA polling.                                                            |
| **Auto-start on startup** | Toggle button | Automatically starts POTA polling when AetherSDR launches. Persisted as `PotaAutoStart`. |
| **POTA Activations**      | Text field    | Read-only console showing the activation feed.                                           |
| **Spot Color:**           | Push button   | Opens a color picker for POTA spots on the panadapter. Persisted as `PotaSpotColor`.     |
## FreeDV Reporter controls (FreeDV tab)

The following controls appear in the **Station Reporting** group box on the **FreeDV** tab. They are only present in builds compiled with `HAVE_WEBSOCKETS`.

| Control | Kind | Behavior |
|---|---|---|
| **Enable FreeDV Reporter reporting when RADE is active** | Checkbox | Reports your station to the public FreeDV Reporter map at `qso.freedv.org` whenever the RADE modem is active. If either the callsign or grid square field is blank when you check this box, a warning dialog appears and the checkbox reverts to unchecked. Persisted as `FreeDvAutoReport`. On Windows, also requires a build compiled with `HAVE_RADE`. |
| **Callsign:** | Text field | Callsign sent to the FreeDV Reporter map. Becomes read-only when **Use radio** is checked. Persisted as `FreeDvMyCallsign`. |
| **Use radio** | Checkbox | Pre-fills the **Callsign:** field from the radio's configured callsign and locks the field read-only. Updates automatically if the callsign changes in Radio Setup. Persisted as `FreeDvUseRadioCallsign`. Default: enabled. |
| **Grid Square:** | Text field | Maidenhead grid square sent to the FreeDV Reporter map. Becomes read-only when **Use GPS** is checked. Persisted as `FreeDvMyGrid`. |
| **Use GPS** | Checkbox | Pre-fills the **Grid Square:** field from the radio's GPS module and locks the field read-only. Only shown on radio models that have GPS hardware. Persisted as `FreeDvUseGpsGrid`. Default: enabled. |
| **Station Msg:** | Text field | Optional free-text message shown beside your callsign on the public FreeDV Reporter map. Persisted as `FreeDvMyMessage`. |

### Enabling FreeDV Reporter reporting

Before enabling **Enable FreeDV Reporter reporting when RADE is active**, AetherSDR resolves your effective callsign and grid square in this order:

1. If **Use radio** is checked and the radio has a non-empty callsign configured, that callsign is used. Otherwise the text entered in **Callsign:** is used.
2. If **Use GPS** is shown and checked and the radio's GPS module provides a non-empty grid square, that grid is used. Otherwise the text entered in **Grid Square:** is used.

If either the resolved callsign or grid square is empty, AetherSDR displays a warning and leaves the checkbox unchecked. Fill in both fields before trying again.

## Auto Mode default change

As of v0.9.5.1, the **Auto Mode:** toggle on the **Display** tab defaults to **Enabled**. The setting is persisted as `SpotAutoSwitchMode`. If you previously left this at its default, it will now be active after a fresh installation. Existing installations retain whatever value was last saved.

## Tips

- POTA spots appear in the unified **Spot List** tab alongside spots from other sources. The **Source** column identifies them.
- Double-clicking a POTA spot row in the Spot List tunes your radio to that frequency. See [Tune to a spot by double-clicking the spot list](tune-to-a-spot-by-double-clicking-the-spot-list.md).
- If spots are not visible on the panadapter, confirm that the **Spots:** master toggle on the **Display** tab is set to **Enabled** (`IsSpotsEnabled`).

## Troubleshooting

- **Status stays at Stopped after clicking Start** — The application cannot reach `api.pota.app`. Check your internet connection and confirm no firewall or proxy is blocking outbound HTTP.
- **No spots appear on the panadapter despite Polling status** — Verify that **Spots:** on the **Display** tab is **Enabled**. Also check that the current band is not filtered out in the **Spot List** tab's **Bands:** checkboxes.
- **POTA Activations console is empty** — There may be no active POTA activations at this time, or the poll has not yet completed. Wait for the next poll interval to elapse.
- **FreeDV Reporter checkbox immediately unchecks** — Either the **Callsign:** or **Grid Square:** field is empty. Enter a valid callsign and Maidenhead grid square (or enable **Use radio** / **Use GPS** if the radio supplies them), then check the box again.

## Related

- [SpotHub overview](overview.md)
- [Tune to a spot by double-clicking the spot list](tune-to-a-spot-by-double-clicking-the-spot-list.md)
- [Pick colors for each spot source](pick-colors-for-each-spot-source.md)
- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
- [Clear all spots from the panadapter](clear-all-spots-from-the-panadapter.md)