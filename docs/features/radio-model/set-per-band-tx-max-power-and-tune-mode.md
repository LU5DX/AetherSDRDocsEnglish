# Set per-band TX max power and tune mode

Each amateur band can have its own maximum TX power level and a separate lower power level used during tune cycles. You can also control which TX outputs are suppressed during a tune cycle to protect connected amplifiers.

## Before you start

- Ensure your radio is connected and recognized by AetherSDR before changing band-specific TX settings.

## Steps

1. Open the per-band TX settings for the band you want to configure.
2. Set **Max TX Power** to the highest output level allowed on that band.
3. Set **Tune Power** to the reduced power level used when the tune function is active.
4. Under **Tune Inhibit**, enable or disable each TX output (**ACC TX**, **TX1**, **TX2**, **TX3**) that should be suppressed during a tune cycle.
5. Save or apply the settings — changes are persisted per band automatically.

## What each control does

| Control | Behavior |
|---|---|
| Max TX Power | Sets the upper power limit for normal transmit on this band. The radio will not exceed this level during regular TX. |
| Tune Power | Sets the output power used specifically during a tune cycle. Typically set lower than Max TX Power to protect the antenna or tuner. |
| Hardware ALC | Enables the radio's hardware automatic level control for this band, limiting output to prevent overdrive. |
| TX Output Enable | Enables the TX output path for this band. Disable to prevent any transmission on the band. |
| Tune Inhibit: ACC TX | When enabled, the ACC TX output is suppressed (held low) for the duration of a tune cycle. Use this when an amplifier connected to ACC TX should not be keyed during tuning. |
| Tune Inhibit: TX1 | When enabled, the TX1 output is suppressed during a tune cycle. |
| Tune Inhibit: TX2 | When enabled, the TX2 output is suppressed during a tune cycle. |
| Tune Inhibit: TX3 | When enabled, the TX3 output is suppressed during a tune cycle. |

## Tips

- Set Tune Inhibit for any output connected to an amplifier that cannot tolerate the power level or duty cycle of a tune cycle — this prevents accidental amplifier keying during antenna matching.
- Tune Power and Tune Inhibit settings are saved per band, so you can configure different protection rules for each band independently.

## Related

- [TX settings overview](tx-settings.md)
- [Amplifier protection](amplifier-protection.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
