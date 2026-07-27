# SpotHub Dialog

The SpotHub dialog is the central hub for connecting to DX spot sources and configuring how spots are displayed on the panadapter.

## Opening SpotHub

Select `Settings > SpotHub...` from the main menu.

## Spot Sources

SpotHub supports multiple spot sources, each on its own tab:

- **Cluster** — DX cluster telnet connection
- **RBN** — Reverse Beacon Network telnet source with rate limiting
- **WSJT-X** — UDP listener for WSJT-X decodes
- **SpotCollector** — UDP listener for Ham Radio Deluxe SpotCollector broadcasts
- **POTA** — HTTP polling of api.pota.app for current activations
- **FreeDV** — WebSocket feed of FreeDV QSO reporter spots (build-gated by WebSocket support)

### Cluster Tab

| Control | Description |
|---------|-------------|
| **Server:** | Hostname of DX cluster to connect to |
| **Port:** | Telnet port on DX cluster (1-65535) |
| **Callsign:** | Login callsign sent to cluster |
| **Connect / Disconnect** | Toggles telnet connection to the cluster |
| **Auto-connect on startup** | Auto-connects cluster on launch |
| **Cluster Console** | Read-only telnet console of raw cluster traffic |
| **Send** | Sends a typed command to the cluster |
| **Spot Color:** | Opens a color picker for cluster spots |

### RBN Tab

| Control | Description |
|---------|-------------|
| **Server:** | RBN telnet hostname |
| **Port:** | RBN telnet port (1-65535) |
| **Callsign:** | Login callsign to RBN |
| **Rate Limit:** | Caps RBN spots per second |
| **Connect / Disconnect** | Toggles RBN connection |
| **Auto-connect on startup** | Starts RBN automatically |
| **RBN Console** | Read-only console of RBN traffic |
| **Send** | Sends command to RBN |
| **Spot Color:** | Color picker for RBN spots |

### WSJT-X Tab

| Control | Description |
|---------|-------------|
| **Address:** | UDP bind address for WSJT-X messages |
| **Port:** | UDP port for WSJT-X (1-65535) |
| **Start / Stop** | Starts or stops UDP listener |
| **Auto-start on startup** | Auto-starts listener on launch |
| **CQ** | Show only CQ calls from WSJT-X |
| **CQ POTA** | Show CQ POTA calls |
| **Calling Me** | Show only decodes addressed to your callsign |
| **CQ color / POTA color / Calling Me color / Default color** | Color pickers for each WSJT-X spot category |
| **WSJT-X Decodes** | Console of decoded transmissions |
| **Spot Life:** | Seconds WSJT-X spots remain on panadapter |

### SpotCollector Tab

| Control | Description |
|---------|-------------|
| **UDP Port:** | UDP port SpotCollector broadcasts on (1-65535) |
| **Start / Stop** | Starts or stops UDP listener |
| **Auto-start on startup** | Auto-starts listener on launch |
| **SpotCollector Spots** | Console of received SpotCollector spots |

### POTA Tab

| Control | Description |
|---------|-------------|
| **Server:** | Fixed indicator showing `api.pota.app (HTTP polling)` |
| **Poll Interval:** | Seconds between POTA polls |
| **Start / Stop** | Starts or stops POTA polling |
| **Auto-start on startup** | Auto-starts POTA on launch |
| **POTA Activations** | Console of activation feed |
| **Spot Color:** | Color picker for POTA spots |

### FreeDV Tab

| Control | Description |
|---------|-------------|
| **Server:** | Fixed indicator showing `qso.freedv.org (WebSocket)` |
| **Start / Stop** | Connects or disconnects the FreeDV WebSocket |
| **Auto-start on startup** | Auto-starts FreeDV on launch |
| **FreeDV Spots** | Console of FreeDV activity |
| **Spot Color:** | Color picker for FreeDV spots |

## Spot List Tab

Displays a unified, searchable table of all live spots from every connected source.

| Control | Description |
|---------|-------------|
| **Bands:** | Per-band checkboxes toggle visibility in table. One checkbox per band (160m, 80m, 60m, 40m, 30m, 20m, 17m, 15m, 12m, 10m, 6m, 2m, etc.). Checkboxes use a wrap layout so they remain readable even when the dialog is narrow. |
| **Clear** | Empties current spot list |
| **Spot table** | Sortable table of spots. Double-click a row to tune. Columns: Time, Freq, DX Call, Comment, Spotter, Band, Mode, Source. Right-click column headers to show or hide individual columns. |

### Changing Visible Columns

