# Bypass every TX stage at once

Use the BYPASS button to silence the entire TX DSP chain in one click — for example, to compare your processed and unprocessed transmit audio, or to rule out a processing stage when troubleshooting.

## Before you start

- The Aetherial Audio Chain applet must be visible. If it is not, click the PUDU tray button in the right sidebar to show it.
- Click TX in the applet header to make sure the TX chain is the active side. BYPASS acts only on the currently-shown chain.

## Steps

1. Open the Aetherial Audio Chain applet by clicking the PUDU tray button in the right sidebar.
2. Click TX in the applet header to select the TX chain. The button turns amber when active.
3. Click BYPASS. The button highlights to show it is checked, and every enabled TX stage (including RN2) is disabled at once.
4. To restore the stages, click BYPASS again. Only the stages that were enabled before you engaged BYPASS are re-enabled.

## What each control does

| Control                                                 | Kind                                                                                                                                                                                                                                                                                                                                                                                   | Default                                                                                                                                                                                                                                                                            |
|---------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TX                                                      | Shows and edits the TX DSP chain (ClientChainWidget) — fully interactive: click-bypass, double-click-edit, drag-reorder.                                                                                                                                                                                                                                                               | Part of an exclusive pair with RX; amber 'VUDU' colour when selected. Last-active tab persists via PooDooAudioActiveTab='TX' / 'RX'.                                                                                                                                               |
| RX                                                      | Toggle button                                                                                                                                                                                                                                                                                                                                                                          | Unchecked                                                                                                                                                                                                                                                                          |
| BYPASS                                                  | Toggle button                                                                                                                                                                                                                                                                                                                                                                          | Unchecked                                                                                                                                                                                                                                                                          |
| RX chain stage (EQ / AGC-G / AGC-C / DESS / TUBE / EVO) | Single-click toggles bypass for the RX stage; double-click opens its frameless floating editor in RX mode; drag reorders the RX chain.                                                                                                                                                                                                                                                 | Delegated to ClientRxChainWidget. All six RX stages (EQ, AGC-G/Gate, AGC-C/Comp, DESS/DeEss, TUBE, EVO/Pudu) are fully implemented. Order is independent of the TX chain. Distinct mime type 'application/x-aethersdr-rx-chain-stage' prevents stray drops between the two strips. |
| ADSP status / bypass tile                               | Interactive RX-side tile that mirrors which client-side noise reducer is currently active. Label rotates to the active module's short name (e.g. 'NR2', 'NR4', 'BNR'); falls back to 'ADSP' when none is on. Single-click bypasses the entire NR cluster with an in-memory snapshot; single-click again restores the prior NR state. Double-click opens the AetherDSP Settings dialog. | Only visible in RX mode. Adopts the same blue-ring + green-LED-dot styling as implemented stage tiles. Snapshot restoration falls back to NR2 if no modules were active at bypass-time.                                                                                            |

Stage order and individual stage state are persisted via `ClientCompTxChainStages`. The applet container visibility is persisted via `Applet_TXDSP`.

## Tips

- TX and RX keep completely separate BYPASS snapshots. Engaging BYPASS on the TX chain has no effect on the RX chain, and vice versa.
- If you manually toggle a stage while BYPASS is active, that manual change is preserved outside the snapshot and will not be reversed when you lift BYPASS.
- The BYPASS checked state shown in the header tracks whichever chain is currently visible. If you switch to RX and back to TX, the TX BYPASS state is restored exactly as you left it.
- In v0.9.8, both TX and RX bypass are owned by the audio engine. The BYPASS button in the Aetherial Audio Chain applet, the BYPASS button in the Aetherial Audio Channel Strip (TX), and any future BYPASS control for RX all reflect and control the same engine-owned state. Clicking BYPASS in any of these locations for the same chain produces the same result.
- Double-clicking any TX chain stage tile now opens the Aetherial Audio Channel Strip — the unified TX DSP editor window — rather than a per-stage floating editor. Individual stage editors remain accessible from within the channel strip.
- The click discrimination interval used for single-click vs double-click detection on both TX and RX chain tiles can be configured in Interaction Settings. By default it uses the system double-click interval, but you can adjust it independently if needed.
- **BYPASS now also disables RN2** on the TX chain. The BYPASS button tooltip was updated in v26.6.1 to clarify this: "Disable every stage in the selected chain (including RN2)."
- **BYPASS scope is global (per audio engine), not per-profile.** The BYPASS button stays pressed across Channel Strip profile switches. Switching profiles does not clear the BYPASS state; you must click BYPASS again to restore stages.

## Troubleshooting

- **BYPASS appears unchecked after switching from RX to TX** — This is expected. TX and RX track separate states. For each side, the displayed state now mirrors the engine's `isTxBypassed` or `isRxBypassed` value directly. Check which side you engaged BYPASS on.
- **Clicking BYPASS re-enables fewer stages than expected** — Any stage you toggled off manually before clicking BYPASS was already disabled and was not part of the snapshot, so it will not be restored.
- **BYPASS state in the applet does not match the channel strip** — Ensure you are running v0.9.8 or later. Earlier versions tracked TX bypass state only in the applet snapshot; v0.9.8 synchronises all BYPASS controls (TX and RX) through the audio engine.
- **Double-click opens the editor inconsistently on the TX or RX chain** — The click discrimination interval can be adjusted in Interaction Settings. If you have a slow double-click motion, increase this interval. If you accidentally trigger editors instead of bypassing, decrease the interval.
- **BYPASS is engaged but RN2 is still active** — In v26.6.1, BYPASS now explicitly disables RN2 as part of the global bypass. Ensure you are running v26.6.1 or later. If RN2 remains active, try toggling BYPASS off and on again.
- **BYPASS on the ADSP tile does not disable BNR** — In v26.7.4, the ADSP tile now disables and restores `nvAfxEnabled` instead of `bnrEnabled`. Clicking the ADSP tile toggles the entire NR cluster, including the new `nvAfx` module. Ensure you have updated to v26.7.4 for this behavior.

## Related

- [Bypass every RX stage at once](bypass-every-rx-stage-at-once.md)
- [Re-enable a specific stage after a global bypass](re-enable-a-specific-stage-after-a-global-bypass.md)
- [Switch between editing the TX and RX chains](switch-between-editing-the-tx-and-rx-chains.md)
- [Aetherial Audio Chain overview](overview.md)
- Configure interaction settings