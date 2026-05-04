# Check which antenna and frequency each TX station is using

AetherSDR tracks every other GUI client connected to the same radio and exposes each client's current TX antenna and frequency. Use the Connected Client Info list to see at a glance what each station is transmitting on.

## Steps

1. Open the connected clients panel in the GUI to display the list of `ClientInfo` entries — one row per connected client.
2. For each entry, read the **TX Antenna** field to see which antenna that client is using and the **TX Frequency** field to see the frequency it is currently transmitting on.

## What each control does

| Control | Behavior |
|---|---|
| Station Name | Identifies the remote client by its configured station name. |
| Program | Shows the software the remote client is running. |
| Source IP / Host | Displays the IP address or hostname the client is connecting from. |
| Local PTT | Indicates whether that client currently holds local PTT rights. |
| TX Antenna | Shows the antenna the client has selected for transmit. |
| TX Frequency | Shows the frequency (in Hz) the client is currently set to transmit on. |

## Tips

- If a client is not actively transmitting, its TX Antenna and TX Frequency fields still reflect the last-known configured values, not a live keyed state. Check the Local PTT field to confirm whether the client is currently keyed.

## Related

- [connected-clients-overview.md](connected-clients-overview.md)
- [ptt-rights.md](ptt-rights.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
