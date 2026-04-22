# Bypass the Compressor from the Chain

Use this page to disable (bypass) the client-side TX compressor so it passes audio through without affecting it. Bypassing lets you compare compressed and uncompressed audio, or temporarily remove the compressor from the TX signal chain without changing any of its settings.

## Before you start

- The TXDSP (PooDoo Audio) parent container must be visible in the applet panel.
- The Compressor stage must already be present in the CHAIN widget.

## Steps

1. Locate the CHAIN widget inside the TXDSP parent container.
2. Single-click the **Comp** stage in the CHAIN widget to toggle bypass on or off.
   - When bypass is active, the COMPRESSOR sub-container tile hides and `ClientCompTxEnabled` is set to `false`.
   - When bypass is off (compressor active), the COMPRESSOR sub-container tile becomes visible and `ClientCompTxEnabled` is set to `true`.

## What each control does

| Control | Kind | Default | Persisted key |
|---|---|---|---|
| Comp stage (CHAIN widget) | Toggle | Enabled (bypass off) | `ClientCompTxEnabled` |
| Thresh | Knob | -18.0 dB | `ClientCompTxThresholdDb` |
| Ratio | Knob | 3.0 | `ClientCompTxRatio` |
| Attack | Knob | 20.0 ms | `ClientCompTxAttackMs` |
| Release | Knob | 200 ms | `ClientCompTxReleaseMs` |
| Makeup | Knob | 0.0 dB | `ClientCompTxMakeupDb` |

Bypassing does not reset any of these values. All knob positions are preserved while the stage is bypassed.

## Tips

- Single-click toggles bypass; double-click opens the floating Compressor editor. Take care not to double-click when you only intend to bypass.
- The COMPRESSOR sub-container tile disappears entirely when bypass is active. This is expected — it reappears as soon as you re-enable the stage.
- The gain-reduction bar reads zero while bypassed, because no attenuation is being applied.

## Related

- [Compressor overview](overview.md)
- [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md)
- [Watch live gain reduction while speaking](watch-live-gain-reduction-while-speaking.md)
