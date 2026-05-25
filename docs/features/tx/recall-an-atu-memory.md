# Recall an ATU Memory

Use ATU memory recall to apply a previously stored tuner solution for the current band or frequency, skipping a full retune cycle.

## Before you start

- AetherSDR must be connected to the radio. The TX Controls applet requires an active radio connection.
- The radio's internal ATU must have stored at least one memory from a prior tuning cycle. If no memory exists for the current frequency, recalling one will have no effect.
- MEM is disabled when the TGXL is in OPERATE mode.

## Steps

1. Open the TX Controls applet. If it is not visible, click the **TX** tray button on the right sidebar.
2. Click **MEM** to toggle ATU memory recall on.
3. Confirm the **Mem** indicator lights green. A green **Mem** indicator confirms the ATU is actively using a stored memory.
4. To stop using the stored memory, click **MEM** again. The **Mem** indicator returns to dim.

## What each control does

| Control | Kind | Behavior |
|---------|------|----------|
| RF Pwr | Meter | Displays forward power at the exciter output. Scale changes based on radio model (0–120 W barefoot, 0–600 W with Aurora 500W exciter). Red above 100 W / 500 W. Includes a peak-hold bar that tracks PEP for 2 seconds, then decays smoothly. |
| SWR | Meter | Displays standing wave ratio at the exciter. Range 1.0–3.0, red above 2.5. |
| RF Power | Slider | Sets transmit RF power level (0–100 W). Shows the current value in watts while dragging. |
| Tune Pwr | Slider | Sets tune-carrier power level (0–100 W). Shows the current value in watts while dragging. |
| TX Profile | Combo box | Selects a TX profile from the radio's profile list. Selecting loads the profile immediately. |
| Success | Indicator | Lights green when ATU status is Successful or OK. |
| Byp | Indicator | Lights orange when the ATU is in Bypass or ManualBypass. |
| Mem | Indicator | Lights green when the ATU is using a memory. |
| TUNE | Push button | Starts/stops tune carrier. Text becomes "TUNING..." with red background while active. Right-click picks the carrier shape (Mono Tone / Two Tone) for the next tune cycle. |
| MOX | Toggle button | Toggles manual transmit. Button turns red while TX is keyed. Routes through Quindar-tone coordinator when QUIN chip is enabled in phone modes. |
| ATU | Push button | Starts the internal ATU tuning cycle. If status is Successful/OK at the same frequency, a second click sends bypass instead. Right-click opens pre-tune sweep and Clear ATU Memories actions. Disabled when TGXL is in OPERATE mode. |
| MEM | Toggle button | Toggles ATU memory recall on/off. Disabled when TGXL is in OPERATE mode. |
| APD | Toggle button | Toggles adaptive pre-distortion on the radio. |
| Active | Indicator | Lights green when APD is on and the equalizer is actively applied. |
| Cal | Indicator | Lights green when APD is on and still calibrating. |
| Avail | Indicator | Lights green when APD is on and a calibration is available but not yet applied. |

## ATU button behavior

Starting with v0.9.5.1, the **ATU** button toggles between tuning and bypass on a per-frequency basis, matching the behavior of SmartSDR. Right-click the **ATU** button to access additional ATU management options.

| Situation | Result of clicking ATU |
|-----------|------------------------|
| No prior successful tune, or frequency has changed since the last tune | Starts a fresh ATU tune cycle. |
| ATU status is Successful or OK **and** the transmit frequency has not changed since that tune completed | Switches the ATU to bypass. |
| ATU is in Bypass or ManualBypass | Starts a fresh ATU tune cycle. |

**Key points:**

- The radio remembers the frequency at which the ATU last reported a successful tune. If you change frequency between clicks, the button always starts a new tune cycle rather than bypassing, even if the previous status was Successful or OK.
- After the ATU enters bypass, the stored tuned frequency is cleared. The next click will start a fresh tune cycle regardless of frequency.

## ATU right-click menu

Right-click the **ATU** button to show a context menu with two additional actions, matching SmartSDR Windows:

