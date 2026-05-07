# Diagnose DAX TX stream registration issues

`DaxStreamDebugState` exposes the internal reason and policy decision used when AetherSDR attempts to register a DAX TX stream. Use it to determine why a stream registration succeeded, was skipped, or was blocked.

## Before you start

- Connect to a radio and ensure at least one TX-capable slice is active.
- Enable developer/debug logging if your build supports it, so `DaxStreamDebugState` output is visible in the log view.

## Steps

1. Trigger the DAX TX path by activating the feature that should register the stream (e.g. start TCI TX audio, enable the RADE modem, or open the hosted DAX bridge).
2. Check the logged `DaxStreamDebugState` output. Locate the `reason` field and the `decision` field. Match them against the table below to confirm whether registration was expected to succeed or be skipped.

## What each request reason means

| Reason token | When it appears | Expected decision |
|---|---|---|
| `hosted_dax_bridge` | Hosted DAX bridge is requesting the TX stream | Allowed (`hosted_dax_available`) if hosted DAX mode is active and available; blocked (`SmartSDR_DAX2_owns_windows_dax`) if SmartSDR DAX2 owns the audio layer; otherwise blocked (`hosted_dax_unavailable`) |
| `tci_tx_audio` | TCI subsystem is routing TX audio | Always allowed (`tci_creates_own_dax_tx_stream`); SmartSDR DAX2 ownership is irrelevant |
| `rade_modem_tx` | RADE modem is sending VITA-49 packets directly via `sendModemTxAudio()` | Always allowed (`rade_sends_vita49_directly`); does not use Windows audio devices, so DAX2 ownership is irrelevant |
| `external_dax_route_only` | An external DAX route is configured but no local stream is needed | Blocked (`SmartSDR_DAX2_owns_windows_dax`) if DAX2 mode is active; otherwise skipped (`route_only_does_not_require_local_stream`) |
| `generic_audio_recreate` | Audio engine is recreating streams after a settings change | Follows standard policy re-evaluation |

## Tips

- If you see `SmartSDR_DAX2_owns_windows_dax` for a `rade_modem_tx` request, the policy logic is not reaching the RADE case — check that the request reason is being set to `RadeModemTx` and not falling back to `HostedDaxBridge`.
- `tci_tx_audio` and `rade_modem_tx` bypass Windows audio device ownership checks entirely. If registration still fails for those reasons, the problem is not DAX policy — check VITA-49 stream slot availability on the radio.
- The decision string is logged verbatim; search log output for `rade_sends_vita49_directly` or `tci_creates_own_dax_tx_stream` to confirm the correct path was taken.

## Related

- [dax-tx-overview.md](dax-tx-overview.md)
- [rade-modem-setup.md](rade-modem-setup.md)
- [tci-tx-audio.md](tci-tx-audio.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
