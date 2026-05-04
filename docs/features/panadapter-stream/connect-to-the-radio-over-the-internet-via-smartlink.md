# Connect to the radio over the internet via SmartLink

SmartLink lets you receive radio data from a remote radio over a WAN connection. AetherSDR binds a local UDP port and registers it with the remote radio's UDP endpoint so data can flow over the internet.

## Before you start

- Your radio must be reachable via SmartLink and your account must have access to it.
- Your local firewall must allow outbound UDP traffic.

## Steps

1. Open your radio connection settings and select the SmartLink (WAN) connection type for your radio.
2. Click **Connect**. AetherSDR automatically binds a local UDP port and registers it with the remote radio to begin the WAN data stream.

## What each control does

| Control | Behavior |
|---|---|
| Connection type (SmartLink/WAN) | Switches the panadapter stream into WAN mode. AetherSDR binds an OS-assigned local UDP port instead of attempting fixed ports, then registers that port with the remote radio's UDP endpoint. |
| Local bind address | Determined automatically from your connection. AetherSDR checks, in order: any explicitly configured local address, the probe-session address, then the TCP local address. If none are found it binds to all IPv4 interfaces (`0.0.0.0`). |

## Tips

- AetherSDR assigns the UDP port automatically. You do not need to open or forward a specific port on your router for outbound WAN connections.
- If the connection fails, check that your firewall is not blocking outbound UDP and that your SmartLink credentials are valid.

## Related

- [Connect to the radio on a local network](connect-lan.md)
- [SmartLink account setup](smartlink-account-setup.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
