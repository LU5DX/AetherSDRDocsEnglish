# Toggle MOX to manually key the transmitter

MOX lets you key the transmitter without a footswitch or PTT line. Use it to check audio, test your signal, or transmit when hardware PTT is unavailable.

## Before you start

- AetherSDR must be connected to the radio. MOX has no effect when the radio is offline.
- Confirm your TX profile and RF Power level are set correctly before keying.
- In v0.9.7, if you have Quindar tones enabled in the Audio Channel Strip, the K and BK tones will play automatically when you engage and disengage MOX on phone modes. No additional configuration is required.

## Steps

1. If the TX Controls applet is not visible, click the **TX** tray button on the right sidebar to show it.
2. Locate the **MOX** button in the button row alongside TUNE, ATU, and MEM.
3. Click **MOX** to key the transmitter. The button turns red while TX is active.
4. Click **MOX** again to unkey the transmitter. The button returns to its unlit state.

## What each control does

| Control          | Behavior                                                                                                                                                                                      | Default |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| **MOX**          | Toggles manual transmit on or off. Button goes red while the transmitter is keyed. In v0.9.7, the click routes through the Quindar-tone coordinator so K/BK tones play on engage/disengage in phone modes when Quindar is enabled in the Audio Channel Strip. | Off     |
| **RF Power**     | Sets the transmit RF power level sent to the radio.                                                                                                                                           | 100     |
| **RF Pwr** meter | Displays forward power at the exciter output. Turns red above 100 W (barefoot) or 500 W (Aurora 500W).                                                                                        | —       |
| **SWR** meter    | Displays standing wave ratio at the exciter. Turns red above 2.5.                                                                                                                             | —       |

## ATU button behavior

Starting in v0.9.5.1, the **ATU** button toggles between starting a tune cycle and bypassing the tuner, matching the per-frequency behavior of SmartSDR.

The button follows this logic each time you click it:

- **First click on a new frequency** — starts an ATU tune cycle.
- **Second click at the same frequency, after a successful tune** — switches the ATU to bypass.
- **Any click after a frequency change** — starts a fresh tune cycle, even if the previous tune was successful.

Entering bypass clears the remembered tuned frequency, so the next click always starts a fresh tune cycle.

The **ATU** and **MEM** buttons are disabled when TGXL is in OPERATE mode.

## Tips

- Watch the **RF Pwr** and **SWR** meters as soon as you key MOX. If SWR exceeds 2.5 (red zone), unkey immediately and investigate your antenna system.
- Set **RF Power** to a low value before using MOX for the first time on a new band.
- MOX keys the radio into full-power transmit in whatever mode is active. If you only need to check SWR or tune an ATU, use **TUNE** instead — it transmits a carrier at the lower **Tune Pwr** level.
- After a successful ATU tune, clicking **ATU** again on the same frequency puts the tuner into bypass. To re-tune after changing bands or frequencies, simply click **ATU** once on the new frequency.
- If Quindar tones are enabled in the Audio Channel Strip, switching to a digital or CW mode suppresses the K/BK tones automatically. MOX itself behaves the same regardless of mode.

## Troubleshooting

- **MOX button is unresponsive** — Confirm AetherSDR is connected to the radio. The TX Controls applet requires an active radio connection.
- **Transmitter keys but no RF power is shown** — Check that **RF Power** is not set to 0 and that the correct TX profile is loaded in the **TX Profile** selector.
- **Radio stays in transmit after clicking MOX a second time** — Another PTT source (footswitch, VOX, CAT command) may be holding the radio keyed. Check external PTT hardware and any connected CAT clients.
- **ATU button starts a new tune instead of bypassing** — The transmit frequency has changed since the last successful tune. The ATU button will always start a fresh tune cycle when the frequency differs from the frequency at which the tuner last reported a successful match.
- **Quindar tones do not play when clicking MOX** — Confirm that the QUIN chip is enabled in the Audio Channel Strip and that the active TX slice is on a phone mode (SSB, AM, FM). Quindar tones are not generated on CW or digital modes.

## Related

- [TX Controls overview](overview.md)
- [Start a tune carrier to check SWR](start-a-tune-carrier-to-check-swr.md)
- [Set RF output power](set-rf-output-power.md)
- [Run the internal ATU](run-the-internal-atu.md)
- [Make your first QSO with AetherSDR](../../getting-started/tutorials/first-qso.md)