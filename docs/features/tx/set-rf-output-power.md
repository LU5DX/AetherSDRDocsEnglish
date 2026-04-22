# Set RF output power

Use the RF Power slider in the TX Controls applet to set how much power the radio outputs during transmit. Adjust this before operating to stay within your licence limits and to protect connected amplifiers.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. If not, go to `Settings > Connect to Radio...`.
- The TX Controls applet must be visible. If it is not, click the TX tray button on the right sidebar to show it.

## Steps

1. Locate the **RF Power** slider in the TX Controls applet.
2. Drag the slider left to decrease power or right to increase power. The numeric readout to the right of the slider updates immediately.
3. Confirm the value shown beside the slider is the level you want. The radio applies the new setting as soon as you move the slider.

## What each control does

| Control | What it does | Default | Valid range |
|---|---|---|---|
| RF Power (slider) | Sets the transmit RF power level sent to the radio. | 100 | 0–100 |
| RF Pwr (meter) | Displays forward power at the exciter output. Read-only. | — | 0–120 W (barefoot); 0–600 W (Aurora 500W). Meter turns red above 100 W / 500 W. |
| SWR (meter) | Displays standing wave ratio at the exciter. Read-only. | — | 1.0–3.0. Meter turns red above 2.5. |

## Tips

- The RF Pwr meter scale changes automatically based on radio model. On a standard FLEX-8600 the red zone begins at 100 W; on an Aurora 500W model it begins at 500 W.
- To set power for a specific band without changing the global slider, use `Settings > TX Band Settings...`. That dialog provides per-band power and tune power values.
- Keep an eye on the SWR meter while transmitting. An SWR reading above 2.5 (red zone) suggests an antenna or feedline problem.

## Related

- [TX Controls overview](overview.md)
- [Set tune-carrier power](set-tune-carrier-power.md)
- [Start a tune carrier to check SWR](start-a-tune-carrier-to-check-swr.md)
- [Switch TX profiles (e.g. SSB, Digital)](switch-tx-profiles-e-g-ssb-digital.md)
- [Make your first QSO with AetherSDR](../../getting-started/tutorials/first-qso.md)
