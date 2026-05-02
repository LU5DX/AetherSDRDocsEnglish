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

| Control | Kind | Behavior |
|---------|------|----------|
| APD | Toggle button | Enables or disables adaptive pre-distortion on the radio. Green when on, unlit when off. |
| Active | Indicator | Lit green when APD is on and the equaliser is actively applied to the signal. |
| Cal | Indicator | Lit green when APD is on and the radio is still calibrating. |
| Avail | Indicator | Lit green when APD is on and a calibration is available but not yet applied. |

The normal progression after enabling APD is: Cal → Avail → Active.

## Tips

- APD calibration takes place automatically after you enable it. You do not need to transmit manually to trigger it; wait for the indicators to step through Cal → Avail → Active.
- If you disable and re-enable APD, the calibration sequence restarts from Cal.

## ATU button behaviour

Starting with v0.9.5.1, the ATU button uses a per-frequency toggle that mirrors SmartSDR behaviour:

- **First click** (or any click after a frequency change): starts a new ATU tune cycle.
- **Second click at the same frequency**, when the ATU reports a successful match: switches the tuner to bypass.
- **Click after any frequency change**: always starts a fresh tune cycle, even if the previous status was successful.

The bypass state is cleared automatically when the transmit frequency changes, so the next click will start a new tune rather than bypassing. There is no change to the ATU button label or appearance; the **Success**, **Byp**, and **Mem** indicators below the button continue to reflect ATU status as before.

| Indicator | Kind | Behavior |
|-----------|------|----------|
| Success | Indicator | Lights green when the ATU reports a successful or OK match. |
| Byp | Indicator | Lights orange when the ATU is in bypass or manual bypass. |
| Mem | Indicator | Lights green when the ATU is using a stored memory. |

## Related

- [TX Controls overview](overview.md)
- [Run a Two-Tone Tune](run-a-two-tone-tune.md)
- [Set RF output power](set-rf-output-power.md)