# Recall an ATU memory

ATU memory recall lets the radio apply a previously stored tuner setting the moment you change to a frequency that matches a saved memory, avoiding a full retune on bands where the ATU has already found a good match.

## Before you start

- AetherSDR must be connected to the radio. TX Controls are unavailable without a radio connection.
- The radio's ATU must have at least one stored memory. Run a full ATU tune first if no memories exist.
- The TX tray button in the right sidebar must be active so the TX Controls applet is visible.

## Steps

1. Click the TX tray button on the right sidebar to open the TX Controls applet (if it is not already visible).
2. Click MEM in the TUNE / MOX / ATU / MEM button row.
   - MEM is a toggle button. When memory recall is on, the button state changes to checked.
   - The Mem indicator in the profile row lights green when the ATU is actively using a stored memory on the current frequency.
3. To turn memory recall off, click MEM again.

## What each control does

| Control | Kind | Behavior | Notes |
|---------|------|----------|-------|
| MEM | Toggle button | Toggles ATU memory recall on/off. When on, the radio applies a stored ATU setting for the current frequency instead of retuning. | Disabled when TGXL is in OPERATE mode. |
| Mem | Indicator | Lights green when the ATU is actively using a memory. Dim when no memory is in use. | Reflects ATU status reported by the radio. |
| Success | Indicator | Lights green when ATU status is Successful or OK. | |
| Byp | Indicator | Lights orange when the ATU is in Bypass or ManualBypass. | |

## Troubleshooting

- **MEM is greyed out and cannot be clicked** — The TGXL is in OPERATE mode. MEM is disabled in this state. Switch the TGXL out of OPERATE mode before enabling memory recall.
- **Mem indicator stays dim after enabling MEM** — No stored ATU memory exists for the current frequency. Use ATU to run a full tune cycle on this frequency first, which will store a new memory.

## Related

- [Run the internal ATU](run-the-internal-atu.md)
- [Start a tune carrier to check SWR](start-a-tune-carrier-to-check-swr.md)
- [TX Controls overview](overview.md)
