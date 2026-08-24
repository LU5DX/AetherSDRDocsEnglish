# RX Controls overview

The RX Controls applet gives you per-slice control over every receive parameter: mode, frequency, antenna selection, filter width, AGC, audio, squelch, RIT/XIT, and FM repeater settings. Open it whenever you need to configure how a slice receives or transmits.

## How it works

The RX applet is always present in the Applet Panel (right sidebar). Toggle its visibility with the RX tray button. When the radio supports more than one slice, a row of slice tabs (A through H) appears at the top; clicking a tab binds the applet to that slice. All controls below the tab row affect the currently selected slice only.

Filter width presets are the one setting that persists across sessions, stored under the `FilterPresets` key. Every other control reflects live radio state and is not independently saved by AetherSDR.

## What each control does

### Slice selection and identity

| Control | Default | Behavior |
|---|---|---|
| Slice tabs (A..H) | — | Select which slice the applet controls. The tab row is hidden when the radio has only one slice. On disconnect, `clearSliceButtons()` tears down all generated tab buttons and restores the static slice badge. Slice button click connections are guarded against duplicate signal handlers across reconnects (v0.9.5.1, #2254). |
| Slice badge | A | Displays the letter of the active slice. Color is driven by slice identity. Read-only. |
| 🔓 / 🔒 | 🔓 (unlocked) | Toggles tune-lock. A locked slice ignores frequency changes from the panadapter and other sources. |
| TX (badge) | — | Click to designate this slice as the TX slice. |

### Frequency and mode

| Control | Default | Valid range | Behavior |
|---|---|---|---|
| Mode combo | USB | USB, LSB, CW, AM, SAM, FM, NFM, DFM, DSTR, DIGU, DIGL, RTTY (+ RADE if HAVE_RADE build flag is set; WFM via VFO-flag button) | Sets slice mode. Changing mode reshapes filter and step presets automatically. When switching to RTTY or digital modes (DIGU, DIGL) squelch is auto-disabled to prevent notching out FSK characters (#2504). When switching out of RADE mode via the mode combo, the applet emits `radeActivated(false)` only if the slice was actually in RADE (#2376), preventing stale deactivate signals when changing modes on a non-RADE slice. Selecting a real radio mode also tears down any active WFM software-demod overlay on this slice. DSTR and FreeDV modes are filtered out when the model doesn't support them. |
| WFM button | — | — | Toggles the software FM demodulator (WFM) on or off for this slice. Uses DAX IQ via Hi-Fi Cable. Active when checked (green background). Selecting any real radio mode from the mode combo automatically deactivates WFM for this slice. |
| Frequency label | 0.000.000 | — | Displays the current VFO frequency with dotted grouping. Click to enter edit mode. |
| Frequency edit | — | 0.001–54.000 MHz (up to 50000.000 MHz on XVTR, or when entry exceeds 54 MHz and is explicit MHz) | Type a frequency in MHz and press Enter to tune and re-center. Supports kHz/Hz auto-scaling: entries above 54000 are treated as Hz, above 54 as kHz (unless the entry is explicit MHz). On XVTR antennas, 3-digit 2m/70cm band shortcuts are supported (e.g. 1446 → 144.6 MHz). Press Escape to cancel and restore the previous frequency. Frequency entry uses `FrequencyEntryParser::normalizedMhzText()` and `isExplicitMhzEntry()` for consistent parsing across the app. |
| STEP | 100 Hz | Per-mode list (e.g. SSB: 1, 10, 50, 100, 500, 1000, 2000, 3000 Hz) | Click the left/right triangle buttons or use the mouse wheel to cycle through step sizes. The available steps change with mode. Both the `stepSizeChanged` and `stepSizeChangedByUser` signals are emitted when the user changes the step. |

### Antenna selection

| Control | Default | Behavior |
|---|---|---|
| ANT1 (RX antenna) | ANT1 | Opens a menu of available antennas. The menu is populated from the radio's antenna list plus any KiwiSDR virtual-antenna tokens from the Kiwi manager. Selecting a Flex antenna sets the slice RX antenna; selecting a KiwiSDR virtual antenna routes to the assigned KiwiSDR receiver profile. Falls back to ANT1/ANT2 when the list is empty. Label is blue. |
| ANT1 (TX antenna) | ANT1 | Opens a menu of TX-capable antennas. RX-only antenna ports (names starting with "RX") are filtered out. Selecting an item sets the TX antenna. Label is red. |

### Filter

| Control | Default / range | Setting key | Behavior |
|---|---|---|---|
| Filter width presets | USB/LSB: 1800/2100/2400/2700/2900/3300 Hz; CW: 50/100/250/400 Hz; AM/SAM: 5600–14000 Hz; DIG: 100–2000 Hz; RTTY: 250–1000 Hz | `FilterPresets` | Click a button to apply that width. Right-click to save the current filter width as a preset. Buttons are hidden in FM, NFM, and DFM modes. Presets are stored as either a plain width value or a `lo:hi` passband pair; both formats are read and written correctly (v0.9.5.1, #2259). |
| Filter width label | 2.7K | — | Shows the current filter bandwidth. Updates when a preset is applied or the passband is dragged. Read-only. The formatting logic is shared with VfoWidget via `RxApplet::formatFilterWidth()` and uses mode-aware logic so SSB/digital modes display the correct labelled width (#2197). |
| Filter passband widget | — | — | Drag the low or high edge to set a custom filter passband. |
| Widen (shortcut action) | — | — | The `stepFilterWidth(+1)` method walks the per-mode preset list to widen the filter passband with mode-correct edge geometry. Accessible via keyboard shortcut (v0.9.8, #2208). |
| Narrow (shortcut action) | — | — | The `stepFilterWidth(-1)` method walks the per-mode preset list to narrow the filter passband with mode-correct edge geometry. Accessible via keyboard shortcut (v0.9.8, #2208). |

### AGC

| Control | Default | Valid range | Behavior |
|---|---|---|---|
| AGC mode | Med | Off, Slow, Med, Fast | Sets the AGC response speed. Hidden in FM family modes. |
| AGC threshold | 65 | 0–100 | Sets the AGC threshold. When AGC mode is Off, adjusts the AGC off-level instead. Right-click on the slider to open a context menu with a "Calibrate AGC-T against noise floor…" option (disabled while a Kiwi replacement receive is active). |

### Audio

| Control | Default | Valid range | Behavior |
|---|---|---|---|
| 🔊 / 🔇 (mute) | 🔊 (unmuted) | — | Single-click mutes/unmutes this slice. Double-click mutes/unmutes all owned slices. The icon updates only when the radio acknowledges (per Radio-Authoritative Settings Policy, #2489). The single-click action is deferred by the platform double-click interval (default ~400 ms) so a double-click can override it. Mute state is NOT saved/restored on reconnect — the radio is the source of truth for audio mute. |
| AF gain | 70 | 0–100 | Adjusts the slice audio output level. Displays a "X%" tooltip with the current percentage value. |
| L / R pan | 50 | 0–100 | Pans audio between left (0) and right (100) channels. Displays "L##", "C" (centre), or "R##" tooltip. Double-click to reset to centre (50). The slider fill anchors from the centre outward, with a centre-mark dot painted on the groove for visual reference. |
| SQL / AUTO | Off | Off, SQL (Manual), AUTO | Three-way cycle button: each click steps Off → SQL (manual threshold) → AUTO (algorithm tracks the noise floor) → Off. In AUTO mode the button shows amber 'AUTO'; in manual mode green 'SQL'. Disabled (and auto-turned off) in RTTY and digital modes (DIGU, DIGL) where squelch would notch out FSK characters (#2504). Mirrored by an identical button in the VFO panel's Audio tab. |
| Squelch level | 20 | Manual: 0–100 (or 0–99 on Kiwi replacement receive); Auto: 5–20 dB margin | In Manual mode adjusts the squelch threshold (takes effect only when squelch is on). In AUTO mode sets the dB margin above the measured noise floor where the gate opens, persisted to `AutoSqlMarginDb`. In Manual mode the level is radio-authoritative per-slice (not persisted); in Auto mode the margin is persisted. Disabled in RTTY and digital modes and in Off mode. Right-click the AGC threshold slider for AGC-T noise calibration. |

### RIT and XIT

| Control | Default | Behavior |
|---|---|---|
| RIT | off | Toggles Receive Incremental Tuning on or off. |
| RIT 0 | — | Zeroes the RIT offset immediately. |
| RIT offset | +0 Hz | Adjust with the left/right buttons or mouse wheel in 10 Hz steps. |
| XIT | off | Toggles Transmit Incremental Tuning on or off. |
| XIT 0 | — | Zeroes the XIT offset immediately. |
| XIT offset | +0 Hz | Adjust with the left/right buttons or mouse wheel in 10 Hz steps. |

### Noise reduction and DSP filter buttons

The following DSP filter buttons are visible in non-FM modes. Button availability depends on the radio series.

| Button | Availability | Behavior |
|---|---|---|
| NR | All series | Enables noise reduction. Hidden in FM family modes. |
| NR2 | All series | Enables noise reduction mode 2. Hidden in FM family modes. |
| NB | All series | Enables noise blanker. Hidden in FM family modes. |
| NRL | All series (including 6000-series) | Enables noise reduction (NRL algorithm). Hidden in FM family modes. Available on 6000-series radios as of V0.9.4; previously required 8000-series firmware. |
| NRS | 8000-series only | Enables NRS noise reduction. Hidden in FM family modes. |
| RNN | 8000-series only | Enables RNN noise reduction. Hidden in CW and FM family modes. |
| NRF | 8000-series only | Enables NRF noise reduction. Hidden in FM family modes. |

### Indicators

| Indicator | States | Meaning |
|---|---|---|
| QSK | Grey / amber | Lights amber when CW full break-in is active. Controlled from the CW applet; read-only here. |
| Filter width label | e.g. '2.7K', '3.3K', '500', '6.0K' | Current slice filter bandwidth. |

### FM repeater controls

These controls are visible only when the slice mode is FM, NFM, or DFM.

| Control | Default | Valid range | Behavior |
|---|---|---|---|
| Tone mode (FM) | Off | Off, CTCSS TX | Selects whether a CTCSS tone is sent on transmit. |
| CTCSS tone value | — | 67.0–254.1 Hz (41 standard EIA/TIA-603 tones) | Selects the CTCSS tone frequency. Active only when Tone mode is CTCSS TX. |
| Offset (FM) | 0.0 MHz | 0.0–100.0 MHz (step 0.1) | Sets the FM repeater offset frequency. |
| − (offset down) | — | — | Sets the TX frequency below the RX frequency by the offset amount. |
| Simplex | checked | — | Sets TX and RX to the same frequency (no offset). |
| + (offset up) | — | — | Sets the TX frequency above the RX frequency by the offset amount. |
| REV / XFC | — | REV (toggle) or XFC (momentary) | For FM repeater operation, REV inverts the TX offset sign to work a reversed repeater pair. On backends that support a transmit-frequency check, the button relabels to XFC: pressing it holds the transmit frequency check for the duration of the press, and while held it briefly forces the radio toward the transmit frequency to confirm coverage. The held XFC is released on hide, deactivate, capability change, or disconnect. |

## Peripherals tab — manual IP connect

The Peripherals tab in the Radio Setup dialog lets you manually connect to external devices by IP address. The following rows are available.

### Antenna Genius (AG) — row 3

Connects to an Antenna Genius device at the specified IP and port. The "Connected" status is shown only when the connected device is an Antenna Genius proper. If the connection is actually to a ShackSwitch, the AG row shows as disconnected and the ShackSwitch row shows as connected instead.

### ShackSwitch — row 4 (added in V0