# Troubleshoot DAX IQ data not appearing in third-party software

When DAX IQ data does not appear in third-party software, the most common cause is a failure in how AetherSDR routes incoming baseband samples to the correct IQ channel. `PanadapterStream::registerIqStream` maps the radio's stream ID to a channel number; if that registration is missing or the UDP socket fails to bind, samples never reach the consumer.

## Before you start

- Confirm the radio is connected and the DAX IQ channel is enabled in AetherSDR.
- Confirm your third-party software is configured to receive on the correct DAX IQ channel number.
- Ensure no other application is exclusively holding the UDP port used for VITA-49 data.

## Steps

1. **Check that the DAX IQ channel is active.** In AetherSDR, open the DAX panel and verify the IQ channel you expect is turned on. If it is off, the stream ID is never registered and no samples are routed.

2. **Verify the UDP socket bound successfully.** Open the AetherSDR diagnostic log (Help > Diagnostic Log) and search for the string `PanadapterStream: LAN VITA UDP bind`. A successful entry looks like:

   ```
   PanadapterStream: LAN VITA UDP bind addr=<address> port=<port> flags=DontShareAddress reason=<reason>
   ```

   If you see `PanadapterStream: failed to bind UDP socket` instead, another process is holding the address exclusively. Close any application that may be using the VITA-49 UDP stream and restart the DAX IQ channel.

3. **Confirm the stream ID is registered to the correct channel.** If the log shows a successful bind but data still does not appear, the stream ID reported by the radio may not match what `registerIqStream` recorded. Disconnect from the radio, reconnect, and re-enable the DAX IQ channel to force a fresh registration.

4. **Check your network interface binding.** If you use a VPN or have multiple network adapters, AetherSDR selects a bind address automatically (explicit → probe-session → tcp-local → any). If the wrong adapter is chosen, samples are sent to an interface your third-party software is not listening on. Use your operating system's network settings to confirm which adapter carries traffic to the radio, and ensure your third-party software listens on the same interface.

## Tips

- The `DontShareAddress` socket flag means only one application can bind to the VITA-49 UDP port at a time. If two DAX-aware applications run simultaneously, the second will fail to bind. Stop the unused application first.
- After any network change (VPN connect/disconnect, adapter enable/disable), disconnect from the radio and reconnect so the bind address is re-evaluated.

## Related

- [Configure DAX IQ channels](configure-dax-iq-channels.md)
- [View diagnostic logs](view-diagnostic-logs.md)
- [Connect to a radio over VPN](connect-radio-vpn.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
