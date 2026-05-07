# Start panadapter and audio streams on a WAN connection

`PanadapterStream::startWan` binds a local UDP port and registers it with the remote radio's UDP endpoint so that panadapter and audio data can flow over a WAN (SmartLink) connection.

## Before you start

- A SmartLink account must be configured and the radio must be reachable through the SmartLink relay.
- The radio must be added to your station list before you attempt to connect.

## Steps

1. In the radio connection list, select the remote radio you want to use.
2. Choose **WAN / SmartLink** as the connection type and click **Connect**.

AetherSDR binds a local UDP port, sends a `client udp_register` command to the radio, and starts a 5-second ping keepalive. Panadapter and audio streams begin flowing automatically once registration is acknowledged.

## What each control does

| Control | Behavior |
|---|---|
| **Connection type selector** | Switches between LAN and WAN (SmartLink) modes. Select **WAN / SmartLink** to use the remote path. |
| **Connect button** | Initiates the WAN handshake: binds the local UDP port, sends the registration datagram to the radio on port 4992, and starts the ping keepalive timer (every 5 seconds). |

## Tips

- If the stream does not start within a few seconds, check that your firewall allows outbound UDP on port 4992.
- The connection sends a one-byte registration probe periodically until the radio acknowledges. You do not need to retry manually.
- Packet error and total counts are tracked per stream and can be read via `packetErrorCount()` and `packetTotalCount()` to monitor WAN link quality.

## Related

- [Connect to a radio over LAN](connect-lan.md)
- [Configure SmartLink credentials](smartlink-setup.md)
- [Monitor network stream quality](network-quality-monitor.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
