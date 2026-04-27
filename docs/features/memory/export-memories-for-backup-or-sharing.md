# Export memories for backup or sharing

Export your stored memory channels to a CSV file for safekeeping or to share with other operators. You can export all memories at once or a specific selection.

## Before you start

- AetherSDR must be connected to the radio. The Memory Channels dialog requires an active radio connection.
- You must have at least one memory channel stored on the radio.

## Steps

1. Open `Settings > Memory...` to open the Memory Channels dialog.
2. Select the memories you want to export from the memory table. Click a row to select it. Shift-click to select a range. Ctrl-click (or Command-click on macOS) to add or remove individual rows.
3. To export every memory, click `Select All` to select all rows before proceeding.
4. Click `Export...`.
5. In the file dialog that opens, confirm or change the destination path and filename. The default filename is in the form `AetherSDR_Memories_<date-time>_v<version>.csv` and is placed in your home `Documents` folder.
6. Confirm the save. AetherSDR writes the selected memories to the CSV file.

## Tips

- If you want to export only the memories belonging to a particular group, use the `Profile:` combo box to filter the table to that group first, then click `Select All` before clicking `Export...`.
- The exported file is sorted by frequency, then by internal memory index, regardless of the current table sort order.
- The exported CSV file can be imported back into AetherSDR using `Import...`.

## Related

- [Import memories from a CSV/JSON file](import-memories-from-a-csv-json-file.md)
- [Add a memory at current frequency](add-a-memory-at-current-frequency.md)
- [Filter memories by profile](filter-memories-by-profile.md)
- [Memory Channels overview](overview.md)
