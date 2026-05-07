# Enable TCI digital-mode transmit on Linux without PipeWire

TCI digital-mode transmit feeds audio over WebSocket into a dedicated `dax_tx` stream that is independent of SmartSDR DAX2, so it works on Linux systems that do not have PipeWire — no hosted-DAX bridge is required.

## Before you start

- AetherSDR V0.9.7 or later installed on Linux.
- A TCI-compatible digital-mode application (for example, WSJT-X, JS8Call, or fldigi) configured to use TCI audio output.
- A radio connection already established in AetherSDR.

## Steps

1. In your digital-mode application, select TCI as the audio output (transmit) device and point it at AetherSDR's TCI endpoint (default `ws://localhost:50001`).
2. Key the transmitter from your digital-mode application. AetherSDR receives the audio over the WebSocket connection and routes it through the `dax_tx` stream automatically — no additional configuration in AetherSDR is needed.

## What each control does

| Control | Behavior |
|---|---|
| TCI audio transmit | Always permitted on every platform. Audio arrives over WebSocket and is written directly into the `dax_tx` stream, bypassing SmartSDR DAX2 entirely. |
| Hosted-DAX bridge | Available on macOS and PipeWire Linux only. Blocked on Windows (SmartSDR DAX2 owns the audio devices) and on non-PipeWire Linux. |

## Tips

- If your digital-mode application offers both TCI and ALSA/PulseAudio output options, choose TCI. ALSA and PulseAudio paths require a hosted-DAX bridge, which is unavailable on non-PipeWire Linux.
- Verify the TCI port in AetherSDR under **Settings > TCI** if the default port `50001` is already in use on your system.

## Related

- [DAX audio overview](dax-audio-overview.md)
- [Connect a TCI client](connect-tci-client.md)
- [Enable hosted-DAX bridge on PipeWire Linux](hosted-dax-pipewire-linux.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
