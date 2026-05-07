# Understand DAX TX stream slots vs SmartSDR DAX2 audio devices

AetherSDR separates DAX TX audio into distinct stream slots depending on the source of the request. Whether a slot can be opened depends on the current platform and who owns the audio devices.

## How DAX TX stream slots work

AetherSDR recognises three reasons a DAX TX stream may be requested:

| Request source | What it does | Platform restriction |
|---|---|---|
| TCI digital-mode transmit | Feeds audio over WebSocket into a dedicated `dax_tx` stream. Always allowed on every platform. | None — works on Windows, macOS, and Linux. |
| Hosted-DAX bridge | Opens a DAX TX stream via the internal hosted-DAX bridge (used when AetherSDR manages audio devices directly). | macOS and PipeWire Linux only. |
| External DAX route | Routes audio from an externally configured DAX path into a TX stream. | macOS and PipeWire Linux only. |

## Why hosted-DAX TX is blocked on Windows

On Windows, SmartSDR DAX2 installs virtual audio devices and holds exclusive ownership of the DAX audio pipeline. AetherSDR cannot open a hosted-DAX bridge TX stream on the same machine without conflicting with those devices. The `DaxTxPolicy` module enforces this restriction automatically — no configuration is required.

TCI transmit is not affected. Because TCI audio travels over a WebSocket connection into a separate `dax_tx` stream, it bypasses the SmartSDR DAX2 device layer entirely and works on all platforms.

## Steps

1. If you are on Windows and need to transmit audio through DAX, use TCI digital-mode transmit. Configure your software to send audio via the TCI interface rather than a virtual audio device.
2. If you are on macOS or Linux (PipeWire), you may use the hosted-DAX bridge or an external DAX route in addition to TCI. No extra steps are needed — the policy allows those requests automatically on supported platforms.

## Tips

- If a DAX TX stream fails to open on Windows, confirm that SmartSDR DAX2 is installed and running. AetherSDR intentionally blocks hosted-DAX TX on that platform to avoid device conflicts.
- TCI transmit is the recommended path for digital modes on all platforms because it is platform-independent and does not depend on virtual audio device availability.

## Related

- [Configure TCI digital-mode transmit](configure-tci-digital-mode-transmit.md)
- [DAX audio routing overview](dax-audio-routing-overview.md)
- [Hosted-DAX bridge setup (macOS and Linux)](hosted-dax-bridge-setup.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
