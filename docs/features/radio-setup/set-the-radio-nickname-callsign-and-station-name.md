# Set the Radio Nickname, Callsign and Station Name

Use this page to assign a human-readable nickname, a callsign, and a station name to your FLEX-8600. These values identify the radio and this client to other multiFLEX stations on the network.

## Before you start

- AetherSDR must be connected to the radio. The Radio (tab) in Radio Setup requires an active radio connection.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Radio** tab if it is not already selected.
3. In the **Radio Identification** group, locate the **Nickname** field and type the name you want to give the radio.
4. Press Tab or click away from the field. AetherSDR sends the new nickname to the radio immediately.
5. Locate the **Callsign** field and type your callsign.
6. Press Tab or click away from the field. AetherSDR sends the callsign to the radio immediately.
7. Locate the **Station Name** field and type the name for this client station. If you leave it blank, AetherSDR uses the OS hostname by default.
8. Press Tab or click away from the field. AetherSDR saves the value locally and sends it to the radio.
9. Click **Close** when finished.

## What each control does

| Control | Description | Default | Persisted key |
|---|---|---|---|
| **Nickname** | User-friendly label for the radio, sent to the radio as `radio name`. | Radio's existing name | — (stored on radio) |
| **Callsign** | Station callsign, sent to the radio as `radio callsign`. | Radio's existing callsign | — (stored on radio) |
| **Station Name** | Identifies this AetherSDR client to other multiFLEX stations. Sent as `client station`. | OS hostname | `StationName` |

## Tips

- **Nickname** and **Callsign** are stored on the radio itself, so they persist across different client computers connecting to the same radio.
- **Station Name** is stored locally in AetherSDR's settings (`StationName`) and also announced to the radio each time you edit it. Other multiFLEX clients see this name to distinguish which station is which.
- Changes take effect as soon as you leave each field — there is no separate Save button for these three fields.

## Related

- [Check radio serial, hardware version, region and options](check-radio-serial-hardware-version-region-and-options.md)
- [Radio Setup overview](overview.md)
