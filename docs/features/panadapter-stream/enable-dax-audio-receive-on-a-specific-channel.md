# Enable DAX audio receive on a specific channel

Registering a DAX stream routes incoming audio packets for a specific DAX channel to the correct audio output. If a stale stream registration exists for that channel, it is automatically removed before the new one is applied, preventing double-speed playback after a reconnect.

## Before you start

- Confirm the radio is connected and a panadapter stream is active for the slice you want to receive audio from.
- Know the DAX channel number you intend to use.

## Steps

1. Identify the stream ID returned by the radio for the panadapter you want to receive DAX audio on.
2. Call `PanadapterStream::registerDaxStream`, passing the radio-assigned stream ID and the target DAX channel number.

```cpp
// Example: register stream ID 0x4C000001 to DAX channel 2
panadapterStream->registerDaxStream(streamId, daxChannel);
```

The method evicts any previously registered stream on that channel before applying the new registration.

## What each control does

| Parameter | Behavior |
|---|---|
| `streamId` | The radio-assigned stream ID for the incoming audio packets. Used to identify which UDP audio stream to route. |
| `daxChannel` | The DAX channel number to receive audio on. Any stale stream already mapped to this channel is removed first. |

## Tips

- Always re-register the stream after a reconnect. The automatic eviction of the old stream ID prevents the duplicate-routing issue that causes audio to play back at double speed.
- Use a unique DAX channel number per slice to avoid unintended eviction of a channel you are actively using elsewhere.

## Related

- [Configure a panadapter stream](configure-panadapter-stream.md)
- [DAX audio overview](dax-audio-overview.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
