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

## Cluster tab controls

The following controls appear on the **Cluster** tab for DX cluster telnet connections.

| Control | Kind | Behavior |
|---|---|---|
| **Server:** | Text field | Hostname of DX cluster to connect to. Persisted as `ClusterHost`. |
| **Port:** | Spinbox | Telnet port on DX cluster. Range 1-65535. Persisted as `ClusterPort`. |
| **Callsign:** | Text field | Login callsign sent to cluster. Persisted as `ClusterCallsign`. |
| **Connect / Disconnect** | Push button | Toggles telnet connection to the cluster. |
| **Auto-connect on startup** | Toggle button | Auto-connects cluster on launch. Persisted as `ClusterAutoConnect`. |
| **Cluster Console** | Text field | Read-only telnet console of raw cluster traffic. |
| **Send** | Push button | Sends a typed command to the cluster. |
| **Spot Color:** | Push button | Opens a color picker for cluster spots. Persisted as `ClusterSpotColor`. |
| **Startup Commands…** | Push button | Opens the startup commands editor. Commands are sent automatically after every login. One command per line. Persisted as `DxClusterStartupCommands`. New in v26.5.2.1 (#2683). |

## RBN tab controls

The following controls appear on the **RBN** tab for Reverse Beacon Network telnet connections.

| Control | Kind | Behavior |
|---|---|---|
| **Server:** | Text field | RBN telnet hostname. Persisted as `RbnHost`. |
| **Port:** | Spinbox | RBN telnet port. Range 1-65535. Persisted as `RbnPort`. |
| **Callsign:** | Text field | Login callsign to RBN. Persisted as `RbnCallsign`. |
| **Rate Limit:** | Spinbox | Caps RBN spots per second. Persisted as `RbnRateLimit`. |
| **Connect / Disconnect (RBN)** | Push button | Toggles RBN connection. |
| **Auto-connect on startup (RBN)** | Toggle button | Starts RBN automatically. Persisted as `RbnAutoConnect`. |
| **RBN Console** | Text field | Read-only console of RBN traffic. |
| **Send (RBN)** | Push button | Sends command to RBN. |
| **Spot Color: (RBN)** | Push button | Color picker for RBN spots. Persisted as `RbnSpotColor`. |
| **Startup Commands…** | Push button | Opens the startup commands editor for the RBN instance. Commands are sent automatically after every login. One command per line. Persisted as `RbnStartupCommands`. New in v26.5.2.1 (#2683). |

## WSJT-X tab controls

The following controls appear on the **WSJT-X** tab for UDP message listening.

| Control | Kind | Behavior |
|---|---|---|
| **Address:** | Text field | UDP bind address for WSJT-X messages. Persisted as `WsjtxAddress`. |
| **Port:** | Spinbox | UDP port for WSJT-X. Range 1-65535. Persisted as `WsjtxPort`. |
| **Start / Stop** | Push button | Starts or stops UDP listener. |
| **Auto-start on startup (WSJT-X)** | Toggle button | Auto-starts listener on launch. Persisted as `WsjtxAutoStart`. |
| **CQ** | Checkbox | Show only CQ calls from WSJT-X. Persisted as `WsjtxFilterCQ`. |
| **CQ POTA** | Checkbox | Show CQ POTA calls. Persisted as `WsjtxFilterPOTA`. |
| **Calling Me** | Checkbox | Show only decodes addressed to your callsign. Persisted as `WsjtxFilterCallingMe`. |
| **CQ color / POTA color / Calling Me color / Default color** | Push button | Color pickers for each WSJT-X spot category. Persisted as `WsjtxColorCQ`, `WsjtxColorPOTA`, `WsjtxColorCallingMe`, `WsjtxColorDefault`. |
| **WSJT-X Decodes** | Text field | Console of decoded transmissions. |
| **Spot Life:** | Spinbox | Seconds WSJT-X spots remain on panadapter. Persisted as `WsjtxSpotLife`. |

## SpotCollector tab controls

The following controls appear on the **SpotCollector** tab for Ham Radio Deluxe SpotCollector UDP broadcasts.

| Control | Kind | Behavior |
|---|---|---|
| **UDP Port:** | Spinbox | UDP port SpotCollector broadcasts on. Range 1-65535. Persisted as `SpotCollectorPort`. |
| **Start / Stop (SpotCollector)** | Push button | Starts or stops UDP listener. |
| **Auto-start on startup (