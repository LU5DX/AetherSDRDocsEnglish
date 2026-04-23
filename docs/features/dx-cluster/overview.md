# SpotHub overview

SpotHub is AetherSDR's central spot management hub. It aggregates DX spots from up to six independent sources — DX cluster, Reverse Beacon Network (RBN), WSJT-X, SpotCollector, POTA, and FreeDV — and overlays them on the panadapter. Use SpotHub to configure each source, control how spots look, and tune to any spot in one click.

## Before you start

- Open SpotHub from `Settings > SpotHub...`. No radio connection is required.
- Each source tab is independent. You can run any combination of sources simultaneously.

## How it works

SpotHub collects spots from multiple sources and merges them into a single live pool. Each spot carries a frequency, callsign, comment, spotter, band, mode, and source label. Spots are rendered as overlays on every panadapter. A unified Spot List tab lets you sort and filter across all active sources, and double-clicking any row tunes the active VFO to that frequency.

The six source tabs each manage one feed. The Display tab controls how the combined pool is rendered. DXCC coloring — driven by your own ADIF log — can color-code spots by worked, confirmed, or needed status.

## What each control does

### Cluster tab

Controls the telnet connection to a traditional DX cluster node.

| Control | Description | Setting key |
|---|---|---|
| Server: | Hostname of the DX cluster to connect to. | `ClusterHost` |
| Port: | Telnet port. Valid range: 1–65535. | `ClusterPort` |
| Callsign: | Login callsign sent to the cluster on connect. | `ClusterCallsign` |
| Connect / Disconnect | Toggles the telnet connection. Default label: Connect. | — |
| Auto-connect on startup | When enabled, connects automatically at launch. | `ClusterAutoConnect` |
| Cluster Console | Read-only display of raw cluster telnet traffic. | — |
| Send | Sends a typed command to the cluster. | — |
| Spot Color: | Opens a color picker for cluster-sourced spots on the panadapter. | `ClusterSpotColor` |

### RBN tab

Controls the telnet connection to the Reverse Beacon Network, with rate limiting to manage high spot volume.

| Control | Description | Setting key |
|---|---|---|
| Server: | RBN telnet hostname. | `RbnHost` |
| Port: | RBN telnet port. Valid range: 1–65535. | `RbnPort` |
| Callsign: | Login callsign sent to RBN. | `RbnCallsign` |
| Rate Limit: | Maximum RBN spots accepted per second. | `RbnRateLimit` |
| Connect / Disconnect | Toggles the RBN telnet connection. Default label: Connect. | — |
| Auto-connect on startup | Connects to RBN automatically at launch. | `RbnAutoConnect` |
| RBN Console | Read-only display of raw RBN telnet traffic. | — |
| Send | Sends a command to the RBN connection. | — |
| Spot Color: | Opens a color picker for RBN-sourced spots. | `RbnSpotColor` |

### WSJT-X tab

Listens on a UDP port for decoded transmissions from a running WSJT-X instance. Filters narrow what appears on the panadapter.

| Control | Description | Setting key |
|---|---|---|
| Address: | UDP bind address for WSJT-X messages. | `WsjtxAddress` |
| Port: | UDP port. Valid range: 1–65535. | `WsjtxPort` |
| Start / Stop | Starts or stops the UDP listener. | — |
| Auto-start on startup | Starts the listener automatically at launch. | `WsjtxAutoStart` |
| CQ | When checked, shows only CQ calls. | `WsjtxFilterCQ` |
| CQ POTA | When checked, shows CQ POTA calls. | `WsjtxFilterPOTA` |
| Calling Me | When checked, shows only decodes addressed to your callsign. | `WsjtxFilterCallingMe` |
| CQ color / POTA color / Calling Me color / Default color | Color pickers for each WSJT-X spot category. | `WsjtxColorCQ` / `WsjtxColorPOTA` / `WsjtxColorCallingMe` / `WsjtxColorDefault` |
| WSJT-X Decodes | Read-only console of decoded transmissions. | — |
| Spot Life: | Seconds WSJT-X spots remain on the panadapter before expiring. | `WsjtxSpotLife` |

### SpotCollector tab

Receives spots broadcast over UDP by Ham Radio Deluxe SpotCollector.

