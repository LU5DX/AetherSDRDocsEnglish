# Diagnose duplicate-client UDP port collision errors

When the radio rejects the initially chosen UDP port because another client is already using it, `PanadapterStream` automatically recovers by releasing the conflicting port, binding to a new OS-assigned (ephemeral) port, and re-registering with the radio so the data stream resumes without manual intervention.

## Before you start

- Confirm you are running AetherSDR v0.9.7 or later, which includes the `rebindToEphemeralPort` fix.
- Ensure you have access to the application log output (console or log file).

## Steps

1. Open the application log and search for the string `PanadapterStream` near the time the panadapter stopped updating. A port collision is indicated by a log entry showing the initial UDP registration was rejected, followed by a new registration attempt to a different port.
2. Verify recovery succeeded by confirming a subsequent log line reads:

   ```
   PanadapterStream: sent UDP registration to <radio-ip>:4992
   ```

   This confirms `rebindToEphemeralPort` completed and the stream re-registered with the radio on the new port.
3. If the log shows repeated registration attempts without a successful confirmation line, check that no firewall or NAT rule is blocking outbound UDP on ephemeral port ranges (typically 49152–65535 on most operating systems).
4. If two instances of AetherSDR are running against the same radio simultaneously, close the duplicate instance. The automatic rebind resolves a one-time collision; persistent conflicts indicate a second client holding the port.

## What each control does

| Component | Behavior |
|---|---|
| `PanadapterStream::rebindToEphemeralPort` | Detects that the radio rejected the chosen UDP port as already in use, closes the current socket, asks the OS to assign a new available port, then sends a fresh UDP registration datagram to the radio on port 4992 so the panadapter data stream resumes. |

## Tips

- The rebind happens automatically and silently in normal operation. You only need this procedure when the panadapter display freezes and log evidence points to a port collision rather than a network or radio fault.
- After a successful rebind, packet error and total counts reset per stream. Use the network quality monitor to confirm clean reception on the new port.

## Related

- [Connect to a radio](connect-to-radio.md)
- [Troubleshoot panadapter display issues](troubleshoot-panadapter.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
