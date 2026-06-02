# Identify each client by program and station name

Use the Connected Stations dialog to see detailed identification (program name and optional station name) for every client connected to your FLEX-8600. This helps you recognize which client to disconnect when multiFLEX is disabled and another session is active.

## Before you start

- Your radio must be connected to AetherSDR.

## Steps

1. Open **Help > Connected Stations…**.

2. In the Radio section, confirm the radio model, nickname, and callsign shown.

3. In the Connected Stations section, review each radio button entry. Each entry displays the client’s program name, and the station name if set, in the format `ProgramName: StationName`.

   – If the client does not report a program or station name, it falls back to `client 0x<HEX>`.

4. To disconnect a client, select its radio button and click **Disconnect Station**.

5. Click **Cancel** to close the dialog without disconnecting.

## What each control does

| Control | Description |
|---|---|
| Radio section | Read-only block showing the connected radio model, nickname, and callsign. |
| Station radio buttons | One per connected client. Label shows program name, optionally followed by `: StationName`. |
| Disconnect Station | Disconnects the selected client. Enabled only when a radio button is checked. |
| Cancel | Closes the dialog without disconnecting. |
| Info label | Explains that multiFLEX is disabled and you must select a station to disconnect before connecting AetherSDR. |

## Theme support

The dialog applies the `dialog/connectedStations` theme container, ensuring consistent styling with other themed dialogs in AetherSDR.

## Related

- [Connected Stations overview](overview.md)
- [Disconnect another client to free a slot](../../getting-started/setup/disconnect-another-client-to-free-a-slot.md)
- [See all stations connected when multiFLEX is off](../../getting-started/setup/see-all-stations-connected-when-multiflex-is-off.md)