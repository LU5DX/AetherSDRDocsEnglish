# Change mode (USB, LSB, CW, AM, FM, etc.)

This page explains how to select a receive mode for a slice. Changing the mode reshapes the filter presets and tuning step sizes to suit the new modulation.

## Before you start

- AetherSDR must be connected to the radio. The RX Controls applet requires an active radio connection.
- If you have more than one slice, select the correct slice first using the A..H tab row at the top of the RX Controls applet.

## Steps

1. If the RX Controls applet is not visible, click the **RX** tray button on the right sidebar to show it.
2. If your radio has more than one slice active, click the appropriate slice tab (**A** through **H**) to bind the applet to the slice you want to change.
3. Click the **Mode combo** drop-down. The current mode is shown (default: **USB**).
4. Select the desired mode from the list:
   - **USB**, **LSB**, **CW**, **AM**, **SAM**, **FM**, **NFM**, **DFM**, **DIGU**, **DIGL**, **RTTY**
   - (RADE appears only in builds with RADE support enabled.)
5. The slice switches to the selected mode. The filter width presets and tuning step sizes update automatically to suit the new mode.
6. If you want to use the software WFM demodulator, click the **WFM** button (see below for details).

## WFM (Software FM Demodulator)

The **WFM** button provides a software-based wideband FM demodulation mode. This is not a radio mode – it uses the DAX IQ stream from the slice and routes demodulated audio through the system's Hi-Fi Cable or similar virtual audio device.

**When WFM is active:**
- The **WFM** button lights green.
- The mode combo shows the last selected radio mode (e.g., USB) but the WFM demodulator overrides the radio's audio path.
- The slice's audio is demodulated in software, allowing reception of broadcast FM (88–108 MHz) and other wideband FM signals.

**When you change modes:**
- Selecting any real radio mode (USB, LSB, CW, etc.) automatically deactivates the WFM demodulator.
- The **WFM** button state updates to reflect that WFM is no longer active on this slice.

**When exiting WFM:**
- Click the **WFM** button again to deactivate it. The slice returns to normal radio-mode audio.

**Limitations:**
- WFM requires a DAX IQ channel to be active on the slice.
- The Hi-Fi Cable or equivalent virtual audio device must be configured as the DAX output.
- WFM is not a radio mode – it does not affect the radio's mode or filter settings.

## What each control does

