# Connected Stations overview

When multiFLEX is disabled on your FLEX-8600, only one client station can be connected at a time. The Connected Stations dialog lists every client currently connected to the radio, so you can identify and disconnect another session before connecting AetherSDR.

## How it works

The dialog opens automatically when AetherSDR attempts to connect to a radio that has multiFLEX disabled and another client already connected. You can also open it manually from **Help > Connected Stations...**.

The dialog is divided into two sections:

**Radio section** — Displays the connected radio's model, nickname, and callsign as read-only information. This helps confirm you are looking at the correct radio.

**Connected Stations section** — Lists each connected client with a radio button. For each entry, you see the client program name and, if available, the station name. If neither is known, the fallback label shows "client 0x<HEX>" using the client's handle.

Select a station by clicking its radio button, then click **Disconnect Station** to remove that client from the radio. The button is enabled only when a station is selected. Click **Cancel** to close the dialog without disconnecting.

## What each control does

| Control | Behavior | Notes |
|---------|----------|-------|
| Radio section | Read-only block showing radio model, nickname, and callsign | Section header reads "Radio" |
| Station radio buttons | Selects which station to disconnect | Each entry shows program name and optionally station name. Fallback: "client 0x<HEX>" |
| **Disconnect Station** | Disconnects the selected station from the radio | Enabled only when a radio button is checked. Styled red/dark themed |
| **Cancel** | Closes the dialog without disconnecting | |
| Info label | Explains that multiFLEX is disabled and a station must be disconnected first | Full text: "multiFLEX is disabled on this radio. Select a station to disconnect before connecting AetherSDR." |

## Tips

- The dialog is application-modal — you cannot interact with the main AetherSDR window until you either disconnect a station or click Cancel.
- The dialog applies the theme container styling `dialog/connectedStations` for consistent appearance with the rest of the application.

## Related

- [Disconnect another client to free a slot](../../getting-started/setup/disconnect-another-client-to-free-a-slot.md)
- [Identify each client by program and station name](identify-each-client-by-program-and-station-name.md)
- [See all stations connected when multiFLEX is off](../../getting-started/setup/see-all-stations-connected-when-multiflex-is-off.md)