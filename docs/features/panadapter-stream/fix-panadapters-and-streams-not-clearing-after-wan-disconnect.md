# Fix panadapters and streams not clearing after WAN disconnect

`RadioConnection` manages the TCP control connection to the radio and coordinates UDP stream registration. Before v0.9.7, panadapters and streams were not cleared from the display after a WAN disconnect, leaving stale data visible.

## Before you start

- Update to AetherSDR v0.9.7 or later. This fix is not available in earlier releases.
- You must be using a WAN (remote) connection, not a direct LAN connection, to encounter this scenario.

## Steps

1. If you are currently connected over WAN and experience a disconnect, open the **Connection** panel.
2. Confirm that all panadapter displays and stream indicators have cleared automatically. No manual action is required — the fix causes AetherSDR to clear panadapters and streams as soon as the WAN connection drops.
3. Reconnect using the **Connect** button in the Connection panel. Panadapters and streams will repopulate normally once the connection is re-established.

## What changed in v0.9.7

| Area | Previous behavior | v0.9.7 behavior |
|---|---|---|
| Panadapters after WAN disconnect | Stale FFT data remained on screen | Panadapter display clears immediately on disconnect |
| Streams after WAN disconnect | Stream indicators remained active | All streams are torn down and cleared on disconnect |
| Byte counters (`totalRxBytes`, `totalTxBytes`) | Non-atomic reads could produce inconsistent values under concurrent access | Now backed by `std::atomic<qint64>` for safe concurrent reads |
| `categoryStats()` | Returned a const reference that could be invalidated | Returns a value copy, protected by an internal mutex |

## Tips

- If panadapters do not clear after a disconnect, verify you are running v0.9.7 or later via **Help > About**.
- After reconnecting, allow a few seconds for the radio to re-register UDP streams before expecting panadapter data to appear.

## Related

- [wan-connection.md](wan-connection.md)
- [panadapter-overview.md](panadapter-overview.md)
- [network-diagnostics.md](network-diagnostics.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
