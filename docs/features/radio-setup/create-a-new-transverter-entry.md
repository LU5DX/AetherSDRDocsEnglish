# Create a new transverter entry

Use this page to add a transverter definition to your FLEX-8600 so AetherSDR can apply the correct frequency offset and display the transverter's output frequency in the panadapter.

## Before you start

- AetherSDR must be connected to the radio. The XVTR tab is not available when offline.
- Know the IF frequency your transverter uses (the frequency the FLEX-8600 will actually transmit and receive on) and the output frequency range you want to display.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the `XVTR` tab.
3. Click `Create New Transverter`.

A new transverter entry appears as a nested tab inside the XVTR tab. Configure the entry using the controls described below.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| `Create New Transverter` | Button | Adds a new transverter entry as a nested tab. |
| `RX Only:` | Toggle button | When enabled, prevents transmitting through this transverter. Use this for receive-only converters or when you want to protect downstream hardware. |
| `Remove` | Button | Permanently deletes the selected transverter definition from the radio. |

## Tips

- If you only want to monitor a transverter band without risking a transmit into the converter, enable `RX Only:` immediately after creating the entry.
- To delete a transverter you no longer need, select its tab and click `Remove`.

## Related

- [Radio Setup overview](overview.md)
- [Set per-band TX max power and tune mode](set-per-band-tx-max-power-and-tune-mode.md)
