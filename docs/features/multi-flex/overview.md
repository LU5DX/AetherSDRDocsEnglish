# multiFLEX Dashboard overview

The multiFLEX Dashboard shows every client currently sharing your FLEX-8600 and lets you enable multiFLEX on the radio, monitor each station's transmit state, and manage local PTT authority. Open it whenever you need to see who else is connected or to claim PTT for your station.

## Before you start

- AetherSDR must be connected to the radio. The multiFLEX Dashboard requires an active radio connection.
- Your FLEX-8600 firmware must support multiFLEX (firmware 4.1.5, SmartSDR protocol v1.4.0.0).

## How it works

Open the dashboard from `Settings > multiFLEX...`. The dialog is titled **multiFLEX Dashboard** and displays the heading **multiFLEX Stations**.

When only one client is connected, the local PTT controls are hidden — PTT management only becomes relevant when two or more stations share the radio. The table and PTT section update automatically whenever another client connects, disconnects, or changes its transmit state.

**multiFLEX enable state** is toggled with the button at the top of the dialog. The button label reflects the current state: it reads **Enabled** (green) when multiFLEX is active on the radio, and **Disabled** (red) when it is not. Clicking the button toggles the state immediately.

**Local PTT** is managed per-station. Only one station can hold PTT authority at a time. If your station does not currently hold PTT, the dashboard shows the label "Enable Local PTT for this station (*station name*):" alongside the **Enable** button. If your station already holds PTT and you select another station's row in the table, the dashboard shows a message indicating that the other station must claim PTT from their own client — you cannot grant it to them from here.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Enabled** / **Disabled** | Push button | Enables or disables multiFLEX on the radio. Label and color reflect the current state. |
| Stations table | List | Lists every connected multiFLEX client. Columns: LOCAL PTT, STATION, TX ANT, TX FREQ (MHz). Your own station is highlighted. A checkmark (✔) in LOCAL PTT marks the station currently holding PTT authority. |
| Local PTT label | Indicator | Shows context-sensitive text: either an invitation to claim PTT for your station, or a message that another selected station must claim PTT themselves. Hidden when only one client is connected. |
| **Enable** (PTT) | Push button | Requests local PTT authority for this station. Visible only when your station does not currently hold PTT and at least one other client is connected. |
| **Close** | Push button | Closes the dialog. |

### Stations table columns

| Column | Content |
|---|---|
| LOCAL PTT | Checkmark if this station currently holds PTT authority. |
| STATION | Program name and station name, formatted as *program: station*. Your own station is shown in blue. |
| TX ANT | The transmit antenna assigned to this station's TX slice. Shows `----` if not available. |
| TX FREQ (MHz) | The transmit frequency in MHz to three decimal places. Shows `----` if not available. |

## Tips

- Selecting a row in the Stations table while your station holds PTT will display a message about that station needing to claim PTT from their own client. No action on your part is required or possible from this dialog in that situation.
- The table updates automatically when other clients connect or disconnect. You do not need to reopen the dialog.

## Related

- [Enable multiFLEX on the radio](enable-multiflex-on-the-radio.md)
- [Grant or revoke local PTT](grant-or-revoke-local-ptt.md)
- [Check which antenna and frequency each TX station is using](check-which-antenna-and-frequency-each-tx-station-is-using.md)
- [See all stations connected to this FLEX](../../getting-started/setup/see-all-stations-connected-to-this-flex.md)
