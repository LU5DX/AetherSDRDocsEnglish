# Diagnose DAX TX stream registration issues

Inspect why a DAX TX stream fails to register by examining the policy decision applied to each registration request. The `DaxStreamDebugState` struct captures the reason, platform, mode, and policy outcome so you can identify exactly where registration is blocked.

## Before you start

- Connect AetherSDR to your radio so that stream status messages are being received.
- Know which client feature triggered the registration attempt (TCI TX audio, hosted DAX bridge, external DAX route, or generic audio recreate).

## Steps

1. Open the AetherSDR debug log or stream diagnostics panel and locate the `DaxStreamDebugState` entry for the TX stream in question.
2. Read the `request_reason`, `platform`, `mode`, and `policy_note` fields and match them against the decision table below to determine why registration was allowed or denied.

## What each field reports

| Field | Values | Meaning |
|---|---|---|
| `request_reason` | `hosted_dax_bridge` | Request came from the hosted DAX bridge path. |
| `request_reason` | `tci_tx_audio` | Request came from a TCI client (WSJT-X / JTDX / MSHV). Always allowed regardless of platform. |
| `request_reason` | `external_dax_route_only` | Request is a route-only path; no local stream is created. |
| `request_reason` | `generic_audio_recreate` | Generic audio recreate path; not a DAX TX registration. |
| `platform` | `windows`, `macos`, `linux`, `other` | Operating system detected at build time. |
| `mode` | `none` | DAX TX is not supported on this build. |
| `mode` | `hosted_dax` | macOS or PipeWire Linux build; hosted DAX is active. |
| `mode` | `external_dax2` | Windows build; SmartSDR DAX2 owns the Windows DAX audio devices. |
| `policy_allowed` | `true` / `false` | Whether the policy permitted stream registration. |
| `policy_note` | `hosted_dax_available` | Hosted DAX is present and mode matched; registration allowed. |
| `policy_note` | `SmartSDR_DAX2_owns_windows_dax` | SmartSDR DAX2 owns the Windows DAX audio devices; AetherSDR will not register a competing stream. |
| `policy_note` | `hosted_dax_unavailable` | Build does not include hosted DAX; bridge request denied. |
| `policy_note` | `tci_creates_own_dax_tx_stream` | TCI audio always gets its own `dax_tx` stream slot; registration allowed. |
| `policy_note` | `route_only_does_not_require_local_stream` | External route-only mode needs no local stream; registration skipped. |
| `policy_note` | `generic_audio_recreate_not_dax_tx` | Generic recreate is not a DAX TX path; registration denied. |

## Tips

- On Windows, `SmartSDR_DAX2_owns_windows_dax` is expected behaviour for `hosted_dax_bridge` and `external_dax_route_only` requests — it is not an error.
- TCI TX audio (`tci_tx_audio`) uses the radio's `dax_tx` stream slot directly over the WebSocket connection and is independent of SmartSDR DAX2. If it is denied, check that the radio firmware reports the stream slot as available, not as an orphan (`client_handle=0x00000000`, `ip=0.0.0.0`).
- A stream status entry with `client_handle=0x00000000` and `ip=0.0.0.0` is a dead orphan left by a previous disconnected client; AetherSDR will not claim it as its own.

## Related

- [dax-rx-stream-troubleshooting.md](dax-rx-stream-troubleshooting.md)
- [stream-status-ownership.md](stream-status-ownership.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
