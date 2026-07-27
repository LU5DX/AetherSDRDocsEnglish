# Set a reminder for an upcoming net

Configure AetherSDR to show a banner on the panadapter before a scheduled net starts, so you don't miss your weekly or daily on-air gathering.

## Before you start

- You need at least one net entry in the schedule. If you haven't created one yet, see [Create a recurring net schedule](create-a-recurring-net-schedule.md).
- A connection to the radio is not required to set reminders, but the banner will only appear while AetherSDR is running and connected.

## Steps

1. Open the Net Scheduler dialog: **Tools > Net Scheduler...**
2. Select the net entry you want a reminder for from the **Net table**.
3. Click **Edit**.
4. In the net editor, set the **Reminder** spinbox to the number of minutes before the net start time you want to be alerted (range: 1–60 minutes). The default is 5 minutes.
5. Confirm the **Recurrence rule** is set to the schedule you want (Once, Daily, Weekly, Biweekly, or Monthly).
6. Save the entry.

When the net is approaching, a banner will appear on the panadapter showing the net name and countdown.

## What each control does

| Control | Default | Valid range | Setting key | Behavior |
|---------|---------|-------------|-------------|----------|
| **Reminder** | 5 min | 1–60 min | None | Minutes before net start to show the reminder banner on the panadapter. |
| **Recurrence rule** | Weekly | Once / Daily / Weekly / Biweekly / Monthly | None | How often the net repeats. Affects when the reminder fires. |

## Tips

- To remove a reminder, set the **Reminder** spinbox to its minimum value (1 minute) or delete the net entry entirely.
- The **Next net** indicator in the Net Scheduler dialog shows the name and countdown to the next upcoming net, so you can verify your reminder settings.

## Related

- [Net Scheduler overview](overview.md)
- [Create a recurring net schedule](create-a-recurring-net-schedule.md)
- [Edit or delete a scheduled net](edit-or-delete-a-scheduled-net.md)
