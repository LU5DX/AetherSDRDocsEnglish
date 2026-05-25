# TX Controls

The TX Controls applet provides all manual transmit controls in AetherSDR, including forward power and SWR metering (with PEP peak-hold), RF/Tune power sliders, TX profile selection, TUNE/MOX/ATU/MEM buttons, and APD (Adaptive Pre-Distortion) status indicators. In v0.9.7+, the MOX button routes through the Quindar-tone coordinator so the K/BK tones play on PTT engage/disengage when Quindar is enabled (phone modes only).

## Before you start

- AetherSDR must be connected to the radio. The TX applet is unavailable without an active radio connection.
- Open the TX Controls applet: click the TX tray button in the right sidebar if the applet is not already visible.

## Set RF output power

The "RF Power" slider sets the maximum forward power the transmitter will produce during normal operation.

### Steps

1. Locate the "RF Power:" slider in the TX Controls applet.
2. Drag the slider left to decrease or right to increase the power level. The numeric readout to the right of the slider updates immediately.
3. Release the slider. The new value is sent to the radio.

### Meter scale

The RF Pwr meter and SWR meter display real-time readings. A PEP peak-hold bar marks the peak envelope power and decays after a 2-second hold window. The peak resets to zero when the transmitter unkeys.

| Meter  | Scale                          | Red threshold |
|--------|--------------------------------|---------------|
| RF Pwr | 0–120 W (barefoot), 0–600 W (Aurora 500W) | > 100 W / > 500 W |
| SWR    | 1.0–3.0                        | > 2.5         |

## Set tune-carrier power

The "Tune Pwr" slider sets the power level of the continuous carrier transmitted when you press TUNE. Keeping this low protects your finals and antenna system during ATU tuning or SWR checks.

### Steps

1. Locate the "Tune Pwr:" slider in the TX Controls applet.
2. Drag the slider left to decrease or right to increase the tune-carrier power level. The numeric readout to the right of the slider updates immediately.
3. Release the slider. The new value is sent to the radio.

### Drag value display

When dragging either the RF Power or Tune Pwr slider, a tooltip shows the current value in watts (e.g., "45 W") as you move the slider. This helps you set precise power levels without releasing the mouse.

## TX profile selection

1. Locate the "TX Profile:" combo box in the TX Controls applet.
2. Click the combo box to reveal the list of available TX profiles from the radio.
3. Select a profile. The radio loads it immediately.

## TUNE button

1. Click TUNE to start a continuous tune carrier at the level set by "Tune Pwr".
   - The button text changes to "TUNING..." and the background turns red.
2. Click TUNE again or click the TUNE button to stop the carrier.

**Right-click context menu (v26.5.2.1)**:
- Right-click the TUNE button to open a context menu for selecting the carrier shape of the next tune cycle.
- Choose **Mono Tone** or **Two Tone**. The selection is a one-shot: the radio's tune mode reverts to single_tone across power cycles, and AetherSDR does not persist the choice in AppSettings.

## MOX button

1. Click MOX to key the transmitter manually.
   - The button turns red while the transmitter is keyed.
2. Click MOX again to unkey.
   - The button returns to blue.

**Quindar tone behavior (v0.9.7+)**:
- On **engage**: if Quindar is enabled in the Audio Channel Strip and the active TX slice is on a phone mode, the K-tone plays before the transmitter is keyed.
- On **disengage**: the BK-tone plays after the transmitter unkeys.
- If Quindar is disabled, or the active TX slice is not on a phone mode, the behavior is immediate — the transmitter keys and unkeys without tones.

## ATU button

The ATU button starts an internal ATU tuning cycle. As of v0.9.5.1, the ATU button toggles between starting a tune cycle and bypassing the tuner, mirroring the per-frequency behavior in SmartSDR.

### Right-click context menu (v26.5.2.1)

Right-click the ATU button to expose additional tuner actions:

| Menu item | Action |
|---|---|
| **Pre-tune bands…** | Opens the Pre-Tune Bands dialog to sweep tuner memories across bands. Enabled only when MEM is on. |
| **Clear ATU memories…** | Confirms and clears all stored ATU memories. |

### Tune cycle behavior

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

## MEM button

1. Click MEM to toggle ATU memory recall on or off.
   - When on, the Mem indicator lights green.
2. Click MEM again to disable memory recall.

The MEM button is disabled when TGXL is in OPERATE mode.

## ATU status indicators

Three indicators show the current ATU state:

| Indicator | Color | Meaning |
|---|---|---|
| **Success** | Green | ATU status is Successful or OK |
| **Byp** | Orange | ATU is in Bypass or ManualBypass |
| **Mem** | Green | ATU is using a memory |

## APD (Adaptive Pre-Distortion)

1. Click **APD** to toggle adaptive pre-distortion on the radio.
2. Observe the three status indicators:

| Indicator | Color | Meaning |
|---|---|---|
| **Active** | Green | APD is on and the equalizer is actively applied |
| **Cal** | Green | APD is on and still calibrating |
| **Avail** | Green | APD is on and a calibration is available but not yet applied |

The typical progression is: **Cal** (calibrating) → **Avail** (ready) → **Active** (applied).

## What each control does

| Control | Description | Default |
|---|---|---|
| RF Power | Sets the maximum transmit RF power level (W). | 100 |
| Tune Pwr | Sets the tune-carrier power level (W). | 10 |
| TX Profile | Selects a TX profile from the radio. | — |
| TUNE | Starts/stops a tune carrier. Right-click for Mono Tone / Two Tone carrier shape. | — |
| MOX | Toggles manual transmit. | — |
| ATU | Starts an ATU tuning cycle or toggles bypass. Right-click for Pre-tune bands / Clear ATU memories. | — |
| MEM | Toggles ATU memory recall. | — |
| APD | Toggles adaptive pre-distortion. | — |

## Tips

- Set "Tune Pwr" to the minimum level that allows your ATU to find a match. Many operators use 10–20 W for ATU tuning.
- The "Tune Pwr" setting is independent of "RF Power", which controls normal transmit power. Adjusting one does not affect the other.
- You can set per-band tune power defaults in `Settings > TX Band Settings...`.
- The RF Pwr peak-hold bar resets to zero when the transmitter unkeys, preventing a held PEP reading from lingering across overs.

## Related

- [Start a tune carrier to check SWR](start-a-tune-carrier-to-check-swr.md)
- [Run the internal ATU](run-the-internal-atu.md)
- [Set RF output power](set-rf-output-power.md)