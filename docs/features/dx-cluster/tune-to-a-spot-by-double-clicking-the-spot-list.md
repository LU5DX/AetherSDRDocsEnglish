# Tune to a Spot by Double-Clicking the Spot List

The Spot List tab in SpotHub shows every live spot from all active sources in a single sortable table. Double-clicking a row tunes the active VFO to that spot's frequency. Starting in v0.9.7, double-clicking also forwards the mode hint extracted from the spot comment, so the receiver switches to the correct mode (for example, CW or FT8) and does not only change frequency.

## Before you start

- At least one spot source (DX Cluster, RBN, WSJT-X, SpotCollector, POTA, or FreeDV) must be connected and receiving spots.
- The radio must be connected to AetherSDR.

## Steps

1. Open `Settings > SpotHub...`.
2. Click the "Spot List" tab.
3. Optionally, use the "Bands:" checkboxes to filter the table by band. Uncheck any bands you do not want to see.
4. Click a column header to sort the table by that column. Columns are: Time, Freq (kHz), DX Call, Mode, Comment, Spotter, Band, Source.
5. Double-click any row in the spot table. AetherSDR tunes the active VFO to the frequency shown in that row. If the spot contains a recognizable mode in its comment field, AetherSDR also switches the slice to that mode.

## What each control does

| Control | Behavior | Setting key |
|---|---|---|
| Bands: | Per-band checkboxes toggle visibility of spots in the table for each amateur band. | One checkbox per band: 160m, 80m, 60m, 40m, 30m, 20m, 17m, 15m, 12m, 10m, 6m. Each persisted as `SpotBandFilter_160m`, `SpotBandFilter_80m`, etc. Stored as `True`/`False` string. The 2m band is recognized by the underlying model (for FreeDV spots) but has no corresponding checkbox — 2m spots bypass the filter and are always visible. |
| Clear | Removes all spots currently shown in the table. | — |
| Spot table | Sortable table of spots; spots are batched and flushed to the table once per second. Double-click a row to tune to that frequency and switch to the spot's mode if one can be identified. | Columns (visual order by enum index): Time, Freq (kHz), DX Call, Comment, Spotter, Band, Mode, Source. Mode (index 6) is auto-extracted from the Comment field. Newest spot always appears at the top. Table holds at most 500 spots. The model internally recognizes the 2m band (144–148 MHz) for FreeDV spots but no filter checkbox for 2m is shown in the UI — 2m spots always appear in the table regardless of band-filter state. |
| Auto Mode: | Automatically switches the slice mode when clicking a spot that includes mode information (for example, CW, FT8, RTTY). Enabled by default. | `SpotAutoSwitchMode` |
| Enable FreeDV Reporter reporting when RADE is active | Enables station-reporting to the public FreeDV Reporter map (qso.freedv.org) whenever the RADE modem is active. Requires a valid callsign and grid square; if either field is blank or unresolvable the checkbox refuses to enable and shows a warning. | `FreeDvAutoReport` |
| Callsign: (FreeDV Reporter) | Callsign to report to the FreeDV Reporter map. Read-only when "Use radio" is checked. When "Use radio" is checked, the field updates automatically if the callsign changes in Radio Setup. | `FreeDvMyCallsign` |
| Use radio (callsign) | Pre-fills the callsign field from the radio's configured callsign and locks the field read-only. | `FreeDvUseRadioCallsign` |
| Grid Square: (FreeDV Reporter) | Maidenhead grid square to report. Read-only when "Use GPS" is checked. | `FreeDvMyGrid` |
| Use GPS (grid) | Pre-fills the grid field from the radio's GPS module and locks the field read-only. Only shown on radio models that have GPS hardware. | `FreeDvUseGpsGrid` |
| Station Msg: (FreeDV Reporter) | Optional free-text message shown beside the callsign on the public FreeDV Reporter map. | `FreeDvMyMessage` |
| Spot Lines: | Draws vertical lines from the spectrum up to each spot label. Enabled by default. Disable during contests to reduce visual clutter. | `IsSpotsLinesEnabled` |
| Total Spots: | Live readout of how many spots are currently tracked across all sources. Updated whenever spots are added or cleared. Resets to 0 when "Clear All Spots" is pressed. | — |

## Enabling FreeDV Reporter broadcasting

The "Enable FreeDV Reporter reporting when RADE is active" checkbox broadcasts your station's activity to the public community map at qso.freedv.org. Because the map is shared, AetherSDR validates your settings before enabling it:

1. Open `Settings > SpotHub...` and click the "FreeDV" tab.
2. In the "Station Reporting" group, set your callsign and grid square:
   - If "Use radio" is checked, the callsign is read from the radio. If the radio has no callsign configured, enter one manually after unchecking "Use radio".
   - If "Use GPS" is shown and checked, the grid is read from the radio's GPS module. Otherwise, type a valid Maidenhead grid square (for example, `EM72`) into the "Grid Square:" field.
3. Optionally, enter a short message in "Station Msg:" to display beside your callsign on the map.
4. Check "Enable FreeDV Reporter reporting when RADE is active".
   - If either the callsign or grid square cannot be resolved to a non-blank value, AetherSDR shows a warning dialog and leaves the checkbox unchecked. Correct the missing field and try again.
5. AetherSDR begins reporting automatically whenever the RADE modem is active.

> **Note:** This feature requires a build with `HAVE_WEBSOCKETS` enabled. On Windows, `HAVE_RADE` must also be present in the build to avoid compile errors.

## Tips

- Sort by "Freq (kHz)" to find spots near your current frequency.
- Sort by "Band" to group all spots on a given band together before double-clicking.
- Spots are added newest-first; the table holds a maximum of the most recent spots across all sources.
- Hiding bands with the "Bands:" checkboxes affects only the Spot List view, not the panadapter overlay.
- "Auto Mode:" is enabled by default. If you do not want the slice mode to change automatically when double-clicking a spot, disable it.
- "Spot Lines:" is enabled by default. Disabling it removes the vertical lines from the panadapter, which can help reduce visual clutter during contests.

## Related

- [SpotHub overview](overview.md)
- [Connect to a DX cluster](../../getting-started/setup/connect-to-a-dx-cluster.md)
- [Connect to the Reverse Beacon Network](../../getting-started/setup/connect-to-the-reverse-beacon-network.md)
- [Start WSJT-X UDP listener and filter for CQ, POTA or calls to me](start-wsjt-x-udp-listener-and-filter-for-cq-pota-or-calls-to-me.md)
- [Poll POTA activations](poll-pota-activations.md)
- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
<!-- docmesh:llm version=V0.9.7 date=2026-05-03 -->