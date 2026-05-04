# Inhibit TX outputs during tune on a specific band

When AetherSDR runs a tune cycle, it can automatically suppress individual TX outputs on a per-band basis to protect connected power amplifiers or ancillary equipment from unintended RF.

## Before you start

- Confirm which physical TX outputs (ACC TX, TX1, TX2, TX3) your amplifiers or accessories are connected to.
- Know which band you want to configure — settings are stored independently for each amateur band.

## Steps

1. Open the band settings for the band you want to configure (for example, via the band selector or band-specific settings panel).
2. Locate the **Tune Inhibit** controls for that band and enable the checkbox for each TX output you want suppressed during a tune cycle: **Tune Inhibit ACC TX**, **Tune Inhibit TX1**, **Tune Inhibit TX2**, and/or **Tune Inhibit TX3**.
3. Save or apply the band settings. The selected outputs will be muted automatically whenever a tune is initiated on that band.

## What each control does

| Control | Behavior |
|---|---|
| **Tune Inhibit ACC TX** | Suppresses the ACC TX output during a tune cycle on this band. Enable this if an accessory connected to ACC TX should not receive RF while tuning. |
| **Tune Inhibit TX1** | Suppresses the TX1 output during a tune cycle on this band. Enable this to protect an amplifier connected to TX1. |
| **Tune Inhibit TX2** | Suppresses the TX2 output during a tune cycle on this band. Enable this to protect an amplifier or device connected to TX2. |
| **Tune Inhibit TX3** | Suppresses the TX3 output during a tune cycle on this band. Enable this to protect an amplifier or device connected to TX3. |

## Tips

- These settings are persisted per band, so you only need to configure each band once. Switching bands will automatically apply the correct inhibit pattern.
- If you use a single amplifier on TX1 across all bands, enable **Tune Inhibit TX1** on every band where that amplifier is active.
- Outputs not checked remain active during tune — only enable inhibits for outputs where connected equipment could be damaged by tune-level RF.

## Related

- [per-band-tx-settings.md](per-band-tx-settings.md)
- [tune-power.md](tune-power.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
