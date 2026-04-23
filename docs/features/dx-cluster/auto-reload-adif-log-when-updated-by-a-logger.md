# Auto-reload ADIF log when updated by a logger

When DXCC coloring is active, AetherSDR can watch your ADIF log file and reload it automatically whenever your logging software writes a new QSO. This keeps worked/confirmed/needed status current on the panadapter without manual intervention.

## Before you start

- DXCC coloring must be enabled and an ADIF file must already be selected. See [Enable DXCC coloring from an ADIF log](enable-dxcc-coloring-from-an-adif-log.md).
- Your logging software must write updates to the same ADIF file path stored in `DxccAdifPath`.

## Steps

1. Open `Settings > SpotHub...`.
2. Click the `Display` tab.
3. Confirm that `DXCC Coloring` is enabled (the toggle shows as active).
4. Confirm that `Log File (ADIF):` shows the correct file path.
5. Click `Auto-Reload Log:` to enable it.

The toggle activates file-change monitoring on the path stored in `DxccAdifPath`. Each time your logger saves the file, AetherSDR re-reads it and updates DXCC coloring on the panadapter.

## What each control does

| Control | Behavior | Setting key |
|---|---|---|
| `DXCC Coloring` | Master toggle; colors spots by worked/confirmed/needed status. Must be on for auto-reload to have any effect. | `DxccColoringEnabled` |
| `Log File (ADIF):` | Opens a file picker and stores the selected ADIF path. | `DxccAdifPath` |
| `Auto-Reload Log:` | Monitors the ADIF file for changes and reloads it automatically when the file is updated. | `DxccAutoReload` |

## Tips

- If your logger writes to a temporary file and then renames it over the target path, the reload will trigger on the rename as long as the final path matches `DxccAdifPath`.
- Disabling `DXCC Coloring` while `Auto-Reload Log:` is on has no effect on the toggle state; the file watcher resumes coloring updates if you re-enable `DXCC Coloring` without changing any other setting.

## Troubleshooting

- **Spots do not update after a new QSO is logged** — Confirm `Auto-Reload Log:` is enabled and that `Log File (ADIF):` shows the exact file your logger is writing to. If your logger writes to a different path or a temp file that is never renamed to the configured path, AetherSDR will not detect the change. Re-select the file using `Log File (ADIF):` after confirming the correct path.
- **DXCC coloring does not reflect the reloaded log** — Verify `DXCC Coloring` is enabled. The auto-reload has no visible effect while the master toggle is off.

## Related

- [Enable DXCC coloring from an ADIF log](enable-dxcc-coloring-from-an-adif-log.md)
- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
