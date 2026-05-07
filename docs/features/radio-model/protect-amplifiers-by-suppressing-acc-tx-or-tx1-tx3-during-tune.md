# Protect amplifiers by suppressing ACC TX or TX1-TX3 during tune

AetherSDR can automatically suppress one or more TX outputs while a tune cycle is running, preventing full-power signals from reaching connected amplifiers. These inhibit flags are saved per band, so each band can have its own suppression profile.

## Before you start

- Identify which physical TX outputs your amplifiers are connected to (ACC TX, TX1, TX2, or TX3).
- Confirm you are configuring the correct band — settings are stored independently for each amateur band.

## Steps

1. Open the per-band TX settings for the band you want to configure.
2. Enable the inhibit flag for each output that should be suppressed during tune:
   - **TuneInhibitAccTx** — suppresses the ACC TX output.
   - **TuneInhibitTx1** — suppresses the TX1 output.
   - **TuneInhibitTx2** — suppresses the TX2 output.
   - **TuneInhibitTx3** — suppresses the TX3 output.
3. Repeat for any other bands that drive the same amplifiers.

## What each control does

| Control | Behavior |
|---|---|
| TuneInhibitAccTx | When enabled, the ACC TX output is held inactive for the duration of the tune cycle on this band. |
| TuneInhibitTx1 | When enabled, the TX1 output is held inactive for the duration of the tune cycle on this band. |
| TuneInhibitTx2 | When enabled, the TX2 output is held inactive for the duration of the tune cycle on this band. |
| TuneInhibitTx3 | When enabled, the TX3 output is held inactive for the duration of the tune cycle on this band. |

## Tips

- Enable only the outputs your amplifiers are actually connected to. Suppressing unused outputs has no effect but leaving an amplifier output un-inhibited during tune can cause damage.
- Because these flags are stored per band, switching bands automatically applies the correct suppression profile without manual changes.
- Tune power is a separate per-band setting. Combining a reduced tune power level with output inhibit gives the most protection during antenna tuning.

## Related

- [Per-Band TX Settings](tx-band-settings.md)
- [Tune power and hardware ALC](tune-power-alc.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
