# Tune to a Spot by Double-Clicking the Spot List

The Spot List tab in SpotHub shows every live spot from all active sources in a single sortable table. Double-clicking a row tunes the active VFO to that spot's frequency. Starting in v0.9.7, double-clicking also forwards the mode hint extracted from the spot comment, so the receiver switches to the correct mode (for example, CW or FT8) and does not only change frequency.

## Before you start

- At least one spot source (DX Cluster, RBN, WSJT-X, SpotCollector, POTA, or FreeDV) must be connected and receiving spots.
- The radio must be connected to AetherSDR.

## Steps

1. Open `Settings > SpotHub...`.
2. Click the "Spot List" tab.
3. Optionally, use the "Bands:" checkboxes to filter the table by band. Uncheck any bands you do not want to see. The band checkboxes use a flow layout that wraps to a new row when horizontal space is limited, keeping the labels readable.
4. Click a column header to sort the table by that column. Columns are: Time, Freq (kHz), DX Call, Mode, Comment, Spotter, Band, Source. Clicking the Time header sorts by time.
5. Right-click any column header to open the column visibility menu. Toggle checkable actions in the menu to show or hide columns. The menu stays open while toggling, so you can adjust several columns in one pass.
6. Double-click any row in the spot table. AetherSDR tunes the active VFO to the frequency shown in that row. If the spot contains a recognizable mode in its comment field, AetherSDR also switches the slice to that mode.

## What each control does

### Cluster tab

| Control                    | Behavior                                                                                                                                                  | Setting key             |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| Server:                    | Hostname of DX cluster to connect to.                                                                                                                     | `ClusterHost`           |
| Port:                      | Telnet port on DX cluster. Range: 1–65535.                                                                                                                 | `ClusterPort`           |
| Callsign:                  | Login callsign sent to cluster.                                                                                                                           | `ClusterCallsign`       |
| Connect / Disconnect       | Toggles telnet connection to the cluster.                                                                                                                  | —                       |
| Auto-connect on startup    | Auto-connects cluster on launch.                                                                                                                          | `ClusterAutoConnect`    |
| Cluster Console            | Read-only telnet console of raw cluster traffic.                                                                                                           | —                       |
| Send                       | Sends a typed command to the cluster.                                                                                                                     | —                       |
| Spot Color:                | Opens a color picker for cluster spots.                                                                                                                   | `ClusterSpotColor`      |
| Startup Commands…          | Opens the startup commands editor. Commands are sent automatically after every login. One command per line (e.g. SET/NAME, SET/QTH, ACCEPT/SPOT).          | `DxClusterStartupCommands` |

### RBN tab

| Control                       | Behavior                                                                                                          | Setting key           |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------|-----------------------|
| Server:                       | RBN telnet hostname.                                                                                              | `RbnHost`             |
| Port:                         | RBN telnet port. Range: 1–65535.                                                                                  | `RbnPort`             |
| Callsign:                     | Login callsign to RBN.                                                                                            | `RbnCallsign`         |
| Rate Limit:                   | Caps RBN spots per second.                                                                                        | `RbnRateLimit`        |
| Connect / Disconnect (RBN)    | Toggles RBN connection.                                                                                           | —                     |
| Auto-connect on startup (RBN) | Starts RBN automatically.                                                                                         | `RbnAutoConnect`      |
| RBN Console                   | Read-only console of RBN traffic.                                                                                 | —                     |
| Send (RBN)                    | Sends command to RBN.                                                                                             | —                     |
| Spot Color: (RBN)             | Color picker for RBN spots.                                                                                       | `RbnSpotColor`        |
| Startup Commands…             | Opens the startup commands editor for RBN. Commands are sent automatically after every login. One command per line. | `RbnStartupCommands`  |

### WSJT-X tab

