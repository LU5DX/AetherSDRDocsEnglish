# Reconnect to SmartLink radio after an unexpected WAN drop

`RadioConnection` manages the TCP control connection to the radio and coordinates UDP stream registration. When the WAN link drops unexpectedly, the radio may hold a stale session. The steps below clear that session and restore the connection.

## Before you start

- Confirm the SmartLink server is reachable and your internet connection has recovered.
- Note the radio's SmartLink host name or IP and the UDP port used for your stream — you may need these if automatic reconnection fails.

## Steps

1. In AetherSDR, open the connection panel and click **Disconnect** to trigger a clean teardown. `RadioConnection` will send a `stream remove` command and wait for the radio to acknowledge it before closing the TCP socket. This clears the stale session from the radio's session table.
2. Wait for the status indicator to show **Disconnected**, then click **Connect** and select your SmartLink radio. `RadioConnection` will open a new TCP control connection, negotiate a session handle, and re-register your UDP stream port with the radio.

## What each control does

| Control | Behavior |
|---|---|
| **Disconnect** | Sends an acknowledged `stream remove` command followed by a `client disconnect` message, then closes the TCP socket. Ensures the radio releases the session so reconnecting with the same client ID does not lock up the radio. |
| **Connect** | Opens a new TCP control connection to the radio (LAN or WAN). Selects a local bind address automatically (session-probed or OS-assigned) and registers the UDP stream port so panadapter and audio data flows to the correct client port. |

## Tips

- If the **Connect** attempt fails immediately with a port conflict error, `RadioConnection` will rebind to an OS-assigned ephemeral UDP port and retry — no manual action is needed.
- On multi-NIC machines, `RadioConnection` can probe the correct local interface automatically. If the wrong interface is selected, set the bind address explicitly in **Settings > Network > Local Bind Address** before reconnecting.
- Check the application log for a `disconnect summary` line (logged at the `Info` level). It shows whether the `stream remove` was acknowledged (`streamAck=yes`) and how long each teardown step took. A `streamAck=no` entry means the radio did not confirm teardown; allow an extra 5–10 seconds before reconnecting.

## Related

- [Connect to a SmartLink radio for the first time](connect-smartlink-first-time.md)
- [Configure local bind address for multi-NIC setups](configure-local-bind-address.md)
- [Panadapter stream troubleshooting](panadapter-stream-troubleshooting.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
