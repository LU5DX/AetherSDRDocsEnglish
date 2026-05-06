# Set tune-carrier power

The "Tune Pwr" slider sets the power level of the continuous carrier transmitted when you press TUNE. Keeping this low protects your finals and antenna system during ATU tuning or SWR checks.

## Before you start

- AetherSDR must be connected to the radio. The TX applet is unavailable without an active radio connection.
- Open the TX Controls applet: click the TX tray button in the right sidebar if the applet is not already visible.

## Steps

1. Locate the "Tune Pwr:" slider in the TX Controls applet.
2. Drag the slider left to decrease or right to increase the tune-carrier power level. The numeric readout to the right of the slider updates immediately.
3. Release the slider. The new value is sent to the radio.

## What each control does

| Control  | Description                                        | Default |
|----------|----------------------------------------------------|---------|
| Tune Pwr | Sets the power level of the tune carrier in watts. | 10      |

## Tips

- Set "Tune Pwr" to the minimum level that allows your ATU to find a match. Many operators use 10–20 W for ATU tuning.
- The "Tune Pwr" setting is independent of "RF Power", which controls normal transmit power. Adjusting one does not affect the other.
- You can set per-band tune power defaults in `Settings > TX Band Settings...`.

## ATU button behavior

As of v0.9.5.1, the ATU button toggles between starting a tune cycle and bypassing the tuner, mirroring the per-frequency behavior in SmartSDR.

The exact action taken when you click ATU depends on the current tuner status and your transmit frequency:

| Situation | What ATU click does |
|---|---|
| No successful tune exists for the current frequency | Starts a fresh ATU tune cycle. |
| ATU reports a successful match and transmit frequency has not changed since that tune | Switches the ATU to bypass. |
| ATU reports a successful match but transmit frequency has changed since that tune | Starts a fresh ATU tune cycle. |
| ATU is already in bypass | Starts a fresh ATU tune cycle. |

In practice this means:

1. Click ATU on a new frequency. The radio runs a tune cycle. The Success indicator lights green when a match is found.
2. Click ATU again without changing frequency. The tuner enters bypass. The Byp indicator lights orange and the Success indicator goes dim.
3. Change frequency and click ATU. The radio runs a fresh tune cycle regardless of the previous result.

The ATU button and MEM button are both disabled when TGXL is in OPERATE mode.

## MOX button and Quindar tones (v0.9.7)

As of v0.9.7, clicking MOX routes through the Quindar-tone coordinator rather than keying the transmitter directly. This means:

- On **engage**: if Quindar is enabled in the Audio Channel Strip and the active TX slice is on a phone mode, the K-tone plays before the transmitter is keyed.
- On **disengage**: the BK-tone plays after the transmitter unkeys.
- If Quindar is disabled, or the active TX slice is not on a phone mode, the behavior is identical to previous versions — the transmitter keys and unkeys immediately.

The MOX button itself continues to show blue (receive) and red (transmitting) as before. No configuration is needed in the TX Controls applet; Quindar tone behavior is controlled entirely from the Audio Channel Strip.

## Related

- [Start a tune carrier to check SWR](start-a-tune-carrier-to-check-swr.md)
- [Run the internal ATU](run-the-internal-atu.md)
- [Set RF output power](set-rf-output-power.md)