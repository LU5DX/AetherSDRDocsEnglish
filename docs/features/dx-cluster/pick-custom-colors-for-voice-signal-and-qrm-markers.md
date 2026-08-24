# SpotHub

The SpotHub dialog is the central control for connecting to DX spot sources, including a traditional DX cluster, the Reverse Beacon Network (RBN), WSJT-X, SpotCollector, POTA, FreeDV, and N1MM. It also provides comprehensive controls for how spots appear on the panadapter, including Signal History markers and DXCC coloring.

## Opening SpotHub

1. Click **Settings** > **SpotHub...**.

The dialog contains tabs for each spot source and a unified Display tab for visual customization.

---

## Cluster (tab)

Connects to a traditional DX cluster via telnet.

| Control | Description | Setting key |
|---|---|---|
| **Server:** | Hostname of the DX cluster. | `ClusterHost` |
| **Port:** | Telnet port (1-65535). | `ClusterPort` |
| **Callsign:** | Login callsign sent to the cluster. | `ClusterCallsign` |
| **Connect / Disconnect** | Toggles the telnet connection. | — |
| **Auto-connect on startup** | When enabled, connects automatically on launch. | `ClusterAutoConnect` |
| **Startup Commands...** | Opens the startup commands editor. Commands entered here (one per line) are sent automatically after every login. Supported commands include `SET/NAME`, `SET/QTH`, `ACCEPT/SPOT`, etc. | `DxClusterStartupCommands` |
| **Cluster Console** | Read-only telnet console showing raw cluster traffic. | — |
| **Send** | Sends a typed command to the cluster. | — |
| **Spot Color:** | Opens a color picker for cluster spots on the panadapter. | `ClusterSpotColor` |

---

## RBN (tab)

Reverse Beacon Network telnet source with rate limiting.

| Control | Description | Setting key |
|---|---|---|
| **Server:** | RBN telnet hostname. | `RbnHost` |
| **Port:** | RBN telnet port (1-65535). | `RbnPort` |
| **Callsign:** | Login callsign for RBN. | `RbnCallsign` |
| **Rate Limit:** | Caps the number of RBN spots per second. | `RbnRateLimit` |
| **Connect / Disconnect** | Toggles the RBN connection. | — |
| **Auto-connect on startup** | When enabled, starts RBN automatically on launch. | `RbnAutoConnect` |
| **Startup Commands...** | Opens the startup commands editor for RBN-specific commands (independent from the DX Cluster tab). Commands are sent after every login. | `RbnStartupCommands` |
| **RBN Console** | Read-only console of RBN traffic. | — |
| **Send** | Sends a command to RBN. | — |
| **Spot Color:** | Color picker for RBN spots. | `RbnSpotColor` |

---

## WSJT-X (tab)

UDP listener for WSJT-X decodes with filtering and color customization.

| Control | Description | Setting key |
|---|---|---|
| **Address:** | UDP bind address for WSJT-X messages. | `WsjtxAddress` |
| **Port:** | UDP port for WSJT-X (1-65535). | `WsjtxPort` |
| **Start / Stop** | Starts or stops the UDP listener. | — |
| **Auto-start on startup** | When enabled, starts the listener automatically on launch. | `WsjtxAutoStart` |
| **CQ** | Show only CQ calls. | `WsjtxFilterCQ` |
| **CQ POTA** | Show CQ POTA calls. | `WsjtxFilterPOTA` |
| **Calling Me** | Show only decodes addressed to your callsign. | `WsjtxFilterCallingMe` |
| **Spot Color: (CQ / POTA / Calling Me / Default)** | Color pickers for each WSJT-X spot category. | `WsjtxColorCQ`, `WsjtxColorPOTA`, `WsjtxColorCallingMe`, `WsjtxColorDefault` |
| **WSJT-X Decodes** | Console showing decoded transmissions. | — |
| **Spot Life:** | Seconds WSJT-X spots remain on the panadapter. | `WsjtxSpotLife` |

---

## SpotCollector (tab)

UDP listener for Ham Radio Deluxe SpotCollector broadcasts.

