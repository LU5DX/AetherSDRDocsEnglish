# Set RF output power

Use the RF Power slider in the TX Controls applet to set the transmit power level sent to your antenna. Adjusting this before transmitting prevents overdriving your amplifier or violating band power limits.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. If not, go to `Settings > Connect to Radio...`.
- The TX Controls applet must be visible. If it is not, click the **TX** tray button on the right sidebar to show it.

## Steps

1. Locate the **RF Power** slider in the TX Controls applet. It appears below the **SWR** gauge.
2. Drag the slider left or right to set your desired power level. The numeric readout to the right of the slider updates immediately, showing "XX W" format.
3. Confirm the value shown in the readout is what you intend. The **RF Pwr** gauge will reflect actual forward power once you transmit.

## What each control does

| Control             | Description                                          | Default |
|---------------------|------------------------------------------------------|---------|
| **RF Power** slider | Sets the transmit RF power level sent to the radio. Drag value shows "XX W" format. | 100     |
| **Tune Pwr** slider | Sets tune-carrier power level. Drag value shows "XX W" format. | 10     |
| **RF Pwr** meter    | Displays actual forward power at the exciter output.  | —       |
| **SWR** meter       | Displays standing wave ratio at the exciter.         | —       |
| **TX Profile** combo box | Selects a transmit profile (e.g. SSB, Digital) from those available on the radio. | — |

## Tips

- The **RF Pwr** meter scale changes automatically depending on your radio model. On a standard FLEX-8600 the red zone begins above 100 W.
- You can set per-band power limits independently of this slider. Go to `Settings > TX Band Settings...` to configure power, tune power, and inhibit settings for each band.
- The **RF Power** slider controls the exciter output level, not a separate amplifier. If you are running an external amplifier, set this slider to the drive level your amplifier expects.
- The **RF Pwr** meter includes a peak-hold bar that holds the highest PEP reading for 2 seconds, then decays smoothly toward the current power level. The peak immediately clears to zero when the transmitter unkeys.

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

### ATU right-click menu

Right-clicking the **ATU** button opens a context menu with two additional options:

- **Pre-tune bands…** — Opens a dialog to run a pre-tune sweep across one or more bands. This option is only available when ATU memories are enabled (the **MEM** button is on).
- **Clear ATU memories…** — Prompts for confirmation, then clears all stored ATU memories on the radio.

## Using the TUNE button right-click menu

Right-clicking the **TUNE** button opens a context menu to select the carrier shape for the next tune cycle. Two options are available:

- **Mono Tone** — A single carrier tone.
- **Two Tone** — Two simultaneous carrier tones.

Selecting either option is a one-shot setting. The radio's tune mode is stored in volatile state and AetherSDR does not persist this choice across restarts. The currently active mode is shown with a check mark.

## Using the MOX button

The **MOX** button manually keys the transmitter. When active, the button turns red.

In v0.9.7, clicking **MOX** routes the PTT request through the Quindar-tone coordinator rather than keying the radio directly. This means:

- On phone modes (SSB, AM, FM, and so on), if the **QUIN** chip is enabled in the Audio Channel Strip, the K-tone plays when you engage MOX and the BK-tone plays when you disengage it.
- If Quindar is disabled, or the active TX slice is not on a phone mode, the behavior is identical to previous versions: the radio keys and unkeys immediately.

No change to how you operate the button is required. The Quindar tones are controlled entirely by the **QUIN** setting in the Audio Channel Strip.

## Using the APD (Adaptive Pre-Distortion) cluster

The **APD** toggle button enables or disables adaptive pre-distortion on the radio. When APD is on, three status indicators show the progress:

- **Cal** (green) — APD is on and still calibrating.
- **Avail** (green) — A calibration is available but not yet applied.
- **Active** (green) — The equalizer is actively applied.

The typical progression is Cal → Avail → Active. When APD is off, all three indicators are dim.

## Troubleshooting

- **RF Pwr meter shows 0 W during transmit** — Confirm the radio is actually keyed. Check that MOX is active (the **MOX** button is red) or that your PTT line is asserted. Also verify the **RF Power** slider is not set to 0.
- **Slider moves but forward power does not change** — The radio connection may have dropped. Check the connection status and reconnect via `Settings > Connect to Radio...` if needed.
- **ATU button starts a fresh tune even though Success was lit** — Confirm you have not changed transmit frequency since the last tune. Any frequency change clears the stored tuned-frequency record and forces a new tune cycle.
- **Quindar tones do not play when using MOX** — Confirm the active slice is set to a phone mode and that the **QUIN** chip is enabled in the Audio Channel Strip. Quindar tones are suppressed on non-phone modes regardless of the QUIN setting.

## Related

- [TX Controls overview](overview.md)
- [Set tune-carrier power](set-tune-carrier-power.md)
- [Start a tune carrier to check SWR](start-a-tune-carrier-to-check-swr.md)
- [Toggle MOX to manually key the transmitter](toggle-mox-to-manually-key-the-transmitter.md)
- [Switch TX profiles (e.g. SSB, Digital)](switch-tx-profiles-e-g-ssb-digital.md)