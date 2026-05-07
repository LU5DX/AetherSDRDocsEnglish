# Clean up DAX stream state on disconnect

When a DAX RX stream becomes inactive, AetherSDR must release its channel slot so other streams or applications can use it. `PanadapterStream::unregisterDaxStream` stops audio routing for that stream and frees the channel.

## Before you start

- Confirm the DAX RX stream you want to release is no longer in active use.
- Ensure you are connected to the radio before attempting stream management.

## Steps

1. Disconnect or stop the client session that owns the DAX RX stream. AetherSDR automatically calls `unregisterDaxStream` when it detects the stream is no longer active, halting audio routing and releasing the DAX channel.
2. Verify the channel is free by checking that no audio is being routed to the previously assigned DAX RX slot. You can confirm this in the panadapter or DAX channel status display.

## What each control does

| Control | Behavior |
|---|---|
| `unregisterDaxStream` | Stops routing audio for the specified DAX RX stream. Releases the associated channel so it becomes available for other streams or applications. Called automatically on disconnect. |

## Tips

- You do not need to call `unregisterDaxStream` manually in normal operation — it runs automatically when a client disconnects or a stream goes inactive.
- If a DAX channel appears stuck or unavailable after a disconnect, restart the client session to trigger re-registration.

## Related

- [DAX stream overview](dax-stream-overview.md)
- [PanadapterStream reference](panadapter-stream.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
