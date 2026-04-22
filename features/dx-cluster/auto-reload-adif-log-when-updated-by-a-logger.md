# Auto-reload ADIF log when updated by a logger

When DXCC coloring is active, AetherSDR can watch your ADIF log file and reload it automatically whenever your logging software saves a new QSO. This keeps the worked/confirmed/needed spot colors on the panadapter current without any manual intervention.

## Before you start

- DXCC coloring must be enabled and an ADIF log file must already be loaded. See [Enable DXCC coloring from an ADIF log](enable-dxcc-coloring-from-an-adif-log.md).
- Your logging software must write QSOs to the same ADIF file that AetherSDR has loaded.

## Steps

1. Open `Settings > SpotHub...`.
2. Click the **Display** tab.
3. Confirm that **DXCC Coloring** is active (the toggle shows as enabled) and that **Log File (ADIF):** shows the correct file path.
4. Click **Auto-Reload Log:** to enable it.

AetherSDR will now monitor the file. Each time the file changes on disk, the ADIF log is re-read and the DXCC coloring on the panadapter updates automatically.

## What each control does

| Control | Behavior | Setting key |
|---|---|---|
| **DXCC Coloring** | Master toggle. Colors spots by worked/confirmed/needed status based on the loaded ADIF log. | `DxccColoringEnabled` |
| **Log File (ADIF):** | Opens a file picker to select the ADIF log file. The chosen path is persisted. | `DxccAdifPath` |
| **Auto-Reload Log:** | Re-reads the ADIF file whenever it changes on disk. | `DxccAutoReload` |

## Tips

- If your logger overwrites the ADIF file in place on each save (common with Log4OM, DXKeeper, and similar), auto-reload will pick up every new QSO within seconds of it being written.
- Disabling **Auto-Reload Log:** does not clear the already-loaded log data. DXCC coloring continues using the last successfully read file until you reload manually or change the file.

## Troubleshooting

- **Spot colors do not update after logging a QSO** — Confirm **Auto-Reload Log:** is enabled on the **Display** tab. Also check that your logger is writing to the exact file shown in **Log File (ADIF):**. Some loggers write to a temporary file and rename it; this may not trigger a reload on all platforms. In that case, disable **Auto-Reload Log:**, reopen `Settings > SpotHub...`, and click **Log File (ADIF):** to reload manually.
- **DXCC Coloring toggle is available but produces no color changes** — The imported QSO count shown in the DXCC stats indicator will be zero if the ADIF file path is invalid or the file is unreadable. Re-select the file using **Log File (ADIF):**.

## Related

- [Enable DXCC coloring from an ADIF log](enable-dxcc-coloring-from-an-adif-log.md)
- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
- [SpotHub overview](overview.md)
