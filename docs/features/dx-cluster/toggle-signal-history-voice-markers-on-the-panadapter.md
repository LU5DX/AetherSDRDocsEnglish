# SpotHub (DX Cluster Dialog)

## Purpose

SpotHub is the central interface for connecting to DX spot sources and configuring how spots are displayed on the panadapter. It consolidates six spot sources — DX Cluster, Reverse Beacon Network (RBN), WSJT-X, SpotCollector, POTA, and FreeDV — into a single dialog with tabbed controls and a unified spot list.

## Opening SpotHub

1. Open **Settings > SpotHub...** or click the **SpotHub** button in the main toolbar.
2. The dialog has seven tabs: **Cluster**, **RBN**, **WSJT-X**, **SpotCollector**, **POTA**, **FreeDV**, **Spot List**, and **Display**.

---

## Cluster Tab

The **Cluster** tab provides a telnet connection to a traditional DX cluster.

### Connection settings

| Control | Default | Valid range | Setting key |
|---|---|---|---|
| **Server:** | (empty) | Any hostname or IP | `ClusterHost` |
| **Port:** | (empty) | 1-65535 | `ClusterPort` |
| **Callsign:** | (empty) | Any amateur callsign | `ClusterCallsign` |

### Connection controls

| Control | Behavior |
|---|---|
| **Connect / Disconnect** | Toggles the telnet connection. |
| **Auto-connect on startup** | If enabled, connects automatically when AetherSDR starts. Setting key: `ClusterAutoConnect`. |

### Console and command line

| Control | Behavior |
|---|---|
| **Cluster Console** | Read-only text area showing raw telnet traffic. |
| **Send** (push button) | Sends the typed command to the cluster. |

### Startup commands

Click **Startup Commands…** on the Cluster tab to open a dialog where you can enter one command per line (e.g. `SET/NAME`, `SET/QTH`, `ACCEPT/SPOT`). These commands are automatically sent to the cluster after every login. The commands are saved in the application settings (`DxClusterStartupCommands` for the Cluster tab, `RbnStartupCommands` for the RBN tab).

### Spot color

| Control | Behavior | Setting key |
|---|---|---|
| **Spot Color:** | Opens a color picker for cluster spots. | `ClusterSpotColor` |

---

## RBN Tab

The **RBN** tab connects to the Reverse Beacon Network via telnet with rate limiting.

### Connection settings

| Control | Default | Valid range | Setting key |
|---|---|---|---|
| **Server:** | (empty) | Any hostname or IP | `RbnHost` |
| **Port:** | (empty) | 1-65535 | `RbnPort` |
| **Callsign:** | (empty) | Any amateur callsign | `RbnCallsign` |
| **Rate Limit:** | (empty) | (unlimited by default) | `RbnRateLimit` |

### Connection controls

| Control | Behavior |
|---|---|
| **Connect / Disconnect** | Toggles the RBN connection. |
| **Auto-connect on startup** | If enabled, connects automatically on launch. Setting key: `RbnAutoConnect`. |

### Console and command line

| Control | Behavior |
|---|---|
| **RBN Console** | Read-only text area showing RBN traffic. |
| **Send** | Sends a command to RBN. |

### Spot color

| Control | Behavior | Setting key |
|---|---|---|
| **Spot Color:** | Opens a color picker for RBN spots. | `RbnSpotColor` |

---

## WSJT-X Tab

The **WSJT-X** tab listens for UDP broadcast messages from WSJT-X.

### Listener settings

| Control | Default | Valid range | Setting key |
|---|---|---|---|
| **Address:** | (empty) | Any local IP address | `WsjtxAddress` |
| **Port:** | (empty) | 1-65535 | `WsjtxPort` |

### Listener controls

| Control | Behavior |
|---|---|
| **Start / Stop** | Starts or stops the UDP listener. |
| **Auto-start on startup** | If enabled, starts the listener automatically on launch. Setting key: `WsjtxAutoStart`. |

### Filters

| Control | Behavior | Setting key |
|---|---|---|
| **CQ** | Show only CQ calls. | `WsjtxFilterCQ` |
| **CQ POTA** | Show CQ POTA calls. | `WsjtxFilterPOTA` |
| **Calling Me** | Show only decodes addressed to your callsign. | `WsjtxFilterCallingMe` |