1. Right-click any column header in the spot table.
2. A menu appears with checkable entries for each column.
3. Click a checkable entry to toggle that column's visibility. The menu remains open so you can toggle multiple columns in one pass.
4. Click outside the menu or press Escape to close the menu when done.

## Display Tab

Configures panadapter spot visualization, Signal History tunables, and DXCC coloring.

### Toggle Row

| Control | Description |
|---------|-------------|
| **Spots:** | Master toggle for DX spot overlay. Enabled by default. |
| **Memories:** | Toggles memory-channel overlay on panadapter. Disabled by default. |
| **Auto:** | Automatically switch slice mode when clicking a spot that includes mode info (e.g. CW, FT8, RTTY). Enabled by default. |
| **Signals** | Gold markers for detected voice-width signals on the panadapter. Disabled by default. |
| **QRM** | Red markers for persistent carriers and wideband interference. Disabled by default. |
| **Clear All** | Clears all DX spots, memory feed, Signal History markers and QRM markers from the spectrum. |

### Sliders

| Control | Range | Default | Description |
|---------|-------|---------|-------------|
| **Levels:** | 1-10 | 3 | Number of vertical stacking rows for spots |
| **Position:** | 0-100 | 50 | Vertical position on panadapter |
| **Font Size:** | 8-32 | 16 | Spot text size |
| **Spot Lifetime:** | 10 sec – 24 hrs (non-linear steps) | — | Seconds before a spot fades away |

### Override Colors

| Control | Description |
|---------|-------------|
| **Override Colors:** | Forces a single text color for all spots. Disabled by default. |
| **Spot text color picker** | Opens color picker for spot text color. Default: `#FFFF00` (yellow). |
| **Override Background: Enabled** | Enables custom spot background color. Enabled by default. |
| **Override Background: Auto** | Auto-picks background color for contrast. Enabled by default. |
| **Spot background color picker** | Opens color picker for spot background color. Default: `#000000` (black). |
| **Background Opacity:** | Opacity of spot background color. Range: 0-100. Default: 48. |
| **Spot Lines:** | Draws vertical lines from the spectrum up to each spot label. Disable during contests to reduce visual clutter. Enabled by default. |

### Total Spots

Displays live count of spots currently tracked across all sources.

### DXCC Coloring Section

Controls in the left column below the divider.

| Control | Description |
|---------|-------------|
| **DXCC Colors:** | Colors spots by worked/confirmed/needed DXCC status. Disabled by default. |
| **Log File (ADIF):** | Loads an ADIF log file to drive DXCC coloring. Auto-watches the file for changes after selection. |
| **Imported:** | Shows QSO count and entity count when a log is loaded. Format: `<N> QSOs / <M> entities`. |
| **DXCC Color swatches** | Color pickers for each DXCC status category: New DXCC, New Band, New Mode, Worked |

### Signal History Section

Controls in the right column below the divider.

| Control | Range | Default | Description |
|---------|-------|---------|-------------|
| **Marker Lifetime:** | 15-300 sec | 60 | How long an inactive Signal History marker persists before being removed |
| **QRM Gate:** | 3-30 sec | 6 | How long a narrow carrier or wideband signal must persist before being classified as QRM |
| **Edge Threshold:** | 1.0-10.0 dB | 3.0 | Threshold above noise floor for the slope edge walk that refines the S-History carrier-side edge |
| **Signal History color swatches** | — | #FFC800 / #FF0000 | Color pickers for voice signal markers (gold) and QRM markers (red) |
| **Snap to Step:** | — | Disabled | Rounds S-History click-to-tune to the nearest multiple of the active slice's step size, hiding the small carrier offset |

## Status Indicators

| Indicator | Possible States | Meaning |
|-----------|----------------|---------|
| Status (each source) | Disconnected, Connected, Stopped, Listening, Polling | Current connection/listener state for each source |
| Total spots count | — | Total spots currently tracked across all sources |
| DXCC stats | — | Imported QSO and entity count from ADIF log when DXCC coloring is enabled. Format: `<N> QSOs / <M> entities`. |

## Related

- [Toggle Signal History voice markers on the panadapter](toggle-signal-history-voice-markers-on-the-panadapter.md)
- [Toggle QRM markers to see persistent carriers and interference](toggle-qrm-markers-to-see-persistent-carriers-and-interference.md)
- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
- [Start WSJT-X UDP listener and filter for CQ, POTA or calls to me](start-wsjt-x-udp-listener-and-filter-for-cq-pota-or-calls-to-me.md)
- [Connect to a DX cluster](../../getting-started/setup/connect-to-a-dx-cluster.md)