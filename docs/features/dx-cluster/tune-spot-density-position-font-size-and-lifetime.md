# Tune spot density, position, font size and lifetime

The Display tab in SpotHub controls how spot labels appear on the panadapter: how many stack vertically, where they sit, how large the text is, and how long each spot lives before it fades. Adjust these settings to reduce clutter on a busy band or make spots more readable on a small screen.

## Before you start

- AetherSDR must be running. A radio connection is not required to change these settings.
- At least one spot source (DX cluster, RBN, WSJT-X, SpotCollector, POTA, or FreeDV) should be active so you can see the effect of your changes in real time.
- The master spot overlay must be on. On the Display tab, confirm `IsSpotsEnabled` is active (the "Spots:" toggle reads Enabled).

## Steps
1. Open `Settings > SpotHub...`.
2. Click the **Display** tab.
3. Confirm **Spots:** is set to Enabled. If it is not, click it to enable the overlay.
4. To control how many spots stack vertically before they start overlapping, drag the **Levels:** slider. Higher values allow more rows of spot labels.
5. To move the spot labels up or down on the panadapter, drag the **Position:** slider.
6. To change the text size of spot labels, drag the **Font Size:** slider.
7. To set how long a spot remains visible before it disappears, drag the **Spot Lifetime:** slider. The value is in seconds.
8. **Auto Mode:** is enabled by default. When on, AetherSDR automatically switches the slice mode when you click a spot that carries mode information (e.g. CW, FT8, RTTY). Click **Auto Mode:** to toggle this behaviour.
9. Close the dialog. Changes take effect immediately.

## What each control does
| Control | Setting key | Behavior |
|---|---|---|
| **Spots:** | `IsSpotsEnabled` | Master toggle for the spot overlay on the panadapter. |
| **Auto Mode:** | `SpotAutoSwitchMode` | Automatically switches the slice mode when you click a spot that carries mode information (e.g. CW, FT8, RTTY). Default: Enabled. |
| **Levels:** | `SpotsMaxLevel` | Number of vertical stacking rows for spot labels. |
| **Position:** | `SpotsStartingHeightPercentage` | Vertical position of the spot label band on the panadapter. |
| **Font Size:** | `SpotFontSize` | Size of the text in each spot label. |
| **Spot Lifetime:** | `DxClusterSpotLifetimeSec` | Seconds a spot label remains visible before fading. Uses a non-linear scale (seconds → minutes → hours). |
| **Enable FreeDV Reporter reporting when RADE is active** | `FreeDvAutoReport` | Enables station-reporting to the public FreeDV Reporter map (qso.freedv.org) whenever the RADE modem is active. Requires a valid callsign and grid square or the checkbox refuses to enable. If either field is blank when you check it, a warning dialog appears and the checkbox reverts to unchecked. |
| **Callsign: (FreeDV Reporter)** | `FreeDvMyCallsign` | Callsign to report to the FreeDV Reporter map. Read-only when **Use radio (callsign)** is checked. Automatically updated when the radio's callsign changes and **Use radio** is active. |
| **Use radio (callsign)** | `FreeDvUseRadioCallsign` | Pre-fills the callsign field from the radio's configured callsign and locks the field read-only. Default: enabled. |
| **Grid Square: (FreeDV Reporter)** | `FreeDvMyGrid` | Maidenhead grid square to report. Read-only when **Use GPS (grid)** is checked. |
| **Use GPS (grid)** | `FreeDvUseGpsGrid` | Pre-fills the grid field from the radio's GPS module and locks the field read-only. Only shown on radio models that have GPS hardware. |
| **Station Msg: (FreeDV Reporter)** | `FreeDvMyMessage` | Optional free-text message shown beside the callsign on the public FreeDV Reporter map. |
| **Total Spots:** | — | Live readout of how many spots are currently tracked across all sources. Updated whenever spots are added or cleared. Resets to 0 when **Clear All Spots** is pressed. |

## FreeDV Reporter reporting

The **FreeDV (tab)** in SpotHub contains a **Station Reporting** group. When **Enable FreeDV Reporter reporting when RADE is active** is checked, AetherSDR reports your station to the public FreeDV Reporter map at qso.freedv.org whenever the RADE modem is running.

Before enabling reporting, supply both a callsign and a grid square. AetherSDR resolves these values in the following order of priority:

1. **Callsign** — if **Use radio (callsign)** is checked and the radio has a callsign configured, that value is used and the field is locked. Otherwise, type a callsign directly into the **Callsign:** field.
2. **Grid Square** — if **Use GPS (grid)** is checked and the radio has GPS hardware with a valid fix, the grid is filled automatically and locked. This checkbox only appears on radio models with GPS hardware. Otherwise, type a Maidenhead grid square (up to six characters) into the **Grid Square:** field.

If either the callsign or grid is empty when you check **Enable FreeDV Reporter reporting when RADE is active**, a warning dialog appears and the checkbox reverts to unchecked. This prevents blank or placeholder values from appearing on the community-shared public map.

Optionally, type a short message in **Station Msg:** to display alongside your callsign on the map.

The FreeDV tab is only present in builds compiled with `HAVE_WEBSOCKETS`. On Windows, the reporting checkbox additionally requires `HAVE_RADE` to be defined.

## Tips
- If spot labels overlap badly on a crowded band, increase **Levels:** to add more stacking rows, or decrease **Spot Lifetime:** so old spots clear sooner.
- **Auto Mode:** is enabled by default as of v0.9.5.1. Disable it if you want manual control over which mode is applied when clicking a spot.
- WSJT-X spots have their own per-source lifetime setting (**Spot Life:** on the WSJT-X tab, stored as `WsjtxSpotLife`). The **Spot Lifetime:** slider on the Display tab applies to all other sources.
- When **Use radio (callsign)** is active, the callsign field updates automatically if you change the callsign in Radio Setup without reopening SpotHub.

## Troubleshooting

- **Spot labels are not visible at all** — Check that **Spots:** on the Display tab is set to Enabled (`IsSpotsEnabled`). Also confirm at least one spot source is connected and receiving spots.
- **Changing Levels: has no effect** — **Auto Mode:** is likely enabled. Click **Auto Mode:** to disable it, then adjust **Levels:** manually.
- **"Enable FreeDV Reporter" checkbox keeps reverting to unchecked** — Both a callsign and a grid square must be set before enabling. Fill in the **Callsign:** and **Grid Square:** fields (or enable **Use radio** and **Use GPS** if the radio provides those values), then check the box again.
- **The FreeDV tab or the reporting checkbox is not visible** — Your build of AetherSDR was compiled without `HAVE_WEBSOCKETS` (tab not present) or without `HAVE_RADE` on Windows (checkbox not present).

## Related

- [SpotHub overview](overview.md)
- [Pick colors for each spot source](pick-colors-for-each-spot-source.md)
- [Clear all spots from the panadapter](clear-all-spots-from-the-panadapter.md)
- [Start WSJT-X UDP listener and filter for CQ, POTA or calls to me](start-wsjt-x-udp-listener-and-filter-for-cq-pota-or-calls-to-me.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-03 -->
