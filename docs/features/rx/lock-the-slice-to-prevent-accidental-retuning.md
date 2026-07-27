# RX Controls (RxApplet)

The RX Controls applet provides per-slice receive controls for mode, frequency tuning, RX/TX antenna selection, filter width, AGC, AF gain/pan, squelch, RIT/XIT, and FM repeater duplex settings.

## Lock the slice to prevent accidental retuning

The tune-lock feature prevents a slice from responding to frequency changes. Use it when you want to monitor a fixed frequency without the risk of nudging the VFO by clicking the panadapter or scrolling the mouse wheel.

### Before you start

- AetherSDR must be connected to the radio. The RX Controls applet requires an active radio connection.
- The RX Controls applet must be visible. If it is not, click the RX tray button on the right sidebar to show it.

### Steps

1. In the RX Controls applet, identify the header row containing the slice badge, lock button, and antenna selectors.
2. If you have more than one slice, click the appropriate slice tab (A through H) to select the slice you want to lock.
3. Click the 🔓 button in the header row. The icon changes to 🔒 and turns blue, confirming the slice is locked.
4. To unlock, click 🔒 again. The icon returns to 🔓 and the slice resumes responding to frequency changes.

### What each control does

| Control | Default | Behavior |
|---------|---------|----------|
| 🔓 / 🔒 | 🔓 (unlocked) | Toggles tune-lock on the active slice. When locked (🔒), the slice ignores all frequency changes. Click again to unlock. |

### Tips

- The lock state applies per slice. You can lock slice A while slice B remains freely tunable.
- The lock button is always visible in the header row regardless of the current mode.
- From v0.9.3, the slice tab buttons and the slice badge both use per-slice colors managed by SliceColorManager. Colors are customizable per slice and persist across sessions. The same color is reflected in the slice tab buttons, the slice badge, VFO widgets, and meter strips.

## Slice tab behavior on reconnect (v0.9.5.1)

