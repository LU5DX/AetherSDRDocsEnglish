# Enable NR2 without freezing audio

The Aetherial Audio Chain includes a DSP status tile that mirrors the active noise reducer (e.g. NR2). When NR2 requires FFTW wisdom for the first time, or when existing wisdom is stale or incompatible, AetherSDR generates it in a background progress dialog so the audio chain and waveform scope remain fully usable.

## Before you start

- Open the Aetherial Audio container by clicking the **PUDU** button in the right sidebar applet tray.
- Make sure the **RX** tab is selected so the RX chain and DSP status tile are visible.

## Steps

1. Enable NR2 from the radio's DSP controls. AetherSDR checks whether valid FFTW wisdom exists. If wisdom is missing or cannot be imported, a background progress dialog opens and generates it — the audio chain remains interactive during this process.
2. When generation completes, the **DSP status tile** in the RX chain updates its label to **NR2**, confirming the noise reducer is active. No restart or manual reload is required.

## What each control does

| Control | Behavior |
|---|---|
| **RX** (toggle button) | Shows the RX DSP chain. The **DSP** and **SPEAK** status tiles are only visible in this mode. Click to switch from the TX view. |
| **DSP status tile** (indicator) | Mirrors which client-side noise reducer is active. Label rotates to the active module's short name (e.g. `NR2`, `NR4`, `BNR`). Falls back to `DSP` when none is active. Non-interactive. |
| **RADIO status tile** (indicator) | Greens when PC Audio (the standard SSB stream) is enabled. Non-interactive. Only visible in RX mode. |
| **SPEAK status tile** (indicator) | Greens when AetherSDR's audio output is unmuted. Non-interactive. Only visible in RX mode. |
| **BYPASS** (toggle button) | Snapshots currently-enabled RX stages and disables all of them while checked. Unchecking re-enables only the stages that were on before. TX and RX maintain separate snapshots. |
| **RX chain stage** — EQ / AGC-T / AGC-C / TUBE / PUDU (drag handle) | Single-click toggles bypass for that RX stage. Double-click opens its frameless floating editor. Drag to reorder the RX chain. |

## Tips

- If the background wisdom dialog appears on first use, let it complete before transmitting — the RX audio chain stays active throughout, but NR2 will not engage until wisdom is ready.
- The DSP status tile label is the quickest way to confirm NR2 is running; if it still shows `DSP` after enabling NR2, check that PC Audio is active (the **RADIO** tile should be green).
- TX and RX BYPASS snapshots are independent. Bypassing the RX chain does not affect TX stages.

## Related

- [aetherial-audio-chain.md](aetherial-audio-chain.md)
- [rx-dsp-chain.md](rx-dsp-chain.md)
<!-- docmesh:llm version=v0.9.5.1 date=2026-05-04 -->
