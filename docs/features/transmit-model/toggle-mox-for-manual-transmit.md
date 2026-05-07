# Toggle MOX for manual transmit

The **MOX** button manually keys your radio into transmit. When enabled, AetherSDR sends a transmit command to the radio immediately, before the radio confirms the TX state.

## Steps

1. Open the TX applet.
2. Click **MOX** to begin transmitting. The button turns red.
3. Click **MOX** again to return to receive.

## What each control does

| Control | Behavior |
|---------|----------|
| **MOX** | Toggles manual transmit on or off. The button turns red immediately on activation (optimistic update) before the radio confirms the TX state. |
| **RF Power:** | Sets the radio's RF transmit power as a percentage of maximum. Default: `100`. Range: `0–100`. |
| **Tune Pwr:** | Sets the carrier power used during antenna tune cycles. Default: `10`. Range: `0–100`. |
| **TUNE** | Starts or stops a single-tone tune carrier. Label changes to **TUNING...** and turns red while a tune is in progress. |
| **ATU** | First click at a frequency starts an ATU tune cycle; second click at the same frequency bypasses the ATU. A frequency change resets the toggle so the next click tunes again. Disabled when a TGXL tuner is in OPERATE mode. |
| **MEM** | Toggles ATU memory recall on or off, allowing the ATU to re-use a previously stored tune solution. Disabled when a TGXL tuner is in OPERATE mode. |
| **APD** | Enables or disables adaptive pre-distortion. Hidden on radios that do not report `apd configurable=1`. |
| **TX profile** | Loads the selected transmit profile on the radio. |
| **VOX** | Enables voice-operated transmit — radio keys TX automatically when audio exceeds the VOX level threshold. |
| **Delay:** | Sets the VOX hang time before the radio returns to receive after audio drops below threshold. Default: `50`. Range: `0–100`. Actual milliseconds = value × 20. |
| **DEXP** | Enables the downward expander (noise gate) to suppress background noise during pauses in speech. |
| **Low Cut** | Sets the TX audio low-frequency cutoff in Hz. Step buttons snap to the nearest 50 Hz multiple. Default: `50`. Range: `0–10000`. |
| **High Cut** | Sets the TX audio high-frequency cutoff in Hz. Step buttons snap to the nearest 50 Hz multiple. Default: `3300`. Range: `0–10000`. |
| **AM Carrier:** | Sets the AM carrier level as a percentage of full power. Default: `48`. Range: `0–100`. |

## Tips

- MOX uses an optimistic update: the button turns red before the radio confirms TX state. If the radio rejects the command, the button reverts automatically.
- On phone modes with Quindar tones enabled, MOX routes through the Quindar tone coordinator to play intro and outro tones before keying and unkeying the radio.
- Do not use MOX while **TUNE** or an **ATU** cycle is already in progress.

## Related

- [transmit-settings.md](transmit-settings.md)
- [antenna-tuner.md](antenna-tuner.md)
- [vox.md](vox.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
