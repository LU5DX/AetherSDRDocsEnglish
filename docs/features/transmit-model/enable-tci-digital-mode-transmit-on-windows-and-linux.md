# Enable TCI digital-mode transmit on Windows and Linux

AetherSDR routes TCI digital-mode transmit audio over a WebSocket connection into a dedicated `dax_tx` stream, independent of SmartSDR DAX2. This path is available on every platform, including Windows and Linux, where SmartSDR DAX2 would otherwise own the audio devices.

## Before you start

- Confirm your radio is connected and the TCI server is running in AetherSDR.
- Ensure your digital-mode application (e.g., WSJT-X, fldigi) is configured to use the TCI audio interface.

## Steps

1. In your digital-mode application, select the AetherSDR TCI audio device as the transmit audio output. AetherSDR automatically opens a `dax_tx` stream when it detects a TCI TX audio request — no additional configuration is required inside AetherSDR.
2. Key the transmitter from your digital-mode application as normal. Audio flows over the TCI WebSocket connection into the `dax_tx` stream and bypasses SmartSDR DAX2 entirely.

## What each control does

| Component | Behavior |
|---|---|
| TCI TX audio path | Feeds transmit audio over WebSocket into a dedicated `dax_tx` stream. Always permitted on Windows, Linux, and all other platforms. |
| SmartSDR DAX2 | Owns the Windows audio devices for other DAX stream types. The TCI TX path does not interact with it and is not blocked by it. |
| Hosted-DAX bridge | Available on macOS and PipeWire Linux only. Blocked on Windows because SmartSDR DAX2 owns the audio devices there. |
| Generic audio recreate | Never granted a DAX TX stream on any platform. |

## Tips

- Because the TCI TX path is independent of SmartSDR DAX2, you do not need to install or configure DAX2 drivers on Windows to use digital-mode transmit.
- On Linux, if you also need hosted-DAX bridge functionality (for non-TCI applications), use a PipeWire audio system; ALSA-only setups are treated the same as Windows and the bridge will be blocked.

## Related

- [DAX audio routing overview](dax-audio-routing.md)
- [TCI server configuration](tci-server-configuration.md)
- [Digital-mode setup](digital-mode-setup.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
