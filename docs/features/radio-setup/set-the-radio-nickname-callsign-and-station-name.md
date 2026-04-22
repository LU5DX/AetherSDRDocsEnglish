# Set the Radio Nickname, Callsign and Station Name

Set a human-readable name, your callsign, and a station identifier on your FLEX-8600. These values are stored on the radio and identify your client to other multiFLEX stations.

## Before you start

- AetherSDR must be connected to the radio. The Radio tab in Radio Setup is not available without an active connection.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Radio** tab.
3. In the **Radio Identification** group, locate the **Nickname** field. Type the name you want to assign to the radio, then press Tab or Enter to commit. AetherSDR sends the new name to the radio immediately.
4. Locate the **Callsign** field. Type your callsign, then press Tab or Enter to commit.
5. Locate the **Station Name** field. Type the name that identifies this client to other multiFLEX stations, then press Tab or Enter to commit. If left empty, AetherSDR uses the OS hostname as the default.
6. Click **Close** when finished.

## What each control does

| Control | Kind | Behavior | Default |
|---|---|---|---|
| **Nickname** | Text field | User-friendly name for the radio. Sent to the radio on commit. | Populated from the radio's current name if no nickname is set. |
| **Callsign** | Text field | Station callsign stored on the radio. Sent to the radio on commit. | Current value held by the radio. |
| **Station Name** | Text field | Identifies this AetherSDR client to other multiFLEX stations. Persisted locally. Sent to the radio on commit. | OS hostname if the field has never been set. |

## Tips

- All three fields send their value to the radio as soon as you finish editing (on focus loss or Enter). There is no separate Save button.
- **Station Name** is stored in AetherSDR's local settings under the key `StationName`. **Nickname** and **Callsign** are stored on the radio itself, not in AetherSDR's local settings.

## Related

- [Check radio serial, hardware version, region and options](check-radio-serial-hardware-version-region-and-options.md)
- [Radio Setup overview](overview.md)
