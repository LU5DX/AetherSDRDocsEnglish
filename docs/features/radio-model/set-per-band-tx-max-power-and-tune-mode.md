# Set per-band TX max power and tune mode

`TxBandInfo` stores the transmit power level, tune power level, hardware ALC state, and TX output enable flags for each amateur band. Use these settings to cap output power on a per-band basis and control which TX outputs are suppressed during a tune cycle to protect connected amplifiers.

## Before you start

- Confirm your radio is connected and that at least one band has been selected as the active TX band.
- Identify which external amplifiers or accessories are connected to ACC TX, TX1, TX2, and TX3 so you know which outputs to inhibit during tuning.

## Steps

1. Open the per-band TX settings panel for the band you want to configure (typically found under the band's TX or power section in the radio settings).
2. Set **TX Max Power** to the maximum output level allowed for that band.
3. Set **Tune Power** to the reduced power level the radio will use during a tune cycle.
4. Enable or disable **Hardware ALC** as required by your amplifier.
5. For each TX output that must be suppressed during tuning, check the corresponding inhibit flag:
   - **Tune Inhibit ACC TX** — suppresses the ACC TX output during tune.
   - **Tune Inhibit TX1** — suppresses TX1 during tune.
   - **Tune Inhibit TX2** — suppresses TX2 during tune.
   - **Tune Inhibit TX3** — suppresses TX3 during tune.
6. Repeat for each band that needs individual power or tune settings.

## What each control does

| Control | Behavior |
|---|---|
| TX Max Power | Sets the upper power limit for this band. The radio will not exceed this level during normal transmission. |
| Tune Power | Sets the output power used specifically during a tune cycle, typically lower than the operating power to protect the antenna and amplifier. |
| Hardware ALC | Enables the radio's hardware automatic level control for this band. Enable this when your amplifier provides an ALC voltage feedback line. |
| TX Output Enable | Enables or disables the TX output for this band globally. |
| Tune Inhibit ACC TX | When checked, the ACC TX output is automatically muted whenever a tune cycle is active on this band. Persisted per band. |
| Tune Inhibit TX1 | When checked, TX1 is automatically muted during a tune cycle on this band. Persisted per band. |
| Tune Inhibit TX2 | When checked, TX2 is automatically muted during a tune cycle on this band. Persisted per band. |
| Tune Inhibit TX3 | When checked, TX3 is automatically muted during a tune cycle on this band. Persisted per band. |

## Tips

- Set all inhibit flags for any amplifier that cannot safely handle full drive during tuning — even a brief full-power burst into an unloaded amplifier can cause damage.
- Tune Power and the inhibit flags are saved separately for each band, so settings for 160 m will not affect 10 m.
- If you use an antenna switch or relay box on ACC TX, enabling **Tune Inhibit ACC TX** prevents the switch from receiving a TX signal before it has finished switching.

## Related

- [TX settings overview](tx-settings-overview.md)
- [Band stack configuration](band-stack-configuration.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
