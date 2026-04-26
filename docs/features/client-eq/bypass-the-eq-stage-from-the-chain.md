# Bypass the EQ stage from the chain

Remove the client-side parametric EQ from the audio processing chain without deleting your band settings. Use this when you want to compare processed and unprocessed audio, or temporarily disable EQ without losing your configuration.

## Before you start

- The ClientEqApplet (labeled "CEQ") must be visible in the applet panel. It is hidden until the EQ stage is enabled via the CHAIN widget or the floating editor.
- Open the floating EQ editor by double-clicking the EQ stage in the CHAIN widget. The bypass control lives in that editor, not in the compact CEQ applet tile.

## Steps

1. Double-click the EQ stage in the CHAIN widget to open the floating EQ editor.
2. In the floating editor, locate the enable toggle for the path you want to bypass — RX or TX.
3. Click the toggle to disable the EQ for that path.

The CEQ applet tile reflects the change: `ClientEqRxEnabled` or `ClientEqTxEnabled` is set to false for the affected path, and the EQ is removed from the signal chain. Your band settings stored in `ClientEqRxBands` and `ClientEqTxBands` are preserved.

## What each control does

| Control | Path | Persisted key | Default | Behavior |
|---|---|---|---|---|
| RX enable toggle | Receive | `ClientEqRxEnabled` | — | Inserts or bypasses the EQ in the RX audio chain. Bands are retained when bypassed. |
| TX enable toggle | Transmit | `ClientEqTxEnabled` | — | Inserts or bypasses the EQ in the TX audio chain. Bands are retained when bypassed. |
| `ClientEqRxBands` | Receive | `ClientEqRxBands` | — | Persisted band configuration for the RX path. Unaffected by bypass. |
| `ClientEqTxBands` | Transmit | `ClientEqTxBands` | — | Persisted band configuration for the TX path. Unaffected by bypass. |

## Tips

- Bypassing one path does not affect the other. You can bypass RX EQ while keeping TX EQ active, or vice versa.
- The summed EQ response curve in the CEQ applet tile shows the current state of the selected path. When bypassed, the curve reflects that the EQ is inactive.

## Troubleshooting

- **The CEQ applet tile is not visible** — The tile is hidden until the EQ stage is enabled from the CHAIN widget or the floating editor. Enable the stage first, then bypass it if needed.
- **Double-clicking the CHAIN widget does not open the floating editor** — Confirm you are double-clicking directly on the EQ stage block within the CHAIN widget, not on the surrounding container.

## Related

- [Parametric EQ (Client) overview](overview.md)
- [Open the floating editor to add / remove / tune bands](open-the-floating-editor-to-add-remove-tune-bands.md)
- [Switch between viewing RX and TX EQ](switch-between-viewing-rx-and-tx-eq.md)
