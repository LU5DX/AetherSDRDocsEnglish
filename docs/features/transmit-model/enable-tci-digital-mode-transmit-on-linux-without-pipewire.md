# Enable TCI digital-mode transmit on Linux without PipeWire

TCI digital-mode transmit feeds audio over WebSocket into a dedicated `dax_tx` stream, independent of SmartSDR DAX2. This path is always available on Linux regardless of whether PipeWire is installed.

## Before you start

- AetherSDR v0.9.5.1 or later installed on Linux.
- A TCI-capable digital-mode application (for example, WSJT-X, JS8Call, or fldigi) configured to use TCI audio output.
- A radio profile already connected in AetherSDR.

## Steps

1. In your digital-mode application, set the audio output to **TCI** mode. The application sends audio over the WebSocket TCI connection — no ALSA or PipeWire device selection is required.
2. Key the transmitter from your digital-mode application. AetherSDR routes the incoming TCI audio directly into the `dax_tx` stream and begins transmitting.

## What each control does

| Control | Behavior |
|---|---|
| TCI audio output (in digital-mode app) | Sends encoded audio frames over the WebSocket TCI connection to AetherSDR. No local audio device is used. |
| `dax_tx` stream | Receives TCI audio and passes it to the transmit chain. Opened automatically when a TCI transmit request arrives; does not depend on SmartSDR DAX2 or PipeWire. |
| Hosted-DAX bridge | Not available on Linux without PipeWire. Requests of this type are blocked; use TCI audio output instead. |

## Tips

- Because TCI transmit bypasses the system audio stack entirely, you do not need to configure ALSA, PulseAudio, or PipeWire for the digital-mode application. If your application offers both a TCI option and a system-audio option, always choose TCI on Linux for the most reliable path.
- The TX EQ and TX FFT analyzer in AetherSDR remain active during TCI transmit. The analyzer taps the audio signal whether or not the EQ stage is enabled, so you can monitor the transmitted waveform in real time.
- Hosted-DAX bridge mode is only supported on macOS and PipeWire-enabled Linux. On plain ALSA Linux systems, TCI is the only supported DAX TX path.

## Related

- [DAX TX Platform Policy](dax-tx-policy.md)
- [TCI overview](tci-overview.md)
- [Connect a digital-mode application via TCI](connect-digital-mode-tci.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
