# Enable TCI digital-mode transmit on Windows and Linux

TCI digital-mode transmit lets you feed audio into a dedicated `dax_tx` stream over WebSocket, bypassing SmartSDR DAX2 entirely. This works on Windows and Linux (including PipeWire Linux) because TCI does not touch the platform audio devices that SmartSDR DAX2 owns.

## Before you start

- AetherSDR V0.9.7 or later installed.
- A TCI-compatible digital-mode application (e.g. WSJT-X, JS8Call) configured to use TCI audio output.
- A radio connection already established in AetherSDR.

## Steps

1. In your digital-mode application, set the audio output to **TCI** mode and point it at the AetherSDR WebSocket address (default `ws://localhost:50001`).
2. Key the transmitter from your digital-mode application. AetherSDR automatically opens a `dax_tx` stream to accept the incoming audio — no additional configuration is required in AetherSDR.

## What each control does

| Control | Behavior |
|---|---|
| TCI audio request | Always allowed on every platform. AetherSDR opens a `dax_tx` WebSocket stream to receive the audio and routes it to the transmitter independently of SmartSDR DAX2. |
| Hosted-DAX bridge request | Allowed only on macOS and PipeWire Linux. Blocked on Windows because SmartSDR DAX2 owns the audio devices on that platform. |
| External DAX route request | Subject to the same platform policy as hosted-DAX bridge requests. |

## Tips

- If you are on Windows and also use SmartSDR DAX2 for other audio routing, TCI transmit will not conflict with it — they operate on separate paths.
- On Linux, if you need hosted-DAX bridge functionality in addition to TCI transmit, ensure PipeWire is running before starting AetherSDR.

## Related

- [dax-tx-stream.md](dax-tx-stream.md)
- [tci-connection.md](tci-connection.md)
- [platform-audio-policy.md](platform-audio-policy.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
