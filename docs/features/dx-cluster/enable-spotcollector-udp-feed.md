# SpotHub

The SpotHub dialog is the central hub for connecting to DX spot sources — DX cluster, Reverse Beacon Network, WSJT-X, SpotCollector, POTA and FreeDV — and configuring how spots are displayed on the panadapter.

## Opening the SpotHub

1. Open `Settings > SpotHub...`.

## SpotHub overview

The SpotHub dialog contains multiple tabs, each dedicated to a different spot source, plus a **Display** tab for panadapter appearance.

## Cluster tab

Connects to a traditional DX cluster via telnet.

1. Click the **Cluster** tab.
2. Enter the cluster hostname in **Server:**. This value is saved as `ClusterHost`.
3. Enter the telnet port in **Port:**. Valid range: 1–65535. This value is saved as `ClusterPort`.
4. Enter your callsign in **Callsign:**. This value is saved as `ClusterCallsign`.
5. Click **Connect**.
6. Confirm the status indicator changes to **Connected**. Raw telnet traffic appears in the **Cluster Console**.
7. To send a command, type in the command line field and click **Send**.
8. To set the spot color, click **Spot Color:** and pick a color. This value is saved as `ClusterSpotColor`.
9. To have the cluster connect automatically every time AetherSDR launches, enable **Auto-connect on startup**. This is saved as `ClusterAutoConnect`.

### Startup commands for cluster

Click **Startup Commands…** to open a dialog where you can enter one command per line. These commands are sent to the cluster server automatically after every login.

Typical commands include:
- `SET/NAME` — set your name
- `SET/QTH` — set your location
- `ACCEPT/SPOT` — configure spot filtering

Commands are stored as `DxClusterStartupCommands`.

## RBN tab

Connects to the Reverse Beacon Network via telnet with rate limiting.

1. Click the **RBN** tab.
2. Enter the RBN hostname in **Server:**. This value is saved as `RbnHost`.
3. Enter the telnet port in **Port:**. Valid range: 1–65535. This value is saved as `RbnPort`.
4. Enter your callsign in **Callsign:**. This value is saved as `RbnCallsign`.
5. Set the **Rate Limit:** to cap the number of spots per second. This value is saved as `RbnRateLimit`.
6. Click **Connect**.
7. Confirm the status indicator changes to **Connected**. Raw telnet traffic appears in the **RBN Console**.
8. To send a command, type in the command line field and click **Send**.
9. To set the spot color, click **Spot Color:** and pick a color. This value is saved as `RbnSpotColor`.
10. To have the RBN connect automatically every time AetherSDR launches, enable **Auto-connect on startup**. This is saved as `RbnAutoConnect`.

### Startup commands for RBN

Click **Startup Commands…** to open a dialog where you can enter one command per line. These commands are sent to the RBN server automatically after every login.

Commands are stored as `RbnStartupCommands`.

## WSJT-X tab

Listens for UDP broadcasts from WSJT-X and displays decoded spots.

1. Click the **WSJT-X** tab.
2. Enter the UDP bind address in **Address:**. This value is saved as `WsjtxAddress`.
3. Enter the UDP port in **Port:**. Valid range: 1–65535. This value is saved as `WsjtxPort`.
4. Click **Start**.
5. Confirm the status indicator changes to **Listening**. Decoded transmissions appear in the **WSJT-X Decodes** console.
6. To have the listener start automatically every time AetherSDR launches, enable **Auto-start on startup**. This is saved as `WsjtxAutoStart`.
7. Use the filter checkboxes to control which spots are shown:
   - **CQ** — show only CQ calls. Saved as `WsjtxFilterCQ`.
   - **CQ POTA** — show CQ POTA calls. Saved as `WsjtxFilterPOTA`.
   - **Calling Me** — show only decodes addressed to your callsign. Saved as `WsjtxFilterCallingMe`.
8. Click each color swatch to set the color for that category:
   - **CQ color** — `WsjtxColorCQ`
   - **POTA color** — `WsjtxColorPOTA`
   - **Calling Me color** — `WsjtxColorCallingMe`
   - **Default color** — `WsjtxColorDefault`
