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

## Tips

- The DXCC stats indicator in the dialog shows how many QSOs were imported from the ADIF file. If it reads zero after loading, verify the file is valid ADIF.
- The **Log File (ADIF):** button stores the path persistently. You do not need to re-select the file after restarting AetherSDR.
- Enabling **Auto-Reload Log:** removes the need to reopen the dialog after logging a new contact — the spot colors on the panadapter update as soon as your logger writes to the file.
- DXCC coloring is independent of per-source spot colors. If **Override Colors:** is also active, see [Pick colors for each spot source](pick-colors-for-each-spot-source.md) for how those settings interact.

## Troubleshooting

- **DXCC stats shows 0 QSOs after selecting a file** — The file may not be valid ADIF, may be empty, or may use an encoding AetherSDR cannot read. Export a fresh ADIF from your logger and try again.
- **Spot colors do not change after enabling DXCC Coloring** — Confirm the **Spots:** toggle on the **Display** tab is enabled (`IsSpotsEnabled`). Also check that **Override Colors:** (`IsSpotsOverrideColorsEnabled`) is not active, as it forces a single color for all spots regardless of DXCC status.
- **New contacts are not reflected on spots** — Enable **Auto-Reload Log:** so AetherSDR detects file changes, or manually re-select the log file with **Log File (ADIF):** to trigger a fresh import.

## Related

- [Auto-reload ADIF log when updated by a logger](auto-reload-adif-log-when-updated-by-a-logger.md)
- [Pick colors for each spot source](pick-colors-for-each-spot-source.md)
- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
- [SpotHub overview](overview.md)
