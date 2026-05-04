# Understand why generic audio-recreate requests do not open a DAX TX stream

The DAX TX Platform Policy (`DaxTxPolicy`) controls whether a DAX TX audio stream is opened, based on the reason for the request and the current platform. Generic audio-recreate requests are unconditionally blocked — no DAX TX stream is ever opened for them, regardless of platform.

## Before you start

- Confirm you are working with AetherSDR v0.9.5.1 or later, which introduces `DaxTxPolicy`.
- Understand the four request reasons the policy evaluates: TCI TX audio, hosted DAX bridge, external DAX route, and generic audio recreate.

## Steps

1. When your code or workflow triggers an audio-recreate event (for example, an audio device change or session restart), check the request reason passed to `DaxTxPolicy`. If the reason is `GenericAudioRecreate`, the policy returns `DaxTxMode::None` — no stream is opened.
2. To open a DAX TX stream, use one of the three permitted request reasons instead:
   - `TciTxAudio` — always allowed on every platform; feeds audio over WebSocket into a dedicated `dax_tx` stream independent of SmartSDR DAX2.
   - `HostedDaxBridge` — allowed on macOS and PipeWire Linux only; blocked on Windows where SmartSDR DAX2 owns the audio devices.
   - `ExternalDaxRouteOnly` — allowed for external DAX routing scenarios.

## What each control does

| Request Reason | Resulting DAX TX Mode | Platforms allowed |
|---|---|---|
| `TciTxAudio` | `ExternalDax2` (dedicated `dax_tx` stream) | All platforms |
| `HostedDaxBridge` | `HostedDax` | macOS, PipeWire Linux only |
| `ExternalDaxRouteOnly` | `ExternalDax2` | Platform-dependent |
| `GenericAudioRecreate` | `None` — stream not opened | None |

## Tips

- A generic audio-recreate request is intentionally excluded because it represents an audio subsystem restart, not a deliberate transmit request. Granting a DAX TX stream in this case could cause unintended transmissions during device reconnection or session recovery.
- On Windows, `HostedDaxBridge` is also blocked because SmartSDR DAX2 owns the audio devices. If you need DAX TX on Windows, use `TciTxAudio` instead.

## Related

- [DAX TX overview](dax-tx-overview.md)
- [TCI audio transmit](tci-audio-transmit.md)
- [Hosted DAX bridge](hosted-dax-bridge.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
