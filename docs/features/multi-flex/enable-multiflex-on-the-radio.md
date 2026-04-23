# Enable multiFLEX on the radio

multiFLEX lets multiple stations share a single Flex radio simultaneously. Use this page to turn multiFLEX on or off from AetherSDR.

## Before you start

- AetherSDR must be connected to the radio. The multiFLEX Dashboard is not available without an active radio connection.
- Your Flex radio must support multiFLEX. Confirm your radio's license includes the multiFLEX feature before proceeding.

## Steps

1. Click `Settings > multiFLEX...` to open the multiFLEX Dashboard.
2. Click the button labeled `Disabled` (shown in red when multiFLEX is currently off) to enable multiFLEX on the radio.
3. The button changes to `Enabled` (shown in green) to confirm multiFLEX is now active on the radio.
4. To disable multiFLEX, click `Enabled`. The button returns to `Disabled`.
5. Click `Close` when finished.

## What each control does

| Control | Behavior |
|---|---|
| `Disabled` / `Enabled` | Toggles multiFLEX on or off on the radio. Label and color reflect current state: green (`Enabled`) or red (`Disabled`). |
| Stations table | Lists every connected multiFLEX client. Columns: LOCAL PTT, STATION, TX ANT, TX FREQ (MHz). |
| `Enable` (PTT) | Toggles local PTT authority for this station. Visible only when another client is connected and holds PTT. |
| `Close` | Closes the multiFLEX Dashboard. |

## Tips

- The stations table updates automatically as clients connect or disconnect. You do not need to reopen the dialog to see changes.
- Your own station entry appears highlighted in the table, making it easy to identify among multiple connected clients.

## Related

- [multiFLEX Dashboard overview](overview.md)
- [Grant or revoke local PTT](grant-or-revoke-local-ptt.md)
- [Check which antenna and frequency each TX station is using](check-which-antenna-and-frequency-each-tx-station-is-using.md)
- [See all stations connected to this FLEX](../../getting-started/setup/see-all-stations-connected-to-this-flex.md)
