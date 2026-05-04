# Connect to the radio over a local network

`RadioConnection` manages the TCP control connection to your radio over a LAN or WAN and coordinates the UDP stream registration so audio and panadapter data flows to the correct port on your machine.

## Before you start

- Your radio and computer must be on the same local network.
- Confirm the radio is powered on and reachable (ping its IP address if unsure).
- If your computer has more than one network interface (NIC), identify which interface is on the same subnet as the radio.

## Steps

1. Open the connection settings in AetherSDR and enter the radio's IP address.
2. Select the local network interface to use. If you have a single NIC, leave this on **Automatic**. For multi-NIC setups, pick the interface on the same subnet as the radio. AetherSDR supports explicit, session-probed, and automatic local bind address selection.
3. Click **Connect**. AetherSDR opens a TCP control connection to the radio, then registers a local UDP port for the panadapter and audio stream. If the radio reports that the selected port or IP pair is already registered by another client, AetherSDR automatically rebinds to an OS-assigned ephemeral UDP port and re-registers.
4. Verify the connection indicator shows **Connected** before operating the radio.

To disconnect cleanly, click **Disconnect**. AetherSDR sends a stream-remove command and waits for the radio to acknowledge it before closing the TCP socket. This prevents stale session entries on the radio when you reconnect.

## What each control does
| Control | Behavior |
|---|---|
| Radio IP address | Sets the TCP destination the connection is opened to. |
| Local bind address | Controls which NIC AetherSDR uses to source the TCP and UDP traffic. Set to **Automatic** to let AetherSDR choose, or enter a specific interface IP for multi-NIC machines. |
| Connect | Opens the TCP control connection and registers the UDP stream port with the radio. |
| Disconnect | Sends a `stream remove` command, waits for acknowledgement (up to 2 seconds), then closes the TCP socket cleanly. A disconnect marker is also written to the session log before the socket closes. |

## Tips

- If you see repeated "port already registered" errors, another AetherSDR session (or a previous session that did not disconnect cleanly) may still be registered on the radio. Power-cycle the radio or wait for the radio's session timeout to clear it.
- On a machine with multiple NICs (e.g., a dedicated RF network plus a management network), always set the local bind address explicitly to the interface that can reach the radio. Using **Automatic** on a multi-NIC machine can result in traffic being sourced from the wrong interface.
- The connection sends a heartbeat every 30 seconds to keep the TCP session alive on NAT routers and firewalls.

## Related

- [Connect to the radio over a WAN](connect-wan.md)
- [Panadapter stream setup](panadapter-stream.md)
- [Troubleshoot connection errors](troubleshoot-connection.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
