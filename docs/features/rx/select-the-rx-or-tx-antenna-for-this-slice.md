# RX Controls applet

The RX Controls applet provides per-slice receive controls: mode, frequency tuning, RX/TX antenna selection, filter width, AGC, AF gain/pan, squelch, RIT/XIT, FM repeater duplex settings, and the WFM software demodulator. Single-click the mute button mutes this slice; double-click mutes/unmutes all owned slices.

## Before you start

- AetherSDR must be connected to the radio. The antenna controls are unavailable without a live connection.
- The antenna list is populated from the radio's own port configuration. Confirm your antennas are connected and recognized by the radio before changing these settings.

## Steps

1. Open the RX Controls applet. If it is not visible, click the **RX** tray button on the right sidebar.
2. If you have more than one slice, click the slice tab (A through H) for the slice you want to change.
3. **To change the RX antenna:** Click the blue antenna label near the top of the applet (shows the current RX antenna, e.g. **ANT1**). A menu appears listing all available antenna ports and any KiwiSDR virtual antenna profiles. Click the port or profile you want. A checkmark shows the current selection.
4. **To change the TX antenna:** Click the red antenna label next to the RX antenna label (also shows the current TX antenna, e.g. **ANT1**). A menu appears listing TX-capable antenna ports. Click the port you want.
5. **To enable WFM:** Click the **WFM** button. This activates a software FM demodulator via DAX IQ → Hi-Fi Cable. The button glows green when active. Switching the mode combo (USB, LSB, etc.) automatically turns WFM off.
6. **To calibrate AGC-T:** Right-click the AGC threshold slider and select **Calibrate AGC-T against noise floor…** from the context menu. This opens the AGC-T calibration panel for the current slice.

## What each control does

| Control                           | Default   | Valid values                                                                |
|-----------------------------------|-----------|-----------------------------------------------------------------------------|
| **ANT1** (RX antenna, blue label) | ANT1      | Antenna ports from the radio's ant_list, slice's own rxAntennaList, or KiwiSDR virtual antenna tokens |
| **ANT1** (TX antenna, red label)  | ANT1      | TX-capable ports from the radio's ant_list                                  |
| **Slice tabs (A..H)**             | None      | 1–8 buttons (capped by hardware max slices)                                 |
| **Slice badge**                   | A         | A/B/C/D/E/F/G/H (rendered as HTML-rich text)                                |
| **🔓 / 🔒**                         | 🔓         | Unlocked / locked                                                           |
| **WFM**                           | Off       | Toggle button; green when active                                            |
| **Mode combo**                    | USB       | USB, LSB, CW, AM, SAM, FM, NFM, DFM, DIGU, DIGL, RTTY, WFM (+ RADE if HAVE_RADE) |
| **Frequency label**               | 0.000.000 | 0.001–54.000 MHz (450.000 MHz on XVTR)                                      |
| **Frequency edit**                | None      | 0.001–54.000 MHz (450.000 MHz on XVTR); accepts kHz/Hz auto-scaling         |
| **STEP**                          | 100 Hz    | Per-mode list of step sizes                                                 |
| **Filter width presets**          | None      | Per-mode preset widths                                                      |
| **Filter passband widget**        | None      | Drag lo/hi edges to adjust passband                                         |
| **Tone mode (FM)**                | Off       | Off, CTCSS TX                                                               |
| **CTCSS tone value**              | None      | 41 standard EIA/TIA-603 tones (67.0–254.1 Hz)                               |
| **Offset (FM)**                   | 0.0 MHz   | 0.0–100.0 MHz (step 0.1)                                                    |
| **− (offset down)**               | None      | Toggle                                                                      |
| **Simplex**                       | Checked   | Toggle                                                                      |
| **+ (offset up)**                 | None      | Toggle                                                                      |
| **REV**                           | None      | Toggle                                                                      |
| **🔊 / 🔇 (mute)**                  | 🔊         | Unmuted / muted                                                             |
| **AF gain**                       | 70        | 0–100                                                                       |
| **L / R pan**                     | 50        | 0–100                                                                       |
| **SQL**                           | None      | Toggle                                                                      |
| **Squelch level**                 | 20        | 0–100 (persisted client-side as `LastManualSquelchLevel`)                   |
| **AGC mode**                      | Med       | Off, Slow, Med, Fast                                                        |
| **AGC threshold**                 | 65        | 0–100                                                                       |
| **RIT**                           | None      | Toggle                                                                      |
| **RIT 0**                         | None      | Push button                                                                 |
| **RIT offset**                    | +0 Hz     | Step 10 Hz                                                                  |
| **XIT**                           | None      | Toggle                                                                      |
| **XIT 0**                         | None      | Push button                                                                 |
| **XIT offset**                    | +0 Hz     | Step 10 Hz                                                                  |
| **TX (badge)**                    | None      | Click to set as TX slice                                                    |
| **QSK**                           | None      | Amber when CW break-in active (read-only)                                   |
| **Filter width (indicator)**      | 2.7K      | Current filter bandwidth                                                    |

