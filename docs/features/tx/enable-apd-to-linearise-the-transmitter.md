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

| Control | Kind          | Behavior                                                                                 |
|---------|---------------|------------------------------------------------------------------------------------------|
| APD     | Toggle button | Enables or disables adaptive pre-distortion on the radio. Green when on, unlit when off. |
| Active  | Indicator     | Lit green when APD is on and the equaliser is actively applied to the signal.            |
| Cal     | Indicator     | Lit green when APD is on and the radio is still calibrating.                             |
| Avail   | Indicator     | Lit green when APD is on and a calibration is available but not yet applied.             |

The normal progression after enabling APD is: Cal → Avail → Active.

## Tips

- APD calibration takes place automatically after you enable it. You do not need to transmit manually to trigger it; wait for the indicators to step through Cal → Avail → Active.
- If you disable and re-enable APD, the calibration sequence restarts from Cal.

## ATU button behaviour

The ATU button uses a per-frequency toggle that mirrors SmartSDR behaviour:

- **First click** (or any click after a frequency change): starts a new ATU tune cycle.
- **Second click at the same frequency**, when the ATU reports a successful match: switches the tuner to bypass.
- **Click after any frequency change**: always starts a fresh tune cycle, even if the previous status was successful.

The bypass state is cleared automatically when the transmit frequency changes, so the next click will start a new tune rather than bypassing. There is no change to the ATU button label or appearance; the **Success**, **Byp**, and **Mem** indicators below the button continue to reflect ATU status as before.

| Indicator | Kind      | Behavior                                                          |
|-----------|-----------|-------------------------------------------------------------------|
| Success   | Indicator | Lights green when the ATU reports a successful or OK match.       |
| Byp       | Indicator | Lights orange when the ATU is in bypass or manual bypass.         |
| Mem       | Indicator | Lights green when the ATU is using a stored memory.               |

### ATU right-click menu

Right-click the ATU button to open a context menu with two actions:

| Action                       | Behavior                                                                                     |
|------------------------------|----------------------------------------------------------------------------------------------|
| Pre-tune bands…              | Opens the ATU Pre-Tune dialog to sweep and store tuner settings across bands. Enabled only when MEM is on. |
| Clear ATU memories…          | Clears all stored ATU memories on the radio. A confirmation dialog appears before clearing.  |

## TUNE button behaviour

Click TUNE to start or stop a tune carrier. The button label changes to **TUNING...** with a red background while the carrier is active.

### TUNE right-click menu

Right-click the TUNE button to choose the carrier shape for the next tune cycle:

| Action      | Behavior                                                                                          |
|-------------|---------------------------------------------------------------------------------------------------|
| Mono Tone   | Sets the tune carrier to a single tone. Checked if this is the current mode.                      |
| Two Tone    | Sets the tune carrier to two tones. Checked if this is the current mode.                          |

The selection is a one-shot transient — the radio's tune mode reverts to single tone across power cycles. AetherSDR does not persist the choice in AppSettings.

## RF Power / Tune Power sliders

| Control    | Kind   | Behavior                                                                                                                                                                                                                                                                      |
|------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RF Power   | Slider | Sets the transmit RF power level as a percentage of maximum (0–100%). Default: 100%. During drag, displays the current value as "XX%" above the slider handle. The value snaps to the last set position after release.                                                          |
| Tune Pwr   | Slider | Sets the tune-carrier power level as a percentage of maximum (0–100%). Default: 10%. During drag, displays the current value as "XX%" above the slider handle. The value snaps to the last set position after release.                                                          |

When you release either slider, the value synchronises from the radio model, ensuring the displayed value matches the actual radio state even if the radio rejected the intermediate value during the drag.

## TX Profile selector

Select a TX profile from the combo box to load it on the radio. Profiles are populated from the radio's profile list.

## RF Pwr and SWR meters

Forward power is displayed as a horizontal bar gauge. The scale changes based on the radio model (barefoot 0–120 W, or Aurora 500W 0–600 W). The gauge turns red above 100 W (barefoot) or 500 W (Aurora).

PEP peak-hold: a peak reading is held for 2 seconds, then decays smoothly to the current value. The peak is cleared immediately when the transmitter unkeys to prevent lingering readings across overs.

Hover the mouse over the RF Pwr gauge to see the exact power reading in watts (e.g., "45 W").

SWR is displayed as a horizontal bar gauge. Range 1.0–3.0. The gauge turns red above 2.5.

Hover the mouse over the SWR gauge to see the exact ratio in conventional form (e.g., "1.52:1").

## MOX button and Quindar tones

Clicking MOX routes through the Quindar-tone coordinator rather than toggling the transmitter directly. This means:

- **Engage (click MOX on):** if Quindar is enabled in the Audio Channel Strip and the active TX slice is on a phone mode, the K-tone plays before the transmitter keys.
- **Disengage (click MOX off):** the BK-tone plays after the transmitter unkeys.
- If Quindar is disabled, or the active TX slice is not on a phone mode, MOX behaves as before and keys the transmitter immediately.

The MOX button has a distinct appearance even when idle (amber border and text) to distinguish it from the TUNE/ATU/MEM buttons. The button turns red while the transmitter is keyed and returns to its amber accent when the transmitter is off. The accent colours are theme-editable via `color.tx.mox.*` tokens.

| Control | Kind          | Behavior                                                                                                                                                      |
|---------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MOX     | Toggle button | Toggles manual transmit. Routes through the Quindar-tone coordinator so K/BK tones play on PTT engage/disengage in phone modes when Quindan is enabled. Button goes red while TX is keyed, amber accent when idle. |

## ATU MEM button

| Control | Kind          | Behavior                                                                        |
|---------|---------------|---------------------------------------------------------------------------------|
| MEM     | Toggle button | Toggles ATU memory recall on/off. Disabled when TGXL is in OPERATE mode.       |

## Theme support

Starting with v26.6.1, the TX Controls applet uses theme-aware colours for all controls and indicators. Slider fill, label colours, and indicator states adapt to the active theme. If you use a custom theme, these controls will respect the `applet/tx` scope in the theme definition.

The MOX button and RF Pwr/SWR gauges also support theme tokens. The MOX button uses `color.tx.mox.border`, `color.tx.mox.text`, `color.tx.mox.border.hover`, and `color.tx.mox.text.hover` for its idle accent colouring. The gauge hover tooltips use the theme's default tooltip styling.

## Related

- [TX Controls overview](overview.md)
- [Run a Two-Tone Tune](run-a-two-tone-tune.md)
- [Set RF output power](set-rf-output-power.md)