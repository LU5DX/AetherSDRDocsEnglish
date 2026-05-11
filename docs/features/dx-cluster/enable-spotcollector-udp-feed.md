# Enable SpotCollector UDP feed

AetherSDR can receive DX spots broadcast by Ham Radio Deluxe's SpotCollector over UDP and display them on the panadapter. This page explains how to start the listener, set the correct port, and configure it to start automatically.

## Before you start

- SpotCollector must be installed, configured, and running on the same machine or local network, and set to broadcast spots via UDP.
- Note the UDP port SpotCollector is broadcasting on — you will need to enter it in AetherSDR.

## Steps

1. Open `Settings > SpotHub...`.
2. Click the **SpotCollector** tab.
3. Set **UDP Port:** to the port SpotCollector is broadcasting on. Valid range: 1–65535. This value is saved as `SpotCollectorPort`.
4. Click **Start**.
5. Confirm the status indicator changes to **Listening**. Incoming spots will appear in the **SpotCollector Spots** console as they arrive.
6. To have the listener start automatically every time AetherSDR launches, enable **Auto-start on startup**. This is saved as `SpotCollectorAutoStart`.

## What each control does

| Control                                                       | Description                                                                                                                                                                                                                                                  | Setting key                                        |
|---------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| **UDP Port:**                                                 | UDP port AetherSDR listens on for SpotCollector broadcasts. Valid range: 1–65535.                                                                                                                                                                            | `SpotCollectorPort`                                |
| **Start / Stop**                                              | Starts or stops the UDP listener.                                                                                                                                                                                                                            | —                                                  |
| **Auto-start on startup**                                     | Starts the listener automatically on launch.                                                                                                                                                                                                                 | `SpotCollectorAutoStart`                           |
| **SpotCollector Spots**                                       | Read-only console showing spots received from SpotCollector.                                                                                                                                                                                                 | —                                                  |
| **Enable FreeDV Reporter reporting when RADE is active**      | Enables station-reporting to the public FreeDV Reporter map (qso.freedv.org) whenever the RADE modem is active. Requires a valid callsign and grid square — if either field is blank or unresolvable, the checkbox refuses to enable and displays a warning. | `FreeDvAutoReport`                                 |
| **Callsign: (FreeDV Reporter)**                               | Callsign to report to the FreeDV Reporter map. Read-only when **Use radio** is checked. When **Use radio** is checked, the field is populated from the radio's configured callsign and updates automatically if that callsign changes.                       | `FreeDvMyCallsign`                                 |
| **Use radio (callsign)**                                      | Pre-fills the callsign field from the radio's configured callsign and locks the field read-only.                                                                                                                                                             | `FreeDvUseRadioCallsign`                           |
| **Grid Square: (FreeDV Reporter)**                            | Maidenhead grid square to report. Read-only when **Use GPS** is checked.                                                                                                                                                                                     | `FreeDvMyGrid`                                     |
| **Use GPS (grid)**                                            | Pre-fills the grid field from the radio's GPS module and locks the field read-only. Only shown on radio models that have GPS hardware.                                                                                                                       | `FreeDvUseGpsGrid`                                 |
| **Station Msg: (FreeDV Reporter)**                            | Optional free-text message shown beside the callsign on the public FreeDV Reporter map.                                                                                                                                                                      | `FreeDvMyMessage`                                  |
| **Auto (Display tab)**                                        | Automatically switches the slice mode when clicking a spot that includes mode information (e.g. CW, FT8, RTTY). Setting key changed from `SpotsAutoMode` to `SpotAutoSwitchMode` in v26.5.1. Default is **Enabled**.                                         | `SpotAutoSwitchMode`                               |
| **Spot Lines:**                                               | Draws vertical lines from the spectrum up to each spot label. Default is **Enabled**. Disable during contests to reduce visual clutter.                                                                                                                      | `IsSpotsLinesEnabled`                              |
| Total Spots:                                                  | Live readout of how many spots are currently tracked across all sources.                                                                                                                                                                                     | Updated whenever spots are added or cleared. Resets to 0 when **Clear All** is pressed. |
| **Signals (Display tab)**                                     | Gold markers for detected voice-width signals on the panadapter. New in v26.5.1 (#2426). Same toggle as View > Signal History Markers.                                                                                                                       | `SHistoryMarkersEnabled`                           |
| **QRM (Display tab)**                                         | Red markers for persistent carriers and wideband interference. New in v26.5.1 (#2426). Same toggle as View > QRM History Markers.                                                                                                                            | `SHistoryQrmEnabled`                              |
| **Clear All (Display tab)**                                   | Clears all DX spots, memory feed, Signal History markers and QRM markers from the spectrum.                                                                                                                                                                  | —                                                  |
| **Spot text color picker**                                    | Opens QColorDialog to pick spot text color.                                                                                                                                                                                                                  | `SpotsOverrideColor`                               |
| **Override Background: Enabled**                              | Enables custom spot background color.                                                                                                                                                                                                                        | `IsSpotsOverrideBackgroundColorsEnabled`           |
| **Override Background: Auto**                                 | Auto-picks background color for contrast.                                                                                                                                                                                                                    | `IsSpotsOverrideToAutoBackgroundColorEnabled`      |
| **Spot background color picker**                              | Opens QColorDialog for spot background color.                                                                                                                                                                                                                | `SpotsOverrideBgColor`                             |
| **DXCC Coloring (section)**                                   | Section header for DXCC coloring controls in the left column below the divider on the Display tab.                                                                                                                                                          | —                                                  |
| **DXCC Colors:**                                              | Colors spots by worked/confirmed/needed DXCC status. Setting key changed from `DxccColoringEnabled` to `IsDxccColoringEnabled` in v26.5.1.                                                                                                                   | `IsDxccColoringEnabled`                            |
| **Log File (ADIF):**                                          | Loads an ADIF log file to drive DXCC coloring. Auto-watches the file for changes after selection. Setting key changed from `DxccAdifPath` to `DxccAdifFilePath` in v26.5.1. Auto-Reload is always enabled when a file is selected (no separate toggle).      | `DxccAdifFilePath`                                 |
| **Imported: (DXCC stats)**                                    | Shows QSO count and entity count when a log is loaded. Format: '<N> QSOs / <M> entities'.                                                                                                                                                                   | —                                                  |
| **DXCC Color swatches (New DXCC / New Band / New Mode / Worked)** | Opens a color picker for each DXCC status category. New in v26.5.1 — replaces previous fixed DXCC color scheme.                                                                                                                                             | `DxccColorNewEntity` / `DxccColorNewBand` / `DxccColorNewMode` / `DxccColorWorked` |
| **Signal History (section)**                                  | Section header for Signal History tunables in the right column below the divider on the Display tab. New in v26.5.1 (#2506).                                                                                                                                 | —                                                  |
| **Marker Lifetime:**                                          | How long an inactive Signal History marker persists before being removed. Slider. Default 60 s, range 15–300 s. New in v26.5.1.                                                                                                                              | `SHistoryLifetimeS`                                |
| **QRM Gate:**                                                 | How long a narrow carrier or wideband signal must persist before being classified as QRM. Slider. Default 6 s, range 3–30 s. New in v26.5.1.                                                                                                                  | `SHistoryQrmGateS`                                 |
| **Edge Threshold:**                                           | Threshold above noise floor for the slope edge walk that refines the S-History carrier-side edge. Slider. Default 3.0 dB, range 1.0–10.0 dB. New in v26.5.1.                                                                                                | `SHistorySoftEdgeDb`                               |
| **Signal History color swatches (Signals / QRM)**             | Opens a color picker for the voice signal markers (gold) and QRM markers (red). New in v26.5.1.                                                                                                                                                              | `SHistoryColorSignals` / `SHistoryColorQrm`        |
| **Snap to Step:**                                             | Rounds S-History click-to-tune to the nearest multiple of the active slice's step size, hiding the small carrier offset. New in v26.5.1. Default Disabled.                                                                                                   | `SHistorySnapToStep`                               |

## FreeDV Reporter reporting

The **FreeDV** tab contains a **Station Reporting** group that controls whether AetherSDR broadcasts your station's activity to the public FreeDV Reporter map at qso.freedv.org.

### Requirements before enabling

- A valid callsign must be available — either from the radio (when **Use radio** is checked) or typed into the **Callsign:** field.
- A valid Maidenhead grid square must be available — either from the radio's GPS module (when **Use GPS** is checked, on supported hardware) or typed into the **Grid Square:** field.

If either value is missing when you attempt to enable **Enable FreeDV Reporter reporting when RADE is active**, AetherSDR displays a warning and leaves the checkbox unchecked. This prevents blank or placeholder values from appearing on the shared public map.

### Steps to enable reporting

1. Open `Settings > SpotHub...` and click the **FreeDV** tab.
2. In the **Station Reporting** group, confirm the **Callsign:** field shows your callsign.
   - If **Use radio** is checked, the field is populated automatically from the radio's configured callsign and is read-only. Uncheck **Use radio** to enter a callsign manually.
3. Confirm the **Grid Square:** field shows your Maidenhead locator.
   - On radios with GPS hardware, check **Use GPS** to populate it automatically. Uncheck **Use GPS** to type a grid square manually.
4. Optionally enter a short message in **Station Msg:** — it appears beside your callsign on the map.
5. Check **Enable FreeDV Reporter reporting when RADE is active**.
   - If either the callsign or grid square is blank, a warning dialog appears. Fill in the missing value and try again.
6. Reporting is now active whenever the RADE modem is running.

## Auto Mode default change

As of v0.9.5.1, **Auto** (`SpotAutoSwitchMode`) defaults to **Enabled** for new installations. If you are upgrading and want to retain the previous behavior, open the **Display** tab and set **Auto** to **Disabled**.

## Tune to a spot by double-clicking

Double-clicking a row in the **Spot List** tab tunes the active slice to that spot's frequency. As of v0.9.7, AetherSDR also reads the mode hint from the spot comment and forwards it to the receiver, so the slice switches to the correct mode (for example CW or SSB) at the same time as the frequency changes. No additional configuration is required.

## Frameless window mode

In v26.5.1, the SpotHub dialog was updated to support frameless window mode. When frameless mode is enabled (default), the dialog features a custom title bar and 8-axis edge resizing. The title bar displays "SpotHub" and can be used to drag the window. This provides a consistent appearance with other AetherSDR dialogs.

## Tips
- Spots received from SpotCollector appear alongside spots from other sources in the **Spot List** tab. The **Source** column identifies them.
- If the panadapter spot overlay is not visible, check that **Spots:** is set to **Enabled** on the **Display** tab.
- **Auto** defaults to **Enabled**. When you double-click a spot that includes mode information (e.g. CW, FT8, RTTY), the slice mode switches automatically. Disable it on the **Display** tab if you prefer to switch modes manually.
- Use **Spot Lines:** on the **Display** tab to control whether vertical lines are drawn from the spectrum up to each spot label. Disable this during contests to reduce visual clutter.
- The **Display** tab was reorganized in v26.5.1 (#2506). Signal History controls now appear in a dedicated section instead of separate sub-tabs. The tab has a top toggle row, common sliders, then a two-column layout with DXCC Coloring on the left and Signal History on the right.

## Troubleshooting

- **Status stays Stopped / no spots appear** — Verify that SpotCollector is actively broadcasting and that the UDP port in AetherSDR matches the port configured in SpotCollector. Check that no firewall is blocking UDP traffic on that port.
- **Listener starts but the panadapter shows no spots** — Confirm that the master spot overlay is on: open the **Display** tab and check that **Spots:** is **Enabled**.
- **FreeDV Reporter checkbox unchecks itself with a warning** — The callsign or grid square field is empty or could not be resolved. Fill in both fields (or enable **Use radio** / **Use GPS** if the radio can supply the values) before enabling reporting.

## Related

- [SpotHub overview](overview.md)
- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
- [Pick colors for each spot source](pick-colors-for-each-spot-source.md)
- [Tune to a spot by double-clicking the spot list](tune-to-a-spot-by-double-clicking-the-spot-list.md)
- [Clear all spots from the panadapter](clear-all-spots-from-the-panadapter.md)
<!-- docmesh