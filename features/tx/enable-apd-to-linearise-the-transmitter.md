# Enable APD to linearise the transmitter

APD (Adaptive Pre-Distortion) reduces transmitter non-linearity by applying a correction equalizer to the output signal. Enable it when you want to improve signal quality and reduce IMD products on air.

## Before you start

- AetherSDR must be connected to the radio. APD is a radio-side function and requires an active connection.
- The TX applet must be visible in the Applet Panel. If it is not, click the TX tray button on the right sidebar.

## Steps

1. Locate the APD button at the bottom of the TX Controls applet.
2. Click APD. The button background turns green when APD is enabled.
3. Watch the status indicators to the right of APD:
   - **Cal** lights green while the radio is collecting calibration data.
   - **Avail** lights green when a calibration is ready but not yet applied.
   - **Active** lights green when the equalizer is applied and APD is fully operational.
4. Wait for **Active** to light. No further action is required.

To disable APD, click APD again. The button returns to its unlit state and all three indicators dim.

## What each control does

| Control | Kind | Behavior | Default |
|---|---|---|---|
| APD | Toggle button | Enables or disables Adaptive Pre-Distortion on the radio. Green when on, unlit when off. | Off |
| Active | Indicator | Lit green when APD is on and the equalizer is actively applied to the transmit signal. | Dim |
| Cal | Indicator | Lit green when APD is on and the radio is still collecting calibration data. | Dim |
| Avail | Indicator | Lit green when APD is on and a calibration result is available but not yet applied. | Dim |

The normal progression after enabling APD is: **Cal** → **Avail** → **Active**.

## Tips

- If **Cal** stays lit for an extended time, transmitting (even briefly with MOX or TUNE) gives the radio signal data to complete calibration faster.
- APD state is controlled at the radio level. If you disconnect and reconnect, AetherSDR will reflect whatever APD state the radio currently holds.

## Related

- [TX Controls overview](overview.md)
- [Start a tune carrier to check SWR](start-a-tune-carrier-to-check-swr.md)
- [Toggle MOX to manually key the transmitter](toggle-mox-to-manually-key-the-transmitter.md)
