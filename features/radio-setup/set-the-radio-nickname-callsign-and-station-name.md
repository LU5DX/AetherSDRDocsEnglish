# Set the Radio Nickname, Callsign and Station Name

Set a human-readable nickname, your station callsign, and a station name on the connected FLEX-8600. These values identify the radio and this client to other multiFLEX stations on the network.

## Before you start

- AetherSDR must be connected to the radio. The Radio (tab) fields are not editable while disconnected.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Radio** tab.
3. In the **Radio Identification** group, locate the **Nickname** field. Type the nickname you want to assign to the radio.
4. Press Tab or click away from the field. AetherSDR sends the new nickname to the radio immediately.
5. Locate the **Callsign** field. Type your callsign.
6. Press Tab or click away from the field. AetherSDR sends the callsign to the radio immediately.
7. Locate the **Station Name** field. Type the name that identifies this client to other multiFLEX stations.
8. Press Tab or click away from the field. AetherSDR saves the value locally and sends it to the radio immediately.

## What each control does

| Control | Description | Default | Setting key |
|---|---|---|---|
| **Nickname** | User-friendly label for the radio. Stored on the radio. | Radio's reported name | — |
| **Callsign** | Station callsign. Stored on the radio. | Value reported by radio | — |
| **Station Name** | Identifies this client to other multiFLEX stations. Stored locally and sent to the radio on change. | OS hostname | `StationName` |

## Tips

- Changes take effect as soon as you leave each field — there is no separate Save button.
- **Station Name** defaults to the operating system hostname if the field has never been set. To restore that default, clear the field and press Tab; it will revert to the hostname on the next dialog open.
- **Nickname** and **Callsign** are stored on the radio itself. **Station Name** is stored in AetherSDR's local settings under the key `StationName` and is also sent to the radio as the client station identifier.

## Troubleshooting

- **Fields appear empty after opening the dialog** — The radio connection may not have finished sending its initial status. Close and reopen the dialog after the radio status bar shows as connected.
- **Changes do not appear on other multiFLEX clients** — Confirm the radio is online and the SmartSDR protocol session is active. Only values sent while connected are received by other clients.

## Related

- [Check radio serial, hardware version, region and options](check-radio-serial-hardware-version-region-and-options.md)
- [Radio Setup overview](overview.md)
