# Use two-tone tune for amplifier testing

The Transmit Model controls RF power and tune carrier settings for the connected radio. Use the two-tone tune variant to drive an amplifier with a two-tone signal for intermodulation distortion testing.

## Before you start

- Confirm your radio is connected and the transmit applet is visible.
- Set an appropriate **RF Power:** level for your amplifier's input rating before transmitting.

## Steps

1. Set **RF Power:** to the level required for your amplifier test (0–100).
2. Set **Tune Pwr:** to the carrier power percentage you want to use during the tune cycle (0–100; default is 10).
3. Press the keyboard shortcut bound to the **two_tone_tune** action to start the two-tone tune carrier. The **TUNE** button label changes to **TUNING...** and turns red while the carrier is active.
4. Run your amplifier measurements.
5. Press the **two_tone_tune** keyboard shortcut again (or press **TUNE**) to stop. Two-tone mode automatically restores single-tone mode when stopped.

## What each control does

| Control | Behavior |
|---|---|
| **RF Power:** | Sets the radio's RF transmit power as a percentage of maximum (0–100). |
| **Tune Pwr:** | Sets the carrier power used during antenna tune cycles (0–100; default 10). |
| **TUNE** | Starts or stops a tune carrier. Button label changes to **TUNING...** and turns red while active. The two-tone variant is started via the `two_tone_tune` keyboard shortcut; two-tone mode automatically restores single-tone mode when stopped. |
| **MOX** | Toggles manual transmit on or off. Button turns red immediately on activation before the radio confirms TX state. |
| **ATU** | First click at a frequency starts an ATU tune cycle; second click at the same frequency (when status is Successful or OK) bypasses the ATU. A frequency change resets the toggle. Disabled when a TGXL tuner is in OPERATE mode. |
| **MEM** | Toggles ATU memory recall on or off, allowing the ATU to reuse a previously stored tune solution. Disabled when a TGXL tuner is in OPERATE mode. |
| **APD** | Enables or disables adaptive pre-distortion. Hidden on radios that do not report `apd configurable=1`. |
| **TX profile** | Loads the selected transmit profile on the radio. |
| **VOX** | Enables voice-operated transmit — radio keys TX automatically when audio exceeds the VOX level threshold. |
| **Delay:** | Sets the VOX hang time before returning to receive after audio drops below threshold (0–100; actual ms = value × 20; default 50). |
| **DEXP** | Enables the downward expander (noise gate) to suppress background noise during pauses in speech. |
| **Low Cut** | Sets the TX audio low-frequency cutoff in Hz; steps snap to the nearest 50 Hz multiple (0–10000; default 50). |
| **High Cut** | Sets the TX audio high-frequency cutoff in Hz; steps snap to the nearest 50 Hz multiple (0–10000; default 3300). |
| **AM Carrier:** | Sets the AM carrier level as a percentage of full power (0–100; default 48). |

## Tips

- Keep **Tune Pwr:** low (10–20) when first connecting an unknown amplifier to avoid overdrive.
- The `two_tone_tune` keyboard shortcut is the only way to start two-tone mode; there is no dedicated button in the UI.
- Do not enable **MOX** while a tune carrier is already active.

## Related

- [transmit-controls.md](transmit-controls.md)
- [antenna-tuner.md](antenna-tuner.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
