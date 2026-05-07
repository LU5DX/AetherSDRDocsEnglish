# Disable a DAX receive channel

Stops audio routing for a specific DAX RX stream, freeing that channel so another application or slice can claim it.

## Before you start

- Confirm the DAX RX channel you want to disable is currently active and assigned to a slice receiver.
- Close any application (such as a DAX client or audio bridge) that is consuming the stream before disabling it.

## Steps

1. In the **DAX** panel, locate the RX channel you want to stop.
2. Click the active channel button to deselect it. AetherSDR calls `unregisterDaxStream` internally, halts audio routing for that stream, and marks the channel as available.

## What each control does

| Control | Behavior |
|---|---|
| DAX RX channel button (active state) | Toggles the channel on or off. Turning it off stops all audio routing for that stream and releases the channel slot for other use. |

## Tips

- After disabling, verify the channel indicator is no longer highlighted before reassigning the slot to a different slice or application.
- If a client application holds the audio device open, the channel may not release immediately; close the client first, then disable the channel.

## Related

- [Enable a DAX receive channel](enable-dax-rx-channel.md)
- [Configure DAX TX audio](configure-dax-tx.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