9. Set **Spot Life:** to control how many seconds WSJT-X spots remain on the panadapter. This value is saved as `WsjtxSpotLife`.

## SpotCollector tab

Receives DX spots broadcast by Ham Radio Deluxe's SpotCollector over UDP.

1. Click the **SpotCollector** tab.
2. Set **UDP Port:** to the port SpotCollector is broadcasting on. Valid range: 1–65535. This value is saved as `SpotCollectorPort`.
3. Click **Start**.
4. Confirm the status indicator changes to **Listening**. Incoming spots appear in the **SpotCollector Spots** console as they arrive.
5. To have the listener start automatically every time AetherSDR launches, enable **Auto-start on startup**. This is saved as `SpotCollectorAutoStart`.

## POTA tab

Polls api.pota.app for current Parks on the Air activations.

1. Click the **POTA** tab.
2. The **Server:** indicator shows `api.pota.app (HTTP polling)`.
3. Set **Poll Interval:** to control how many seconds between polls. This value is saved as `PotaPollInterval`.
4. Click **Start**.
5. Confirm the status indicator changes to **Polling**. The activation feed appears in the **POTA Activations** console.
6. To set the spot color, click **Spot Color:** and pick a color. This value is saved as `PotaSpotColor`.
7. To have the polling start automatically every time AetherSDR launches, enable **Auto-start on startup**. This is saved as `PotaAutoStart`.

## FreeDV tab

Connects to a WebSocket feed of FreeDV QSO reporter spots.

1. Click the **FreeDV** tab.
2. The **Server:** indicator shows `qso.freedv.org (WebSocket)`.
3. Click **Start**.
4. Confirm the status indicator changes to **Connected**. FreeDV activity appears in the **FreeDV Spots** console.
5. To set the spot color, click **Spot Color:** and pick a color. This value is saved as `FreeDvSpotColor`.
6. To have the connection start automatically every time AetherSDR launches, enable **Auto-start on startup**. This is saved as `FreeDvAutoStart`.

### FreeDV Reporter reporting

The **FreeDV** tab also contains station reporting controls that broadcast your activity to the public FreeDV Reporter map.

#### Requirements before enabling

- A valid callsign must be available — either from the radio (when **Use radio** is checked) or typed into the **Callsign:** field.
- A valid Maidenhead grid square must be available — either from the radio's GPS module (when **Use GPS** is checked, on supported hardware) or typed into the **Grid Square:** field.

If either value is missing when you attempt to enable reporting, AetherSDR displays a warning and leaves the checkbox unchecked.

#### Steps to enable reporting

1. Click the **FreeDV** tab.
2. In the station reporting section, confirm the **Callsign:** field shows your callsign.
   - If **Use radio** is checked, the field is populated automatically from the radio's configured callsign and is read-only. Uncheck **Use radio** to enter a callsign manually.
3. Confirm the **Grid Square:** field shows your Maidenhead locator.
   - On radios with GPS hardware, check **Use GPS** to populate it automatically. Uncheck **Use GPS** to type a grid square manually.
4. Optionally enter a short message in **Station Msg:** — it appears beside your callsign on the map.
5. Check **Enable FreeDV Reporter reporting when RADE is active**.
   - If either the callsign or grid square is blank, a warning dialog appears. Fill in the missing value and try again.
6. Reporting is now active whenever the RADE modem is running.

## Spot List tab

Displays a unified, searchable table of all live spots from all sources.

1. Click the **Spot List** tab.
2. Use the **Bands:** checkboxes to toggle visibility in the table. One checkbox per band (160m, 80m, 60m, 40m, 30m, 20m, 17m, 15m, 12m, 10m, 6m, 2m, etc.).
3. Click **Clear** to empty the current spot list.
4. The **Spot table** shows all spots with columns: Time, Freq, DX Call, Comment, Spotter, Band, Mode, Source. Double-click any row to tune the active slice to that frequency. AetherSDR reads the mode hint from the spot comment and switches the slice to the correct mode at the same time.

