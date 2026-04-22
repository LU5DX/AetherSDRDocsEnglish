# Run the internal ATU

Use the ATU controls in the TX Controls applet to run the FLEX-8600's internal automatic antenna tuner and check the result. This reduces SWR and optimises the match between the radio and your antenna on the current frequency.

## Before you start

- Connect to a FLEX-8600 radio. The TX Controls applet requires an active radio connection.
- Ensure the TX Controls applet is visible. If it is not, click the TX tray button on the right sidebar.
- Check that you are not operating with a TGXL in OPERATE mode — ATU and MEM are disabled in that state.

## Steps

1. In the TX Controls applet, set the `Tune Pwr` slider to the power level you want the ATU to use during the tuning cycle (default: 10, range: 0–100).
2. Click ATU.
3. Watch the ATU status indicators — `Success`, `Byp`, and `Mem` — to confirm the outcome:
   - `Success` lights green when the tuner finds an acceptable match.
   - `Byp` lights orange if the ATU is in bypass or manual bypass.
   - `Mem` lights green if the tuner applied a stored memory rather than running a full tune cycle.

## What each control does

| Control | Kind | Default | Range | Behavior |
|---|---|---|---|---|
| ATU | Push button | — | — | Starts the internal ATU tuning cycle. Disabled when TGXL is in OPERATE mode. |
| MEM | Toggle button | — | — | Toggles ATU memory recall on or off. Disabled when TGXL is in OPERATE mode. |
| Tune Pwr | Slider | 10 | 0–100 | Sets the carrier power level used during tuning. |
| Success | Indicator | dim | dim / green | Lights green when ATU status is Successful or OK. |
| Byp | Indicator | dim | dim / orange | Lights orange when ATU is in Bypass or ManualBypass. |
| Mem | Indicator | dim | dim / green | Lights green when ATU is using a stored memory. |

## Tips

- Lower the `Tune Pwr` slider before clicking ATU if you want to tune at reduced power, for example when using a QRP antenna or protecting a linear amplifier.
- If `Byp` lights after the cycle completes, the ATU could not find a match and has bypassed itself. Check your antenna system and SWR with the `SWR` meter before transmitting.
- Use MEM to let the radio recall a previously stored ATU setting when you return to a frequency you have tuned before, avoiding a full tune cycle.

## Troubleshooting

- **ATU button does nothing** — Verify you are not running a TGXL in OPERATE mode. The ATU button is disabled in that configuration.
- **`Byp` lights instead of `Success`** — The tuner could not find an acceptable match. Check your feedline and antenna connections, then try again. See [Start a tune carrier to check SWR](start-a-tune-carrier-to-check-swr.md) to inspect SWR before retrying.
- **`Mem` lights but SWR is poor** — The recalled memory may be stale (antenna or feedline changed). Click ATU again to force a fresh tune cycle.

## Related

- [Recall an ATU memory](recall-an-atu-memory.md)
- [Start a tune carrier to check SWR](start-a-tune-carrier-to-check-swr.md)
- [Set tune-carrier power](set-tune-carrier-power.md)
- [TX Controls overview](overview.md)
