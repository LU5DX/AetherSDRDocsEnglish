# Toggle MOX to manually key the transmitter

MOX lets you key the transmitter without using a microphone PTT or footswitch. Use it to hold the radio in transmit for testing, adjusting audio, or any situation where you need manual TX control.

## Before you start

- AetherSDR must be connected to the radio. MOX requires a live radio connection.
- Open the TX Controls applet. If it is not visible, click the TX tray button in the right sidebar.

## Steps

1. In the TX Controls applet, locate the row of four buttons: TUNE, MOX, ATU, MEM.
2. Click MOX.
3. The button turns red and the radio keys the transmitter.
4. Click MOX again to unkey. The button returns to its default (blue) appearance and the radio returns to receive.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| MOX | Toggle button | Toggles manual transmit on and off. Red while TX is keyed; blue (off) while in receive. |
| RF Pwr | Meter | Displays forward power at the exciter output. Scale: 0–120 W (barefoot); red above 100 W. Aurora 500W model: 0–600 W, red above 500 W. |
| SWR | Meter | Displays standing wave ratio at the exciter. Scale: 1.0–3.0; red above 2.5. |
| RF Power | Slider | Sets transmit RF power level. Default: 100. Range: 0–100. |

## Tips

- Watch the RF Pwr and SWR meters while MOX is active to confirm the radio is transmitting and the antenna system is within acceptable limits.
- MOX and TUNE are independent controls. If a tune carrier is already running (TUNE shows "TUNING..."), stop it before using MOX.

## Troubleshooting

- **MOX button does not respond** — The TX Controls applet requires an active radio connection. Check that AetherSDR is connected to the FLEX-8600 via `Settings > Connect to Radio...`.
- **Radio transmits but RF Pwr reads zero** — Verify the RF Power slider is not set to 0.

## Related

- [TX Controls overview](overview.md)
- [Set RF output power](set-rf-output-power.md)
- [Start a tune carrier to check SWR](start-a-tune-carrier-to-check-swr.md)
- [Make your first QSO with AetherSDR](../../getting-started/tutorials/first-qso.md)
