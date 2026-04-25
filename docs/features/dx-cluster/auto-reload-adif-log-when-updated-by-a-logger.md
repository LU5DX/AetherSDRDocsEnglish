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

## Tips

- If your logger writes a temporary file and then renames it into place, the file watcher may not detect every save. Point your logger to write directly to the file at the path stored in `DxccAdifPath` for reliable detection.
- For large ADIF files, AetherSDR reads only the last 500 lines on each reload to avoid blocking the UI.

## Troubleshooting

- **Spot colors do not update after logging a new QSO** — Verify that `Auto-Reload Log:` is enabled and that `DXCC Coloring` is also enabled. Check that your logger is writing to the exact same file path shown next to `Log File (ADIF):`. If the path has changed, click `Log File (ADIF):` to re-select the file.
- **DXCC stats indicator shows 0 QSOs** — The ADIF file may not be readable or may be empty. Open the file in a text editor to confirm it contains valid ADIF records, then reload AetherSDR or re-select the file using `Log File (ADIF):`.

## Related

- [Enable DXCC coloring from an ADIF log](enable-dxcc-coloring-from-an-adif-log.md)
- [SpotHub overview](overview.md)
