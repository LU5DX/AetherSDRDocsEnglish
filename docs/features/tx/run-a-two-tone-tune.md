# Run a Two-Tone Tune

A two-tone tune lets you check transmitter linearity and drive levels by keying the radio manually with MOX while monitoring forward power and SWR. Use this procedure when your rig is in SSB mode and you want to verify output without transmitting audio.

## Before you start

- AetherSDR is connected to the FLEX-8600 (radio indicator shows connected).
- The TX Controls applet is visible. If it is not, click the TX tray button on the right sidebar.
- Your transceiver is set to SSB mode and is on a clear frequency.
- A two-tone audio source (external generator or software) is ready to feed the radio's microphone or line input.

## Steps

1. In the TX Controls applet, set the **Tune Pwr** slider to the power level you want to use for the test. Default is 10; valid range is 0–100. While dragging the slider handle, a tooltip shows the power value in percent (e.g., "10%").
2. Set the **RF Power** slider to the desired output level. Default is 100; valid range is 0–100. While dragging the slider handle, a tooltip shows the power value in percent (e.g., "100%").
3. If you want to use a specific transmit profile (for example, a clean SSB profile without processing), select it from the **TX Profile** drop-down.
4. Start the two-tone audio signal from your external source so it is feeding the radio's input.
5. Click **MOX**. The button turns red and the radio keys up.
6. Watch the **RF Pwr** meter (0–120 W, red above 100 W) and the **SWR** meter (1.0–3.0, red above 2.5). The RF Pwr meter includes a peak-hold bar that holds the peak level for 2 seconds before decaying toward the current power level. The peak-hold resets to zero immediately when you unkey. Adjust the **RF Power** slider while transmitting to reach your target output.
   - Hover the mouse over the RF Pwr meter to see the exact wattage as a tooltip (e.g., "47 W").
   - Hover the mouse over the SWR meter to see the exact ratio as a tooltip (e.g., "1.35:1").
7. When the test is complete, click **MOX** again to unkey the transmitter. The button returns to its unlit state with an amber border and text accent.
8. Stop the two-tone audio source.

## What each control does

