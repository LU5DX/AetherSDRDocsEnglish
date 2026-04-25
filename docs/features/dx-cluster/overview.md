# SpotHub overview

SpotHub is AetherSDR's central hub for receiving DX spots from multiple sources and displaying them as overlays on the panadapter. Use it to connect to traditional DX clusters, the Reverse Beacon Network, WSJT-X, SpotCollector, POTA, and FreeDV — all from one dialog.

## Before you start

- Open SpotHub via `Settings > SpotHub...`. No radio connection is required.
- Have your login callsign ready if you plan to connect to a DX cluster or RBN.
- Have an ADIF log file available if you want DXCC coloring.

## How it works

SpotHub aggregates spots from up to six independent sources. Each source runs independently — you can enable any combination simultaneously. All incoming spots are merged into a unified list and rendered as frequency markers on the panadapter.

Spots from each source are color-coded separately so you can distinguish their origin at a glance. A global display layer (the **Display** tab) controls how all spots appear on the panadapter, regardless of source.

### Sources

**Cluster tab** — Connects to a DX cluster via a telnet session. You provide the hostname (`ClusterHost`), port (`ClusterPort`, 1–65535), and login callsign (`ClusterCallsign`). The **Cluster Console** shows raw telnet traffic. You can type cluster commands in the command line field and send them with Send. Spot color is set via **Spot Color:**, persisted as `ClusterSpotColor`.

**RBN tab** — Connects to the Reverse Beacon Network via telnet. Configuration mirrors the Cluster tab: `RbnHost`, `RbnPort` (1–65535), `RbnCallsign`. The **Rate Limit:** spinbox (`RbnRateLimit`) caps the number of spots accepted per second, which is useful because RBN traffic volume can be very high. The **RBN Console** shows raw traffic. Spot color is set via **Spot Color:** (`RbnSpotColor`).

**WSJT-X tab** — Listens for UDP datagrams broadcast by a running WSJT-X instance. Set the bind address (`WsjtxAddress`) and port (`WsjtxPort`, 1–65535), then click Start. Three checkboxes filter which decodes appear as spots: **CQ** (`WsjtxFilterCQ`), **CQ POTA** (`WsjtxFilterPOTA`), and **Calling Me** (`WsjtxFilterCallingMe`). Each category has its own color picker: CQ color (`WsjtxColorCQ`), POTA color (`WsjtxColorPOTA`), Calling Me color (`WsjtxColorCallingMe`), and Default color (`WsjtxColorDefault`). **Spot Life:** (`WsjtxSpotLife`) controls how long WSJT-X spots remain on the panadapter. The **WSJT-X Decodes** console shows the raw decode stream.

**SpotCollector tab** — Listens on a UDP port for spot broadcasts from Ham Radio Deluxe SpotCollector. Set **UDP Port:** (`SpotCollectorPort`, 1–65535) and click Start. The **SpotCollector Spots** console shows received spots.

**POTA tab** — Polls `api.pota.app` over HTTP at a configurable interval (**Poll Interval:**, `PotaPollInterval`). The server address is fixed and shown as an indicator. The **POTA Activations** console shows the activation feed. Spot color is set via **Spot Color:** (`PotaSpotColor`).

**FreeDV tab** — Connects to the FreeDV QSO Reporter via WebSocket at `qso.freedv.org`. The server address is fixed. The **FreeDV Spots** console shows activity. Spot color is set via **Spot Color:** (`FreeDvSpotColor`). This tab is only present in builds that include WebSocket support.

### Auto-connect and auto-start

Each source has an **Auto-connect on startup** or **Auto-start on startup** toggle. When enabled, that source connects or starts automatically every time AetherSDR launches, without manual intervention. The persisted keys are `ClusterAutoConnect`, `RbnAutoConnect`, `WsjtxAutoStart`, `SpotCollectorAutoStart`, `PotaAutoStart`, and `FreeDvAutoStart`.

### Spot List tab

The **Spot List** tab shows a unified, sortable table of all live spots from all active sources. Columns are: Time, Freq (kHz), DX Call, Mode, Comment, Spotter, Band, and Source. Per-band checkboxes under **Bands:** toggle visibility for each amateur band. Click **Clear** to empty the current list. Double-click any row to tune the active VFO to that spot's frequency.

### Display tab

The **Display** tab controls how spots appear on the panadapter.

