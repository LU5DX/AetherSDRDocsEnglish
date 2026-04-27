# multiFLEX Dashboard overview

The multiFLEX Dashboard shows every client station currently sharing your FLEX-8600 and lets you manage PTT authority across those stations. Use it when you are operating in a multi-operator or multi-software environment and need to see who is transmitting, on what antenna, and at what frequency.

## Before you start

- AetherSDR must be connected to the radio. The multiFLEX Dashboard is not available without an active radio connection.
- Your FLEX-8600 firmware must support the SmartSDR multiFLEX feature.

## How it works

Open the dashboard from `Settings > multiFLEX...`. The dialog displays the heading **multiFLEX Stations** and refreshes automatically whenever a client connects or disconnects, or when slice status changes on the radio.

At the top of the dialog, the **Enabled** / **Disabled** button reflects the current multiFLEX state on the radio. Clicking it toggles multiFLEX on or off and the button label updates immediately to reflect the new state.

The **Stations table** lists every connected multiFLEX client in four columns:

| Column | Content |
|---|---|
| LOCAL PTT | A check mark (✔) appears in green when that station currently holds local PTT authority. |
| STATION | Displays the client program name and station name in the form *program: station*. Your own station is highlighted in blue. |
| TX ANT | The transmit antenna assigned to that station's TX slice. Shows `----` if not available. |
| TX FREQ (MHz) | The transmit frequency of that station's TX slice in MHz to three decimal places. Shows `----` if not available. |

Below the table, the **Local PTT label** and the **Enable** (PTT) button appear only when more than one client is connected. Their content depends on the current PTT state:

- If your station does not hold PTT, the label reads *Enable Local PTT for this station (station name):* and the **Enable** button is shown. Clicking **Enable** requests local PTT authority for your station.
- If your station already holds PTT and you select another station's row, the label informs you that the selected station must claim PTT from their own client. The **Enable** button is hidden in this state.
- If only one client is connected, both the label and the **Enable** button are hidden.

Clicking **Close** dismisses the dialog.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Enabled** / **Disabled** | Button | Toggles multiFLEX on or off on the radio. Label shows current state: **Enabled** (green) or **Disabled** (red). |
| **Stations table** | List | Shows all connected multiFLEX clients. Columns: LOCAL PTT, STATION, TX ANT, TX FREQ (MHz). Selecting a row updates the PTT section below. |
| **Enable** (PTT) | Button | Requests local PTT authority for your station. Visible only when your station does not currently hold PTT and more than one client is connected. |
| Local PTT label | Indicator | Shows context-dependent text about PTT state for the selected station. Hidden when only one client is connected. |
| **Close** | Button | Closes the multiFLEX Dashboard dialog. |

## Tips

- Your own station's row in the Stations table is highlighted in blue, making it easy to identify your entry among multiple clients.
- TX antenna and frequency data for your own station is drawn directly from your active TX slice, so it reflects the current state even if the client info from the radio has not yet been updated.
- The table refreshes automatically; you do not need to close and reopen the dialog to see new clients.

## Related

- [Enable multiFLEX on the radio](enable-multiflex-on-the-radio.md)
- [Grant or revoke local PTT](grant-or-revoke-local-ptt.md)
- [Check which antenna and frequency each TX station is using](check-which-antenna-and-frequency-each-tx-station-is-using.md)
- [See all stations connected to this FLEX](../../getting-started/setup/see-all-stations-connected-to-this-flex.md)