| Control    | Kind                                                                                                                                                                                              | Default                                                                                                                                                                 |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RF Power   | Slider                                                                                                                                                                                            | 100                                                                                                                                                                     |
| Tune Pwr   | Slider                                                                                                                                                                                            | 10                                                                                                                                                                      |
| TX Profile | Drop-down                                                                                                                                                                                         | —                                                                                                                                                                       |
| MOX        | Toggle button                                                                                                                                                                                     | —                                                                                                                                                                       |
| RF Pwr     | Displays forward power at the exciter output with PEP peak-hold (2 s hold then decay to current smoothed value over ~2.5 s). Peak resets immediately on un-key. Hover for exact wattage tooltip.   | Scale changes based on radio model via setPowerScale. Peak-hold ballistics match SmartSDR's peak-hold bar and the RX S-meter peak-hold pattern in SMeterWidget (#2561). |
| SWR        | Meter                                                                                                                                                                                             | —                                                                                                                                                                       |
| TUNE       | Starts/stops tune carrier; text becomes 'TUNING...' with red background while active. Right-click picks the carrier shape (Mono Tone / Two Tone) for the next tune cycle.                         | Right-click context menu (showTuneContextMenu) is a transient one-shot — nothing is persisted; the radio reverts to single_tone across power cycles.                    |
| ATU        | Starts the internal ATU tuning cycle. If status is Successful/OK at the same frequency, a second click sends bypass instead. Right-click opens the pre-tune sweep and Clear ATU Memories actions. | Disabled when TGXL is in OPERATE mode. Right-click context menu (showAtuContextMenu) exposes pre-tune band sweep (#2624) and Clear ATU Memories.                        |
| MEM        | Toggle button                                                                                                                                                                                     | —                                                                                                                                                                       |
| APD        | Toggle button                                                                                                                                                                                     | —                                                                                                                                                                       |
| Active     | Indicator (green)                                                                                                                                                                                 | dim                                                                                                                                                                     |
| Cal        | Indicator (green)                                                                                                                                                                                 | dim                                                                                                                                                                     |
| Avail      | Indicator (green)                                                                                                                                                                                 | dim                                                                                                                                                                     |
| Success    | Indicator (green)                                                                                                                                                                                 | dim                                                                                                                                                                     |
| Byp        | Indicator (orange)                                                                                                                                                                                | dim                                                                                                                                                                     |
| Mem        | Indicator (green)                                                                                                                                                                                 | dim                                                                                                                                                                     |
## Tips

- Keep SWR below 2.5 during the test. The SWR meter turns red above 2.5 as a visual warning.
- Select a TX profile that has microphone processing disabled before running a two-tone test. Processing can distort the two-tone envelope and produce misleading IMD readings.
- If you have ATU memories available, consider recalling a known-good memory before keying to ensure the antenna is matched. See [Recall an ATU memory](recall-an-atu-memory.md).
- If the QUIN chip is enabled in the Audio Channel Strip and the active TX slice is on a phone mode, clicking **MOX** will play the Quindar K-tone on engage and the BK-tone on disengage. If Quindar is disabled or the TX slice is not on a phone mode, **MOX** behaves as in earlier versions.
- The RF Power and Tune Pwr sliders now also update their displayed value from the model when you release the slider handle. This ensures the displayed value always matches the radio's actual setting.

## ATU button behavior

The **ATU** button toggles between starting a tune cycle and bypassing the tuner, mirroring the per-frequency behavior in SmartSDR.

- **First click on a new frequency** — starts a fresh ATU tune cycle. The **Success** indicator lights green when the tuner finds a match.
- **Second click at the same frequency** — if the ATU status is already Successful or OK and you have not changed frequency since the last tune, clicking **ATU** again switches the tuner to bypass. The **Byp** indicator lights orange.
- **Click after a frequency change** — always starts a fresh tune cycle, even if the previous status was Successful or OK.
- **After bypass** — the internally stored tuned frequency is cleared. The next click will start a fresh tune cycle regardless of frequency.

The **ATU** and **MEM** buttons are disabled when TGXL is in OPERATE mode.

## ATU button right-click menu

Right-click the **ATU** button to show a context menu with two additional actions:

- **Pre-tune bands…** — Opens the Pre-Tune dialog for running a sweep across selected bands. This action is only available when ATU memories are enabled. If memories are disabled, the menu item is grayed out with a tooltip suggesting you enable MEM first.
- **Clear ATU memories…** — Clears all stored ATU memories after a confirmation dialog.

## TUNE button right-click menu

Right-click the **TUNE** button to select the carrier shape for the next tune cycle:

- **Mono Tone** — Single tone, the default carrier shape.
- **Two Tone** — Two-tone carrier for linearity testing.

The selection is a one-shot and is not persisted across power cycles. The radio's tune mode reverts to single tone on its own across power cycles. A check mark next to either entry shows the radio's current tune mode.

## APD (Adaptive Pre-Distortion)

The **APD** toggle button enables or disables adaptive pre-distortion on the radio. When enabled, the three status indicators below the button show the current state:

- **Active** — Lit green when the equalizer is actively applied.
- **Cal** — Lit green when the radio is still calibrating.
- **Avail** — Lit green when a calibration is available but not yet applied.

The indicators progress through Cal → Avail → Active as the APD system completes its calibration cycle.

## MOX button idle accent

When not transmitting (idle state), the **MOX** button displays an amber border and text accent that distinguishes it from the neutral TUNE, ATU, and MEM buttons. This accent is editable in the Theme Editor under the `color.tx.mox.*` tokens, mirroring the LIVE chip accent on the waterfall.

## Troubleshooting

- **MOX keys but RF Pwr reads zero** — The two-tone audio source may not be reaching the radio's input, or the mode is not SSB. Confirm the audio routing and mode selection before re-keying.
- **SWR immediately goes red when MOX is pressed** — The antenna is unmatched. Click MOX to unkey, then run the ATU or check the feedline before continuing. See [Run the internal ATU](run-the-internal-atu.md).
- **RF Pwr meter pegs at full scale** — RF Power slider is set too high for the connected antenna and amplifier. Click MOX to unkey, then reduce the RF Power slider before re-keying.
- **ATU button starts a new tune instead of bypassing** — The transmit frequency changed since the last successful tune. This is expected. The button will only switch to bypass when the current frequency matches the frequency at which the ATU last reported a successful tune.
- **Quindar tones play unexpectedly when clicking MOX** — The QUIN chip is enabled in the Audio Channel Strip and the TX slice is on a phone mode. If you do not want Quindar tones during this test, disable the QUIN chip in the Audio Channel Strip before keying.

## Related

- [Set RF output power](set-rf-output-power.md)
- [Set tune-carrier power](set-tune-carrier-power.md)
- [Toggle MOX to manually key the transmitter](toggle-mox-to-manually-key-the-transmitter.md)
- [Switch TX profiles (e.g. SSB, Digital)](switch-tx-profiles-e-g-ssb-digital.md)
- [Run the internal ATU](run-the-internal-atu.md)
- [Recall an ATU memory](recall-an-atu-memory.md)
- Pre-tune bands for the ATU
- Clear ATU memories