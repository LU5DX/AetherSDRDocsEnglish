# Bypass the EQ stage from the chain

The client-side parametric EQ can be removed from the audio processing chain without deleting your band settings. Bypassing lets you A/B the EQ effect or temporarily disable processing on one path while leaving the other unchanged. The bypass state is saved per path in `ClientEqRxEnabled` and `ClientEqTxEnabled`.

## Before you start

- The CEQ sub-container must be visible inside the PooDoo Audio (TXDSP) parent container. It is hidden until the EQ stage has been enabled at least once via the CHAIN widget or the floating editor.
- Decide whether you want to bypass the RX path, the TX path, or both, before you start.

## Steps

1. Locate the CHAIN widget inside the PooDoo Audio (TXDSP) container.
2. Find the EQ stage block in the chain.
3. Single-click the EQ stage block to toggle bypass for that path. A single click enables or disables the stage directly in the chain.
4. To bypass the other path, switch to it first — use the RX or TX tab at the top of the CEQ applet to confirm which path is active — then single-click the EQ stage block again.

## What each control does

| Control | Kind | Default | Persisted key | Behavior |
|---|---|---|---|---|
| EQ stage (CHAIN widget, single-click) | Toggle | Enabled | `ClientEqRxEnabled` / `ClientEqTxEnabled` | Bypasses or re-inserts the client EQ for the selected path. Does not clear band data stored in `ClientEqRxBands` or `ClientEqTxBands`. |
| RX | Tab | Checked | — | Selects the receive path for display in the CEQ applet. |
| TX | Tab | Unchecked | — | Selects the transmit path for display in the CEQ applet. |

## Tips

- Bypassing a path leaves all band settings intact. Re-enabling restores the full curve immediately.
- The analyzer / curve area in the CEQ applet continues to display the stored EQ response shape even while the stage is bypassed, so you can still inspect your curve without processing it.

## Troubleshooting

- **The CEQ sub-container is not visible** — The EQ stage has not yet been enabled. Enable it once via the CHAIN widget or the floating editor to make the CEQ sub-container appear.
- **Single-clicking the EQ stage has no effect** — Confirm you are clicking the correct block in the CHAIN widget. Double-clicking opens the floating editor instead of toggling bypass.

## Related

- [Parametric EQ (Client) overview](overview.md)
- [Open the floating editor to add / remove / tune bands](open-the-floating-editor-to-add-remove-tune-bands.md)
- [Switch between viewing RX and TX EQ](switch-between-viewing-rx-and-tx-eq.md)
