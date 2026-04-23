# PooDoo Audio Chain Overview

The PooDoo Audio Chain applet shows your TX DSP signal flow as an interactive strip of processing stages. Use it to bypass, reorder, and edit individual stages, or to capture and review a short sample of your processed TX audio.

## Before you start

- Open the PooDoo Audio container by clicking the PUDU tray button in the right sidebar. The chain applet is always visible at the top of that container when the tile is enabled.
- A radio connection is not required to view or arrange the chain, but audio processing requires an active audio engine.

## How it works

The applet header contains three controls — TX, RX, and BYPASS — followed by the record and play monitor buttons. Below the header is the chain strip itself, showing each processing stage as a draggable tile. A static hint line below the strip reads "Click to bypass · Double click to edit · Drag to reorder".

The TX button is selected by default. In TX mode the full chain strip is interactive. Clicking RX switches to a placeholder that reads "Client RX chain — coming in a future phase"; no stage editing or bypass is available in that mode.

The chain runs audio through up to seven stages in the order shown in the strip: Eq, Comp, Gate, DeEss, Tube, Enh (PUDU), and Reverb. Each stage can be individually bypassed, opened for editing, or dragged to a new position. Stage order and enabled states are persisted in `ClientCompTxChainStages`. The visibility state of the container itself is persisted in `Applet_TXDSP`.

When you are transmitting, the TX endpoint indicator pulses red in the chain strip, driven by your slice's MOX state.

## What each control does

| Control | Kind | Default | Behavior |
|---|---|---|---|
| TX | Toggle button | Checked | Switches to the TX DSP chain view. Amber color when selected. |
| RX | Toggle button | Unchecked | Switches to the RX chain placeholder. BYPASS is a no-op in this mode. |
| BYPASS | Toggle button | Unchecked | Checked: snapshots all currently-enabled stages and disables them all. Unchecked: re-enables exactly the stages that were on before the snapshot. Stages toggled manually while BYPASS was active are preserved outside the snapshot. |
| Record (⏺) | Toggle button | Unchecked | Captures up to 30 s of post-PUDU TX audio. Click again to stop; playback starts automatically. Pulses red while recording. Enabled only when MIC source is set to PC, DAX is off, and playback is not running. |
| Play (▶) | Toggle button | Unchecked | Plays back the captured audio. Click again to cancel. Pulses green while playing. Enabled only once a recording exists and recording is not active. |
| Chain stage (Eq) | Drag handle | — | Single-click toggles bypass for the EQ stage. Double-click opens the EQ editor. Drag to reorder. |
| Chain stage (Comp) | Drag handle | — | Single-click toggles bypass for the compressor. Double-click opens the compressor editor. Drag to reorder. |
| Chain stage (Gate) | Drag handle | — | Single-click toggles bypass for the gate. Double-click opens the gate editor. Drag to reorder. |
| Chain stage (DeEss) | Drag handle | — | Single-click toggles bypass for the de-esser. Double-click opens the de-ess editor. Drag to reorder. |
| Chain stage (Tube) | Drag handle | — | Single-click toggles bypass for the tube saturator. Double-click opens the tube editor. Drag to reorder. |
| Chain stage (Enh / PUDU) | Drag handle | — | Single-click toggles bypass for the PUDU exciter. Double-click opens the PUDU editor. Drag to reorder. |
| Chain stage (Reverb) | Drag handle | — | Single-click toggles bypass for the reverb. Double-click opens the reverb editor. Drag to reorder. |

## Tips

- While BYPASS is active you can still toggle individual stages. Those per-stage changes are not included in the bypass snapshot and will persist after you uncheck BYPASS.
- The Record button stays enabled while recording so you can click it a second time to stop early.
- The hint line "Click to bypass · Double click to edit · Drag to reorder" is only shown in TX mode.

## Related

- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
- [Re-enable a specific stage after a global bypass](re-enable-a-specific-stage-after-a-global-bypass.md)
- [Reorder the TX DSP chain](reorder-the-tx-dsp-chain.md)
- [Open a stage's floating editor from the chain](open-a-stage-s-floating-editor-from-the-chain.md)
- [Record up to 30 seconds of post-PUDU TX audio](record-up-to-30-seconds-of-post-pudu-tx-audio.md)
- [Play back the captured PUDU audio](play-back-the-captured-pudu-audio.md)
- [Switch between TX chain view and RX placeholder](switch-between-tx-chain-view-and-rx-placeholder.md)
- [Visually confirm when TX (MOX) is live](visually-confirm-when-tx-mox-is-live.md)
