# Create a recurring net schedule

Set up a personal net schedule with recurrence rules so AetherSDR reminds you before each weekly, daily, or monthly net and lets you tune to its frequency with one click.

## Before you start

- AetherSDR must be running (a radio connection is not required to create or edit schedule entries).
- Know the net’s frequency, mode, and how often it repeats.

## Steps

1. Open the Net Scheduler: `Tools > Net Scheduler...`
2. Click **Add Net**.
3. In the net editor, enter a name for the net.
4. Set the frequency and mode using one of these methods:
   - Manually type the frequency and select a mode from the available options.
   - Click **Capture Current** to copy the active slice’s frequency, mode, and filter settings into the new entry.
5. From the **Recurrence rule** combo box, choose how often the net repeats:
   - **Once** — runs a single time only
   - **Daily**
   - **Weekly**
   - **Biweekly**
   - **Monthly**
6. Set the **Reminder** spinbox to the number of minutes before the net start time when you want the reminder banner to appear on the panadapter (1–60 minutes, default 5 min).
7. Confirm the entry. The new net appears in the **Net table** sorted by start time.

## What each control does

| Control | What it does | Default / Range | Setting key |
|---------|--------------|-----------------|-------------|
| **Net table** | Sortable list of all scheduled nets showing name, frequency, recurrence rule, next occurrence, and reminder time. Double-click to QSY. | — | `Nets` |
| **Add Net** | Opens the net editor to create a new schedule entry. | — | — |
| **Edit / Delete** | Edit the selected net’s properties or remove it from the schedule. | — | — |
| **Tune Now** | Immediately tunes the active slice to the selected net’s frequency, mode, and filter. | — | — |
| **Capture Current** | Fills the current VFO frequency, mode, and filter into the net editor as a tuning preset. | — | — |
| **Import / Export** | Save or load the entire net schedule as a JSON file. | — | — |
| **Recurrence rule** | How often the net repeats. | **Once** / Daily / Weekly / Biweekly / Monthly | — |
| **Reminder** | Minutes before the net starts to show the panadapter reminder banner. | 5 min (1–60 min) | — |

## Tips

- Use **Capture Current** while tuned to a net’s usual frequency to avoid typing the exact kHz and mode manually.
- The **Next net** indicator in the Net Scheduler dialog shows the name of the next upcoming net and a countdown timer.

## Related

- [Overview](overview.md)
- [Capture the current frequency as a net preset](capture-the-current-frequency-as-a-net-preset.md)
- [Edit or delete a scheduled net](edit-or-delete-a-scheduled-net.md)
- [Set a reminder for an upcoming net](set-a-reminder-for-an-upcoming-net.md)
- [Tune to a net with one click](tune-to-a-net-with-one-click.md)
- [Import or export net schedules](import-or-export-net-schedules.md)
