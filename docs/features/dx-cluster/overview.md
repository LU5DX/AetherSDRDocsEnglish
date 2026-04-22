# SpotHub overview

SpotHub is AetherSDR's central hub for receiving DX spots from multiple sources and displaying them as overlays on the panadapter. Use it to connect to a DX cluster, the Reverse Beacon Network, WSJT-X, SpotCollector, POTA, or FreeDV — and to control how spots look and behave on screen.

## Before you start

- AetherSDR does not need to be connected to a radio to configure SpotHub, but spot overlays on the panadapter only appear when a radio is connected.
- The FreeDV tab is only present in builds that include WebSocket support.

## How it works

Open SpotHub from `Settings > SpotHub...`. The dialog contains eight tabs: **Cluster**, **RBN**, **WSJT-X**, **SpotCollector**, **POTA**, **FreeDV**, **Spot List**, and **Display**.

Each source tab manages one incoming spot feed independently. Spots from all active sources flow into a single unified pool, visible in the **Spot List** tab and rendered as overlays on the panadapter according to the settings on the **Display** tab.

### Cluster tab

Connects to a DX cluster via telnet. The **Cluster Console** shows raw telnet traffic. You can type commands into the command line and click **Send** to submit them.

| Control | Persisted setting | Notes |
|---|---|---|
| `Server:` | `ClusterHost` | Hostname of the DX cluster. |
| `Port:` | `ClusterPort` | Telnet port; valid range 1–65535. |
| `Callsign:` | `ClusterCallsign` | Login callsign sent on connect. |
| `Connect` / `Disconnect` | — | Toggles the telnet connection. |
| `Auto-connect on startup` | `ClusterAutoConnect` | Reconnects automatically on launch. |
| `Spot Color:` | `ClusterSpotColor` | Color picker for cluster spot labels. |

### RBN tab

Connects to the Reverse Beacon Network via telnet. Includes a rate limiter to reduce panadapter clutter from high-volume beacon spots.

| Control | Persisted setting | Notes |
|---|---|---|
| `Server:` | `RbnHost` | RBN telnet hostname. |
| `Port:` | `RbnPort` | Telnet port; valid range 1–65535. |
| `Callsign:` | `RbnCallsign` | Login callsign sent to RBN. |
| `Rate Limit:` | `RbnRateLimit` | Caps the number of RBN spots per second. |
| `Connect` / `Disconnect` | — | Toggles the RBN connection. |
| `Auto-connect on startup` | `RbnAutoConnect` | Reconnects automatically on launch. |
| `Spot Color:` | `RbnSpotColor` | Color picker for RBN spot labels. |

### WSJT-X tab

Listens on a UDP port for decoded transmissions from a running WSJT-X instance. Filters let you reduce the display to only the decodes that matter.

| Control | Persisted setting | Notes |
|---|---|---|
| `Address:` | `WsjtxAddress` | UDP bind address. |
| `Port:` | `WsjtxPort` | UDP port; valid range 1–65535. |
| `Start` / `Stop` | — | Starts or stops the UDP listener. |
| `Auto-start on startup` | `WsjtxAutoStart` | Starts listener automatically on launch. |
| `CQ` | `WsjtxFilterCQ` | Show only CQ calls. |
| `CQ POTA` | `WsjtxFilterPOTA` | Show CQ POTA calls. |
| `Calling Me` | `WsjtxFilterCallingMe` | Show only decodes addressed to your callsign. |
| CQ / POTA / Calling Me / Default color pickers | `WsjtxColorCQ` / `WsjtxColorPOTA` / `WsjtxColorCallingMe` / `WsjtxColorDefault` | Per-category spot colors. |
| `Spot Life:` | `WsjtxSpotLife` | Seconds WSJT-X spots remain on the panadapter. |

### SpotCollector tab

Listens on a UDP port for spot broadcasts from Ham Radio Deluxe SpotCollector.

| Control | Persisted setting | Notes |
|---|---|---|
| `UDP Port:` | `SpotCollectorPort` | Valid range 1–65535. |
| `Start` / `Stop` | — | Starts or stops the UDP listener. |
| `Auto-start on startup` | `SpotCollectorAutoStart` | Starts listener automatically on launch. |

### POTA tab

Polls `api.pota.app` over HTTP at a configurable interval to retrieve current Parks on the Air activations.

