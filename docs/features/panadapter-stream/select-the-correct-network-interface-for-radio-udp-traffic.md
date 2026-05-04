# Select the correct network interface for radio UDP traffic

AetherSDR's `RadioConnection` class manages both the TCP control connection to your radio and the UDP streams that carry panadapter and audio data. On machines with more than one network interface (NIC), you must tell the application which interface to use so UDP traffic reaches the correct client port.

## Before you start

- Your radio must be reachable on your local network (LAN) or via WAN.
- You must know the IP address assigned to the network interface that is on the same subnet as the radio.
- Close any existing connection to the radio before changing the bind address.

## Steps

1. Open **Settings > Network** and locate the **Local Bind Address** field.
2. Enter the IP address of the network interface that faces the radio (for example, `192.168.1.50`). Leave the field blank to let AetherSDR select the address automatically.
3. Click **Connect**. AetherSDR binds the UDP port to the specified interface and registers it with the radio using the `client udpport` command.
4. If the radio reports that the port or IP pair is already registered by another client, AetherSDR automatically rebinds to an OS-assigned (ephemeral) UDP port and re-registers. No action is required from you, but reconnecting resolves the conflict if it persists.

## What each control does

| Control | Behavior |
|---|---|
| **Local Bind Address** (blank) | AetherSDR probes the active TCP session to determine the best local interface automatically. Use this on single-NIC machines. |
| **Local Bind Address** (explicit IP) | Binds the UDP socket to the specified IP address. Required when multiple NICs are present and the automatic selection picks the wrong interface. |
| **Connect** | Opens the TCP control connection and registers the local UDP port with the radio so stream data is directed to this machine. |

## Tips

- On multi-NIC systems, the automatic selection may prefer a VPN or virtual adapter over your physical Ethernet port. Setting an explicit bind address avoids this.
- If you see no panadapter data after connecting, verify that the bound IP address is on the same subnet as the radio and that no firewall is blocking inbound UDP traffic on the registered port.
- LAN mode binds a unique local VITA UDP port per session. If a previous session was not cleanly torn down, the radio may still consider that port registered — disconnecting and reconnecting forces a fresh registration.

## Related

- [Connect to a radio over LAN](connect-lan.md)
- [Connect to a radio over WAN](connect-wan.md)
- [Troubleshoot UDP stream issues](troubleshoot-udp.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
