# Fix TCI TX audio silent on Windows or Linux non-PipeWire

AetherSDR uses `PanadapterStream::sendToRadio` to transmit raw VITA-49 UDP datagrams directly to the radio. On Windows and non-PipeWire Linux systems, a DAX TX policy check previously blocked TCI TX audio streams from registering their own DAX TX slot, causing silence during transmission.

## Before you start

- Update AetherSDR to v0.9.7 or later. This release contains the policy fix; no manual workaround is available in earlier versions.
- Confirm your radio is reachable and the panadapter stream is connected before testing audio.

## Steps

1. Update AetherSDR to v0.9.7 or later using your normal installation method.
2. Restart AetherSDR so the updated DAX TX policy takes effect.
3. Start a TCI TX audio session as you normally would. The stream now registers its own DAX TX slot regardless of platform or whether SmartSDR DAX2 owns the Windows audio device layer.

## What changed

| Area | Behavior before v0.9.7 | Behavior from v0.9.7 |
|---|---|---|
| TCI TX audio DAX policy | Policy evaluation could block TCI TX stream registration on Windows or non-PipeWire Linux | Policy always allows TCI TX audio to create its own DAX TX stream, independent of platform and hosted-DAX availability |
| VITA-49 UDP delivery | Not affected | VITA-49 datagrams are sent directly to the radio; no Windows audio device involvement |
| TX byte counters | Non-atomic integer increments | Atomic `fetch_add` operations; no user-visible change |

## Tips

- If TX audio is still silent after updating, verify that your TCI client is actually sending audio data and that the radio's DAX TX channel is not held exclusively by another application such as SmartSDR DAX2.
- Check the AetherSDR debug log for entries containing `tci_creates_own_dax_tx_stream` to confirm the correct policy decision is being applied.

## Related

- [dax-tx-configuration.md](dax-tx-configuration.md)
- [tci-audio-setup.md](tci-audio-setup.md)
- [panadapter-stream.md](panadapter-stream.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
