# Net Scheduler overview

The Net Scheduler helps you manage recurring on-air nets — think weekly club nets, daily DX nets, or monthly ARES drills. You can create entries with recurrence rules, set reminders that show a banner on the panadapter, and tune to a net with one click. Schedules can be imported or exported as JSON for backup or sharing.

## How it works

1. Open the dialog via `Tools > Net Scheduler...`.
2. The **Net table** lists every scheduled net with its name, frequency, recurrence rule, next occurrence, and reminder time. Double-click a row, or select it and click **Tune Now**, to QSY the active slice.
3. **Add Net** opens the net editor where you supply a name, frequency, mode, **Recurrence rule**, and **Reminder** time.
4. **Capture Current** grabs the current VFO frequency, mode, and filter settings to pre-fill a new or existing entry.
5. **Edit / Delete** modifies or removes the selected net.
6. **Import / Export** saves or loads the entire schedule as a `.json` file.
7. When a net is due, a reminder banner appears on the panadagger the specified number of minutes beforehand.

A **Next net** indicator displays the name and countdown to the next upcoming scheduled net.

## What each control does

| Control | Default | Valid range | Behavior |
|---|---|---|---|
| Net table | — | — | Sortable table of scheduled nets. Double-click or use **Tune Now** to QSY. Mirrors the Memory dialog table layout. |
| Add Net | — | — | Opens the net editor to create a new entry with name, frequency, mode, recurrence rule, and reminder settings. |
| Edit / Delete | — | — | Edit the selected net entry or delete it from the schedule. |
| Tune Now | — | — | Tunes the active slice to the selected net's frequency with stored mode and filter settings. Uses the same recall path as memory recalls. |
| Capture Current | — | — | Captures the current VFO frequency, mode, and filter as a tuning preset for a new or existing net. |
| Import / Export | — | — | Import or export the net schedule as a JSON file for backup or sharing. |
| Recurrence rule | Weekly | Once / Daily / Weekly / Biweekly / Monthly | How often the net repeats. Sets the schedule planner's recurrence engine. |
| Reminder | 5 min | 1–60 min | Minutes before net start to show the panadapter reminder banner. |

## Related

- [Create a recurring net schedule](create-a-recurring-net-schedule.md)
- [Edit or delete a scheduled net](edit-or-delete-a-scheduled-net.md)
- [Tune to a net with one click](tune-to-a-net-with-one-click.md)
- [Capture the current frequency as a net preset](capture-the-current-frequency-as-a-net-preset.md)
- [Import or export net schedules](import-or-export-net-schedules.md)
- [Set a reminder for an upcoming net](set-a-reminder-for-an-upcoming-net.md)
