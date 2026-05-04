# Protect amplifiers by suppressing ACC TX or TX1-TX3 during tune

AetherSDR can automatically suppress one or more TX outputs while a tune cycle is running, preventing full power from reaching a connected amplifier. These suppression flags are saved per band, so each band can have its own set of protected outputs.

## Before you start

- Confirm which TX outputs your amplifier is connected to (ACC TX, TX1, TX2, or TX3).
- Identify the band(s) where the amplifier is in use.

## Steps

1. Open the per-band TX settings for the band you want to protect.
2. Enable the suppression flag for each output connected to your amplifier: **Tune Inhibit ACC TX**, **Tune Inhibit TX1**, **Tune Inhibit TX2**, and/or **Tune Inhibit TX3**.
3. Repeat for any other bands where that amplifier is active.

## What each control does

| Control | Behavior |
|---|---|
| **Tune Inhibit ACC TX** | Suppresses the ACC TX output for the duration of a tune cycle on this band. |
| **Tune Inhibit TX1** | Suppresses the TX1 output for the duration of a tune cycle on this band. |
| **Tune Inhibit TX2** | Suppresses the TX2 output for the duration of a tune cycle on this band. |
| **Tune Inhibit TX3** | Suppresses the TX3 output for the duration of a tune cycle on this band. |

These settings are persisted per band. Changing the flag on one band does not affect other bands.

## Tips

- Enable inhibit only on the outputs that feed an amplifier. Outputs driving other loads (dummy loads, analyzers) do not need to be suppressed.
- If you use the same amplifier across multiple bands, configure the inhibit flags on each band individually — there is no global override.

## Related

- [Per-band TX settings](tx-band-settings.md)
- [Tune cycle overview](tune-cycle.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