### Spot lifetime

| Control | Default | Valid range | Setting key |
|---|---|---|---|
| **Spot Life:** | (empty) | Seconds | `WsjtxSpotLife` |

### Spot colors

| Control | Setting key |
|---|---|
| **CQ color** | `WsjtxColorCQ` |
| **POTA color** | `WsjtxColorPOTA` |
| **Calling Me color** | `WsjtxColorCallingMe` |
| **Default color** | `WsjtxColorDefault` |

### Console

| Control | Behavior |
|---|---|
| **WSJT-X Decodes** | Console of decoded transmissions. |

---

## SpotCollector Tab

The **SpotCollector** tab listens for UDP broadcasts from Ham Radio Deluxe SpotCollector.

### Listener settings

| Control | Default | Valid range | Setting key |
|---|---|---|---|
| **UDP Port:** | (empty) | 1-65535 | `SpotCollectorPort` |

### Listener controls

| Control | Behavior |
|---|---|
| **Start / Stop** | Starts or stops the UDP listener. |
| **Auto-start on startup** | If enabled, starts the listener automatically on launch. Setting key: `SpotCollectorAutoStart`. |

### Console

| Control | Behavior |
|---|---|
| **SpotCollector Spots** | Console of received SpotCollector spots. |

---

## POTA Tab

The **POTA** tab polls api.pota.app for current Parks on the Air activations.

### Polling settings

| Control | Default | Valid range | Setting key |
|---|---|---|---|
| **Server:** | api.pota.app (HTTP polling) | Fixed endpoint (indicator only) | — |
| **Poll Interval:** | (empty) | Seconds between polls | `PotaPollInterval` |

### Polling controls

| Control | Behavior |
|---|---|
| **Start / Stop** | Starts or stops POTA polling. |
| **Auto-start on startup** | If enabled, starts polling automatically on launch. Setting key: `PotaAutoStart`. |

### Console

| Control | Behavior |
|---|---|
| **POTA Activations** | Console of activation feed. |

### Spot color

| Control | Behavior | Setting key |
|---|---|---|
| **Spot Color:** | Opens a color picker for POTA spots. | `PotaSpotColor` |

---

## FreeDV Tab

The **FreeDV** tab connects to the qso.freedv.org WebSocket feed for FreeDV QSO reporter spots. This tab is only available when AetherSDR is built with WebSocket support (`HAVE_WEBSOCKETS`).

### Connection settings

| Control | Default | Setting key |
|---|---|---|
| **Server:** | qso.freedv.org (WebSocket) | Fixed endpoint (indicator only) |

### Connection controls

| Control | Behavior |
|---|---|
| **Start / Stop** | Connects or disconnects the FreeDV WebSocket. |
| **Auto-start on startup** | If enabled, connects automatically on launch. Setting key: `FreeDvAutoStart`. |

### Console

| Control | Behavior |
|---|---|
| **FreeDV Spots** | Console of FreeDV activity. |

### Spot color

| Control | Behavior | Setting key |
|---|---|---|
| **Spot Color:** | Opens a color picker for FreeDV spots. | `FreeDvSpotColor` |

---

## Spot List Tab

The **Spot List** tab shows a unified, searchable table of all live spots from all active sources.

### Band filters

| Control | Behavior |
|---|---|
| **Bands:** | Per-band checkboxes toggle visibility in the table. One checkbox per band (160m, 80m, 60m, 40m, 30m, 20m, 17m, 15m, 12m, 10m, 6m, 2m, etc.). The checkboxes use a flow layout that wraps to a new row when the dialog is too narrow for all bands on one line. |

### Table controls

| Control | Behavior |
|---|---|
| **Clear** | Empties the current spot list. |
| **Spot table** | Sortable table of spots. Double-click a row to tune your active slice to that frequency. Columns: Time, Freq, DX Call, Comment, Spotter, Band, Mode, Source. |

### Column visibility

Right-click any column header in the spot table to show or hide columns. The menu stays open while toggling multiple checkable columns, allowing you to show or hide several columns in one pass without the menu closing after each toggle.

#### Sorting

Click any column header to sort by that column. The **Time** column is sortable, so you can always return to newest-first order after sorting by other columns.

