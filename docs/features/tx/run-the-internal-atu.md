# TX Controls overview

*Introduced in v0.9.0. Updated for v26.8.4.*

The TX Controls applet provides all transmit-related controls: forward power and SWR meters, RF/Tune power sliders, TX profile selector, and TUNE/MOX/ATU/MEM buttons. It also includes the APD (Adaptive Pre-Distortion) toggle with Active/Cal/Avail status indicators.

## Opening the TX Controls applet

1. Click the TX tray button (TX icon) in the right sidebar of the main window.
2. The TX Controls applet opens as a floating panel.

## Forward power and SWR meters

The forward power meter displays the output power at the exciter. A peak-hold bar tracks the peak envelope power (PEP) on each transmission with a 2-second hold and gradual decay back to the current smoothed power level. The peak-hold resets to zero immediately when the transmitter is un-keyed.

Hover the mouse cursor over the forward power meter to display the exact value in watts (e.g., "34 W"). This readout is useful for reading precise power levels between the 40 W tick marks during transmission.

The SWR meter displays the standing wave ratio at the exciter output.

Hover the mouse cursor over the SWR meter to display the exact ratio in the conventional N.N:1 form (e.g., "1.88:1").

The forward power meter automatically scales based on the connected radio model:
- Barefoot FlexRadio: 0–120 W (red zone above 100 W)
- With Aurora 500W amplifier: 0–600 W (red zone above 500 W)

Both meters clear immediately when the transmitter is un-keyed: the forward power gauge returns to zero and the SWR gauge returns to its 1.0 rest position. This prevents stale readings from lingering after a transmission ends.

## RF Power and Tune Pwr sliders

| Control | Default | Range | Behavior |
|---|---|---|---|
| RF Power | 100 | 0–100 | Sets the transmit RF power level as a percentage of maximum. When dragging the slider handle, a tooltip shows the value in percent (e.g., "75%"). Releasing the slider handle syncs the final value from the model. |
| Tune Pwr | 10 | 0–100 | Sets the tune-carrier power level for tuning operations as a percentage of maximum. When dragging the slider handle, a tooltip shows the value in percent (e.g., "25%"). Releasing the slider handle syncs the final value from the model. |

Both sliders display a tooltip showing the current value in percent while you drag the handle. The tooltip appears next to the slider handle and updates in real time as you adjust the value. The slider fill color follows the selected theme.

When you release the slider handle, the value is synced from the model to ensure consistency. This prevents the slider from reporting a different value than what the radio is actually using.

## TX Profile selector

The TX Profile combo box lists all TX profiles stored on the radio. Selecting a profile loads it onto the active slice.

## Transmit control buttons

| Button | Type | Behavior |
|---|---|---|
| TUNE | Push button | Starts/stops a tune carrier. Button text changes to "TUNING..." with red background while active. Right-click to select carrier shape. |
| MOX | Toggle button | Toggles manual transmit. Button turns red while transmitting. Routes through Quindar-tone coordinator when QUIN chip is enabled. In idle state, MOX has an amber accent (border and text) to visually distinguish it from the neutral TUNE/ATU/MEM buttons. This accent is editable in the Theme Editor using the `color.tx.mox.*` tokens. |
| ATU | Push button | Starts the internal ATU tuning cycle. Disabled on radios without a tuner or when the TGXL is in OPERATE mode. Right-click for pre-tune and memory management options. |
| MEM | Toggle button | Toggles ATU memory recall on/off. Disabled on radios without a tuner or when the TGXL is in OPERATE mode. |

## TUNE button right-click menu

Right-click the TUNE button to select the carrier shape for the next tune cycle. This is a one-shot setting — the choice is not persisted across power cycles.

Available options:
- **Mono Tone** — Single tone carrier
- **Two Tone** — Two-tone carrier for intermodulation distortion testing

The current selection shows a check mark next to the active option.

## ATU button right-click menu

Right-click the ATU button to access additional tuning features. The menu appears when MEM is enabled.

Available options:
- **Pre-tune bands…** — Opens the pre-tune sweep dialog to run tuning sweeps across multiple bands (requires MEM enabled)
- **Clear ATU memories…** — Clears all stored ATU memories after confirmation

## ATU button behavior

The ATU button toggles between starting a tune cycle and switching the tuner into bypass, depending on the current ATU status and transmit frequency.

| Situation | What ATU click does |
|---|---|
| No previous tune on this frequency, or ATU is not in a Successful/OK state | Starts a fresh ATU tune cycle |
| ATU status is Successful or OK, and TX frequency has not changed since the last tune | Switches the ATU into bypass |
| ATU status is Successful or OK, but TX frequency has changed since the last tune | Starts a fresh ATU tune cycle |

