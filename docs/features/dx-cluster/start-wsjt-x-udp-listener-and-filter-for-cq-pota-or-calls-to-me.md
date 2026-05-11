# Start WSJT-X UDP Listener and Filter for CQ, POTA or Calls to Me

Configure AetherSDR to receive decoded transmissions from WSJT-X over UDP and show only the spot categories you care about — CQ calls, POTA activations, or stations calling your callsign — as overlays on the panadapter.

## Before you start

- WSJT-X must be running on the same machine or network and configured to send UDP status messages to the address and port you will set here.
- Know the UDP address and port WSJT-X is broadcasting to (check WSJT-X under **File > Settings > Reporting**, UDP Server section).
- Your callsign must be set in WSJT-X for the "Calling Me" filter to work.

## Steps

1. Open `Settings > SpotHub...`.
2. Click the **WSJT-X** tab.
3. In **Address:**, enter the UDP bind address AetherSDR should listen on (stored as `WsjtxAddress`). Use `127.0.0.1` if WSJT-X runs on the same machine, or `0.0.0.0` to listen on all interfaces.
4. In **Port:**, enter the UDP port number that matches the port configured in WSJT-X (stored as `WsjtxPort`; valid range 1–65535).
5. Click **Start**. The status indicator changes to **Listening**.
6. To start the listener automatically every time AetherSDR launches, enable **Auto-start on startup (WSJT-X)** (stored as `WsjtxAutoStart`).
7. Under the filter checkboxes, enable one or more of the following to restrict which decodes appear as panadapter spots:
   - **CQ** — shows stations sending a general CQ call (stored as `WsjtxFilterCQ`).
   - **CQ POTA** — shows stations sending CQ POTA (stored as `WsjtxFilterPOTA`).
   - **Calling Me** — shows decodes addressed to your callsign (stored as `WsjtxFilterCallingMe`).
8. Optionally assign a distinct color to each category by clicking the corresponding color button:
   - **CQ color** (stored as `WsjtxColorCQ`)
   - **POTA color** (stored as `WsjtxColorPOTA`)
   - **Calling Me color** (stored as `WsjtxColorCallingMe`)
   - **Default color** for decodes that pass no active filter (stored as `WsjtxColorDefault`)
9. Set **Spot Life:** to the number of seconds a WSJT-X spot should remain visible on the panadapter (stored as `WsjtxSpotLife`).
10. Confirm decoded transmissions are arriving in the **WSJT-X Decodes** console at the bottom of the tab.

## What each control does

