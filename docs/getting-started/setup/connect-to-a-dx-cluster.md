# Connect to a DX cluster

AetherSDR's SpotHub dialog lets you connect to a telnet DX cluster and show incoming spots as overlays on the panadapter. Use this page to make your first connection and optionally reconnect automatically on every launch.

## Before you start

- Know the hostname (or IP address) and telnet port of your chosen DX cluster (for example, `dxc.k0xm.net` on port `7373`).
- Know the callsign you will use to log in to the cluster.

## Steps

1. Open `Settings > SpotHub...`.
2. Click the **Cluster** tab.
3. In the **Server:** field, type the cluster hostname or IP address. This saves to `ClusterHost`.
4. In the **Port:** field, set the telnet port (1–65535). This saves to `ClusterPort`.
5. In the **Callsign:** field, type your callsign. This saves to `ClusterCallsign`.
6. Click **Connect**.
   - The status indicator changes to **Connected** and the button label changes to **Disconnect**.
   - Incoming cluster traffic appears in the **Cluster Console** read-only display.
7. To reconnect automatically every time AetherSDR starts, enable **Auto-connect on startup**. This saves to `ClusterAutoConnect`.

## What each control does

| Control | Description | Setting key |
|---|---|---|
| **Server:** | Hostname or IP address of the DX cluster telnet server. | `ClusterHost` |
| **Port:** | Telnet port. Valid range: 1–65535. | `ClusterPort` |
| **Callsign:** | Login callsign sent to the cluster on connect. | `ClusterCallsign` |
| **Connect / Disconnect** | Toggles the telnet connection. Label shows current action. | — |
| **Auto-connect on startup** | Connects to the cluster automatically when AetherSDR launches. | `ClusterAutoConnect` |
| **Cluster Console** | Read-only display of raw telnet traffic from the cluster. | — |
| **Send** (command line) | Sends a typed command to the cluster while connected. | — |
| **Spot Color:** | Opens a color picker for cluster spot overlays on the panadapter. | `ClusterSpotColor` |
| **Spots:** (Display tab) | Master toggle for DX spot overlay on the panadapter. Default: Enabled. | `IsSpotsEnabled` |
| **Memories:** (Display tab) | Toggles memory-channel overlay on the panadapter. Default: Disabled. | `IsMemorySpotsEnabled` |
| **Auto:** (Display tab) | Automatically switches the slice mode when clicking a spot that includes mode information (e.g. CW, FT8, RTTY). Default: Enabled. Setting key changed from `SpotsAutoMode` to `SpotAutoSwitchMode` in v26.5.1. | `SpotAutoSwitchMode` |
| **Signals (Signal History)** (Display tab) | Gold markers for detected voice-width signals on the panadapter. New in v26.5.1 (#2426). Same toggle as View > Signal History Markers. | `SHistoryMarkersEnabled` |
| **QRM (Signal History)** (Display tab) | Red markers for persistent carriers and wideband interference. New in v26.5.1 (#2426). Same toggle as View > QRM History Markers. | `SHistoryQrmEnabled` |
| **Clear All** (Display tab) | Clears all DX spots, memory feed, Signal History markers and QRM markers from the spectrum. | — |
| **Levels:** (Display tab) | Number of vertical stacking rows for spots (1–10). Default: 3. | `SpotsMaxLevel` |
| **Position:** (Display tab) | Vertical position on panadapter (0–100). Default: 50. | `SpotsStartingHeightPercentage` |
| **Font Size:** (Display tab) | Spot text size (8–32). Default: 16. | `SpotFontSize` |
| **Spot Lifetime:** (Display tab) | Seconds before a spot fades away (10 sec – 24 hrs, non-linear steps). | `DxClusterSpotLifetimeSec` |
| **Override Colors:** (Display tab) | Forces a single text color for all spots. | `IsSpotsOverrideColorsEnabled` |
| **Spot text color picker** (Display tab) | Opens QColorDialog to pick spot text color. Default: #FFFF00. | `SpotsOverrideColor` |
| **Override Background: Enabled** (Display tab) | Enables custom spot background color. Default: Enabled. | `IsSpotsOverrideBackgroundColorsEnabled` |
| **Override Background: Auto** (Display tab) | Auto-picks background color for contrast. Default: Enabled. | `IsSpotsOverrideToAutoBackgroundColorEnabled` |
| **Spot background color picker** (Display tab) | Opens QColorDialog for spot background color. Default: #000000. | `SpotsOverrideBgColor` |
| **Background Opacity:** (Display tab) | Opacity of spot background color (0–100). Default: 48. | `SpotsBackgroundOpacity` |
| **Spot Lines:** (Display tab) | Draws vertical lines from the spectrum up to each spot label. Disable during contests to reduce visual clutter. Default: Enabled. New in v0.9.7 (#2349). | `IsSpotsLinesEnabled` |
| **Total Spots:** (Display tab) | Live count of spots currently tracked across all sources. | — |
| **DXCC Coloring (section)** (Display tab) | Section header for DXCC coloring controls in the left column below the divider. | — |
| **DXCC Colors:** (Display tab) | Colors spots by worked/confirmed/needed DXCC status. Setting key changed from `DxccColoringEnabled` to `IsDxccColoringEnabled` in v26.5.1. | `IsDxccColoringEnabled` |
| **Log File (ADIF):** (Display tab) | Loads an ADIF log file to drive DXCC coloring. Auto-watches the file for changes after selection. Setting key changed from `DxccAdifPath` to `DxccAdifFilePath` in v26.5.1. | `DxccAdifFilePath` |
| **Imported: (DXCC stats)** (Display tab) | Shows QSO count and entity count when a log is loaded. Format: '<N> QSOs / <M> entities'. | — |
| **DXCC Color swatches (New DXCC / New Band / New Mode / Worked)** (Display tab) | Opens a color picker for each DXCC status category. New in v26.5.1 — replaces previous fixed DXCC color scheme. | `DxccColorNewEntity`, `DxccColorNewBand`, `DxccColorNewMode`, `DxccColorWorked` |
| **Signal History (section)** (Display tab) | Section header for Signal History tunables in the right column below the divider. New in v26.5.1 (#2506). | — |
| **Marker Lifetime:** (Display tab) | How long an inactive Signal History marker persists before being removed (15–300 sec). Default: 60 s. New in v26.5.1. | `SHistoryLifetimeS` |
| **QRM Gate:** (Display tab) | How long a narrow carrier or wideband signal must persist before being classified as QRM (3–30 sec). Default: 6 s. New in v26.5.1. | `SHistoryQrmGateS` |
| **Edge Threshold:** (Display tab) | Threshold above noise floor for the slope edge walk that refines the S-History carrier-side edge (1.0–10.0 dB). Default: 3.0 dB. New in v26.5.1. | `SHistorySoftEdgeDb` |
| **Signal History color swatches (Signals / QRM)** (Display tab) | Opens a color picker for the voice signal markers (gold) and QRM markers (red). New in v26.5.1. | `SHistoryColorSignals`, `SHistoryColorQrm` |
| **Snap to Step:** (Display tab) | Rounds S-History click-to-tune to the nearest multiple of the active slice's step size, hiding the small carrier offset. Default: Disabled. New in v26.5.1. | `SHistorySnapToStep` |

## Tuning to a spot by double-clicking

Double-clicking a row in the **Spot List** tab tunes the active slice to the spot's frequency. As of v0.9.7, AetherSDR also forwards mode information extracted from the spot comment, so the slice switches to the appropriate mode (for example, CW or SSB) to match the spot rather than only changing frequency.

## FreeDV Reporter reporting

The **Station Reporting** group on the **FreeDV** tab lets AetherSDR broadcast your station's activity to the public FreeDV Reporter map at qso.freedv.org while the RADE modem is active.

### Requirements

- The FreeDV tab and all reporting controls are only present in builds compiled with `HAVE_WEBSOCKETS`. On Windows, the **Enable FreeDV Reporter reporting when RADE is active** checkbox additionally requires `HAVE_RADE`.
- Both a callsign and a grid square must be resolvable before reporting can be enabled. If either is blank when you check **Enable FreeDV Reporter reporting when RADE is active**, AetherSDR shows a warning dialog and leaves the checkbox unchecked.

### Setting up reporting

1. Open `Settings > SpotHub...` and click the **FreeDV** tab.
2. In the **Station Reporting** group, confirm or enter your callsign:
   - If **Use radio** is checked (default), the **Callsign:** field is filled automatically from the radio's configured callsign and is read-only. Uncheck **Use radio** to type a different callsign.
3. Confirm or enter your grid square:
   - If **Use GPS** is checked (default, GPS-capable radios only), the **Grid Square:** field is filled from the radio's GPS and is read-only. Uncheck **Use GPS** to type a grid square manually.
4. Optionally, enter a short message in **Station Msg:** to appear beside your callsign on the map.
5. Check **Enable FreeDV Reporter reporting when RADE is active**.
   - If both callsign and grid square are present, reporting is enabled and saved to `FreeDvAutoReport`.
   - If either is missing, a warning dialog appears and the checkbox remains unchecked. Fill in the missing field and try again.

### Reporting controls

| Control | Description | Setting key |
|---|---|---|
| **Enable FreeDV Reporter reporting when RADE is active** | Master switch for public map reporting. Blocked if callsign or grid square is blank. | `FreeDvAutoReport` |
| **Callsign:** | Callsign sent to the FreeDV Reporter map. | `FreeDvMyCallsign` |
| **Use radio** | Copies the callsign from the radio and locks the field read-only. | `FreeDvUseRadioCallsign` |
| **Grid Square:** | Maidenhead locator sent to the FreeDV Reporter map. | `FreeDvMyGrid` |
| **Use GPS** | Copies the grid from the radio's GPS and locks the field read-only. Visible only on GPS-capable radio models. | `FreeDvUseGpsGrid` |
| **Station Msg:** | Optional free-text status line shown on the public map. | `FreeDvMyMessage` |

## Display tab: Auto Mode default changed

As of v0.9.5.1, the **Auto:** toggle on the **Display** tab defaults to **Enabled**. In previous releases the default was **Disabled**. `SpotAutoSwitchMode` is saved as `True` unless you have previously set it otherwise. If you preferred the old behavior, open the **Display** tab and disable **Auto:**.

## Display tab: Spot Lines (new in v0.9.7)

The **Spot Lines:** toggle on the **Display** tab controls whether AetherSDR draws a vertical line from the spectrum baseline up to each spot label on the panadapter. The toggle defaults to **Enabled** and saves to `IsSpotsLinesEnabled`.

Disable **Spot Lines:** during contests or when the panadapter is heavily populated with spots to reduce visual clutter.

## Display tab: Signal History (new in v26.5.1)

The **Display** tab now includes a **Signal History (section)** in the right column below the divider. This section consolidates all Signal History tunables:

- **Signals (Signal History)** and **QRM (Signal History)** toggles control gold and red marker visibility.
- **Marker Lifetime:** slider controls how long inactive markers persist (15–300 seconds).
- **QRM Gate:** slider sets how long a signal must persist before being classified as QRM (3–30 seconds).
- **Edge Threshold:** slider sets the dB threshold for edge refinement (1.0–10.0 dB).
- **Snap to Step:** toggle rounds click-to-tune to the nearest step size.
- Color swatches let you pick custom colors for Signals (gold) and QRM (red) markers.

## Display tab: DXCC Coloring (updated in v26.5.1)

The **Display** tab now includes a **DXCC Coloring (section)** in the left column below the divider. This section replaces the previous fixed DXCC color scheme with customizable color swatches for each DXCC status category: New DXCC, New Band, New Mode, and Worked.

The DXCC Coloring toggle and Log File (AD