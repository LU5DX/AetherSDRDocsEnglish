# Visually confirm when TX (MOX) is live

The Aetherial Audio Chain applet shows a red pulsing indicator on the TX endpoint whenever your slice is actively transmitting. This gives you an at-a-glance confirmation that MOX is live without looking away from the chain.

## Before you start

- The Aetherial Audio Chain applet must be visible. If it is not, click the `PUDU` tray button in the right sidebar to enable the container.
- The TX chain must be shown. Click TX in the applet header if RX is currently selected.
- Your radio must be connected and a slice must be active.

## Steps

1. Open the Aetherial Audio Chain applet by clicking the `PUDU` tray button in the right sidebar.
2. Click `TX` in the applet header to show the TX chain. The TX button turns amber when selected.
3. Key the transmitter using your normal method (PTT, MOX, or keyboard shortcut).
4. Watch the TX endpoint indicator at the end of the TX chain strip. It pulses red while your slice is transmitting.
5. Release the transmitter. The red pulse stops and the indicator returns to its idle state.

## What each control does

| Control | Kind | Behavior | Default |
|---|---|---|---|
| `TX` | Toggle button | Shows and edits the TX DSP chain. Amber when selected. Last-active tab persists via `PooDooAudioActiveTab`. | Checked |
| `RX` | Toggle button | Shows and edits the RX DSP chain. Hides the TX endpoint indicator. Last-active tab persists via `PooDooAudioActiveTab`. | Unchecked |
| TX endpoint indicator | Indicator | Pulses red while the active slice is transmitting (MOX on). Returns to idle when transmission ends. | Idle |

## Tips

- The TX endpoint indicator is only visible when the `TX` chain is shown. Switching to `RX` hides it. If you need to monitor TX state while editing RX settings, switch back to `TX` first.
- The red pulse is driven by the transmit state of your own slice only. Other operators in a multiFLEX session do not trigger it.

## Related

- [Aetherial Audio Chain overview](overview.md)
- [Switch between editing the TX and RX chains](switch-between-editing-the-tx-and-rx-chains.md)
- [See at a glance whether PC Audio, the noise reducer, and audio output are live (RX status tiles)](see-at-a-glance-whether-pc-audio-the-noise-reducer-and-audio-output-are-live-rx-status-tiles.md)
