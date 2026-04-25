# Visually confirm when TX (MOX) is live

The PooDoo Audio Chain applet includes a TX endpoint indicator that pulses red whenever your slice is transmitting. This page explains where to find it and what it looks like.

## Before you start

- The PooDoo Audio applet must be visible. If it is not, click the **PUDU** tray button in the right sidebar to open the PooDoo Audio container.
- The **TX** mode button must be selected (it is selected by default). The TX endpoint indicator is not active in RX mode.

## Steps

1. Open the PooDoo Audio container by clicking the **PUDU** tray button in the right sidebar.
2. Confirm the **TX** button at the top of the applet is checked. When checked, it shows in amber.
3. Key your transmitter (MOX on). The TX endpoint indicator in the chain strip pulses red while your slice is transmitting.
4. Release MOX. The red pulse stops and the indicator returns to its idle state.

## What each control does

| Control | Description | Default | Setting key |
|---|---|---|---|
| **TX** | Selects the TX DSP chain view. Must be active for the TX endpoint indicator to reflect transmit state. | Checked (amber) | — |
| TX endpoint indicator | Pulses red while the user is transmitting on their own slice. Returns to idle when MOX is released. | Idle | — |

## Tips

- The **TX** button uses the amber PooDoo colour when checked, so you can confirm at a glance that you are viewing the TX chain before keying up.
- The TX endpoint indicator is independent of the **BYPASS** button state. The indicator still pulses red during transmit even when all stages are bypassed.

## Related

- [PooDoo Audio Chain overview](overview.md)
- [Bypass every TX stage at once](bypass-every-tx-stage-at-once.md)
- [Switch between TX chain view and RX placeholder](switch-between-tx-chain-view-and-rx-placeholder.md)
