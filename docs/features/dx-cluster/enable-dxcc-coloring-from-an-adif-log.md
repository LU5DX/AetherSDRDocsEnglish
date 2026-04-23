# Enable DXCC Coloring from an ADIF Log

DXCC coloring overlays worked, confirmed, and needed status on panadapter spots by comparing each spot's callsign against your ADIF log. This lets you see at a glance which stations represent new entities, new band-slots, or already-worked contacts.

## Before you start

- AetherSDR is running and at least one spot source is configured and producing spots. Spots must be visible on the panadapter for coloring to have any visible effect.
- You have an ADIF log file exported from your logging software and accessible on the local filesystem.

## Steps

1. Click `Settings > SpotHub...` to open the SpotHub dialog.
2. Click the **Display** tab.
3. Click **DXCC Coloring** to enable it. The toggle activates DXCC-based spot coloring.
4. Click **Log File (ADIF):** to open a file browser.
5. Navigate to your ADIF log file and select it. The path is saved to `DxccAdifPath`. The DXCC stats indicator in the dialog will show the number of QSOs imported once the file is read.
6. If your logging software updates the ADIF file while AetherSDR is running, click **Auto-Reload Log:** to enable automatic re-reading when the file changes. This saves to `DxccAutoReload`.

## What each control does

| Control | Behavior | Setting key |
|---|---|---|
| **DXCC Coloring** | Master toggle. Colors panadapter spots by worked/confirmed/needed status. | `DxccColoringEnabled` |
| **Log File (ADIF):** | Opens a file browser to select the ADIF log file that drives DXCC coloring. | `DxccAdifPath` |
| **Auto-Reload Log:** | When enabled, re-reads the ADIF file automatically whenever it changes on disk. | `DxccAutoReload` |

## Tips

- The DXCC stats indicator in the SpotHub dialog shows the count of QSOs imported from the selected ADIF file. If the count reads zero after selecting a file, verify the file is a valid ADIF export and is not empty.
- Enable **Auto-Reload Log:** if your logger writes to the ADIF file in real time. Coloring will update within seconds of a new QSO being logged without requiring any manual action.
- DXCC coloring applies on top of the spot overlay. Ensure **Spots:** is set to Enabled on the **Display** tab or no spots will appear regardless of coloring settings.

## Troubleshooting

- **Spots appear but show no DXCC coloring** — Confirm **DXCC Coloring** is toggled on and that a valid ADIF file path is set under **Log File (ADIF):**. Check the DXCC stats indicator for a non-zero QSO count.
- **DXCC stats show 0 QSOs after loading a file** — The file may not be a valid ADIF format, or it may be empty. Re-export from your logger and select the new file again using **Log File (ADIF):**.
- **Coloring does not update after new QSOs are logged** — Enable **Auto-Reload Log:**. If it is already enabled, confirm your logging software is writing to the same file path stored in `DxccAdifPath`.

## Related

- [Auto-reload ADIF log when updated by a logger](auto-reload-adif-log-when-updated-by-a-logger.md)
- [SpotHub overview](overview.md)
- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
- [Pick colors for each spot source](pick-colors-for-each-spot-source.md)
