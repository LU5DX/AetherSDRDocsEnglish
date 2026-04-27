# Check which antenna and frequency each TX station is using

The multiFLEX Dashboard shows the TX antenna and TX frequency for every station currently sharing the FLEX-8600. Use this when you need to confirm that other operators on the radio are not conflicting with your intended operating frequency or antenna.

## Before you start

- AetherSDR must be connected to the radio.
- multiFLEX must be enabled on the radio. If the Stations table is empty or the feature is not active, see [Enable multiFLEX on the radio](enable-multiflex-on-the-radio.md).

## Steps

1. Click `Settings > multiFLEX...` to open the multiFLEX Dashboard.
2. Look at the Stations table. Each row is one connected station.
3. Read the **TX ANT** column for the antenna that station is transmitting on.
4. Read the **TX FREQ (MHz)** column for that station's transmit frequency in MHz, shown to three decimal places.
5. Click Close when finished.

## What each control does

| Control | Description |
|---|---|
| Stations table | Lists every connected multiFLEX client. Columns: LOCAL PTT, STATION, TX ANT, TX FREQ (MHz). |
| LOCAL PTT column | Shows a check mark for the station that currently holds PTT authority. |
| STATION column | Shows the program name and station name for each client. Your own station is highlighted in blue. |
| TX ANT column | Shows the antenna assigned to that station's TX slice. Displays `----` if no data is available yet. |
| TX FREQ (MHz) column | Shows the transmit frequency in MHz to three decimal places. Displays `----` if no data is available yet. |
| Close | Closes the dialog. |

## Tips

- The table refreshes automatically when any client's status changes. You do not need to reopen the dialog to see updated values.
- Your own station's row is distinguished by blue text in the STATION column.
- TX ANT and TX FREQ values come from the radio's slice status. If a station has just connected, those columns may briefly show `----` until the radio reports slice data.

## Related

- [Enable multiFLEX on the radio](enable-multiflex-on-the-radio.md)
- [Grant or revoke local PTT](grant-or-revoke-local-ptt.md)
- [See all stations connected to this FLEX](../../getting-started/setup/see-all-stations-connected-to-this-flex.md)
