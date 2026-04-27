# Aetherial Audio Chain overview

The Aetherial Audio Chain applet gives you a visual, interactive view of AetherSDR's client-side DSP signal processing. Use it to monitor, bypass, reorder, and edit the stages that shape your transmitted and received audio before it reaches the radio or your speakers.

## Before you start

- The Aetherial Audio container must be visible. Click the tray button labelled "PUDU" in the right sidebar to toggle it. The chain applet appears as the top section of that container.
- No radio connection is required to view or edit the chains.

## How it works

The applet presents two independent DSP chains — TX and RX — as a horizontal strip of stage tiles. Only one chain is shown at a time. Use the TX and RX buttons to switch between them.

**TX chain** processes audio on the transmit path through these stages in order: EQ, COMP, GATE, DESS, TUBE, PUDU, VERB.

**RX chain** processes received audio through: EQ, GATE, COMP, TUBE, PUDU. The RX strip is bookended by three non-interactive status tiles — RADIO, DSP, and SPEAK — that show at a glance whether the receive path is live end to end.

Each stage tile supports three interactions:

- **Single-click** — toggles bypass for that stage only.
- **Double-click** — opens the stage's frameless floating editor.
- **Drag** — reorders the stage within its chain. A vertical cyan bar shows where the stage will land before you release. The TX and RX chains are ordered independently; a drag on one chain has no effect on the other.

A static hint below the chain reads: *Click to bypass · Double click to edit · Drag to reorder*.

The chain order and individual stage states are persisted separately for TX and RX via `ClientCompTxChainStages` and `ClientCompRxChainStages`. The last-active tab (TX or RX) is persisted via `PooDooAudioActiveTab`. The container's visibility is persisted via `Applet_TXDSP`.

## What each control does

| Control | Kind | Default | Behavior | Setting key |
|---|---|---|---|---|
| TX | Toggle button | Checked | Shows and makes the TX chain active for editing. Displays amber when selected. | `PooDooAudioActiveTab` |
| RX | Toggle button | Unchecked | Shows and makes the RX chain active for editing. Displays amber when selected. | `PooDooAudioActiveTab` |
| BYPASS | Toggle button | Unchecked | Checked: snapshots currently enabled stages on the active side and disables all of them. Unchecked: re-enables only the stages that were on before. TX and RX maintain separate snapshots. | — |
| Record (⏺) | Toggle button | Unchecked | Captures up to 30 s of post-PUDU TX audio. Click again to stop; playback starts automatically. Pulses red while recording. Only visible in TX mode. Enabled when MIC source is PC, DAX is off, and playback is not running. | — |
| Play (▶) | Toggle button | Unchecked | Plays back the captured PUDU audio. Click again to cancel. Pulses green while playing. Only visible in TX mode. Enabled once a recording exists and recording is not active. | — |
| TX chain stage tile | Drag handle | — | Single-click bypasses the stage; double-click opens its editor; drag reorders the TX chain. | — |
| RX chain stage tile | Drag handle | — | Single-click bypasses the stage; double-click opens its editor; drag reorders the RX chain. | — |
| RADIO status tile | Indicator | — | Greens when PC Audio is enabled. Only visible in RX mode. | — |
| DSP status tile | Indicator | — | Mirrors the active client-side noise reducer (e.g. NR2, NR4, BNR). Shows generic "DSP" when none is active. Only visible in RX mode. | — |
| SPEAK status tile | Indicator | — | Greens when AetherSDR's audio output is unmuted. Only visible in RX mode. | — |

## Tips

- The BYPASS button preserves a snapshot of which stages were enabled. If you manually toggle individual stages while BYPASS is checked, those manual changes are preserved outside the snapshot and will not be automatically restored when you uncheck BYPASS.
- The TX endpoint indicator pulses red while you are transmitting (MOX active), giving a live confirmation that the TX chain is processing audio.
- Switching from TX to RX and back does not affect either chain's stage states or BYPASS snapshot. Each side is fully independent.
- The Record button tooltip reads: "Record up to 30 s of post-PooDoo™ TX audio (MIC must be set to PC and DAX off)." If the button is greyed out, check your MIC source setting and DAX state first.

## Related

- [Switch between editing the TX and RX chains](switch-between-editing-the-tx-and-rx-chains.md)
- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
- [Bypass every RX stage at once](bypass-every-rx-stage-at-once.md)
- [Re-enable a specific stage after a global bypass](re-enable-a-specific-stage-after-a-global-bypass.md)
- [Reorder the TX DSP chain](reorder-the-tx-dsp-chain.md)
- [Reorder the RX DSP chain (independent of TX order)](reorder-the-rx-dsp-chain-independent-of-tx-order.md)
- [Open a stage's frameless floating editor from the chain](open-a-stage-s-frameless-floating-editor-from-the-chain.md)
- [Record up to 30 seconds of post-PUDU TX audio](record-up-to-30-seconds-of-post-pudu-tx-audio.md)
- [Play back the captured PUDU audio](play-back-the-captured-pudu-audio.md)
- [See at a glance whether PC Audio, the noise reducer, and audio output are live (RX status tiles)](see-at-a-glance-whether-pc-audio-the-noise-reducer-and-audio-output-are-live-rx-status-tiles.md)
- [Visually confirm when TX (MOX) is live](visually-confirm-when-tx-mox-is-live.md)
