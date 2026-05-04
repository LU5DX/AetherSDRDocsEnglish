# Select and load a TX profile

The Transmit Model manages all transmit state for the connected radio. Use the **TX profile** combo box to switch between stored transmit profiles and apply one to the radio immediately.

## Steps

1. Open the TX applet to locate the transmit controls.
2. Click the **TX profile** combo box and select the profile you want to load.
3. The radio loads the selected profile immediately — no additional confirmation is required.

## What each control does

| Control | Behavior |
|---|---|
| **TX profile** | Loads the selected transmit profile on the radio. |
| **RF Power:** | Sets the radio's RF transmit power as a percentage of maximum (0–100). |
| **Tune Pwr:** | Sets the carrier power used during antenna tune cycles (0–100). |
| **TUNE** | Starts or stops a tune carrier. Label changes to **TUNING...** and turns red while a tune is in progress. A two-tone variant is available via keyboard shortcut. |
| **MOX** | Toggles manual transmit on or off. Turns red immediately (optimistic update) before the radio confirms the TX state. |
| **ATU** | First click at a frequency starts an ATU tune cycle; second click at the same frequency (when status is Successful or OK) bypasses the ATU. A frequency change resets the toggle. Disabled when a TGXL tuner is in OPERATE mode. |
| **MEM** | Toggles ATU memory recall on or off, allowing the ATU to reuse a previously stored tune solution. Disabled when a TGXL tuner is in OPERATE mode. |
| **APD** | Enables or disables adaptive pre-distortion. Hidden on radios that do not report `apd configurable=1`. |
| **VOX** | Enables voice-operated transmit — the radio keys TX automatically when audio exceeds the VOX level threshold. |
| **Delay:** | Sets the VOX hang time before the radio returns to receive after audio drops below threshold (0–100; actual milliseconds = value × 20). Default: 50. |
| **DEXP** | Enables the downward expander (noise gate) to suppress background noise during pauses in speech. |
| **Low Cut** | Sets the TX audio low-frequency cutoff in Hz. Step buttons snap to the nearest 50 Hz multiple. Range: 0–10000. Default: 50. |
| **High Cut** | Sets the TX audio high-frequency cutoff in Hz. Step buttons snap to the nearest 50 Hz multiple. Range: 0–10000. Default: 3300. |
| **AM Carrier:** | Sets the AM carrier level as a percentage of full power (0–100). Default: 48. |

## Tips

- Switching profiles overwrites transmit settings such as audio processing and filter edges on the radio — confirm the desired profile name before selecting.
- After loading a profile, check **Low Cut** and **High Cut** values to verify the TX audio filter edges match your operating intent.
- The **RF Power:** slider range is always 0–100 regardless of radio model; the forward-power gauge in the TX applet rescales automatically.

## Related

- [transmit-model.md](transmit-model.md)
- [atu-tune.md](atu-tune.md)
- [vox-setup.md](vox-setup.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
