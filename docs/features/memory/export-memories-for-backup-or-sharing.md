# Export memories for backup or sharing

Export lets you save selected memory channels to a CSV file on your computer so you can back them up or share them with other operators.

## Before you start

- AetherSDR must be connected to your FLEX-8600 radio. The Memory Channels dialog requires an active radio connection.
- Open the Memory Channels dialog via `Settings > Memory...`.

## Steps

1. Open `Settings > Memory...`.
2. Select the memories you want to export. Click a row to select it. Shift-click to select a range. Ctrl-click (or Command-click on macOS) to add or remove individual rows. Click `Select All` to select every row in the current view.
3. Click `Export...`.
4. In the file dialog, choose a destination folder and confirm or change the filename. The default filename is generated automatically in the form `AetherSDR_Memories_<date-time>_v<version>.csv` and is placed in your home `Documents` folder.
5. Confirm the save. The selected memories are written to the CSV file.

## What each control does

| Control | Behavior |
|---|---|
| `Select All` | Selects every row currently visible in the memory table. |
| `Export...` | Exports the currently selected rows to a CSV file. |
| `Search:` | Filters the table by memory name. Use this to narrow the table before selecting rows for export. |
| `Profile:` | Filters the table by active global profile. Use this to isolate memories belonging to a specific profile before exporting. |

## Tips

- Use `Search:` or `Profile:` to filter the table before selecting, so `Select All` captures only the rows you want.
- The exported file is sorted by frequency, then by internal index, regardless of the current sort order in the table.

## Related

- [Import memories from a CSV/JSON file](import-memories-from-a-csv-json-file.md)
- [Memory Channels overview](overview.md)
- [Filter memories by profile](filter-memories-by-profile.md)
- [Search memories by name](search-memories-by-name.md)
