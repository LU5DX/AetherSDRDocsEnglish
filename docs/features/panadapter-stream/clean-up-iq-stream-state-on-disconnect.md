# Clean up IQ stream state on disconnect

`PanadapterStream::unregisterIqStream` stops routing DAX IQ samples for a specific stream when that stream is no longer active, ensuring no stale state remains after a disconnect.

## Before you start

- Confirm the IQ stream you want to clean up is no longer in use.
- Ensure you have an active connection to the radio before initiating a disconnect sequence.

## Steps

1. Disconnect the IQ stream through your application or client. AetherSDR automatically calls `unregisterIqStream` to halt sample routing for that stream.
2. Verify the stream is no longer listed as active in your client. No further action is required — the SDK releases the associated UDP socket state and stops all sample delivery for that stream ID.

## What each control does

| Control | Behavior |
|---|---|
| `unregisterIqStream` | Stops routing DAX IQ samples for the specified stream. Releases the stream's UDP socket binding and clears all associated IQ stream state. |

## Tips

- If you restart a stream immediately after disconnecting, wait for the unregister operation to complete before calling the start sequence again to avoid port conflicts.
- Check application logs for `PanadapterStream: LAN VITA UDP bind` entries to confirm a clean rebind when the stream is re-established.

## Related

- [panadapter-stream.md](panadapter-stream.md)
- [dax-iq-overview.md](dax-iq-overview.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
