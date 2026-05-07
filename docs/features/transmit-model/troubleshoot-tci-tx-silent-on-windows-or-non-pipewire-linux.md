# Troubleshoot TCI TX silent on Windows or non-PipeWire Linux

AetherSDR's DAX TX Platform Policy controls which audio paths are permitted to open a DAX TX stream. TCI digital-mode transmit is always allowed on every platform and feeds audio over WebSocket into a dedicated `dax_tx` stream, independent of SmartSDR DAX2. Hosted-DAX bridge requests, however, are blocked on Windows and on Linux systems without PipeWire, because SmartSDR DAX2 owns the audio devices on those platforms.

## Before you start

- Confirm you are running AetherSDR v0.9.7 or later.
- Know which TX audio path you are using: TCI digital mode or hosted-DAX bridge.
- On Linux, know whether your system uses PipeWire (`pactl info | grep "Server Name"` should show `PulseAudio (on PipeWire)`).

## Steps

1. **Confirm your TX source is TCI, not hosted-DAX bridge.** In AetherSDR, verify that the transmit audio source is set to TCI digital mode. Hosted-DAX bridge is not available on Windows or non-PipeWire Linux — only TCI is permitted on those platforms. If you have selected a hosted-DAX bridge source, the stream will be silently blocked.

2. **If you need hosted-DAX bridge, switch to a supported platform.** Move your AetherSDR session to macOS or a PipeWire-enabled Linux system. On Windows, use TCI audio exclusively and let SmartSDR DAX2 manage the audio devices independently.

## What each control does

| Control | Behavior |
|---|---|
| TCI digital-mode TX | Always permitted on all platforms. Sends audio over WebSocket into the dedicated `dax_tx` stream. Does not interact with SmartSDR DAX2 audio devices. |
| Hosted-DAX bridge | Permitted only on macOS and PipeWire Linux. Blocked on Windows and non-PipeWire Linux because SmartSDR DAX2 owns the audio devices on those platforms. |
| External DAX route | Subject to the same platform policy as hosted-DAX bridge. |

## Tips

- On Windows, SmartSDR DAX2 and AetherSDR TCI TX can operate at the same time without conflict — TCI audio bypasses the DAX2 audio device layer entirely.
- If you are unsure whether your Linux system uses PipeWire, run `pactl info` in a terminal and look for `PipeWire` in the `Server Name` line. If it is absent, hosted-DAX bridge will be blocked.
- Switching from hosted-DAX bridge to TCI digital mode requires no hardware changes — TCI feeds audio over the existing WebSocket connection.

## Related

- [DAX TX Audio Setup](dax-tx-audio-setup.md)
- [TCI Digital Mode Overview](tci-digital-mode-overview.md)
- [Hosted-DAX Bridge Configuration](hosted-dax-bridge-configuration.md)
- [Platform Requirements](platform-requirements.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
