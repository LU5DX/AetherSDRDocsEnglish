# Connect to the radio over the internet via SmartLink

SmartLink lets you receive radio data over a WAN connection by binding a local UDP port and registering with the remote radio's UDP endpoint.

## Before you start

- Your radio must be reachable over the internet and have SmartLink enabled.
- You must have a valid SmartLink account and your radio must be linked to it.
- Ensure your local firewall allows outbound UDP traffic.

## Steps

1. Open the radio connection dialog and select your radio from the SmartLink list.
2. Click **Connect**. AetherSDR binds a local UDP port, sends a registration datagram to the radio, and begins the WAN ping keepalive (every 5 seconds) to maintain the connection.

## What each control does

| Control | Behavior |
|---|---|
| SmartLink radio list | Lists radios registered to your SmartLink account that are currently reachable over the WAN. |
| **Connect** | Initiates the WAN connection: binds a local UDP port, sends `client udp_register` to the radio, and starts a 5-second ping keepalive to hold the session open. |

## Tips

- If the connection stalls after clicking **Connect**, check that UDP port 4992 is not blocked on either end — the registration datagram is sent to port 4992 on the radio.
- The keepalive ping fires every 5 seconds automatically; you do not need to keep the connection dialog open once connected.

## Related

- [connect-local.md](connect-local.md)
- [network-quality-monitor.md](network-quality-monitor.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
