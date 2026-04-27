# Create a new transverter entry

Use this page to add a transverter definition to your FLEX-8600 so AetherSDR knows the IF-to-RF frequency offset and operating parameters for your transverter band.

## Before you start

- The radio must be connected. Radio Setup requires an active radio connection.
- Know the IF frequency range your transverter uses and the RF frequency offset you want to display.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **XVTR** tab.
3. Click **Create New Transverter**.
4. A new nested tab appears. Configure the fields for the new entry on that tab.
5. To restrict the entry to receive only, set **RX Only:** to the enabled state.
6. To delete an entry you no longer need, click **Remove** on that entry's tab.
7. Close the dialog with **Close**.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Create New Transverter** | Button | Adds a new transverter entry and opens its configuration tab. |
| **RX Only:** | Toggle button | Forces the transverter to receive-only, preventing TX through it. |
| **Remove** | Button | Permanently deletes the selected transverter definition. |

## Tips

- Each transverter gets its own nested tab inside the XVTR tab. If you have multiple transverters, use those tabs to switch between entries.
- If you need to return to this dialog later to adjust a transverter, reopen `Settings > Radio Setup...` and go directly to the **XVTR** tab.

## Related

- [Radio Setup overview](overview.md)
- [Set per-band TX max power and tune mode](set-per-band-tx-max-power-and-tune-mode.md)
