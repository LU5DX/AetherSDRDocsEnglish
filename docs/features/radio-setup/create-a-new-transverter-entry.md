# Create a new transverter entry

Use this page to add a transverter definition to your FLEX-8600 so AetherSDR can display and tune RF frequencies above the radio's native range.

## Before you start

- AetherSDR must be connected to the radio. The Radio Setup dialog requires an active radio connection.
- Know the IF frequency your transverter uses and the RF frequency offset you want to apply.

## Steps

1. Click `Settings > Radio Setup...` to open the Radio Setup dialog.
2. Click the `XVTR` tab.
3. Click `Create New Transverter`.
4. A new nested tab appears for the transverter entry. Configure the entry using the controls on that tab.
5. To restrict the transverter to receive only, enable `RX Only:`.
6. Close the dialog when finished. Settings are sent to the radio immediately.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| `Create New Transverter` | Push button | Adds a new transverter entry and opens a nested tab for it. |
| `RX Only:` | Toggle button | When enabled, prevents transmitting through this transverter. |
| `Remove (xvtr)` | Push button | Deletes the selected transverter definition from the radio. |

## Tips

- Each transverter entry appears as its own nested tab inside the XVTR tab. To edit an existing entry, click its tab.
- Use `Remove (xvtr)` only if you no longer need the entry. The deletion is immediate.

## Related

- [Radio Setup overview](overview.md)
- [Set per-band TX max power and tune mode](set-per-band-tx-max-power-and-tune-mode.md)
