# Enable DXCC Coloring from an ADIF Log

DXCC coloring lets AetherSDR highlight panadapter spots in different colors based on whether you have worked, confirmed, or still need a DXCC entity. You drive this by pointing AetherSDR at an ADIF log file exported from your logging software.

## Before you start

- You have an ADIF (.adi or .adif) log file exported from your logger.
- At least one spot source is active and spots are appearing on the panadapter. DXCC coloring only affects how existing spots are colored; it does not create spots on its own.
- Spot display is enabled: the `IsSpotsEnabled` toggle in SpotHub is on.

## Steps

1. Go to `Settings > SpotHub...`.
2. Click the **Display** tab.
3. Click **DXCC Coloring** to enable it. The toggle must be active before the log file path is used.
4. Click **Log File (ADIF):**. A file browser opens.
5. Navigate to your ADIF file and select it. The path is saved to `DxccAdifPath`.
6. Confirm the DXCC stats indicator below the controls shows a non-zero imported QSO count. This confirms the file was read successfully.
7. If you want AetherSDR to automatically re-read the file whenever your logger updates it, enable **Auto-Reload Log:**. This saves to `DxccAutoReload`.

## What each control does

| Control | What it does | Setting key |
|---|---|---|
| **DXCC Coloring** | Master toggle. Colors spots by worked/confirmed/needed DXCC status. | `DxccColoringEnabled` |
| **Log File (ADIF):** | Opens a file browser to select your ADIF log. The chosen path is persisted. | `DxccAdifPath` |
| **Auto-Reload Log:** | Re-reads the ADIF file automatically when it changes on disk. Useful when a logger writes to the file in real time. | `DxccAutoReload` |

## Tips

- The DXCC stats indicator in the dialog shows the number of QSOs imported from the ADIF file. If it reads zero after selecting a file, the file may be empty or in an unsupported format.
- If your logger continuously appends to the ADIF file during a session, enable **Auto-Reload Log:** so coloring stays current without reopening SpotHub.
- DXCC coloring is applied on top of spot source colors. If **Override Colors:** is also enabled, the override color takes precedence. Disable **Override Colors:** if DXCC coloring is not visible.

## Troubleshooting

- **DXCC stats shows 0 QSOs after selecting a file** — The file may not be valid ADIF, may be empty, or may be open exclusively by another application. Close any exclusive file lock in your logger, re-export if necessary, and re-select the file.
- **Spot colors do not change after enabling DXCC Coloring** — Check that **Override Colors:** on the same **Display** tab is not active. Override Colors supersedes DXCC coloring. Also confirm that **Spots:** is enabled (`IsSpotsEnabled`).
- **Auto-Reload Log: does not pick up new QSOs** — Some loggers write to a temporary file and then rename it, which may not trigger a file-change notification. In that case, disable **Auto-Reload Log:** and re-select the file manually after each session.

## Related

- [Auto-reload ADIF log when updated by a logger](auto-reload-adif-log-when-updated-by-a-logger.md)
- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
- [Pick colors for each spot source](pick-colors-for-each-spot-source.md)
- [SpotHub overview](overview.md)
