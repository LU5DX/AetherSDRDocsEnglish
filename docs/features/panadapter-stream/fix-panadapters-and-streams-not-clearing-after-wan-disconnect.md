# Fix panadapters and streams not clearing after WAN disconnect

`RadioConnection` manages the TCP control connection to the radio and coordinates UDP stream registration. Before this fix, panadapters and streams were not torn down cleanly when a WAN session ended, leaving stale entries on the radio that could block reconnection.

## Before you start

- You must be connected to the radio over WAN (not LAN) before performing a deliberate disconnect.
- Ensure no other clients are registered to the same GUIClientID on the radio.

## Steps

1. Disconnect from the radio using the normal disconnect control in the application. `RadioConnection` now sends a `stream remove` command and waits for the radio to acknowledge it (up to 2 seconds) before closing the TCP connection, ensuring the panadapter and audio streams are cleared on the radio side.
2. If the disconnect does not complete cleanly (for example, the radio does not acknowledge within the timeout), the application logs a disconnect summary showing whether the stream-remove was acknowledged (`streamAck=yes/no`) and how long each phase took. Check the application log for a line beginning `RadioConnection: disconnect summary` to confirm teardown status.

## What each control does

| Control | Behavior |
|---|---|
| Disconnect | Stops the heartbeat timer, sends a `stream remove 0x<streamId>` command to the radio and waits up to 2 000 ms for an acknowledgement, then closes the TCP socket. Previously this was fire-and-forget; now it waits for the radio to confirm before closing. |
| Reconnect | After a clean disconnect, the radio session table is cleared so a new connection using the same client identity succeeds without a stale-session error. |

## Tips

- If reconnection still fails after a WAN disconnect, check the log for `streamAck=no`. This means the radio did not acknowledge the stream removal within 2 seconds. The connection is still closed, but the radio may need a moment before it accepts a new session from the same client.
- On socket errors, `RadioConnection` now explicitly transitions to the `Disconnected` state when the socket is already unconnected, preventing the UI from showing a stale `Error` state.

## Related

- [RadioConnection overview](radio-connection.md)
- [WAN connection setup](wan-connection-setup.md)
- [Panadapter streams](panadapter-streams.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
