# Set per-band TX max power and tune mode

When the radio reports a new maximum allowed TX output power, AetherSDR fires the `maxPowerLevelChanged` signal to scale the forward-power gauge and cap the RF Power slider in the TX applet to the radio's safe operating limit for the current band.

## Before you start

- Connect to a radio that reports per-band power limits over the network.
- Open the TX applet.

## Steps

1. Select the operating band using the band selector. The radio reports its maximum allowed TX power for that band; AetherSDR receives the value automatically via `maxPowerLevelChanged`.
2. In the TX applet, drag the **RF Power** slider to your desired output level. The slider ceiling is capped to the radio-reported maximum — you cannot set a value above the safe limit for the current band.
3. To change the tune mode, locate the **Tune Mode** control in the TX applet and select the desired mode from the drop-down.

## What each control does

| Control | Behavior |
|---|---|
| RF Power slider | Sets TX output power in watts. The upper limit is capped in real time to the value received from the radio for the active band via `maxPowerLevelChanged`. |
| Forward-power gauge | Displays current forward power scaled against the radio-reported band maximum. Updates whenever `maxPowerLevelChanged` fires. |
| Tune Mode selector | Selects the tune mode for the active band (e.g., carrier, two-tone, noise). Applied immediately on change. |

## Tips

- Switching bands resets the RF Power slider ceiling automatically; you do not need to adjust any setting manually.
- If the slider appears stuck below your expected value, the radio is enforcing a lower band limit — check the radio's own band-plan settings.

## Related

- [tx-applet.md](tx-applet.md)
- [forward-power-gauge.md](forward-power-gauge.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