## What each indicator shows

| Indicator        | States                                       | Meaning                                        |
|------------------|----------------------------------------------|------------------------------------------------|
| Filter width     | e.g. '2.7K', '3.3K', '500', '6.0K'          | Current slice filter bandwidth                 |
| QSK              | off (grey), on (amber)                       | CW full break-in state reflected from the CW applet |

## Tips

- The RX antenna label is shown in blue; the TX antenna label is shown in red. This is the only visual distinction between the two controls, as they appear side by side in the header row.
- Antenna ports whose names begin with `RX` are filtered out of the TX antenna menu. They will still appear in the RX antenna menu. The TX antenna menu also includes ports whose names begin with `ANT`, `TX`, or `XVTR`.
- Each slice has its own independent RX and TX antenna assignment. Changing the antenna on slice A does not affect slice B.
- From v0.9.3, the slice tab buttons and the slice badge use per-slice colors managed by SliceColorManager. These colors persist across sessions and are also reflected in VFO widgets and meter strips. The colors are not configurable from the antenna controls page; they apply applet-wide.
- The filter width indicator shares mode-aware formatting logic with the VFO panel (`RxApplet::formatFilterWidth`), ensuring consistent readouts across both locations (#2197).
- The `stepFilterWidth()` method walks the per-mode filter preset list so widen/narrow keyboard shortcuts produce mode-correct edge geometry (#2208). For example, widening from a 2.7 kHz USB filter selects the next larger preset (e.g. 2.9 kHz) with proper edge placement for USB mode rather than a symmetrical passband.
- From v26.5.2.1, the slice badge supports HTML-rich text rendering (#2606). This allows the slice letter to be styled with HTML formatting if needed.
- The squelch manual level is persisted client-side as the setting `LastManualSquelchLevel`. This preserves your manual squelch preference across mode cycles, radio reconnects, and application restarts. The radio's own automatic squelch algorithm may modify the slice's squelch level, but AetherSDR restores the last user-chosen manual level when Auto mode is not active.
- From v26.6.1, the filter-preset buttons (1.8K, 2.1K, etc.) use theme-aware styling via `kButtonBase()`, which resolves tokens through the ThemeManager. These buttons now re-theme alongside the rest of the UI when the application theme changes. The theme tokens used are `{{color.background.1}}`, `{{color.background.2}}`, and `{{color.text.primary}}`.
- From v26.6.3, the frequency edit field uses `FreqLineEdit` (a subclass of `QLineEdit`) for improved input handling. It shows "MHz" as hint text rather than placeholder text.
- From v26.6.3, the **STEP** spinbox emits `stepSizeChangedByUser` in addition to `stepSizeChanged` when the user manually changes the step size. This allows other components to distinguish programmatic step changes from user-initiated ones.
- From v26.6.3, the AGC threshold slider has a right-click context menu with a **Calibrate AGC-T against noise floor…** option. The tooltip now includes the "Right-click to calibrate against the noise floor" hint for discoverability.
- From v26.7.4, the CW filter preset list has been expanded from 4 to 6 presets: 50, 100, 250, 400, 500, and 600 Hz.

## Antenna menu changes in v26.5.2.1

The RX and TX antenna menus have been updated to provide clearer feedback:

- Each menu item shows the antenna port name as both tooltip and status tip.
- The menu action data carries the raw antenna identifier, rather than using the display text. This means menu items can display formatted labels (e.g. with port type indicators) while still selecting the correct antenna port.
- The RX antenna menu now prefers the slice's own `rxAntennaList()` if it is non-empty, falling back to the radio's `ant_list`. This ensures the menu reflects any per-slice antenna restrictions reported by the radio.

## KiwiSDR virtual antenna integration (v26.7.4)

When a KiwiSDR manager is active, the RX antenna menu includes virtual antenna profile tokens from the KiwiSDR manager. These profiles appear as additional entries in the RX antenna menu.

- Virtual antenna profiles are identified by a profile ID rather than a physical port name.
- When you select a KiwiSDR virtual antenna from the menu, AetherSDR emits `kiwiRxAntennaSelected(sliceId, profileId)` and does not call `slice->setRxAntenna()`.
- When you select a physical Flex antenna port, AetherSDR emits `flexRxAntennaSelected(sliceId)` and calls `slice->setRxAntenna()` with the selected port.
- Each KiwiSDR profile is assigned to at most one slice at a time. The menu shows a checkmark next to the profile assigned to the current slice.
- The menu is rebuilt each time it opens, ensuring the available profiles are current.

## WFM software demodulator (v26.6.3)

The **WFM** button provides a software FM demodulator that uses DAX IQ audio routed through your system's Hi-Fi Cable virtual audio device.

- **To enable WFM:** Click the **WFM** button. It glows green when active. The button sits to the right of the mode combo in the frequency row.
- **To disable WFM:** Click the **WFM** button again, or select any real radio mode from the mode combo (USB, LSB, CW, etc.). Switching modes automatically deactivates WFM for that slice.
- **Per-slice behavior:** Each slice has its own WFM state. Enabling WFM on one slice does not affect other slices.
- **State management:** AetherSDR emits `wfmActivated(true, sliceId)` when WFM is turned on, and `wfmActivated(false, sliceId)` when WFM is turned off (either by clicking the button or by changing the mode combo). The `setWfmActive()` method allows other components to synchronize the WFM button state programmatically.
- **Mode combo interaction:** When you select a real radio mode from the mode combo while WFM is active on that slice, AetherSDR automatically emits `wfmActivated(false, sliceId)` to tear down the WFM overlay. Selecting "WFM" from the mode combo is not supported; WFM is controlled exclusively by the dedicated button.

## RADE mode changes

The RADE mode activation logic has been updated to reflect the fact that "RADE" is a client-side mode only:

- When you select RADE from the mode combo, the client sets the slice mode to "RADE" and emits `radeActivated(true, sliceId)`. The radio itself immediately echoes back the real underlying mode (typically DIGL or DIGU).
- AetherSDR no longer sets the slice mode on the radio when RADE is selected. The radio's mode feedback is used instead.
- In v26.5.3, `radeActivated(false)` is emitted only when switching away from RADE on a slice that was genuinely in RADE mode (#2376). This prevents stale deactivate signals when changing modes on a non-RADE slice.
- If you need to explicitly deactivate RADE mode on a slice, switch the mode to a non-RADE mode using the mode combo.

## Slice tab behavior

In v0.9.5.1, the slice tab row gained more robust lifecycle management to fix issues seen across radio reconnects (#2254).

- When the radio reports a different number of slices than the current tab row contains, AetherSDR tears down all existing tab buttons (`clearSlice