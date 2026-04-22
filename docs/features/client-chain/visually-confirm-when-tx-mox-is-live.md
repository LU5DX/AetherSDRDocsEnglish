# Visually confirm when TX (MOX) is live

The PooDoo Audio Chain applet shows a visual indicator whenever your slice is transmitting. Use this to confirm at a glance that MOX is active without looking away from the chain strip.

## Before you start

- The PooDoo Audio (TXDSP) container must be visible. If it is not, click the `PUDU` tray button in the right sidebar to show it.
- The TX mode must be selected in the applet (TX is selected by default).

## Steps

1. Click the `PUDU` tray button in the right sidebar if the PooDoo Audio container is not already open.
2. Confirm that the TX button at the top of the applet is selected (it shows amber text and border when active). If it is not, click TX.
3. Key the transmitter (MOX on). The TX endpoint indicator at the right end of the chain strip pulses red while your slice is transmitting.
4. Release MOX. The red pulse stops and the indicator returns to idle.

## What each control does

| Control | Behavior | Default | Setting key |
|---|---|---|---|
| TX | Selects the TX DSP chain view; required for the TX endpoint indicator to be visible. | Checked | — |
| TX endpoint indicator | Pulses red while MOX is active on your own slice. Returns to idle when transmission ends. | Idle | — |

## Tips

- The red pulse is driven by the radio's MOX state for your own slice. It does not reflect other slices or other connected clients.
- If the PooDoo Audio container closes between sessions, AetherSDR restores its visibility from the `Applet_TXDSP` setting.

## Troubleshooting

- **The TX endpoint indicator does not pulse red during transmit** — Confirm the TX button is selected, not RX. The indicator is only visible in TX mode. Also confirm the PooDoo Audio container is fully expanded and not scrolled out of view.
- **The chain strip is not visible** — Click the `PUDU` tray button to open the container, then click TX to switch to the TX chain view.

## Related

- [PooDoo Audio Chain overview](overview.md)
- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
- [Switch between TX chain view and RX placeholder](switch-between-tx-chain-view-and-rx-placeholder.md)
