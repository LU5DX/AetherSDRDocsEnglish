# Diagnose DAX transmit packet delivery issues

`PanadapterStream::sendToRadio` transmits raw VITA-49 UDP datagrams to the radio, delivering DAX TX audio packets from the client for over-the-air transmission. Use this guide when packets are not reaching the radio or DAX TX audio is silently dropped.

## Before you start

- Confirm the radio is connected and the DAX TX channel is assigned.
- Know which request path is in use: Hosted DAX bridge, TCI TX audio, External DAX route-only, or Generic audio recreate.
- Note your operating system — DAX TX mode is determined at build time per platform (Windows uses External DAX2; macOS and Linux with PipeWire use Hosted DAX; all others have no DAX TX mode).

## Steps

1. Identify the **request reason** that applies to your workflow:

   | Reason | String reported in logs |
   |---|---|
   | Hosted DAX bridge | `hosted_dax_bridge` |
   | TCI TX audio (WSJT-X / JTDX / MSHV) | `tci_tx_audio` |
   | External DAX route-only | `external_dax_route_only` |
   | Generic audio recreate | `generic_audio_recreate` |

2. Check the policy decision the SDK logged for that reason against the table below to confirm whether transmission was allowed and why it was blocked if not.

## What each policy decision means

| Request reason | Allowed? | Note in logs | What to do |
|---|---|---|---|
| `hosted_dax_bridge` | Yes | `hosted_dax_available` | Hosted DAX is active — no action needed. |
| `hosted_dax_bridge` | No | `SmartSDR_DAX2_owns_windows_dax` | On Windows, SmartSDR DAX2 owns the DAX audio devices. Use SmartSDR DAX2 instead of the hosted bridge. |
| `hosted_dax_bridge` | No | `hosted_dax_unavailable` | The current build does not include Hosted DAX support. Switch to an External DAX2 or TCI path. |
| `tci_tx_audio` | Yes | `tci_creates_own_dax_tx_stream` | TCI opens its own `dax_tx` stream slot independent of platform DAX mode. Always allowed — check your WebSocket source (WSJT-X, JTDX, MSHV) if audio is still missing. |
| `external_dax_route_only` | No | `SmartSDR_DAX2_owns_windows_dax` | Route-only mode on Windows is blocked because SmartSDR DAX2 controls the audio devices. No local stream is created. |
| `external_dax_route_only` | No | `route_only_does_not_require_local_stream` | Expected behavior — a route-only request deliberately skips local stream creation. |
| `generic_audio_recreate` | No | `generic_audio_recreate_not_dax_tx` | A generic audio-recreate request is not a DAX TX operation. Use an explicit DAX TX request reason instead. |

## Tips

- TCI TX audio (`tci_tx_audio`) is always allowed regardless of platform or Hosted DAX availability. If TCI audio is not reaching the radio, the problem is upstream — verify the WebSocket connection from your digital-modes application.
- On Windows, SmartSDR DAX2 exclusively owns the DAX audio device layer. Do not attempt to run a Hosted DAX bridge or External DAX route-only path alongside it.
- Multiple GUI clients can each register their own `dax_tx` stream slot on the radio simultaneously; stream-slot conflicts are not the cause of a policy denial.
- If you see `unknown_reason` in the logs, the request reason value is unrecognized — check that your client is compiled against the current SDK headers.

## Related

- [dax-tx-overview.md](dax-tx-overview.md)
- [tci-audio-setup.md](tci-audio-setup.md)
- [panadapter-stream-reference.md](panadapter-stream-reference.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
