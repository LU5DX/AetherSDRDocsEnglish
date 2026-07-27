# Bypass every RX stage at once

Use the **BYPASS** button to disable all RX chain stages in a single click, without losing track of which stages were active. Clicking **BYPASS** again restores only the stages that were enabled before.

## Before you start

- The Aetherial Audio Chain applet must be visible. If it is not, click the PUDU tray button in the right sidebar to show the container.
- You must be viewing the RX chain. The **BYPASS** button acts on whichever chain side is currently shown.

## Steps

1. In the Aetherial Audio Chain applet header, click **RX**. The RX chain stages appear below.
2. Click **BYPASS**. The button changes to its checked appearance (amber border and fill). Every stage in the RX chain is disabled immediately, including all noise reduction modules (NR2, NR4, MNR, DFNR, RN2, NVAFX). AetherSDR snapshots which stages were enabled at the moment you clicked.
3. To restore the previous stage states, click **BYPASS** again. Only the stages that were enabled before the bypass are re-enabled.

## What each control does

| Control | Kind | Default | Behavior | Notes |
|---------|------|---------|----------|-------|
| **RX** | Toggle button | Unchecked | Shows and edits the RX DSP chain (ClientRxChainWidget) — fully interactive with click-bypass, double-click-edit, drag-reorder; bookended by RADIO / DSP / SPEAK status tiles. | Part of an exclusive pair with TX; amber 'VUDU' colour when selected. Each side keeps independent stage state, chain order, and BYPASS snapshot. Last-active tab persists via PooDooAudioActiveTab. |
| **BYPASS** | Toggle button | Unchecked | Checked: snapshots the currently-enabled stages on the active side (TX or RX) and disables all of them (including all noise reduction modules). Unchecked: re-enables just the stages that were on before. The snapshot is global (per audio engine), not per-profile — the button stays pressed across Channel Strip profile switches. | Stages toggled manually while BYPASS was active are preserved outside the snapshot. TX and RX maintain separate snapshots — the visual checked state tracks the side currently shown. |
| RX chain stage (EQ / AGC-G / AGC-C / DESS / TUBE / EVO) | Drag handle | None | Single-click toggles bypass for the RX stage; double-click opens its frameless floating editor in RX mode; drag reorders the RX chain. | Delegated to ClientRxChainWidget. All six RX stages (EQ, AGC-G/Gate, AGC-C/Comp, DESS/DeEss, TUBE, EVO/Pudu) are fully implemented. Order is independent of the TX chain. Distinct mime type 'application/x-aethersdr-rx-chain-stage' prevents stray drops between the two strips. |
| RADIO status tile | Indicator | None | Non-interactive RX-side bookend. Greens when PC Audio (the standard SSB stream) is enabled. | Only visible in RX mode. |
| ADSP status / bypass tile | Toggle button | Unchecked | Interactive RX-side tile that mirrors which client-side noise reducer is currently active. Label rotates to the active module's short name (e.g. 'NR2', 'NR4', 'NVAFX'); falls back to 'ADSP' when none is on. Single-click bypasses the entire NR cluster with an in-memory snapshot; single-click again restores the prior NR state. Double-click opens the AetherDSP Settings dialog. | Only visible in RX mode. Adopts the same blue-ring + green-LED-dot styling as implemented stage tiles. Snapshot restoration falls back to NR2 if no modules were active at bypass-time. The 'BNR' label has been replaced by 'NVAFX' in v26.7.4. |
| SPEAK status tile | Indicator | None | Non-interactive RX-side bookend. Greens when AetherSDR's audio output is unmuted. | Only visible in RX mode. |

## Customise click discrimination interval

The applet uses a configurable interval to distinguish between a single click and a double-click on any chain stage. By default, this interval matches the operating system's double-click time.

### Steps

