# Pick colors for each spot source

AetherSDR can display spots from up to six sources simultaneously. Assigning a distinct color to each source makes it easy to tell them apart on the panadapter at a glance.

## Before you start

- Open SpotHub: `Settings > SpotHub...`
- At least one spot source should be configured so you can see the effect of your color choice.

## Steps

### DX Cluster spot color
1. In SpotHub, click the **Cluster** tab.
2. Click the **Spot Color:** button.
3. Choose a color in the color picker that opens and confirm your selection.
4. The new color is saved to `ClusterSpotColor` and applied immediately to cluster spots on the panadapter.

### RBN spot color

1. Click the **RBN** tab.
2. Click the **Spot Color:** button.
3. Choose a color and confirm.
4. Saved to `RbnSpotColor`.

### WSJT-X spot colors

WSJT-X supports four separate colors, one per decode category.

1. Click the **WSJT-X** tab.
2. Click the color button for each category you want to change:
   - **CQ color** — spots decoded as CQ calls. Saved to `WsjtxColorCQ`.
   - **POTA color** — spots decoded as CQ POTA calls. Saved to `WsjtxColorPOTA`.
   - **Calling Me color** — decodes addressed to your callsign. Saved to `WsjtxColorCallingMe`.
   - **Default color** — all other WSJT-X decodes. Saved to `WsjtxColorDefault`.
3. Confirm each color in the color picker before moving to the next.

### POTA spot color

1. Click the **POTA** tab.
2. Click the **Spot Color:** button.
3. Choose a color and confirm.
4. Saved to `PotaSpotColor`.

### FreeDV spot color

1. Click the **FreeDV** tab.
2. Click the **Spot Color:** button.
3. Choose a color and confirm.
4. Saved to `FreeDvSpotColor`.

> **Note:** The FreeDV tab is present only if AetherSDR was built with WebSocket support.

### SpotCollector

SpotCollector does not have a dedicated spot-color picker in SpotHub. See the Display tab options below if you need a uniform override for all sources.

