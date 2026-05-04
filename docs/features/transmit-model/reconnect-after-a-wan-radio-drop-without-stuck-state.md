# Reconnect after a WAN radio drop without stuck state

AetherSDR's WAN connection layer now checks both the logical connected flag and the underlying socket state before allowing a new connection attempt. This prevents the application from getting stuck when a previous connection is still closing at the socket level.

## Before you start

- Confirm the radio is reachable over WAN (verify your SmartLink credentials and network path).
- Ensure you have disconnected from the radio in the UI before attempting to reconnect — do not click reconnect while a disconnect is still in progress.

## Steps

1. If AetherSDR shows the radio as disconnected but the reconnect attempt does nothing, wait a few seconds for the underlying socket to fully close (the new guard checks `UnconnectedState`), then click **Connect** again from the radio selection screen.
2. Once connected, confirm the TX panel is functional by checking that **MOX** responds and the **RF Power:** slider reflects the expected value.

## What each control does

| Control | Behavior | Notes |
|---|---|---|
| **RF Power:** | Sets the radio's RF transmit power as a percentage of maximum (0–100). Default: 100. |  |
| **Tune Pwr:** | Sets the carrier power used during antenna tune cycles (0–100). Default: 10. |  |
| **TUNE** | Starts or stops a tune carrier. Button label changes to **TUNING...** and turns red while a tune is in progress. A two-tone variant is available via keyboard shortcut. |  |
| **MOX** | Toggles manual transmit on or off. Turns red immediately (optimistic update) before the radio confirms TX state. Default: off. |  |
| **ATU** | First click tunes the ATU; second click at the same frequency bypasses it. Resets when the frequency changes. Disabled when a TGXL tuner is in OPERATE mode. |  |
| **MEM** | Toggles ATU memory recall so the ATU can reuse a previously stored tune solution. Disabled when a TGXL tuner is in OPERATE mode. Default: off. |  |
| **APD** | Enables or disables adaptive pre-distortion. Hidden on radios that do not report `apd configurable=1`. Default: off. |  |
| **TX profile** | Loads the selected transmit profile on the radio. |  |
| **VOX** | Enables voice-operated transmit; radio keys TX when audio exceeds the VOX level threshold. Default: off. |  |
| **Delay:** | Sets the VOX hang time before returning to receive (0–100; actual ms = value × 20). Default: 50. |  |
| **DEXP** | Enables the downward expander (noise gate) to suppress background noise. State is persisted to AppSettings. Default: off. |  |
| **Low Cut** | Sets the TX audio low-frequency cutoff in Hz, snapping to the nearest 50 Hz multiple (0–10000). Default: 50 Hz. |  |
| **High Cut** | Sets the TX audio high-frequency cutoff in Hz, snapping to the nearest 50 Hz multiple (0–10000). Default: 3300 Hz. |  |
| **AM Carrier:** | Sets the AM carrier level as a percentage of full power (0–100). Default: 48. |  |
## Tips

- If the reconnect button remains unresponsive immediately after a drop, wait 5–10 seconds before retrying. The guard introduced in V0.9.5.1 blocks a new connection attempt until the socket reaches `UnconnectedState`, so clicking too quickly will silently return without connecting.
- After reconnecting, verify **RF Power:** is at your intended level — the radio does not always restore slider position automatically after a WAN drop.

## Related

- [transmit-model.md](transmit-model.md)
- [wan-connection.md](wan-connection.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
