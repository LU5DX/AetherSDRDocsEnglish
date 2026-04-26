# Visually confirm when TX (MOX) is live

The PooDoo Audio Chain applet shows a red pulsing indicator on the TX endpoint whenever your slice is transmitting. Use this to confirm at a glance that MOX is active without looking elsewhere in the UI.

## Before you start

- The PooDoo Audio (TXDSP) container must be visible. If it is not, click the `PUDU` tray button in the right sidebar to show it.
- The TX view must be active. The `TX` toggle button in the applet header must be selected (amber highlight). If `RX` is selected instead, click `TX`.

## Steps

1. Click the `PUDU` tray button in the right sidebar to open the PooDoo Audio container if it is not already visible.
2. Confirm the `TX` button in the applet header is checked (amber text and border). If not, click `TX`.
3. Key your transmitter using MOX, PTT, or VOX as you normally would.
4. Watch the TX endpoint indicator at the right end of the chain strip. It pulses red while your slice is transmitting.
5. Release MOX or PTT. The red pulse stops and the indicator returns to idle.

## What each control does

| Control | States | Meaning |
|---|---|---|
| TX endpoint indicator | Idle, red pulse | Pulses red while you are transmitting on your own slice. Driven by the radio's MOX state. Returns to idle when transmission ends. |
| `TX` | Checked (amber), unchecked | Selects the TX chain view. The TX endpoint indicator is only meaningful in this mode. Default: checked. |
| `RX` | Checked (amber), unchecked | Switches to the RX chain placeholder. Default: unchecked. |

## Tips

- The red pulse is independent of the `BYPASS` state. Even if all stages are bypassed, the TX endpoint indicator still reflects the live MOX state.
- If you use the monitor Record (⏺) button to capture post-PUDU audio, that button also pulses red while recording — this is separate from the TX endpoint indicator. Do not confuse the two.

## Troubleshooting

- **The indicator does not pulse when transmitting** — Confirm the PooDoo Audio container is visible and `TX` is the active mode. The indicator is not shown in `RX` mode.
- **The PUDU tray button is not visible** — Open `View > Applet Panel` to ensure the applet panel is displayed, then locate the `PUDU` tray button in the right sidebar.

## Related

- [PooDoo Audio Chain overview](overview.md)
- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
- [Switch between TX chain view and RX placeholder](switch-between-tx-chain-view-and-rx-placeholder.md)
- [Record up to 30 seconds of post-PUDU TX audio](record-up-to-30-seconds-of-post-pudu-tx-audio.md)