| Control                              | Behavior                                                                                   | Setting key                 |
|--------------------------------------|--------------------------------------------------------------------------------------------|-----------------------------|
| Address:                             | UDP bind address for WSJT-X messages.                                                      | `WsjtxAddress`             |
| Port:                                | UDP port for WSJT-X. Range: 1–65535.                                                       | `WsjtxPort`                |
| Start / Stop                         | Starts or stops UDP listener.                                                              | —                           |
| Auto-start on startup (WSJT-X)       | Auto-starts listener on launch.                                                            | `WsjtxAutoStart`           |
| CQ                                   | Show only CQ calls from WSJT-X.                                                            | `WsjtxFilterCQ`            |
| CQ POTA                              | Show CQ POTA calls.                                                                        | `WsjtxFilterPOTA`          |
| Calling Me                           | Show only decodes addressed to your callsign.                                              | `WsjtxFilterCallingMe`     |
| CQ color / POTA color / Calling Me color / Default color | Color pickers for each WSJT-X spot category.                    | `WsjtxColorCQ`, `WsjtxColorPOTA`, `WsjtxColorCallingMe`, `WsjtxColorDefault` |
| WSJT-X Decodes                       | Console of decoded transmissions.                                                         | —                           |
| Spot Life:                           | Seconds WSJT-X spots remain on panadapter.                                                 | `WsjtxSpotLife`            |

### SpotCollector tab

| Control                              | Behavior                                                    | Setting key                 |
|--------------------------------------|-------------------------------------------------------------|-----------------------------|
| UDP Port:                            | UDP port SpotCollector broadcasts on. Range: 1–65535.       | `SpotCollectorPort`         |
| Start / Stop (SpotCollector)         | Starts or stops UDP listener.                               | —                           |
| Auto-start on startup (SpotCollector)| Auto-starts listener on launch.                             | `SpotCollectorAutoStart`    |
| SpotCollector Spots                  | Console of received SpotCollector spots.                    | —                           |

### POTA tab

| Control                        | Behavior                                              | Setting key           |
|--------------------------------|-------------------------------------------------------|-----------------------|
| Server:                        | Shows fixed POTA endpoint: api.pota.app (HTTP polling).| —                     |
| Poll Interval:                 | Seconds between POTA polls.                            | `PotaPollInterval`    |
| Start / Stop (POTA)            | Starts or stops POTA polling.                          | —                     |
| Auto-start on startup (POTA)   | Auto-starts POTA on launch.                            | `PotaAutoStart`       |
| POTA Activations               | Console of activation feed.                            | —                     |
| Spot Color: (POTA)             | Color picker for POTA spots.                           | `PotaSpotColor`       |

### FreeDV tab

| Control                          | Behavior                                                    | Setting key             |
|----------------------------------|-------------------------------------------------------------|-------------------------|
| Server:                          | Shows fixed FreeDV endpoint: qso.freedv.org (WebSocket).     | —                       |
| Start / Stop (FreeDV)            | Connects or disconnects the FreeDV WebSocket.                | —                       |
| Auto-start on startup (FreeDV)   | Auto-starts FreeDV on launch.                                | `FreeDvAutoStart`       |
| FreeDV Spots                     | Console of FreeDV activity.                                  | —                       |
| Spot Color: (FreeDV)             | Color picker for FreeDV spots.                               | `FreeDvSpotColor`       |

### Spot List tab

