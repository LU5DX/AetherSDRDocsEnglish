# Toggle MOX to manually key the transmitter

MOX lets you key the transmitter without a footswitch or PTT line. Use it to check audio, test your signal, or transmit when hardware PTT is unavailable.

## Before you start

- AetherSDR must be connected to the radio. MOX has no effect when the radio is offline.
- Confirm your TX profile and RF Power level are set correctly before keying.

## Steps

1. If the TX Controls applet is not visible, click the **TX** tray button on the right sidebar to show it.
2. Locate the **MOX** button in the button row alongside TUNE, ATU, and MEM.
3. Click **MOX** to key the transmitter. The button turns red while TX is active.
4. Click **MOX** again to unkey the transmitter. The button returns to its unlit state.

## What each control does

| Control | Behavior | Default | Range |
|---------|----------|---------|-------|
| **MOX** | Toggles manual transmit on or off. Button goes red while the transmitter is keyed. | Off | Off / On (red) |
| **RF Power** | Sets the transmit RF power level sent to the radio. | 100 | 0–100 |
| **RF Pwr** meter | Displays forward power at the exciter output. Turns red above 100 W (barefoot) or 500 W (Aurora 500W). | — | 0–120 W / 0–600 W |
| **SWR** meter | Displays standing wave ratio at the exciter. Turns red above 2.5. | — | 1.0–3.0 |

## Tips

- Watch the **RF Pwr** and **SWR** meters as soon as you key MOX. If SWR exceeds 2.5 (red zone), unkey immediately and investigate your antenna system.
- Set **RF Power** to a low value before using MOX for the first time on a new band.
- MOX keys the radio into full-power transmit in whatever mode is active. If you only need to check SWR or tune an ATU, use **TUNE** instead — it transmits a carrier at the lower **Tune Pwr** level.

## Troubleshooting

- **MOX button is unresponsive** — Confirm AetherSDR is connected to the radio. The TX Controls applet requires an active radio connection.
- **Transmitter keys but no RF power is shown** — Check that **RF Power** is not set to 0 and that the correct TX profile is loaded in the **TX Profile** selector.
- **Radio stays in transmit after clicking MOX a second time** — Another PTT source (footswitch, VOX, CAT command) may be holding the radio keyed. Check external PTT hardware and any connected CAT clients.

## Related

- [TX Controls overview](overview.md)
- [Start a tune carrier to check SWR](start-a-tune-carrier-to-check-swr.md)
- [Set RF output power](set-rf-output-power.md)
- [Run the internal ATU](run-the-internal-atu.md)
- [Make your first QSO with AetherSDR](../../getting-started/tutorials/first-qso.md)
