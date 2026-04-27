# Enable multiFLEX on the radio

Use the multiFLEX Dashboard to turn multiFLEX on or off on the connected FLEX-8600. Enabling multiFLEX allows multiple client stations to share the radio simultaneously.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. multiFLEX Dashboard requires an active radio connection.

## Steps

1. Click `Settings > multiFLEX...` to open the multiFLEX Dashboard.
2. Click the toggle button in the center of the dialog. When multiFLEX is disabled, the button reads **Disabled**. When enabled, it reads **Enabled**.
3. Click **Close** to dismiss the dialog.

## What each control does

| Control | Behavior |
|---|---|
| **Enabled** / **Disabled** button | Toggles multiFLEX on or off on the radio. The button label and color reflect the current state: **Enabled** (green) or **Disabled** (red). |
| Stations table | Lists every multiFLEX client currently connected to the radio. Columns: LOCAL PTT, STATION, TX ANT, TX FREQ (MHz). |
| **Enable** (PTT) | Toggles local PTT authority for this station. Only shown when more than one client is connected and this station does not currently hold PTT. |
| **Close** | Closes the multiFLEX Dashboard dialog. |

## Tips

- Your station's entry in the Stations table is highlighted in blue. Other connected stations appear in the default color.
- When only one client is connected, the LOCAL PTT controls are hidden automatically.

## Related

- [multiFLEX Dashboard overview](overview.md)
- [Grant or revoke local PTT](grant-or-revoke-local-ptt.md)
- [Check which antenna and frequency each TX station is using](check-which-antenna-and-frequency-each-tx-station-is-using.md)
- [See all stations connected to this FLEX](../../getting-started/setup/see-all-stations-connected-to-this-flex.md)
