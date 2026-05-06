# Enable DXCC Coloring from an ADIF Log

DXCC coloring lets AetherSDR mark panadapter spots by whether the DX entity has been worked, confirmed, or is still needed, based on contacts in your ADIF log file. This helps you quickly distinguish new entities from ones you have already logged.

## Before you start

- AetherSDR must be running. A radio connection is not required to configure this feature.
- You need an ADIF log file exported from your logging software. The file must use the standard `.adi` or `.adif` format.
- At least one spot source (DX cluster, RBN, WSJT-X, POTA, etc.) should be active so spots appear on the panadapter.

## Steps

1. Open `Settings > SpotHub...`.
2. Click the **Display** tab.
3. Click the **DXCC Coloring** toggle button to enable it. The button activates DXCC coloring (`DxccColoringEnabled`).
4. Click **Log File (ADIF):** to open a file chooser. Select your ADIF log file. The path is stored in `DxccAdifPath`.
5. Confirm the DXCC stats indicator updates to show the number of QSOs imported from the file.
6. If your logging software updates the ADIF file while AetherSDR is running and you want spots to reflect new contacts automatically, enable **Auto-Reload Log:** (`DxccAutoReload`).

## What each control does

| Control | Behavior | Setting key |
|---|---|---|
| **DXCC Coloring** | Master toggle. Colors panadapter spots by worked/confirmed/needed DXCC status. | `DxccColoringEnabled` |
| **Log File (ADIF):** | Opens a file picker. The chosen ADIF file is read to populate DXCC status. | `DxccAdifPath` |
| **Auto-Reload Log:** | When enabled, re-reads the ADIF file whenever it changes on disk. | `DxccAutoReload` |
| **Auto Mode:** | Auto-selects spot density based on zoom level. Defaults to **Enabled** as of v0.9.5.1. | `SpotsAutoMode` |
| **Spot Lines:** | Draws vertical lines from the spectrum up to each spot label. Disable during contests to reduce visual clutter. New in v0.9.7. | `IsSpotsLinesEnabled` |
| **Enable FreeDV Reporter reporting when RADE is active** | Enables station-reporting to the public FreeDV Reporter map (qso.freedv.org) whenever the RADE modem is active. Requires a valid callsign and grid square; if either field is blank or resolves to empty, the checkbox refuses to enable and displays a warning. | `FreeDvAutoReport` |
| **Callsign: (FreeDV Reporter)** | Callsign to report to the FreeDV Reporter map. Read-only when **Use radio (callsign)** is checked. Automatically updates if the radio's configured callsign changes while **Use radio (callsign)** is checked. | `FreeDvMyCallsign` |
| **Use radio (callsign)** | Pre-fills the callsign field from the radio's configured callsign and locks the field read-only. Defaults to enabled. | `FreeDvUseRadioCallsign` |
| **Grid Square: (FreeDV Reporter)** | Maidenhead grid square to report. Read-only when **Use GPS (grid)** is checked. | `FreeDvMyGrid` |
| **Use GPS (grid)** | Pre-fills the grid field from the radio's GPS module and locks the field read-only. Only shown on radio models that have GPS hardware. Defaults to enabled. | `FreeDvUseGpsGrid` |
| **Station Msg: (FreeDV Reporter)** | Optional free-text message shown beside the callsign on the public FreeDV Reporter map. | `FreeDvMyMessage` |
| Total Spots: | Live readout of how many spots are currently tracked across all sources. Updated whenever spots are added or cleared. Resets to 0 when **Clear All Spots** is pressed. | — |

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

- The DXCC stats indicator in the dialog shows how many QSOs were imported from the ADIF file. If it reads zero after loading, verify the file is valid ADIF.
- The **Log File (ADIF):** button stores the path persistently. You do not need to re-select the file after restarting AetherSDR.
- Enabling **Auto-Reload Log:** removes the need to reopen the dialog after logging a new contact — the spot colors on the panadapter update as soon as your logger writes to the file.
- DXCC coloring is independent of per-source spot colors. If **Override Colors:** is also active, see [Pick colors for each spot source](pick-colors-for-each-spot-source.md) for how those settings interact.
- **Auto Mode:** (`SpotsAutoMode`) defaults to **Enabled** as of v0.9.5.1. If you previously disabled it, check the current state on the **Display** tab after upgrading.
- **Spot Lines:** (`IsSpotsLinesEnabled`) defaults to **Enabled**. During contests or when the panadapter feels visually busy, disable this toggle on the **Display** tab to remove the vertical lines while keeping spot labels visible.
- When **Use radio (callsign)** is checked, the callsign field updates automatically if you change the callsign in Radio Setup without reopening SpotHub.
- Reporter broadcasting is build-gated by `HAVE_WEBSOCKETS`. On Windows it additionally requires `HAVE_RADE`. If the **Station Reporting** group or the enable checkbox is absent, your build does not include the required components.

## Troubleshooting

- **DXCC stats shows 0 QSOs after selecting a file** — The file may not be valid ADIF, may be empty, or may use an encoding AetherSDR cannot read. Export a fresh ADIF from your logger and try again.
- **Spot colors do not change after enabling DXCC Coloring** — Confirm the **Spots:** toggle on the **Display** tab is enabled (`IsSpotsEnabled`). Also check that **Override Colors:** (`IsSpotsOverrideColorsEnabled`) is not active, as it forces a single color for all spots regardless of DXCC status.
- **New contacts are not reflected on spots** — Enable **Auto-Reload Log:** so AetherSDR detects file changes, or manually re-select the log file with **Log File (ADIF):** to trigger a fresh import.
- **Double-clicking a spot does not switch mode** — Mode is derived from the spot comment text. If the comment does not contain a recognizable mode token, only the frequency changes.
- **Warning appears when enabling FreeDV Reporter** — Either the callsign or grid square field is blank. Fill in both fields (or check **Use radio (callsign)** / **Use GPS (grid)** to populate them from the radio) before enabling the checkbox.
- **Station Reporting group is not visible** — The FreeDV and reporting features require a build with `HAVE_WEBSOCKETS` support. On Windows, `HAVE_RADE` is also required. Contact your package maintainer if you need these features.

## Related

- [Auto-reload ADIF log when updated by a logger](auto-reload-adif-log-when-updated-by-a-logger.md)
- [Pick colors for each spot source](pick-colors-for-each-spot-source.md)
- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
- [SpotHub overview](overview.md)

<!-- docmesh:llm version=V0.9.7 date=2026-05-03 -->