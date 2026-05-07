# Switch between editing the TX and RX chains

The Aetherial Audio Chain applet shows either the TX or RX DSP chain at a time. Use the TX and RX toggle buttons to switch which chain is visible and editable. Your last-used selection is restored when you reopen the applet.

## Before you start

- The Aetherial Audio (TXDSP) container must be visible. If it is not, click the tray button labelled PUDU in the right sidebar to show it.
- The TX chain is shown by default. If you have never changed the selection, clicking RX is all that is needed.

## Steps

1. Locate the header row at the top of the Aetherial Audio Chain applet. It contains the buttons TX, RX, and BYPASS.
2. Click TX to display and edit the TX DSP chain (Parametric EQ, Compressor, Gate, De-Ess, Tube, PUDU, Reverb).
3. Click RX to display and edit the RX DSP chain (EQ, AGC-T, AGC-C, TUBE, PUDU), which also shows the RADIO, DSP, and SPEAK status tiles.
4. The selected button turns amber. The chain strip below updates immediately to show the chosen side.

## What each control does
| Control | Kind | Default |
|---|---|---|
| TX | Toggle button | Checked |
| RX | Toggle button | Unchecked |
| RX chain stage (EQ / AGC-T / AGC-C / TUBE / PUDU) | Single-click toggles bypass for the RX stage; double-click opens its frameless floating editor in RX mode; drag reorders the RX chain. | Delegated to ClientRxChainWidget. All five RX stages (EQ, AGC-T/Gate, AGC-C/Comp, Tube, PUDU) are fully implemented. Order is independent of the TX chain. Distinct mime type `application/x-aethersdr-rx-chain-stage` prevents stray drops between the two strips. |
| RX DSP status tile (DSP) | Double-click opens the RX-chain DSP editor. | Delegated to ClientRxChainWidget. |
| NR2 status tile (when NR2 is in LastClientNr state) | Single-click re-enables NR2 and triggers wisdom preparation. | Delegated to ClientRxChainWidget. |

TX and RX form an exclusive pair — only one can be active at a time. The active tab is saved as `PooDooAudioActiveTab` with the value `TX` or `RX` and is restored on next launch.

The TX and RX chains are fully independent: each has its own stage order, per-stage bypass state, and global BYPASS snapshot. Switching sides does not affect the other chain's state. The TX chain order is persisted as `ClientCompTxChainStages`; the RX chain order as `ClientCompRxChainStages`.

## How double-click works on TX chain stages
In v0.9.7, double-clicking any TX chain stage tile no longer opens a per-stage floating editor directly. Instead, it opens the Aetherial Audio Channel Strip — the unified TX DSP window. The individual stage editors remain accessible from within the channel strip. Double-clicking a TX stage tile is now the canonical way to open your TX audio settings.

Double-clicking an RX chain stage tile continues to open that stage's own floating editor as before.

Double-clicking the RX **DSP status tile** (one of the RADIO / DSP / SPEAK tiles shown when the RX side is active) opens the RX-chain DSP editor directly.

Single-clicking the NR2 status tile when it is in the LastClientNr state re-enables NR2 and starts the wisdom-preparation path automatically — no separate menu step is needed.

## How the TX BYPASS button stays in sync

In v0.9.7, the TX bypass state is owned by the audio engine rather than derived solely from the applet's internal snapshot. As a result, the BYPASS button on the chain applet and the BYPASS button on the Aetherial Audio Channel Strip always reflect the same state. Clicking BYPASS on either control updates the other automatically. When you switch to the TX side, the BYPASS button initialises its visual state from the engine's current bypass state.

The RX BYPASS button continues to use the snapshot-based behaviour from previous releases.

## Tips

- The BYPASS button always acts on the currently shown side only. Switching from TX to RX and clicking BYPASS bypasses only the RX chain; the TX chain's bypass state is unchanged.
- The record (⏺) and play (▶) monitor buttons are hidden when RX is selected — they are TX-only features.
- The hint text below the chain strip, "Click to bypass · Double click to edit · Drag to reorder", applies equally to both the TX and RX chains.
- The RX stage tiles are labelled AGC-T (gate) and AGC-C (compressor). These labels appear on the stage tiles themselves and in any stage editor titles.
- If you click BYPASS on the channel strip while the chain applet is showing the TX side, the applet's BYPASS button updates immediately to match — no manual refresh is needed.

## Related

- [Aetherial Audio Chain overview](overview.md)
- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
- [Bypass every RX stage at once](bypass-every-rx-stage-at-once.md)
- [Reorder the TX DSP chain](reorder-the-tx-dsp-chain.md)
- [Reorder the RX DSP chain (independent of TX order)](reorder-the-rx-dsp-chain-independent-of-tx-order.md)
- [See at a glance whether PC Audio, the noise reducer, and audio output are live (RX status tiles)](see-at-a-glance-whether-pc-audio-the-noise-reducer-and-audio-output-are-live-rx-status-tiles.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
