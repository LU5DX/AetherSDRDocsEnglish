# SpotHub (DX Cluster Dialog)

AetherSDR can connect to multiple DX spot sources—DX cluster telnet, Reverse Beacon Network (RBN), WSJT-X, SpotCollector, POTA, and FreeDV—and display spots on your panadapter. The unified SpotHub dialog centralizes all connection, filter, color, and display settings.

## Before you start

- AetherSDR must be running. A radio connection is not required to configure spot sources.
- For DX cluster and RBN connections, outbound telnet access to the respective servers must not be blocked by a firewall.
- For WSJT-X, SpotCollector, and FreeDV, the respective applications must be running and configured to broadcast on the expected ports or WebSocket endpoint.
- For POTA, outbound HTTP access to `api.pota.app` must not be blocked by a firewall.

## Opening SpotHub

1. Click `Settings > SpotHub...` to open the **SpotHub** dialog.

The dialog is organized into tabs for each spot source, plus a unified **Spot List** tab and a **Display** tab for panadapter visualization settings.

## Poll POTA activations

This section describes how to configure the **POTA** tab to periodically fetch current Parks on the Air activations from `api.pota.app` and display them as spots on your panadapter.

### Steps

1. Click `Settings > SpotHub...` to open the SpotHub dialog.
2. Click the **POTA** tab.
3. Review the **Server:** indicator, which shows `api.pota.app (HTTP polling)`. This endpoint is fixed and cannot be changed.
4. Set **Poll Interval:** to the number of seconds between each poll. This value is persisted as `PotaPollInterval`.
5. Click **Start** to begin polling. The status indicator changes to **Polling** when active. Click **Stop** to halt polling at any time.
6. To change the color used for POTA spots on the panadapter, click **Spot Color:**. Select a color from the picker. This is persisted as `PotaSpotColor`.
7. To start polling automatically each time AetherSDR launches, click **Auto-start on startup** so it is active. This is persisted as `PotaAutoStart`.
8. Monitor incoming activations in the **POTA Activations** console on the same tab.

### POTA tab controls

| Control | Kind | Behavior |
|---|---|---|
| **Server:** | Indicator | Shows the fixed polling endpoint: `api.pota.app (HTTP polling)`. Not configurable. |
| **Poll Interval:** | Spinbox | Seconds between POTA API polls. Persisted as `PotaPollInterval`. |
| **Start / Stop** | Push button | Starts or stops POTA polling. |
| **Auto-start on startup** | Toggle button | Automatically starts POTA polling when AetherSDR launches. Persisted as `PotaAutoStart`. |
| **POTA Activations** | Text field | Read-only console showing the activation feed. |
| **Spot Color:** | Push button | Opens a color picker for POTA spots on the panadapter. Persisted as `PotaSpotColor`. |

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

The following controls appear on the **SpotCollector** tab for Ham Radio Deluxe SpotCollector UDP broadcast listening.

| Control | Kind | Behavior |
|---|---|---|
| **UDP Port:** | Spinbox | UDP port SpotCollector broadcasts on. Range 1-65535. Persisted as `SpotCollectorPort`. |
| **Start / Stop** | Push button | Starts or stops UDP listener. |
| **Auto-start on startup** | Toggle button | Auto-starts listener on launch. Persisted as `SpotCollectorAutoStart`. |
| **SpotCollector Spots** | Text field | Read-only console of received SpotCollector spots. |

## FreeDV tab controls

The following controls appear on the **FreeDV** tab for WebSocket feed of FreeDV QSO reporter spots. This tab is only available when AetherSDR is built with WebSocket support.

| Control | Kind | Behavior |
|---|---|---|
| **Server:** | Indicator | Shows the fixed WebSocket endpoint: `qso.freedv.org (WebSocket)`. Not configurable. |
| **Start / Stop** | Push button | Connects or disconnects the FreeDV WebSocket. |
| **Auto-start on startup** | Toggle button | Auto-starts FreeDV on launch. Persisted as `FreeDvAutoStart`. |
| **FreeDV Spots** | Text field | Read-only console of FreeDV activity. |
| **Spot Color:** | Push button | Opens a color picker for FreeDV spots. Persisted as `FreeDvSpotColor`. |

## Spot List tab

The **Spot List** tab displays a unified, searchable table of all live spots from all connected sources.