1. Open the main menu: **Settings > Interaction Settings**.
2. In the **Click discrimination interval** field, enter a value in milliseconds (range: 100–1000 ms).
3. Click **Save** or press Enter. The change takes effect immediately — no restart required.

A shorter interval makes double-click detection more responsive but may cause accidental single-click actions during fast double-clicks. A longer interval makes it easier to perform single-click bypasses but may feel sluggish when double-clicking to edit.

## Tips

- TX and RX keep separate BYPASS snapshots. Activating BYPASS on the RX chain does not affect the TX chain, and vice versa.
- If you manually toggle an individual stage while BYPASS is checked, that change is preserved outside the snapshot and will not be reversed when you uncheck BYPASS.
- The BYPASS checked state shown in the header tracks whichever chain side is currently visible. Switch to TX and back to RX to confirm the RX BYPASS state at a glance.
- BYPASS state for both TX and RX is owned by the audio engine. On the TX side, the BYPASS button is shared with the Aetherial Audio Channel Strip — engaging or disengaging TX BYPASS from the Channel Strip updates the BYPASS button in the Aetherial Audio Chain applet automatically, and vice versa. Similarly, the RX BYPASS state synchronises with the engine, so any changes made through other controls will be reflected when viewing the RX chain.
- BYPASS is global (per audio engine), not per-profile. If you switch Channel Strip profiles while BYPASS is active, the BYPASS button remains checked and continues to disable all stages regardless of which profile is loaded.
- The RADIO tile greens when PC Audio (the standard SSB stream) is enabled. The SPEAK tile greens when AetherSDR's audio output is unmuted.

## Troubleshooting

- **BYPASS appears checked but some stages are still active** — You may have toggled individual stages manually after engaging BYPASS. Those manual changes are independent of the snapshot. Uncheck and re-check BYPASS to take a fresh snapshot of the current stage states.
- **Clicking BYPASS re-enables stages you did not expect** — The snapshot was taken when BYPASS was first checked. Only the stages that were enabled at that moment are restored. Any stages you disabled before engaging BYPASS will remain off.
- **The TX BYPASS button state does not match what you set in the Channel Strip** — The applet synchronises with the audio engine when the TX side is shown. Click **TX** to switch to the TX chain; the BYPASS button will reflect the current engine state immediately.
- **The RX BYPASS button state does not match what you expect** — RX BYPASS state is also owned by the engine. Click **RX** to switch to the RX chain; the BYPASS button will reflect the current engine state. If the engine state was changed elsewhere, the button updates automatically when viewing the RX chain.
- **BYPASS appears unchecked after switching Channel Strip profiles** — BYPASS state is per audio engine, not per profile. If you switch profiles, the BYPASS button may appear unchecked even though the engine still has it enabled. Click **RX** to refresh the display, or simply re-click BYPASS to toggle it off and on.
- **Noise reduction remains active after engaging BYPASS** — In v26.7.4, BYPASS now disables NVAFX along with all other noise reduction modules. If noise reduction remains active, ensure you are using the latest version and that the BYPASS button is fully checked (amber border and fill).
- **The ADSP tile label shows 'BNR' instead of 'NVAFX'** — In v26.7.4, the 'BNR' noise reduction module has been renamed to 'NVAFX'. The ADSP tile will now display 'NVAFX' when that module is active. If you see 'BNR', you may need to update to the latest version.
- **Clicking a stage toggles bypass when you intended to edit, or opens the editor when you intended to bypass** — Adjust the click discrimination interval in **Settings > Interaction Settings**. A longer interval helps if you are accidentally opening editors when trying to bypass; a shorter interval helps if you are accidentally bypassing when trying to edit.

## Related

- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
- [Re-enable a specific stage after a global bypass](re-enable-a-specific-stage-after-a-global-bypass.md)
- [Switch between editing the TX and RX chains](switch-between-editing-the-tx-and-rx-chains.md)
- [Aetherial Audio Chain overview](overview.md)
- Interaction Settings