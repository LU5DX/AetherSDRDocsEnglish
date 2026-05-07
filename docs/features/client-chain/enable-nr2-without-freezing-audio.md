# Enable NR2 without freezing audio

The Aetherial Audio Chain shows the client-side DSP signal flow as a horizontal strip of stages. When NR2 requires FFTW wisdom generation (first run, or after a stale or incompatible wisdom file), the process runs in a background progress dialog so the audio chain and waveform scope remain fully usable.

## Steps

1. Open the Aetherial Audio container by clicking the **PUDU** button in the right sidebar applet tray.
2. Click the **RX** toggle button to switch to the RX chain view.
3. Check the **DSP status tile** — its label rotates to **NR2** when the NR2 noise reducer becomes active. The tile turns green once NR2 is running.

> FFTW wisdom generation runs in a background progress dialog. The audio chain and waveform scope are not blocked while wisdom is being computed.

## What each control does

| Control | Behavior |
|---|---|
| **TX** | Shows and edits the TX DSP chain. Single-click a stage to bypass it, double-click to open its editor, drag to reorder. Amber when selected. |
| **RX** | Shows and edits the RX DSP chain (EQ, AGC-T, AGC-C, Tube, PUDU), bookended by RADIO / DSP / SPEAK status tiles. Single-click, double-click, and drag work the same as TX. |
| **BYPASS** | Checked: snapshots all currently-enabled stages on the active side and disables them. Unchecked: re-enables only the stages that were on before. TX and RX keep separate snapshots. |
| **RX chain stage (EQ / AGC-T / AGC-C / TUBE / PUDU)** | Single-click toggles bypass for that stage; double-click opens its frameless floating editor; drag reorders the RX chain. |
| **DSP status tile** | Read-only indicator. Mirrors which client-side noise reducer is active. Label changes to the module's short name (e.g. **NR2**, **NR4**, **BNR**); falls back to **DSP** when none is active. Visible in RX mode only. |
| **RADIO status tile** | Read-only indicator. Turns green when PC Audio (the standard SSB stream) is enabled. Visible in RX mode only. |
| **SPEAK status tile** | Read-only indicator. Turns green when AetherSDR's audio output is unmuted. Visible in RX mode only. |

## Tips

- Wisdom generation only runs on the first use of NR2 or when an existing wisdom file is stale or incompatible. Subsequent starts use the cached file and are immediate.
- If you need to verify NR2 is active, watch the **DSP status tile** — it shows **NR2** as the label when that reducer is selected.
- TX and RX chains are independent; switching to RX to enable NR2 does not affect your TX DSP stage order or bypass state.

## Related

- [aetherial-audio-chain.md](aetherial-audio-chain.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
