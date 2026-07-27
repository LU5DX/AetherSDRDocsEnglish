# Aetherial Audio Chain overview

The Aetherial Audio Chain applet gives you a visual, interactive view of AetherSDR's client-side DSP signal processing. Use it to monitor, bypass, reorder, and edit the stages that shape your transmitted and received audio before it reaches the radio or your speakers.

## Before you start

- The Aetherial Audio container must be visible. Click the tray button labelled "PUDU" in the right sidebar to toggle it. The chain applet appears as the top section of that container.
- No radio connection is required to view or edit the chains.

## How it works

The applet presents two independent DSP chains — TX and RX — as a horizontal strip of stage tiles. Only one chain is shown at a time. Use the TX and RX buttons to switch between them.

**TX chain** processes audio on the transmit path through these stages in order: EQ, COMP, GATE, DESS, TUBE, PUDU, VERB.

**RX chain** processes received audio through: EQ, AGC-G, AGC-C, DESS, TUBE, EVO. The RX strip is bookended by three non-interactive status tiles — RADIO, ADSP, and SPEAK — that show at a glance whether the receive path is live end to end. All six RX stages are fully implemented.

Each stage tile supports three interactions:

- **Single-click** — toggles bypass for that stage only.
- **Double-click** — opens the stage's editor (see behaviour differences between TX and RX below).
- **Drag** — reorders the stage within its chain. A vertical cyan bar shows where the stage will land before you release. The TX and RX chains are ordered independently; a drag on one chain has no effect on the other.

A static hint below the chain reads: *Click to bypass · Double click to edit · Drag to reorder*.

### Double-click behaviour by chain

**TX chain:** Double-clicking any TX stage tile opens the Aetherial Audio Channel Strip — the unified TX DSP window. This is the canonical way to edit your TX audio from the chain. Individual per-stage floating editors remain accessible from within the channel strip itself.

**RX chain:** Double-clicking an RX stage tile opens that stage's own frameless floating editor directly, as before.

### BYPASS and the audio engine

The BYPASS button is synchronised with the BYPASS control in the Aetherial Audio Channel Strip on the TX side, and with the audio engine on both sides. Clicking BYPASS in either location updates both. When you switch the applet between TX and RX sides, the BYPASS button reflects the engine's current bypass state for that side.

The chain order and individual stage states are persisted separately for TX and RX via `ClientCompTxChainStages` and `ClientCompRxChainStages`. The last-active tab (TX or RX) is persisted via `PooDooAudioActiveTab`. The container's visibility is persisted via `Applet_TXDSP`.

### Click discrimination interval

The chain widgets use a configurable click discrimination interval instead of the system double-click interval. This interval is set in the Interaction Settings and determines how long the widget waits after a mouse release to decide whether the action was a single click (bypass toggle) or the start of a double-click (open editor). Adjusting this interval in the Interaction Settings affects how responsive the chain tiles feel.

## What each control does

| Control                   | Kind                                                                                                                     | Default                                                                                                                              |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| TX                        | Shows and edits the TX DSP chain (ClientChainWidget) — fully interactive: click-bypass, double-click-edit, drag-reorder. | Part of an exclusive pair with RX; amber 'VUDU' colour when selected. Last-active tab persists via PooDooAudioActiveTab='TX' / 'RX'. |
| RX                        | Toggle button                                                                                                            | Unchecked                                                                                                                            |
| BYPASS                    | Toggle button                                                                                                            | Unchecked                                                                                                                            |
| Record (⏺)                | Toggle button                                                                                                            | Unchecked                                                                                                                            |
| Play (▶)                  | Toggle button                                                                                                            | Unchecked                                                                                                                            |
| TX chain stage tile       | Drag handle                                                                                                              | —                                                                                                                                    |
| RX chain stage tile       | Drag handle                                                                                                              | —                                                                                                                                    |
| RADIO status tile         | Indicator                                                                                                                | —                                                                                                                                    |
| ADSP status / bypass tile | Toggle button                                                                                                            | Unchecked                                                                                                                            |
| SPEAK status tile         | Indicator                                                                                                                | —                                                                                                                                    |
### TX

Switches the applet to show and edit the TX DSP chain. The button is styled in amber ("PooDoo" colour) when selected. The last-active tab is persisted via `PooDooAudioActiveTab`.

### RX

Switches the applet to show and edit the RX DSP chain. Each side keeps independent stage state, chain order, and BYPASS snapshot. The last-active tab is persisted via `PooDooAudioActiveTab`.