| Control                                                       | Behavior                                                                                                                                                               | Setting key                                                                                                        |
|---------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| **Address:**                                                  | UDP bind address for incoming WSJT-X messages.                                                                                                                         | `WsjtxAddress`                                                                                                     |
| **Port:**                                                     | UDP port number. Must match WSJT-X reporting port.                                                                                                                     | `WsjtxPort`                                                                                                        |
| **Start / Stop**                                              | Starts or stops the UDP listener.                                                                                                                                      | —                                                                                                                  |
| **Auto-start on startup (WSJT-X)**                            | Starts the listener automatically on launch.                                                                                                                           | `WsjtxAutoStart`                                                                                                   |
| **CQ**                                                        | Passes only CQ transmissions to the panadapter.                                                                                                                        | `WsjtxFilterCQ`                                                                                                    |
| **CQ POTA**                                                   | Passes only CQ POTA transmissions.                                                                                                                                     | `WsjtxFilterPOTA`                                                                                                  |
| **Calling Me**                                                | Passes only decodes addressed to your callsign.                                                                                                                        | `WsjtxFilterCallingMe`                                                                                             |
| **CQ color**                                                  | Color for CQ spots on the panadapter.                                                                                                                                  | `WsjtxColorCQ`                                                                                                     |
| **POTA color**                                                | Color for CQ POTA spots.                                                                                                                                               | `WsjtxColorPOTA`                                                                                                   |
| **Calling Me color**                                          | Color for spots calling your callsign.                                                                                                                                 | `WsjtxColorCallingMe`                                                                                              |
| **Default color**                                             | Color for spots that match no active filter.                                                                                                                           | `WsjtxColorDefault`                                                                                                |
| **Spot Life:**                                                | Seconds a WSJT-X spot remains on the panadapter before fading.                                                                                                         | `WsjtxSpotLife`                                                                                                    |
| **WSJT-X Decodes**                                            | Read-only console showing decoded transmissions as they arrive.                                                                                                        | —                                                                                                                  |
| **Spots:**                                                    | Master toggle for DX spot overlay on the panadapter. Default: Enabled.                                                                                                 | `IsSpotsEnabled`                                                                                                   |
| **Spot Lines:**                                               | Draws vertical lines from the spectrum up to each spot label. Disable during contests to reduce visual clutter. Default: Enabled.                                      | `IsSpotsLinesEnabled`                                                                                              |
| Total Spots:                                                  | Live readout of how many spots are currently tracked across all sources. Resets to 0 when **Clear All Spots** is pressed.                                              | —                                                                                                                  |
| **Auto:**                                                     | Automatically switch slice mode when clicking a spot that includes mode info (e.g. CW, FT8, RTTY). Default: Enabled.                                                   | `SpotAutoSwitchMode` (changed from `SpotsAutoMode` in v26.5.1)                                                     |
| **Signals (Signal History)**                                  | Gold markers for detected voice-width signals on the panadapter. Default: Disabled.                                                                                    | `SHistoryMarkersEnabled` (new in v26.5.1, same toggle as View > Signal History Markers)                            |
| **QRM (Signal History)**                                      | Red markers for persistent carriers and wideband interference. Default: Disabled.                                                                                      | `SHistoryQrmEnabled` (new in v26.5.1, same toggle as View > QRM History Markers)                                  |
| **Clear All**                                                 | Clears all DX spots, memory feed, Signal History markers and QRM markers from the spectrum.                                                                            | —                                                                                                                  |
| **Levels:**                                                   | Number of vertical stacking rows for spots. Default: 3. Valid range: 1–10.                                                                                             | `SpotsMaxLevel` (migrated from `SpotsStackLevels` in v0.9.7)                                                      |
| **Position:**                                                 | Vertical position on panadapter. Default: 50. Valid range: 0–100.                                                                                                      | `SpotsStartingHeightPercentage` (migrated from `SpotsPosition` in v0.9.7)                                          |
| **Font Size:**                                                | Spot text size. Default: 16. Valid range: 8–32.                                                                                                                        | `SpotFontSize` (migrated from `SpotsFontSize` in v0.9.7)                                                           |
| **Spot Lifetime:**                                            | Seconds before a spot fades away. Valid range: 10 sec – 24 hrs (non-linear steps).                                                                                     | `DxClusterSpotLifetimeSec` (migrated from `SpotsLifetime` in v0.9.7, migrates old minutes-based key)               |
| **Override Colors:**                                          | Forces a single text color for all spots.                                                                                                                              | `IsSpotsOverrideColorsEnabled`                                                                                     |
| **Spot text color picker**                                    | Opens QColorDialog to pick spot text color. Default: `#FFFF00`.                                                                                                        | `SpotsOverrideColor`                                                                                               |
| **Override Background: Enabled**                              | Enables custom spot background color. Default: Enabled.                                                                                                                | `IsSpotsOverrideBackgroundColorsEnabled`                                                                           |
| **Override Background: Auto**                                 | Auto-picks background color for contrast. Default: Enabled.                                                                                                            | `IsSpotsOverrideToAutoBackgroundColorEnabled`                                                                      |
| **Spot background color picker**                              | Opens QColorDialog for spot background color. Default: `#000000`.                                                                                                      | `SpotsOverrideBgColor`                                                                                             |
| **Background Opacity:**                                       | Opacity of spot background color. Default: 48. Valid range: 0–100.                                                                                                     | `SpotsBackgroundOpacity` (migrated from `SpotsOverrideBgOpacity` in v0.9.7)                                        |
| **DXCC Colors:**                                              | Colors spots by worked/confirmed/needed DXCC status.                                                                                                                   | `IsDxccColoringEnabled` (changed from `DxccColoringEnabled` in v26.5.1)                                            |
| **Log File (ADIF):**                                          | Loads an ADIF log file to drive DXCC coloring. Auto-watches the file for changes after selection.                                                                      | `DxccAdifFilePath` (changed from `DxccAdifPath` in v26.5.1)                                                        |
| **Imported: (DXCC stats)**                                    | Shows QSO count and entity count when a log is loaded. Format: `<N> QSOs / <M> entities`.                                                                              | —                                                                                                                  |
| **DXCC Color swatches (New DXCC / New Band / New Mode / Worked)** | Opens a color picker for each DXCC status category.                                                                                                                | `DxccColorNewEntity`, `DxccColorNewBand`, `DxccColorNewMode`, `DxccColorWorked` (new in v26.5.1)                  |
| **Marker Lifetime:**                                           | How long an inactive Signal History marker persists before being removed. Default: 60 s. Valid range: 15–300 sec.                                                     | `SHistoryLifetimeS` (new in v26.5.1)                                                                               |
| **QRM Gate:**                                                  | How long a narrow carrier or wideband signal must persist before being classified as QRM. Default: 6 s. Valid range: 3–30 sec.                                         | `SHistoryQrmGateS` (new in v26.5.1)                                                                                |
| **Edge Threshold:**                                            | Threshold above noise floor for the slope edge walk that refines the S-History carrier-side edge. Default: 3.0 dB. Valid range: 1.0–10.0 dB.                          | `SHistorySoftEdgeDb` (new in v26.5.1)                                                                              |
| **Signal History color swatches (Signals / QRM)**              | Opens a color picker for the voice signal markers (gold) and QRM markers (red). Default: `#FFC800` / `#FF0000`.                                                       | `SHistoryColorSignals`, `SHistoryColorQrm` (new in v26.5.1)                                                        |
| **Snap to Step:**                                              | Rounds S-History click-to-tune to the nearest multiple of the active slice's step size. Default: Disabled.                                                            | `SHistorySnapToStep` (new in v26.5.1)                                                                              |

