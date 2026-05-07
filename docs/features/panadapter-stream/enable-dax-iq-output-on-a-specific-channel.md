# Enable DAX IQ output on a specific channel

`PanadapterStream::registerIqStream` routes incoming DAX IQ baseband samples for a specific IQ channel to the correct consumer by registering the radio's stream ID with a channel number.

## Before you start

- A radio connection must be active before registering an IQ stream.
- Know the stream ID provided by the radio and the DAX IQ channel number you want to target.

## Steps

1. Obtain the stream ID assigned by the radio for the DAX IQ output you want to use.
2. Call `registerIqStream(streamId, channel)`, passing the radio-assigned stream ID and the target DAX IQ channel number.

## What each control does

| Parameter | Behavior |
|-----------|----------|
| `streamId` | The radio-assigned stream ID that identifies the incoming DAX IQ data flow. |
| `channel` | The DAX IQ channel number that will receive the baseband samples from the given stream. |

## Tips

- Each channel number must map to exactly one stream ID. Registering the same channel again with a different stream ID overwrites the previous mapping.
- If you are unsure of the stream ID, check the radio's DAX IQ configuration response before calling this method.

## Related

- [PanadapterStream overview](panadapter-stream.md)
- [Enable DAX audio output on a specific channel](enable-dax-audio-channel.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
