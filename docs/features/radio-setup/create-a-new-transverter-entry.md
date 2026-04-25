# Create a new transverter entry

This page explains how to add a transverter definition to your FLEX-8600 so AetherSDR can display and tune the transverter's output frequency instead of the radio's IF frequency.

## Before you start

- AetherSDR must be connected to the radio. The Radio Setup dialog requires an active radio connection.
- Know the transverter's IF frequency range and output frequency offset before you begin.

## Steps

1. Click `Settings > Radio Setup...` to open the Radio Setup dialog.
2. Click the **XVTR** tab.
3. Click **Create New Transverter**.

A new transverter entry appears as a nested tab inside the XVTR tab.

4. Configure the entry using the controls on the new tab (frequency range, offset, name, and RX-only setting — see below).
5. To remove an entry at any time, select its tab and click **Remove**.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Create New Transverter** | Button | Adds a new transverter entry and creates a nested tab for it. |
| **RX Only:** | Toggle button | When enabled, prevents transmitting through this transverter. |
| **Remove** | Button | Permanently deletes the selected transverter entry. |

## Tips

- The XVTR tab uses nested tabs — one tab per transverter, plus a tab for creating new entries. If you have multiple transverters, select the correct nested tab before clicking **Remove**.
- If you want a transverter that cannot transmit (for example, a receive-only downconverter), enable **RX Only:** immediately after creating the entry.

## Related

- [Radio Setup overview](overview.md)
- [Set per-band TX max power and tune mode](set-per-band-tx-max-power-and-tune-mode.md)
