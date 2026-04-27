# Recall an ATU Memory

Use ATU memory recall to apply a previously stored tuner solution for the current band or frequency, skipping a full retune cycle.

## Before you start

- AetherSDR must be connected to the radio. The TX Controls applet requires an active radio connection.
- The radio's internal ATU must have stored at least one memory from a prior tuning cycle. If no memory exists for the current frequency, recalling one will have no effect.
- MEM is disabled when the TGXL is in OPERATE mode.

## Steps

1. Open the TX Controls applet. If it is not visible, click the **TX** tray button on the right sidebar.
2. Click **MEM** to toggle ATU memory recall on.
3. Confirm the **Mem** indicator lights green. A green **Mem** indicator confirms the ATU is actively using a stored memory.
4. To stop using the stored memory, click **MEM** again. The **Mem** indicator returns to dim.

## What each control does

| Control | Kind | Behavior | Default |
|---|---|---|---|
| MEM | Toggle button | Toggles ATU memory recall on/off. When on, the radio applies a stored tuner solution rather than running a new tune cycle. Disabled when TGXL is in OPERATE mode. | Off |
| Mem | Indicator | Lights green when the ATU is using a memory. Dim when memory recall is off or no memory is in use. | Dim |
| Success | Indicator | Lights green when ATU status is Successful or OK. | Dim |
| Byp | Indicator | Lights orange when the ATU is in Bypass or ManualBypass. | Dim |

## Tips

- If **Byp** lights orange after enabling **MEM**, the ATU has fallen back to bypass. Run a fresh tune cycle with **ATU** to build a new memory for the current frequency.
- The **Mem** indicator and the **Success** indicator can both be lit at the same time; **Mem** confirms a memory is in use, while **Success** confirms the stored solution is valid.

## Troubleshooting

- **MEM button is greyed out and cannot be clicked** — The TGXL is in OPERATE mode. Memory recall cannot be toggled in this mode. Check the TGXL operating mode before proceeding.
- **Mem indicator stays dim after clicking MEM** — No stored ATU memory exists for the current frequency. Run a full ATU tune cycle first using **ATU**, then try **MEM** again.
- **Byp lights orange instead of Mem going green** — The ATU has entered bypass because no usable memory was found. Use **ATU** to tune and store a new solution.

## Related

- [Run the internal ATU](run-the-internal-atu.md)
- [Start a tune carrier to check SWR](start-a-tune-carrier-to-check-swr.md)
- [TX Controls overview](overview.md)