In practice:
- The first click on a new frequency always starts a tune cycle.
- After a successful tune, clicking ATU again on the same frequency bypasses the tuner.
- Changing frequency resets the toggle, so the next click starts a fresh tune cycle regardless of the previous status.
- Entering bypass clears the stored tuned frequency, so the next click always starts a fresh tune.

When the ATU and MEM buttons are disabled, hovering over either button shows the reason:
- **This radio has no antenna tuner** — The connected radio model has no ATU hardware.
- **Disabled — TGXL is in OPERATE mode** — The TGXL external tuner is in OPERATE mode.

## ATU status indicators

| Indicator | Color | Meaning |
|---|---|---|
| Success | Green | ATU tuning result is successful or OK |
| Byp | Orange | ATU is in Bypass or ManualBypass |
| Mem | Green | ATU is using a stored memory |

## APD (Adaptive Pre-Distortion) controls

The APD toggle button enables or disables adaptive pre-distortion on the radio. When enabled, three status indicators show the calibration progression.

| Control/Indicator | Type | Behavior |
|---|---|---|
| APD | Toggle button | Toggles adaptive pre-distortion on/off |
| Active | Indicator (green) | Lit when APD is on and the equalizer is actively applied |
| Cal | Indicator (green) | Lit when APD is on and still calibrating |
| Avail | Indicator (green) | Lit when APD is on and a calibration is available but not yet applied |

The APD status indicators follow this progression: Cal (calibrating) → Avail (ready) → Active (applied).

The APD row is hidden entirely when the connected radio does not support adaptive pre-distortion, so a live-looking APD button never appears with no function behind it.

## MOX and Quindar tones

Starting in v0.9.7, clicking MOX routes through the Quindar-tone coordinator rather than toggling transmit directly. When the QUIN chip is enabled in the Audio Channel Strip and the active TX slice is on a phone mode, clicking MOX to engage transmit plays the K tone and clicking it again to disengage plays the BK tone. When Quindar is disabled or the active TX slice is not on a phone mode, MOX behaves as before and toggles transmit directly.

## Tips

- The forward power peak-hold bar helps you monitor PEP during voice transmission. The 2-second hold gives you time to read the value, and the gradual decay prevents distracting jumps.
- Hover over the forward power meter to read the exact wattage, which is especially helpful when fine-tuning between the 40 W tick marks.
- Hover over the SWR meter to see the exact ratio in the conventional N.N:1 form, making precise SWR adjustments easier.
- Use the TUNE button right-click menu to select a two-tone carrier for intermodulation distortion testing when working with external amplifiers.
- The ATU right-click menu provides access to pre-tuning multiple bands at once, saving time during band changes.
- If Byp lights after the tuning cycle, the ATU was unable to find a match and has bypassed itself. Check your antenna system and SWR before transmitting at full power.
- If Mem lights, the ATU applied a previously stored tuning memory rather than running a full tune. This is normal when MEM is enabled and a valid memory exists for the current frequency.
- To manually force the tuner into bypass after a successful tune, click ATU a second time without changing frequency.
- When adjusting the RF Power or Tune Pwr sliders, the tooltip that appears while dragging shows the exact value in percent, making fine adjustments easier. Release the slider handle to sync the final value with the radio.
- The MOX button's amber accent (border and text) when idle visually distinguishes it from the other buttons, confirming you are about to key the transmitter. This accent can be customized in the Theme Editor using the `color.tx.mox.*` tokens.

## Troubleshooting

- **ATU button is unresponsive** — The radio's TGXL is in OPERATE mode, or the radio has no ATU hardware. Hover over the ATU button to see which reason applies. Switch the TGXL out of OPERATE mode before attempting to tune, or use an external tuner if the radio has none.
- **Success indicator does not light after tuning** — The ATU may have bypassed (check Byp) or the tune-carrier power may be too low for the ATU to work with your antenna. Increase Tune Pwr and try again.
- **Clicking ATU bypasses instead of tuning** — The ATU status is Successful or OK and the TX frequency has not changed since the last tune. This is the expected second-click bypass behavior. Change frequency to force a fresh tune cycle, or leave the tuner in its current matched state.
- **Quindar tones do not play on MOX** — Confirm that the QUIN chip is enabled in the Audio Channel Strip and that the active TX slice is set to a phone mode. Quindar tones are not played on CW or digital modes.
- **TUNE button right-click menu is unresponsive** — The radio may not be connected or the TX controls may be in a transitional state. Ensure the radio is connected and try again.
- **Power or SWR meter shows a stale reading after un-keying** — The meters are designed to clear immediately when the transmitter is un-keyed. If a reading persists, this indicates a firmware or connection issue. Reconnect the radio and try again.

## Related

- [Recall an ATU memory](recall-an-atu-memory.md)
- [Start a tune carrier to check SWR](start-a-tune-carrier-to-check-swr.md)
- [Set tune-carrier power](set-tune-carrier-power.md)
- Run a pre-tune sweep
- Clear ATU memories