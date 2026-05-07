# Inhibit TX outputs during tune on a specific band

Per-band TX settings let you suppress specific TX outputs automatically whenever a tune cycle runs, protecting connected amplifiers from full-power transients during antenna tuning.

## Before you start

- Identify which band you want to configure and which physical TX outputs (ACC TX, TX1, TX2, TX3) feed your amplifier or other sensitive equipment.

## Steps

1. Open the per-band TX settings for the target band.
2. Enable one or more of the tune inhibit flags — **Tune Inhibit ACC TX**, **Tune Inhibit TX1**, **Tune Inhibit TX2**, or **Tune Inhibit TX3** — for each output you want suppressed during tune.
3. Save or confirm the settings. AetherSDR will automatically hold those outputs inactive for the duration of every tune cycle on that band.

## What each control does

| Control | Behavior |
|---|---|
| Tune Inhibit ACC TX | Suppresses the ACC TX output during a tune cycle on this band. |
| Tune Inhibit TX1 | Suppresses the TX1 output during a tune cycle on this band. |
| Tune Inhibit TX2 | Suppresses the TX2 output during a tune cycle on this band. |
| Tune Inhibit TX3 | Suppresses the TX3 output during a tune cycle on this band. |

## Tips

- These settings are saved per band. Configure each band independently if you use different amplifiers on different bands.
- If an amplifier is connected to more than one TX output, inhibit all relevant outputs for that band to ensure it is fully protected during tune.
- Outputs not flagged for inhibition continue to operate normally during tune. Only enable inhibition for outputs connected to equipment that cannot tolerate tune power levels.

## Related

- [Per-Band TX Settings overview](tx-band-settings.md)
- [Tune power configuration](tune-power.md)
- [Hardware ALC settings](hardware-alc.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
