# Disable a DAX IQ channel

When a DAX IQ stream is no longer active, use `unregisterIqStream` to stop routing DAX IQ samples for that stream and release the associated resources.

## Before you start

- Confirm the DAX IQ channel is currently active and streaming.
- Ensure you have an open connection to the radio before making changes.

## Steps

1. Identify the stream ID of the DAX IQ channel you want to disable.
2. Call `PanadapterStream::unregisterIqStream` with that stream ID to stop sample routing for the stream.

## What each control does

| Control | Behavior |
|---|---|
| `unregisterIqStream` | Stops routing DAX IQ samples for the specified stream. Call this when the stream is no longer active to cleanly release it. |

## Tips

- Always call `unregisterIqStream` before closing the associated connection or destroying the stream object. Skipping this step may leave the channel registered until the session ends.
- If you need to re-enable the channel later, start a new stream and register it again through the normal activation flow.

## Related

- [Enable a DAX IQ channel](enable-dax-iq-channel.md)
- [PanadapterStream overview](panadapter-stream.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
