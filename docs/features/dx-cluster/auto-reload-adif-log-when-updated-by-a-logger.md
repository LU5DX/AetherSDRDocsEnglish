# SpotHub

The SpotHub dialog (`Settings > SpotHub...`) is the central hub for connecting to DX spot sources and configuring how spots are displayed on the panadapter.

## Opening SpotHub

1. Open `Settings > SpotHub...`.

The dialog remembers its size and position between sessions. The dialog has a minimum width of 360 pixels, so it can be narrowed to just the Spot List tab's visible-column width once columns are hidden.

## Source tabs

### Cluster (tab)

The Cluster tab provides a telnet connection to a DX cluster.

1. In the `Server:` field, enter the hostname of the DX cluster.
2. In the `Port:` field, enter the telnet port (1-65535).
3. In the `Callsign:` field, enter your login callsign.
4. Click `Connect` to establish the telnet connection. The button label changes to `Disconnect` while connected.
5. Optionally, enable `Auto-connect on startup` to connect automatically on launch.

The `Cluster Console` shows raw telnet traffic. Type commands in the input field and click `Send` to send them to the cluster.

Click `Spot Color:` to open a color picker for cluster spots.

Click `Startup Commands…` to edit commands sent automatically after every login. One command per line — for example:
- `SET/NAME`
- `SET/QTH`
- `ACCEPT/SPOT`

### RBN (tab)

The RBN tab connects to the Reverse Beacon Network via telnet with rate limiting.

1. In the `Server:` field, enter the RBN telnet hostname.
2. In the `Port:` field, enter the telnet port.
3. In the `Callsign:` field, enter your login callsign.
4. In the `Rate Limit:` field, set the maximum spots per second.
5. Click `Connect` to establish the telnet connection.
6. Optionally, enable `Auto-connect on startup` to connect automatically on launch.

The `RBN Console` shows raw telnet traffic. Type commands in the input field and click `Send` to send them to the RBN server.

Click `Spot Color:` to open a color picker for RBN spots.

Click `Startup Commands…` to edit commands sent automatically after every login (independent from the Cluster tab commands). One command per line.

### WSJT-X (tab)

The WSJT-X tab listens for UDP broadcasts from WSJT-X.

1. In the `Address:` field, enter the UDP bind address for WSJT-X messages.
2. In the `Port:` field, enter the UDP port.
3. Click `Start` to begin listening. The button label changes to `Stop` while listening.
4. Optionally, enable `Auto-start on startup` to start the listener automatically on launch.

Use the filter checkboxes to control which decodes appear:
- **CQ** — Show only CQ calls.
- **CQ POTA** — Show only CQ POTA calls.
- **Calling Me** — Show only decodes addressed to your callsign.

Click a color swatch to open a color picker for each WSJT-X spot category (CQ color, POTA color, Calling Me color, Default color).

Set `Spot Life:` to control how many seconds WSJT-X spots remain on the panadapter.

### SpotCollector (tab)

The SpotCollector tab listens for UDP broadcasts from Ham Radio Deluxe SpotCollector.

1. In the `UDP Port:` field, enter the port SpotCollector broadcasts on.
2. Click `Start` to begin listening. The button label changes to `Stop` while listening.
3. Optionally, enable `Auto-start on startup` to start the listener automatically on launch.

### POTA (tab)

The POTA tab polls api.pota.app for current activations.

1. In the `Poll Interval:` field, set the seconds between polls.
2. Click `Start` to begin polling. The button label changes to `Stop` while polling.
3. Optionally, enable `Auto-start on startup` to start polling automatically on launch.

Click `Spot Color:` to open a color picker for POTA spots.

### FreeDV (tab)

The FreeDV tab connects to the FreeDV QSO reporter WebSocket feed at qso.freedv.org. This tab is only available when the build includes WebSocket support.

1. Click `Start` to connect to the FreeDV WebSocket. The button label changes to `Stop` while connected.
2. Optionally, enable `Auto-start on startup` to connect automatically on launch.

Click `Spot Color:` to open a color picker for FreeDV spots.