| Control                    | Default          | Valid values                                                                                                                                                                                          |
|----------------------------|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Slice tabs (A..H)**      | —                | 1–8 buttons (capped by hardware max slices). Row hidden if maxSlices ≤ 1.                                                                                                                             |
| **Slice badge**            | A                | A/B/C/D/E/F/G/H, coloured by slice identity.                                                                                                                                                          |
| **🔓 / 🔒**                  | 🔓 (unlocked)     | Toggle button. Toggles tune-lock on the slice; locked slice ignores frequency changes.                                                                                                                |
| **Mode combo**             | USB              | USB, LSB, CW, AM, SAM, FM, NFM, DFM, DIGU, DIGL, RTTY (+ RADE if available)                                                                                                                           |
| **WFM**                    | Off              | Toggle button. Enables software FM demodulation via DAX IQ. Overrides radio audio path.                                                                                                               |
| **Frequency label**        | 0.000.000        | Displays current VFO frequency with dotted grouping. Click to edit.                                                                                                                                   |
| **Frequency edit**         | —                | Enter MHz (0.001–54.000 MHz, up to 450.000 MHz on XVTR). Escape cancels and restores previous frequency.                                                                                              |
| **STEP**                   | 100 Hz (index 2) | Per-mode list (e.g. SSB: 1, 10, 50, 100, 500, 1000, 2000, 3000 Hz; CW: 1, 5, 10, 50, 100, 200, 400 Hz; FM family: 50–12500 Hz)                                                                        |
| **Filter width presets**   | Mode-dependent   | USB/LSB: 1800/2100/2400/2700/2900/3300 Hz; CW: 50/100/250/400 Hz; AM/SAM: 5600–14000 Hz; DIGU/DIGL: 100–2000 Hz; RTTY: 250–1000 Hz. Hidden for FM/NFM/DFM.                                            |
| **Filter passband widget** | —                | Drag lo/hi edges to adjust filter passband.                                                                                                                                                           |
| **Tone mode (FM)**         | Off              | Off, CTCSS TX. Visible only in FM family modes.                                                                                                                                                       |
| **CTCSS tone value**       | —                | 41 standard EIA/TIA-603 tones (67.0 Hz to 254.1 Hz). Enabled only when Tone mode = CTCSS TX.                                                                                                          |
| **Offset (FM)**            | 0.0 MHz          | Spinbox (0.0–100.0 MHz, step 0.1). Sets FM repeater offset frequency.                                                                                                                                 |
| **− (offset down)**        | —                | Toggle button. Sets repeater offset direction to down (TX below RX).                                                                                                                                  |
| **Simplex**                | checked          | Toggle button. Sets repeater offset to simplex (TX = RX).                                                                                                                                             |
| **+ (offset up)**          | —                | Toggle button. Sets repeater offset direction to up (TX above RX).                                                                                                                                    |
| **REV**                    | —                | Toggle button. Inverts the TX offset sign for reversed repeater pairs.                                                                                                                                |
| **🔊 / 🔇 (mute)**           | 🔊 (unmuted)      | Push button. Single-click mutes/unmutes this slice. Double-click mutes/unmutes all owned slices. Icon flips when radio acknowledges.                                                                  |
| **AF gain**                | 70               | Slider (0-100) for slice audio output gain.                                                                                                                                                           |
| **L / R pan**              | 50 (centre)      | Slider (0-100) for stereo pan position. Double-click resets to centre. The slider fill now paints from centre outward for better visual feedback (v26.6.1).                                           |
| **SQL**                    | Off              | Toggle button to enable squelch. Auto-disabled in RTTY, DIGU, DIGL, NT, CW, and CWL modes. In RTTY and digital modes, squelch is also turned off automatically to prevent gating FSK signals (#2504). |
| **Squelch level**          | 20               | Slider (0-100) to set squelch threshold. Disabled in RTTY, DIGU, DIGL, NT, CW, and CWL modes.                                                                                                         |
| **AGC mode**               | Med              | Off, Slow, Med, Fast. Hidden in FM family modes.                                                                                                                                                      |
| **AGC threshold**          | 65               | Slider (0-100). Sets AGC threshold (or AGC off-level when AGC mode is Off). Right-click to calibrate against the noise floor (see below).                                                             |
| **RX antenna**             | ANT1             | Combo box listing available receive antennas. Populated from the radio's `ant_list` or the slice's `rxAntennaList()` when available. Blue-coloured label.                                             |
| **TX antenna**             | ANT1             | Combo box listing TX-capable antennas. RX-only antenna ports (prefix 'RX') are filtered out. Red-coloured label.                                                                                      |
| **TX (badge)**             | —                | Toggle button. Click to set this slice as the TX slice.                                                                                                                                               |
| **RIT**                    | —                | Toggle button. Toggles Receive Incremental Tuning on/off.                                                                                                                                             |
| **RIT 0**                  | —                | Push button. Zeroes the RIT offset.                                                                                                                                                                   |
| **RIT offset**             | +0 Hz            | Spinbox (step 10 Hz). Adjusts RIT offset.                                                                                                                                                             |
| **XIT**                    | —                | Toggle button. Toggles Transmit Incremental Tuning on/off.                                                                                                                                            |
| **XIT 0**                  | —                | Push button. Zeroes the XIT offset.                                                                                                                                                                   |
| **XIT offset**             | +0 Hz            | Spinbox (step 10 Hz). Adjusts XIT offset.                                                                                                                                                             |
| **QSK**                    | —                | Indicator. Lights amber when CW break-in (QSK) is active. Read-only; controlled via CW applet.                                                                                                        |
| **Filter width label**     | 2.7K             | Indicator. Shows current filter bandwidth (e.g., '2.7K', '3.3K', '500', '6.0K').                                                                                                                      |

## AGC-T Noise Calibration

The AGC threshold slider now supports a noise floor calibration feature. This helps you set an optimal AGC threshold based on the current noise floor.

**To calibrate:**
1. Right-click on the **AGC threshold** slider.
2. Select **Calibrate AGC-T against noise floor…** from the context menu.
3. The calibration process samples the noise floor and adjusts the AGC threshold slider to an appropriate level.

The right-click context menu is available regardless of the AGC mode setting. The tooltip on the slider now includes a reminder: "Right-click to calibrate against the noise floor".

## Tips

- FM, NFM, and DFM modes do not show filter width preset buttons. The filter is fixed for those modes.
- After switching to FM or NFM, the CTCSS tone and repeater offset controls (**Tone mode**, **Offset**, **−**, **Simplex**, **+**, **REV**) become visible. See [Work an FM repeater with CTCSS tone and +/- offset](work-an-fm-repeater-with-ctcss-tone-and-offset.md) for details.
- After switching to CW, the **QSK** indicator in the header becomes relevant. Its state is controlled from the CW applet, not from RX Controls.
- AGC mode controls are hidden when an FM family mode is active.
- Filter presets are now stored in a `lo:hi` format (e.g. `300:3000`) as well as the older plain-width format. Both formats are read correctly. If you have saved custom presets from an earlier version, they continue to work without any action on your part.
- The `stepFilterWidth()` method walks the per-mode preset list so widen/narrow shortcuts produce mode-correct edge geometry. This ensures that when you widen or narrow the filter using keyboard shortcuts, the filter stays within the appropriate preset boundaries for the current mode.
- When switching to RTTY or digital modes (DIGU, DIGL), the squelch is automatically disabled and turned off. This prevents the squelch from notching out FSK characters and breaking decoding (#2504).
- The manual squelch level is persisted across sessions. The last user-chosen value is stored in the `LastManualSquelchLevel` setting and restored on launch. This preserves the operator's manual preference across mode cycles, as auto mode may otherwise clobber the slice's `squelchLevel` with algorithm-suggested values (#2606).
- The slice badge now supports rich text formatting (HTML) for the slice letter (#2606).

## Mute button behaviour (v26.5.3)

The mute button (🔊 / 🔇) operates as a push button, not a toggle button. The behaviour follows the **Radio-Authoritative Settings Policy (#2489)** — mute state is NOT saved or restored on reconnect; the radio is the source of truth for audio mute.

**Single-click:** Mutes or unmutes the current slice. The action is deferred by the platform double-click interval (typically ~400 ms) so a double-click can override it. The icon updates only when the radio acknowledges the change via `SliceModel::audioMuteChanged`.

**Double-click:** Mutes or unmutes all owned slices. The double-click handler is implemented in the `eventFilter` method and cancels the single-click timer, preventing the single-click action from firing.

When a double-click sequence occurs, the second press does not emit a `clicked()` signal — the eventFilter returns true on `MouseButtonDblClick`, so `QAbstractButton::mouseDoubleClickEvent` is never called. This ensures clean single-click vs double-click discrimination.

## L/R Pan slider fill (v26.6.1)

The L/R pan slider now uses a **centre-anchored fill** instead of the default Qt left-to-right fill. This means the coloured portion of the slider groove extends from the centre mark outward toward the handle position, giving a clear visual indication of the pan bias. This is a visual change only; the control behaviour is unchanged.

The centre mark dot (small blue-grey circle at the midpoint) remains to show the neutral position at a glance. Double-click resets the slider to centre.

## Slice tab behaviour (v0.9.5.1)

When the radio reports a change in the number of available slices, the A..H tab row is now rebuilt correctly instead of being skipped. The