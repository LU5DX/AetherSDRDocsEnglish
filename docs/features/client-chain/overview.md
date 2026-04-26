# PooDoo Audio Chain overview

The PooDoo Audio Chain applet shows the TX DSP signal flow as an ordered strip of processing stages. It lets you bypass, reorder, and edit each stage without leaving the main window, and provides a built-in monitor recorder to audition the processed audio before transmitting.

## Before you start

- Open the PooDoo Audio container by clicking the PUDU tray button in the right sidebar. The chain applet is always visible at the top of that container when the container is enabled.
- No radio connection is required to configure the chain.

## How it works

The chain applet displays up to seven processing stages in a horizontal strip: Eq, Comp, Gate, DeEss, Tube, Enh (PUDU), and Reverb. Audio flows left to right through whatever stages are currently active. The stage order is yours to change by dragging.

A single-row header sits above the strip containing the TX/RX mode selector, the post-PUDU monitor recorder buttons, and the BYPASS toggle. A static hint line below the strip reads "Click to bypass · Double click to edit · Drag to reorder".

The active stage order and the enabled/bypassed state of each stage are persisted in `ClientCompTxChainStages`. Whether the PooDoo Audio container itself is shown is persisted in `Applet_TXDSP`.

**TX mode** is the fully implemented path. Clicking TX makes the chain strip interactive and shows the hint line.

**RX mode** currently shows a placeholder ("Client RX chain — coming in a future phase"). BYPASS has no effect in RX mode.

## What each control does

| Label | Kind | Default | Behavior |
|---|---|---|---|
| TX | Toggle button | Checked | Switches to the TX DSP chain view. Amber color when selected. |
| RX | Toggle button | Unchecked | Switches to the RX chain view. Currently a placeholder only. |
| BYPASS | Toggle button | Unchecked | Checked: snapshots all currently-enabled stages and disables them all. Unchecked: re-enables exactly the stages that were on before the snapshot. Stages toggled individually while BYPASS is active are preserved outside the snapshot. |
| Record (⏺) | Toggle button | Unchecked | Captures up to 30 s of post-PUDU TX audio. Click again to stop; playback starts automatically. Enabled only when the mic input is set to PC and DAX is off, and playback is not running. Pulses red while recording. |
| Play (▶) | Toggle button | Unchecked | Plays back the most recent captured recording. Click again to cancel. Enabled only once a recording exists and recording is not active. Pulses green while playing. |
| Chain stage (Eq) | Drag handle | — | Single-click toggles bypass for the EQ stage. Double-click opens the EQ editor. Drag to reorder. |
| Chain stage (Comp) | Drag handle | — | Single-click toggles bypass for the compressor. Double-click opens the compressor editor. Drag to reorder. |
| Chain stage (Gate) | Drag handle | — | Single-click toggles bypass for the gate. Double-click opens the gate editor. Drag to reorder. |
| Chain stage (DeEss) | Drag handle | — | Single-click toggles bypass for the de-esser. Double-click opens the de-ess editor. Drag to reorder. |
| Chain stage (Tube) | Drag handle | — | Single-click toggles bypass for the tube saturator. Double-click opens the tube editor. Drag to reorder. |
| Chain stage (Enh / PUDU) | Drag handle | — | Single-click toggles bypass for the PUDU exciter. Double-click opens the PUDU editor. Drag to reorder. |
| Chain stage (Reverb) | Drag handle | — | Single-click toggles bypass for the reverb. Double-click opens the reverb editor. Drag to reorder. |

## Tips

- The TX endpoint indicator pulses red while you are transmitting on your own slice, giving you a live confirmation that MOX is active without leaving the audio chain view.
- The Record button is disabled whenever DAX is on or the mic source is not set to PC. Check both conditions if the button remains grayed out.
- Stages you toggle individually while BYPASS is checked are tracked separately. When you uncheck BYPASS, only the stages that were enabled before you engaged BYPASS are restored.

## Related

- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
- [Re-enable a specific stage after a global bypass](re-enable-a-specific-stage-after-a-global-bypass.md)
- [Reorder the TX DSP chain](reorder-the-tx-dsp-chain.md)
- [Open a stage's floating editor from the chain](open-a-stage-s-floating-editor-from-the-chain.md)
- [Record up to 30 seconds of post-PUDU TX audio](record-up-to-30-seconds-of-post-pudu-tx-audio.md)
- [Play back the captured PUDU audio](play-back-the-captured-pudu-audio.md)
- [Switch between TX chain view and RX placeholder](switch-between-tx-chain-view-and-rx-placeholder.md)
- [Visually confirm when TX (MOX) is live](visually-confirm-when-tx-mox-is-live.md)
