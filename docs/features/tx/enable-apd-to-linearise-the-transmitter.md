# Enable APD to Linearise the Transmitter

APD (Adaptive Pre-Distortion) reduces transmitter non-linearity by applying a correction equalizer to the TX signal. Enable it to improve spectral purity, particularly on SSB and digital modes.

## Before you start

- AetherSDR must be connected to the radio. APD requires an active radio connection.
- Open the TX Controls applet if it is not already visible.

## Steps

1. Click the **TX** tray button on the right sidebar to open the TX Controls applet, if it is not already shown.
2. Click **APD**. The button background turns green when enabled.
3. Watch the status indicators to the right of **APD**:
   - **Cal** lights green while the radio is calibrating.
   - **Avail** lights green when a calibration result is available but not yet applied.
   - **Active** lights green when the equalizer is applied and APD is fully operational.
4. When **Active** is lit, APD is running. No further action is required.
5. To disable APD, click **APD** again. The button returns to its unlit state and all three indicators go dim.

## What each control does

| Control | Kind | Behavior | Default |
|---|---|---|---|
| **APD** | Toggle button | Enables or disables adaptive pre-distortion on the radio. Green when on, unlit when off. | Off |
| **Active** | Indicator | Lit green when APD is on and the equalizer is actively applied to the TX signal. | Dim |
| **Cal** | Indicator | Lit green when APD is on and the radio is still calibrating. | Dim |
| **Avail** | Indicator | Lit green when APD is on and a calibration is available but not yet applied. | Dim |

## Tips

- The normal progression after enabling APD is: **Cal** → **Avail** → **Active**. If the indicator stalls at **Cal** or **Avail**, transmitting a signal gives the radio data to complete calibration.
- APD state is controlled on the radio itself. If you disconnect and reconnect, the indicator states will reflect whatever the radio reports.

## Related

- [TX Controls overview](overview.md)
- [Set RF output power](set-rf-output-power.md)
- [Switch TX profiles (e.g. SSB, Digital)](switch-tx-profiles-e-g-ssb-digital.md)
