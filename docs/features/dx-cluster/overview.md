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

**Cluster tab** — Connects to a DX cluster via a telnet session. You provide the hostname (`ClusterHost`), port (`ClusterPort`, 1–65535), and login callsign (`ClusterCallsign`). The **Cluster Console** shows raw telnet traffic. You can type cluster commands in the command line field and send them with **Send**. Spot color is set via **Spot Color:**, persisted as `ClusterSpotColor`.

The **Startup Commands…** button opens an editor for cluster commands sent automatically after every login. Enter one command per line — for example `SET/NAME`, `SET/QTH`, `ACCEPT/SPOT`. The commands are persisted as `DxClusterStartupCommands` and replayed by the cluster client after each login.

**RBN tab** — Connects to the Reverse Beacon Network via telnet. Configuration mirrors the Cluster tab: `RbnHost`, `RbnPort` (1–65535), `RbnCallsign`. The **Rate Limit:** spinbox (`RbnRateLimit`) caps the number of spots accepted per second, which is useful because RBN traffic volume can be very high. The **RBN Console** shows raw traffic. Spot color is set via **Spot Color:** (`RbnSpotColor`).

The **Startup Commands…** button opens an editor for RBN-specific cluster commands sent automatically after every login. Enter one command per line. The commands are persisted as `RbnStartupCommands` and replayed independently from the DX cluster startup commands.

**WSJT-X tab** — Listens for UDP datagrams broadcast by a running WSJT-X instance. Set the bind address (`WsjtxAddress`) and port (`WsjtxPort`, 1–65535), then click **Start**. Three checkboxes filter which decodes appear as spots: **CQ** (`WsjtxFilterCQ`), **CQ POTA** (`WsjtxFilterPOTA`), and **Calling Me** (`WsjtxFilterCallingMe`). Each category has its own color picker: CQ color (`WsjtxColorCQ`), POTA color (`WsjtxColorPOTA`), Calling Me color (`WsjtxColorCallingMe`), and Default color (`WsjtxColorDefault`). **Spot Life:** (`WsjtxSpotLife`) controls how long WSJT-X spots remain on the panadapter. The **WSJT-X Decodes** console shows the raw decode stream.

**SpotCollector tab** — Listens on a UDP port for spot broadcasts from Ham Radio Deluxe SpotCollector. Set **UDP Port:** (`SpotCollectorPort`, 1–65535) and click **Start**. The **SpotCollector Spots** console shows received spots.

**POTA tab** — Polls `api.pota.app` over HTTP at a configurable interval (**Poll Interval:**, `PotaPollInterval`). The server address is fixed and shown as an indicator. The **POTA Activations** console shows the activation feed. Spot color is set via **Spot Color:** (`PotaSpotColor`).

**FreeDV tab** — Connects to the FreeDV QSO Reporter via WebSocket at `qso.freedv.org`. The server address is fixed. The **FreeDV Spots** console shows activity. Spot color is set via **Spot Color:** (`FreeDvSpotColor`). This tab is only present in builds that include WebSocket support.

### Auto-connect and auto-start

Each source has an **Auto-connect on startup** or **Auto-start on startup** toggle. When enabled, that source connects or starts automatically every time AetherSDR launches, without manual intervention. The persisted keys are `ClusterAutoConnect`, `RbnAutoConnect`, `WsjtxAutoStart`, `SpotCollectorAutoStart`, `PotaAutoStart`, and `FreeDvAutoStart`.

### Spot List tab

The **Spot List** tab shows a unified, sortable table of all live spots from all active sources. Columns are: Time, Freq (kHz), DX Call, Mode, Comment, Spotter, Band, and Source. Per-band checkboxes under **Bands:** toggle visibility for each amateur band. Click **Clear** to empty the current list. Double-click any row to tune the active VFO to that spot's frequency and, where the spot carries mode information (for example CW, FT8, or RTTY), automatically switch the slice to that mode.

### Display tab
The **Display** tab controls how spots appear on the panadapter.

