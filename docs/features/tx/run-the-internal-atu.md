# Run the internal ATU

Use the internal automatic antenna tuner (ATU) to find a low-SWR match on your current frequency. After a successful tune cycle, the ATU stores the result in memory for quick recall.

## Before you start

- AetherSDR must be connected to the radio. The TX applet is not functional without a radio connection.
- The TGXL must not be in OPERATE mode. ATU is disabled when TGXL is in OPERATE mode.
- Set `Tune Pwr` to an appropriate level for your antenna before running the ATU. The default is 10.

## Steps

1. Click the TX tray button in the right sidebar to open the TX Controls applet if it is not already visible.
2. Adjust the `Tune Pwr` slider to the desired tune-carrier power level (0–100; default 10).
3. Click `ATU`.
4. Wait for the tuning cycle to complete. Monitor the `Success`, `Byp`, and `Mem` indicators for the result.

## What each control does

| Control | Kind | Behavior | Default | Range |
|---|---|---|---|---|
| ATU | Push button | Starts the internal ATU tuning cycle. Disabled when TGXL is in OPERATE mode. | — | — |
| MEM | Toggle button | Toggles ATU memory recall on/off. Disabled when TGXL is in OPERATE mode. | — | — |
| Tune Pwr | Slider | Sets the tune-carrier power level sent to the radio during tuning. | 10 | 0–100 |
| Success | Indicator | Lights green when the ATU tuning result is successful or OK. | dim | dim / green |
| Byp | Indicator | Lights orange when the ATU is in Bypass or ManualBypass. | dim | dim / orange |
| Mem | Indicator | Lights green when the ATU is using a stored memory. | dim | dim / green |

## Tips

- If `Byp` lights after the tuning cycle, the ATU was unable to find a match and has bypassed itself. Check your antenna system and SWR before transmitting at full power.
- If `Mem` lights, the ATU applied a previously stored tuning memory rather than running a full tune. This is normal when `MEM` is enabled and a valid memory exists for the current frequency.

## Troubleshooting

- **ATU button is unresponsive** — The radio's TGXL is in OPERATE mode. ATU is disabled in this mode. Switch the TGXL out of OPERATE mode before attempting to tune.
- **Success indicator does not light after tuning** — The ATU may have bypassed (check `Byp`) or the tune-carrier power may be too low for the ATU to work with your antenna. Increase `Tune Pwr` and try again.

## Related

- [Recall an ATU memory](recall-an-atu-memory.md)
- [Start a tune carrier to check SWR](start-a-tune-carrier-to-check-swr.md)
- [Set tune-carrier power](set-tune-carrier-power.md)
- [TX Controls overview](overview.md)
