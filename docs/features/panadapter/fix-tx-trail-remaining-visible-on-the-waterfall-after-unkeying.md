# Fix TX trail remaining visible on the waterfall after unkeying

After transmitting, the waterfall could continue displaying a bright TX trail for 10–23 seconds after you released the key. This page explains what caused the artifact and confirms it is resolved in v0.9.7.

## Before you start

- AetherSDR v0.9.7 or later is required. Earlier versions exhibit the 10–23 s trail artifact by design.
- The radio must be connected. The fix relies on receiving the radio's interlock TRANSMITTING state over the SmartSDR protocol.

## Steps

The artifact is fixed automatically in v0.9.7. No user action is required.

When you transmit, the waterfall freezes as soon as the radio's interlock reports TRANSMITTING. When you unkey, the waterfall unfreezes as soon as the radio's interlock reports the TRANSMITTING state cleared. The freeze and unfreeze now track the radio's actual interlock state rather than a local software edge, which is what caused the trailing artifact in earlier versions.

If you are running v0.9.7 and still see a persistent trail after unkeying, work through the troubleshooting steps below.

## Tips

- In a multi-operator (multiFLEX) session, any connected client transmitting will trigger the waterfall freeze on your panadapter. This is expected behavior.

## Troubleshooting

- **Trail still visible after unkeying on v0.9.7** — Confirm the radio firmware is 4.1.5. If the firmware is older, the interlock TRANSMITTING state may not be reported correctly over the protocol, preventing the freeze/unfreeze from triggering at the right time.
- **Waterfall stays frozen after unkeying** — The radio's interlock state has not cleared. Check that nothing else (a foot switch, VOX, or another client) is holding the radio in TRANSMITTING. See `Settings > multiFLEX...` to review connected clients.
- **Artifact only appears on a popped-out panadapter** — On macOS, a popped-out panadapter can develop GPU surface issues after float/dock cycles. See [Fix a static/stale spectrum in a popped-out panadapter on macOS](fix-a-static-stale-spectrum-in-a-popped-out-panadapter-on-macos.md).

## Related

- [Panadapter overview](overview.md)
- [Fix a static/stale spectrum in a popped-out panadapter on macOS](fix-a-static-stale-spectrum-in-a-popped-out-panadapter-on-macos.md)
- [Pop a panadapter out into its own window](pop-a-panadapter-out-into-its-own-window.md)
