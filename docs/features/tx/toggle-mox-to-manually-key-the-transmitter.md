# Toggle MOX to manually key the transmitter

MOX lets you key the transmitter manually, without a footswitch or PTT line. Use it when you need continuous carrier for testing, net check-ins, or any situation where you want direct software control of TX.

## Before you start

- Connect to a FLEX-8600 radio. MOX requires an active radio connection.
- Open the TX Controls applet. Click the TX tray button on the right sidebar, or confirm the applet is already visible in the Applet Panel.

## Steps

1. In the TX Controls applet, locate the row containing TUNE, MOX, ATU, and MEM.
2. Click MOX to key the transmitter. The button turns red to confirm TX is active.
3. Click MOX again to return to receive. The button returns to its default (blue off) state.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| MOX | Toggle button | Toggles manual transmit. Red when TX is keyed; blue (off) when in receive. |
| RF Pwr | Meter | Displays forward power at the exciter output. Scale: 0–120 W (barefoot); red above 100 W. |
| SWR | Meter | Displays standing wave ratio. Red above 2.5. |

## Tips

- Watch the RF Pwr and SWR meters while MOX is active to confirm expected output and a safe SWR.
- MOX keys the transmitter regardless of mode. Make sure your microphone, keyer, or audio source is configured before engaging MOX on a live frequency.
- To transmit a clean carrier for SWR checks, use TUNE with the Tune Pwr slider instead of MOX. See [Start a tune carrier to check SWR](start-a-tune-carrier-to-check-swr.md).

## Troubleshooting

- **MOX button does not respond** — The radio connection may be inactive. Check the connection status and reconnect via `Settings > Connect to Radio...`.
- **MOX activates but RF Pwr reads zero** — RF Power slider may be set to 0. Increase the RF Power slider before keying.
- **MOX stays red after clicking** — A SmartSDR protocol update from the radio may be holding TX state. Click MOX once more to toggle off; if the button remains red, check for a stuck PTT source on the radio.

## Related

- [TX Controls overview](overview.md)
- [Start a tune carrier to check SWR](start-a-tune-carrier-to-check-swr.md)
- [Set RF output power](set-rf-output-power.md)
- [Make your first QSO with AetherSDR](../../getting-started/tutorials/first-qso.md)
