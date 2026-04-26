# Bypass the Compressor from the Chain

Enable or disable the Aetherial Compressor (TX) or Aetherial AGC-C (RX) without changing any of its settings. Bypassing lets you compare processed and unprocessed audio or temporarily take the compressor out of the signal path.

## Before you start

- The CHAIN widget must be visible in the Aetherial Audio (TXDSP) parent container.
- Identify which side you want to bypass: the TX compressor (COMP stage on the TX chain) or the RX compressor (COMP stage on the RX chain).

## Steps

1. Locate the CHAIN widget for the side you want to affect (TX or RX).
2. Single-click the **COMP** stage in the CHAIN widget.
   - One click toggles the bypass state for that stage.
   - When bypassed, the stage is inactive and the Aetherial Compressor (TX) or Aetherial AGC-C (RX) sub-container tile hides itself.
   - When enabled (bypass off), the tile becomes visible and the compressor processes audio.
3. To re-enable, single-click the **COMP** stage again.

## What each control does

| Control | What it does | Setting key |
|---|---|---|
| COMP stage (TX, single-click) | Toggles the TX compressor in or out of the signal chain. Enabled state is persisted. | `ClientCompTxEnabled` |
| COMP stage (RX, single-click) | Toggles the RX compressor in or out of the signal chain. Enabled state is persisted. | `ClientCompRxEnabled` |

## Tips

- Bypassing does not reset any knob values. Thresh, Ratio, Attack, Release, and Makeup all remain at their last positions when you re-enable the stage.
- Double-clicking the **COMP** stage opens the full Compressor editor rather than toggling bypass. Use a single click for bypass only.
- The gain-reduction bar in the applet tile reads zero when bypassed, since no processing is occurring. Use this as a quick confirmation that bypass is active.

## Related

- [Aetherial Compressor (TX) / Aetherial AGC-C (RX) overview](overview.md)
- [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md)
- [Watch live gain reduction while speaking or listening](watch-live-gain-reduction-while-speaking-or-listening.md)
