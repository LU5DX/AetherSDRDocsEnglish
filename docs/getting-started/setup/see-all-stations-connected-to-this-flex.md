# See all stations connected to this FLEX

The multiFLEX Dashboard shows every SmartSDR client currently sharing your FLEX-8600. Use it to check which stations are online, which antenna and frequency each is using, who holds local PTT, and disconnect individual clients.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The multiFLEX Dashboard is not available when no radio is connected.
- multiFLEX must be enabled on the radio. If it is not yet enabled, see [Enable multiFLEX on the radio](../../features/multi-flex/enable-multiflex-on-the-radio.md).

## Steps

1. Click `Settings > multiFLEX...`.
2. The **multiFLEX Dashboard** dialog opens, showing the Stations table populated with all currently connected clients.
3. Review the table. Each row is one connected station.
4. Click `Close` when finished.

## What each control does

| Control | What it does |
|---|---|
| `Enable` button | Enables or disables multiFLEX on the radio. Click to toggle multiFLEX on or off. |
| Stations table | Lists every connected multiFLEX client. Columns: **LOCAL PTT**, **STATION**, **TX ANT**, **TX FREQ (MHz)**, and a disconnect column. Your own station is highlighted in blue. A checkmark (✔) in the **LOCAL PTT** column identifies which station currently holds PTT authority. |
| `Enable` (PTT) | Appears when more than one station is connected and your station does not currently hold PTT. Click to claim local PTT authority for your station. |
| Local PTT label | Text indicating which station currently holds PTT. |
| `Close` | Closes the dialog. |
| Disconnect button (in table) | A red button in the fifth column of each station row. Click to disconnect that client station from the radio. The button is disabled for your own station. |

## Tips

- The STATION column displays the program name and station name in the format `program: station`. If the station name matches the program name, only the program name is shown. If only a station name is available, that name is shown alone. If no name data is reported, the display shows the client handle (e.g., `client 0x00000000`).
- TX ANT and TX FREQ (MHz) show `----` if the radio has not yet reported that data for a given station.
- The table updates automatically as stations connect or disconnect. You do not need to reopen the dialog.
- If only one station is connected, the `Enable` (PTT) button and Local PTT label are hidden — they are not needed when you are the only client.
- The disconnect button is grayed out and disabled for your own station. You cannot disconnect yourself.
- The dialog remembers its position and size between sessions.

## Troubleshooting

- **`Settings > multiFLEX...` is grayed out or missing** — AetherSDR is not connected to a radio. Connect to a radio first, then reopen the menu.
- **Stations table is empty** — multiFLEX may be disabled. Click `Enable` to enable it, then check whether other stations appear.
- **TX ANT and TX FREQ show `----` for all stations** — The radio has not yet sent slice status for those clients. Wait a moment and the table will refresh automatically.

## Related

- [multiFLEX Dashboard overview](../../features/multi-flex/overview.md)
- [Enable multiFLEX on the radio](../../features/multi-flex/enable-multiflex-on-the-radio.md)
- [Grant or revoke local PTT](../../features/multi-flex/grant-or-revoke-local-ptt.md)
- [Check which antenna and frequency each TX station is using](../../features/multi-flex/check-which-antenna-and-frequency-each-tx-station-is-using.md)
- Disconnect a client station