## Display tab

Controls how spots appear on the panadapter, plus Signal History markers and DXCC coloring.

1. Click the **Display** tab.

### Top toggle row

| Toggle | Description | Setting key |
|--------|-------------|-------------|
| **Spots:** | Master toggle for DX spot overlay. Default is **Enabled**. | `IsSpotsEnabled` |
| **Memories:** | Toggles memory-channel overlay on panadapter. Default is **Disabled**. | `IsMemorySpotsEnabled` |
| **Auto:** | Automatically switches slice mode when clicking a spot that includes mode info (e.g. CW, FT8, RTTY). Default is **Enabled**. | `SpotAutoSwitchMode` |
| **Signals** | Gold markers for detected voice-width signals on the panadapter. Default is **Disabled**. Same toggle as View > Signal History Markers. | `SHistoryMarkersEnabled` |
| **QRM** | Red markers for persistent carriers and wideband interference. Default is **Disabled**. Same toggle as View > QRM History Markers. | `SHistoryQrmEnabled` |
| **Clear All** | Clears all DX spots, memory feed, Signal History markers and QRM markers from the spectrum. | — |

### Common sliders

| Slider | Description | Setting key |
|--------|-------------|-------------|
| **Levels:** | Number of vertical stacking rows for spots. Range 1–10, default 3. | `SpotsMaxLevel` |
| **Position:** | Vertical position on panadapter. Range 0–100, default 50. | `SpotsStartingHeightPercentage` |
| **Font Size:** | Spot text size. Range 8–32, default 16. | `SpotFontSize` |
| **Spot Lifetime:** | Seconds before a spot fades away. Non-linear steps from 10 sec to 24 hrs. | `DxClusterSpotLifetimeSec` |

### Override colors section

| Control | Description | Setting key |
|---------|-------------|-------------|
| **Override Colors:** | Forces a single text color for all spots. | `IsSpotsOverrideColorsEnabled` |
| Spot text color picker | Opens QColorDialog to pick spot text color. Default #FFFF00. | `SpotsOverrideColor` |
| **Override Background: Enabled** | Enables custom spot background color. Default **Enabled**. | `IsSpotsOverrideBackgroundColorsEnabled` |
| **Override Background: Auto** | Auto-picks background color for contrast. Default **Enabled**. | `IsSpotsOverrideToAutoBackgroundColorEnabled` |
| Spot background color picker | Opens QColorDialog for spot background color. Default #000000. | `SpotsOverrideBgColor` |
| **Background Opacity:** | Opacity of spot background color. Range 0–100, default 48. | `SpotsBackgroundOpacity` |
| **Spot Lines:** | Draws vertical lines from the spectrum up to each spot label. Disable during contests to reduce visual clutter. Default **Enabled**. | `IsSpotsLinesEnabled` |
| **Total Spots:** | Live count of spots currently tracked across all sources. | — |

### DXCC Coloring section

Controls in the left column below the divider.

| Control | Description | Setting key |
|---------|-------------|-------------|
| **DXCC Colors:** | Colors spots by worked/confirmed/needed DXCC status. | `IsDxccColoringEnabled` |
| **Log File (ADIF):** | Loads an ADIF log file to drive DXCC coloring. Auto-watches the file for changes after selection. Auto-Reload is always enabled when a file is selected. | `DxccAdifFilePath` |
| **Imported:** | Shows QSO count and entity count when a log is loaded. Format: '<N> QSOs / <M> entities'. | — |
| **DXCC Color swatches (New DXCC / New Band / New Mode / Worked)** | Opens a color picker for each DXCC status category. | `DxccColorNewEntity` / `DxccColorNewBand` / `DxccColorNewMode` / `DxccColorWorked` |

### Signal History section

Controls in the right column below the divider.

| Control | Description | Setting key |
|---------|-------------|-------------|
| **Marker Lifetime:** | How long an inactive Signal History marker persists before being removed. Slider, range 15–300