# Copy the full diagnostics snapshot to the clipboard

The `DaxStreamDebugState` struct captures a point-in-time snapshot of DAX stream diagnostics. Use this task to copy that snapshot to the clipboard for pasting into a bug report or support ticket.

## Before you start

- A radio must be connected and at least one DAX stream must be active before a meaningful snapshot is available.

## Steps

1. Open the Diagnostics panel for the active DAX stream.
2. Click **Copy to Clipboard** to copy the full `DaxStreamDebugState` snapshot to the system clipboard.

## Tips

- Paste the snapshot directly into a plain-text editor or issue tracker — the output is formatted as readable key-value pairs.
- If the snapshot appears empty, confirm that a DAX stream is currently running; the struct only contains data while a stream is active.

## Related

- [dax-stream-diagnostics.md](dax-stream-diagnostics.md)
- [troubleshooting-dax.md](troubleshooting-dax.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
