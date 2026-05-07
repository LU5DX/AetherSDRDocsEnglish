# Select and load a TX profile

The Transmit Model holds and synchronizes all transmit state for the connected radio. Use the TX profile combo box to switch between stored transmit profiles without manually adjusting individual TX parameters.

## Steps

1. Locate the **TX profile** combo box in the TX applet.
2. Select the profile you want from the drop-down list. The radio loads the selected transmit profile immediately.

## What each control does

| Control | Behavior |
|---|---|
| **TX profile** | Loads the selected transmit profile on the radio. |
| **RF Power:** | Sets the radio's RF transmit power as a percentage of maximum (0–100). Default: 100. |
| **Tune Pwr:** | Sets the carrier power used during antenna tune cycles (0–100). Default: 10. |
| **TUNE** | Starts or stops a single-tone tune carrier. Button label changes to **TUNING...** and turns red while a tune is in progress. |
| **MOX** | Toggles manual transmit on or off. Button turns red immediately when enabled. Default: off. |
| **ATU** | First click tunes the ATU; second click at the same frequency bypasses it. A frequency change resets the toggle. Disabled when a TGXL tuner is in OPERATE mode. |
| **MEM** | Toggles ATU memory recall on or off, allowing the ATU to reuse a previously stored tune solution. Disabled when a TGXL tuner is in OPERATE mode. Default: off. |
| **APD** | Enables or disables adaptive pre-distortion. Hidden on radios that do not report `apd configurable=1`. Default: off. |
| **VOX** | Enables voice-operated transmit — radio keys TX automatically when audio exceeds the VOX level threshold. Default: off. |
| **Delay:** | Sets the VOX hang time before the radio returns to receive after audio drops below threshold (0–100; actual milliseconds = value × 20). Default: 50. |
| **DEXP** | Enables the downward expander (noise gate) to suppress background noise during pauses in speech. Default: off. |
| **Low Cut** | Sets the TX audio low-frequency cutoff in Hz; step buttons snap to the nearest 50 Hz multiple (0–10000). Default: 50. |
| **High Cut** | Sets the TX audio high-frequency cutoff in Hz; step buttons snap to the nearest 50 Hz multiple (0–10000). Default: 3300. |
| **AM Carrier:** | Sets the AM carrier level as a percentage of full power (0–100). Default: 48. |

## Tips

- Switching profiles overwrites the radio's active TX settings. If you have unsaved adjustments to filters, power, or audio, note them before switching.
- TX profiles are stored on the radio, not in AetherSDR. Create or rename profiles from your radio's own profile management interface.

## Related

- [transmit-model.md](transmit-model.md)
- [tune-antenna.md](tune-antenna.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
