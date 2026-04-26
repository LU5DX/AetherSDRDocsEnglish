# Recall an ATU Memory

The ATU memory feature lets the radio recall a previously stored tuning solution for the current frequency, skipping a full retune. Use this when you return to a band or frequency you have tuned before and want the tuner to apply the stored match immediately.

## Before you start

- AetherSDR must be connected to the radio. The TX Controls applet requires an active radio connection.
- The internal ATU must have previously completed a successful tune on or near the target frequency, so a stored memory exists.
- The TX tray button must be enabled so the TX Controls applet is visible in the Applet Panel.

## Steps

1. Open the TX Controls applet. Click the **TX** tray button on the right sidebar if the applet is not already visible.
2. Click **MEM** to toggle ATU memory recall on.
3. Check the **Mem** indicator. It lights green when the ATU is actively using a stored memory for the current frequency.

To turn memory recall off, click **MEM** again. The **Mem** indicator returns to dim.

## What each control does

| Control | Kind | Behavior | Default |
|---|---|---|---|
| **MEM** | Toggle button | Toggles ATU memory recall on or off. Disabled when TGXL is in OPERATE mode. | Off |
| **Mem** | Indicator | Lights green when the ATU is using a stored memory. Dim when memory recall is off or no memory applies. | Dim |
| **Success** | Indicator | Lights green when ATU status is Successful or OK. | Dim |
| **Byp** | Indicator | Lights orange when the ATU is in Bypass or ManualBypass. | Dim |

## Tips

- If **Mem** does not light after enabling **MEM**, no stored memory exists for the current frequency. Run the ATU first using the **ATU** button, then enable **MEM** on your next visit to that frequency.
- **MEM** and **ATU** are both disabled when TGXL is in OPERATE mode. If either button is greyed out, check your TGXL mode.

## Troubleshooting

- **MEM button is greyed out** — The TGXL is in OPERATE mode. ATU memory recall is not available in this mode. Switch the TGXL out of OPERATE mode to re-enable the control.
- **Mem indicator stays dim after enabling MEM** — No ATU memory exists for the current frequency. Run a full ATU tune with **ATU**, then toggle **MEM** on.

## Related

- [Run the internal ATU](run-the-internal-atu.md)
- [Start a tune carrier to check SWR](start-a-tune-carrier-to-check-swr.md)
- [TX Controls overview](overview.md)
