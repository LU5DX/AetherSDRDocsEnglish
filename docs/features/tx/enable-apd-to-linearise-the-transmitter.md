# Enable APD to linearise the transmitter

APD (Adaptive Pre-Distortion) reduces transmitter non-linearity by calibrating and applying an equalizer to the exciter output. Enable it when you want to improve signal quality and reduce spurious emissions on transmit.

## Before you start

- AetherSDR must be connected to the radio. APD requires an active radio connection.
- The TX applet must be visible in the Applet Panel. If it is not, click the TX tray button on the right sidebar.

## Steps

1. In the Applet Panel, locate the row at the bottom of the TX Controls applet containing the APD button.
2. Click APD. The button background turns green when APD is on.
3. Watch the status indicators to the right of APD:
   - **Cal** lights green while the radio is calibrating.
   - **Avail** lights green when a calibration has completed but is not yet applied.
   - **Active** lights green when the equalizer is applied and pre-distortion is running.

No further action is required. The radio progresses from Cal to Avail to Active automatically.

To disable APD, click APD again. The button returns to its default (unlit) state and all three indicators dim.

## What each control does

| Control | Kind | Behavior | Default |
|---|---|---|---|
| APD | Toggle button | Enables or disables adaptive pre-distortion on the radio. Green background when on. | Off |
| Active | Indicator | Lit green when APD is on and the equalizer is actively applied. | Dim |
| Cal | Indicator | Lit green when APD is on and still calibrating. | Dim |
| Avail | Indicator | Lit green when APD is on and a calibration result is available but not yet applied. | Dim |

## Tips

- The three indicators show progression in order: Cal → Avail → Active. If the indicator stays on Cal for an extended period, the radio may still be gathering data from live transmissions.
- APD operates on the exciter output. Check the RF Pwr and SWR meters during normal operation to confirm the transmitter is working within its expected range before enabling APD.

## Related

- [TX Controls overview](overview.md)
- [Set RF output power](set-rf-output-power.md)
- [Start a tune carrier to check SWR](start-a-tune-carrier-to-check-swr.md)