## What each control does
| Control                                                       | Tab                                                                                                                      | Saved setting                                                                                                                                                          |
|---------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Spot Color:**                                               | Cluster                                                                                                                  | `ClusterSpotColor`                                                                                                                                                     |
| **Startup Commands…**                                         | Cluster                                                                                                                  | `DxClusterStartupCommands` — commands sent automatically after every login (#2683). One command per line.                                                              |
| **Spot Color:**                                               | RBN                                                                                                                      | `RbnSpotColor`                                                                                                                                                         |
| **Startup Commands…**                                         | RBN                                                                                                                      | `RbnStartupCommands` — independent setting from DX cluster startup commands. One command per line.                                                                    |
| **CQ color**                                                  | WSJT-X                                                                                                                   | `WsjtxColorCQ`                                                                                                                                                         |
| **POTA color**                                                | WSJT-X                                                                                                                   | `WsjtxColorPOTA`                                                                                                                                                       |
| **Calling Me color**                                          | WSJT-X                                                                                                                   | `WsjtxColorCallingMe`                                                                                                                                                  |
| **Default color**                                             | WSJT-X                                                                                                                   | `WsjtxColorDefault`                                                                                                                                                    |
| **Spot Color:**                                               | POTA                                                                                                                     | `PotaSpotColor`                                                                                                                                                        |
| **Spot Color:**                                               | FreeDV                                                                                                                   | `FreeDvSpotColor`                                                                                                                                                      |
| **Enable FreeDV Reporter reporting when RADE is active**      | FreeDV                                                                                                                   | `FreeDvAutoReport`                                                                                                                                                     |
| **Callsign:**                                                 | FreeDV — Station Reporting                                                                                               | `FreeDvMyCallsign`                                                                                                                                                     |
| **Use radio (callsign)**                                      | FreeDV — Station Reporting                                                                                               | `FreeDvUseRadioCallsign`                                                                                                                                               |
| **Grid Square:**                                              | FreeDV — Station Reporting                                                                                               | `FreeDvMyGrid`                                                                                                                                                         |
| **Use GPS (grid)**                                            | FreeDV — Station Reporting                                                                                               | `FreeDvUseGpsGrid`                                                                                                                                                     |
| **Station Msg:**                                              | FreeDV — Station Reporting                                                                                               | `FreeDvMyMessage`                                                                                                                                                      |
| **Auto:**                                                     | Display                                                                                                                  | `SpotAutoSwitchMode` — setting key changed from `SpotsAutoMode` in v26.5.1. Default changed to **Enabled** in v0.9.5.1.                                               |
| **Signals (Signal History)**                                  | Display                                                                                                                  | `SHistoryMarkersEnabled` — new in v26.5.1 (#2426). Same toggle as View > Signal History Markers.                                                                     |
| **QRM (Signal History)**                                      | Display                                                                                                                  | `SHistoryQrmEnabled` — new in v26.5.1 (#2426). Same toggle as View > QRM History Markers.                                                                            |
| **Clear All**                                                 | Display                                                                                                                  | Clears all DX spots, memory feed, Signal History markers and QRM markers from the spectrum.                                                                           |
| **Spot Lines:**                                               | Display                                                                                                                  | `IsSpotsLinesEnabled` — new in v0.9.7                                                                                                                                  |
| Total spots count                                             | Status bar                                                                                                               | Live readout of how many spots are currently tracked across all sources. Updated whenever spots are added or cleared. Resets to 0 when **Clear All Spots** is pressed. |
| **Spot text color picker**                                    | Display                                                                                                                  | `SpotsOverrideColor` — default `#FFFF00`                                                                                                                               |
| **Override Background: Enabled**                              | Display                                                                                                                  | `IsSpotsOverrideBackgroundColorsEnabled`                                                                                                                               |
| **Override Background: Auto**                                 | Display                                                                                                                  | `IsSpotsOverrideToAutoBackgroundColorEnabled`                                                                                                                          |
| **Spot background color picker**                              | Display                                                                                                                  | `SpotsOverrideBgColor` — default `#000000`                                                                                                                             |
| **Background Opacity:**                                       | Display                                                                                                                  | `SpotsBackgroundOpacity` — setting key migrated from `SpotsOverrideBgOpacity` in v0.9.7                                                                                |
| **Total Spots:**                                              | Display                                                                                                                  | Live count of spots currently tracked across all sources.                                                                                                              |
| **DXCC Colors:**                                              | Display — DXCC Coloring section                                                                                          | `IsDxccColoringEnabled` — setting key changed from `DxccColoringEnabled` in v26.5.1.                                                                                   |
| **Log File (ADIF):**                                          | Display — DXCC Coloring section                                                                                          | `DxccAdifFilePath` — setting key changed from `DxccAdifPath` in v26.5.1. Auto-Reload is always enabled when a file is selected.                                        |
| **Imported: (DXCC stats)**                                    | Display — DXCC Coloring section                                                                                          | Shows QSO count and entity count when a log is loaded. Format: '<N> QSOs / <M> entities'.                                                                             |
| **DXCC Color swatches** (New DXCC / New Band / New Mode / Worked) | Display — DXCC Coloring section                                                                                       | `DxccColorNewEntity` / `DxccColorNewBand` / `DxccColorNewMode` / `DxccColorWorked` — new in v26.5.1                                                                   |
| **Marker Lifetime:**                                          | Display — Signal History section                                                                                         | `SHistoryLifetimeS` — new in v26.5.1. Default 60 s.                                                                                                                    |
| **QRM Gate:**                                                 | Display — Signal History section                                                                                         | `SHistoryQrmGateS` — new in v26.5.1. Default 6 s.                                                                                                                      |
| **Edge Threshold:**                                           | Display — Signal History section                                                                                         | `SHistorySoftEdgeDb` — new in v26.5.1. Default 3.0 dB.                                                                                                                 |
| **Signal History color swatches** (Signals / QRM)             | Display — Signal History section                                                                                         | `SHistoryColorSignals` (gold) / `SHistoryColorQrm` (red) — new in v26.5.1.                                                                                            |
| **Snap to Step:**                                             | Display — Signal History section                                                                                         | `SHistorySnapToStep` — new in v26.5.1. Default Disabled.                                                                                                               |

## FreeDV Reporter — Station Reporting

v0.9.3 adds a **Station Reporting** group inside the **FreeDV** tab. When enabled, AetherSDR broadcasts your station's activity to the public FreeDV Reporter map at qso.freedv.org whenever the RADE modem is active.

> **Note:** Station Reporting is present only if AetherSDR was built with WebSocket support (`HAVE_WEBSOCKETS`). On Windows builds it additionally requires `HAVE_RADE`.

### Enable reporting

1. Click the **FreeDV** tab in SpotHub.
2. In the **Station Reporting** group, fill in a valid callsign and grid square (see below) before enabling the checkbox.
3. Check **Enable FreeDV Reporter reporting when RADE is active**.
   - If either the callsign or grid square field is blank when you check the box, a warning dialog appears and the checkbox reverts to unchecked. Fill both fields first, then try again.
4. The setting is saved to `FreeDvAutoReport`.

### Callsign field

- The **Callsign:** field (`FreeDvMyCallsign`) sets the callsign reported to the public map.
- When **Use radio** is checked (default), the field is pre-filled from the radio's configured callsign and locked read-only. The field updates automatically if you change the callsign in Radio Setup.
- Uncheck **Use radio** to type a callsign manually. The value is saved to `FreeDvMyCallsign` and uppercased on exit.
- **Use radio** is saved to `FreeDvUseRadioCallsign`.

### Grid Square field

- The **Grid Square:** field (`FreeDvMyGrid`) sets the Maidenhead locator reported to the public map.
- On radio models with GPS hardware, a **Use GPS** checkbox appears. When checked (default), the field is pre-filled from the radio's GPS module and locked read-only.
- Uncheck **Use GPS** to type a grid square manually. The value is saved to `FreeDvMyGrid` and uppercased on exit.
- **Use GPS** is saved to `FreeDvUseGpsGrid`. The checkbox is hidden on radio models that have no GPS hardware.

### Station message

- The optional **Station Msg:** field (`FreeDvMyMessage`) accepts free text that appears beside your callsign on the public FreeDV Reporter map. Leave it blank if you have nothing to add.

## Auto Mode default changed in v0.9.5.1

The **Auto:** toggle on the **Display** tab now defaults to **Enabled** for new installations. If you are upgrading from an earlier version and `SpotAutoSwitchMode` was not previously set, AetherSDR will treat it as enabled after the update. To disable it, open the **Display** tab and click **Auto:** until it shows **Disabled**.

> **Note:** The setting key changed from `SpotsAutoMode` to `SpotAutoSwitchMode` in v26.5.1.

## Spot Lines (new in v0.9.7)

The **Spot Lines:** toggle on the **Display** tab controls whether vertical lines are drawn from the spectrum baseline up to each spot label on the panadapter. The setting is saved to `IsSpotsLinesEnabled` and defaults to **Enabled**.

To turn off spot lines:

1. Open SpotHub: `Settings > SpotHub...`
2. Click the **Display** tab.
3. Click **Spot Lines:** until it shows **Disabled**.

Disabling spot lines reduces visual clutter during contests or when spot density is high.

## Signal History and QRM markers (new in v26.5.1)

The **Display** tab includes Signal History controls for detecting and marking signals on the panadapter:

- **Signals (Signal History):** Gold markers for detected voice-width signals on the panadapter. Saved to `SHistoryMarkersEnabled`.
- **QRM (Signal History):** Red markers for persistent carriers and wideband interference. Saved to `SHistoryQrmEnabled`.

Both toggles mirror the same controls found under `View > Signal History Markers` and `View > QRM History Markers`.

### Signal History tunables

The **Signal History** section below the divider on the Display tab provides fine-tuning:

- **Marker Lifetime:** Slider (15–300 seconds, default 60 s) controlling how long an inactive Signal History marker persists. Saved to `SHistoryLifetimeS`.
- **QRM Gate:** Slider (3–30 seconds, default 6 s) controlling how long a narrow carrier or wideband signal must persist before being classified as QRM. Saved to `SHistoryQrmGateS`.
- **Edge Threshold:** Slider (1.0–10.0 dB, default 3.0 dB) for the slope edge walk that refines the S-History carrier-side edge. Lower values are closer to the carrier but more noise-sensitive. Saved to `SHistorySoftEdgeDb`.
- **Signal History color swatches:** Click to open a color picker for the voice signal markers (default gold `#FFC800`) and QRM markers (default red `#FF0000`). Saved to