---

## Display Tab

The **Display** tab controls how spots appear on the panadapter, Signal History marker settings, and DXCC coloring.

### Master toggles

| Control | Default | Setting key |
|---|---|---|
| **Spots:** | Enabled | `IsSpotsEnabled` |
| **Memories:** | Disabled | `IsMemorySpotsEnabled` |
| **Auto:** | Enabled | `SpotAutoSwitchMode` |

- **Spots:** Master toggle for the DX spot overlay on the panadapter.
- **Memories:** Toggles memory-channel overlay on the panadapter.
- **Auto:** When enabled and a spot includes mode information (e.g. CW, FT8, RTTY), clicking the spot automatically switches the active slice to that mode.

### Signal History toggles

| Control | Default | Setting key |
|---|---|---|
| **Signals** (labeled "Signal History") | Disabled | `SHistoryMarkersEnabled` |
| **QRM** (labeled "QRM History") | Disabled | `SHistoryQrmEnabled` |

- **Signals:** Gold markers on the panadapter for detected voice-width signals. This toggle can also be activated from **View > Signal History Markers**.
- **QRM:** Red markers for persistent carriers and wideband interference. This toggle can also be activated from **View > QRM History Markers**.

### Clear All

| Control | Behavior |
|---|---|
| **Clear All** | Clears all DX spots, memory feed, Signal History markers, and QRM markers from the spectrum. |

### Spot display sliders

| Control | Default | Valid range | Setting key |
|---|---|---|---|
| **Levels:** | 3 | 1-10 | `SpotsMaxLevel` |
| **Position:** | 50 | 0-100 | `SpotsStartingHeightPercentage` |
| **Font Size:** | 16 | 8-32 | `SpotFontSize` |
| **Spot Lifetime:** | (varies) | 10 sec – 24 hrs (non-linear steps) | `DxClusterSpotLifetimeSec` |

- **Levels:** Number of vertical stacking rows for spots.
- **Position:** Vertical position of spots on the panadapter.
- **Font Size:** Spot text size.
- **Spot Lifetime:** How long a spot remains visible before fading.

### Color override controls

| Control | Default | Setting key |
|---|---|---|
| **Override Colors:** | Off | `IsSpotsOverrideColorsEnabled` |
| **Spot text color picker** | #FFFF00 | `SpotsOverrideColor` |
| **Override Background: Enabled** | Enabled | `IsSpotsOverrideBackgroundColorsEnabled` |
| **Override Background: Auto** | Enabled | `IsSpotsOverrideToAutoBackgroundColorEnabled` |
| **Spot background color picker** | #000000 | `SpotsOverrideBgColor` |
| **Background Opacity:** | 48 | 0-100 | `SpotsBackgroundOpacity` |

- **Override Colors:** When enabled, forces a single text color for all spots.
- **Override Background: Enabled:** When enabled, allows custom spot background color.
- **Override Background: Auto:** When enabled, automatically picks the background color for contrast.

### Spot Lines

| Control | Default | Setting key |
|---|---|---|
| **Spot Lines:** | Enabled | `IsSpotsLinesEnabled` |

When enabled, draws vertical lines from the spectrum up to each spot label. Disable during contests to reduce visual clutter.

### Total Spots

| Control | Behavior |
|---|---|
| **Total Spots:** | Live count of spots currently tracked across all sources. |

---

### DXCC Coloring Section

Controls for coloring spots based on DXCC worked/confirmed/needed status.

| Control | Default | Setting key |
|---|---|---|
| **DXCC Colors:** | Off | `IsDxccColoringEnabled` |
| **Log File (ADIF):** | (no file) | `DxccAdifFilePath` |
| **Imported:** | (no log loaded) | — (indicator) |

- **DXCC Colors:** When enabled, colors spots by worked/confirmed/needed DXCC status.
- **Log File (ADIF):** Click to load an ADIF log file. AetherSDR automatically watches the file for changes and reloads when modifications are detected.
- **Imported:** Shows the QSO count and entity count from the loaded log. Format: `<N> QSOs / <M> entities`.

#### DXCC color swatches

| Control | Setting key |
|---|---|
| **New DXCC** | `DxccColorNewEntity` |
| **New