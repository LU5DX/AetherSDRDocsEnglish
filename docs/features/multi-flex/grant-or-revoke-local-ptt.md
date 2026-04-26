# Grant or revoke local PTT

Use the multiFLEX Dashboard to claim local PTT authority for your station or to see which station currently holds it. This is necessary when multiple clients share a single FLEX-8600 and only one may transmit at a time.

## Before you start

- AetherSDR must be connected to the radio. The multiFLEX Dashboard requires an active radio connection.
- multiFLEX must be enabled on the radio. If the Enable button in the dashboard shows "Disabled", see [Enable multiFLEX on the radio](enable-multiflex-on-the-radio.md) before continuing.
- At least two stations must be connected for the PTT controls to appear. With only one station connected, the PTT section is hidden.

## Steps

1. Click `Settings > multiFLEX...` to open the multiFLEX Dashboard.
2. Check the Stations table. The LOCAL PTT column shows a check mark next to the station that currently holds PTT.
3. If your station does not hold PTT, a label reading `Enable Local PTT for this station (<your station name>):` appears below the table, along with an Enable button.
4. Click Enable to claim local PTT for your station.

To release PTT, another station must claim it from their own client. You cannot grant PTT to another station from your client. If you select another station's row while you hold PTT, the dashboard displays a message indicating that the other station must claim PTT from their own client.

## What each control does

| Control | Behavior |
|---|---|
| Enable (multiFLEX) | Toggles multiFLEX on or off for the radio. Shows "Enabled" (green) or "Disabled" (red) to reflect current state. |
| Stations table | Lists every connected multiFLEX client. Columns: LOCAL PTT, STATION, TX ANT, TX FREQ (MHz). Your station is highlighted in blue. A green check mark in LOCAL PTT indicates which station holds PTT authority. |
| Enable (PTT) | Claims local PTT for your station. Visible only when your station does not currently hold PTT and more than one station is connected. |
| Close | Closes the multiFLEX Dashboard. |

## Tips

- The Stations table updates automatically as clients connect, disconnect, or change state. You do not need to reopen the dialog to see current PTT status.
- Your station's row is highlighted in a distinct color so you can identify it quickly in a crowded table.
- If the Enable button and the PTT label are both absent, either only one station is connected or your station already holds PTT.

## Troubleshooting

- **Enable button and PTT label do not appear** — Either your station already holds PTT, or fewer than two stations are currently connected. Check the LOCAL PTT column to confirm which station holds it.
- **PTT controls are missing entirely** — multiFLEX may be disabled. Click the Enable button at the top of the dashboard to enable it, then check that the radio acknowledges the change (button turns green and shows "Enabled").
- **You cannot grant PTT to another station** — This is by design. Each station must claim PTT from its own client. Inform the other operator to open their multiFLEX Dashboard and click Enable under the PTT section.

## Related

- [Enable multiFLEX on the radio](enable-multiflex-on-the-radio.md)
- [Check which antenna and frequency each TX station is using](check-which-antenna-and-frequency-each-tx-station-is-using.md)
- [See all stations connected to this FLEX](../../getting-started/setup/see-all-stations-connected-to-this-flex.md)
