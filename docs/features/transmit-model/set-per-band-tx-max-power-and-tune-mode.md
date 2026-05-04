# Set per-band TX max power and tune mode

When the radio reports a new maximum allowed TX output power, AetherSDR fires the `maxPowerLevelChanged` signal to cap the RF Power slider and scale the forward-power gauge in the TX applet to the radio's safe operating limit for the current band.

## Before you start

- Confirm the radio is connected and the TX applet is open.
- Verify you are transmitting on the band whose limit you want to inspect or work within — the maximum power level is reported per band by the radio firmware and cannot be overridden in software.

## Steps

1. Open the TX applet and locate the **RF Power** slider. When you change bands, the radio reports a new maximum power level; the slider ceiling and forward-power gauge update automatically to reflect that limit.
2. Drag the **RF Power** slider to set your desired output level anywhere from the minimum up to the band's reported maximum (in watts).
3. To set the tune mode, select the desired mode from the **Tune Mode** selector in the TX applet before initiating a transmission.

## What each control does

| Control | Behavior |
|---|---|
| RF Power slider | Sets the TX output power in watts. The upper bound is capped automatically each time `maxPowerLevelChanged` fires, preventing output above the radio's safe limit for the active band. |
| Forward-power gauge | Scaled to the current band's maximum power level. The full-scale reading always represents the radio-reported maximum for the active band. |
| Tune Mode selector | Selects the transmit tune mode (e.g., CW, tone, or noise) used when keying the radio for antenna tuning purposes. |

## Tips

- You do not need to manually read or set the per-band power limit — the radio reports it automatically on every band change and the UI adjusts instantly.
- If the RF Power slider appears lower than expected after a band change, the radio has reported a lower maximum for that band; this is normal and protects the hardware.

## Related

- [tx-applet-overview.md](tx-applet-overview.md)
- [connect-to-radio.md](connect-to-radio.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
