# Set the radio nickname, callsign and station name

Set a human-readable nickname, your callsign, and a station name on the connected FLEX-8600. These values identify the radio and this client to other multiFLEX stations on the network.

## Before you start

- AetherSDR must be connected to the radio. The Radio (tab) controls are not available without an active connection.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Radio** tab.
3. In the **Radio Identification** group, locate the **Nickname** field. Type the nickname you want to assign to the radio.
4. Press Tab or click away from the field to confirm. AetherSDR sends the new name to the radio immediately.
5. In the **Callsign** field, type your station callsign.
6. Press Tab or click away from the field to confirm.
7. In the **Station Name** field, type the name that identifies this client to other multiFLEX stations.
8. Press Tab or click away from the field to confirm.
9. Click **Close** to dismiss the dialog.

## What each control does

| Control | Description | Default | Setting key |
|---|---|---|---|
| **Nickname** | User-friendly label for the radio. Sent to the radio as the radio name. | Radio's reported name | — |
| **Callsign** | Your station callsign, stored on the radio. | _(blank)_ | — |
| **Station Name** | Identifies this AetherSDR client to other multiFLEX stations. | OS hostname | `StationName` |

## Tips

- If **Nickname** is left blank, AetherSDR pre-fills the field with the radio's reported name from the network.
- **Station Name** defaults to the OS hostname when no value has been saved. To restore the default, clear the field and press Tab — then re-enter the hostname manually if needed.
- Changes to **Nickname** and **Callsign** are pushed to the radio the moment you leave each field. No separate Save or Apply step is required.
- **Station Name** is saved locally in AetherSDR's settings and also sent to the radio as the client station identifier for multiFLEX.

## Related

- [Check radio serial, hardware version, region and options](check-radio-serial-hardware-version-region-and-options.md)
- [Radio Setup overview](overview.md)
