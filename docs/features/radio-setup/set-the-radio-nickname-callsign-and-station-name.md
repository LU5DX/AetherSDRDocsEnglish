# Set the Radio Nickname, Callsign and Station Name

Set the human-readable name, callsign, and station identifier stored on your FLEX-8600. These values appear in multiFLEX client lists and help identify your radio on the network.

## Before you start

- AetherSDR must be connected to the radio. The Radio (tab) controls are not available without an active radio connection.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Radio** tab if it is not already selected.
3. In the **Radio Identification** group, locate the **Nickname** field. Type the name you want to assign to the radio.
4. Press Tab or click away from the field. AetherSDR sends the new nickname to the radio immediately.
5. In the **Callsign** field, type your station callsign.
6. Press Tab or click away from the field. AetherSDR sends the callsign to the radio immediately.
7. In the **Station Name** field, type the name for this client station. This value identifies your AetherSDR instance to other multiFLEX stations. If left empty, it defaults to the OS hostname.
8. Press Tab or click away from the field. AetherSDR saves the value locally and sends it to the radio immediately.

## What each control does

| Control | Description | Default | Persisted setting |
|---|---|---|---|
| **Nickname** | User-friendly name assigned to the radio. | Populated from the radio's stored name if set. | Stored on the radio, not in AppSettings. |
| **Callsign** | Station callsign stored on the radio. | Populated from the radio's stored callsign if set. | Stored on the radio, not in AppSettings. |
| **Station Name** | Name for this AetherSDR client, sent to the radio as the client station identifier. | OS hostname if no value has been saved. | `StationName` |

## Tips

- Each field saves as soon as you finish editing it — there is no separate Save button. Move focus away from the field to trigger the update.
- **Station Name** is particularly useful in multiFLEX setups where more than one client connects to the same radio simultaneously. Set a distinct name on each machine.

## Related

- [Check radio serial, hardware version, region and options](check-radio-serial-hardware-version-region-and-options.md)
- [Radio Setup overview](overview.md)