### Station Reporting

The **Station Reporting** group inside the FreeDV tab lets AetherSDR broadcast your station's activity to the public FreeDV Reporter map at qso.freedv.org whenever the RADE modem is active.

#### Requirements

- The build must include WebSocket support (`HAVE_WEBSOCKETS`). On Windows, `HAVE_RADE` is also required.
- Both a callsign and a grid square must resolve to non-empty values before the `Enable FreeDV Reporter reporting when RADE is active` checkbox can be turned on.

#### How callsign and grid are resolved

When you enable reporting, AetherSDR resolves the callsign and grid in the following order:

**Callsign**
1. If `Use radio` is checked and the radio has a configured callsign, that callsign is used.
2. Otherwise, the value typed in `Callsign:` is used.

**Grid square**
1. If `Use GPS` is checked, the radio has GPS hardware, and a GPS-derived grid is available, that grid is used.
2. Otherwise, the value typed in `Grid Square:` is used.

If either value is empty after resolution, a warning dialog appears and the checkbox reverts to unchecked. This prevents blank or placeholder values (such as `N0CALL` or `AA00`) from being broadcast to the shared public map.

#### Setting up reporting

1. Open `Settings > SpotHub...`.
2. Click the `FreeDV` tab.
3. In the **Station Reporting** group, confirm the callsign field shows the correct callsign.
   - If `Use radio` is checked, the field is populated from the radio's configured callsign and is read-only. Uncheck `Use radio` to enter a callsign manually.
4. Confirm the grid square field shows a valid Maidenhead locator.
   - If `Use GPS` is checked (visible only on radios with GPS hardware), the field is populated from the GPS module and is read-only. Uncheck `Use GPS` to enter a grid manually.
5. Optionally, enter a short message in `Station Msg:`. This text appears beside your callsign on the public map.
6. Check `Enable FreeDV Reporter reporting when RADE is active`.
   - If either the callsign or grid is empty, a warning appears and the checkbox remains unchecked. Fill in the missing field and try again.

AetherSDR saves the setting to `FreeDvAutoReport` and begins reporting to qso.freedv.org whenever the RADE modem is active.

### Spot List (tab)

The Spot List tab shows a unified searchable table of all live spots.

1. Use the per-band checkboxes to toggle visibility of spots on each band (160m, 80m, 60m, 40m, 30m, 20m, 17m, 15m, 12m, 10m, 6m, 2m, etc.). The band checkboxes use a flow layout that wraps to a new row when the dialog is narrowed, keeping the labels readable instead of compressing them.
2. Click `Clear` to empty the current spot list.
3. Double-click a row in the table to tune the active slice to the spot's frequency. If mode information is present in the spot comment and `Auto:` is enabled on the Display tab, the slice switches to that mode automatically.

The table columns are: Time, Freq, DX Call, Comment, Spotter, Band, Mode, Source.

Right-click any column header to show or hide individual columns. The header menu stays open while checkable columns are toggled (for example, hide "Band" and "Mode" in one pass instead of reopening the menu for each). Click a non-checkable area or press Escape to dismiss the menu.

### Display (tab)

The Display tab controls panadapter spot-visualization, Signal History tunables, and DXCC coloring.

#### Master toggles

| Control | Description | Setting Key |
|---------|-------------|-------------|
| `Spots:` | Master toggle for DX spot overlay. The button always shows "Enabled". | `IsSpotsEnabled` |
| `Memories:` | Toggles memory-channel overlay on panadapter. | `IsMemorySpotsEnabled` |
| `Auto:` | Automatically switch slice mode when clicking a spot that includes mode info (e.g. CW, FT8, RTTY). | `SpotAutoSwitchMode` |
| `Signals` (Signal History) | Gold markers for detected voice-width signals on the panadapter. | `SHistoryMarkersEnabled` |
| `QRM` (Signal History) | Red markers for persistent carriers and wideband interference. | `SHistoryQrmEnabled` |
| `Clear All` | Clears all DX spots, memory feed, Signal History markers and QRM markers from the spectrum. | — |