| Control | Kind | Behavior |
|---|---|---|
| **Bands:** | Checkbox group | Per-band checkboxes toggle visibility in the table. One checkbox per band (160m, 80m, 60m, 40m, 30m, 20m, 17m, 15m, 12m, 10m, 6m, 2m, etc.). Checkboxes use a flow layout that wraps to a new row when horizontal space is low, keeping labels readable. |
| **Clear** | Push button | Empties the current spot list. |
| **Spot table** | List / Table | Sortable table of spots. Double-click a row to tune the radio to that frequency. Columns: Time, Freq, DX Call, Comment, Spotter, Band, Mode, Source. Column visibility can be toggled via a right-click context menu on the table header; the menu stays open while multiple columns are toggled, allowing several columns to be shown or hidden in one pass. Both the **Time** and **Freq** columns are sortable; click either column header to re-sort the table. |

## Display tab

The **Display** tab controls how spots are visualized on the panadapter, including Signal History tunables and DXCC coloring. In v26.5.1, the tab was reorganized to have a top toggle row, common sliders, then a two-column section with DXCC Coloring (left) and Signal History (right).

### Display tab controls

| Control | Kind | Behavior |
|---|---|---|
| **Spots:** | Toggle button | Master toggle for DX spot overlay. Persisted as `IsSpotsEnabled`. |
| **Memories:** | Toggle button | Toggles memory-channel overlay on panadapter. Persisted as `IsMemorySpotsEnabled`. |
| **Auto:** | Toggle button | Automatically switch slice mode when clicking a spot that includes mode info (e.g. CW, FT8, RTTY). Persisted as `SpotAutoSwitchMode`. |
| **Signals (Signal History)** | Toggle button | Gold markers for detected voice-width signals on the panadapter. Persisted as `SHistoryMarkersEnabled`. Same toggle as View > Signal History Markers. |
| **QRM (Signal History)** | Toggle button | Red markers for persistent carriers and wideband interference. Persisted as `SHistoryQrmEnabled`. Same toggle as View > QRM History Markers. |
| **Clear All** | Push button | Clears all DX spots, memory feed, Signal History markers and QRM markers from the spectrum. |
| **Levels:** | Slider | Number of vertical stacking rows for spots. Range 1-10. Default 3. Persisted as `SpotsMaxLevel`. |
| **Position:** | Slider | Vertical position on panadapter. Range 0-100. Default 50. Persisted as `SpotsStartingHeightPercentage`. |
| **Font Size:** | Slider | Spot text size. Range 8-32. Default 16. Persisted as `SpotFontSize`. |
| **Spot Lifetime:** | Slider | Seconds before a spot fades away. Non-linear steps from 10 sec to 24 hrs. Persisted as `DxClusterSpotLifetimeSec`. |
| **Override Colors:** | Toggle button | Forces a single text color for all spots. Persisted as `IsSpotsOverrideColorsEnabled`. |
| Spot text color picker | Push button | Opens QColorDialog to pick spot text color. Default #FFFF00. Persisted as `SpotsOverrideColor`. |
| **Override Background: Enabled** | Toggle button | Enables custom spot background color. Persisted as `IsSpotsOverrideBackgroundColorsEnabled`. |
| **Override Background: Auto** | Toggle button | Auto-picks background color for contrast. Persisted as `IsSpotsOverrideToAutoBackgroundColorEnabled`. |
| Spot background color picker | Push button | Opens QColorDialog for spot background color. Default #000000. Persisted as `SpotsOverrideBgColor`. |
| **Background Opacity:** | Slider | Opacity of spot background color. Range 0-100. Default 48. Persisted as `SpotsBackgroundOpacity`. |
| **Spot Lines:** | Toggle button | Draws vertical lines from the spectrum up to each spot label. Disable during contests to reduce visual clutter. Persisted as `IsSpotsLinesEnabled`. |
| **Total Spots:** | Indicator | Live count of spots currently tracked across all sources. |
| DXCC Coloring (section) | Indicator | Section header for DXCC coloring controls in the left column below the divider. |
| **DXCC Colors:** | Toggle button | Colors spots by worked/confirmed/needed DXCC status. Persisted as `IsDxccColoringEnabled`. |
| **Log File (ADIF):** | Push button | Loads an ADIF log file to drive DXCC coloring. Auto-watches the file for changes after selection. Persisted as `DxccAdifFilePath`. |
| **Imported:** (DXCC stats) | Indicator | Shows QSO count and entity count when a log is loaded. Format: