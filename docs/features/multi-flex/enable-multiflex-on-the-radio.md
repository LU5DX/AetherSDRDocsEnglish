# Enable multiFLEX on the radio

multiFLEX lets multiple stations share a single FLEX-8600 simultaneously. This page explains how to turn multiFLEX on or off from within AetherSDR.

## Before you start

- AetherSDR must be connected to the radio. The multiFLEX Dashboard is unavailable without an active radio connection.

## Steps

1. Click `Settings > multiFLEX...` to open the multiFLEX Dashboard.
2. Click the toggle button at the top of the dialog. When multiFLEX is off, the button reads "Disabled". When it is on, the button reads "Enabled".
3. Click Close to dismiss the dialog.

## What each control does

| Control | Behavior |
|---|---|
| Enable / Disable toggle | Enables or disables multiFLEX on the radio. The button label reflects the current state: "Enabled" (green) or "Disabled" (red). Clicking it toggles to the opposite state. |
| Stations table | Lists every multiFLEX client currently connected to the radio. Columns: LOCAL PTT, STATION, TX ANT, TX FREQ (MHz). |
| Enable (PTT) | Toggles local PTT authority for this station. Visible only when more than one station is connected and this station does not currently hold PTT. |
| Close | Closes the multiFLEX Dashboard dialog. |

## Tips

- The Stations table is empty until at least one client connects. If you are the only client, the LOCAL PTT and Enable (PTT) controls are hidden.
- Your own station entry appears highlighted in the Stations table, making it easy to identify among other connected clients.

## Troubleshooting

- **"multiFLEX..." is grayed out in the Settings menu** — AetherSDR is not connected to the radio. Establish a radio connection first, then return to `Settings > multiFLEX...`.
- **The button shows "Enabled" but other stations cannot connect** — multiFLEX licensing and slot availability are enforced by the radio firmware, not by AetherSDR. Verify that the FLEX-8600 firmware is 4.1.5 and that available multiFLEX slots have not been exhausted.

## Related

- [multiFLEX Dashboard overview](overview.md)
- [Grant or revoke local PTT](grant-or-revoke-local-ptt.md)
- [Check which antenna and frequency each TX station is using](check-which-antenna-and-frequency-each-tx-station-is-using.md)
- [See all stations connected to this FLEX](../../getting-started/setup/see-all-stations-connected-to-this-flex.md)
