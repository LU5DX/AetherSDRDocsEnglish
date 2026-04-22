# Enable DXCC Coloring from an ADIF Log

DXCC coloring overlays spot labels on the panadapter with colors that reflect your worked, confirmed, or needed status for each entity. To drive that coloring, AetherSDR reads an ADIF log file you export from your logging software.

## Before you start

- You have an ADIF (.adi or .adif) log file exported from your logging software.
- The spot overlay is active: `IsSpotsEnabled` is enabled. If spots are not visible on the panadapter, DXCC coloring will have no visible effect.
- At least one spot source (DX cluster, RBN, WSJT-X, etc.) is connected and delivering spots.

## Steps

1. Open `Settings > SpotHub...`.
2. Click the **Display** tab.
3. Click **DXCC Coloring** to enable it. The toggle must be active for coloring to apply.
4. Click **Log File (ADIF):** to open a file browser, then select your ADIF log file.
5. Confirm the DXCC stats indicator below the control shows a non-zero imported QSO count. This confirms the file was parsed successfully.
6. If your logging software updates the ADIF file automatically while AetherSDR is running, click **Auto-Reload Log:** to enable it. AetherSDR will re-read the file whenever it changes on disk.

## What each control does

| Control | What it does | Persisted key |
|---|---|---|
| **DXCC Coloring** (toggle) | Master switch. Enables or disables DXCC-based spot coloring on the panadapter. | `DxccColoringEnabled` |
| **Log File (ADIF):** (button) | Opens a file picker. The selected path is saved and the file is parsed immediately. | `DxccAdifPath` |
| **Auto-Reload Log:** (toggle) | Re-reads the ADIF file automatically whenever it changes on disk. | `DxccAutoReload` |

## Tips

- The DXCC stats indicator in the dialog shows the number of QSOs imported from the ADIF file. If it reads zero after loading, the file may be empty or in an unsupported format.
- If your logger appends to the ADIF file in real time (common with Log4OM, DXKeeper, and similar applications), enable **Auto-Reload Log:** so your worked status stays current without reopening the dialog.
- DXCC coloring works alongside per-source spot colors. If **Override Colors:** is also active, the override color takes precedence. Disable **Override Colors:** if DXCC coloring is not appearing as expected.

## Troubleshooting

- **DXCC stats shows zero QSOs after selecting the file** — The file may not be a valid ADIF format, or it may be empty. Re-export from your logging software and try again.
- **Spot colors on the panadapter do not change after enabling DXCC Coloring** — Check that **Override Colors:** is not active on the **Display** tab; it will override DXCC coloring. Also confirm that **Spots:** is enabled.
- **Colors do not update when a new QSO is logged** — Enable **Auto-Reload Log:** so AetherSDR detects file changes automatically.

## Related

- [Auto-reload ADIF log when updated by a logger](auto-reload-adif-log-when-updated-by-a-logger.md)
- [Pick colors for each spot source](pick-colors-for-each-spot-source.md)
- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
- [SpotHub overview](overview.md)
