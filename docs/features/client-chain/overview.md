# PooDoo Audio Chain overview

The PooDoo Audio Chain applet shows the TX DSP signal path as a horizontal strip of stages and lets you bypass, reorder, or edit each one. Use it to shape your transmitted audio before it reaches the radio.

## Before you start

- The PooDoo Audio (TXDSP) container must be visible. If it is not, click the tray button labelled **PUDU** in the right sidebar to toggle it on.
- A radio connection is not required to configure the chain, but stages have no effect on audio until a radio is connected and a mic source is active.

## How it works

The applet appears as the top section of the TXDSP container. It presents a header row of controls above a horizontal strip of processing stages. Audio flows left to right through whichever stages are not bypassed.

The chain currently has two modes, selected by the **TX** and **RX** toggle buttons in the header:

- **TX mode** (default) — shows the interactive DSP chain. All stage controls and the hint text "Click to bypass · Double click to edit · Drag to reorder" are active.
- **RX mode** — shows the placeholder message "Client RX chain — coming in a future phase". No stage controls are available and **BYPASS** has no effect.

When you transmit on your own slice, the TX endpoint indicator pulses red to confirm the chain is live.

The chain order and per-stage state are saved to `ClientCompTxChainStages`. Whether the TXDSP container is shown is saved to `Applet_TXDSP`.

## What each control does

| Control | Kind | Default | Behavior |
|---|---|---|---|
| **TX** | Toggle button | Checked | Selects TX chain view. Shown in amber when active. |
| **RX** | Toggle button | Unchecked | Selects RX placeholder view. BYPASS is a no-op in this mode. |
| **BYPASS** | Toggle button | Unchecked | Checked: snapshots enabled stages and disables all of them. Unchecked: restores only the stages that were enabled before the snapshot. Stages toggled manually while BYPASS was active are not affected by the restore. |
| **Record (⏺)** | Toggle button | Unchecked | Captures up to 30 seconds of post-PUDU TX audio. Click again to stop; playback starts automatically. Enabled only when MIC is set to PC, DAX is off, and playback is not running. Pulses red while recording. |
| **Play (▶)** | Toggle button | Unchecked | Plays back the captured audio. Click again to cancel. Enabled only once a recording exists and recording is not active. Pulses green during playback. |
| **Chain stage (Eq)** | Drag handle | — | Single-click toggles bypass for the EQ stage. Double-click opens the EQ editor. Drag to reorder. |
| **Chain stage (Comp)** | Drag handle | — | Single-click toggles bypass for the compressor. Double-click opens the compressor editor. Drag to reorder. |
| **Chain stage (Gate)** | Drag handle | — | Single-click toggles bypass for the gate. Double-click opens the gate editor. Drag to reorder. |
| **Chain stage (DeEss)** | Drag handle | — | Single-click toggles bypass for the de-esser. Double-click opens the de-ess editor. Drag to reorder. |
| **Chain stage (Tube)** | Drag handle | — | Single-click toggles bypass for the tube saturator. Double-click opens the tube editor. Drag to reorder. |
| **Chain stage (Enh / PUDU)** | Drag handle | — | Single-click toggles bypass for the PUDU exciter. Double-click opens the PUDU editor. Drag to reorder. |
| **Chain stage (Reverb)** | Drag handle | — | Single-click toggles bypass for the reverb. Double-click opens the reverb editor. Drag to reorder. |

## Tips

- Stages toggled individually while **BYPASS** is checked are excluded from the automatic restore when you uncheck **BYPASS**. Use individual stage clicks when you want a particular stage to stay off after the global bypass is lifted.
- The **Record (⏺)** button remains enabled while recording so you can click it to stop early. Similarly, **Play (▶)** remains enabled during playback so you can cancel at any time.
- The hint text "Click to bypass · Double click to edit · Drag to reorder" is shown only in TX mode and does not appear when **RX** is selected.

## Related

- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
- [Re-enable a specific stage after a global bypass](re-enable-a-specific-stage-after-a-global-bypass.md)
- [Reorder the TX DSP chain](reorder-the-tx-dsp-chain.md)
- [Open a stage's floating editor from the chain](open-a-stage-s-floating-editor-from-the-chain.md)
- [Record up to 30 seconds of post-PUDU TX audio](record-up-to-30-seconds-of-post-pudu-tx-audio.md)
- [Play back the captured PUDU audio](play-back-the-captured-pudu-audio.md)
- [Switch between TX chain view and RX placeholder](switch-between-tx-chain-view-and-rx-placeholder.md)
- [Visually confirm when TX (MOX) is live](visually-confirm-when-tx-mox-is-live.md)
