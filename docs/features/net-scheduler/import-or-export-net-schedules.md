# Import or export net schedules

Save your net schedule as a JSON file for backup, transfer to another computer, or sharing with another AetherSDR user. You can also load a previously exported schedule back into the application.

## Before you start

- Ensure you have at least one net entry in the Net Scheduler table, or a previously exported JSON file ready to import.

## Steps

1. Open the Net Scheduler: `Tools > Net Scheduler...`  
2. Click **Import / Export**.  
3. To **export**:  
   - Select the destination folder and filename in the file dialog.  
   - Click **Save**. The schedule is written as a JSON file.  
4. To **import**:  
   - Select the JSON file to load.  
   - Click **Open**. Existing net entries are replaced by the imported schedule.  

## Tips

- The exported JSON file contains all net entries with their names, frequencies, modes, recurrence rules, reminder settings, and tuning presets.  
- Importing overwrites your current schedule — there is no merge. Export your existing schedule first if you want to keep it.  

## Troubleshooting

- **Import does nothing or shows no nets** — The selected file may not be a valid AetherSDR net schedule JSON. Make sure you are importing a file previously exported by AetherSDR.

## Related

- [Net Scheduler overview](overview.md)
- [Create a recurring net schedule](create-a-recurring-net-schedule.md)
- [Edit or delete a scheduled net](edit-or-delete-a-scheduled-net.md)
- [Tune to a net with one click](tune-to-a-net-with-one-click.md)
