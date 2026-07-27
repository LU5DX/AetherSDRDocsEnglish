# SpotHub (DX Cluster Dialog)

Central hub for connecting to DX spot sources -- DX cluster, Reverse Beacon Network, WSJT-X, SpotCollector, POTA and FreeDV -- and configuring how spots are displayed on the panadapter.

## Opening SpotHub

1. Click **Settings > SpotHub...** on the main menu.

## Connecting to a DX Cluster

1. Click the **Cluster** tab.
2. Enter the hostname in **Server:** (default: `dxc.nc7j.com`).
3. Enter the telnet port in **Port:** (default: `7373`).
4. Enter your callsign in **Callsign:**.
5. Click **Connect**. The button label changes to **Disconnect** when connected.
6. Optional: Toggle **Auto-connect on startup** to connect automatically on launch.

### Cluster Console

- View raw telnet traffic in the read-only console area.
- Type commands in the text field beside **Send** and click **Send** to transmit.

### Spot Color

- Click **Spot Color:** to open a color picker and choose a unique color for DX cluster spots on the panadapter.

## Connecting to the Reverse Beacon Network (RBN)

1. Click the **RBN** tab.
2. Enter the hostname in **Server:** (default: `telnet.reversebeacon.net`).
3. Enter the port in **Port:** (default: `7000`).
4. Enter your callsign in **Callsign:**.
5. Set the **Rate Limit:** to cap spots per second (prevents overload on busy bands).
6. Click **Connect**. The button label changes to **Disconnect** when connected.
7. Optional: Toggle **Auto-connect on startup** to connect automatically on launch.

### RBN Console

- View raw RBN traffic in the read-only console area.
- Type commands in the text field beside **Send** and click **Send** to transmit.

### RBN Spot Color

- Click **Spot Color:** to open a color picker for RBN spots.

## Receiving WSJT-X Spots

1. Click the **WSJT-X** tab.
2. Enter the UDP bind address in **Address:** (default: `127.0.0.1`).
3. Enter the UDP port in **Port:** (default: `2237`).
4. Click **Start**. The button label changes to **Stop** when listening.
5. Optional: Toggle **Auto-start on startup** to start the listener automatically on launch.

### WSJT-X Filters

Select which decodes appear as spots:

- **CQ** — Show only CQ calls.
- **CQ POTA** — Show CQ POTA calls.
- **Calling Me** — Show only decodes addressed to your callsign.

### WSJT-X Colors

Assign colors to each decode category:

- **CQ color** — Click to set color for CQ spots.
- **POTA color** — Click to set color for CQ POTA spots.
- **Calling Me color** — Click to set color for spots calling you.
- **Default color** — Click to set default color for all other spots.

### WSJT-X Decodes Console

- View decoded transmissions in the read-only area.

### Spot Life

- Use **Spot Life:** spinbox to set how many seconds WSJT-X spots remain on the panadapter (default: 60 s).

## Connecting to SpotCollector

1. Click the **SpotCollector** tab.
2. Enter the UDP port in **UDP Port:** (default: `7373`).
3. Click **Start**. The button label changes to **Stop** when listening.
4. Optional: Toggle **Auto-start on startup** to start the listener automatically on launch.

### SpotCollector Spots Console

- View received SpotCollector spots in the read-only area.

## Polling POTA Spots

1. Click the **POTA** tab.
2. The server field shows **api.pota.app (HTTP polling)** — this is fixed.
3. Set the **Poll Interval:** in seconds (default: `60`).
4. Click **Start**. The button label changes to **Stop** when polling.
5. Optional: Toggle **Auto-start on startup** to start polling automatically on launch.

### POTA Activations Console

- View the activation feed in the read-only area.

### POTA Spot Color

- Click **Spot Color:** to open a color picker for POTA spots.

## Connecting to FreeDV

1. Click the **FreeDV** tab.
2. The server field shows **qso.freedv.org (WebSocket)** — this is fixed.
3. Click **Start**. The button label changes to **Stop** when connected.
4. Optional: Toggle **Auto-start on startup** to connect automatically on launch.

