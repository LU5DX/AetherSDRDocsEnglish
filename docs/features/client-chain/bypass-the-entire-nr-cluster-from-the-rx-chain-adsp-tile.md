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

| Control | Behavior |
|---|---|
| **ADSP tile** | Click to bypass the entire NR cluster. The label rotates to show the active module's short name (`NR2`, `NR4`, `BNR`) or `ADSP` when none is on. Double-click opens the AetherDSP Settings dialog. |
| **BYPASS button** | Disables every stage on the current chain (TX or RX). Does not affect the ADSP bypass — they operate independently. |

## Tips

- The ADSP bypass is independent of the **BYPASS** button. Bypassing all RX stages with **BYPASS** does not affect the ADSP tile's state, and vice versa.
- Double-click the **ADSP** tile to open AetherDSP Settings for fine-tuning individual noise reducer parameters.

## Related

- [Bypass every RX stage at once](bypass-every-rx-stage-at-once.md)
- [Open a stage's frameless floating editor from the chain](open-a-stage-s-frameless-floating-editor-from-the-chain.md)
- [See at a glance whether PC Audio, the noise reducer, and audio output are live (RX status tiles)](see-at-a-glance-whether-pc-audio-the-noise-reducer-and-audio-output-are-live-rx-status-tiles.md)
