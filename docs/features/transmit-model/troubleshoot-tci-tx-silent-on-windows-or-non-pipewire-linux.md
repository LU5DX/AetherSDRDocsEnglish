# Troubleshoot TCI TX silent on Windows or non-PipeWire Linux

AetherSDR routes TCI digital-mode transmit audio over a WebSocket into a dedicated `dax_tx` stream, separate from SmartSDR DAX2. On Windows, SmartSDR DAX2 owns the audio devices, so hosted-DAX bridge requests are blocked; on Linux without PipeWire, the same restriction applies. If your TCI TX is silent, the steps below identify which request type is being used and whether the platform policy is the cause.

## Before you start

- Confirm you are running AetherSDR v0.9.5.1 or later.
- Know which transmit path you are using: TCI audio (WebSocket), hosted-DAX bridge, or an external DAX route.

## Steps

1. Verify that your transmit path is **TCI TX audio**, not a hosted-DAX bridge request. TCI audio is always permitted on every platform — if you are using the TCI path and still hear silence, the problem is not the platform policy; check your WebSocket connection and audio device selection instead.
2. If you are using a hosted-DAX bridge path on Windows or non-PipeWire Linux, the stream will be blocked by design. Switch to the TCI audio path or move to a supported platform (macOS or PipeWire Linux) to use hosted-DAX bridge.
3. If you are using a **generic audio-recreate** request, be aware that this request type is never granted a DAX TX stream on any platform. Change the request reason to `TciTxAudio` or `ExternalDaxRouteOnly` in your integration.

## What each control does

| Request type | Behavior |
|---|---|
| TCI TX audio | Always allowed on every platform. Audio is fed over WebSocket into the dedicated `dax_tx` stream, independent of SmartSDR DAX2. |
| Hosted-DAX bridge | Allowed only on macOS and PipeWire Linux. Blocked on Windows (SmartSDR DAX2 owns the audio devices) and non-PipeWire Linux. |
| External DAX route | Allowed as an external route; does not depend on hosted-DAX availability. |
| Generic audio-recreate | Never granted a DAX TX stream on any platform. |

## Tips

- On Windows, SmartSDR DAX2 exclusively owns the audio devices. Do not attempt to open a hosted-DAX bridge stream from AetherSDR on the same machine — use the TCI audio path instead.
- On Linux, check whether PipeWire is running (`pactl info | grep "Server Name"`) before assuming hosted-DAX bridge will work. If PulseAudio or ALSA is reported instead, the hosted-DAX bridge path will be blocked.

## Related

- [DAX audio routing overview](dax-audio-routing.md)
- [Configure TCI TX audio](configure-tci-tx-audio.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
