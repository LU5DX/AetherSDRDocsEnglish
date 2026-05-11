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

| Control                                                       | Kind                                                                                                                     | Behavior                                                                                                                                                                               |
|---------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Server:**                                                   | Indicator                                                                                                                | Shows the fixed polling endpoint: `api.pota.app (HTTP polling)`. Not configurable.                                                                                                     |
| **Poll Interval:**                                            | Spinbox                                                                                                                  | Seconds between POTA API polls. Persisted as `PotaPollInterval`.                                                                                                                       |
| **Start / Stop**                                              | Push button                                                                                                              | Starts or stops POTA polling.                                                                                                                                                          |
| **Auto-start on startup**                                     | Toggle button                                                                                                            | Automatically starts POTA polling when AetherSDR launches. Persisted as `PotaAutoStart`.                                                                                               |
| **POTA Activations**                                          | Text field                                                                                                               | Read-only console showing the activation feed.                                                                                                                                         |
| **Spot Color:**                                               | Push button                                                                                                              | Opens a color picker for POTA spots on the panadapter. Persisted as `PotaSpotColor`.                                                                                                   |
| Total Spots:                                                  | Indicator                                                                                                                | Live readout of how many spots are currently tracked across all sources. Updated whenever spots are added or cleared. Resets to 0 when **Clear All Spots** is pressed.                 |
| **Spot Lines:**                                               | Toggle button                                                                                                            | Draws vertical lines from the spectrum up to each spot label. Enabled by default. Disable during contests to reduce visual clutter. Persisted as `IsSpotsLinesEnabled`. New in v0.9.7. |
| Auto:                                                         | Toggle button                                                                                                            | Automatically switch slice mode when clicking a spot that includes mode info (e.g. CW, FT8, RTTY). Persisted as `SpotAutoSwitchMode`. Setting key changed from `SpotsAutoMode` in v26.5.1. |
| Signals (Signal History)                                      | Toggle button                                                                                                            | Gold markers for detected voice-width signals on the panadapter. Persisted as `SHistoryMarkersEnabled`. New in v26.5.1 (#2426). Same toggle as View > Signal History Markers. |
| QRM (Signal History)                                          | Toggle button                                                                                                            | Red markers for persistent carriers and wideband interference. Persisted as `SHistoryQrmEnabled`. New in v26.5.1 (#2426). Same toggle as View > QRM History Markers. |
| Clear All                                                     | Push button                                                                                                              | Clears all DX spots, memory feed, Signal History markers and QRM markers from the spectrum. |
| **Levels:**                                                   | Slider                                                                                                                   | Number of vertical stacking rows for spots. Range 1-10. Default 3. Persisted as `SpotsMaxLevel`. |
| **Position:**                                                 | Slider                                                                                                                   | Vertical position on panadapter. Range 0-100. Default 50. Persisted as `SpotsStartingHeightPercentage`. |
| **Font Size:**                                                | Slider                                                                                                                   | Spot text size. Range 8-32. Default 16. Persisted as `SpotFontSize`. |
| **Spot Lifetime:**                                            | Slider                                                                                                                   | Seconds before a spot fades away. Non-linear steps from 10 sec to 24 hrs. Persisted as `DxClusterSpotLifetimeSec`. |
| **Override Colors:**                                          | Toggle button                                                                                                            | Forces a single text color for all spots. Persisted as `IsSpotsOverrideColorsEnabled`. |
| Spot text color picker                                        | Push button                                                                                                              | Opens QColorDialog to pick spot text color. Default #FFFF00. Persisted as `SpotsOverrideColor`. |
| **Override Background: Enabled**                              | Toggle button                                                                                                            | Enables custom spot background color. Persisted as `IsSpotsOverrideBackgroundColorsEnabled`. |
| **Override Background: Auto**                                 | Toggle button                                                                                                            | Auto-picks background color for contrast. Persisted as `IsSpotsOverrideToAutoBackgroundColorEnabled`. |
| Spot background color picker                                  | Push button                                                                                                              | Opens QColorDialog for spot background color. Default #000000. Persisted as `SpotsOverrideBgColor`. |
| **Background Opacity:**                                       | Slider                                                                                                                   | Opacity of spot background color. Range 0-100. Default 48. Persisted as `SpotsBackgroundOpacity`. |
| DXCC Coloring (section)                                       | Indicator                                                                                                                | Section header for DXCC coloring controls in the left column below the divider. |
| **DXCC Colors:**                                              | Toggle button                                                                                                            | Colors spots by worked/confirmed/needed DXCC status. Persisted as `IsDxccColoringEnabled`. Setting key changed from `DxccColoringEnabled` in v26.5.1. |
| **Log File (ADIF):**                                          | Push button                                                                                                              | Loads an ADIF log file to drive DXCC coloring. Auto-watches the file for changes after selection. Persisted as `DxccAdifFilePath`. Setting key changed from `DxccAdifPath` in v26.5.1. Auto-Reload is always enabled when a file is selected. |
| **Imported:** (DXCC stats)                                    | Indicator                                                                                                                | Shows QSO count and entity count when a log is loaded. Format: '<N> QSOs / <M> entities'. |
| DXCC Color swatches (New DXCC / New Band / New Mode / Worked) | Push button                                                                                                              | Opens a color picker for each DXCC status category. Persisted as `DxccColorNewEntity`, `DxccColorNewBand`, `DxccColorNewMode`, `DxccColorWorked`. New in v26.5.1. |
| Signal History (section)                                      | Indicator                                                                                                                | Section header for Signal History tunables in the right column below the divider. New in v26.5.1 (#2506). |
| **Marker Lifetime:**                                          | Slider                                                                                                                   | How long an inactive Signal History marker persists before being removed. Range 15-300 sec. Default 60 s. Persisted as `SHistoryLifetimeS`. New in v26.5.1. |
| **QRM Gate:**                                                 | Slider                                                                                                                   | How long a narrow carrier or wideband signal must persist before being classified as QRM. Range 3-30 sec. Default 6 s. Persisted as `SHistoryQrmGateS`. New in v26.5.1. |
| **Edge Threshold:**                                           | Slider                                                                                                                   | Threshold above noise floor for the slope edge walk that refines the S-History carrier-side edge. Range 1.0-10.0 dB. Default 3.0 dB. Persisted as `SHistorySoftEdgeDb`. New in v26.5.1. |
| Signal History color swatches (Signals / QRM)                 | Push button                                                                                                              | Opens a color picker for the voice signal markers (gold) and QRM markers (red). Default #FFC800 / #FF0000. Persisted as `SHistoryColorSignals` / `SHistoryColorQrm`. New in v26.5.1. |
| **Snap to Step:**                                             | Toggle button                                                                                                            | Rounds S-History click-to-tune to the nearest multiple of the active slice's step size, hiding the small carrier offset. Default Disabled. Persisted as `SHistorySnapToStep`. New in v26.5.1. |

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

As of v0.9.5.1, the **Auto** toggle on the **Display** tab defaults to **Enabled**. The setting is persisted as `SpotAutoSwitchMode`. If you previously left this at its default, it will now be active after a fresh installation. Existing installations retain whatever value was last saved.

## Tune to a spot by double-clicking the spot list

As of v0.9.7, double-clicking a row in the **Spot List** tab tunes your radio to the spot frequency and also forwards a mode hint derived from the spot comment. AetherSDR will switch the active slice to CW, SSB, or the appropriate digital mode to match the spot, rather than only changing the frequency. If the spot comment contains no recognizable mode token, the slice mode is left unchanged.

## Tips

- POTA spots appear in the unified **Spot List** tab alongside spots from other sources. The **Source** column identifies them.
- Double-clicking a POTA spot row in the Spot List tunes your radio to that frequency and switches the slice mode to match the spot where possible. See [Tune to a spot by double-clicking the spot list](tune-to-a-spot-by-double-clicking-the-spot-list.md).
- If spots are not visible on the panadapter, confirm that the **Spots:** master toggle on the **Display** tab is set to **Enabled** (`IsSpotsEnabled`).
- To reduce panadapter clutter during a contest, set **Spot Lines:** to **Disabled** on the **Display** tab. This hides the vertical lines while keeping spot labels visible.

## Troubleshooting

- **Status stays at Stopped after clicking Start** — The application cannot reach `api.pota.app`. Check your internet connection and confirm no firewall or proxy is blocking outbound HTTP.
- **No spots appear on the panadapter despite Polling status** — Verify that **Spots:** on the **Display** tab is **Enabled**. Also check that the current band is not filtered out in the **Spot List** tab's **Bands:** checkboxes.
- **POTA Activations console is empty** — There may be no active POTA activations at this time, or the poll has not yet completed. Wait for the next poll interval to elapse.
- **FreeDV Reporter checkbox immediately unchecks** — Either the **Callsign:** or **Grid Square:** field is empty. Enter a valid