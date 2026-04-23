# Set the Radio Nickname, Callsign and Station Name

Change how the radio and this client identify themselves — the nickname appears in connection lists, the callsign is stored on the radio, and the station name identifies this AetherSDR client to other multiFLEX stations.

## Before you start

- AetherSDR must be connected to the radio. The Radio (tab) controls are unavailable without an active connection.

## Steps

1. Go to `Settings > Radio Setup...`.
2. Click the **Radio** tab if it is not already selected.
3. In the **Radio Identification** group, locate the **Nickname** field. Type the name you want to use for this radio and press Tab or Enter to confirm.
4. In the same group, locate the **Callsign** field. Type your callsign and press Tab or Enter to confirm.
5. Locate the **Station Name** field. Type the name that identifies this client to other multiFLEX stations and press Tab or Enter to confirm.
6. Click **Close**.

## What each control does

| Control | Behavior | Default | Persisted |
|---|---|---|---|
| **Nickname** | User-friendly name stored on the radio. Sent to the radio when you finish editing. | Populated from the radio's current name if no nickname is set. | On the radio (not in AetherSDR app settings) |
| **Callsign** | Station callsign stored on the radio. Sent to the radio when you finish editing. | Current callsign from the radio. | On the radio |
| **Station Name** | Identifies this AetherSDR client to other multiFLEX stations. Sent to the radio as the client station name. | OS hostname if the field has not been set before. | `StationName` |

## Tips

- Each field is applied immediately when you press Tab or Enter — there is no separate Save button for these fields.
- **Station Name** defaults to the operating system hostname if you have never entered a value. To restore that default, clear the field and press Enter, then re-open the dialog; it will show the hostname again.

## Related

- [Check radio serial, hardware version, region and options](check-radio-serial-hardware-version-region-and-options.md)