| Control | Description | Setting key |
|---|---|---|
| **UDP Port:** | UDP port SpotCollector broadcasts on (1-65535). | `SpotCollectorPort` |
| **Start / Stop** | Starts or stops the UDP listener. | — |
| **Auto-start on startup** | When enabled, starts the listener automatically on launch. | `SpotCollectorAutoStart` |
| **SpotCollector Spots** | Console showing received SpotCollector spots. | — |

---

## POTA (tab)

Polls api.pota.app for current activations.

| Control | Description | Setting key |
|---|---|---|
| **Server:** | Fixed endpoint: api.pota.app (HTTP polling). | — |
| **Poll Interval:** | Seconds between POTA polls. | `PotaPollInterval` |
| **Start / Stop** | Starts or stops polling. | — |
| **Auto-start on startup** | When enabled, starts POTA polling automatically on launch. | `PotaAutoStart` |
| **POTA Activations** | Console showing the activation feed. | — |
| **Spot Color:** | Color picker for POTA spots. | `PotaSpotColor` |

---

## FreeDV (tab)

WebSocket feed of FreeDV QSO reporter spots.

| Control | Description | Setting key |
|---|---|---|
| **Server:** | Fixed endpoint: qso.freedv.org (WebSocket). | — |
| **Start / Stop** | Connects or disconnects the WebSocket. | — |
| **Auto-start on startup** | When enabled, starts FreeDV automatically on launch. | `FreeDvAutoStart` |
| **FreeDV Spots** | Console showing FreeDV activity. | — |
| **Spot Color:** | Color picker for FreeDV spots. | `FreeDvSpotColor` |

---

## N1MM (tab)

UDP listener for N1MM Logger+ spot broadcasts.

| Control | Description | Setting key |
|---|---|---|
| **UDP Port:** | UDP port N1MM Logger+ broadcasts on (1-65535). | `N1MMPort` |
| **Start / Stop** | Starts or stops the UDP listener. | — |
| **Auto-start on startup** | When enabled, starts the listener automatically on launch. | `N1MMAutoStart` |
| **N1MM Spots** | Console showing received N1MM spots. | — |

---

## Spot List (tab)

Unified searchable table of all live spots from all sources.

The band-filter checkboxes use a flow layout that wraps to a new row when horizontal space runs out, rather than compressing the labels. This keeps the checked state readable even when the SpotHub dialog is narrow.

| Control | Description |
|---|---|
| **Bands:** | Per-band checkboxes to toggle visibility. One checkbox per band (160m, 80m, 60m, 40m, 30m, 20m, 17m, 15m, 12m, 10m, 6m, 2m, etc.). |
| **Clear** | Empties the current spot list. |
| **Spot table** | Sortable table with columns: Time, Freq, DX Call, Comment, Spotter, Band, Mode, Source. Double-click a row to tune to that frequency. Click any column header to sort by that column; click Time to return to newest-first order. |

### Showing and hiding table columns

Right-click any column header in the spot table to open a context menu. Each column name appears as a checkable menu item. The menu stays open while you toggle multiple columns, so you can show or hide several columns in one pass instead of reopening the menu for each column.

1. Right-click a column header in the spot table.
2. Check or uncheck any column name to show or hide it.
3. Click outside the menu or press Escape to close it.

---

## Display (tab)

Controls how spots and markers appear on the panadapter. This tab combines spot visualization settings, DXCC coloring, and Signal History tunables.

### Top toggle row

| Control | Default | Description | Setting key |
|---|---|---|---|
| **Spots:** | Enabled | Master toggle for DX spot overlay. | `IsSpotsEnabled` |
| **Memories:** | Disabled | Toggles memory-channel overlay on the panadapter. | `IsMemorySpotsEnabled` |
| **Auto:** | Enabled | Automatically switches slice mode when clicking a spot that includes mode info (e.g. CW, FT8, RTTY). | `SpotAutoSwitchMode` |
| **Signals** (Signal History) | Disabled | Gold markers for detected voice-width signals on the panadapter. Same toggle as **View > Signal History Markers**. | `SHistoryMarkersEnabled` |
| **QRM** (Signal History) | Disabled | Red markers for persistent carriers and wideband interference. Same toggle as **View > QRM History Markers**. | `SHistoryQrmEnabled` |
| **Clear All** | — | Clears all DX spots, memory feed, Signal History markers, and QRM markers from the spectrum. | — |

