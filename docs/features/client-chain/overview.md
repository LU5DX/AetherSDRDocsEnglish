# Aetherial Audio Chain overview

The Aetherial Audio Chain is AetherSDR's client-side DSP pipeline. It lets you shape both your transmitted and received audio through a sequence of processing stages that you can reorder, bypass individually, or bypass all at once — without touching the radio's own DSP settings.

## Before you start

- Open the Aetherial Audio container by clicking the PUDU tray button in the right applet panel. The chain applet is always visible as the top section of that container when it is enabled.
- A radio connection is not required to configure the chain, but audio processing only takes effect when audio is flowing.

## How it works

The applet presents two independent processing chains — TX and RX — in a horizontal strip of stage tiles. Use the TX and RX toggle buttons to switch which chain is shown and edited. Only one chain is visible at a time; both retain their own stage order, bypass states, and editor settings independently.

### TX chain

The TX chain runs left to right through up to seven stages:

| Stage | Description |
|---|---|
| EQ | Parametric equalizer applied to outgoing audio |
| COMP | Compressor |
| GATE | Noise gate |
| DESS | De-esser |
| TUBE | Tube saturation |
| PUDU | PooDoo™ voice processing |
| VERB | Reverb |

### RX chain

The RX chain runs through up to five user-controllable stages, bracketed by three read-only status tiles:

| Stage / Tile | Description |
|---|---|
| RADIO status tile | Indicates whether PC Audio (the standard SSB stream) is enabled |
| EQ | Receive equalizer |
| GATE | AGC-T gate |
| COMP | AGC-C compressor |
| TUBE | Dynamic tube |
| PUDU | PooDoo™ receive processing |
| DSP status tile | Mirrors the active noise reducer (e.g. NR2, NR4, BNR); shows DSP when none is active |
| SPEAK status tile | Indicates whether AetherSDR's audio output is unmuted |

The RADIO, DSP, and SPEAK tiles are non-interactive indicators. They appear only when the RX chain is shown.

### Interacting with stages

Each stage tile supports three interactions, summarised in the hint line below the chain:

- **Single-click** — toggles bypass on that stage only.
- **Double-click** — opens the stage's frameless floating editor.
- **Drag** — reorders the chain. A vertical cyan bar between tiles shows where the stage will land before you release. TX and RX use separate drag types, so a TX stage cannot be accidentally dropped into the RX chain.

### Global BYPASS

BYPASS disables every stage on the currently shown chain at once. When you check BYPASS, AetherSDR snapshots which stages were enabled and turns them all off. Unchecking BYPASS re-enables exactly those stages. Stages you toggle manually while BYPASS is checked are not included in the snapshot. TX and RX maintain separate bypass snapshots; the checked state shown tracks whichever side is currently visible.

### Post-PUDU TX monitor

Two small icon buttons to the right of the TX/RX toggles let you record and play back a short capture of your transmit audio as it exits the PUDU stage:

- The **⏺** (Record) button captures up to 30 seconds of post-PUDU TX audio. Click it again to stop early; playback starts automatically. It pulses red while recording. It is enabled only when the mic input is set to PC and DAX is off, and playback is not already running.
- The **▶** (Play) button plays back the last capture. Click it again to cancel. It pulses green while playing. It is enabled only once a recording exists and recording is not active.

Both buttons are hidden when the RX chain is shown.

### TX activity indicator

While you are transmitting (MOX active), the TX chain strip pulses red to confirm the live transmit path.

## What each control does

| Control | Kind | Default | Persisted setting | Notes |
|---|---|---|---|---|
| TX | Toggle button | Checked | `PooDooAudioActiveTab` | Shows and edits the TX chain. Amber highlight when selected. Last-active tab persists as `TX` or `RX`. |
| RX | Toggle button | Unchecked | `PooDooAudioActiveTab` | Shows and edits the RX chain, including the RADIO / DSP / SPEAK status tiles. |
| BYPASS | Toggle button | Unchecked | — | Snapshots and disables all currently-enabled stages on the active chain. Uncheck to restore them. TX and RX snapshots are independent. |
| ⏺ (Record) | Toggle button | Unchecked | — | Records up to 30 s of post-PUDU TX audio. Click again to stop. Pulses red while active. TX only. |
| ▶ (Play) | Toggle button | Unchecked | — | Plays back the captured audio. Click again to cancel. Pulses green while active. TX only. |
| TX / RX chain stage tiles | Drag handles | — | `ClientCompTxChainStages` / `ClientCompRxChainStages` | Single-click to bypass, double-click to edit, drag to reorder. |
| RADIO status tile | Indicator | — | — | Greens when PC Audio is enabled. RX mode only. |
| DSP status tile | Indicator | — | — | Shows the active noise reducer short name (e.g. NR2, NR4, BNR), or DSP when none is on. RX mode only. |
| SPEAK status tile | Indicator | — | — | Greens when AetherSDR's audio output is unmuted. RX mode only. |

The `Applet_TXDSP` setting controls whether the Aetherial Audio container (which hosts this applet) is shown at all.

## Tips

- TX and RX chain orders are saved independently. Reordering one chain does not affect the other.
- You can drag stages into any order you want on either chain. The cyan drop indicator shows the exact insertion point before you release.
- The post-PUDU recorder is useful for checking how your processing chain sounds without needing a second station. Make sure your mic source is set to PC and DAX is off before recording, or the Record button will remain disabled.
- BYPASS is per-chain. Checking BYPASS while viewing TX does not affect the RX chain's bypass state.

## Troubleshooting

- **The ⏺ (Record) button is greyed out** — The mic input is not set to PC, DAX is enabled, or playback is currently running. Check your audio input settings and ensure DAX is off before attempting to record.
- **Dragging a TX stage does not land on the RX strip** — This is by design. The two chains use incompatible drag types to prevent accidental cross-chain drops.
- **BYPASS is checked but some stages are still bypassed after unchecking** — Stages you toggled manually while BYPASS was active are not part of the snapshot and will not be automatically restored. Re-enable them individually.

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
