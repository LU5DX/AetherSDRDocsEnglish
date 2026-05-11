# Enable DXCC Coloring from an ADIF Log

DXCC coloring lets AetherSDR mark panadapter spots by whether the DX entity has been worked, confirmed, or is still needed, based on contacts in your ADIF log file. This helps you quickly distinguish new entities from ones you have already logged.

## Before you start

- AetherSDR must be running. A radio connection is not required to configure this feature.
- You need an ADIF log file exported from your logging software. The file must use the standard `.adi` or `.adif` format.
- At least one spot source (DX cluster, RBN, WSJT-X, POTA, etc.) should be active so spots appear on the panadapter.

## Steps

1. Open `Settings > SpotHub...`.
2. Click the **Display** tab.
3. Click the **DXCC Colors:** toggle button to enable it. The button activates DXCC coloring (`IsDxccColoringEnabled`).
4. Click **Log File (ADIF):** to open a file chooser. Select your ADIF log file. The path is stored in `DxccAdifFilePath`.
5. Confirm the DXCC stats indicator updates to show the number of QSOs and entities imported from the file.
6. Optionally click the color swatches for **New DXCC**, **New Band**, **New Mode**, and **Worked** to customize the color assigned to each DXCC status category.

## What each control does

| Control                                                       | Behavior                                                                                                                                                                                                            | Setting key                                                                                |
|---------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| **DXCC Colors:**                                              | Master toggle. Colors panadapter spots by worked/confirmed/needed DXCC status.                                                                                                                                       | `IsDxccColoringEnabled` (changed from `DxccColoringEnabled` in v26.5.1)                    |
| **Log File (ADIF):**                                          | Opens a file picker. The chosen ADIF file is read to populate DXCC status. Auto-watches the file for changes after selection.                                                                                        | `DxccAdifFilePath` (changed from `DxccAdifPath` in v26.5.1)                               |
| **Imported:**                                                 | Shows QSO count and entity count when a log is loaded. Format: `<N> QSOs / <M> entities`.                                                                                                                            | —                                                                                          |
| **New DXCC** color swatch                                     | Opens a color picker for the color assigned to never-worked DXCC entities.                                                                                                                                           | `DxccColorNewEntity` (new in v26.5.1)                                                      |
| **New Band** color swatch                                     | Opens a color picker for the color assigned to DXCC entities worked on other bands but needed on the current band.                                                                                                   | `DxccColorNewBand` (new in v26.5.1)                                                        |
| **New Mode** color swatch                                     | Opens a color picker for the color assigned to DXCC entities worked on other modes but needed on the current mode.                                                                                                   | `DxccColorNewMode` (new in v26.5.1)                                                        |
| **Worked** color swatch                                       | Opens a color picker for the color assigned to fully-worked and confirmed DXCC entities.                                                                                                                             | `DxccColorWorked` (new in v26.5.1)                                                         |
| **Spots:**                                                    | Master toggle for DX spot overlay on the panadapter.                                                                                                                                                                 | `IsSpotsEnabled`                                                                           |
| **Memories:**                                                 | Toggles memory-channel overlay on the panadapter.                                                                                                                                                                    | `IsMemorySpotsEnabled`                                                                     |
| **Auto:**                                                     | Automatically switch slice mode when clicking a spot that includes mode info (e.g. CW, FT8, RTTY).                                                                                                                   | `SpotAutoSwitchMode` (changed from `SpotsAutoMode` in v26.5.1)                             |
| **Signals (Signal History)**                                  | Gold markers for detected voice-width signals on the panadapter. New in v26.5.1 (#2426). Same toggle as View > Signal History Markers.                                                                               | `SHistoryMarkersEnabled` (new in v26.5.1)                                                  |
| **QRM (Signal History)**                                      | Red markers for persistent carriers and wideband interference. New in v26.5.1 (#2426). Same toggle as View > QRM History Markers.                                                                                    | `SHistoryQrmEnabled` (new in v26.5.1)                                                      |
| **Clear All**                                                 | Clears all DX spots, memory feed, Signal History markers and QRM markers from the spectrum.                                                                                                                          | —                                                                                          |
| **Levels:**                                                   | Number of vertical stacking rows for spots (1–10).                                                                                                                                                                   | `SpotsMaxLevel`                                                                            |
| **Position:**                                                 | Vertical position on panadapter (0–100%).                                                                                                                                                                            | `SpotsStartingHeightPercentage`                                                            |
| **Font Size:**                                                | Spot text size (8–32).                                                                                                                                                                                              | `SpotFontSize`                                                                             |
| **Spot Lifetime:**                                            | Seconds before a spot fades away (10 sec – 24 hrs, non-linear steps).                                                                                                                                                | `DxClusterSpotLifetimeSec`                                                                 |
| **Override Colors:**                                          | Forces a single text color for all spots.                                                                                                                                                                            | `IsSpotsOverrideColorsEnabled`                                                             |
| **Spot text color picker**                                    | Opens QColorDialog to pick spot text color when Override Colors is enabled. Default #FFFF00.                                                                                                                         | `SpotsOverrideColor`                                                                       |
| **Override Background: Enabled**                              | Enables custom spot background color.                                                                                                                                                                                | `IsSpotsOverrideBackgroundColorsEnabled`                                                   |
| **Override Background: Auto**                                 | Auto-picks background color for contrast when custom background is enabled.                                                                                                                                          | `IsSpotsOverrideToAutoBackgroundColorEnabled`                                              |
| **Spot background color picker**                              | Opens QColorDialog for spot background color. Default #000000.                                                                                                                                                       | `SpotsOverrideBgColor`                                                                     |
| **Background Opacity:**                                       | Opacity of spot background color (0–100%). Default 48.                                                                                                                                                               | `SpotsBackgroundOpacity`                                                                   |
| **Spot Lines:**                                               | Draws vertical lines from the spectrum up to each spot label. Disable during contests to reduce visual clutter. Default enabled.                                                                                     | `IsSpotsLinesEnabled`                                                                      |
| **DXCC Coloring (section)**                                   | Section header for DXCC coloring controls in the left column below the divider.                                                                                                                                      | —                                                                                          |
| **Signal History (section)**                                  | Section header for Signal History tunables in the right column below the divider. New in v26.5.1 (#2506).                                                                                                            | —                                                                                          |
| **Marker Lifetime:**                                          | How long an inactive Signal History marker persists before being removed (15–300 sec). Default 60 s. New in v26.5.1.                                                                                                 | `SHistoryLifetimeS` (new in v26.5.1)                                                       |
| **QRM Gate:**                                                 | How long a narrow carrier or wideband signal must persist before being classified as QRM (3–30 sec). Default 6 s. New in v26.5.1.                                                                                     | `SHistoryQrmGateS` (new in v26.5.1)                                                        |
| **Edge Threshold:**                                           | Threshold above noise floor for the slope edge walk that refines the S-History carrier-side edge (1.0–10.0 dB). Default 3.0 dB. Lower = closer to carrier but more noise-sensitive. New in v26.5.1.                   | `SHistorySoftEdgeDb` (new in v26.5.1)                                                      |
| **Signals** color swatch                                      | Opens a color picker for the voice signal markers (gold). Default #FFC800. New in v26.5.1.                                                                                                                           | `SHistoryColorSignals` (new in v26.5.1)                                                    |
| **QRM** color swatch                                          | Opens a color picker for the QRM markers (red). Default #FF0000. New in v26.5.1.                                                                                                                                     | `SHistoryColorQrm` (new in v26.5.1)                                                        |
| **Snap to Step:**                                             | Rounds S-History click-to-tune to the nearest multiple of the active slice's step size, hiding the small carrier offset. Default disabled. New in v26.5.1.                                                           | `SHistorySnapToStep` (new in v26.5.1)                                                      |
| Total Spots:                                                  | Live readout of how many spots are currently tracked across all sources. Updated whenever spots are added or cleared.                                                                                                | —                                                                                          |

## Tuning from the Spot List

Double-clicking a row in the **Spot List** tab tunes the active receiver to that spot's frequency. As of v0.9.7, AetherSDR also forwards the mode derived from the spot comment, so the receiver switches to the appropriate mode (for example, CW or SSB) to match the spot rather than only changing frequency.

## FreeDV Reporter reporting

The **Station Reporting** group on the **FreeDV** tab lets AetherSDR broadcast your station's activity to the public FreeDV Reporter map at qso.freedv.org whenever the RADE modem is active.

### Requirements before enabling

- A non-empty callsign must be available, either from the radio (when **Use radio (callsign)** is checked) or entered manually in the **Callsign:** field.
- A non-empty Maidenhead grid square must be available, either from the radio's GPS (when **Use GPS (grid)** is checked, on supported hardware) or entered manually in the **Grid Square:** field.
- If either value is missing when you check **Enable FreeDV Reporter reporting when RADE is active**, a warning dialog appears and the checkbox reverts to unchecked.

### Steps

1. Open `Settings > SpotHub...` and click the **FreeDV** tab.
2. In the **Station Reporting** group, confirm **Use radio (callsign)** is checked if you want AetherSDR to pull the callsign from the radio automatically. Uncheck it and type a callsign in **Callsign:** to enter one manually.
3. If your radio has GPS hardware, confirm **Use GPS (grid)** is checked to populate **Grid Square:** automatically. Otherwise uncheck it and type your Maidenhead grid square (up to six characters) in **Grid Square:**.
4. Optionally type a short message in **Station Msg:** to display beside your callsign on the map.
5. Check **Enable FreeDV Reporter reporting when RADE is active** (`FreeDvAutoReport`). If callsign or grid is missing, a warning appears — fill in the missing field and try again.
6. To have reporting start automatically each time AetherSDR launches, enable **Auto-start on startup (FreeDV)** (`FreeDvAutoStart`).

## Tips

- The DXCC stats indicator in the dialog shows how many QSOs and entities were imported from the ADIF file. If it reads zero after loading, verify the file is valid ADIF.
- The **Log File (ADIF):** button stores the path persistently. You do not need to re-select the file after restarting AetherSDR.
- AetherSDR auto-watches the ADIF file for changes after selection. When your logger writes to the file, spot colors on the panadapter update automatically — no separate reload toggle is needed.
- DXCC coloring is independent of per-source spot colors. If **Override Colors:** is also active, see [Pick colors for each spot source](pick-colors-for-each-spot-source.md) for how those settings interact.
- **Spot Lines:** (`IsSpotsLinesEnabled`) defaults to **Enabled**. During contests or when the panadapter feels visually busy, disable this toggle on the **Display** tab to remove the vertical lines while keeping spot labels visible.
- The four DXCC color swatches (**New DXCC**, **New Band**, **New Mode**, **Worked**) replace the previous fixed color scheme. Customize each to suit your preference.
- When **Use radio (callsign)** is checked, the callsign field updates automatically if you change the callsign in Radio Setup without reopening SpotHub.
- Reporter broadcasting is build-gated by `HAVE_WEBSOCKETS`. On Windows it additionally requires `HAVE_RADE`. If the **Station Reporting** group or the enable checkbox is absent, your build does not include the required components.

## Troubleshooting

- **DXCC stats shows 0 QSOs after selecting a file** — The file may not be valid ADIF, may be empty, or may use an encoding AetherSDR cannot read. Export a fresh ADIF from your logger and try again.
- **Spot colors do not change after enabling DXCC Colors** — Confirm the **Spots:** toggle on the **Display** tab is enabled (`IsSpotsEnabled`). Also check that **Override Colors:** (`IsSpotsOverrideColorsEnabled`) is not active, as it forces a single color for all spots regardless of DXCC status.
- **New contacts are not reflected on spots** — AetherSDR auto-watches the ADIF file for changes, so spot colors should update automatically. If they do not, try re-selecting the log file with **Log File (ADIF):** to trigger a fresh import.
- **Double-clicking a spot does not switch mode** — Mode is derived from the spot comment text. If the comment does not contain a recognizable mode token, only the frequency changes.
- **Warning appears when enabling FreeDV Reporter** — Either the callsign or grid square field is blank. Fill in both fields (or check