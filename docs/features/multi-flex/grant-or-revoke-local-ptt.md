# Grant or revoke local PTT

When multiple stations share a FLEX-8600 via multiFLEX, only one station holds local PTT authority at a time. This page explains how to claim local PTT for your station and how to read which station currently holds it.

## Before you start

- AetherSDR must be connected to the radio. The multiFLEX Dashboard requires an active radio connection.
- multiFLEX must be enabled on the radio. If the Enable button in the dashboard shows "Disabled", see [Enable multiFLEX on the radio](enable-multiflex-on-the-radio.md) first.
- At least one other multiFLEX client must be connected. The Enable (PTT) button only appears when another station is present and your station does not currently hold PTT.

## Steps

1. Open `Settings > multiFLEX...`.
2. In the Stations table, locate the LOCAL PTT column. A checkmark (✔) in that column identifies the station currently holding PTT authority.
3. If another station holds PTT and you need to claim it for your station, click `Enable` in the PTT row below the table. The label above that button names the other station for confirmation.
4. Check the LOCAL PTT column again. The checkmark should now appear on your station's row.
5. Click `Close` when finished.

## What each control does

| Control | Description |
|---|---|
| Enable (multiFLEX) | Toggles multiFLEX on or off for the radio. The button label reflects current state: "Enabled" or "Disabled". |
| Stations table | Lists every connected multiFLEX client. Columns: LOCAL PTT, STATION, TX ANT, TX FREQ (MHz). Your station's name is highlighted. |
| Local PTT label | Text above the Enable (PTT) button. Shows the name of the other station currently holding PTT. Only visible when another station has PTT and your station does not. |
| Enable (PTT) | Requests local PTT authority for your station. Only visible when another client holds PTT. |
| Close | Closes the multiFLEX Dashboard. |

## Tips

- The LOCAL PTT column uses a checkmark to show which station holds PTT. If you are the only connected station, PTT is automatically yours and the Enable (PTT) button does not appear.
- The STATION column shows entries in the format `program: station`. Your station's entry is highlighted in a distinct color.
- TX ANT and TX FREQ (MHz) update automatically as station state changes. If no data is available for a column, it shows `----`.

## Troubleshooting

- **The Enable (PTT) button is not visible** — Either your station already holds PTT, or there is only one station connected. The button only appears when another client holds PTT authority. Check the LOCAL PTT column to confirm.
- **The Stations table is empty** — The radio may not have reported client status yet. Close and reopen `Settings > multiFLEX...` to force a refresh, or verify the radio connection is active.
- **TX ANT and TX FREQ show `----` for your station** — Your TX slice information may not have been received yet. Verify you have an active slice with TX enabled.

## Related

- [multiFLEX Dashboard overview](overview.md)
- [Enable multiFLEX on the radio](enable-multiflex-on-the-radio.md)
- [Check which antenna and frequency each TX station is using](check-which-antenna-and-frequency-each-tx-station-is-using.md)
- [See all stations connected to this FLEX](../../getting-started/setup/see-all-stations-connected-to-this-flex.md)
