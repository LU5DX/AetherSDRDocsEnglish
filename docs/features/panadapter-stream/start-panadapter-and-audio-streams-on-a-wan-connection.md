# Start panadapter and audio streams on a WAN connection

`PanadapterStream::startWan` binds a local UDP port and registers it with the remote radio's UDP endpoint so that panadapter and audio data can flow over a WAN (SmartLink) connection.

## Before you start

- You must have an active SmartLink (WAN) session established with the radio before starting streams.
- The local machine must allow outbound UDP traffic on the ephemeral port assigned by the OS.

## Steps

1. Establish a SmartLink connection to the radio through the normal connection dialog.
2. Call `startWan` on the `PanadapterStream` instance associated with that connection. The SDK binds a local UDP socket to an OS-assigned ephemeral port using `DontShareAddress` mode and registers the port with the remote radio endpoint automatically.

## What each control does

| Control | Behavior |
|---|---|
| Local UDP bind address | Resolved from the connection in priority order: explicit local bind address → probe-session address → TCP local address → `0.0.0.0` (any IPv4) if none is available. |
| Local UDP port | Assigned by the OS (ephemeral). The port number is logged after a successful bind and sent to the remote radio for registration. |
| Bind mode | Always `DontShareAddress` — the socket is not shared with other processes on the same host. |

## Tips

- If the bind fails, check that the OS is not blocking UDP socket creation for the process. The error string from the socket is written to the `lcVita49` log category and can help diagnose the problem.
- For LAN connections the SDK previously tried port 4991 and counted down; on WAN connections the OS always assigns the port, so no manual port configuration is needed or available.

## Related

- [Connect to a radio over SmartLink](connect-smartlink.md)
- [Start panadapter and audio streams on a LAN connection](start-streams-lan.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
