# Diagnose DAX transmit packet delivery issues

`PanadapterStream::sendToRadio` transmits raw VITA-49 UDP datagrams to the radio, delivering DAX TX audio packets from the client for transmission. Use this guide to identify why those packets are not reaching the radio.

## Before you start

- Confirm the radio is reachable on the network and the UDP port is not blocked by a firewall.
- Know which DAX TX request reason applies to your setup (see the table below).

## Steps

1. Check the DAX TX policy decision for your request reason. Open the AetherSDR debug log and filter for `lcVita49`. Look for the policy result string next to your stream — for example, `hosted_dax_available`, `rade_sends_vita49_directly`, or `SmartSDR_DAX2_owns_windows_dax`. A `false` decision means the stream was intentionally blocked; match the result string to the table below to understand why.
2. Verify bytes are leaving the client. In the debug log, locate the `totalRx` value printed by the WAN ping keepalive line. If `totalRx` stays at zero and no registration datagrams appear, the UDP socket is not sending. Rebind the socket (disconnect and reconnect the radio) and watch for the `sent UDP registration to <ip>:4992` log line to confirm the registration datagram was delivered.

## What each control does

| Request reason | Policy behavior |
|---|---|
| `hosted_dax_bridge` | Allowed when DAX mode is `HostedDax` and hosted DAX is available. Blocked (`SmartSDR_DAX2_owns_windows_dax`) when DAX mode is `ExternalDax2`. Otherwise blocked with `hosted_dax_unavailable`. |
| `tci_tx_audio` | Always allowed. TCI creates its own DAX TX stream and never uses Windows audio devices. |
| `rade_modem_tx` | Always allowed. RADE encodes the mic waveform and sends VITA-49 packets directly via `sendModemTxAudio()`, bypassing Windows audio devices entirely. SmartSDR DAX2 ownership of the audio device layer does not affect this path. |
| `external_dax_route_only` | Blocked when DAX mode is `ExternalDax2` (`SmartSDR_DAX2_owns_windows_dax`). Otherwise blocked with `route_only_does_not_require_local_stream`. |
| `generic_audio_recreate` | Evaluated based on general DAX TX policy context. |

## Tips

- If you are using RADE modem TX and packets are not arriving, the policy decision will always be `rade_sends_vita49_directly`. The problem is almost certainly a UDP routing or firewall issue rather than a policy block — confirm port 4992 is open between client and radio.
- When SmartSDR DAX2 is installed on Windows, `hosted_dax_bridge` and `external_dax_route_only` requests are blocked by design. Switch to `tci_tx_audio` or `rade_modem_tx` if you need to bypass that restriction.
- The `totalRx` byte counter in the keepalive log line confirms the socket is receiving data back from the radio. Zero bytes after a successful registration indicates a network-layer problem, not a policy block.

## Related

- [dax-tx-overview.md](dax-tx-overview.md)
- [vita49-stream-troubleshooting.md](vita49-stream-troubleshooting.md)
- [rade-modem-setup.md](rade-modem-setup.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
