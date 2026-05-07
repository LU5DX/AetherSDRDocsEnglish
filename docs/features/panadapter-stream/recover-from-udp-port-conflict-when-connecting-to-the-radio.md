# Recover from UDP port conflict when connecting to the radio

When the radio rejects the initially chosen UDP port because another client is already using it, AetherSDR automatically releases that port, asks the OS to assign a new one, and re-registers with the radio so the data stream resumes without manual intervention.

## Before you start

- Ensure the radio is powered on and reachable on the network.
- Ensure no firewall rule blocks outbound UDP traffic from AetherSDR to the radio on port 4992.

## Steps

1. Attempt to connect to the radio as normal. If the initially chosen UDP port is already in use, AetherSDR detects the rejection and calls the internal recovery path automatically.
2. Wait a moment. AetherSDR closes the conflicting socket, binds a new socket to an OS-assigned (ephemeral) port, and re-sends the UDP registration to the radio. No user action is required.

If the connection does not recover after a few seconds, disconnect and reconnect manually using the connect button in the toolbar.

## What each control does

| Control | Behavior |
|---|---|
| `rebindToEphemeralPort` | Closes the rejected UDP socket, opens a new socket bound to an OS-assigned port, sends a fresh UDP registration datagram to the radio on port 4992, and resumes the panadapter data stream. |

## Tips

- If port conflicts occur repeatedly, another SDR client application may be running in the background and holding the same port. Close any other SDR applications before connecting.
- Check the application log for messages containing `PanadapterStream: sent UDP registration` to confirm the recovery succeeded.

## Related

- [connecting-to-the-radio.md](connecting-to-the-radio.md)
- [troubleshoot-network-connection.md](troubleshoot-network-connection.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
