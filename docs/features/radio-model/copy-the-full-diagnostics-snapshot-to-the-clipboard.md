# Copy the full diagnostics snapshot to the clipboard

The `DaxStreamDebugState` struct captures a point-in-time snapshot of DAX stream diagnostics. Use this procedure to copy that snapshot to the clipboard for pasting into a bug report or support ticket.

## Before you start

- Ensure AetherSDR is connected to a radio so that stream state is populated.

## Steps

1. Open the diagnostics panel that displays the DAX stream debug state.
2. Click **Copy to Clipboard** to copy the full diagnostics snapshot.

## What each control does

| Control | Behavior |
|---|---|
| Copy to Clipboard | Serializes the current `DaxStreamDebugState` snapshot to plain text and writes it to the system clipboard. |

## Tips

- Paste the snapshot into a plain-text editor to review individual fields before attaching it to a report.
- Capture the snapshot while the problem is actively occurring; stream state can change quickly after a disconnect or reconnect.

## Related

- [DAX stream diagnostics overview](dax-stream-diagnostics.md)
- [Reporting issues](reporting-issues.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
