# Disconnect another client to free a slot

When multiFLEX is disabled on your FLEX-8600, only one client can be connected at a time. If another client is already connected, this page shows you how to disconnect it so AetherSDR can connect.

## Before you start

- AetherSDR must be trying to connect to a radio where multiFLEX is disabled and another client is already connected. The Connected Stations dialog appears automatically in this situation.
- You do not need to use the menu to open the dialog — it opens on its own when the radio rejects the connection.

## Steps

1. If the Connected Stations dialog does not appear automatically, open it manually: **Help > Connected Stations...**
2. In the **Connected Stations** section, click the radio button next to the client you want to disconnect. Each entry shows the client program name and optionally the station name. Unknown clients are labelled "client 0x&lt;HEX&gt;".
3. Click **Disconnect Station** (the red button). The button is enabled only after you select a station.
4. AetherSDR will now attempt to connect to the freed slot.

## What each control does

| Control | Description |
|---|---|
| **Radio section** | Read-only section at the top showing the radio model, nickname, and callsign of the connected radio. Section header reads "Radio". |
| **Station radio buttons** | One for each connected client. Selecting one enables **Disconnect Station**. Each entry shows the client program name and optionally the station name. Fallback label is "client 0x&lt;HEX&gt;" if no program or station is known. |
| **Disconnect Station** | Disconnects the selected client from the radio. Label is "Disconnect Station" and appears in red. Enabled only when a station radio button is checked. |
| **Cancel** | Closes the dialog without disconnecting. |
| **Info label** | Explains that multiFLEX is disabled on this radio and you must select a station to disconnect before connecting AetherSDR. Full text: "multiFLEX is disabled on this radio. Select a station to disconnect before connecting AetherSDR." |

## Troubleshooting

- **The Disconnect Station button is grayed out** — Select a station by clicking its radio button. The button stays disabled until a selection is made.
- **The dialog does not appear, but you know another client is connected** — Open it manually via **Help > Connected Stations...**
- **The dialog appears with a dark theme on first launch** — This is expected behavior. The dialog now applies theme styling immediately upon opening, ensuring a consistent visual appearance across all supported operating systems.

## Related

- [See all stations connected when multiFLEX is off](see-all-stations-connected-when-multiflex-is-off.md)
- [Identify each client by program and station name](../../features/connected-stations/identify-each-client-by-program-and-station-name.md)