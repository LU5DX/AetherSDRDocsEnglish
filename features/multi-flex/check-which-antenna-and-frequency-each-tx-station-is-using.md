# Check which antenna and frequency each TX station is using

The multiFLEX Dashboard shows the transmit antenna and frequency for every station currently sharing the radio. Use this page to confirm what each connected client is doing before you transmit.

## Before you start

- AetherSDR must be connected to the radio. The multiFLEX Dashboard requires an active radio connection.
- multiFLEX must be enabled on the radio. If the dashboard shows no stations, see [Enable multiFLEX on the radio](enable-multiflex-on-the-radio.md).

## Steps

1. Click `Settings > multiFLEX...` to open the multiFLEX Dashboard.
2. Read the Stations table. Each row is one connected client.
3. Find the **TX ANT** column for the transmit antenna in use by each station.
4. Find the **TX FREQ (MHz)** column for the transmit frequency of each station, shown in MHz to three decimal places.
5. Click `Close` when finished.

## What each control does

| Control | Description |
|---|---|
| Stations table | Lists every multiFLEX client currently connected to the radio. Columns: **LOCAL PTT**, **STATION**, **TX ANT**, **TX FREQ (MHz)**. |
| LOCAL PTT | A check mark (✔) indicates the station currently holds local PTT authority. |
| STATION | The program name and station name of the client. Your own station is highlighted in blue. |
| TX ANT | The transmit antenna the station's TX slice is using. Displays `----` if no data is available. |
| TX FREQ (MHz) | The transmit frequency of the station's TX slice, in MHz. Displays `----` if no data is available. |

## Tips

- The table updates automatically whenever a client connects, disconnects, or changes its TX slice. You do not need to close and reopen the dialog to see current values.
- Your own station's row is highlighted in a distinct color, making it easy to identify yourself among multiple clients.

## Troubleshooting

- **TX ANT or TX FREQ (MHz) shows `----` for a station** — The radio has not yet reported TX slice data for that client. Wait a moment for the table to refresh, or ask the other operator to confirm they have a TX slice active.
- **No rows appear in the Stations table** — multiFLEX may not be enabled, or no other clients are connected. Verify the Enable button shows "Enabled" and check the network connection to the radio.

## Related

- [Enable multiFLEX on the radio](enable-multiflex-on-the-radio.md)
- [Grant or revoke local PTT](grant-or-revoke-local-ptt.md)
- [See all stations connected to this FLEX](../../getting-started/setup/see-all-stations-connected-to-this-flex.md)
