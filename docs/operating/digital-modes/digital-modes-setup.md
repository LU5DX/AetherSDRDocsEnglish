# SpotHub

The **SpotHub** window is the central hub for connecting to DX spot sources — DX cluster, Reverse Beacon Network (RBN), WSJT-X, SpotCollector, POTA, and FreeDV — and configuring how spots are displayed on the panadapter.

## Opening SpotHub

Click the **SpotHub** button in the toolbar, or press `Ctrl+Shift+S`.

## SpotHub Layout

The SpotHub window contains a tabbed interface with the following tabs:

| Tab | Purpose |
|-----|---------|
| **Cluster** | DX cluster telnet connection |
| **RBN** | Reverse Beacon Network |
| **WSJT-X** | WSJT-X UDP listener |
| **SpotCollector** | Ham Radio Deluxe SpotCollector |
| **POTA** | Parks on the Air activations |
| **FreeDV** | FreeDV QSO reporter |
| **Spot List** | Unified, searchable table of live spots |
| **Display** | Panadapter spot visualization, Signal History, and DXCC coloring |

Each source tab provides connection controls, a console view, and a spot color picker. Source status indicators appear at the top of the tab: **Disconnected**, **Connected**, **Stopped**, **Listening**, or **Polling**.

## Cluster Tab

The Cluster tab connects to a traditional DX cluster via telnet.

| Control | Default | Range | Setting Key | Behavior |
|---------|---------|-------|-------------|----------|
| **Server:** | (empty) | hostname | `ClusterHost` | DX cluster hostname |
| **Port:** | 23 | 1–65535 | `ClusterPort` | Telnet port |
| **Callsign:** | (empty) | callsign | `ClusterCallsign` | Login callsign |
| **Connect / Disconnect** | Connect | — | — | Toggles telnet connection |
| **Auto-connect on startup** | off | on/off | `ClusterAutoConnect` | Auto-connects on launch |
| **Cluster Console** | (read-only) | — | — | Raw telnet traffic |
| **Send** | — | — | — | Sends command to cluster |
| **Spot Color:** | — | color | `ClusterSpotColor` | Opens color picker for spot text |

## RBN Tab

The RBN tab connects to the Reverse Beacon Network.

| Control | Default | Range | Setting Key | Behavior |
|---------|---------|-------|-------------|----------|
| **Server:** | (empty) | hostname | `RbnHost` | RBN hostname |
| **Port:** | 23 | 1–65535 | `RbnPort` | RBN telnet port |
| **Callsign:** | (empty) | callsign | `RbnCallsign` | Login callsign |
| **Rate Limit:** | 10 | 1–100 | `RbnRateLimit` | Spots per second cap |
| **Connect / Disconnect** | Connect | — | — | Toggles RBN connection |
| **Auto-connect on startup** | off | on/off | `RbnAutoConnect` | Starts automatically |
| **RBN Console** | (read-only) | — | — | Raw RBN traffic |
| **Send** | — | — | — | Sends command to RBN |
| **Spot Color:** | — | color | `RbnSpotColor` | Color picker for RBN spots |

## WSJT-X Tab

The WSJT-X tab listens for UDP broadcast messages from WSJT-X. The fill and border of the **Start/Stop** button go green when the listener is running.

| Control | Default | Range | Setting Key | Behavior |
|---------|---------|-------|-------------|----------|
| **Address:** | 127.0.0.1 | IP address | `WsjtxAddress` | UDP bind address |
| **Port:** | 2237 | 1–65535 | `WsjtxPort` | UDP port |
| **Start / Stop** | Stop | — | — | Starts/stops UDP listener |
| **Auto-start on startup** | off | on/off | `WsjtxAutoStart` | Starts listener on launch |
| **CQ** | off | on/off | `WsjtxFilterCQ` | Show only CQ calls |
| **CQ POTA** | off | on/off | `WsjtxFilterPOTA` | Show CQ POTA calls |
| **Calling Me** | off | on/off | `WsjtxFilterCallingMe` | Show only decodes addressed to your callsign |
| **CQ color** | — | color | `WsjtxColorCQ` | Color picker for CQ spots |
| **POTA color** | — | color | `WsjtxColorPOTA` | Color picker for POTA spots |
| **Calling Me color** | — | color | `WsjtxColorCallingMe` | Color picker for Calling Me spots |
| **Default color** | — | color | `WsjtxColorDefault` | Color picker for default spots |
| **WSJT-X Decodes** | (read-only) | — | — | Console of decoded transmissions |
| **Spot Life:** | 60 | 10–3600 sec | `WsjtxSpotLife` | Seconds spots remain on panadapter |

