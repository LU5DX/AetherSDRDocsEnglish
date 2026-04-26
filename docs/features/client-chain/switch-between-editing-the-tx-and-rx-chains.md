# Switch between editing the TX and RX chains

The Aetherial Audio Chain applet shows either the TX or RX DSP chain at a time. Use the TX and RX toggle buttons to select which chain is visible and editable. Your last-used selection is restored when you reopen AetherSDR.

## Before you start

- The Aetherial Audio (TXDSP) container must be open. If it is not visible, click the tray button labelled PUDU in the right sidebar to show it.
- Both chains are available without a radio connection.

## Steps

1. Locate the header row at the top of the Aetherial Audio Chain applet. It contains two mode buttons: TX and RX.
2. Click TX to show and edit the TX DSP chain (Parametric EQ, Compressor, Gate, De-Ess, Tube, PUDU, Reverb).
3. Click RX to show and edit the RX DSP chain (RX EQ, AGC-T, AGC-C, Dynamic Tube, RX PUDU), along with the RADIO, DSP, and SPEAK status tiles.
4. The selected button turns amber. The previously visible chain hides and the newly selected chain appears in its place.

Your selection persists across sessions via `PooDooAudioActiveTab`.

## What each control does

| Control | Kind | Default | Behavior | Persisted setting |
|---|---|---|---|---|
| TX | Toggle button | Checked | Shows and enables editing of the TX DSP chain. Amber when selected. | `PooDooAudioActiveTab` = `TX` |
| RX | Toggle button | Unchecked | Shows and enables editing of the RX DSP chain. Amber when selected. | `PooDooAudioActiveTab` = `RX` |

TX and RX form an exclusive pair — only one can be selected at a time. Each side keeps its own independent stage state, chain order, and BYPASS snapshot. The stage order in the TX chain (`ClientCompTxChainStages`) has no effect on the RX chain order (`ClientCompRxChainStages`), and vice versa.

## Tips

- The BYPASS button always acts on whichever chain is currently shown. Check which mode is active before engaging BYPASS to avoid silencing the wrong chain.
- The Record and Play monitor buttons are visible only in TX mode; they are hidden when RX is selected.
- The hint text below the chain strip — "Click to bypass · Double click to edit · Drag to reorder" — applies to both TX and RX modes.

## Related

- [Aetherial Audio Chain overview](overview.md)
- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
- [Bypass every RX stage at once](bypass-every-rx-stage-at-once.md)
- [Reorder the TX DSP chain](reorder-the-tx-dsp-chain.md)
- [Reorder the RX DSP chain (independent of TX order)](reorder-the-rx-dsp-chain-independent-of-tx-order.md)
- [See at a glance whether PC Audio, the noise reducer, and audio output are live (RX status tiles)](see-at-a-glance-whether-pc-audio-the-noise-reducer-and-audio-output-are-live-rx-status-tiles.md)
