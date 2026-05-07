# Send DAX TX audio to the radio over UDP

`PanadapterStream::sendToRadio` transmits a raw VITA-49 UDP datagram from the client to the radio. Use this path to deliver DAX TX audio packets directly to the radio for transmission.

## Before you start

- A `RadioConnection` must be established and the `PanadapterStream` must be started before sending audio packets.
- Your audio data must already be packed into a valid VITA-49 datagram. AetherSDR does not repack raw PCM at this stage.
- Confirm the request reason is appropriate for your use case. For RADE modem transmit, use `RadeModemTx`; for TCI-sourced audio, use `TciTxAudio`.

## Steps

1. Obtain the active `PanadapterStream` instance from your `RadioConnection`.
2. Pack your audio payload into a VITA-49 UDP datagram.
3. Call `sendToRadio` with the datagram to dispatch it to the radio's DAX TX stream slot over UDP.

## What each control does

| Control | Behavior |
|---|---|
| `sendToRadio(datagram)` | Writes the supplied VITA-49 datagram to the UDP socket bound to the radio address and port. Increments the internal `m_totalTxBytes` counter by the number of bytes sent. |
| `DaxTxRequestReason::RadeModemTx` | Grants DAX TX stream access unconditionally. RADE encodes the mic waveform itself and sends VITA-49 packets directly, bypassing Windows audio devices. SmartSDR DAX2 ownership of the audio device layer does not block this path. |
| `DaxTxRequestReason::TciTxAudio` | Grants DAX TX stream access unconditionally. TCI creates its own DAX TX stream and never touches Windows audio devices. |
| `DaxTxRequestReason::HostedDaxBridge` | Grants access only when hosted DAX is available. Blocked when SmartSDR DAX2 owns the Windows audio device layer. |

## Tips

- `RadeModemTx` and `TciTxAudio` are the correct reasons whenever your code generates VITA-49 packets directly and does not route through Windows audio. Choosing `HostedDaxBridge` or `ExternalDaxRouteOnly` for these cases will cause the policy to deny the stream unnecessarily under SmartSDR DAX2.
- Monitor `m_totalTxBytes` during development to verify datagrams are being dispatched. A value that does not increase after calling `sendToRadio` indicates a socket or addressing problem.
- Keep datagrams within the MTU of your network path to avoid fragmentation of VITA-49 packets.

## Related

- [DAX TX policy overview](dax-tx-policy.md)
- [TCI TX audio](tci-tx-audio.md)
- [PanadapterStream lifecycle](panadapter-stream-lifecycle.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
