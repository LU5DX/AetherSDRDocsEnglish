# Export memories for backup or sharing

Export one or more stored memory channels to a CSV file for safekeeping or to share with another operator.

## Before you start

- AetherSDR must be connected to your FLEX-8600 radio. The Memory Channels dialog requires an active radio connection.
- The memories you want to export must already exist in the memory table.

## Steps

1. Open `Settings > Memory...` to open the Memory Channels dialog.
2. Select the memories you want to export. Click a row to select it. Shift-click to select a range. Ctrl-click (or Command-click on macOS) to add or remove individual rows. To export every memory, click `Select All`.
3. Optionally, use the `Search:` field or the `Profile:` combo box to filter the table before selecting, so only the relevant memories are visible.
4. Click `Export...`.
5. In the file dialog that opens, confirm or change the save location and filename, then save the file. The default filename includes the current date and time and the AetherSDR version (for example, `AetherSDR_Memories_01-15-25_14_30_v4.1.5.csv`), saved to your home `Documents` folder.

## What each control does

| Control | Behavior |
|---|---|
| `Search:` | Filters the memory table by name. Clear with the built-in clear button or by deleting the text. |
| `Profile:` | Filters the memory table by the active global profile. |
| Memory table | Shows all memories matching the current filter. Selection count is shown in the `<N> selected` indicator at the bottom right. |
| `Select All` | Selects every row currently visible in the table. |
| `Export...` | Writes the selected memories to a CSV file of your choosing. |

## Tips

- The selection count indicator at the bottom of the dialog shows how many rows are currently selected, which helps confirm you have the right memories before clicking `Export...`.
- If you want to export only a single group, use the `Profile:` filter to narrow the table to that group first, then click `Select All` before exporting.
- The default export path is your home `Documents` folder. Change it in the file dialog if you prefer a different location.

## Related

- [Import memories from a CSV/JSON file](import-memories-from-a-csv-json-file.md)
- [Memory Channels overview](overview.md)
- [Filter memories by profile](filter-memories-by-profile.md)
- [Search memories by name](search-memories-by-name.md)
