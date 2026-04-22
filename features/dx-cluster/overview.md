# SpotHub overview

SpotHub is AetherSDR's central hub for receiving DX spots from multiple sources and displaying them as overlays on the panadapter. Use it to connect to a DX cluster, the Reverse Beacon Network (RBN), WSJT-X, SpotCollector, POTA, and FreeDV — and to control how spots look on screen.

## Before you start

- No radio connection is required to configure SpotHub.
- Open SpotHub from `Settings > SpotHub...`.

## How it works

SpotHub aggregates spots from up to six independent sources. Each source has its own tab for connection settings, a read-only console showing live traffic, and a spot color picker. All incoming spots feed into a unified spot list and are drawn as labeled markers on the panadapter.

### Sources

| Tab | How it connects | What it receives |
|---|---|---|
| Cluster | Telnet to a user-specified host and port | DX spots from a traditional packet cluster |
| RBN | Telnet to the Reverse Beacon Network | CW, RTTY, and FT8 skimmer spots with optional rate limiting |
| WSJT-X | UDP listener on a local address and port | Decoded transmissions from a running WSJT-X instance |
| SpotCollector | UDP listener on a local port | Spots broadcast by Ham Radio Deluxe SpotCollector |
| POTA | HTTP polling of `api.pota.app` | Current Parks on the Air activations |
| FreeDV | WebSocket connection to `qso.freedv.org` | FreeDV QSO reporter spots (requires WebSocket support) |

Each source can be started manually or configured to start automatically when AetherSDR launches using its respective "Auto-connect on startup" or "Auto-start on startup" toggle.

### Spot List tab

The Spot List tab shows a unified, sortable table of all live spots across every active source. Columns are Time, Freq (kHz), DX Call, Mode, Comment, Spotter, Band, and Source. Per-band checkboxes filter which bands appear in the table. Double-click any row to tune the active VFO to that spot's frequency. Click Clear to empty the current list.

### Display tab

The Display tab controls how spots appear on the panadapter and does not affect connectivity.

## What each control does

### Cluster tab

| Control | Behavior | Setting key |
|---|---|---|
| Server: | Hostname of the DX cluster | `ClusterHost` |
| Port: | Telnet port (1–65535) | `ClusterPort` |
| Callsign: | Login callsign sent to the cluster | `ClusterCallsign` |
| Connect / Disconnect | Toggles the telnet connection | — |
| Auto-connect on startup | Connects automatically at launch | `ClusterAutoConnect` |
| Cluster Console | Read-only display of raw cluster traffic | — |
| Send | Sends a typed command to the cluster | — |
| Spot Color: | Opens a color picker for cluster spots | `ClusterSpotColor` |

### RBN tab

| Control | Behavior | Setting key |
|---|---|---|
| Server: | RBN telnet hostname | `RbnHost` |
| Port: | RBN telnet port (1–65535) | `RbnPort` |
| Callsign: | Login callsign sent to RBN | `RbnCallsign` |
| Rate Limit: | Maximum RBN spots per second | `RbnRateLimit` |
| Connect / Disconnect | Toggles the RBN connection | — |
| Auto-connect on startup | Connects RBN automatically at launch | `RbnAutoConnect` |
| RBN Console | Read-only display of raw RBN traffic | — |
| Send | Sends a command to RBN | — |
| Spot Color: | Opens a color picker for RBN spots | `RbnSpotColor` |

### WSJT-X tab

| Control | Behavior | Setting key |
|---|---|---|
| Address: | UDP bind address for WSJT-X messages | `WsjtxAddress` |
| Port: | UDP port (1–65535) | `WsjtxPort` |
| Start / Stop | Starts or stops the UDP listener | — |
| Auto-start on startup | Starts listener automatically at launch | `WsjtxAutoStart` |
| CQ | Show spots for CQ calls only | `WsjtxFilterCQ` |
| CQ POTA | Show CQ POTA calls | `WsjtxFilterPOTA` |
| Calling Me | Show decodes addressed to your callsign | `WsjtxFilterCallingMe` |
| CQ color | Color for CQ spots | `WsjtxColorCQ` |
| POTA color | Color for CQ POTA spots | `WsjtxColorPOTA` |
| Calling Me color | Color for spots calling you | `WsjtxColorCallingMe` |
| Default color | Color for all other WSJT-X spots | `WsjtxColorDefault` |
| WSJT-X Decodes | Read-only console of decoded transmissions | — |
| Spot Life: | Seconds WSJT-X spots remain on the panadapter | `WsjtxSpotLife` |