| Action | Description |
|--------|-------------|
| **Pre-tune bands…** | Opens a dialog to run a pre-tune sweep across selected bands. This action is only available when ATU memory recall (MEM) is enabled. If MEM is off, the action is greyed out with a tooltip suggesting you enable MEM first. |
| **Clear ATU memories…** | Prompts for confirmation, then clears all stored ATU memories on the radio. |

## MOX and Quindar tones

Clicking **MOX** routes through the Quindar-tone coordinator rather than directly toggling transmit. When the QUIN chip is enabled in the Audio Channel Strip and the active TX slice is on a phone mode, the K tone plays on PTT engage and the BK tone plays on PTT disengage. When Quindar is disabled or the active TX slice is not on a phone mode, the behavior is identical to previous versions.

No additional configuration is required in the TX Controls applet. Enable or disable Quindar tones from the Audio Channel Strip's QUIN control.

## TUNE right-click menu

Right-click the **TUNE** button to set the carrier shape for the next tune cycle. This is a one-shot selection — the radio's tune mode is stored in volatile state and is not persisted across power cycles or saved in AetherSDR settings.

| Menu option | Description |
|-------------|-------------|
| **Mono Tone** | Sets the tune carrier to a single tone. This is the default behavior. |
| **Two Tone** | Sets the tune carrier to a two-tone pattern. |

The currently active tune mode is shown with a check mark. Selecting an option immediately applies it for the next TUNE press.

## Forward power peak-hold meter

The **RF Pwr** meter includes a peak-hold bar that tracks the peak envelope power (PEP). The peak value holds for 2 seconds, then decays smoothly toward the current power level. The decay rate is scaled to the gauge's full-scale range (120 W barefoot or 600 W with Aurora 500W exciter), so the visual feel remains consistent.

- The peak-hold value resets to zero immediately when the radio un-keys, preventing a held PEP reading from lingering across overs.
- The peak-hold behavior matches SmartSDR's peak-hold bar and the RX S-meter peak-hold pattern.

## Slider wattage display

The **RF Power** and **Tune Pwr** sliders now display the current value in watts (e.g., "25 W") while you drag the slider handle. This provides precise visual feedback when setting power levels.

## Tips

- If **Byp** lights orange after enabling **MEM**, the ATU has fallen back to bypass. Run a fresh tune cycle with **ATU** to build a new memory for the current frequency.
- The **Mem** indicator and the **Success** indicator can both be lit at the same time; **Mem** confirms a memory is in use, while **Success** confirms the stored solution is valid.
- To bypass the ATU without running a new tune cycle, click **ATU** a second time at the same frequency where the last successful tune occurred. The **Byp** indicator will light orange to confirm bypass is active.
- To clear ATU memories across all bands, right-click **ATU** and select **Clear ATU memories…**. Use **Pre-tune bands…** to rebuild memories for frequently used bands.

## Troubleshooting

- **MEM button is greyed out and cannot be clicked** — The TGXL is in OPERATE mode. Memory recall cannot be toggled in this mode. Check the TGXL operating mode before proceeding.
- **Mem indicator stays dim after clicking MEM** — No stored ATU memory exists for the current frequency. Run a full ATU tune cycle first using **ATU**, then try **MEM** again.
- **Byp lights orange instead of Mem going green** — The ATU has entered bypass because no usable memory was found. Use **ATU** to tune and store a new solution.
- **ATU button starts a new tune instead of bypassing** — The transmit frequency changed since the last successful tune. The button will not bypass until you are back on the exact frequency that was tuned. Tune again at the current frequency first.
- **MOX engages but no Quindar tones play** — Confirm that the QUIN chip is enabled in the Audio Channel Strip and that the active TX slice is set to a phone mode. Quindar tones do not play on CW or digital modes.
- **Pre-tune bands… is greyed out** — Enable MEM first by clicking the **MEM** button. The pre-tune sweep requires memory recall to be active.

## Related

- [Run the internal ATU](run-the-internal-atu.md)
- [Start a tune carrier to check SWR](start-a-tune-carrier-to-check-swr.md)
- [TX Controls overview](overview.md)