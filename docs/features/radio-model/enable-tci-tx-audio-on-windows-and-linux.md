# Enable TCI TX audio on Windows and Linux

TCI TX audio lets applications such as WSJT-X, JTDX, and MSHV send transmit audio to AetherSDR over a WebSocket connection. AetherSDR routes that audio through a dedicated DAX TX stream that is independent of SmartSDR DAX2, so it works on both Windows and Linux without conflicting with other DAX audio devices.

## Before you start

- AetherSDR v0.9.5.1 or later is required.
- The TCI-capable application (e.g. WSJT-X, JTDX, or MSHV) must be configured to use TCI as its audio output.
- On Linux, your build must include PipeWire support (`HAVE_PIPEWIRE`) if you also need hosted DAX for other purposes; TCI TX audio itself has no PipeWire requirement.

## Steps

1. In your TCI-capable application, set the audio output (or sound card / PTT method) to **TCI** and point it at AetherSDR's TCI WebSocket address (e.g. `ws://localhost:50001`).
2. Key the transmitter from the application as normal. AetherSDR automatically opens a DAX TX stream for the TCI audio and routes it to the radio.

No additional settings are required inside AetherSDR. The DAX TX stream is created and torn down automatically each time TCI TX audio is active.

## Tips

- TCI TX audio creates its own DAX TX stream slot. Multiple GUI clients can each register their own stream simultaneously without blocking one another.
- On Windows, SmartSDR DAX2 manages the Windows DAX *audio devices*, but it does not own the radio's DAX TX stream slots. TCI TX audio therefore works alongside SmartSDR DAX2 on the same machine.
- On Linux without PipeWire, hosted DAX is unavailable, but TCI TX audio is unaffected — it does not depend on hosted DAX at all.

## Related

- [DAX audio overview](dax-audio-overview.md)
- [Per-Band TX Settings](per-band-tx-settings.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
