# Clean up IQ stream state on disconnect

`PanadapterStream::unregisterIqStream` stops routing DAX IQ samples for a specific stream as soon as that stream is no longer active, ensuring stale state does not accumulate after a disconnect.

## Before you start

- You must have an active DAX IQ stream configured before a disconnect event can trigger cleanup.
- AetherSDR V0.9.7 or later is required.

## Steps

1. Disconnect the DAX IQ client (close the client application or drop the network connection). AetherSDK automatically calls `unregisterIqStream` for the affected stream ID — no manual action is required.
2. Confirm the stream is gone: open the DAX IQ panel and verify the disconnected stream no longer appears in the active stream list.

## What each control does

| Control | Behavior |
|---|---|
| `unregisterIqStream` (internal) | Removes the stream ID from the active IQ routing table and stops forwarding DAX IQ samples for that stream. Called automatically on disconnect. |

## Tips

- If a stream entry persists in the DAX IQ panel after disconnecting, restart the radio connection to force a full state reset.
- Per-category packet and byte statistics (`categoryStats`) are now mutex-protected; stat reads after a disconnect reflect only samples received before the stream was unregistered.

## Related

- [DAX IQ overview](dax-iq-overview.md)
- [PanadapterStream reference](panadapter-stream-reference.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
