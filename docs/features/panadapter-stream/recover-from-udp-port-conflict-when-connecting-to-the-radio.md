# Recover from UDP port conflict when connecting to the radio

When the radio rejects the initially chosen UDP port because another client is already using it, AetherSDR automatically rebinds the data stream to a new OS-assigned port and re-registers with the radio so the connection can proceed.

## Before you start

- You must have a `RadioConnection` established or in progress before recovery can run.
- The `PanadapterStream` must have been initialised (i.e. `init()` called) before rebinding is attempted.

## Steps

1. Attempt to connect to the radio as normal. If the radio reports a UDP port conflict, AetherSDR calls `rebindToEphemeralPort` automatically — no manual action is required.
2. If the automatic recovery fails (for example, the socket itself cannot be rebound), check the application log for a warning beginning with `PanadapterStream:` and verify that no firewall rule is blocking all ephemeral UDP ports on your machine, then retry the connection.

## What each control does

| Control | Behavior |
|---|---|
| `rebindToEphemeralPort` | Stops any pending stream timers, closes the current UDP socket binding, asks the OS to assign a new free port (port 0 bind), and re-registers that port with the radio so the data stream can resume. |

## Tips

- The OS-assigned port is logged at info level. Search the application log for `PanadapterStream: LAN VITA UDP bind` to confirm which port was chosen after recovery.
- If your network has firewall rules that only allow specific UDP ports, you may need to open a range of ephemeral ports (typically 49152–65535) to allow the recovered stream through.

## Related

- [Connect to a radio](connect-to-radio.md)
- [Troubleshoot UDP stream issues](troubleshoot-udp-stream.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
