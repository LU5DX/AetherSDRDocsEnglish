# Prevent duplicate DAX channel routing after reconnect

`PanadapterStream::registerDaxStream` routes incoming audio packets for a specific DAX channel to the correct audio output. When you reconnect to a radio, it automatically evicts any stale stream previously registered to the same channel, preventing double-speed playback caused by duplicate routing.

## Before you start

- Ensure you have an active or recently interrupted connection to the radio.
- Confirm the DAX channel number you intend to use is known before reconnecting.

## Steps

1. Reconnect to the radio as you normally would (for example, re-enter the radio's address and initiate the connection).
2. AetherSDR automatically calls `registerDaxStream` for each DAX channel during the connection handshake. No manual action is required — any stale stream registered to the same channel is evicted before the new stream is registered.

## What each control does

| Control | Behavior |
|---|---|
| `registerDaxStream` (stream ID, DAX channel) | Registers the radio's stream ID with the given DAX channel number. If a previous stream ID is already mapped to that channel, it is removed first, then the new stream ID is registered. This prevents two streams from feeding the same audio output simultaneously. |

## Tips

- If audio still plays back at double speed after a reconnect, check that your radio firmware is current. The eviction logic depends on the stream ID supplied by the radio being updated on reconnect; a firmware bug that reuses stale stream IDs can interfere with correct eviction.
- You do not need to manually close or unregister DAX channels before disconnecting — the eviction step at registration time handles cleanup on the next connect.

## Related

- [DAX channel configuration](dax-channel-configuration.md)
- [Connecting to a radio](connecting-to-a-radio.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
