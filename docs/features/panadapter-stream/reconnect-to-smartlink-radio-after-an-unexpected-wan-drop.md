# Reconnect to SmartLink radio after an unexpected WAN drop

`RadioConnection` manages the TCP control connection to the radio (LAN or WAN) and coordinates UDP stream registration so data flows to the correct client port. When the WAN link drops unexpectedly, you need to re-establish that TCP connection and confirm that UDP streams are re-registered to your client port.

## Before you start

- Confirm your internet connection is restored and the SmartLink server is reachable.
- Have your SmartLink login credentials available.

## Steps

1. Open the **Connection Panel** and locate the radio entry that shows a disconnected or error state.
2. Click **Connect** (or the equivalent reconnect control) for that SmartLink radio entry. `RadioConnection` will re-establish the TCP control connection and re-register UDP streams to your current client port automatically.

## What each control does

| Control | Behavior |
|---|---|
| Connection Panel radio entry | Displays available LAN and WAN (SmartLink) radios and their current connection state. |
| Connect | Initiates a new TCP control connection through SmartLink and triggers UDP stream re-registration to the correct client port. |

## Tips

- If the reconnect attempt fails immediately, wait 10–15 seconds before retrying — the SmartLink server may still be releasing the previous session.
- A successful reconnect restores both the TCP control channel and all UDP data streams (panadapter, audio, etc.) without requiring a full application restart.
- If the radio remains unreachable, verify the SmartLink server status independently before attempting further reconnects.

## Related

- [Connect to a radio over SmartLink (first-time setup)](smartlink-first-connect.md)
- [Diagnose network stream quality](network-diagnostics.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
