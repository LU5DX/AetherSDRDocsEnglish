# Check which antenna and frequency each TX station is using

The multiFLEX Dashboard shows a live table of every station sharing the FLEX radio, including the TX antenna and transmit frequency each station is currently using. Use this when you need to confirm what other operators on the same radio are doing before transmitting.

## Before you start

- AetherSDR must be connected to the radio. The multiFLEX Dashboard requires an active radio connection.
- multiFLEX must be enabled on the radio. If the dashboard shows no stations, see [Enable multiFLEX on the radio](enable-multiflex-on-the-radio.md).

## Steps

1. Click `Settings > multiFLEX...` to open the multiFLEX Dashboard.
2. Read the Stations table. Each row is one connected client.
3. Find the **TX ANT** column for the antenna each station is using, and the **TX FREQ (MHz)** column for their current transmit frequency.
4. Click `Close` when finished.

## What each control does

| Control | Description |
|---|---|
| Stations table | Lists every connected multiFLEX client. Columns: **LOCAL PTT**, **STATION**, **TX ANT**, **TX FREQ (MHz)**. |
| **LOCAL PTT** column | Shows a checkmark for the station currently holding PTT authority. |
| **STATION** column | Shows the program name and station name for each client. Your own station is highlighted in blue. |
| **TX ANT** column | Shows the transmit antenna selected by each station. Displays `----` if no antenna data is available. |
| **TX FREQ (MHz)** column | Shows each station's transmit frequency in MHz, to three decimal places. Displays `----` if no frequency data is available. |

## Tips

- The table updates automatically as stations change frequency or antenna. You do not need to reopen the dialog to see current values.
- Your own station's row is shown in a distinct color, making it easy to locate your entry among multiple clients.

## Troubleshooting

- **TX ANT or TX FREQ shows `----` for a station** — The radio has not yet reported slice status for that client. Wait a moment and the table will refresh automatically when the data arrives.
- **No rows appear in the Stations table** — multiFLEX may not be enabled. Click `Enable` at the top of the dialog to enable it, or see [Enable multiFLEX on the radio](enable-multiflex-on-the-radio.md).

## Related

- [Enable multiFLEX on the radio](enable-multiflex-on-the-radio.md)
- [Grant or revoke local PTT](grant-or-revoke-local-ptt.md)
- [See all stations connected to this FLEX](../../getting-started/setup/see-all-stations-connected-to-this-flex.md)
