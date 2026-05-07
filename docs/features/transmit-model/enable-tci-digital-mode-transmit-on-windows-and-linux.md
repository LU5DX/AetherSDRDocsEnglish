# Enable TCI digital-mode transmit on Windows and Linux

TCI digital-mode transmit feeds audio over a WebSocket connection into a dedicated `dax_tx` stream, bypassing SmartSDR DAX2 entirely. This means TCI TX is available on Windows and Linux without any additional audio device configuration.

## Before you start

- AetherSDR V0.9.7 or later must be installed.
- A TCI-compatible digital-mode application (e.g. WSJT-X, fldigi) must be installed and configured to use TCI audio output.
- The radio must be connected and the RX stream must be running before transmitting.

## Steps

1. In your digital-mode application, select **TCI** as the audio output (transmit) device or protocol. The application sends audio over the WebSocket connection AetherSDR already has open.
2. Key the transmitter from your digital-mode application as normal. AetherSDR routes the incoming TCI audio directly into the `dax_tx` stream — no additional steps are required on Windows or Linux.

## What each control does

| Control | Behavior |
|---|---|
| TCI audio (transmit) | Always permitted on every platform. Audio arrives over the existing WebSocket connection and is written into a dedicated `dax_tx` stream independent of SmartSDR DAX2. |
| Hosted-DAX bridge | Available on macOS and PipeWire Linux only. Blocked on Windows because SmartSDR DAX2 owns the audio devices on that platform. |
| External DAX route | Subject to platform policy in the same way as the hosted-DAX bridge. |

## Tips

- Because TCI TX does not use SmartSDR DAX2, you do not need to install or configure DAX audio drivers on Windows or Linux for digital-mode transmit.
- If your digital-mode application offers both a TCI mode and a virtual audio cable mode, prefer TCI on Windows to avoid conflicts with SmartSDR DAX2.

## Related

- [DAX TX audio routing](dax-tx-audio-routing.md)
- [Connect a TCI client](connect-tci-client.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