| Control | Persisted setting | Notes |
|---|---|---|
| `Poll Interval:` | `PotaPollInterval` | Seconds between polls of the POTA API. |
| `Start` / `Stop` | — | Starts or stops polling. |
| `Auto-start on startup` | `PotaAutoStart` | Starts polling automatically on launch. |
| `Spot Color:` | `PotaSpotColor` | Color picker for POTA spot labels. |

### FreeDV tab

Connects to the FreeDV QSO reporter at `qso.freedv.org` via WebSocket. This tab is only present in builds with WebSocket support.

| Control | Persisted setting | Notes |
|---|---|---|
| `Start` / `Stop` | — | Connects or disconnects the WebSocket feed. |
| `Auto-start on startup` | `FreeDvAutoStart` | Connects automatically on launch. |
| `Spot Color:` | `FreeDvSpotColor` | Color picker for FreeDV spot labels. |

### Spot List tab

Displays a unified, sortable table of all live spots from every active source. Columns are Time, Freq (kHz), DX Call, Mode, Comment, Spotter, Band, and Source. Double-clicking a row tunes the active VFO to that spot's frequency.

Per-band checkboxes at the top of the tab toggle visibility of spots by band (160m through 2m). Click **Clear** to empty the current spot list without disconnecting any source.

### Display tab

Controls how spots are rendered on the panadapter and whether DXCC award status affects their color.

| Control | Persisted setting | Default | Notes |
|---|---|---|---|
| `Spots:` | `IsSpotsEnabled` | Enabled | Master toggle for the spot overlay. Disable to hide all spots without disconnecting sources. |
| `Memories:` | `IsMemoriesShownOnPanadapter` | Disabled | Toggles memory-channel markers on the panadapter. |
| `Auto Mode:` | `SpotsAutoMode` | — | Automatically adjusts spot density based on panadapter zoom level. |
| `Levels:` | `SpotsStackLevels` | — | Number of vertical stacking rows used when spots overlap. |
| `Position:` | `SpotsPosition` | — | Vertical position of spot labels on the panadapter. |
| `Font Size:` | `SpotsFontSize` | — | Text size of spot labels. |
| `Spot Lifetime:` | `SpotsLifetime` | — | Seconds before a spot label fades away. |
| `Override Colors:` | `IsSpotsOverrideColorsEnabled` | — | Forces a single text color for all spots, ignoring per-source colors. |
| `Override Background:` Enabled / Auto | `IsSpotsOverrideBackgroundColorsEnabled` / `IsSpotsOverrideToAutoBackgroundColorEnabled` | — | Enables a custom spot background color; Auto selects a contrasting background automatically. |
| `Background Opacity:` | `SpotsOverrideBgOpacity` | 48 | Opacity of the spot background fill. |
| `DXCC Coloring` | `DxccColoringEnabled` | — | Colors spots by worked, confirmed, or needed DXCC status. |
| `Log File (ADIF):` | `DxccAdifPath` | — | Path to an ADIF log file used to determine DXCC status. |
| `Auto-Reload Log:` | `DxccAutoReload` | — | Re-reads the ADIF file automatically when it is updated by a logging application. |
| `Clear All Spots` | — | — | Removes every spot currently tracked across all sources. |

## Tips

- Each source tab shows a status indicator: **Connected**, **Disconnected**, **Listening**, **Polling**, or **Stopped**. Check this before assuming a source is active.
- The total number of spots currently tracked is shown in the dialog and updates as new spots arrive.
- Each source console (Cluster Console, RBN Console, WSJT-X Decodes, POTA Activations, FreeDV Spots, SpotCollector Spots) auto-scrolls when you are already at the bottom, but stops following if you scroll up to review earlier traffic.
- DXCC coloring has no effect unless you have loaded an ADIF file with `Log File (ADIF):`.

## Related

- [Connect to a DX cluster](../../getting-started/setup/connect-to-a-dx-cluster.md)
- [Connect to the Reverse Beacon Network](../../getting-started/setup/connect-to-the-reverse-beacon-network.md)
- [Start WSJT-X UDP listener and filter for CQ, POTA or calls to me](start-wsjt-x-udp-listener-and-filter-for-cq-pota-or-calls-to-me.md)
- [Enable SpotCollector UDP feed](enable-spotcollector-udp-feed.md)
- [Poll POTA activations](poll-pota-activations.md)
- [Enable FreeDV QSO reporter WebSocket](enable-freedv-qso-reporter-websocket