When the radio disconnects or the number of available slices changes, AetherSDR now tears down all generated slice tab buttons and restores the static slice badge automatically (`clearSliceButtons()`, #2254). On reconnect, the tab row is rebuilt to match the new slice count. If the count has not changed, the existing buttons are reused without a rebuild.

Signal connections between the slice button group and the `sliceActivationRequested` handler are guarded so that reconnecting to the radio does not accumulate duplicate signal handlers.

## Filter preset storage format (v0.9.5.1)

Filter presets saved for a given mode (setting key `FilterPresets`) now support two storage formats:

- **Width only** — a plain integer representing the filter bandwidth in Hz (for example, `2700`). This is the legacy format and continues to work.
- **Lo:Hi** — a colon-separated pair of low-edge and high-edge offsets in Hz (for example, `-1400:1300`). This format preserves an asymmetric passband exactly as you set it by dragging the filter passband widget edges.

When you right-click a filter preset button to save the current width, AetherSDR writes the `lo:hi` form when the passband is asymmetric (#2259). Presets saved in the old width-only format are read and applied as centred passbands, exactly as before.

Up to six presets are stored and displayed per mode in the RX Controls applet. Buttons are hidden for FM, NFM, and DFM modes.

## Step filter width (v0.9.8)

The filter width preset system now supports a `stepFilterWidth()` method that walks the per-mode preset list. This enables widen/narrow shortcuts that produce mode-correct edge geometry for all modes (LSB, CWL, DIGL, RTTY, AM, CW, USB).

When you apply a widen or narrow operation:

- AetherSDR finds the closest matching preset width to the current filter passband.
- It then selects the next wider or narrower preset from the per-mode list.
- The preset is applied through `applyFilterPreset()`, which uses the correct edge offsets for the current mode.

This ensures that widening or narrowing a filter always stays within the mode-appropriate preset values and produces the correct passband geometry.

## Filter width formatting (v0.9.8)

The `formatFilterWidth()` method is now a public static function, shared with the VFO panel (`VfoWidget`). This ensures both the RX Controls applet and the VFO panel display identical filter width readouts. The method uses mode-aware logic so SSB and digital modes display the correct labelled width (#2197).

## NT and RTTY mode squelch behavior (v26.5.1)

Squelch is disabled in NT mode, RTTY mode, and the existing digital modes (`DIGU`, `DIGL`). This prevents squelch from gating weak FSK signals and notching out characters, which would break decoding (#2504). If squelch was active when you switched into RTTY or a digital mode, AetherSDR turns it off automatically and saves the state so it can be restored when you leave the mode. The squelch button and slider remain disabled while the mode is active.

## RADE mode activation (v26.5.2.1)

RADE ("Reverse Adaptive Digital Enhancement" or a specific digital mode) is a client-side only mode label. When you select RADE from the mode combo box, AetherSDR sets the mode immediately on the slice but the radio echoes back the real underlying mode (DIGL or DIGU) on the next status update. Because of this, the slice's internal `mode()` property will never be `"RADE"` after the radio responds.

When switching away from RADE mode to any other mode:

- AetherSDR checks if the slice's mode was `"RADE"` before issuing the `radeActivated(false)` deactivation signal.
- Because the radio overrides RADE with DIGL/DIGU, `mode() == "RADE"` is never true at the time of the switch. This means the deactivation signal is not emitted when switching away from RADE.

To activate RADE mode from code (for example, via VFO combo, profile load on startup, or `MainWindow::activateRADE`), AetherSDR calls the internal RADE activation path directly rather than relying on the mode combo's value change. Use the `Activate RADE` button in the mode menu or the profile system to enable RADE.

## Manual squelch threshold persistence (v26.5.2.1)

The squelch level slider now persists the last user-chosen manual value across sessions. This is necessary because auto squelch mode can overwrite the `squelchLevel` on the slice with algorithm-suggested values, and the radio does not preserve the operator's manual preference across mode cycles or application launches.

AetherSDR stores the manual threshold in the application settings under the key `LastManualSquelchLevel`. The value is clamped to the valid range of 0–100. On first launch, the default is 20.

When you enable squelch and adjust the slider, the new value is saved immediately. When you launch a new session, the slider returns to the last saved manual level rather than the default.

## NT mode

Version 0.9.3 adds the `NT` mode alongside the existing digital modes (`DIGU`, `DIGL`). It behaves identically to other digital modes in the following ways:

- **Filter presets** — NT shares the DIG filter preset set (100–2000 Hz). The filter width label updates accordingly.
- **Filter width calculation** — The filter width display measures the high-edge offset, the same as USB and DIGU.
- **Squelch** — The SQL button and squelch slider are disabled in NT mode. Because audio is routed via DAX in digital modes, squelch is not meaningful. If squelch was active when you switched into NT mode, AetherSDR turns it off automatically and restores it when you leave NT mode.

## Antenna selection improvements (v26.5.2.1)

The RX and TX antenna combo boxes now use the per-slice antenna lists when available, rather than relying solely on the global antenna list from the radio. This provides more accurate antenna options, especially for slices on different panadapters.

### RX antenna menu

- When the slice provides an `rxAntennaList()`, the menu shows only those antenna ports.
- If the slice does not provide a list, the global `ant_list` from the panadapter status is used as a fallback.
- Each menu action stores its antenna port name in the action's data property, ensuring correct selection even when display labels differ from port names.
- Tooltips and status tips show the raw antenna port name for clarity.

### TX antenna menu

- The TX antenna menu is populated by a helper function `txAntennaOptions()`.
- This function collects TX-capable antennas from both the global antenna list and any additional sources.
- RX-only antenna ports (those starting with `RX` case-insensitively) are excluded from the menu.
- Antenna ports with prefixes `ANT`, `TX`, or the exact string `XVTR` are considered TX-capable fallback tokens.

### Display formatting

Both antenna menus now use a helper `antennaMenuLabel()` to format display labels. The label includes the antenna port name followed by frequency range information in parentheses where available, making it easier to identify which antenna to select for a given band.

## Slice badge formatting (v26.5.2.1)

The slice badge label now supports rich text (HTML) rendering. This allows the slice letter to include formatting, such as superscript or subscript characters, when the slice identity requires it (#2606). The badge continues to use the same per-slice color scheme and fixed 20x20 pixel size as before.

## Frequency entry improvements (v26.5.3)

The frequency entry system now uses `FrequencyEntryParser::normalizedMhzText()` for parsing and `FrequencyEntryParser::isExplicitMhzEntry()` for detecting explicit MHz entries. This provides more robust handling of frequency formatting and entry detection.

### Explicit MHz entries

When you enter a frequency value greater than 54.0 MHz in the frequency edit field, AetherSDR checks whether it is an explicit MHz entry. If the entry is detected as explicitly in MHz (for example, `146.520` or `446.000`), the radio allows tuning up to 50,000 MHz, enabling direct access to VHF/UHF/SHF bands without requiring an XVTR antenna. This is particularly useful for entering 2m, 70cm, or higher band frequencies directly.

### Entry frequency normalization

The `normalizedMhzText()` function cleans up the entered frequency text by removing extraneous dots and formatting characters. This ensures that entries like `14.250.000` (with digit grouping dots) are correctly parsed as `14.250000` MHz.

### 3-digit band convenience

For XVTR slices (or when the frequency is above 54 MHz), the system applies 3-digit band convenience logic: an entry like `1446` is interpreted as 144.6 MHz (for the 2m band), while entries for 23cm/microwave bands (e.g., `1296`) are treated as direct MHz values. This logic only applies when the entry is not an explicit MHz entry.

### Escape to cancel (v0.9.0)

Pressing Escape while the frequency editor is active cancels the edit, restores the previous frequency, and dismisses the editor (Fixed in v0.9.0, #1954).

## Mute button behavior (v26.5.3)

The mute button (🔊 / 🔇) now uses timer-based single-click discrimination. This provides more reliable double-click detection for muting/unmuting all owned slices.

### Single click

A single click starts a timer set to the platform's double-click interval (~400 ms). When the timer expires, the mute state of the current slice toggles.

### Double click

A double-click immediately cancels the single-click timer and emits `muteAllToggled`, which mutes or unmutes all slices owned by the current client. The second press of the double-click sequence does not produce a separate `clicked()` signal because the event filter intercepts the `MouseButtonDblClick` event and returns true, preventing `QAbstractButton::mouseDoubleClickEvent` from running.

### Icon update

The mute button icon (🔊 or 🔇) is updated only when the radio acknowledges the mute state change via `SliceModel::audioMuteChanged`. This ensures the icon always reflects the radio-authoritative state, as required by the Radio-Authoritative Settings Policy (#2489).

### State persistence

Mute state is NOT saved or restored on reconnect. The radio is always the source of truth for audio mute state.

## L/R pan slider centre-mark (v26.6.1)

The L/R pan slider now paints a small centre-mark dot on the groove. This provides a visual landmark for the neutral (centre) position, making it easier to identify when pan is centred.

### How the fill works

The slider fill is anchored from the centre outward:

- When the handle is left of centre, the sub-page section between the handle and centre is painted in the accent colour.
- When the handle is right of centre, the sub-page section between centre and the handle is painted in the accent colour, and the section from 0 to centre is erased with the groove colour.

This prevents misleading visual feedback where the default Qt stylesheet would paint the entire section from the left edge to the handle, which reads incorrectly for a centre-anchored control.

### Visual indicator

A small dot (2.5 pixel radius, colour `#608090`) is painted at the centre