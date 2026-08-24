# Toggle MOX to manually key the transmitter

MOX lets you key the transmitter without a footswitch or PTT line. Use it to check audio, test your signal, or transmit when hardware PTT is unavailable.

## Before you start

- AetherSDR must be connected to the radio. MOX has no effect when the radio is offline.
- Confirm your TX profile and RF Power level are set correctly before keying.
- If you have Quindar tones enabled in the Audio Channel Strip, the K and BK tones will play automatically when you engage and disengage MOX on phone modes. No additional configuration is required.

## Steps

1. If the TX Controls applet is not visible, click the **TX** tray button on the right sidebar to show it.
2. Locate the **MOX** button in the button row alongside TUNE, ATU, and MEM.
3. Click **MOX** to key the transmitter. The button turns red while TX is active.
4. Click **MOX** again to unkey the transmitter. The button returns to its idle state with an amber accent border and text, distinguishing it from the TUNE, ATU, and MEM buttons.

## What each control does

| Control                                        | Behavior                                                                                                                                                                                                                                                                       | Default |
|------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| **MOX**                                        | Toggles manual transmit on or off. Button turns red while the transmitter is keyed. In the idle state, the button has an amber accent border and text to distinguish it from the TUNE, ATU, and MEM neighbors. Click routes through the Quindar-tone coordinator so K/BK tones play on engage/disengage in phone modes when Quindar is enabled in the Audio Channel Strip. | Off     |
| **RF Power**                                   | Sets the transmit RF power level sent to the radio (0–100% of maximum). While dragging the slider handle, a tooltip shows the current value in percent (e.g., "50%"). Releasing the slider handle syncs the value back to the radio.                                            | 100     |
| **Tune Pwr**                                   | Sets the tune-carrier power level (0–100% of maximum). While dragging the slider handle, a tooltip shows the current value in percent (e.g., "10%"). Releasing the slider handle syncs the value back to the radio.                                                             | 10      |
| **RF Pwr** meter                               | Displays forward power at the exciter output. Turns red above 100 W (barefoot) or 500 W (Aurora 500W). Peak-hold bar holds the peak PEP reading for 2 seconds, then decays to the current power level at a rate of 48 W/s (scaled proportionally for the Aurora 500W exciter). Hover your mouse over the gauge to see the exact wattage readout in a popup (e.g., "75 W"). The gauge and peak-hold reset to 0 immediately when you unkey. | —       |
| **SWR** meter                                  | Displays standing wave ratio at the exciter. Turns red above 2.5. Hover your mouse over the gauge to see the exact ratio readout in a popup (e.g., "1.42:1"). The gauge rests at 1.0 when not transmitting or when SWR data is unavailable.                                    | —       |
| **TX Profile**                                 | Selects a TX profile from those loaded on the radio.                                                                                                                                                                                                                           | —       |
| **TUNE**                                       | Starts or stops the tune carrier. Button text becomes **TUNING...** with a red background while active. Right-click to select the carrier shape (Mono Tone or Two Tone) for the next tune cycle. This selection is a one-shot and is not persisted across power cycles.        | TUNE    |
| **ATU**                                        | Starts an ATU tune cycle. Disabled when the radio has no antenna tuner or when TGXL is in OPERATE mode. Right-click to open a context menu with **Pre-tune bands…** and **Clear ATU memories…** options (see ATU button behavior below).                                       | —       |
| **MEM**                                        | Toggles ATU memory recall on or off. Disabled when the radio has no antenna tuner or when TGXL is in OPERATE mode.                                                                                                                                                            | Off     |
| **ATU indicators** (Success, Byp, Mem)         | **Success** lights green when ATU status is Successful or OK. **Byp** lights orange when ATU is in Bypass or ManualBypass. **Mem** lights green when ATU is using a memory.                                                                                                    | Dim     |
| **APD**                                        | Toggles adaptive pre-distortion on the radio.                                                                                                                                                                                                                                  | Off     |
| **APD status indicators** (Active, Cal, Avail) | **Active** lights green when APD is on and the equalizer is actively applied. **Cal** lights green when APD is on and still calibrating. **Avail** lights green when APD is on and a calibration is available but not yet applied.                                             | Dim     |

## ATU button behavior

Starting in v0.9.5.1, the **ATU** button toggles between starting a tune cycle and bypassing the tuner, matching the per-frequency behavior of SmartSDR.

The button follows this logic each time you click it:

- **First click on a new frequency** — starts an ATU tune cycle.
- **Second click at the same frequency, after a successful tune** — switches the ATU to bypass.
- **Any click after a frequency change** — starts a fresh tune cycle, even if the previous tune was successful.