| Control          | Behavior                                                                                                                                                                                                                                                                                             | Setting key     |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| Bands:           | Per-band checkboxes toggle visibility of spots in the table for each amateur band. The checkboxes use a flow layout that wraps to a new row when horizontal space is limited (#4157).                                                                                                                | One checkbox per band: 160m, 80m, 60m, 40m, 30m, 20m, 17m, 15m, 12m, 10m, 6m. Each persisted as `SpotBandFilter_160m`, `SpotBandFilter_80m`, etc. Stored as `True`/`False` string. The 2m band is recognized by the underlying model (for FreeDV spots) but has no corresponding checkbox — 2m spots bypass the filter and are always visible. |
| Clear            | Removes all spots currently shown in the table.                                                                                                                                                                                                                                                      | —               |
| Spot table       | Sortable table of spots; spots are batched and flushed to the table once per second. Double-click a row to tune to that frequency and switch to the spot's mode if one can be identified. Right-click any column header to open the column visibility menu — the menu stays open while toggling so you can show or hide several columns in one pass (#4157). | Columns (visual order by enum index): Time, Freq (kHz), DX Call, Comment, Spotter, Band, Mode, Source. Mode (index 6) is auto-extracted from the Comment field. Newest spot always appears at the top. Table holds at most 500 spots. The model internally recognizes the 2m band (144–148 MHz) for FreeDV spots but no filter checkbox for 2m is shown in the UI — 2m spots always appear in the table regardless of band-filter state. |

### Display tab

| Control                                                  | Behavior                                                                                                                                                                                                                                                | Setting key                                                                                                                                                                   |
|----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Spots:                                                   | Master toggle for DX spot overlay on the panadapter.                                                                                                                                                                                                    | `IsSpotsEnabled`                                                                                                                                                              |
| Memories:                                                | Toggles memory-channel overlay on the panadapter.                                                                                                                                                                                                       | `IsMemorySpotsEnabled`                                                                                                                                                        |
| Auto:                                                    | Automatically switch slice mode when clicking a spot that includes mode info (e.g. CW, FT8, RTTY).                                                                                                                                                      | Setting key changed from `SpotsAutoMode` to `SpotAutoSwitchMode` in v26.5.1.                                                                                                  |
| Signals (Signal History)                                 | Gold markers for detected voice-width signals on the panadapter.                                                                                                                                                                                        | New in v26.5.1 (#2426). Setting key: `SHistoryMarkersEnabled`. Same toggle as View > Signal History Markers.                                                                  |
| QRM (Signal History)                                     | Red markers for persistent carriers and wideband interference.                                                                                                                                                                                          | New in v26.5.1 (#2426). Setting key: `SHistoryQrmEnabled`. Same toggle as View > QRM History Markers.                                                                         |
| Clear All                                                | Clears all DX spots, memory feed, Signal History markers and QRM markers from the spectrum.                                                                                                                                                             | —                                                                                                                                                                             |
| Levels:                                                  | Number of vertical stacking rows for spots.                                                                                                                                                                                                             | Setting key migrated from `SpotsStackLevels` in v0.9.7 to `SpotsMaxLevel`.                                                                                                    |
| Position:                                                | Vertical position on panadapter.                                                                                                                                                                                                                        | Setting key migrated from `SpotsPosition` in v0.9.7 to `SpotsStartingHeightPercentage`.                                                                                       |
| Font Size:                                               | Spot text size.                                                                                                                                                                                                                                         | Setting key migrated from `SpotsFontSize` in v0.9.7 to `SpotFontSize`.                                                                                                        |
| Spot Lifetime:                                           | Seconds before a spot fades away.                                                                                                                                                                                                                       | Setting key migrated from `SpotsLifetime` in v0.9.7 to `DxClusterSpotLifetimeSec`. Migrates old minutes-based `DxClusterSpotLifetime` key on first read.                      |
| Override Colors:                                         | Forces a single text color for all spots. Toggle button always shows "Enabled" regardless of state.                                                                                                                                                     | `IsSpotsOverrideColorsEnabled`                                                                                                                                                |
| Spot text color picker                                   | Opens QColorDialog to pick spot text color.                                                                                                                                                                                                             | `SpotsOverrideColor`                                                                                                                                                          |
| Override Background: Enabled                             | Enables custom spot background color.                                                                                                                                                                                                                   | `IsSpotsOverrideBackgroundColorsEnabled`                                                                                                                                      |
| Override Background: Auto                                | Auto-picks background color for contrast.                                                                                                                                                                                                               | `IsSpotsOverrideToAutoBackgroundColorEnabled`                                                                                                                                 |
| Spot background color picker                             | Opens QColorDialog for spot background color.                                                                                                                                                                                                           | `SpotsOverrideBgColor`                                                                                                                                                        |
| Background Opacity:                                      | Opacity of spot background color.                                                                                                                                                                                                                       | Setting key migrated from `SpotsOverrideBgOpacity` in v0.9.7 to `SpotsBackgroundOpacity`.                                                                                     |
| Spot Lines:                                              | Draws vertical lines from the spectrum up to each spot label. Toggle button always shows "Enabled" regardless of state. Disable during contests to reduce visual clutter.                                                                                | `IsSpotsLinesEnabled`                                                                                                                                                         |
| Total Spots:                                             | Live readout of how many spots are currently tracked across all sources. Updated whenever spots are added or cleared. Resets to 0 when "Clear All Spots" is pressed.                                                                                    | —                                                                                                                                                                             |
| DXCC Colors:                                             | Colors spots by worked/confirmed/needed DXCC status. Toggle button always shows "Enabled" regardless of state.                                                                                                                                          | Setting key changed from `DxccColoringEnabled` to `IsDx