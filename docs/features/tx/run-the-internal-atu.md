# Run the internal ATU

Use the internal automatic antenna tuner (ATU) to find the best match for your antenna on the current frequency. This reduces SWR and protects your finals before operating.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The TX Controls applet requires an active radio connection.
- Your radio must have an internal ATU fitted and enabled. ATU and MEM controls are disabled when a TGXL amplifier is in OPERATE mode.
- Set your tune-carrier power level before starting. A low power level (default 10) is recommended for the tuning cycle.

## Steps

1. Click the TX tray button in the right sidebar to open the TX Controls applet if it is not already visible.
2. Check the **Tune Pwr** slider. The default is 10. Adjust if needed before tuning.
3. Click **ATU**.

The radio immediately begins its ATU tuning cycle. Watch the three ATU status indicators:

- **Success** lights green when the tuner finds an acceptable match.
- **Byp** lights orange if the ATU enters bypass or manual bypass.
- **Mem** lights green if the tuner applied a stored memory rather than performing a full sweep.

## What each control does

| Control | Kind | Default | Behavior |
|---|---|---|---|
| ATU | Button | — | Starts the internal ATU tuning cycle. Disabled when TGXL is in OPERATE mode. |
| MEM | Toggle button | — | Toggles ATU memory recall on or off. Disabled when TGXL is in OPERATE mode. |
| Tune Pwr | Slider | 10 | Sets the tune-carrier power level used during tuning. Range 0–100. |
| Success | Indicator | dim | Lights green when ATU status is Successful or OK. |
| Byp | Indicator | dim | Lights orange when ATU is in Bypass or ManualBypass. |
| Mem | Indicator | dim | Lights green when the ATU is using a stored memory. |

## Tips

- If you change band or move significantly in frequency, click **ATU** again to re-tune. A stored match from a distant frequency may not be optimal.
- To let the radio reuse previously stored matches without running a full tuning sweep each time, enable **MEM** before clicking **ATU**.

## Troubleshooting

- **ATU and MEM buttons are greyed out** — A TGXL amplifier is connected and is in OPERATE mode. Switch the TGXL out of OPERATE mode before using the ATU.
- **Byp lights orange after tuning** — The ATU could not find a match within its range and has bypassed itself. Check your antenna system and feedline for faults, then try again.

## Related

- [Recall an ATU memory](recall-an-atu-memory.md)
- [Set tune-carrier power](set-tune-carrier-power.md)
- [Start a tune carrier to check SWR](start-a-tune-carrier-to-check-swr.md)
- [Set RF output power](set-rf-output-power.md)
