# Visually confirm when TX (MOX) is live

The Aetherial Audio Chain applet shows a red pulsing indicator on the TX endpoint whenever your slice is transmitting (MOX active). This lets you confirm at a glance that your radio is on the air without looking away from your audio chain.

## Before you start

- The Aetherial Audio Chain applet must be visible. If it is not, click the tray button labelled `PUDU` in the right sidebar to open the Aetherial Audio container.
- Click `TX` in the applet header so the TX chain is the active view.

## Steps

1. Click the `TX` tray button in the applet header to show the TX DSP chain.
2. Key the radio (PTT, VOX, or MOX).
3. Watch the TX endpoint indicator at the far end of the TX chain strip.

The TX endpoint indicator pulses red while your slice is transmitting. When you unkey, the indicator returns to its idle (non-pulsing) state.

## What each control does

| Label | Kind | Behavior |
|---|---|---|
| `TX` | Toggle button | Shows the TX DSP chain. Default: checked. Part of an exclusive pair with `RX`; appears amber when selected. |
| TX endpoint indicator | Indicator | Pulses red while the radio is transmitting on the active slice (driven by MOX state). Idle when not transmitting. |
| `BYPASS` | Toggle button | Checked: snapshots the currently-enabled stages on the active side (TX or RX) and disables all of them. Unchecked: re-enables just the stages that were on before. When the TX side is shown, the button mirrors the engine-owned TX bypass state — toggling `BYPASS` in the Aetherial Channel Strip and toggling it here produce the same result. TX and RX maintain separate snapshots. |
| RX chain stage (EQ / AGC-T / AGC-C / TUBE / PUDU) | Drag handle | Single-click toggles bypass for the RX stage; double-click opens its frameless floating editor in RX mode; drag reorders the RX chain. All five RX stages (EQ, AGC-T/Gate, AGC-C/Comp, Tube, PUDU) are fully implemented. Order is independent of the TX chain. Distinct mime type `application/x-aethersdr-rx-chain-stage` prevents stray drops between the two strips. |

## Editing TX DSP stages

Double-clicking any TX chain stage tile (EQ, COMP, GATE, DESS, TUBE, PUDU, VERB) opens the **Aetherial Audio Channel Strip** — the unified TX DSP window — rather than a per-stage floating editor. This is the canonical way to edit your TX audio processing. Individual stage editors remain accessible from within the channel strip itself.

## Tips

- The TX endpoint indicator is only present in TX mode. Switch to `TX` using the `TX` button in the applet header if you see the RX chain instead.
- The red pulse is driven by the radio's MOX state, so it reflects actual on-air status regardless of how transmit was triggered (hardware PTT, software MOX, VOX).
- The `BYPASS` button on the TX side stays in sync with the channel strip's own bypass control. Whichever you click last is authoritative.

## Related

- [Aetherial Audio Chain overview](overview.md)
- [Switch between editing the TX and RX chains](switch-between-editing-the-tx-and-rx-chains.md)
- [See at a glance whether PC Audio, the noise reducer, and audio output are live (RX status tiles)](see-at-a-glance-whether-pc-audio-the-noise-reducer-and-audio-output-are-live-rx-status-tiles.md)