| Control | Setting key | Default | What it does |
|---|---|---|---|
| **Spots:** | `IsSpotsEnabled` | Enabled | Master toggle for the spot overlay. Disable to hide all spots without disconnecting sources. |
| **Memories:** | `IsMemoriesShownOnPanadapter` | Disabled | Overlays stored memory channels on the panadapter alongside spots. |
| **Auto Mode:** | `SpotsAutoMode` | — | Automatically adjusts spot density based on the current panadapter zoom level. |
| **Levels:** | `SpotsStackLevels` | — | Number of vertical rows used when spots at nearby frequencies would overlap. |
| **Position:** | `SpotsPosition` | — | Vertical placement of the spot overlay on the panadapter. |
| **Font Size:** | `SpotsFontSize` | — | Text size of spot labels. |
| **Spot Lifetime:** | `SpotsLifetime` | — | How long a spot remains visible before fading, in seconds. |
| **Override Colors:** | `IsSpotsOverrideColorsEnabled` | — | Forces all spot labels to a single text color, ignoring per-source colors. |
| **Override Background: Enabled** | `IsSpotsOverrideBackgroundColorsEnabled` | — | Enables a custom background color behind spot labels. |
| **Override Background: Auto** | `IsSpotsOverrideToAutoBackgroundColorEnabled` | — | Selects an automatic contrast color for spot backgrounds. |
| **Background Opacity:** | `SpotsOverrideBgOpacity` | 48 | Opacity of the spot background. |
| **DXCC Coloring** | `DxccColoringEnabled` | — | Colors spots by worked, confirmed, or needed DXCC entity status, derived from a loaded ADIF log. |
| **Log File (ADIF):** | `DxccAdifPath` | — | Opens a file picker to load an ADIF log for DXCC coloring. |
| **Auto-Reload Log:** | `DxccAutoReload` | — | Watches the ADIF file for changes and re-reads it automatically when updated. |
| **Clear All Spots** | — | — | Immediately removes every spot currently tracked across all sources. |

## Tips

- RBN produces a very high spot rate. Set **Rate Limit:** to a value your display can handle before connecting, to avoid flooding the panadapter.
- WSJT-X spots are ephemeral by nature. Set **Spot Life:** to match the FT8 or FT4 transmission cycle length (15 or 7.5 seconds) if you want spots to clear between periods.
- The **Calling Me** filter in the WSJT-X tab highlights decodes specifically addressed to your callsign, which makes it easy to see when a station is responding to your CQ.
- **Auto Mode:** is useful during contests or DXpeditions when spot density varies significantly across bands and zoom levels.

## Troubleshooting

- **Cluster or RBN connects but no spots appear on the panadapter** — Check that **Spots:** on the **Display** tab is set to Enabled (`IsSpotsEnabled`). Also verify the relevant band checkboxes on the **Spot List** tab are checked.
- **WSJT-X spots are not received** — Confirm WSJT-X is configured to send UDP broadcasts to the same address and port shown in AetherSDR's WSJT-X tab, and that the listener is started (Start / Stop shows the running state).
- **FreeDV tab is not visible** — This tab is only present in builds compiled with WebSocket support. Your installed build may not include it.
- **DXCC coloring is not working** — Ensure an ADIF file has been loaded via **Log File (ADIF):** and that **DXCC Coloring** is enabled. The DXCC stats indicator shows how many QSOs were imported from the file.

## Related

- [Connect to a DX cluster](../../getting-started/setup/connect-to-a-dx-cluster.md)
- [Connect to the Reverse Beacon Network](../../getting-started/setup/connect-to-the-reverse-beacon-network.md)
- [Start WSJT-X UDP listener and filter for CQ, POTA or calls to me](start-wsjt-x-udp-listener-and-filter-for-cq-pota-or-calls-to-me.md)
- [Enable SpotCollector UDP feed](enable-spotcollector-udp-feed.md)
- [Poll POTA activations](poll-pota-activations.md)
- [Enable FreeDV QSO reporter WebSocket](enable-freedv-qso-reporter-websocket.md)
- [Enable DXCC coloring from an ADIF log](enable-dxcc-coloring-from-an-adif-log.md)
- [Auto-reload ADIF log when updated by a logger](auto-reload-adif-log-when-updated-by-a-logger.md)
- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
- [Tune to a spot by double-clicking the spot list](tune-to-a-spot-by-double-clicking-the-spot-list.md)
- [Pick colors for each spot source](pick-colors-for-each-spot-source
