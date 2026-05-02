# Run the internal ATU

Use the internal automatic antenna tuner (ATU) to find a low-SWR match on your current frequency. After a successful tune cycle, the ATU stores the result in memory for quick recall.

## Before you start

- AetherSDR must be connected to the radio. The TX applet is not functional without a radio connection.
- The TGXL must not be in OPERATE mode. ATU is disabled when TGXL is in OPERATE mode.
- Set `Tune Pwr` to an appropriate level for your antenna before running the ATU. The default is 10.

## Steps

1. Click the TX tray button in the right sidebar to open the TX Controls applet if it is not already visible.
2. Adjust the `Tune Pwr` slider to the desired tune-carrier power level (0–100; default 10).
3. Click `ATU` to start the tuning cycle.
4. Wait for the tuning cycle to complete. Monitor the `Success`, `Byp`, and `Mem` indicators for the result.

## What each control does

| Control  | Kind          | Behavior                                                                                                                                                                               |
|----------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ATU      | Push button   | Starts or bypasses the ATU depending on context (see [ATU button behavior](#atu-button-behavior)). Disabled when TGXL is in OPERATE mode. |
| MEM      | Toggle button | Toggles ATU memory recall on/off. Disabled when TGXL is in OPERATE mode.                                                                                                              |
| Tune Pwr | Slider        | Sets the tune-carrier power level sent to the radio during tuning.                                                                                                                     |
| Success  | Indicator     | Lights green when the ATU tuning result is successful or OK.                                                                                                                           |
| Byp      | Indicator     | Lights orange when the ATU is in Bypass or ManualBypass.                                                                                                                               |
| Mem      | Indicator     | Lights green when the ATU is using a stored memory.                                                                                                                                    |

## ATU button behavior

Starting with v0.9.5.1, the `ATU` button toggles between starting a tune cycle and switching the tuner into bypass, depending on the current ATU status and transmit frequency. This mirrors the per-frequency toggle behavior in SmartSDR.

| Situation | What `ATU` click does |
|---|---|
| No previous tune on this frequency, or ATU is not in a Successful/OK state | Starts a fresh ATU tune cycle. |
| ATU status is Successful or OK, and TX frequency has not changed since the last tune | Switches the ATU into bypass. |
| ATU status is Successful or OK, but TX frequency has changed since the last tune | Starts a fresh ATU tune cycle. |

In practice:
- The first click on a new frequency always starts a tune cycle.
- After a successful tune, clicking `ATU` again on the same frequency bypasses the tuner.
- Changing frequency resets the toggle, so the next click starts a fresh tune cycle regardless of the previous status.
- Entering bypass clears the stored tuned frequency, so the next click always starts a fresh tune.

## Tips

- If `Byp` lights after the tuning cycle, the ATU was unable to find a match and has bypassed itself. Check your antenna system and SWR before transmitting at full power.
- If `Mem` lights, the ATU applied a previously stored tuning memory rather than running a full tune. This is normal when `MEM` is enabled and a valid memory exists for the current frequency.
- To manually force the tuner into bypass after a successful tune, click `ATU` a second time without changing frequency.

## Troubleshooting

- **ATU button is unresponsive** — The radio's TGXL is in OPERATE mode. ATU is disabled in this mode. Switch the TGXL out of OPERATE mode before attempting to tune.
- **Success indicator does not light after tuning** — The ATU may have bypassed (check `Byp`) or the tune-carrier power may be too low for the ATU to work with your antenna. Increase `Tune Pwr` and try again.
- **Clicking ATU bypasses instead of tuning** — The ATU status is Successful or OK and the TX frequency has not changed since the last tune. This is the expected second-click bypass behavior. Change frequency to force a fresh tune cycle, or leave the tuner in its current matched state.

## Related

- [Recall an ATU memory](recall-an-atu-memory.md)
- [Start a tune carrier to check SWR](start-a-tune-carrier-to-check-swr.md)
- [Set tune-carrier power](set-tune-carrier-power.md)
- [TX Controls overview](overview.md)