# Reconnect after a WAN radio drop without stuck state

TransmitModel holds all transmit state for the connected radio. When a WAN radio drops and reconnects, transmit controls can be left in a stuck state (for example, MOX showing as active when the radio is not actually transmitting). The steps below clear that condition safely.

## Before you start

- Confirm the radio has reconnected and is visible in the application before attempting to reset transmit state.
- If a tune cycle was in progress when the drop occurred, wait for the TUNE button label to return to **TUNE** before proceeding.

## Steps

1. Check the **MOX** button. If it appears active (red), click it once to toggle transmit off. This sends `xmit 0` to the radio and clears the stuck TX state.
2. Check the **TUNE** button. If it still shows **TUNING...** in red, click it once to stop the tune carrier.
3. If an ATU cycle was in progress, click **ATU** to reset it. The next click at the current frequency will start a fresh tune cycle.

## What each control does

| Control | Behavior |
|---|---|
| **RF Power:** | Sets the radio's RF transmit power as a percentage of maximum (0–100). Default: 100. |
| **Tune Pwr:** | Sets the carrier power used during antenna tune cycles (0–100). Default: 10. |
| **TUNE** | Starts or stops a single-tone tune carrier. Label changes to **TUNING...** and turns red while a tune is in progress. |
| **MOX** | Toggles manual transmit on or off. Sends `xmit 1` or `xmit 0` to the radio. Turns red immediately on press before the radio confirms TX state. Default: off. |
| **ATU** | First click at a frequency starts an ATU tune cycle; second click at the same frequency bypasses the ATU. A frequency change resets the toggle. Disabled when a TGXL tuner is in OPERATE mode. |
| **MEM** | Toggles ATU memory recall on or off, allowing the ATU to reuse a stored tune solution. Disabled when a TGXL tuner is in OPERATE mode. Default: off. |
| **APD** | Enables or disables adaptive pre-distortion. Hidden on radios that do not report `apd configurable=1`. Default: off. |
| **TX profile** | Loads the selected transmit profile on the radio. |
| **VOX** | Enables voice-operated transmit. Radio keys TX automatically when audio exceeds the VOX level threshold. Default: off. |
| **Delay:** | Sets the VOX hang time before the radio returns to receive (0–100; actual milliseconds = value × 20). Default: 50. |
| **DEXP** | Enables the downward expander (noise gate) to suppress background noise during speech pauses. Default: off. |
| **Low Cut** | Sets the TX audio low-frequency cutoff in Hz; steps snap to the nearest 50 Hz. Range: 0–10000. Default: 50. |
| **High Cut** | Sets the TX audio high-frequency cutoff in Hz; steps snap to the nearest 50 Hz. Range: 0–10000. Default: 3300. |
| **AM Carrier:** | Sets the AM carrier level as a percentage of full power (0–100). Default: 48. |

## Tips

- MOX uses an optimistic update, so the button turns red before the radio confirms the TX state. If the button stays red after a reconnect, the radio did not receive the prior `xmit 0` command — clicking MOX once will resend it.
- VOX is disabled by default. If the radio keys TX unexpectedly after reconnecting, verify **VOX** is off.
- DEXP state is saved to application settings (`DexpEnabled`) and will be restored on the next connection. If you changed it before the drop, verify it matches your intent after reconnecting.

## Related

- [transmit-model.md](transmit-model.md)
- [wan-connection.md](wan-connection.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
