# Grant or revoke local PTT

Use the multiFLEX Dashboard to claim local PTT authority for your station or to see which station currently holds it. This is necessary when multiple clients share the same FLEX-8600 and only one station may transmit at a time.

## Before you start

- AetherSDR must be connected to the radio. The multiFLEX Dashboard requires an active radio connection.
- multiFLEX must be enabled on the radio. If the dashboard shows "Disabled", see [Enable multiFLEX on the radio](enable-multiflex-on-the-radio.md) first.
- At least two stations must be connected before the PTT controls appear. With only one station present, the PTT button is hidden.

## Steps

1. Click `Settings > multiFLEX...` to open the multiFLEX Dashboard.
2. Review the Stations table. The LOCAL PTT column shows a checkmark next to the station that currently holds PTT.
3. If your station does not hold PTT, the label beneath the table reads `Enable Local PTT for this station (<your station name>):` and the Enable button is visible.
4. Click `Enable` to claim local PTT for your station.

If another station already holds PTT, the Enable button is hidden. The label instead identifies the other station and notes that they must claim or release PTT from their own client. You cannot force PTT away from another station through this dialog.

5. Click `Close` when done.

## What each control does

| Control | Behavior |
|---|---|
| Enable (top) | Enables or disables multiFLEX on the radio. Displays "Enabled" (green) or "Disabled" (red) to reflect current state. |
| Stations table | Lists every connected multiFLEX client. Columns: LOCAL PTT, STATION, TX ANT, TX FREQ (MHz). Your own station appears highlighted. A checkmark in LOCAL PTT indicates which station holds PTT. |
| Local PTT label | Describes the current PTT state relative to your station, or names the other station that must act. Hidden when only one station is connected. |
| Enable (PTT) | Claims local PTT authority for your station. Visible only when your station does not currently hold PTT and at least two stations are connected. |
| Close | Closes the dialog. |

## Tips

- Your station is highlighted in the STATION column, making it easy to find in a crowded table.
- The STATION column displays entries as `program: station` when the program name and station name differ.
- TX ANT and TX FREQ (MHz) reflect the transmitting slice for each station. If that data is not yet available, the columns show `----`.

## Troubleshooting

- **The Enable (PTT) button is not visible** — Either your station already holds PTT, only one station is connected (single-station mode grants PTT automatically), or another station holds PTT and must release it from their own client.
- **PTT controls are missing entirely** — Only one station is currently connected. The controls appear only when two or more stations are present in the Stations table.
- **The Stations table is empty** — The radio connection may have dropped, or multiFLEX is not enabled. Verify the Enable button at the top of the dialog shows "Enabled".

## Related

- [Enable multiFLEX on the radio](enable-multiflex-on-the-radio.md)
- [Check which antenna and frequency each TX station is using](check-which-antenna-and-frequency-each-tx-station-is-using.md)
- [See all stations connected to this FLEX](../../getting-started/setup/see-all-stations-connected-to-this-flex.md)