## Tuning from the Spot List

Double-clicking a row in the **Spot List** tab tunes the active slice to that spot's frequency. As of v0.9.7, AetherSDR also forwards any mode information extracted from the spot comment, so the slice automatically switches to the correct mode (for example, CW or SSB) to match the spot rather than only changing frequency.

## FreeDV Reporter station reporting

The **FreeDV** tab contains a **Station Reporting** group that lets AetherSDR broadcast your station's activity to the public FreeDV Reporter map at `qso.freedv.org`. This section is only present in builds compiled with `HAVE_WEBSOCKETS`; on Windows it additionally requires `HAVE_RADE`.

### Controls

| Control | Behavior | Setting key |
|---|---|---|
| **Enable FreeDV Reporter reporting when RADE is active** | Enables station-reporting to the public FreeDV Reporter map whenever the RADE modem is active. The checkbox refuses to enable if either the callsign or grid square field resolves to an empty value; a warning dialog explains what is missing. Default: disabled. | `FreeDvAutoReport` |
| **Callsign:** | Callsign sent to the FreeDV Reporter map. The field is read-only while **Use radio** is checked. Callsign is automatically updated if you change it in Radio Setup while **Use radio** is active. | `FreeDvMyCallsign` |
| **Use radio (callsign)** | Pre-fills the callsign field from the radio's configured callsign and locks the field read-only. Default: enabled. | `FreeDvUseRadioCallsign` |
| **Grid Square:** | Maidenhead grid square sent to the FreeDV Reporter map. The field is read-only while **Use GPS** is checked. | `FreeDvMyGrid` |
| **Use GPS (grid)** | Pre-fills the grid field from the radio's GPS module and locks the field read-only. Only shown on radio models that have GPS hardware. | `FreeDvUseGpsGrid` |
| **Station Msg:** | Optional free-text message shown beside your callsign on the public FreeDV Reporter map. | `FreeDvMyMessage` |

### Enabling FreeDV Reporter reporting

1. Open `Settings > SpotHub...` and click the **FreeDV** tab.
2. In the **Station Reporting** group, verify the **Callsign:** field shows your callsign.
   - If **Use radio** is checked, the callsign is taken automatically from the radio. Uncheck it to enter a callsign manually