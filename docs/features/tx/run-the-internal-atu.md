# Run the internal ATU

Use this page to start an automatic antenna tuner (ATU) cycle on the FLEX-8600. The ATU finds a matching network that minimises SWR on the current frequency.

## Before you start

- AetherSDR must be connected to the radio. The TX Controls applet is only active when a radio connection is present.
- The radio must not be in TGXL OPERATE mode. ATU is disabled in that mode.
- Set your tune power to an appropriate level before starting. See [Set tune-carrier power](set-tune-carrier-power.md).

## Steps

1. Click the TX tray button in the right sidebar to open TX Controls if it is not already visible.
2. Adjust the `Tune Pwr` slider to the desired carrier power (default: 10, range: 0–100).
3. Click `ATU`.

The radio transmits a carrier and runs the tuning cycle. Watch the `Success`, `Byp`, and `Mem` indicators below the TX Profile selector to follow the result.

## What each control does

| Control | Kind | Description | Default | Range |
|---|---|---|---|---|
| ATU | Push button | Starts the internal ATU tuning cycle. Disabled in TGXL OPERATE mode. | — | — |
| Tune Pwr | Slider | Sets the carrier power used during tuning. | 10 | 0–100 |
| Success | Indicator | Lights green when the ATU tuning result is successful. | Dim | Dim / green |
| Byp | Indicator | Lights orange when the ATU is in bypass or manual bypass. | Dim | Dim / orange |
| Mem | Indicator | Lights green when the ATU is using a stored memory. | Dim | Dim / green |
| MEM | Toggle button | Toggles ATU memory recall on or off. Disabled in TGXL OPERATE mode. | — | On / Off |

## Tips

- If `Byp` lights after the cycle, the ATU was unable to find a match and has bypassed itself. Check your antenna system or try a different frequency.
- If `Mem` lights immediately after clicking ATU, the radio applied a stored memory rather than running a full tune cycle. Use [Recall an ATU memory](recall-an-atu-memory.md) for details on managing memories.
- Keep tune power low enough to satisfy your licence conditions and amplifier requirements. The `Tune Pwr` slider default is 10.

## Troubleshooting

- **ATU button is greyed out** — The radio is in TGXL OPERATE mode. ATU cannot be started in this mode. Switch the TGXL out of OPERATE mode first.
- **Success indicator does not light after tuning** — The ATU could not find an acceptable match. Check the antenna connection and SWR on the `SWR` gauge. Try reducing frequency deviation from the antenna's resonant point.
- **Byp lights instead of Success** — The ATU has bypassed itself. The antenna system may be outside the tuner's matching range.

## Related

- [Recall an ATU memory](recall-an-atu-memory.md)
- [Set tune-carrier power](set-tune-carrier-power.md)
- [Start a tune carrier to check SWR](start-a-tune-carrier-to-check-swr.md)
- [Set RF output power](set-rf-output-power.md)
