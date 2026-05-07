# Enable DAX audio receive on a specific channel

`PanadapterStream::registerDaxStream` routes incoming audio packets for a specific DAX channel to the correct audio output by binding the radio's stream ID to a DAX channel number, so each channel receives only its own audio.

## Before you start

- Confirm the radio is connected and a panadapter stream is active.
- Know the DAX channel number you want to receive audio on.

## Steps

1. Open the DAX audio settings for the panadapter you want to configure.
2. Select the target DAX channel number from the channel selector.
3. Enable the **DAX RX** option for that channel. AetherSDR registers the radio's stream ID with the selected channel, and incoming audio packets are routed to that channel's audio output.

## What each control does

| Control | Behavior |
|---|---|
| DAX channel number | Identifies which DAX receive channel the stream is bound to. Each channel number maps to a unique stream ID; selecting the wrong number causes audio to route to the wrong output. |
| DAX RX enable | Triggers the stream registration that links the radio's VITA-49 stream ID to the selected channel. Disabling it unregisters the stream and stops audio delivery to that channel. |

## Tips

- Each DAX channel can only be bound to one stream at a time. If audio is not arriving, check that no other panadapter or client has already registered the same channel number.
- Stream registration is re-applied automatically when the connection is re-established after a disconnect.

## Related

- [Configure DAX audio output devices](configure-dax-audio-output-devices.md)
- [Start a panadapter stream](start-panadapter-stream.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