| Control | Description | Setting key |
|---|---|---|
| UDP Port: | UDP port SpotCollector broadcasts on. Valid range: 1–65535. | `SpotCollectorPort` |
| Start / Stop | Starts or stops the UDP listener. | — |
| Auto-start on startup | Starts the listener automatically at launch. | `SpotCollectorAutoStart` |
| SpotCollector Spots | Read-only console of received SpotCollector spots. | — |

### POTA tab

Polls `api.pota.app` over HTTP for current Parks on the Air activations.

| Control | Description | Setting key |
|---|---|---|
| Server: | Fixed endpoint indicator: `api.pota.app` (HTTP polling). Not editable. | — |
| Poll Interval: | Seconds between polls. | `PotaPollInterval` |
| Start / Stop | Starts or stops POTA polling. | — |
| Auto-start on startup | Starts polling automatically at launch. | `PotaAutoStart` |
| POTA Activations | Read-only console of the activation feed. | — |
| Spot Color: | Opens a color picker for POTA-sourced spots. | `PotaSpotColor` |

### FreeDV tab

Connects to the FreeDV QSO reporter via WebSocket to display FreeDV activity spots. This tab is only present in builds with WebSocket support.

| Control | Description | Setting key |
|---|---|---|
| Server: | Fixed endpoint indicator: `qso.freedv.org` (WebSocket). Not editable. | — |
| Start / Stop | Connects or disconnects the FreeDV WebSocket. | — |
| Auto-start on startup | Connects automatically at launch. | `FreeDvAutoStart` |
| FreeDV Spots | Read-only console of FreeDV activity. | — |
| Spot Color: | Opens a color picker for FreeDV-sourced spots. | `FreeDvSpotColor` |

### Spot List tab

A unified, sortable table of all live spots from every active source.

| Control | Description | Setting key |
|---|---|---|
| Bands: | Per-band checkboxes (160m, 80m, 60m, 40m, 30m, 20m, 17m, 15m, 12m, 10m, 6m, 2m, and others). Uncheck a band to hide it from the table. | — |
| Clear | Removes all spots from the current spot list. | — |
| Spot table | Sortable table with columns: Time, Freq (kHz), DX Call, Mode, Comment, Spotter, Band, Source. Double-click a row to tune to that frequency. | — |

### Display tab

Controls how spots are rendered on the panadapter and enables DXCC log-based coloring.

| Control | Default | Description | Setting key |
|---|---|---|---|
| Spots: | Enabled | Master toggle for the spot overlay. Disable to hide all spots without disconnecting sources. | `IsSpotsEnabled` |
| Memories: | Disabled | Toggles the memory-channel overlay on the panadapter. | `IsMemoriesShownOnPanadapter` |
| Auto Mode: | — | Automatically adjusts spot density based on current zoom level. | `SpotsAutoMode` |
| Levels: | — | Number of vertical stacking rows used when spots overlap. | `SpotsStackLevels` |
| Position: | — | Vertical position of the spot overlay on the panadapter. | `SpotsPosition` |
| Font Size: | — | Text size for spot labels. | `SpotsFontSize` |
| Spot Lifetime: | — | Seconds before a spot fades from the panadapter. | `SpotsLifetime` |
| Override Colors: | — | Forces a single text color for all spots, overriding per-source colors. | `IsSpotsOverrideColorsEnabled` |
| Override Background: Enabled / Auto | — | Enables a custom spot background color. Auto applies automatic contrast. | `IsSpotsOverrideBackgroundColorsEnabled` / `IsSpotsOverrideToAutoBackgroundColorEnabled` |
| Background Opacity: | 48 | Opacity of the spot background color. | `SpotsOverrideBgOpacity` |
| DXCC Coloring | — | Colors spots by worked, confirmed, or needed DXCC status from your ADIF log. | `DxccColoringEnabled` |
| Log File (ADIF): | — | Opens a file picker to load an ADIF log file that drives DXCC coloring. | `DxccAdifPath` |
| Auto-Reload Log: | — | Re-reads the ADIF file automatically whenever it changes on disk. | `DxccAutoReload` |
| Clear All Spots | — | Removes every spot currently tracked across all sources. | — |

## Tips

- Each source's status indicator shows the current state: Disconnected, Connected, Stopped, Listening, or Polling. Check the status indicator on each tab before troubleshooting.
- The total spots count indicator shows how many spots are currently tracked across all sources combined.
- RBN can generate very high spot rates. Set Rate Limit: on the RBN tab to prevent the spot pool from being overwhelmed.
- WSJT-X spots are short-lived by nature. Use Spot Life: to match the duration to
