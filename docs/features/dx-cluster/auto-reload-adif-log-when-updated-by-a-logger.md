# Auto-reload ADIF log when updated by a logger

When DXCC coloring is enabled, AetherSDR can watch your ADIF log file and re-read it automatically whenever your logging software writes a new QSO. This keeps spot colors current without requiring you to reload manually.

## Before you start

- DXCC coloring must be enabled and an ADIF file must already be loaded. See [Enable DXCC coloring from an ADIF log](enable-dxcc-coloring-from-an-adif-log.md).
- Your logging software must write updates to the same ADIF file path that AetherSDR has loaded.

## Steps

1. Open `Settings > SpotHub...`.
2. Click the **Display** tab.
3. Confirm that **DXCC Coloring** is enabled (the toggle shows as active).
4. Confirm that **Log File (ADIF):** shows the correct file path.
5. Click **Auto-Reload Log:** to enable it.

AetherSDR will now watch the file and re-read it each time the file changes. Spot colors on the panadapter update to reflect the new log contents.

## What each control does

| Control | Behavior | Persisted setting |
|---|---|---|
| **DXCC Coloring** | Master toggle for coloring spots by worked/confirmed/needed DXCC status. | `DxccColoringEnabled` |
| **Log File (ADIF):** | Opens a file picker to select the ADIF log file that drives DXCC coloring. The chosen path is saved. | `DxccAdifPath` |
| **Auto-Reload Log:** | When enabled, re-reads the ADIF file whenever it is modified on disk. | `DxccAutoReload` |

## Tips

- Point your logging software's ADIF export at the same file path stored in `DxccAdifPath`. Many loggers support a continuous or on-QSO-save export option that writes to a fixed file.
- If your logger writes a new file each export rather than updating in place, the file watcher will not detect the change. Configure your logger to overwrite the same file.

## Troubleshooting

- **Spot colors do not update after logging a QSO** — Verify that **Auto-Reload Log:** is enabled on the **Display** tab. Also confirm that your logger is writing to the exact file path shown next to **Log File (ADIF):**. If the logger writes to a different file or renames the file on each export, the watcher will not trigger.
- **DXCC Coloring toggle is off** — **Auto-Reload Log:** has no effect unless **DXCC Coloring** is also enabled. Enable **DXCC Coloring** first.

## Related

- [Enable DXCC coloring from an ADIF log](enable-dxcc-coloring-from-an-adif-log.md)
- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
