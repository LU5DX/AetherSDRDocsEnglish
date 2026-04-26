# Recall an ATU memory

Use the MEM toggle to enable ATU memory recall, which lets the radio apply a previously stored tuner solution for the current frequency instead of running a full tune cycle.

## Before you start

- AetherSDR must be connected to the radio. MEM is unavailable without an active radio connection.
- A stored ATU memory must exist for the current frequency. Run a full ATU tune first if none is available.
- The TX applet must be visible. If it is not, click the TX tray button in the right sidebar to show it.
- MEM is disabled when the TGXL is in OPERATE mode. Ensure the TGXL is not in OPERATE mode before proceeding.

## Steps

1. Open the TX applet by clicking the TX tray button in the right sidebar if it is not already visible.
2. Click MEM in the TUNE / MOX / ATU / MEM button row.
3. Confirm that the Mem indicator lights green. This confirms the ATU is actively using a stored memory for the current frequency.

## What each control does

| Control | Kind | Behavior | Default |
|---|---|---|---|
| MEM | Toggle button | Toggles ATU memory recall on or off. When on, the radio applies a stored tuner solution for the current frequency. | Off |
| Mem | Indicator | Lights green when the ATU is using a memory. Dim when memory recall is off or no memory applies. | Dim |
| Success | Indicator | Lights green when ATU status is Successful or OK. | Dim |
| Byp | Indicator | Lights orange when ATU is in Bypass or ManualBypass. | Dim |

## Tips

- If the Mem indicator does not light after clicking MEM, no stored ATU memory exists for the current frequency. Click ATU to run a full tune cycle and store a new memory, then click MEM again.
- Clicking MEM a second time toggles memory recall off. The button returns to its unlit state and the Mem indicator goes dim.

## Troubleshooting

- **MEM button is greyed out and cannot be clicked** — The TGXL is in OPERATE mode. ATU memory recall is disabled in this mode. Check your TGXL configuration.
- **Mem indicator stays dim after clicking MEM** — No stored ATU memory exists for the current frequency. Run an ATU tune cycle first using the ATU button, then re-enable MEM.
- **Byp indicator lights instead of Mem** — The ATU has fallen back to bypass. This can happen if the stored memory is no longer valid for current antenna conditions. Run a new tune cycle.

## Related

- [Run the internal ATU](run-the-internal-atu.md)
- [Start a tune carrier to check SWR](start-a-tune-carrier-to-check-swr.md)
- [TX Controls overview](overview.md)
