# Auto-reload ADIF log when updated by a logger

When DXCC coloring is enabled, AetherSDR reads your ADIF log once at startup. Enabling auto-reload tells AetherSDR to re-read the file whenever your logging software updates it, so worked/confirmed/needed coloring on the panadapter stays current without manual intervention.

## Before you start

- DXCC coloring must be enabled and an ADIF log file must already be loaded. See [Enable DXCC coloring from an ADIF log](enable-dxcc-coloring-from-an-adif-log.md).
- Your logging software must write updates to the same ADIF file path stored in `DxccAdifPath`.

## Steps

1. Open `Settings > SpotHub...`.
2. Click the `Display` tab.
3. Confirm that `DXCC Coloring` is enabled (the toggle shows its active state).
4. Confirm that `Log File (ADIF):` shows the correct file path.
5. Click `Auto-Reload Log:` to enable it.

AetherSDR now watches the file at `DxccAdifPath` for changes. Each time your logger writes a new QSO, AetherSDR re-reads the file and updates spot coloring on the panadapter.

## What each control does

| Control | Description | Setting key |
|---|---|---|
| `DXCC Coloring` | Master toggle for coloring spots by worked/confirmed/needed status. Auto-reload has no effect when this is off. | `DxccColoringEnabled` |
| `Log File (ADIF):` | Opens a file picker to select the ADIF log. The chosen path is persisted. | `DxccAdifPath` |
| `Auto-Reload Log:` | Toggle. When enabled, AetherSDR watches the file for changes and reloads it automatically. | `DxccAutoReload` |
| `Enable FreeDV Reporter reporting when RADE is active` | Enables station-reporting to the public FreeDV Reporter map (qso.freedv.org) whenever the RADE modem is active. Requires a valid callsign and grid square; if either field is blank or resolves to empty, the checkbox refuses to enable and displays a warning. | `FreeDvAutoReport` |
| `Callsign: (FreeDV Reporter)` | Callsign to report to the FreeDV Reporter map. Read-only when `Use radio` is checked. When `Use radio` is checked, the field is kept in sync automatically if the callsign is changed in Radio Setup. | `FreeDvMyCallsign` |
| `Use radio (callsign)` | Pre-fills the callsign field from the radio's configured callsign and locks the field read-only. Defaults to enabled. | `FreeDvUseRadioCallsign` |
| `Grid Square: (FreeDV Reporter)` | Maidenhead grid square to report (up to six characters). Read-only when `Use GPS` is checked. | `FreeDvMyGrid` |
| `Use GPS (grid)` | Pre-fills the grid field from the radio's GPS module and locks the field read-only. Only shown on radio models that have GPS hardware. | `FreeDvUseGpsGrid` |
| `Station Msg: (FreeDV Reporter)` | Optional free-text message shown beside the callsign on the public FreeDV Reporter map. | `FreeDvMyMessage` |
| `Auto Mode:` | Toggle. When enabled, automatically switches the slice mode when clicking a spot that includes mode information (e.g. CW, FT8, RTTY). Defaults to **Enabled** as of v0.9.5.1. | `SpotAutoSwitchMode` |
| `Spot Lines:` | Toggle. Draws vertical lines from the spectrum up to each spot label. Defaults to **Enabled**. Disable during contests to reduce visual clutter. New in v0.9.7. | `IsSpotsLinesEnabled` |
| `Total Spots:` | Live readout of how many spots are currently tracked across all sources. Updated whenever spots are added or cleared. Resets to 0 when **Clear All Spots** is pressed. | — |

## Tuning from the Spot List

Double-clicking a row in the Spot List tab tunes the active slice to the spot's frequency. As of v0.9.7, AetherSDR also forwards mode information extracted from the spot comment. If a recognized mode (such as CW, FT8, or SSB) is present, the slice switches to that mode automatically, provided `Auto Mode:` is enabled on the Display tab.

## FreeDV Reporter reporting

The **Station Reporting** group inside the `FreeDV` tab lets AetherSDR broadcast your station's activity to the public FreeDV Reporter map at qso.freedv.org whenever the RADE modem is active.

### Requirements

- The build must include WebSocket support (`HAVE_WEBSOCKETS`). On Windows, `HAVE_RADE` is also required.
- Both a callsign and a grid square must resolve to non-empty values before the `Enable FreeDV Reporter reporting when RADE is active` checkbox can be turned on.

### How callsign and grid are resolved

When you enable reporting, AetherSDR resolves the callsign and grid in the following order:

**Callsign**
1. If `Use radio` is checked and the radio has a configured callsign, that callsign is used.
2. Otherwise, the value typed in `Callsign:` is used.

**Grid square**
1. If `Use GPS` is checked, the radio has GPS hardware, and a GPS-derived grid is available, that grid is used.
2. Otherwise, the value typed in `Grid Square:` is used.

If either value is empty after resolution, a warning dialog appears and the checkbox reverts to unchecked. This prevents blank or placeholder values (such as `N0CALL` or `AA00`) from being broadcast to the shared public map.

### Setting up reporting

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

## Tips

- If your logger writes a temporary file and then renames it into place, the file watcher may not detect every save. Point your logger to write directly to the file at the path stored in `DxccAdifPath` for reliable detection.
- For large ADIF files, AetherSDR reads only the last 500 lines on each reload to avoid blocking the UI.
- If you change the radio's callsign in Radio Setup while `Use radio` is checked, the `Callsign:` field in the FreeDV Reporter section updates automatically.
- `Auto Mode:` defaults to **Enabled**. If the slice mode switches unexpectedly when you click a spot, open the Display tab and set `Auto Mode:` to Disabled.
- `Spot Lines:` defaults to **Enabled**. During contests, disabling it reduces visual clutter on the panadapter.

## Troubleshooting

- **Spot colors do not update after logging a new QSO** — Verify that `Auto-Reload Log:` is enabled and that `DXCC Coloring` is also enabled. Check that your logger is writing to the exact same file path shown next to `Log File (ADIF):`. If the path has changed, click `Log File (ADIF):` to re-select the file.
- **DXCC stats indicator shows 0 QSOs** — The ADIF file may not be readable or may be empty. Open the file in a text editor to confirm it contains valid ADIF records, then reload AetherSDR or re-select the file using `Log File (ADIF):`.
- **FreeDV Reporter checkbox reverts to unchecked immediately** — A callsign or grid square is missing or empty. Fill in both fields (or enable `Use radio` / `Use GPS` so that the radio supplies the values) and then check the box again.
- **FreeDV Reporter controls are not visible** — The build does not include WebSocket support. On Windows, RADE support may also be absent. Contact your build provider or rebuild with `HAVE_WEBSOCKETS` (and `HAVE_RADE` on Windows) enabled.
- **Auto Mode was previously disabled and is now behaving differently after upgrading** — The default for `Auto Mode:` changed to **Enabled** in v0.9.5.1. If you want to keep the old behaviour, open the **Display** tab and set `Auto Mode:` to **Disabled**.
- **Double-clicking a spot no longer tunes without switching mode** — As of v0.9.7, tuning from the Spot List also forwards mode information to the slice. If you do not want automatic mode switching, open the **Display** tab and set `Auto Mode:` to **Disabled**.

## Related

- [Enable DXCC coloring from an ADIF log](enable-dxcc-coloring-from-an-adif-log.md)
- [SpotHub overview](overview.md)
<!-- docmesh:llm version=v0.9.7 date=2026-05-03 -->