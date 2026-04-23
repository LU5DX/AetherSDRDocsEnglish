# multiFLEX Dashboard overview

The multiFLEX Dashboard shows every SmartSDR client currently sharing your Flex radio and lets you manage PTT authority between them. Use it when more than one operator or application is connected to the same radio and you need to see who holds transmit control.

## Before you start

- AetherSDR must be connected to the radio. The dashboard requires an active radio connection.
- multiFLEX must be supported by your radio firmware (Flex radio, firmware 4.1.5).

## How it works

Open the dashboard from `Settings > multiFLEX...`. The dialog title reads "multiFLEX Dashboard".

When the dialog opens, AetherSDR queries the radio for its current list of connected clients and populates the Stations table automatically. The table refreshes whenever a client connects, disconnects, or changes its PTT state — you do not need to reload manually.

Each row in the Stations table represents one connected SmartSDR client. Your own station is highlighted in blue. A checkmark (✔) in the LOCAL PTT column identifies the station that currently holds PTT authority.

When another client holds PTT and more than one client is connected, the "Enable Local PTT for this station" label and the Enable (PTT) button appear below the table. When you are the only connected client, PTT authority is yours implicitly and those controls are hidden.

The Enable / Disabled toggle at the top of the dialog reflects the current multiFLEX state on the radio itself. Clicking it toggles multiFLEX on or off at the radio level and immediately refreshes the dialog.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| Enable / Disabled | Button | Enables or disables multiFLEX on the radio. The label shows "Enabled" (green) when active and "Disabled" (red) when inactive. Click to toggle. |
| Stations table | Table | Lists each connected multiFLEX client. Columns: LOCAL PTT, STATION, TX ANT, TX FREQ (MHz). Your station appears in blue. A ✔ in LOCAL PTT marks the station with transmit authority. |
| Local PTT label | Label | Displays "Enable Local PTT for this station (station name):" when another client holds PTT. Hidden when you have PTT or are the only client. |
| Enable (PTT) | Button | Toggles local PTT authority for this station. Visible only when another client holds PTT and more than one client is connected. |
| Close | Button | Closes the dialog. |

### Stations table columns

| Column | Content |
|---|---|
| LOCAL PTT | Checkmark (✔) if this station currently holds local PTT. Empty otherwise. |
| STATION | Client program name and station name, formatted as "program: station". Your station appears highlighted in blue. |
| TX ANT | The transmit antenna assigned to this station's TX slice. Shows `----` if not available. |
| TX FREQ (MHz) | The transmit frequency of this station's TX slice in MHz, to three decimal places. Shows `----` if not available. |

## Tips

- The Stations table updates automatically as clients join or leave. You do not need to close and reopen the dialog to see changes.
- TX ANT and TX FREQ reflect the TX slice assigned to each client. If a client has no active TX slice, both columns show `----`.
- The Enable (PTT) button only appears when another station holds PTT. If you are the sole connected client, PTT is granted implicitly and the button is not shown.

## Related

- [Enable multiFLEX on the radio](enable-multiflex-on-the-radio.md)
- [Grant or revoke local PTT](grant-or-revoke-local-ptt.md)
- [Check which antenna and frequency each TX station is using](check-which-antenna-and-frequency-each-tx-station-is-using.md)
- [See all stations connected to this FLEX](../../getting-started/setup/see-all-stations-connected-to-this-flex.md)
