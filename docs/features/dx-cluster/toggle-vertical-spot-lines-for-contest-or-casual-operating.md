# SpotHub

The **SpotHub** is the central hub for connecting to DX spot sources — DX cluster, Reverse Beacon Network, WSJT-X, SpotCollector, POTA and FreeDV — and configuring how spots are displayed on the panadapter.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- For each spot source, you'll need the appropriate server address, port, and login credentials (where applicable).

## Opening SpotHub

1. Click `Settings > SpotHub...`.
2. The SpotHub dialog opens with seven tabs: **Cluster**, **RBN**, **WSJT-X**, **SpotCollector**, **POTA**, **FreeDV**, **Spot List**, and **Display**.

---

## Cluster (tab)

The **Cluster** tab provides a telnet connection to a traditional DX cluster.

1. In the **Server:** field, enter the hostname of the DX cluster (e.g., `dxc.nc7j.com`).
2. In the **Port:** field, enter the telnet port (default `7300`, range 1–65535). This setting is stored in `ClusterPort`.
3. In the **Callsign:** field, enter your login callsign. This setting is stored in `ClusterCallsign`.
4. Click **Connect** to initiate the telnet connection. The button changes to **Disconnect** while connected.
5. Enable **Auto-connect on startup** to have AetherSDR automatically connect to the cluster when the application launches. This setting is stored in `ClusterAutoConnect`.
6. The **Cluster Console** shows raw telnet traffic (read-only).
7. Type a command in the text field next to **Send** and click **Send** to send it to the cluster.
8. Click **Spot Color:** to open a color picker and choose the color for spots received from this cluster. This setting is stored in `ClusterSpotColor`.

## RBN (tab)

The **RBN** tab provides a telnet connection to the Reverse Beacon Network with rate limiting.

1. In the **Server:** field, enter the RBN telnet hostname (e.g., `telnet.reversebeacon.net`).
2. In the **Port:** field, enter the RBN telnet port (e.g., `7000`, range 1–65535). This setting is stored in `RbnPort`.
3. In the **Callsign:** field, enter your login callsign. This setting is stored in `RbnCallsign`.
4. In the **Rate Limit:** field, set the maximum number of RBN spots per second. This setting is stored in `RbnRateLimit`.
5. Click **Connect** to initiate the RBN telnet connection. The button changes to **Disconnect** while connected.
6. Enable **Auto-connect on startup** to have AetherSDR automatically connect to RBN on launch. This setting is stored in `RbnAutoConnect`.
7. The **RBN Console** shows raw RBN traffic (read-only).
8. Type a command and click **Send** to send it to RBN.
9. Click **Spot Color:** to open a color picker for RBN spots. This setting is stored in `RbnSpotColor`.

## WSJT-X (tab)

The **WSJT-X** tab listens for UDP decodes from WSJT-X.

1. In the **Address:** field, enter the UDP bind address for WSJT-X messages. This setting is stored in `WsjtxAddress`.
2. In the **Port:** field, enter the UDP port (range 1–65535). This setting is stored in `WsjtxPort`.
3. Click **Start** to begin listening for WSJT-X UDP messages. The button changes to **Stop** while listening.
4. Enable **Auto-start on startup** to have the listener start automatically on launch. This setting is stored in `WsjtxAutoStart`.
5. Use the **CQ** checkbox to show only CQ calls from WSJT-X. This setting is stored in `WsjtxFilterCQ`.
6. Use the **CQ POTA** checkbox to show only CQ POTA calls. This setting is stored in `WsjtxFilterPOTA`.
7. Use the **Calling Me** checkbox to show only decodes addressed to your callsign. This setting is stored in `WsjtxFilterCallingMe`.
8. Click the color buttons to set colors for each category: **CQ color**, **POTA color**, **Calling Me color**, and **Default color**. These are stored in `WsjtxColorCQ`, `WsjtxColorPOTA`, `WsjtxColorCallingMe`, and `WsjtxColorDefault`.
9. The **WSJT-X Decodes** console shows decoded transmissions (read-only).
10. Use **Spot Life:** to set how many seconds WSJT-X spots remain on the panadapter. This setting is stored in `WsjtxSpotLife`.

