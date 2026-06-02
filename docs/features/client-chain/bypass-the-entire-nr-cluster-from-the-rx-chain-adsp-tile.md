# Bypass the entire NR cluster from the RX chain ADSP tile

Bypass every client-side noise reducer (NR2, NR4, MNR, DFNR, RN2, BNR) at once using the ADSP tile on the RX chain. The tile remembers which noise reducer was active before bypass, so clicking it again restores that module.

## Before you start

- The Aetherial Audio Chain container must be visible. Click the **PUDU** tray button in the right sidebar to toggle it.
- Click **RX** in the header row to show the RX DSP chain.

## Steps

1. Locate the **ADSP** tile in the RX chain strip. It sits between **RADIO** (left) and **SPEAK** (right).
   - When a noise reducer is active, the tile shows its short name (e.g. `NR2`, `NR4`, `BNR`).
   - When no noise reducer is active, the tile shows `ADSP`.

2. **Single-click** the **ADSP** tile.

   - All client-side noise reducers are bypassed. The tile's label shows `ADSP`.
   - AetherSDR takes an in-memory snapshot of which noise reducer was active.

3. To restore the prior noise reducer, **single-click** the **ADSP** tile again.

   - The previously active module is re-enabled and its short name reappears on the tile. If no module was active at bypass time, NR2 is enabled as a fallback.

## What each control does

| Control | Behavior | Notes |
|---|---|---|
| **ADSP tile** | Click to bypass the entire NR cluster. The label rotates to show the active module's short name (`NR2`, `NR4`, `BNR`) or `ADSP` when none is on. Double-click opens the AetherDSP Settings dialog. | Only visible in RX mode. Adopts blue-ring + green-LED-dot styling. |
| **BYPASS button** | Disables every stage in the selected chain (including RN2). Click again to restore the stages that were on before. Scope is global (per audio engine), not per-profile — the button stays pressed across Channel Strip profile switches. | TX and RX maintain separate snapshots. |
| **TX** tab | Shows and edits the TX DSP chain (Parametric EQ, Compressor with pre-comp Drive and Phase-rotator PAPR reduction, Gate, De-Ess with user-selectable 12–48 dB/oct slope, Tube with RN2 noise-reduction toggle, PUDU exciter, Reverb). Amber 'VUDU' colour when selected. Last-active tab persists via `PooDooAudioActiveTab`. | Part of an exclusive pair with RX. |
| **RX** tab | Shows and edits the RX DSP chain (EQ, AGC-G/Gate, AGC-C/Compressor, DESS/DeEss, TUBE, EVO/Pudu). All six stages are fully implemented. Bookended by RADIO / ADSP / SPEAK status tiles. Interactive: click-bypass, double-click-edit, drag-reorder. Color indicates active side. Last-active tab persists via `PooDooAudioActiveTab`. | Each side keeps independent stage state, chain order, and BYPASS snapshot. |
| **Record** (circle glyph) | Captures up to 30 seconds of post-PUDU TX audio. Click again to stop (playback starts automatically). Tooltip: "Record up to 30 s of post-PooDoo™ TX audio (MIC must be set to PC and DAX off)." Hidden in RX mode. Only enabled when the mic input is ready and playback is not running. Pulses red while recording. | |
| **Play** (triangle glyph) | Plays back the captured PUDU audio. Click again to cancel. Hidden in RX mode. Only enabled once a recording exists and recording is not active. Pulses green while playing. | |
| **TX chain stage** (EQ / COMP / GATE / DESS / TUBE / PUDU / VERB) | Single-click toggles bypass for the stage. Double-click opens its frameless floating editor. Drag reorders the TX chain. | Delegated to ClientChainWidget. Hint text: "Click to bypass · Double click to edit · Drag to reorder". |
| **RX chain stage** (EQ / AGC-G / AGC-C / DESS / TUBE / EVO) | Single-click toggles bypass for the stage. Double-click opens its frameless floating editor. Drag reorders the RX chain. | Delegated to ClientRxChainWidget. Distinct mime type `application/x-aethersdr-rx-chain-stage` prevents stray drops between TX and RX strips. |
| **RADIO status tile** | Non-interactive. Greens when PC Audio (the standard SSB stream) is enabled. Only visible in RX mode. | |
| **ADSP status/bypass tile** | Interactive. Mirrors which noise reducer is currently active. Label rotates to the active module's short name (e.g. `NR2`, `NR4`, `BNR`). Falls back to `ADSP` when none is on. Single-click bypasses the entire NR cluster with an in-memory snapshot; single-click again restores the prior NR state. Double-click opens the AetherDSP Settings dialog. | Only visible in RX mode. Blue-ring + green-LED-dot styling. |
| **SPEAK status tile** | Non-interactive. Greens when AetherSDR's audio output is unmuted. Only visible in RX mode. | |

## Tips

- The ADSP bypass is independent of the **BYPASS** button. Bypassing all RX stages with **BYPASS** does not affect the ADSP tile's state, and vice versa.
- Double-click the **ADSP** tile to open AetherDSP Settings for fine-tuning individual noise reducer parameters.
- The click discrimination interval for distinguishing single-click from double-click follows the choice in Click Discrimination Interval, not the system double-click interval.
- The **BYPASS** button operates globally (per audio engine), not per-profile. It remains pressed even after switching Channel Strip profiles.

## Related

- [Bypass every RX stage at once](bypass-every-rx-stage-at-once.md)
- [Open a stage's frameless floating editor from the chain](open-a-stage-s-frameless-floating-editor-from-the-chain.md)
- [See at a glance whether PC Audio, the noise reducer, and audio output are live (RX status tiles)](see-at-a-glance-whether-pc-audio-the-noise-reducer-and-audio-output-are-live-rx-status-tiles.md)
- Click Discrimination Interval