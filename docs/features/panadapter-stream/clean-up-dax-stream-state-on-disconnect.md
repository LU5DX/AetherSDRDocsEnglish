# Clean up DAX stream state on disconnect

When a DAX RX stream is no longer active, `PanadapterStream::unregisterDaxStream` stops routing audio for that stream and frees the channel for other use.

## Steps

1. Disconnect the DAX RX stream from within your application or client. AetherSDR automatically calls `unregisterDaxStream` to stop audio routing and release the channel.
2. Confirm the channel is free by attempting to register a new DAX RX stream on the same channel. If the cleanup completed successfully, the channel will be available immediately.

## What each control does

| Control | Behavior |
|---|---|
| `PanadapterStream::unregisterDaxStream` | Stops routing audio for the specified DAX RX stream and frees the associated channel so another stream can claim it. |

## Tips

- Unregistration happens automatically on disconnect. You do not need to call any additional cleanup method after the stream closes.
- If a channel appears unavailable after a disconnect, verify that the disconnect was clean and that `unregisterDaxStream` was reached. An ungraceful connection drop may delay channel release until the connection timeout expires.

## Related

- [DAX stream overview](dax-stream-overview.md)
- [PanadapterStream reference](panadapter-stream.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