### FreeDV Spots Console

- View FreeDV activity in the read-only area.

### FreeDV Spot Color

- Click **Spot Color:** to open a color picker for FreeDV spots.

## Using the Spot List

1. Click the **Spot List** tab to view all live spots in a unified, sortable table.
2. Use the **Bands:** checkboxes to filter by band (160m, 80m, 60m, 40m, 30m, 20m, 17m, 15m, 12m, 10m, 6m, 2m, etc.). Band filter checkboxes wrap to new rows when the dialog is narrow to keep labels readable.
3. Click **Clear** to empty the current spot list.
4. Double-click any row in the **Spot table** to tune your radio to that frequency.

The **Spot table** columns are:

| Column | Description |
|---|---|
| Time | Time the spot was received |
| Freq | Frequency in MHz |
| DX Call | The station being spotted |
| Comment | Spotter's comment |
| Spotter | The station that posted the spot |
| Band | Band name |
| Mode | Mode (e.g., CW, FT8, RTTY) |
| Source | Which source provided the spot (Cluster, RBN, WSJT-X, SpotCollector, POTA, FreeDV) |

### Hiding and showing table columns

Right-click the spot table header row to open a context menu where you can show or hide individual columns. The menu stays open while you toggle checkable columns, so you can show or hide several columns in one pass instead of reopening the menu for each column.

## Configuring Spot Display

1. Click the **Display** tab.
2. Use the following toggles and controls:

### Master Toggles

| Control | Default | Behavior | Setting key |
|---|---|---|---|
| **Spots:** | Enabled | Master toggle for DX spot overlay | `IsSpotsEnabled` |
| **Memories:** | Disabled | Toggles memory-channel overlay on panadapter | `IsMemorySpotsEnabled` |
| **Auto:** | Enabled | Automatically switch slice mode when clicking a spot that includes mode info (e.g., CW, FT8, RTTY) | `SpotAutoSwitchMode` |
| **Signals (Signal History)** | Disabled | Gold markers for detected voice-width signals on the panadapter | `SHistoryMarkersEnabled` |
| **QRM (Signal History)** | Disabled | Red markers for persistent carriers and wideband interference | `SHistoryQrmEnabled` |

### Global Controls

| Control | Default | Range | Behavior | Setting key |
|---|---|---|---|---|
| **Clear All** | — | — | Clears all DX spots, memory feed, Signal History markers and QRM markers from the spectrum | — |
| **Levels:** | 3 | 1–10 | Number of vertical stacking rows for spots | `SpotsMaxLevel` |
| **Position:** | 50 | 0–100 | Vertical position on panadapter | `SpotsStartingHeightPercentage` |
| **Font Size:** | 16 | 8–32 | Spot text size | `SpotFontSize` |
| **Spot Lifetime:** | — | 10 sec – 24 hrs (non-linear steps) | Seconds before a spot fades away | `DxClusterSpotLifetimeSec` |

### Color Overrides

| Control | Default | Behavior | Setting key |
|---|---|---|---|
| **Override Colors:** | Off | Forces a single text color for all spots | `IsSpotsOverrideColorsEnabled` |
| Spot text color picker | `#FFFF00` | Opens color picker to choose override text color | `SpotsOverrideColor` |
| **Override Background: Enabled** | Enabled | Enables custom spot background color | `IsSpotsOverrideBackgroundColorsEnabled` |
| **Override Background: Auto** | Enabled | Auto-picks background color for contrast | `IsSpotsOverrideToAutoBackgroundColorEnabled` |
| Spot background color picker | `#000000` | Opens color picker for spot background color | `SpotsOverrideBgColor` |
| **Background Opacity:** | 48 | 0–100 | Opacity of spot background color | `SpotsBackgroundOpacity` |

### Spot Lines

| Control | Default | Behavior | Setting key |
|---|---|---|---|
| **Spot Lines:** | Enabled | Draws vertical lines from the spectrum up to each spot label. Disable during contests to reduce visual clutter | `IsSpotsLinesEnabled` |

