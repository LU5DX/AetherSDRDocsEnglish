# Enable APD to Linearise the Transmitter

APD (Adaptive Pre-Distortion) reduces transmitter non-linearity by applying a correction equaliser to the signal before it reaches the PA. Enable it to improve spectral purity, particularly on SSB and digital modes.

## Before you start

- AetherSDR must be connected to the radio. APD is a radio-side function and requires an active connection.
- Open the TX Controls applet. If it is not visible, click the TX tray button on the right sidebar.

## Steps

1. Locate the APD button at the bottom of the TX Controls applet.
2. Click APD to toggle adaptive pre-distortion on. The button background changes to green when enabled.
3. Watch the status indicators to the right of the button:
   - **Cal** lights green while the radio is collecting calibration data.
   - **Avail** lights green when a calibration is complete but not yet applied.
   - **Active** lights green when the equaliser is applied to the transmit signal.
4. To turn APD off, click APD again. The button returns to its unlit state and all three indicators go dim.

## What each control does

| Control | Kind | Behavior | Default |
|---------|------|----------|---------|
| APD | Toggle button | Enables or disables adaptive pre-distortion on the radio. Green when on, unlit when off. | Off |
| Active | Indicator | Lit green when APD is on and the equaliser is actively applied to the signal. | Dim |
| Cal | Indicator | Lit green when APD is on and the radio is still calibrating. | Dim |
| Avail | Indicator | Lit green when APD is on and a calibration result is available but not yet applied. | Dim |

The normal progression after enabling APD is: Cal → Avail → Active.

## Tips

- APD calibration takes place automatically after you enable it. You do not need to transmit manually to trigger it; wait for the indicators to step through Cal → Avail → Active.
- If you disable and re-enable APD, the calibration sequence restarts from Cal.

## Related

- [TX Controls overview](overview.md)
- [Run a Two-Tone Tune](run-a-two-tone-tune.md)
- [Set RF output power](set-rf-output-power.md)
