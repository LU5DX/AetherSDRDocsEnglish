# Troubleshoot DAX RX audio routing or double-speed playback

DAX RX audio is routed by associating the radio's stream ID with a specific DAX channel number. If that association becomes stale after a reconnect, audio can play back at double speed because the same channel receives duplicate streams.

## Before you start

- Confirm you can connect to the radio from AetherSDR.
- Note which DAX RX channel number is affected.

## Steps

1. Disconnect from the radio, then reconnect. On reconnect, AetherSDR calls `registerDaxStream` internally, which evicts any stale stream previously registered to the same DAX channel and registers the current stream ID in its place.
2. Open the DAX panel and verify the affected RX channel shows a single active stream. If audio still plays at double speed, repeat the disconnect/reconnect cycle — the eviction runs automatically each time a new stream registers for that channel.

## What each control does

| Control | Behavior |
|---|---|
| DAX RX channel registration | Maps an incoming audio packet stream (identified by stream ID) to a DAX channel number. Only one stream ID may be active per channel at a time. |
| Stale stream eviction | When a new stream ID registers for a channel that already has a stream, the old stream is removed automatically before the new one is added. This prevents the double-speed playback that occurs when two streams feed the same channel simultaneously. |

## Tips

- Double-speed playback after reconnect is the most common sign of a duplicate stream registration. A single disconnect/reconnect cycle is usually sufficient to clear it.
- If you are running multiple GUI clients connected to the same radio, each client manages its own stream registration independently. Ensure only the intended client is active on a given DAX RX channel to avoid conflicts.

## Related

- [DAX overview](dax-overview.md)
- [Connect to a radio](connect-to-radio.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