## SpotCollector Tab

Connects to Ham Radio Deluxe SpotCollector via UDP broadcast.

| Control | Default | Range | Setting Key | Behavior |
|---------|---------|-------|-------------|----------|
| **UDP Port:** | 58779 | 1–65535 | `SpotCollectorPort` | UDP port for broadcasts |
| **Start / Stop** | Stop | — | — | Starts/stops listener |
| **Auto-start on startup** | off | on/off | `SpotCollectorAutoStart` | Starts listener on launch |
| **SpotCollector Spots** | (read-only) | — | — | Console of received spots |

## POTA Tab

Polls api.pota.app for current Parks on the Air activations.

| Control | Default | Range | Setting Key | Behavior |
|---------|---------|-------|-------------|----------|
| **Server:** | api.pota.app (HTTP polling) | — | — | Fixed endpoint indicator |
| **Poll Interval:** | 60 | 10–3600 sec | `PotaPollInterval` | Seconds between polls |
| **Start / Stop** | Stop | — | — | Starts/stops polling |
| **Auto-start on startup** | off | on/off | `PotaAutoStart` | Starts polling on launch |
| **POTA Activations** | (read-only) | — | — | Console of activation feed |
| **Spot Color:** | — | color | `PotaSpotColor` | Color picker for POTA spots |

## FreeDV Tab

Connects to the FreeDV QSO reporter via WebSocket.

| Control | Default | Range | Setting Key | Behavior |
|---------|---------|-------|-------------|----------|
| **Server:** | qso.freedv.org (WebSocket) | — | — | Fixed endpoint indicator |
| **Start / Stop** | Stop | — | — | Connects/disconnects WebSocket |
| **Auto-start on startup** | off | on/off | `FreeDvAutoStart` | Starts FreeDV on launch |
| **FreeDV Spots** | (read-only) | — | — | Console of FreeDV activity |
| **Spot Color:** | — | color | `FreeDvSpotColor` | Color picker for FreeDV spots |

## Spot List Tab

A unified, searchable table of all live spots from all sources.

| Control | Behavior |
|---------|----------|
| **Bands:** | Per-band checkboxes toggle visibility in table |
| **Clear** | Empties current spot list |
| **Spot table** | Sortable table. Double-click row to tune. Columns: Time, Freq, DX Call, Comment, Spotter, Band, Mode, Source |

## Display Tab

Controls how spots appear on the panadapter. The Display tab presents controls in a single layout with a top toggle row, common slider row, and a two-column section for DXCC Coloring (left) and Signal History (right).

### Top Toggle Row

| Control | Default | Setting Key | Behavior |
|---------|---------|-------------|----------|
| **Spots:** | Enabled | `IsSpotsEnabled` | Master toggle for DX spot overlay |
| **Memories:** | Disabled | `IsMemorySpotsEnabled` | Memory-channel overlay on panadapter |
| **Auto:** | Enabled | `SpotAutoSwitchMode` | Auto-switch slice mode when clicking a spot with mode info |
| **Signals (Signal History)** | Disabled | `SHistoryMarkersEnabled` | Gold markers for detected voice-width signals |
| **QRM (Signal History)** | Disabled | `SHistoryQrmEnabled` | Red markers for persistent carriers and interference |

### Common Sliders

