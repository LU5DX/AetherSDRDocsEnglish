# Disable a DAX receive channel

When a DAX RX stream is no longer active, use `unregisterDaxStream` to stop routing audio for that channel and free it for other use.

## Before you start

- Confirm the DAX RX channel you want to disable is currently active and assigned to a panadapter stream.
- Note the channel number you intend to free.

## Steps

1. In the DAX panel, locate the active RX channel you want to disable.
2. Deactivate the channel by toggling it off (click the enabled/active control for that channel). AetherSDR calls `unregisterDaxStream` internally, stops audio routing for that stream, and releases the channel.

## What each control does

| Control | Behavior |
|---|---|
| DAX RX channel toggle | Enables or disables audio routing for the selected DAX RX channel. Turning it off unregisters the stream and frees the channel number for other use. |

## Tips

- A freed channel becomes immediately available for reassignment to another panadapter or application.
- If audio from the channel persists after disabling, check that no other client holds a reference to the same stream slot.

## Related

- [Configure a DAX receive channel](configure-dax-rx-channel.md)
- [DAX overview](dax-overview.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