| Control                                                       | Setting key                                                                                                              | Default                                                                                                            |
|---------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| **Spots:**                                                    | `IsSpotsEnabled`                                                                                                         | Enabled                                                                                                            |
| **Memories:**                                                 | `IsMemorySpotsEnabled`                                                                                                   | Disabled                                                                                                           |
| **Auto:**                                                     | `SpotAutoSwitchMode`                                                                                                     | Enabled                                                                                                            |
| **Signals (Signal History)**                                  | `SHistoryMarkersEnabled`                                                                                                 | Disabled                                                                                                           |
| **QRM (Signal History)**                                      | `SHistoryQrmEnabled`                                                                                                     | Disabled                                                                                                           |
| **Clear All**                                                 | —                                                                                                                        | —                                                                                                                  |
| **Levels:**                                                   | `SpotsMaxLevel`                                                                                                          | 3                                                                                                                  |
| **Position:**                                                 | `SpotsStartingHeightPercentage`                                                                                          | 50                                                                                                                 |
| **Font Size:**                                                | `SpotFontSize`                                                                                                           | 16                                                                                                                 |
| **Spot Lifetime:**                                            | `DxClusterSpotLifetimeSec`                                                                                               | —                                                                                                                  |
| **Override Colors:**                                          | `IsSpotsOverrideColorsEnabled`                                                                                           | —                                                                                                                  |
| **Spot text color picker**                                    | `SpotsOverrideColor`                                                                                                     | #FFFF00                                                                                                            |
| **Override Background: Enabled**                              | `IsSpotsOverrideBackgroundColorsEnabled`                                                                                 | Enabled                                                                                                            |
| **Override Background: Auto**                                 | `IsSpotsOverrideToAutoBackgroundColorEnabled`                                                                            | Enabled                                                                                                            |
| **Spot background color picker**                              | `SpotsOverrideBgColor`                                                                                                   | #000000                                                                                                            |
| **Background Opacity:**                                       | `SpotsBackgroundOpacity`                                                                                                 | 48                                                                                                                 |
| **Spot Lines:**                                               | `IsSpotsLinesEnabled`                                                                                                    | Enabled                                                                                                            |
| **Total Spots:**                                              | Live readout of how many spots are currently tracked across all sources.                                                 | Updated whenever spots are added or cleared. Resets to 0 when **Clear All** is pressed.                            |
| **DXCC Coloring (section)**                                   | Section header for DXCC coloring controls in the left column below the divider.                                          | —                                                                                                                  |
| **DXCC Colors:**                                              | `IsDxccColoringEnabled`                                                                                                  | —                                                                                                                  |
| **Log File (ADIF):**                                          | `DxccAdifFilePath`                                                                                                       | —                                                                                                                  |
| **Imported: (DXCC stats)**                                    | Shows QSO count and entity count when a log is loaded.                                                                   | (no log loaded)                                                                                                    |
| **DXCC Color swatches (New DXCC / New Band / New Mode / Worked)** | `DxccColorNewEntity`, `DxccColorNewBand`, `DxccColorNewMode`, `DxccColorWorked`                                     | —                                                                                                                  |
| **Signal History (section)**                                  | Section header for Signal History tunables in the right column below the divider.                                        | —                                                                                                                  |
| **Marker Lifetime:**                                          | `SHistoryLifetimeS`                                                                                                      | 60 s                                                                                                               |
| **QRM Gate:**                                                 | `SHistoryQrmGateS`                                                                                                       | 6 s                                                                                                                |
| **Edge Threshold:**                                           | `SHistorySoftEdgeDb`                                                                                                     | 3.0 dB                                                                                                             |
| **Signal History color swatches (Signals / QRM)**             | `SHistoryColorSignals` / `SHistoryColorQrm`                                                                              | #FFC800 / #FF0000                                                                                                  |
| **Snap to Step:**                                             | `SHistorySnapToStep`                                                                                                     | Disabled                                                                                                           |

