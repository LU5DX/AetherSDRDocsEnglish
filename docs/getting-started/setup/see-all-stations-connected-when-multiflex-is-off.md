# See all stations connected when multiFLEX is off

Use the Connected Stations dialog to view every client currently connected to your FLEX-8600 radio when multiFLEX is disabled. This helps you identify which station to disconnect before AetherSDR can take a connection slot.

## Before you start

- Your radio must be powered on and reachable on the network.
- multiFLEX must be disabled on the radio (the dialog only appears under this condition).
- AetherSDR must be in the process of connecting to the radio (the dialog appears automatically, or you can open it manually).

## Steps

1. Open AetherSDR and attempt to connect to your radio.
   - If multiFLEX is disabled and another client is already connected, **Connected Stations** appears automatically.
2. If you need to open it later: **Help > Connected Stations...**
3. Read the **Radio** section at the top to confirm the radio model, nickname, and callsign.
4. Review the **Connected Stations** list below. Each entry shows the client program name and optionally the station name.
   - If no program or station name is known, the entry shows `client 0x<HEX>`.
5. Select the radio button next to the station you want to disconnect.
6. Click **Disconnect Station**.
7. The dialog closes, and AetherSDR proceeds with its connection.

## What each control does

| Control | Behavior |
|---|---|
| **Radio** section | Read-only info block showing the connected radio model, nickname, and callsign. |
| Station radio buttons | Select which station to disconnect. Each entry shows the client program name and optionally the station name. Fallback: `client 0x<HEX>`. |
| **Disconnect Station** | Disconnects the selected station. Enabled only when a radio button is checked. |
| **Cancel** | Closes the dialog without disconnecting. |
| Info label | Reads "multiFLEX is disabled on this radio. Select a station to disconnect before connecting AetherSDR." |

## Tips

- The dialog centers itself on the screen where AetherSDR is located, or on your primary monitor if unavailable.
- You cannot connect AetherSDR while another client occupies the sole slot — you must disconnect one first.

## Related

- [Disconnect another client to free a slot](disconnect-another-client-to-free-a-slot.md)
- [Identify each client by program and station name](../../features/connected-stations/identify-each-client-by-program-and-station-name.md)
- [Connected Stations overview](../../features/connected-stations/overview.md)
- [See all stations connected to this FLEX](see-all-stations-connected-to-this-flex.md)
