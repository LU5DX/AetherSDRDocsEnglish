# Enable multiFLEX on the radio

multiFLEX lets multiple stations share a single FLEX-8600 simultaneously. This page explains how to enable or disable multiFLEX from within AetherSDR.

## Before you start

- AetherSDR must be connected to the radio. The multiFLEX Dashboard is not available without an active radio connection.
- You need operator access to the FLEX-8600. Enabling multiFLEX is a radio-wide setting that affects all connected stations.

## Steps

1. Click `Settings > multiFLEX...` to open the multiFLEX Dashboard.
2. At the top of the dialog, locate the enable/disable button. When multiFLEX is off, the button reads "Disabled". When it is on, it reads "Enabled".
3. Click the button to toggle multiFLEX on or off. The button label and color update immediately to reflect the new state.
4. Click `Close` to dismiss the dialog.

## What each control does

| Control | Description |
|---|---|
| Enable / Disable button | Toggles multiFLEX on or off for the radio. Displays "Enabled" (green) when active and "Disabled" (red) when inactive. |
| Stations table | Lists every multiFLEX client currently connected. Columns: LOCAL PTT, STATION, TX ANT, TX FREQ (MHz). |
| Enable (PTT) | Toggles local PTT authority for this station. Appears only when more than one station is connected and this station does not currently hold PTT. |
| Close | Closes the multiFLEX Dashboard. |

## Tips

- When only one station is connected, the PTT controls are hidden. They appear automatically once a second station joins.
- Your own station is highlighted in the Stations table so you can identify it among other connected clients.
- Clicking the enable/disable button takes effect immediately on the radio. You do not need to disconnect and reconnect.

## Related

- [multiFLEX Dashboard overview](overview.md)
- [Grant or revoke local PTT](grant-or-revoke-local-ptt.md)
- [Check which antenna and frequency each TX station is using](check-which-antenna-and-frequency-each-tx-station-is-using.md)
- [See all stations connected to this FLEX](../../getting-started/setup/see-all-stations-connected-to-this-flex.md)
