# Export memories for backup or sharing

Export one or more memory channels to a CSV file so you can back them up or share them with another operator.

## Before you start

- A Flex radio must be connected. The Memory Channels dialog requires an active radio connection.
- The memories you want to export must already exist. See [Add a memory at current frequency](add-a-memory-at-current-frequency.md) if you need to create them first.

## Steps

1. Open `Settings > Memory...`.
2. Select the memories you want to export. Click a row to select it. Shift-click selects a range. Ctrl-click (or Command-click on macOS) adds or removes individual rows. To export every memory, click `Select All`.
3. Click `Export...`.
4. In the file dialog, choose a destination folder and confirm or change the filename. The default filename is of the form `AetherSDR_Memories_<date-time>_v<version>.csv` inside your Documents folder.
5. Confirm the save. The selected memories are written to the CSV file.

## What each control does

| Control | Behavior |
|---|---|
| `Select All` | Selects every row in the memory table. |
| `Export...` | Exports the currently selected memory rows to a CSV file. |
| `Profile:` | Filters the table by the active global profile, which narrows which memories are visible and selectable before export. |
| `Search:` | Filters the table by memory name, letting you locate specific memories before selecting them. |
| Selection count | Shows the number of currently selected rows (for example, `3 selected`) in the lower-right area of the dialog. |

## Tips

- If you only want to export memories belonging to one group, use the `Profile:` combo box to filter the table before clicking `Select All`. Only the visible rows matching that profile will be shown, making bulk selection straightforward.
- The default export path places the file in your home `Documents` folder with a timestamp and version number in the name, which helps you keep multiple backups distinct.

## Related

- [Import memories from a CSV/JSON file](import-memories-from-a-csv-json-file.md)
- [Add a memory at current frequency](add-a-memory-at-current-frequency.md)
- [Delete one or more memories](delete-one-or-more-memories.md)
- [Filter memories by profile](filter-memories-by-profile.md)
- [Memory Channels overview](overview.md)
