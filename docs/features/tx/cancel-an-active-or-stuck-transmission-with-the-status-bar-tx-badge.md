# Cancel an active or stuck transmission with the status bar TX badge

The status bar TX badge gives you a single click to drop the transmitter out of TX — useful when MOX is stuck on, a tune carrier is still running, or any other condition has left the radio keyed and the TX Controls applet is not immediately to hand.

## Before you start

- AetherSDR must be connected to the radio. The TX badge only appears in the status bar when a radio connection is active.
- The radio must currently be in a transmitting state (MOX keyed or tune carrier active) for the badge to be actionable.

## Steps

1. Locate the TX badge in the AetherSDR status bar at the bottom of the main window. The badge is visible and lit when the radio is transmitting.
2. Click the TX badge once.
3. Confirm the radio has returned to receive: the RF Pwr gauge in the TX Controls applet drops to zero, the MOX button returns to its unlit state (blue), and the TUNE button label returns to "TUNE" if a tune carrier was running.

## Tips

- If the TX Controls applet is visible, you can also click MOX to toggle transmit off, or click TUNE to stop an active tune carrier (the button reads "TUNING..." while active). The status bar TX badge is the fastest path when the applet is collapsed or out of view.
- If MOX was engaged by an external CAT or TCI command, clicking the TX badge sends the same unkey command. The source of the original PTT does not matter.

## Troubleshooting

- **Clicking the TX badge does not stop transmission** — The radio may be keyed by hardware PTT (footswitch or microphone PTT line). Release the hardware PTT first; software commands cannot override a held hardware PTT line.
- **TX badge is not visible during transmission** — The status bar may be hidden. Check that the main window is not in Minimal Mode (`View > Minimal Mode`). Disabling Minimal Mode restores the status bar.

## Related

- [Toggle MOX to manually key the transmitter](toggle-mox-to-manually-key-the-transmitter.md)
- [Start a tune carrier to check SWR](start-a-tune-carrier-to-check-swr.md)
- [TX Controls overview](overview.md)

***

# TX Controls overview

The TX Controls applet provides the primary interface for transmit operations: meters for forward power and SWR, sliders for RF power and tune power (displayed as percentage), a TX profile selector, and buttons for TUNE, MOX, ATU, MEM, and APD (Adaptive Pre-Distortion).

## Before you start

- AetherSDR must be connected to a FlexRadio FLEX-8600 with firmware 4.2 or later.
- The radio must be in an operational state (not in standby or offline).

## Controls

### RF Pwr (Forward Power Meter)

- Displays forward power at the exciter output in watts.
- Scale changes based on radio model: 0–120 W (barefoot) or 0–600 W (with Aurora 500W amplifier).
- Red zone indicates >100 W (barefoot) or >500 W (with amplifier).
- The meter includes a **peak-hold bar** that captures the maximum PEP value during transmission. The peak holds for 2 seconds, then decays toward the current power level at approximately 2.5 seconds from peak to floor.
- When not transmitting, the meter rests at zero. When the transmitter is unkeyed, both the live reading and the peak-hold bar drop to zero immediately, so no stale power sample lingers on screen.
- Hover the mouse cursor over the gauge to see an exact numeric readout in the format "X W" (e.g., "75 W").

### SWR (Standing Wave Ratio Meter)

- Displays SWR at the exciter output.
- Range 1.0–3.0, with red zone indicating >2.5.
- When not transmitting, the gauge rests at 1.0 (minimum). When the transmitter is unkeyed, the gauge returns to 1.0 immediately.
- If an SWR reading is unavailable during transmit, the gauge also rests at 1.0 rather than displaying a raw zero or a stale ratio.
- Hover the mouse cursor over the gauge to see an exact numeric readout in the format "N.N:1" (e.g., "1.32:1").

### RF Power Slider

- Sets the transmit RF power level as a percentage (0–100), which maps to watts based on the radio's power scale.
- Calls `TransmitModel::setRfPower` when adjusted.
- When dragging the slider, a tooltip displays the current value in the format "X%" (e.g., "75%").
- When you finish dragging (release the mouse button), the value is synchronized from the radio model to ensure accurate display.

### Tune Pwr Slider

- Sets the tune carrier power level as a percentage (0–100), which maps to watts based on the radio's power scale.
- Calls `TransmitModel::setTunePower` when adjusted.
- When dragging the slider, a tooltip displays the current value in the format "X%" (e.g., "10%").
- When you finish dragging (release the mouse button), the value is synchronized from the radio model to ensure accurate display.

### TX Profile Combo Box

- Selects a transmit profile from the list provided by the radio (`profileList()`).
- Changing the profile calls `TransmitModel::loadProfile`.

### ATU Indicators

