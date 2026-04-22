# Create a new transverter entry

Use this page to add a transverter definition to your FLEX-8600. Once created, the radio exposes the transverter's IF-to-RF frequency offset so you can tune on the actual operating frequency rather than the IF frequency.

## Before you start

- AetherSDR must be connected to the radio. The XVTR tab is only active while a radio connection is present.
- Know the IF frequency range your transverter uses and its RF offset.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **XVTR** tab.
3. Click **Create New Transverter**.
4. A new nested tab appears inside the XVTR tab. Configure the entry using the fields on that tab.
5. To restrict the entry to receive only, enable **RX Only:**.
6. To delete an entry you no longer need, click **Remove (xvtr)** on its tab.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Create New Transverter** | Button | Adds a new transverter entry and opens its configuration tab. |
| **RX Only:** | Toggle button | When enabled, prevents transmitting through this transverter. |
| **Remove (xvtr)** | Button | Permanently deletes the transverter definition from the radio. |

## Tips

- Each transverter gets its own nested tab inside the XVTR tab. If you have multiple transverters, switch between them using those inner tabs.
- **RX Only:** is useful during initial setup when you want to verify receive operation before allowing transmit.

## Related

- [Radio Setup overview](overview.md)
- [Set per-band TX max power and tune mode](set-per-band-tx-max-power-and-tune-mode.md)