### SpotCollector tab

| Control | Behavior | Setting key |
|---|---|---|
| UDP Port: | Port SpotCollector broadcasts on (1–65535) | `SpotCollectorPort` |
| Start / Stop | Starts or stops the UDP listener | — |
| Auto-start on startup | Starts listener automatically at launch | `SpotCollectorAutoStart` |
| SpotCollector Spots | Read-only console of received spots | — |

### POTA tab

| Control | Behavior | Setting key |
|---|---|---|
| Server: | Fixed endpoint: `api.pota.app` (HTTP polling) | — |
| Poll Interval: | Seconds between POTA polls | `PotaPollInterval` |
| Start / Stop | Starts or stops POTA polling | — |
| Auto-start on startup | Starts POTA polling automatically at launch | `PotaAutoStart` |
| POTA Activations | Read-only console of the activation feed | — |
| Spot Color: | Opens a color picker for POTA spots | `PotaSpotColor` |

### FreeDV tab

FreeDV is available only in builds that include WebSocket support.

| Control | Behavior | Setting key |
|---|---|---|
| Server: | Fixed endpoint: `qso.freedv.org` (WebSocket) | — |
| Start / Stop | Connects or disconnects the FreeDV WebSocket | — |
| Auto-start on startup | Connects automatically at launch | `FreeDvAutoStart` |
| FreeDV Spots | Read-only console of FreeDV activity | — |
| Spot Color: | Opens a color picker for FreeDV spots | `FreeDvSpotColor` |

### Display tab

| Control | Default | Behavior | Setting key |
|---|---|---|---|
| Spots: | Enabled | Master toggle for the panadapter spot overlay | `IsSpotsEnabled` |
| Memories: | Disabled | Toggles memory-channel markers on the panadapter | `IsMemoriesShownOnPanadapter` |
| Auto Mode: | — | Auto-selects spot density based on zoom level | `SpotsAutoMode` |
| Levels: | — | Number of vertical stacking rows for spot labels | `SpotsStackLevels` |
| Position: | — | Vertical position of spot labels on the panadapter | `SpotsPosition` |
| Font Size: | — | Spot label text size | `SpotsFontSize` |
| Spot Lifetime: | — | Seconds before a spot fades from the panadapter | `SpotsLifetime` |
| Override Colors: | — | Forces a single text color for all spots | `IsSpotsOverrideColorsEnabled` |
| Override Background: Enabled | — | Enables a custom background color for spot labels | `IsSpotsOverrideBackgroundColorsEnabled` |
| Override Background: Auto | — | Applies auto-contrast to spot label backgrounds | `IsSpotsOverrideToAutoBackgroundColorEnabled` |
| Background Opacity: | 48 | Opacity of the spot label background | `SpotsOverrideBgOpacity` |
| DXCC Coloring | — | Colors spots by worked/confirmed/needed status from an ADIF log | `DxccColoringEnabled` |
| Log File (ADIF): | — | Loads an ADIF log file to drive DXCC coloring | `DxccAdifPath` |
| Auto-Reload Log: | — | Re-reads the ADIF file automatically when it changes | `DxccAutoReload` |
| Clear All Spots | — | Removes every spot currently tracked across all sources | — |

## Tips

- Each source's spot color can be set independently. If you enable Override Colors: on the Display tab, that single color takes precedence over all per-source colors.
- Auto Mode: reduces clutter automatically at wide zoom levels. If spots are overlapping, enable it before adjusting Levels: manually.
- DXCC Coloring requires an ADIF log file. Enable Auto-Reload Log: if your logging software updates the file during a session so that coloring stays current without reopening SpotHub.

## Related

- [Connect to a DX cluster](../../getting-started/setup/connect-to-a-dx-cluster.md)
- [Connect to the Reverse Beacon Network](../../getting-started/setup/connect-to-the-reverse-beacon-network.md)
- [Start WSJT-X UDP listener and filter for CQ, POTA or calls to me](start-wsjt-x-udp-listener-and-filter-for-cq-pota-or-calls-to-me.md)
- [Enable SpotCollector UDP feed](enable-spotcollector-udp-feed.md)
- [Poll POTA activations](poll-pota-activations.md)
- [Enable FreeDV QSO reporter WebSocket](enable-freedv-qso-reporter-websocket.