Three status LEDs indicate the ATU state:

- **Success** — Lights green when ATU status is `Successful` or `OK`.
- **Byp** — Lights orange when ATU is in `Bypass` or `ManualBypass`.
- **Mem** — Lights green when ATU is using a memory.

### TUNE Button

- Starts or stops a tune carrier. The button label changes to "TUNING..." with a red background while active.
- **Right-click** to open a context menu for selecting the carrier shape for the next tune cycle:
  - **Mono Tone** — Traditional single-tone carrier.
  - **Two Tone** — Two-tone carrier for intermodulation distortion testing.
  
  The selection is a transient one-shot — it applies only to the next TUNE press and is not persisted in AppSettings. The radio's `tune_mode` reverts to `single_tone` across power cycles.
- The button is marked as a TX-keying control in the UI (emits a tune carrier).

### MOX Button

- Toggles manual transmit on/off. The button turns red while TX is keyed.
- When Quindar tones are enabled in the Audio Channel Strip, the K and BK tones play on engage and disengage in phone modes.
- The button is marked as a TX-keying control in the UI (manual PTT).
- **Idle appearance:** When not transmitting, the MOX button displays an amber border and amber text accent, distinguishing it from the neutral TUNE, ATU, and MEM buttons. This accent is customizable in the Theme Editor using the tokenized colors `color.tx.mox.border`, `color.tx.mox.text`, `color.tx.mox.border.hover`, and `color.tx.mox.text.hover`.

### ATU Button

- Starts the internal ATU tuning cycle.
- If the ATU status is `Successful` or `OK` at the current frequency, a second click sends a bypass instead.
- **Disabled** when the radio has no antenna tuner (e.g., a Hermes-Lite 2) or when TGXL is in OPERATE mode. Hover over the disabled button to see why:
  - **"This radio has no antenna tuner"** — The radio does not have an ATU fitted. The no-tuner reason is reported first because it is the more fundamental condition, even if TGXL is also in OPERATE mode.
  - **"Disabled — TGXL is in OPERATE mode"** — The radio has a tuner, but TGXL is in OPERATE mode.
- The button is marked as a TX-keying control in the UI (starts ATU tune).
- **Right-click** to open a context menu with two options:
  - **Pre-tune bands…** — Opens a dialog to run the ATU pre-tune sweep across user-selected bands. This action requires MEM to be enabled first; if MEM is off, the menu item is grayed out with a tooltip.
  - **Clear ATU memories…** — Prompts for confirmation and then clears all ATU memories from the radio.

### MEM Button

- Toggles ATU memory recall on/off.
- **Disabled** when the radio has no antenna tuner or when TGXL is in OPERATE mode. The tooltip explains the reason, using the same logic as the ATU button.

### APD Button and Status Cluster

- **APD** — Toggle button that enables or disables Adaptive Pre-Distortion on the radio.
- Three status indicators show the APD state:
  - **Active** — Lit green when APD is on and the equalizer is actively applied.
  - **Cal** — Lit green when APD is on and still calibrating.
  - **Avail** — Lit green when APD is on and a calibration is available but not yet applied.
  
  The typical progression is: Cal (calibrating) → Avail (ready) → Active (applied).
- The APD button and status cluster are hidden on radios that do not support APD. On a cold launch, the cluster does not appear until the radio confirms it is APD-capable — it never shows a live-looking button with no backing functionality.

## Peak-Hold Behavior

The forward power meter includes a peak-hold feature that captures the maximum PEP (Peak Envelope Power) during a transmission. The peak-hold bar:

- Updates instantly when a new peak is detected.
- Holds the peak value for 2 seconds.
- After the hold period, decays toward the current smoothed power level. The decay rate is scaled to the gauge's full-scale range (120 W or 600 W), so the visual feel (~2.5 seconds from peak to floor) is consistent across both scales.
- Resets to zero immediately when the transmitter is unkeyed (MOX released or TUNE stopped). This prevents a held PEP reading from lingering across overs.

When the transmitter is unkeyed, the live power reading also drops to zero immediately — the last sample is not left painted on the gauge.

## TX-Keying Control Markers

The TUNE, MOX, and ATU buttons are internally marked as TX-keying controls (`markTxKeying`). This marker is used by the `TxKeyingMarker` utility to identify controls that can key the transmitter. The marker does not change the visible appearance of the buttons but is used internally for consistent behavior across the application.

## Related

- [Cancel an active or stuck transmission with the status bar TX badge](cancel-an-active-or-stuck-transmission-with-the-status-bar-tx-badge.md)
- [Toggle MOX to manually key the transmitter](toggle-mox-to-manually-key-the-transmitter.md)
- [Start a tune carrier to check SWR](start-a-tune-carrier-to-check-swr.md)