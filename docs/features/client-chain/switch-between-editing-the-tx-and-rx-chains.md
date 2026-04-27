# Switch between editing the TX and RX chains

The Aetherial Audio Chain applet shows either the TX or RX DSP chain at a time. Use the TX and RX toggle buttons to switch which chain is visible and editable. Your last-used selection is restored when you reopen the applet.

## Before you start

- The Aetherial Audio (TXDSP) container must be visible. If it is not, click the tray button labelled PUDU in the right sidebar to show it.
- The TX chain is shown by default. If you have never changed the selection, clicking RX is all that is needed.

## Steps

1. Locate the header row at the top of the Aetherial Audio Chain applet. It contains the buttons TX, RX, and BYPASS.
2. Click TX to display and edit the TX DSP chain (Parametric EQ, Compressor, Gate, De-Ess, Tube, PUDU, Reverb).
3. Click RX to display and edit the RX DSP chain (RX EQ, AGC-T, AGC-C, Dynamic Tube, RX PUDU), which also shows the RADIO, DSP, and SPEAK status tiles.
4. The selected button turns amber. The chain strip below updates immediately to show the chosen side.

## What each control does

| Control | Kind | Default | Persisted key | Behavior |
|---|---|---|---|---|
| TX | Toggle button | Checked | `PooDooAudioActiveTab` | Shows and makes editable the TX DSP chain. Amber when selected. |
| RX | Toggle button | Unchecked | `PooDooAudioActiveTab` | Shows and makes editable the RX DSP chain. Amber when selected. |

TX and RX form an exclusive pair — only one can be active at a time. The active tab is saved as `PooDooAudioActiveTab` with the value `TX` or `RX` and is restored on next launch.

The TX and RX chains are fully independent: each has its own stage order, per-stage bypass state, and global BYPASS snapshot. Switching sides does not affect the other chain's state. The TX chain order is persisted as `ClientCompTxChainStages`; the RX chain order as `ClientCompRxChainStages`.

## Tips

- The BYPASS button always acts on the currently shown side only. Switching from TX to RX and clicking BYPASS bypasses only the RX chain; the TX chain's bypass state is unchanged.
- The record (⏺) and play (▶) monitor buttons are hidden when RX is selected — they are TX-only features.
- The hint text below the chain strip, "Click to bypass · Double click to edit · Drag to reorder", applies equally to both the TX and RX chains.

## Related

- [Aetherial Audio Chain overview](overview.md)
- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
- [Bypass every RX stage at once](bypass-every-rx-stage-at-once.md)
- [Reorder the TX DSP chain](reorder-the-tx-dsp-chain.md)
- [Reorder the RX DSP chain (independent of TX order)](reorder-the-rx-dsp-chain-independent-of-tx-order.md)
- [See at a glance whether PC Audio, the noise reducer, and audio output are live (RX status tiles)](see-at-a-glance-whether-pc-audio-the-noise-reducer-and-audio-output-are-live-rx-status-tiles.md)
