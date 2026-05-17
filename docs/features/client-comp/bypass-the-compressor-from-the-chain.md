# Bypass the Compressor from the Chain

Enable or disable the Aetherial Compressor (TX) or Aetherial AGC-C (RX) without changing any of its settings. Bypassing lets you compare processed and unprocessed audio or temporarily take the compressor out of the signal path.

## Before you start

- The CHAIN widget must be visible in the Aetherial Audio (TXDSP) parent container.
- Identify which side you want to bypass: the TX compressor (COMP stage on the TX chain) or the RX compressor (COMP stage on the RX chain).

## Steps

1. Locate the CHAIN widget for the side you want to affect (TX or RX).
2. Single-click the **COMP** stage in the CHAIN widget.
   - One click toggles the bypass state for that stage.
   - When bypassed, the stage is inactive and the Aetherial Compressor (TX) or Aetherial AGC-C (RX) applet tile dims to reduced opacity (approximately 55% of normal brightness), matching the dim effect used by the EQ curve when its stage is bypassed.
   - When enabled (bypass off), the tile returns to full opacity and the compressor processes audio.
3. To re-enable, single-click the **COMP** stage again.

## What each control does

| Control | What it does | Setting key |
|---|---|---|
| COMP stage (TX, single-click) | Toggles the TX compressor in or out of the signal chain. Enabled state is persisted. | `ClientCompTxEnabled` |
| COMP stage (RX, single-click) | Toggles the RX compressor in or out of the signal chain. Enabled state is persisted. | `ClientCompRxEnabled` |

## Applet tile controls

The Aetherial Compressor (TX) and Aetherial AGC-C (RX) applet tiles provide a compact view of compressor state with live feedback and five tuning knobs.

| Control | What it does | Setting key |
|---|---|---|
| Transfer curve | View-only display of the input/output transfer curve with a live ball showing the current envelope level. Editable in the floating Compressor editor. | N/A |
| Gain-reduction bar | Horizontal amber strip showing 0 to 20 dB of gain reduction right-filled. A tick at -6 dB marks a typical working amount. Refreshed ~30 Hz. | N/A |
| Thresh knob | Sets the level above which compression starts. Range -60.0 to 0.0 dB, default -18.0 dB. | `ClientCompTxThresholdDb` or `ClientCompRxThresholdDb` |
| Ratio knob | Sets how hard peaks are held once threshold is crossed. Range 1.0 to 20.0, default 3.0. Label formatted as "X.XX:1". | `ClientCompTxRatio` or `ClientCompRxRatio` |
| Attack knob | Sets how quickly the compressor clamps down after threshold is crossed. Range 0.1 to 300.0 ms, default 20.0 ms. | `ClientCompTxAttackMs` or `ClientCompRxAttackMs` |
| Release knob | Sets how quickly gain returns after input drops below threshold. Range 5 to 2000 ms, default 200 ms. | `ClientCompTxReleaseMs` or `ClientCompRxReleaseMs` |
| Makeup knob | Adds back gain lost to compression. Range -12.0 to 24.0 dB, default 0.0 dB. Positive values show a "+" sign. | `ClientCompTxMakeupDb` or `ClientCompRxMakeupDb` |

## Inline value editing

Knobs in the applet tile support inline value editing for precise adjustment:

1. Click a knob's current value label. The label transforms into an editable text field with a subtle dark background and cyan border.
2. Type a new value. Locale-aware parsing supports both period and comma decimal separators.
3. Press **Enter** to commit the value, or click elsewhere on the interface. The knob position updates to match the entered value.
4. Press **Escape** to cancel editing and revert to the previous value.
5. While the inline editor is active, mouse wheel events still adjust the knob normally.

## Tips

- Bypassing does not reset any knob values. Thresh, Ratio, Attack, Release, and Makeup all remain at their last positions when you re-enable the stage.
- Double-clicking the **COMP** stage opens the full Compressor editor rather than toggling bypass. Use a single click for bypass only.
- The gain-reduction bar in the applet tile reads zero when bypassed, since no processing is occurring. The dimmed tile appearance provides an additional at-a-glance confirmation that bypass is active.
- The TX and RX compressor instances have fully independent settings. Changing knobs in one does not affect the other.

## Related

- [Aetherial Compressor (TX) / Aetherial AGC-C (RX) overview](overview.md)
- [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md)
- [Watch live gain reduction while speaking or listening](watch-live-gain-reduction-while-speaking-or-listening.md)