# PooDoo Audio Chain overview

The PooDoo Audio Chain applet shows the TX DSP signal flow as a horizontal strip of processing stages. Use it to bypass, reorder, or open editors for individual stages, and to capture a short post-processing audio sample to audition your TX sound.

## Before you start

- The PooDoo Audio (TXDSP) container must be visible. If it is not, click the tray button labelled **PUDU** in the right sidebar to toggle it on.
- No radio connection is required to view or configure the chain. Some features (record, playback) require the mic input source to be set to PC with DAX off.

## How it works

The applet appears as the top section of the TXDSP container. It has two layers: a header row of controls, and below that, the chain strip itself.

**Header row**

The header row contains the mode buttons, monitor buttons, and the BYPASS button, left to right.

- **TX** and **RX** are exclusive toggle buttons that select which chain view is shown. TX is selected by default (amber highlight). Selecting RX shows the placeholder text "Client RX chain — coming in a future phase"; no stage processing is available in that view.
- The **Record** button (⏺) and **Play** button (▶) are the post-PUDU monitor recorder controls, described below.
- **BYPASS** sits at the far right of the header row.

**Chain strip**

Below the header, each DSP stage appears as a draggable tile in signal-flow order. The default stage order is: Eq, Comp, Gate, DeEss, Tube, Enh (PUDU), Reverb. A static hint line below the strip reads "Click to bypass · Double click to edit · Drag to reorder".

Each stage tile responds to three interactions:

| Interaction | Result |
|---|---|
| Single-click | Toggles bypass for that stage only |
| Double-click | Opens that stage's floating editor |
| Drag | Moves the stage to a new position in the chain |

The chain order and stage enable states are persisted in `ClientCompTxChainStages`. Whether the TXDSP container is shown is persisted in `Applet_TXDSP`.

## What each control does

| Control | Default | Behavior |
|---|---|---|
| **TX** | Selected | Displays the interactive TX DSP chain. Amber highlight when active. |
| **RX** | Not selected | Displays the RX placeholder. BYPASS is a no-op in this mode. |
| **BYPASS** | Unchecked | When checked: snapshots which stages are currently enabled and disables all of them. When unchecked: re-enables only the stages that were on before the snapshot. Stages toggled individually while BYPASS was active are not affected by the restore. |
| **Record** (⏺) | Disabled | Captures up to 30 seconds of post-PUDU TX audio. Click again to stop early; playback starts automatically when recording stops. Enabled only when the mic input is set to PC and playback is not active. Pulses red while recording. |
| **Play** (▶) | Disabled | Plays back the most recently captured audio. Click again to cancel. Enabled only when a recording exists and recording is not active. Pulses green during playback. |
| **Chain stage (Eq)** | — | Single-click bypasses/restores EQ; double-click opens the EQ editor; drag to reorder. |
| **Chain stage (Comp)** | — | Single-click bypasses/restores the compressor; double-click opens the compressor editor; drag to reorder. |
| **Chain stage (Gate)** | — | Single-click bypasses/restores the gate; double-click opens the gate editor; drag to reorder. |
| **Chain stage (DeEss)** | — | Single-click bypasses/restores the de-esser; double-click opens the de-ess editor; drag to reorder. |
| **Chain stage (Tube)** | — | Single-click bypasses/restores the tube saturator; double-click opens the tube editor; drag to reorder. |
| **Chain stage (Enh / PUDU)** | — | Single-click bypasses/restores the PUDU exciter; double-click opens the PUDU editor; drag to reorder. |
| **Chain stage (Reverb)** | — | Single-click bypasses/restores the reverb; double-click opens the reverb editor; drag to reorder. |

## Tips

- The TX endpoint indicator pulses red in the chain strip while your slice is transmitting (MOX active), giving you a live confirmation that TX is hot.
- BYPASS is intended for quick A/B comparisons. Because it snapshots the enabled stages at the moment you check it, you can safely toggle individual stages during a bypass without losing your original configuration on restore.
- The Record button requires the mic source to be set to PC and DAX to be off. If the button is dimmed, check those two conditions first.

## Related

- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
- [Re-enable a specific stage after a global bypass](re-enable-a-specific-stage-after-a-global-bypass.md)
- [Reorder the TX DSP chain](reorder-the-tx-dsp-chain.md)
- [Open a stage's floating editor from the chain](open-a-stage-s-floating-editor-from-the-chain.md)
- [Record up to 30 seconds of post-PUDU TX audio](record-up-to-30-seconds-of-post-pudu-tx-audio.md)
- [Play back the captured PUDU audio](play-back-the-captured-pudu-audio.md)
- [Switch between TX chain view and RX placeholder](switch-between-tx-chain-view-and-rx-placeholder.md)
- [Visually confirm when TX (MOX) is live](visually-confirm-when-tx-mox-is-live.md)
