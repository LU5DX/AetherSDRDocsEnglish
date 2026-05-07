# Disable a DAX IQ channel

Stopping a DAX IQ channel unregisters the stream from the panadapter, halting the routing of DAX IQ samples for that stream.

## Before you start

- The DAX IQ channel must already be active and registered.
- You must have an active connection to the radio.

## Steps

1. Locate the DAX IQ channel you want to disable in the panadapter stream list.
2. Deactivate the channel. AetherSDR calls `unregisterIqStream` internally, which stops routing IQ samples for that stream immediately.

## What each control does

| Control | Behavior |
|---|---|
| DAX IQ channel toggle | Disables the selected DAX IQ channel and stops all IQ sample routing for that stream. |

## Tips

- Disabling a channel does not affect other active DAX IQ channels on the same panadapter.
- If you need to re-enable the channel later, reactivate it from the same control — the stream will re-register automatically.

## Related

- [Enable a DAX IQ channel](enable-dax-iq-channel.md)
- [DAX IQ overview](dax-iq-overview.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