#### Spot appearance

| Control | Description | Setting Key |
|---------|-------------|-------------|
| `Levels:` | Number of vertical stacking rows for spots (1-10). | `SpotsMaxLevel` |
| `Position:` | Vertical position on panadapter (0-100). | `SpotsStartingHeightPercentage` |
| `Font Size:` | Spot text size (8-32). | `SpotFontSize` |
| `Spot Lifetime:` | Seconds before a spot fades away (10 sec – 24 hrs, non-linear steps). | `DxClusterSpotLifetimeSec` |

#### Color overrides

| Control | Description | Setting Key |
|---------|-------------|-------------|
| `Override Colors:` | Forces a single text color for all spots. The button always shows "Enabled". | `IsSpotsOverrideColorsEnabled` |
| Spot text color picker | Opens QColorDialog to pick spot text color. | `SpotsOverrideColor` |
| `Override Background: Enabled` | Enables custom spot background color. | `IsSpotsOverrideBackgroundColorsEnabled` |
| `Override Background: Auto` | Auto-picks background color for contrast. | `IsSpotsOverrideToAutoBackgroundColorEnabled` |
| Spot background color picker | Opens QColorDialog for spot background color. | `SpotsOverrideBgColor` |
| `Background Opacity:` | Opacity of spot background color (0-100). | `SpotsBackgroundOpacity` |
| `Spot Lines:` | Draws vertical lines from the spectrum up to each spot label. The button always shows "Enabled". Disable during contests to reduce visual clutter. | `IsSpotsLinesEnabled` |

#### DXCC Coloring (section)

The left column below the divider.

| Control | Description | Setting Key |
|---------|-------------|-------------|
| `DXCC Colors:` | Colors spots by worked/confirmed/needed DXCC status. The button always shows "Enabled". | `IsDxccColoringEnabled` |
| `Log File (ADIF):` | Loads an ADIF log file to drive DXCC coloring. Auto-watches the file for changes after selection. | `DxccAdifFilePath` |
| `Imported:` | Shows QSO count and entity count when a log is loaded. Format: `<N> QSOs / <M> entities`. | — |
| DXCC Color swatches (New DXCC / New Band / New Mode / Worked) | Opens a color picker for each DXCC status category. | `DxccColorNewEntity / DxccColorNewBand / DxccColorNewMode / DxccColorWorked` |

#### Signal History (section)

The right column below the divider.

| Control | Description | Setting Key |
|---------|-------------|-------------|
| `Marker Lifetime:` | How long an inactive Signal History marker persists before being removed (15-300 sec). Default 60 s. | `SHistoryLifetimeS` |
| `QRM Gate:` | How long a narrow carrier or wideband signal must persist before being classified as QRM (3-30 sec). Default 6 s. | `SHistoryQrmGateS` |
| `Edge Threshold:` | Threshold above noise floor for the slope edge walk that refines the S-History carrier-side edge (1.0-10.0 dB). Default 3.0 dB. | `SHistorySoftEdgeDb` |
| Signal History color swatches (Signals / QRM) | Opens a color picker for the voice signal markers (gold) and QRM markers (red). Defaults: #FFC800 / #FF0000. | `SHistoryColorSignals / SHistoryColorQrm` |
| `Snap to Step:` | Rounds S-History click-to-tune to the nearest multiple of the active slice's step size, hiding the small carrier offset. The button always shows "Enabled". Default Disabled. | `SHistorySnapToStep` |

#### Indicator

`Total Spots:` shows the live count of spots currently tracked across all sources.

## Auto-reload ADIF log when updated by a logger

When DXCC coloring is enabled, AetherSDR reads your ADIF log once at startup. Auto-reload tells AetherSDR to re-read the file whenever your logging software updates it, so worked/confirmed/needed coloring on the panadapter stays current without manual intervention.

### Before you start

- DXCC coloring must be enabled and an ADIF log file must already be loaded. See [Enable DXCC coloring from an ADIF log](enable-dxcc-coloring-from-an-ad