## SpotCollector (tab)

The **SpotCollector** tab listens for Ham Radio Deluxe SpotCollector UDP broadcasts.

1. In the **UDP Port:** field, enter the port SpotCollector broadcasts on (range 1–65535). This setting is stored in `SpotCollectorPort`.
2. Click **Start** to begin listening. The button changes to **Stop** while listening.
3. Enable **Auto-start on startup** to have the listener start automatically on launch. This setting is stored in `SpotCollectorAutoStart`.
4. The **SpotCollector Spots** console shows received spots (read-only).

## POTA (tab)

The **POTA** tab polls `api.pota.app` for current Parks On The Air activations.

1. The **Server:** indicator shows the fixed endpoint `api.pota.app (HTTP polling)`.
2. Set the **Poll Interval:** in seconds between POTA polls. This setting is stored in `PotaPollInterval`.
3. Click **Start** to begin polling. The button changes to **Stop** while polling.
4. Enable **Auto-start on startup** to have polling start automatically on launch. This setting is stored in `PotaAutoStart`.
5. The **POTA Activations** console shows the activation feed (read-only).
6. Click **Spot Color:** to open a color picker for POTA spots. This setting is stored in `PotaSpotColor`.

## FreeDV (tab)

The **FreeDV** tab connects via WebSocket to the FreeDV QSO reporter (build-gated by `HAVE_WEBSOCKETS`).

1. The **Server:** indicator shows the fixed endpoint `qso.freedv.org (WebSocket)`.
2. Click **Start** to connect the WebSocket. The button changes to **Stop** while connected.
3. Enable **Auto-start on startup** to have the connection start automatically on launch. This setting is stored in `FreeDvAutoStart`.
4. The **FreeDV Spots** console shows FreeDV activity (read-only).
5. Click **Spot Color:** to open a color picker for FreeDV spots. This setting is stored in `FreeDvSpotColor`.

## Spot List (tab)

The **Spot List** tab provides a unified searchable table of all live spots from all sources.

1. Use the **Bands:** checkboxes to toggle visibility of spots per band (160m, 80m, 60m, 40m, 30m, 20m, 17m, 15m, 12m, 10m, 6m, 2m, etc.).
2. Click **Clear** to empty the current spot list.
3. The **Spot table** shows spots with columns: **Time**, **Freq**, **DX Call**, **Comment**, **Spotter**, **Band**, **Mode**, **Source**. Double-click a row to tune the radio to that frequency.

## Display (tab)

The **Display** tab controls panadapter spot visualization, DXCC coloring, and Signal History tunables. The tab is organized as follows:

### Top toggle row

| Control | Default | Behavior | Setting key |
|---------|---------|----------|-------------|
| **Spots:** | Enabled | Master toggle for DX spot overlay. The button shows **Enabled** when active and **Disabled** when inactive. | `IsSpotsEnabled` |
| **Memories:** | Disabled | Toggles memory-channel overlay on panadapter. The button shows **Enabled** when active and **Disabled** when inactive. | `IsMemorySpotsEnabled` |
| **Auto:** | Enabled | Automatically switch slice mode when clicking a spot that includes mode info (e.g. CW, FT8, RTTY) | `SpotAutoSwitchMode` |
| **Signals (Signal History)** | Disabled | Gold markers for detected voice-width signals on the panadapter | `SHistoryMarkersEnabled` |
| **QRM (Signal History)** | Disabled | Red markers for persistent carriers and wideband interference | `SHistoryQrmEnabled` |
| **Clear All** | — | Clears all DX spots, memory feed, Signal History markers and QRM markers from the spectrum | (no key) |

### Common sliders

