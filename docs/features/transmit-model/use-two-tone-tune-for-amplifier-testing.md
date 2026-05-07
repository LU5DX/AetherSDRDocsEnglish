# Use two-tone tune for amplifier testing

The Transmit Model drives all transmit state for your connected radio, including the tune carrier used to drive an external amplifier to a known power level. Use the TUNE control to place a single-tone carrier on air at a defined power, then adjust levels to stress-test your amplifier.

## Before you start

- Confirm the radio is connected and a TX slice is active.
- Connect your amplifier and any associated ATU before transmitting.
- Ensure antenna or a dummy load is attached.

## Steps

1. Set **Tune Pwr:** to the desired carrier power level (0–100). A lower value, such as 10 (the default), is a safe starting point; increase it incrementally to the level your amplifier test requires.
2. Set **RF Power:** to the output level you want the radio to produce (0–100; default is 100).
3. Press **TUNE**. The button label changes to **TUNING...** and turns red while the carrier is active. The radio transmits a single-tone carrier at the power level set by **Tune Pwr:**.
4. Monitor your amplifier's forward power, reflected power, and any IMD measurements with your test equipment.
5. Press **TUNE** again to stop the carrier and return the radio to receive.

> **Note on two-tone testing:** AetherSDR's TUNE function produces a single-tone carrier. To perform a true two-tone IMD test, you must inject two equal-amplitude audio tones into the TX audio chain (for example, 700 Hz and 1900 Hz via an external generator or software) while **MOX** is active, rather than using the TUNE carrier. Set **RF Power:** to your target level, key the radio with **MOX**, apply the two tones, then observe the amplifier output.

## What each control does

| Control | Behavior |
|---|---|
| **RF Power:** | Sets the radio's RF transmit power as a percentage of maximum (0–100; default 100). |
| **Tune Pwr:** | Sets the carrier power used during antenna tune cycles (0–100; default 10). |
| **TUNE** | Starts or stops a single-tone tune carrier. Label changes to **TUNING...** and turns red while a tune is in progress. |
| **MOX** | Toggles manual transmit on or off. Button turns red immediately when activated (optimistic update). |
| **ATU** | First press at a frequency starts an ATU tune cycle; second press at the same frequency bypasses the ATU. Resets when the frequency changes. Disabled when a TGXL tuner is in OPERATE mode. |
| **MEM** | Toggles ATU memory recall on or off, allowing the ATU to reuse a previously stored tune solution. Disabled when a TGXL tuner is in OPERATE mode. |
| **APD** | Enables or disables adaptive pre-distortion. Hidden on radios that do not report `apd configurable=1`. |
| **TX profile** | Loads the selected transmit profile on the radio. |
| **VOX** | Enables voice-operated transmit; radio keys TX automatically when audio exceeds the VOX level threshold. |
| **Delay:** | Sets the VOX hang time before the radio returns to receive (0–100; actual milliseconds = value × 20; default 50). |
| **DEXP** | Enables the downward expander (noise gate) to suppress background noise during pauses in speech. |
| **Low Cut** | Sets the TX audio low-frequency cutoff in Hz, snapping to the nearest 50 Hz multiple (0–10000; default 50). |
| **High Cut** | Sets the TX audio high-frequency cutoff in Hz, snapping to the nearest 50 Hz multiple (0–10000; default 3300). |
| **AM Carrier:** | Sets the AM carrier level as a percentage of full power (0–100; default 48). |

## Tips

- Keep **Tune Pwr:** well below 100 when first connecting an unknown amplifier. Step it up gradually while watching the forward-power gauge.
- If you need the ATU matched before testing, press **ATU** first (with a reduced power level) to let the tuner find a solution, then run the TUNE carrier or two-tone test.
- Disable **VOX** and **DEXP** before a two-tone MOX test to prevent the noise gate from interrupting the tone burst.
- The **RF Power:** slider controls the radio's output level and rescales the forward-power gauge; lower it if the amplifier is already providing gain.

## Related

- [transmit-model.md](transmit-model.md)
- [atu-tuning.md](atu-tuning.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
