# See all stations connected to this FLEX

The multiFLEX Dashboard shows every SmartSDR client currently sharing your FLEX-8600 and their transmit details. Open it to confirm which stations are on the radio and who holds local PTT.

## Before you start

- AetherSDR must be connected to the radio. The multiFLEX Dashboard requires an active radio connection.
- multiFLEX must be enabled on the radio. If it is not, the Stations table will be empty or show only your own station.

## Steps

1. Click `Settings > multiFLEX...`.
2. The **multiFLEX Dashboard** opens. The Stations table lists every connected client with four columns: **LOCAL PTT**, **STATION**, **TX ANT**, and **TX FREQ (MHz)**.
3. Review the rows. Your own station is highlighted in blue in the **STATION** column. A checkmark in the **LOCAL PTT** column indicates which station currently holds PTT authority.
4. Click **Close** when finished.

## What each control does

| Control | What it does |
|---|---|
| **Enabled** / **Disabled** button | Shows whether multiFLEX is currently active on the radio. Click to toggle it on or off. |
| Stations table | Lists each connected multiFLEX client. Columns: **LOCAL PTT**, **STATION**, **TX ANT**, **TX FREQ (MHz)**. |
| **Enable** (PTT) | Claims local PTT authority for your station. Visible only when another station holds PTT or when more than one station is connected and you do not currently hold PTT. |
| **Close** | Closes the dialog. |
| Local PTT label | Shows which station holds PTT, or prompts you to enable PTT for your station. |

## Tips

- The **STATION** column shows the remote program name and station name in the format `program: station`. Your own entry appears in blue.
- If only one station is connected, the **Enable** (PTT) button and Local PTT label are hidden — PTT is implicitly yours.
- If another station holds PTT and you select their row, the label reads that the other station must claim PTT from their own client. You cannot grant PTT to another station from this dialog.
- TX antenna and frequency show `----` if the radio has not yet reported slice data for that client.

## Troubleshooting

- **Stations table is empty or shows only your station** — multiFLEX may be disabled. Click the **Disabled** button to enable it, then check whether other clients appear.
- **LOCAL PTT column shows no checkmark for any row** — No station currently holds PTT. Click **Enable** to claim it for your station.
- **TX ANT and TX FREQ show `----` for a station** — Slice status has not yet arrived for that client. Wait a moment, then reopen the dialog; the table refreshes automatically when client information changes.

## Related

- [multiFLEX Dashboard overview](../../features/multi-flex/overview.md)
- [Enable multiFLEX on the radio](../../features/multi-flex/enable-multiflex-on-the-radio.md)
- [Grant or revoke local PTT](../../features/multi-flex/grant-or-revoke-local-ptt.md)
- [Check which antenna and frequency each TX station is using](../../features/multi-flex/check-which-antenna-and-frequency-each-tx-station-is-using.md)
