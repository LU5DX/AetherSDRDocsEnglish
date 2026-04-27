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

| Label | Kind | Behavior | Persisted setting |
|---|---|---|---|
| `TX` | Toggle button | Shows the TX DSP chain. Default: checked. Part of an exclusive pair with `RX`; appears amber when selected. | `PooDooAudioActiveTab` = `TX` |
| TX endpoint indicator | Indicator | Pulses red while the radio is transmitting on the active slice (driven by MOX state). Idle when not transmitting. | — |

## Tips

- The TX endpoint indicator is only present in TX mode. Switch to `TX` using the `TX` button in the applet header if you see the RX chain instead.
- The red pulse is driven by the radio's MOX state, so it reflects actual on-air status regardless of how transmit was triggered (hardware PTT, software MOX, VOX).

## Related

- [Aetherial Audio Chain overview](overview.md)
- [Switch between editing the TX and RX chains](switch-between-editing-the-tx-and-rx-chains.md)
- [See at a glance whether PC Audio, the noise reducer, and audio output are live (RX status tiles)](see-at-a-glance-whether-pc-audio-the-noise-reducer-and-audio-output-are-live-rx-status-tiles.md)