| Control | Default | Range | Behavior | Setting key |
|---------|---------|-------|----------|-------------|
| **Levels:** | 3 | 1–10 | Number of vertical stacking rows for spots | `SpotsMaxLevel` |
| **Position:** | 50 | 0–100 | Vertical position on panadapter | `SpotsStartingHeightPercentage` |
| **Font Size:** | 16 | 8–32 | Spot text size | `SpotFontSize` |
| **Spot Lifetime:** | Varies | 10 sec – 24 hrs (non-linear steps) | Seconds before a spot fades away | `DxClusterSpotLifetimeSec` |

### Override Colors section

| Control | Default | Behavior | Setting key |
|---------|---------|----------|-------------|
| **Override Colors:** | Disabled | Forces a single text color for all spots. The button shows **Enabled** when active and **Disabled** when inactive. | `IsSpotsOverrideColorsEnabled` |
| **Spot text color picker** | #FFFF00 | Opens QColorDialog to pick spot text color | `SpotsOverrideColor` |
| **Override Background:** | Enabled | Enables custom spot background color. The button shows **Enabled** when active and **Disabled** when inactive. | `IsSpotsOverrideBackgroundColorsEnabled` |
| **Override Background: Auto** | Enabled | Auto-picks background color for contrast. The button shows **Auto** when active. | `IsSpotsOverrideToAutoBackgroundColorEnabled` |
| **Spot background color picker** | #000000 | Opens QColorDialog for spot background color | `SpotsOverrideBgColor` |
| **Background Opacity:** | 48 | 0–100 | Opacity of spot background color | `SpotsBackgroundOpacity` |
| **Spot Lines:** | Enabled | Draws vertical lines from the spectrum up to each spot label. Disable during contests to reduce visual clutter. The button shows **Enabled** when active and **Disabled** when inactive. | `IsSpotsLinesEnabled` |
| **Clear All Spots** | — | Clears all spots from the panadapter | (no key) |
| **Total Spots:** | — | Live count of spots currently tracked across all sources | (indicator) |

### DXCC Coloring (section)

The left column below the divider contains DXCC coloring controls.

| Control | Default | Behavior | Setting key |
|---------|---------|----------|-------------|
| **DXCC Colors:** | Disabled | Colors spots by worked/confirmed/needed DXCC status. The button shows **Enabled** when active and **Disabled** when inactive. | `IsDxccColoringEnabled` |
| **Log File (ADIF):** | — | Loads an ADIF log file to drive DXCC coloring. Auto-watches the file for changes after selection. | `DxccAdifFilePath` |
| **Imported: (DXCC stats)** | (no log loaded) | Shows QSO count and entity count when a log is loaded. Format: `<N> QSOs / <M> entities` | (indicator) |
| **DXCC Color swatches (New DXCC / New Band / New Mode / Worked)** | — | Opens a color picker for each DXCC status category | `DxccColorNewEntity`, `DxccColorNewBand`, `DxccColorNewMode`, `DxccColorWorked` |

### Signal History (section)

The right column below the divider contains Signal History tunables.

| Control | Default | Range | Behavior | Setting key |
|---------|---------|-------|----------|-------------|
| **Marker Lifetime:** | 60 | 15–300 sec | How long an inactive Signal History marker persists before being removed | `SHistoryLifetimeS` |
| **QRM Gate:** | 6 | 3–30 sec | How long a narrow carrier or wideband signal must persist before being classified as QRM | `SHistoryQrmGateS` |
| **Edge Threshold:** | 3.0 | 1.0–10.0 dB | Threshold above noise floor for the slope edge walk that refines the S-History carrier-side edge | `SHistorySoftEdgeDb` |
| **Signal History color swatches (Signals / QRM)** | #FFC800 / #FF0000 | — | Opens a color picker for the voice signal markers (gold) and QRM markers (red) | `SHistoryColorSignals`, `SHistoryColorQrm` |
| **Snap to Step:** | Disabled | — | Rounds S-History click-to-tune to the nearest multiple of the active slice's step size, hiding the small carrier offset. The button shows **Enabled** when active and **Disabled** when inactive. | `SHistorySnapToStep` |

---

## Toggle vertical spot lines