### Total Spots

- **Total Spots:** indicator shows the live count of spots currently tracked across all sources.

## DXCC Coloring

In the **Display** tab, the **DXCC Coloring** section controls color-coding spots based on your log.

1. Click **Load ADIF Log** to select an ADIF log file (uses `DxccAdifFilePath` setting).
2. After loading, the **Imported:** indicator shows `<N> QSOs / <M> entities`.

| Control | Default | Behavior | Setting key |
|---|---|---|---|
| **DXCC Colors:** | Off | Colors spots by worked/confirmed/needed DXCC status | `IsDxccColoringEnabled` |
| **Log File (ADIF):** | — | Opens file dialog to select an ADIF log. Auto-watches file for changes | `DxccAdifFilePath` |
| **Imported:** | (no log loaded) | Shows QSO count and entity count | — |

### DXCC Color Settings

| Control | Behavior | Setting key |
|---|---|---|
| New DXCC color swatch | Opens color picker for new entity spots | `DxccColorNewEntity` |
| New Band color swatch | Opens color picker for new band spots | `DxccColorNewBand` |
| New Mode color swatch | Opens color picker for new mode spots | `DxccColorNewMode` |
| Worked color swatch | Opens color picker for already-worked spots | `DxccColorWorked` |

## Signal History

In the **Display** tab, the **Signal History** section configures markers for voice-width signals and QRM.

| Control | Default | Range | Behavior | Setting key |
|---|---|---|---|---|
| **Signals (Signal History)** | Disabled | On/Off | Gold markers for detected voice-width signals | `SHistoryMarkersEnabled` |
| **QRM (Signal History)** | Disabled | On/Off | Red markers for persistent carriers and wideband interference | `SHistoryQrmEnabled` |
| **Marker Lifetime:** | 60 | 15–300 sec | How long an inactive Signal History marker persists before being removed | `SHistoryLifetimeS` |
| **QRM Gate:** | 6 | 3–30 sec | How long a narrow carrier or wideband signal must persist before being classified as QRM | `SHistoryQrmGateS` |
| **Edge Threshold:** | 3.0 | 1.0–10.0 dB | Threshold above noise floor for the slope edge walk that refines the S-History carrier-side edge. Lower = closer to carrier but more noise-sensitive | `SHistorySoftEdgeDb` |
| **Snap to Step:** | Disabled | On/Off | Rounds S-History click-to-tune to the nearest multiple of the active slice's step size, hiding the small carrier offset | `SHistorySnapToStep` |

### Signal History Color Settings

| Control | Default | Behavior | Setting key |
|---|---|---|---|
| Signals color swatch | `#FFC800` | Opens color picker for voice signal markers (gold) | `SHistoryColorSignals` |
| QRM color swatch | `#FF0000` | Opens color picker for QRM markers (red) | `SHistoryColorQrm` |

## Tips

- All slider controls support **left-double-click** to reset to their stored default value.
- The SpotHub dialog uses your current theme colors for status labels and tab styling. Connected status appears in the accent color, disconnected in the label color, and error messages in the danger accent color.
- The Spot List band-filter checkboxes wrap to new rows when the dialog is narrow, keeping labels readable (#4157).
- Right-click the Spot List table header to show/hide columns; the menu stays open while you toggle multiple columns in one pass (#4157).
- Snap to Step only affects clicks on Signal History markers — it does not change how the slice tunes when you click the spectrum directly.

## Troubleshooting

- **Spot List band-filter checkboxes are unreadable when the dialog is narrow** — The band-filter checkboxes now wrap to a new row when they run out of horizontal space. If they still appear compressed, drag the dialog wider.
- **Clicking a marker still tunes to the exact carrier frequency** — Make sure the **Snap to Step** toggle shows a green fill. If it's still gray, click it once to enable.

## Related

- [Toggle Signal History voice markers on the panadapter](toggle-signal-history-voice-markers-on-the-panadapter.md)
- [Adjust S-History marker lifetime, QRM gate and edge threshold](adjust-s-history-m