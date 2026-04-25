# multiFLEX Dashboard overview

The multiFLEX Dashboard shows every SmartSDR client currently sharing your FLEX-8600 and lets you manage PTT authority between stations. Use it when more than one operator or application is connected to the same radio and you need to see who is transmitting, on what antenna, and at what frequency.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The dashboard requires an active radio connection.
- multiFLEX must be supported by your radio firmware (4.1.5 or later).

## How it works

Open the dashboard with `Settings > multiFLEX...`. The dialog title is **multiFLEX Dashboard** and its central element is the **Stations table**, which refreshes automatically whenever clients connect, disconnect, or change state.

Each row in the **Stations table** represents one connected SmartSDR client. The table has four columns:

| Column | What it shows |
|---|---|
| LOCAL PTT | A checkmark (✔) if that station currently holds local PTT authority. |
| STATION | The program name and station name of the client. Your own station is highlighted in blue. |
| TX ANT | The transmit antenna that client is using. Shows `----` if not available. |
| TX FREQ (MHz) | The transmit frequency in MHz to three decimal places. Shows `----` if not available. |

The **Local PTT label** above the PTT button shows context-sensitive status text. If your station does not hold PTT, it reads something like `Enable Local PTT for this station (<your station name>):`. If another station holds PTT, it identifies that station and notes they must claim PTT from their own client.

When only one client is connected, the PTT label and PTT button are hidden — they are only relevant in a multi-station scenario.

## What each control does

| Control | Behavior |
|---|---|
| Enable | Toggles multiFLEX on or off for the radio. When multiFLEX is active, the button label changes to **Enabled** (green); when inactive it reads **Disabled** (red). Clicking it toggles the current state. |
| Stations table | Lists all connected multiFLEX clients with their LOCAL PTT status, station name, TX antenna, and TX frequency. Updated automatically on any client change. |
| Enable (PTT) | Appears when your station does not currently hold local PTT and more than one client is connected. Click it to claim local PTT authority for your station. The button label is **Enable**. |
| Close | Closes the dialog. |

## Tips

- Your own station's row is highlighted in a distinct color in the STATION column, making it easy to identify yourself among multiple clients.
- If you hold PTT and need another station to transmit, that operator must claim PTT from their own client — you cannot grant it to them from this dialog.
- The TX ANT and TX FREQ columns pull data from the radio's slice status. If a client connected before its slice status was received, these fields may briefly show `----` until the dashboard refreshes.

## Related

- [Enable multiFLEX on the radio](enable-multiflex-on-the-radio.md)
- [Grant or revoke local PTT](grant-or-revoke-local-ptt.md)
- [Check which antenna and frequency each TX station is using](check-which-antenna-and-frequency-each-tx-station-is-using.md)
- [See all stations connected to this FLEX](../../getting-started/setup/see-all-stations-connected-to-this-flex.md)
