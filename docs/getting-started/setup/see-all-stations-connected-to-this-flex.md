# See all stations connected to this FLEX

The multiFLEX Dashboard lists every client currently sharing the radio, showing each station's name, transmit antenna, and transmit frequency. Use it to check who else is on the radio before transmitting.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The menu item is unavailable without an active radio connection.
- multiFLEX must be enabled on the radio. If it is not, the Stations table will be empty or show only your own station.

## Steps

1. Click `Settings > multiFLEX...`.
2. The **multiFLEX Dashboard** opens. The **Stations table** lists every connected client with four columns: **LOCAL PTT**, **STATION**, **TX ANT**, and **TX FREQ (MHz)**.
3. Review the table. Your own station is highlighted in blue. A checkmark in the **LOCAL PTT** column indicates which station currently holds PTT authority.
4. Click **Close** when finished.

## What each control does

| Control | What it does |
|---|---|
| **Enabled** / **Disabled** button | Toggles multiFLEX on or off for the radio. Displays **Enabled** (green) or **Disabled** (red) to reflect the current state. |
| **Stations table** | Lists each connected multiFLEX client. Columns: **LOCAL PTT** (checkmark if this station holds PTT), **STATION** (program and station name), **TX ANT** (transmit antenna), **TX FREQ (MHz)** (transmit frequency in MHz). |
| **Enable** (PTT) | Claims local PTT authority for your station. Visible only when another station holds PTT and you do not. |
| **Close** | Closes the dialog. |

## Tips

- Your own station's row is shown in blue. Other stations are shown in the default color.
- If only one station is connected, the PTT label and **Enable** button are hidden — PTT is not contested.
- TX antenna and frequency show `----` if the radio has not yet reported slice data for that station.

## Troubleshooting

- **The Stations table shows only one row or is empty** — multiFLEX may not be enabled on the radio. Click the **Disabled** button to enable it, then check whether other clients appear.
- **TX ANT and TX FREQ show `----` for a station** — Slice status data for that client has not yet arrived from the radio. Wait a moment and the table will refresh automatically when the data is received.

## Related

- [multiFLEX Dashboard overview](../../features/multi-flex/overview.md)
- [Enable multiFLEX on the radio](../../features/multi-flex/enable-multiflex-on-the-radio.md)
- [Grant or revoke local PTT](../../features/multi-flex/grant-or-revoke-local-ptt.md)
- [Check which antenna and frequency each TX station is using](../../features/multi-flex/check-which-antenna-and-frequency-each-tx-station-is-using.md)
