# Toggle MOX to manually key the transmitter

MOX lets you key the transmitter without a PTT input or microphone activity. Use it when you need to hold the radio in transmit — for example, to check SWR, test audio, or send a manual carrier.

## Before you start

- AetherSDR must be connected to the radio. MOX has no effect when the radio is offline.
- Confirm your RF power level is set appropriately before keying. See [Set RF output power](set-rf-output-power.md).

## Steps

1. If the TX Controls applet is not visible, click the TX tray button on the right sidebar to open it.
2. Click MOX.
   - The button turns red and the radio keys immediately.
3. Click MOX again to unkey.
   - The button returns to its default (blue) state and the radio returns to receive.

## What each control does

| Control | Kind | Behavior | Default | Range |
|---|---|---|---|---|
| MOX | Toggle button | Keys or unkeys the transmitter manually. Red while transmit is active. | Off (blue) | Off / On (red) |
| RF Pwr | Meter | Displays forward power at the exciter output while transmitting. | — | 0–120 W; red above 100 W (barefoot) / 0–600 W; red above 500 W (Aurora 500W) |
| SWR | Meter | Displays standing wave ratio at the exciter while transmitting. | — | 1.0–3.0; red above 2.5 |

## Tips

- Watch the RF Pwr and SWR meters while MOX is active. If SWR reads red (above 2.5), unkey and address the antenna system before continuing.
- MOX and TUNE are independent controls. TUNE sends a constant carrier at the Tune Pwr level; MOX keys the radio at the RF Power level using your active mode and audio.

## Troubleshooting

- **MOX button is visible but the radio does not key** — Confirm AetherSDR is connected to the radio. The applet requires an active radio connection.
- **Radio stays keyed after clicking MOX a second time** — The button state may have lost sync with the radio. Click MOX once more to force a toggle, or cycle the connection.

## Related

- [Start a tune carrier to check SWR](start-a-tune-carrier-to-check-swr.md)
- [Set RF output power](set-rf-output-power.md)
- [Run the internal ATU](run-the-internal-atu.md)
- [TX Controls overview](overview.md)
