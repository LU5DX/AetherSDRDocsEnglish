# Enable TCI digital-mode transmit on Windows and Linux

TCI digital-mode transmit lets you feed audio from a TCI client into a dedicated `dax_tx` stream over WebSocket, independently of SmartSDR DAX2. This path is available on every platform, including Windows, where SmartSDR DAX2 owns the system audio devices.

## Before you start

- Your TCI client must support TCI audio output.
- AetherSDR must be connected to your radio.

## Steps

1. In your TCI client, enable audio output and point it at the AetherSDR TCI endpoint (host and port shown in AetherSDR's TCI settings panel).
2. Key the transmitter from your TCI client. AetherSDR opens a `dax_tx` stream automatically and routes the incoming WebSocket audio to the radio — no additional DAX configuration is required.

## What each control does

| Control | Behavior |
|---|---|
| TCI audio output (TCI client) | Streams audio over WebSocket to AetherSDR. AetherSDR accepts this on all platforms (Windows, Linux, macOS). |
| `dax_tx` stream | Dedicated transmit audio stream opened by AetherSDR when a TCI audio request arrives. Separate from SmartSDR DAX2 — does not conflict with DAX2 device ownership on Windows. |

## Tips

- On Windows, only TCI digital-mode transmit is available for DAX TX. Hosted-DAX bridge requests are blocked because SmartSDR DAX2 owns the audio devices. Use TCI audio output from your logging or digital-mode application instead.
- On macOS and PipeWire Linux, hosted-DAX bridge is also available as an alternative path if your application does not support TCI.

## Related

- [DAX TX overview](dax-tx-overview.md)
- [TCI connection setup](tci-connection-setup.md)
- [Hosted DAX bridge (macOS and Linux)](hosted-dax-bridge.md)
<!-- docmesh:llm version=v0.9.5.1 date=2026-05-04 -->
