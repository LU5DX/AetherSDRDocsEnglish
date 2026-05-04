# Fix TCI TX audio silent on Windows or Linux non-PipeWire

`PanadapterStream::sendToRadio` transmits raw VITA-49 UDP datagrams to the radio, including DAX TX audio packets sourced from TCI clients such as WSJT-X, JTDX, and MSHV. On Windows and Linux systems without PipeWire, a policy gate previously blocked TCI from opening its own DAX TX stream, causing transmitted audio to be silent.

## Before you start

- Update to AetherSDR v0.9.5.1 or later. This release contains the `DaxTxPolicy` fix (issue #2276) that allows TCI TX audio to create its own DAX TX stream regardless of platform.
- Confirm your TCI client (WSJT-X, JTDX, or MSHV) is connected to AetherSDR over the WebSocket interface before transmitting.

## Steps

1. Upgrade AetherSDR to v0.9.5.1 or later — no configuration change is required. The fix is applied automatically at startup.
2. Verify that your TCI client's audio is routing through the WebSocket connection (not a local audio device). TCI TX audio uses the WebSocket stream, not the system DAX audio devices managed by SmartSDR DAX2.

## What each control does

| Component | Behavior |
|---|---|
| `PanadapterStream::sendToRadio` | Sends a VITA-49 UDP datagram to the radio. For TCI TX audio, the datagram is sourced from the TCI WebSocket client and delivered through a dedicated `dax_tx` stream slot registered by AetherSDR, independent of SmartSDR DAX2's audio devices. |
| DAX TX stream (TCI path) | AetherSDR registers its own `dax_tx` stream slot on the radio. Multiple GUI clients can each hold a slot simultaneously, so TCI's stream does not conflict with SmartSDR DAX2. |
| `DaxTxPolicy` (v0.9.5.1) | Evaluates whether a given caller is permitted to open a DAX TX stream. For TCI TX audio the policy always returns `allowed = true` regardless of platform or whether hosted DAX (PipeWire / macOS) is available. |

## Tips

- If audio is still silent after upgrading, confirm the TCI client is transmitting on the correct frequency slice and that PTT is being asserted through the TCI interface, not a separate CAT/serial path that may not gate the DAX TX stream.
- On Linux without PipeWire, SmartSDR DAX2 audio *devices* are unavailable, but TCI TX audio is unaffected because it never relied on them.
- On Windows, SmartSDR DAX2 owns the Windows DAX audio devices; TCI TX audio bypasses those entirely and communicates directly with the radio's `dax_tx` stream slot.

## Related

- [tci-setup.md](tci-setup.md)
- [dax-tx-audio.md](dax-tx-audio.md)
- [pipewire-linux-audio.md](pipewire-linux-audio.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