### BYPASS

Checked: snapshots the currently-enabled stages on the active side (TX or RX), including RN2, and disables all of them. Unchecked: re-enables just the stages that were on before. TX and RX maintain separate snapshots.

On both TX and RX sides, BYPASS state is owned by the audio engine and is kept in sync across the chain applet and any other UI controls that manage bypass (such as the Aetherial Audio Channel Strip). The button reflects the engine's actual bypass state whenever you are viewing either chain.

Stages toggled manually while BYPASS is active are preserved outside the snapshot and will not be automatically restored when you uncheck BYPASS.

Note: The BYPASS scope is global (per audio engine), not per-profile. The button stays pressed across Channel Strip profile switches.

### Record (⏺)

Captures up to 30 seconds of post-PUDU TX audio. Click again to stop; playback starts automatically. Only enabled when the mic input source is set to PC and DAX is off. Pulses red while recording. Hidden in RX mode.

Tooltip: *Record up to 30 s of post-PooDoo™ TX audio (MIC must be set to PC and DAX off).*

### Play (▶)

Plays back the captured PUDU audio. Click again to cancel. Only enabled once a recording exists and recording is not currently active. Pulses green while playing. Hidden in RX mode.

### TX chain stage tile (EQ / COMP / GATE / DESS / TUBE / PUDU / VERB)

Single-click toggles bypass for that stage. Double-click opens the Aetherial Audio Channel Strip (the unified TX DSP window). Drag reorders the TX chain.

### RX chain stage tile (EQ / AGC-G / AGC-C / DESS / TUBE / EVO)

Single-click toggles bypass for that stage. Double-click opens the stage's frameless floating editor. Drag reorders the RX chain. All six RX stages are fully implemented. Order is independent of the TX chain. A distinct drag mime type (`application/x-aethersdr-rx-chain-stage`) prevents accidental drops between the two strips.

### RADIO status tile

Non-interactive. Only visible in RX mode. Turns green when PC Audio (the standard SSB stream) is enabled.

### ADSP status / bypass tile

Interactive. Only visible in RX mode. Mirrors which client-side noise reducer is currently active. The label rotates to the active module's short name (for example, `NR2`, `NR4`, `BNR`, or `NVAFX`). Falls back to `ADSP` when no noise reducer is on. Single-click bypasses the entire NR cluster with an in-memory snapshot; single-click again restores the prior NR state. Double-click opens the AetherDSP Settings dialog. Adopts the same blue-ring + green-LED-dot styling as implemented stage tiles. Snapshot restoration falls back to NR2 if no modules were active at bypass-time.

Note: The `NVAFX` module is treated as the equivalent of the legacy `BNR` module for snapshot and restore purposes. When bypassing, if NVAFX is active it will be disabled along with all other NR modules. Upon restore, if the saved snapshot indicates BNR was active, NVAFX will be enabled instead.

### SPEAK status tile

Non-interactive. Only visible in RX mode. Turns green when AetherSDR's audio output is unmuted.

## Tips

- The BYPASS button on both TX and RX sides is synchronised with the audio engine. Clicking BYPASS in any location that offers it has the same effect for the currently-active chain.
- If you manually toggle individual stages while BYPASS is checked, those changes are preserved outside the snapshot and will not be automatically restored when you uncheck BYPASS.
- The TX endpoint indicator pulses red while you are transmitting (MOX active), giving a live confirmation that the TX chain is processing audio.
- Switching from TX to RX and back does not affect either chain's stage states or BYPASS snapshot. Each side is fully independent.
- The Record button tooltip reads: "Record up to 30 s of post-PooDoo™ TX audio (MIC must be set to PC and DAX off)." If the button is greyed out, check your MIC source setting and DAX state first.
- Double-clicking a TX stage tile now opens the full Aetherial Audio Channel Strip rather than a per-stage editor. Access individual stage editors from within the strip.
- The ADSP tile's label updates dynamically to show which noise reducer module is currently active, or falls back to "ADSP" when no module is engaged. The NVAFX module is labelled as "NVAFX" when active.
- The click discrimination interval used by chain tiles is configured in Interaction Settings. Adjust it if the tiles feel too sensitive or not responsive enough when distinguishing single clicks from double clicks.
- The BYPASS scope is global (per audio engine), not per-profile. Switching profiles in the Channel Strip will not reset the BYPASS state.
- BYPASS also disables the RN2 module on the TX side, and restoration re-enables RN2 if it was active when bypass was engaged.

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