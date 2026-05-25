# Switch between editing the TX and RX chains

The Aetherial Audio Chain applet shows either the TX or RX DSP chain at a time. Use the TX and RX toggle buttons to switch which chain is visible and editable. Your last-used selection is restored when you reopen the applet.

## Before you start

- The Aetherial Audio (TXDSP) container must be visible. If it is not, click the tray button labelled PUDU in the right sidebar to show it.
- The TX chain is shown by default. If you have never changed the selection, clicking RX is all that is needed.

## Steps

1. Locate the header row at the top of the Aetherial Audio Chain applet. It contains the buttons TX, RX, and BYPASS.
2. Click TX to display and edit the TX DSP chain (Parametric EQ, Compressor, Gate, De-Ess, Tube, PUDU, Reverb).
3. Click RX to display and edit the RX DSP chain (EQ, AGC-G, AGC-C, DESS, TUBE, EVO), which also shows the RADIO, ADSP, and SPEAK status tiles.
4. The selected button turns amber. The chain strip below updates immediately to show the chosen side.

## What each control does

| Control                                                       | Kind                                                                                                                                                                                                                                                                                                                                                                                   | Default                                                                                                                                                                                                                                                                            |
|---------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TX                                                            | Shows and edits the TX DSP chain (ClientChainWidget) — fully interactive: click-bypass, double-click-edit, drag-reorder.                                                                                                                                                                                                                                                               | Part of an exclusive pair with RX; amber 'VUDU' colour when selected. Last-active tab persists via PooDooAudioActiveTab='TX' / 'RX'.                                                                                                                                               |
| RX                                                            | Toggle button                                                                                                                                                                                                                                                                                                                                                                          | Unchecked                                                                                                                                                                                                                                                                          |
| BYPASS                                                        | Toggle button                                                                                                                                                                                                                                                                                                                                                                          | Unchecked                                                                                                                                                                                                                                                                          |
| Record (circle glyph)                                         | Toggle button                                                                                                                                                                                                                                                                                                                                                                          | Unchecked                                                                                                                                                                                                                                                                          |
| Play (triangle glyph)                                         | Toggle button                                                                                                                                                                                                                                                                                                                                                                          | Unchecked                                                                                                                                                                                                                                                                          |
| TX chain stage (EQ / COMP / GATE / DESS / TUBE / PUDU / VERB) | Single-click toggles bypass for the stage; double-click opens its frameless floating editor; drag reorders the TX chain.                                                                                                                                                                                                                                                               | Delegated to ClientChainWidget                                                                                                                                                                                                                                                     |
| RX chain stage (EQ / AGC-G / AGC-C / DESS / TUBE / EVO)       | Single-click toggles bypass for the RX stage; double-click opens its frameless floating editor in RX mode; drag reorders the RX chain.                                                                                                                                                                                                                                                 | Delegated to ClientRxChainWidget. All six RX stages (EQ, AGC-G/Gate, AGC-C/Comp, DESS/DeEss, TUBE, EVO/Pudu) are fully implemented. Order is independent of the TX chain. Distinct mime type 'application/x-aethersdr-rx-chain-stage' prevents stray drops between the two strips. |
| RADIO status tile                                             | Non-interactive RX-side bookend. Greens when PC Audio (the standard SSB stream) is enabled.                                                                                                                                                                                                                                                                                            | Only visible in RX mode                                                                                                                                                                                                                                                            |
| ADSP status / bypass tile                                     | Interactive RX-side tile that mirrors which client-side noise reducer is currently active. Label rotates to the active module's short name (e.g. 'NR2', 'NR4', 'BNR'); falls back to 'ADSP' when none is on. Single-click bypasses the entire NR cluster with an in-memory snapshot; single-click again restores the prior NR state. Double-click opens the AetherDSP Settings dialog. | Only visible in RX mode. Adopts the same blue-ring + green-LED-dot styling as implemented stage tiles. Snapshot restoration falls back to NR2 if no modules were active at bypass-time.                                                                                            |
| SPEAK status tile                                             | Non-interactive RX-side bookend. Greens when AetherSDR's audio output is unmuted.                                                                                                                                                                                                                                                                                                      | Only visible in RX mode                                                                                                                                                                                                                                                            |

TX and RX form an exclusive pair — only one can be active at a time. The active tab is saved as `PooDooAudioActiveTab` with the value `TX` or `RX` and is restored on next launch.

The TX and RX chains are fully independent: each has its own stage order, per-stage bypass state, and global BYPASS snapshot. Switching sides does not affect the other chain's state. The TX chain order is persisted as `ClientCompTxChainStages`; the RX chain order as `ClientCompRxChainStages`.

## How double-click works on TX chain stages

Double-clicking any TX chain stage tile opens the Aetherial Audio Channel Strip — the unified TX DSP window. The individual stage editors remain accessible from within the channel strip. Double-clicking a TX stage tile is the canonical way to open your TX audio settings.

Double-clicking an RX chain stage tile opens that stage's own floating editor.

## How the BYPASS button stays in sync

In v0.9.8, the bypass state is owned by the audio engine for both TX and RX sides. The BYPASS button on the chain applet and the BYPASS button on the Aetherial Audio Channel Strip (for TX) always reflect the same state. Clicking BYPASS on either control updates the other automatically. When you switch between TX and RX modes, the BYPASS button initialises its visual state from the engine's current bypass state for that side.

## Click discrimination interval

In v26.5.3, the chain applet uses a configurable click discrimination interval instead of the system double-click interval. This interval controls how long the applet waits after a mouse release before deciding whether the action is a single click or the first of a double-click. To adjust this interval:

1. Open Settings from the main menu.
2. Navigate to the Interaction settings page.
3. Adjust the click discrimination interval slider to your preference (in milliseconds).
4. The new interval takes effect immediately for all chain stage interactions.

This setting applies to both the TX and RX chain widgets. A shorter interval makes double-clicking more responsive but may cause inadvertent single-click actions on fast double-clicks. A longer interval makes single-click actions more reliable at the cost of a slight delay before they execute.

## Tips

- The BYPASS button always acts on the currently shown side only. Switching from TX to RX and clicking BYPASS bypasses only the RX chain; the TX chain's bypass state is unchanged.
- The record (⏺) and play (▶) monitor buttons are hidden when RX is selected — they are TX-only features.
- The hint text below the chain strip, "Click to bypass · Double click to edit · Drag to reorder", applies equally to both the TX and RX chains.
- The RX stage tiles are labelled AGC-G (gate) and AGC-C (compressor). These labels appear on the stage tiles themselves and in any stage editor titles.
- If you click BYPASS on the channel strip while the chain applet is showing the TX side, the applet's BYPASS button updates immediately to match — no manual refresh is needed.
- The ADSP tile label changes dynamically to show the active noise reducer module (e.g. NR2, NR4, BNR). If no noise reducer is active, it shows ADSP.

## Related

- [Aetherial Audio Chain overview](overview.md)
- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
- [Bypass every RX stage at once](bypass-every-rx-stage-at-once.md)
- [Reorder the TX DSP chain](reorder-the-tx-dsp-chain.md)
- [Reorder the RX DSP chain (independent of TX order)](reorder-the-rx-dsp-chain-independent-of-tx-order.md)
- [See at a glance whether PC Audio, the noise reducer, and audio output are live (RX status tiles)](see-at-a-glance-whether-pc-audio-the-noise-reducer-and-audio-output-are-live-rx-status-tiles.md)