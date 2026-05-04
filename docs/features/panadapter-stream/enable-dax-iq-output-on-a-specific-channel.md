# Enable DAX IQ output on a specific channel

`PanadapterStream::registerIqStream` routes incoming DAX IQ baseband samples for a specific IQ channel to the correct consumer by registering the radio's stream ID with a channel number.

## Before you start

- A radio connection must be active before registering an IQ stream.
- The target DAX IQ channel number must be known in advance.

## Steps

1. Establish a connection to the radio so that a valid stream ID is available.
2. Call `registerIqStream` with the stream ID returned by the radio and the DAX IQ channel number you want to receive output on.

## What each control does

| Control | Behavior |
|---|---|
| Stream ID | Identifies the radio's VITA-49 data stream. Passed to `registerIqStream` to associate incoming packets with the correct source. |
| IQ Channel Number | Selects which DAX IQ channel receives the routed baseband samples. Must match the channel configured on the radio. |

## Tips

- Each DAX IQ channel requires its own `registerIqStream` call. Registering a new stream ID on a channel that is already registered replaces the previous mapping.

## Related

- [Start a panadapter stream](panadapter-stream-start.md)
- [DAX IQ channel overview](dax-iq-overview.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
