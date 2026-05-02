# Set RF output power

Use the RF Power slider in the TX Controls applet to set the transmit power level sent to your antenna. Adjusting this before transmitting prevents overdriving your amplifier or violating band power limits.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. If not, go to `Settings > Connect to Radio...`.
- The TX Controls applet must be visible. If it is not, click the **TX** tray button on the right sidebar to show it.

## Steps

1. Locate the **RF Power** slider in the TX Controls applet. It appears below the **SWR** gauge.
2. Drag the slider left or right to set your desired power level. The numeric readout to the right of the slider updates immediately.
3. Confirm the value shown in the readout is what you intend. The **RF Pwr** gauge will reflect actual forward power once you transmit.

## What each control does

| Control             | Description                                          | Default |
|---------------------|------------------------------------------------------|---------|
| **RF Power** slider | Sets the transmit RF power level sent to the radio.  | 100     |
| **RF Pwr** meter    | Displays actual forward power at the exciter output. | —       |
| **SWR** meter       | Displays standing wave ratio at the exciter.         | —       |

## Tips

- The **RF Pwr** meter scale changes automatically depending on your radio model. On a standard FLEX-8600 the red zone begins above 100 W.
- You can set per-band power limits independently of this slider. Go to `Settings > TX Band Settings...` to configure power, tune power, and inhibit settings for each band.
- The **RF Power** slider controls the exciter output level, not a separate amplifier. If you are running an external amplifier, set this slider to the drive level your amplifier expects.

## Using the ATU button

The **ATU** button behavior changed in v0.9.5.1 to mirror the per-frequency toggle found in SmartSDR.

- **First click** (or any click after a frequency change): starts a fresh ATU tune cycle.
- **Second click at the same frequency**: if the tuner already reports a successful match (the **Success** indicator is lit) and you have not changed frequency since the last tune, clicking **ATU** again switches the tuner to bypass instead of starting a new cycle.
- **After any frequency change**: the tuned-frequency record is cleared automatically. The next click always starts a fresh tune cycle, even if the prior status was successful.

The **Byp** indicator lights orange when the tuner is in bypass. The **Success** indicator lights green when a match is active. The **Mem** indicator lights green when the tuner is using a stored memory.

| Scenario | ATU button result |
|---|---|
| No prior tune, or frequency has changed | Starts tune cycle |
| Success/OK match, same frequency as last tune | Switches to bypass |
| Bypass active | Starts fresh tune cycle on next click |

> **Note:** The **ATU** and **MEM** buttons are disabled when the TGXL transverter is in OPERATE mode.

## Troubleshooting

- **RF Pwr meter shows 0 W during transmit** — Confirm the radio is actually keyed. Check that MOX is active (the **MOX** button is red) or that your PTT line is asserted. Also verify the **RF Power** slider is not set to 0.
- **Slider moves but forward power does not change** — The radio connection may have dropped. Check the connection status and reconnect via `Settings > Connect to Radio...` if needed.
- **ATU button starts a fresh tune even though Success was lit** — Confirm you have not changed transmit frequency since the last tune. Any frequency change clears the stored tuned-frequency record and forces a new tune cycle.

## Related

- [TX Controls overview](overview.md)
- [Set tune-carrier power](set-tune-carrier-power.md)
- [Start a tune carrier to check SWR](start-a-tune-carrier-to-check-swr.md)
- [Toggle MOX to manually key the transmitter](toggle-mox-to-manually-key-the-transmitter.md)
- [Switch TX profiles (e.g. SSB, Digital)](switch-tx-profiles-e-g-ssb-digital.md)