Entering bypass clears the remembered tuned frequency, so the next click always starts a fresh tune cycle.

The **ATU** and **MEM** buttons are disabled when TGXL is in OPERATE mode. They are also disabled entirely when the connected radio has no antenna tuner (for example, a Hermes-Lite 2). When disabled, hovering over either button shows the reason: "This radio has no antenna tuner" or "Disabled — TGXL is in OPERATE mode".

### ATU right-click context menu

Right-clicking the **ATU** button opens a context menu with two options:

- **Pre-tune bands…** — Opens the ATU pre-tune dialog to run a sweep across selected bands. This option is only available when MEM is enabled. If MEM is off, the option is grayed out with a tooltip: "Enable MEM before running the pre-tune sweep."
- **Clear ATU memories…** — Opens a confirmation dialog. Clicking Yes clears all stored ATU memories on the radio.

## TUNE right-click menu

Right-clicking the **TUNE** button opens a context menu to select the carrier shape for the next tune cycle:

- **Mono Tone** — A single tone carrier.
- **Two Tone** — Two-tone test signal.

The selection is a one-shot applied to the next Tune button press only. The radio's tune mode reverts to single tone across power cycles; AetherSDR does not persist this choice in AppSettings.

## Tips

- Watch the **RF Pwr** and **SWR** meters as soon as you key MOX. If SWR exceeds 2.5 (red zone), unkey immediately and investigate your antenna system.
- Set **RF Power** to a low value before using MOX for the first time on a new band.
- MOX keys the radio into full-power transmit in whatever mode is active. If you only need to check SWR or tune an ATU, use **TUNE** instead — it transmits a carrier at the lower **Tune Pwr** level.
- After a successful ATU tune, clicking **ATU** again on the same frequency puts the tuner into bypass. To re-tune after changing bands or frequencies, simply click **ATU** once on the new frequency.
- While dragging the **RF Power** or **Tune Pwr** slider, a tooltip displays the current value in percent to help you set your desired level precisely. The value is synced to the radio when you release the slider handle.
- Hover your mouse over the **RF Pwr** or **SWR** gauge to see an exact readout popup (e.g., "75 W" for power or "1.42:1" for SWR), helping you read precise values without estimating between tick marks.
- If Quindar tones are enabled in the Audio Channel Strip, switching to a digital or CW mode suppresses the K/BK tones automatically. MOX itself behaves the same regardless of mode.
- The peak-hold bar on the **RF Pwr** meter holds the peak reading for 2 seconds, then decays to the current power level. The peak is cleared immediately when you unkey.
- The power and tune power sliders now use theme-aware styling. The slider fill color follows the configured theme's slider foreground color. The text labels use the theme's primary and secondary text colors for better readability across light and dark themes.
- The MOX button idle accent (amber border and text) is editable in the Theme Editor under `color.tx.mox.*`, allowing you to customize its appearance to match your operating setup.

## Troubleshooting

- **MOX button is unresponsive** — Confirm AetherSDR is connected to the radio. The TX Controls applet requires an active radio connection.
- **Transmitter keys but no RF power is shown** — Check that **RF Power** is not set to 0% and that the correct TX profile is loaded in the **TX Profile** selector.
- **Radio stays in transmit after clicking MOX a second time** — Another PTT source (footswitch, VOX, CAT command) may be holding the radio keyed. Check external PTT hardware and any connected CAT clients.
- **ATU button starts a new tune instead of bypassing** — The transmit frequency has changed since the last successful tune. The ATU button will always start a fresh tune cycle when the frequency differs from the frequency at which the tuner last reported a successful match.
- **ATU and MEM buttons are grayed out** — The connected radio may have no internal antenna tuner, or the TGXL may be in OPERATE mode. Hover over either button to see the specific reason displayed as a tooltip.
- **Quindar tones do not play when clicking MOX** — Confirm that the QUIN chip is enabled in the Audio Channel Strip and that the active TX slice is on a phone mode (SSB, AM, FM). Quindar tones are not generated on CW or digital modes.
- **Pre-tune bands option is grayed out** — Enable the **MEM** button first. The pre-tune sweep requires ATU memories to be active.

## Related

- [TX Controls overview](overview.md)
- [Start a tune carrier to check SWR](start-a-tune-carrier-to-check-swr.md)
- [Set RF output power](set-rf-output-power.md)
- [Run the internal ATU](run-the-internal-atu.md)
- [Make your first QSO with AetherSDR](../../getting-started/tutorials/first-qso.md)