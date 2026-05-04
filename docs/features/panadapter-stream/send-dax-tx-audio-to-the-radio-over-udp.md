# Send DAX TX audio to the radio over UDP

`PanadapterStream::sendToRadio` transmits a raw VITA-49 UDP datagram to the radio. Use this when you need to send DAX TX audio packets from the client to the radio for transmission.

## Before you start

- Confirm the radio is connected and a DAX TX stream has been registered for your client session.
- Identify which DAX TX mode applies to your platform:
  - **Windows** — uses External DAX 2 (SmartSDR DAX2 owns the Windows DAX audio devices; TCI TX audio sources create their own independent `dax_tx` stream slot and are always allowed).
  - **macOS / Linux with PipeWire** — uses Hosted DAX.
  - **Other platforms** — DAX TX is not available.

## Steps

1. Build a valid VITA-49 packet containing the PCM audio payload you want to transmit.
2. Call `PanadapterStream::sendToRadio`, passing the raw datagram bytes. The method sends the packet to the radio over UDP on the bound local address.

## What each control does

| Control | Behavior |
|---|---|
| `sendToRadio(datagram)` | Writes the supplied raw VITA-49 UDP datagram directly to the radio's DAX TX stream endpoint. Returns immediately after the socket write is queued. |

## Tips

- TCI TX audio (e.g. from WSJT-X, JTDX, or MSHV) feeds packets into a dedicated `dax_tx` stream that is independent of SmartSDR DAX2. This path is always permitted regardless of platform or Hosted DAX availability.
- On Windows, only the TCI TX audio path is allowed. Do not attempt to route a Hosted DAX bridge or an External DAX route-only stream — both are blocked because SmartSDR DAX2 owns the Windows DAX audio devices.
- Each GUI client can register its own `dax_tx` stream slot; multiple clients are not limited to a single shared slot.

## Related

- [DAX overview](dax-overview.md)
- [Connect to a radio](connect-to-radio.md)
- [TCI TX audio](tci-tx-audio.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
