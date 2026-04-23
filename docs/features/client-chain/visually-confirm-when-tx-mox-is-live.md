# Visually confirm when TX (MOX) is live

The PooDoo Audio Chain applet includes a TX endpoint indicator that pulses red whenever your slice is transmitting. This lets you confirm at a glance that MOX is active without looking away from the chain.

## Before you start

- The PooDoo Audio (TXDSP) container must be open. If it is not visible, click the PUDU tray button in the right sidebar to show it.
- The TX mode must be selected in the applet. The TX button should be checked (amber). If it is not, click TX.
- Your radio must be connected.

## Steps

1. Open the PooDoo Audio container by clicking the PUDU tray button in the right sidebar.
2. Confirm the TX button at the top of the applet is checked. If not, click TX.
3. Key your transmitter (PTT, MOX, or VOX).
4. Watch the TX endpoint indicator in the chain strip. It pulses red while your slice is transmitting.
5. Release PTT. The red pulse stops and the indicator returns to idle.

## What each control does

| Control | Behavior | Default | Setting key |
|---|---|---|---|
| TX | Selects TX chain view; required for the TX endpoint indicator to be visible | Checked | — |
| RX | Switches to the RX placeholder view; TX endpoint indicator is not shown | Unchecked | — |
| TX endpoint indicator | Pulses red while the radio is transmitting on your slice (driven by MOX state) | Idle | — |

## Tips

- The red pulse is driven directly by MOX state. It reflects actual transmit activity on your slice, not just a PTT button press.
- If BYPASS is checked while you transmit, the indicator still pulses red. The TX endpoint indicator is independent of the BYPASS state.
- The TX button uses an amber highlight when selected. If the applet header shows RX highlighted instead, click TX first — the endpoint indicator is only present in TX mode.

## Troubleshooting

- **Indicator does not pulse red when transmitting** — Confirm the TX button is checked, not RX. The indicator is not shown in RX mode.
- **PUDU tray button is not visible** — Open the applet panel via View > Applet Panel, then locate the PUDU tray button in the right sidebar.
- **Applet shows no chain strip, only a placeholder** — The RX button is selected. Click TX to switch back to the TX chain view.

## Related

- [PooDoo Audio Chain overview](overview.md)
- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
- [Switch between TX chain view and RX placeholder](switch-between-tx-chain-view-and-rx-placeholder.md)