**Spot Lines:** draws a vertical line from the spectrum baseline up to each spot label. Disable this during contests to reduce visual clutter. The setting is persisted as `IsSpotsLinesEnabled` and defaults to Enabled.

**Auto:** defaults to **Enabled** (`SpotAutoSwitchMode` defaults to `True`). If you previously relied on Auto Mode being off by default, verify this setting after upgrading.

### FreeDV Reporter reporting

The **FreeDV** tab includes a **Station Reporting** section that lets AetherSDR broadcast your station activity to the public FreeDV Reporter map at `qso.freedv.org` whenever the RADE modem is active. This feature is only present in builds compiled with WebSocket support.

#### Enable reporting

1. Open the **FreeDV** tab.
2. Fill in a valid callsign and grid square in the **Callsign:** and **Grid Square:** fields (see below). The checkbox refuses to enable if either field is blank or unresolvable.
3. Check **Enable FreeDV Reporter reporting when RADE is active** (`FreeDvAutoReport`). If the callsign or grid cannot be resolved, a warning dialog appears and the checkbox reverts to unchecked.

> **Note:** Reporter data is published to a community-shared public map. Do not enable reporting with placeholder values.

#### Callsign field

| Control | Setting key | Default | Notes |
|---|---|---|---|
| **Callsign:** | `FreeDvMyCallsign` | — | The callsign sent to the FreeDV Reporter map. Field is read-only when **Use radio** is checked. |
| **Use radio** | `FreeDvUseRadioCallsign` | True | Pre-fills the callsign from the radio's configured callsign and locks the field read-only. Updates automatically if you change the callsign in Radio Setup. |

When **Use radio** is checked, the field displays the radio's callsign. Uncheck it to enter a callsign manually.

#### Grid Square field

| Control | Setting key | Default | Notes |
|---|---|---|---|
| **Grid Square:** | `FreeDvMyGrid` | — | Maidenhead grid square sent to the FreeDV Reporter map. Field is read-only when **Use GPS** is checked. |
| **Use GPS** | `FreeDvUseGpsGrid` | True | Pre-fills the grid from the radio's GPS module and locks the field read-only. Only shown on radio models that have GPS hardware. |

#### Station message

| Control | Setting key | Default | Notes |
|---|---|---|---|
| **Station Msg:** | `FreeDvMyMessage` | — | Optional free-text message shown beside your callsign on the public FreeDV Reporter map. |

## SWR sweep overlay

V0.9.4 adds a SWR sweep overlay that plots SWR versus frequency directly on the panadapter. An external source (for example, an antenna analyzer integration) supplies the data by calling `setSwrSweepPoints()`. The panadapter renders the curve via the internal `drawSwrSweep()` layer.

### Supplying sweep data

Call `setSwrSweepPoints()` with a vector of `SwrSweepPoint` values. Each point carries two fields:

| Field | Type | Default | Description |
|---|---|---|---|
| `freqMhz` | `double` | `0.0` | Frequency of the measurement in MHz. |
| `swr` | `float` | `1.0` | SWR value at that frequency. |

The method signature is:

```
setSwrSweepPoints(points, running, currentFreqMhz, sourceLabel)
```

| Parameter | Type | Default | Description |
|---|---|---|---|
| `points` | `QVector<SwrSweepPoint>` | — | The sweep data to display. |
| `running` | `bool` | `false` | Pass `true` while a sweep is in progress to indicate a live, incomplete trace. |
| `currentFreqMhz` | `double` | `-1.0` | The frequency currently being swept. Pass `-1.0` to suppress the cursor. |
| `sourceLabel` | `QString` | *(empty)* | Optional label identifying the source of the sweep data, shown on the overlay. |

### Clearing sweep data

Call `clearSwrSweepPoints()` to remove all sweep data and hide the overlay.

### Theme support

The SpotHub dialog and all its connection status labels now use theme-aware colors. The dialog container is registered as `dialog/dxCluster` for theme styling. Connection status labels use:

| State | Theme color token |
|---|---|
| Connected | `{{color.accent}}` |
| Disconnected