### Spot appearance sliders

| Control | Default | Valid range | Description | Setting key |
|---|---|---|---|---|
| **Levels:** | 3 | 1-10 | Number of vertical stacking rows for spots. | `SpotsMaxLevel` |
| **Position:** | 50 | 0-100 | Vertical position on the panadapter. | `SpotsStartingHeightPercentage` |
| **Font Size:** | 16 | 8-32 | Spot text size. | `SpotFontSize` |
| **Spot Lifetime:** | — | 10 sec – 24 hrs (non-linear steps) | Seconds before a spot fades away. | `DxClusterSpotLifetimeSec` |

### Override colors

| Control | Default | Description | Setting key |
|---|---|---|---|
| **Override Colors:** | Disabled | Forces a single text color for all spots. Button label is static and always shows "Enabled" when checked. | `IsSpotsOverrideColorsEnabled` |
| **Spot text color picker** | `#FFFF00` | Opens color picker for spot text color. | `SpotsOverrideColor` |
| **Override Background: Enabled** | Enabled | Enables custom spot background color. | `IsSpotsOverrideBackgroundColorsEnabled` |
| **Override Background: Auto** | Enabled | Auto-picks background color for contrast. | `IsSpotsOverrideToAutoBackgroundColorEnabled` |
| **Spot background color picker** | `#000000` | Opens color picker for spot background color. | `SpotsOverrideBgColor` |
| **Background Opacity:** | 48 | 0-100 | Opacity of spot background color. | `SpotsBackgroundOpacity` |
| **Spot Lines:** | Enabled | Draws vertical lines from the spectrum up to each spot label. Disable during contests to reduce visual clutter. Button label is static and always shows "Enabled" when checked. | `IsSpotsLinesEnabled` |

### Total Spots indicator

Live count of spots currently tracked across all sources.

### DXCC Coloring (section)

Colors spots by worked/confirmed/needed DXCC status using an imported ADIF log.

| Control | Description | Setting key |
|---|---|---|
| **DXCC Colors:** | Enables DXCC-based spot coloring. Button label is static and always shows "Enabled" when checked. | `IsDxccColoringEnabled` |
| **Log File (ADIF):** | Loads an ADIF log file to drive DXCC coloring. Auto-watches the file for changes after selection. | `DxccAdifFilePath` |
| **Imported: (DXCC stats)** | Shows QSO count and entity count when a log is loaded. Format: `<N> QSOs / <M> entities`. | — |
| **New DXCC / New Band / New Mode / Worked** color swatches | Opens a color picker for each DXCC status category. | `DxccColorNewEntity`, `DxccColorNewBand`, `DxccColorNewMode`, `DxccColorWorked` |

### Signal History (section)

Controls for Signal History marker behavior and appearance.

| Control | Default | Valid range | Description | Setting key |
|---|---|---|---|---|
| **Marker Lifetime:** | 60 | 15-300 sec | How long an inactive Signal History marker persists before being removed. | `SHistoryLifetimeS` |
| **QRM Gate:** | 6 | 3-30 sec | How long a narrow carrier or wideband signal must persist before being classified as QRM. | `SHistoryQrmGateS` |
| **Edge Threshold:** | 3.0 | 1.0-10.0 dB | Threshold above noise floor for the slope edge walk that refines the S-History carrier-side edge. Lower values pull the marker closer to the carrier. | `SHistorySoftEdgeDb` |
| **Signals** color swatch | `#FFC800` (gold) | Any QColor | Color for voice signal markers. | `SHistoryColorSignals` |
| **QRM** color swatch | `#FF0000` (red) | Any QColor | Color for QRM markers. | `SHistoryColorQrm` |
| **Snap to Step:** | Disabled | — | Rounds S-History click-to-tune to the nearest multiple of the active slice's step size, hiding the small carrier offset. Button label