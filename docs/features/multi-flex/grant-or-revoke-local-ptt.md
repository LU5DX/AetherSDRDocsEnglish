# Grant or revoke local PTT

Use the multiFLEX Dashboard to claim local PTT authority for your station or to see which station currently holds it. This is necessary when multiple clients share the same FLEX-8600 and only one can transmit at a time.

## Before you start

- AetherSDR must be connected to the radio. The multiFLEX Dashboard requires an active radio connection.
- multiFLEX must be enabled on the radio. If it is not, see [Enable multiFLEX on the radio](enable-multiflex-on-the-radio.md).
- At least two stations must be connected for the PTT controls to appear.

## Steps

1. Click `Settings > multiFLEX...` to open the multiFLEX Dashboard.
2. Look at the **Stations table**. The LOCAL PTT column shows a check mark next to the station that currently holds PTT.
3. If your station does not hold PTT, a label reading `Enable Local PTT for this station (<your station name>):` appears below the table, followed by the Enable button.
4. Click `Enable` to claim local PTT for your station.
5. The check mark in the LOCAL PTT column moves to your station's row, confirming the change.
6. Click `Close` when finished.

## What each control does

| Control | Description |
|---|---|
| Enable (multiFLEX toggle) | Enables or disables multiFLEX on the radio. Displays as **Enabled** or **Disabled** depending on current state. |
| Stations table | Lists every connected multiFLEX client. Columns: LOCAL PTT, STATION, TX ANT, TX FREQ (MHz). Your station is highlighted in blue. |
| Local PTT label | Shows which station currently holds PTT, or prompts you to claim it for your station. Hidden when only one station is connected. |
| Enable (PTT) | Claims local PTT authority for your station. Only shown when your station does not currently hold PTT. |
| Close | Closes the multiFLEX Dashboard. |

## Tips

- The PTT controls (label and Enable button) are hidden when only one station is connected. They appear automatically once a second station joins.
- If your station already holds PTT and you select another station's row in the table, the label will read that the other station must claim PTT from their own client. You cannot push PTT authority to another operator from your side.
- Your station's row is always shown in blue in the STATION column, making it easy to identify your entry among multiple clients.

## Troubleshooting

- **Enable button is not visible** — Either your station already holds PTT, or only one station is currently connected. Check the LOCAL PTT column for the check mark. If you are the only connected station, no PTT negotiation is needed.
- **Check mark does not move after clicking Enable** — Confirm the radio connection is active and multiFLEX is enabled. The Enable button at the top of the dialog should read **Enabled**.
- **Local PTT label and Enable button are both hidden** — Only one client is connected to the radio. The controls appear only when two or more clients are present.

## Related

- [Enable multiFLEX on the radio](enable-multiflex-on-the-radio.md)
- [Check which antenna and frequency each TX station is using](check-which-antenna-and-frequency-each-tx-station-is-using.md)
- [See all stations connected to this FLEX](../../getting-started/setup/see-all-stations-connected-to-this-flex.md)
