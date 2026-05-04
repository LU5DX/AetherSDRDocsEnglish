# Understand DAX TX stream slots vs SmartSDR DAX2 audio devices

AetherSDR applies a platform-aware policy to decide whether a DAX TX audio stream may be opened. The rules differ depending on why the stream is being requested and which operating system you are running on.

## How the policy works

Each request to open a DAX TX stream carries one of four reasons. The policy evaluates the reason together with the current platform and either grants or blocks the stream.

| Request reason | Windows | macOS | Linux (PipeWire) | Notes |
|---|---|---|---|---|
| **TCI TX audio** | Allowed | Allowed | Allowed | TCI feeds audio over WebSocket into a dedicated `dax_tx` stream. This path is independent of SmartSDR DAX2 and is always available. |
| **Hosted DAX bridge** | **Blocked** | Allowed | Allowed | On Windows, SmartSDR DAX2 owns the audio devices. The hosted DAX bridge is therefore unavailable on that platform. |
| **External DAX route only** | Allowed | Allowed | Allowed | Routes audio through an external DAX path without requiring the hosted bridge. |
| **Generic audio recreate** | **Blocked** | **Blocked** | **Blocked** | A generic audio-recreate request is never granted a DAX TX stream on any platform. |

## What this means in practice

- **TCI digital-mode transmit** always works regardless of platform. Configure your TCI source and transmit normally; the `dax_tx` stream opens automatically.
- **Windows users** cannot use the hosted DAX bridge because SmartSDR DAX2 holds exclusive access to the DAX audio devices. Use TCI TX audio or an external DAX route instead.
- **macOS and PipeWire Linux users** can use the hosted DAX bridge in addition to TCI and external DAX routes.
- **Generic audio recreate** should not be used as a mechanism to reopen a DAX TX stream. If a stream needs to be recovered, trigger a new TCI or DAX-route request instead.

## Tips

- If your DAX TX stream fails to open on Windows, check whether SmartSDR DAX2 is running and holding the audio device. Switch to a TCI-based TX audio path if you need to transmit without SmartSDR.
- On macOS or PipeWire Linux, the hosted DAX bridge and external DAX route can coexist; only one DAX TX slot is active at a time, so avoid opening both simultaneously.
- TCI TX audio operates independently of the system audio device stack, making it the most portable option across all platforms.

## Related

- [dax-audio-overview.md](dax-audio-overview.md)
- [tci-transmit-audio.md](tci-transmit-audio.md)
- [smartsdr-dax2-compatibility.md](smartsdr-dax2-compatibility.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