| Control | Default | Range | Setting Key | Behavior |
|---------|---------|-------|-------------|----------|
| **Levels:** | 3 | 1–10 | `SpotsMaxLevel` | Vertical stacking rows for spots |
| **Position:** | 50 | 0–100 | `SpotsStartingHeightPercentage` | Vertical position on panadapter |
| **Font Size:** | 16 | 8–32 | `SpotFontSize` | Spot text size |
| **Spot Lifetime:** | 300 | 10 sec – 24 hrs | `DxClusterSpotLifetimeSec` | Seconds before spot fades |

### Clear All and Action Buttons

| Control | Default | Setting Key | Behavior |
|---------|---------|-------------|----------|
| **Clear All** | — | — | Clears all DX spots, memory feed, Signal History markers, and QRM markers |
| **Override Colors:** | off | `IsSpotsOverrideColorsEnabled` | Forces single text color for all spots |
| **Spot text color picker** | #FFFF00 | `SpotsOverrideColor` | Opens color dialog |
| **Override Background: Enabled** | Enabled | `IsSpotsOverrideBackgroundColorsEnabled` | Enables custom spot background |
| **Override Background: Auto** | Enabled | `IsSpotsOverrideToAutoBackgroundColorEnabled` | Auto-picks background color for contrast |
| **Spot background color picker** | #000000 | `SpotsOverrideBgColor` | Opens color dialog |
| **Background Opacity:** | 48 | 0–100 | `SpotsBackgroundOpacity` | Opacity of spot background color |
| **Spot Lines:** | Enabled | `IsSpotsLinesEnabled` | Vertical lines from spectrum to spot labels |
| **Total Spots:** | — | — | Live count of spots across all sources |

### DXCC Coloring (Left Column)

Controls in the left column below the divider section header **DXCC Coloring**:

| Control | Default | Setting Key | Behavior |
|---------|---------|-------------|----------|
| **DXCC Colors:** | off | `IsDxccColoringEnabled` | Colors spots by worked/confirmed/needed DXCC status |
| **Log File (ADIF):** | — | `DxccAdifFilePath` | Loads ADIF log for DXCC coloring. Auto-watches file for changes |
| **Imported:** | (no log loaded) | — | Shows QSO count and entity count |
| **New DXCC** | — | `DxccColorNewEntity` | Color picker for new entity |
| **New Band** | — | `DxccColorNewBand` | Color picker for new band |
| **New Mode** | — | `DxccColorNewMode` | Color picker for new mode |
| **Worked** | — | `DxccColorWorked` | Color picker for worked entities |

### Signal History (Right Column)

Controls in the right column below the divider section header **Signal History**:

| Control | Default | Range | Setting Key | Behavior |
|---------|---------|-------|-------------|----------|
| **Marker Lifetime:** | 60 | 15–300 sec | `SHistoryLifetimeS` | How long inactive marker persists |
| **QRM Gate:** | 6 | 3–30 sec | `SHistoryQrmGateS` | Persistence before classifying as QRM |
| **Edge Threshold:** | 3.0 | 1.0–10.0 dB | `SHistorySoftEdgeDb` | Threshold for edge walk refinement |
| **Signals color** | #FFC800 | color | `SHistoryColorSignals` | Color picker for voice signal markers |
| **QRM color** | #FF0000 | color | `SHistoryColorQrm` | Color picker for QRM markers |
| **Snap to Step:** | Disabled | on/off | `SHistorySnapToStep` | Rounds click-to-tune to nearest step size |

## Signal History Markers

The Signal History system detects and displays two types of markers on the spectrum:

- **Signal markers (gold, #FFC800)** — Markers for detected voice-width signals. These appear as gold indicators on the panadapter.
- **QRM markers (red, #FF0000)** — Markers for persistent narrow carriers and wideband interference. These appear as red indicators.

Both marker types are displayed as markers on the spectrum waterfall. Clicking a marker tunes the active slice to that frequency. Double-clicking a marker opens the VFO panel for that frequency.

The **Signals (Signal History)** and **QRM (Signal History)** toggles in the Display tab share the same behavior as the **View > Signal History Markers** and **View > QRM History Markers** menu items.

When **Snap to Step** is enabled, clicking a Signal History marker rounds the tune frequency to the