# RX Controls Applet (v26.8.4)

The RX Controls applet provides per-slice receive controls including mode selection, frequency tuning, RX/TX antenna selection, filter width, AGC, AF gain/pan, squelch, RIT/XIT, and FM repeater duplex settings. Single-click the mute button mutes this slice; double-click mutes/unmutes all owned slices. The filter-width formatter is shared with the VFO panel for consistent readouts (#2197), and the stepFilterWidth() method walks per-mode preset lists so widen/narrow shortcuts produce mode-correct edge geometry. Switching to RTTY or digital modes (DIGU, DIGL) auto-disables squelch, which would otherwise notch out FSK characters and break decoding (#2504). When switching out of RADE mode via the mode combo, the applet emits radeActivated(false) only if the slice was actually in RADE (#2376), preventing stale deactivate signals when changing modes on a non-RADE slice.

## Before you start

- Ensure the RX applet is visible in the Applet Panel. If it is not, click the **RX** tray button on the right sidebar.
- The controls displayed depend on the currently selected slice and its mode.

## What each control does

| Control | Behavior | Default | Notes |
|---------|----------|---------|-------|
| Slice tabs (A..H) | Selects which slice the RX applet is bound to; emits sliceActivationRequested. | Row hidden if maxSlices <= 1 | clearSliceButtons() tears down all generated tab buttons and restores the static slice badge on disconnect (v0.9.5.1, #2254). Slice button click connections are guarded against duplicate signal handlers across reconnects. |
| Slice badge | Displays the letter of the currently bound slice. | A | Coloured by slice identity. |
| 🔓 / 🔒 | Toggles tune-lock on the slice; locked slice ignores frequency changes. | 🔓 (unlocked) | Icon flips between open and closed padlock. |
| ANT1 (RX antenna) | Opens a menu listing available antennas and KiwiSDR virtual antennas; selecting sets the slice's RX antenna or activates a KiwiSDR profile. The menu is populated from the radio's ant_list, the slice's rxAntennaList, and any KiwiSDR virtual antenna tokens. KiwiSDR profile entries are highlighted in the menu when active. | ANT1 | Blue-coloured label. Menu items show both the antenna token and a human-readable label (e.g. "ANT1 - 1"). KiwiSDR virtual antennas are added to the menu if a KiwiSDR manager is available. When a KiwiSDR profile is selected, the applet emits `kiwiRxAntennaSelected(sliceId, profileId)`. When a Flex antenna is selected, it emits `flexRxAntennaSelected(sliceId)`. |
| ANT1 (TX antenna) | Opens a menu listing TX-capable antennas; sets slice->setTxAntenna. RX-only antenna ports (prefix 'RX') are filtered out. Menu items display with optional port number labels for clarity. | ANT1 | Red-coloured label. Menu items show both the antenna token and a human-readable label. The txAntennaOptions() method returns all ANT*, TX*, and XVTR ports, excluding RX-only ports. |
| 2.7K (filter width) | Shows current filter width in kHz. Updates when filter preset is applied. | 2.7K | The width readout uses mode-aware logic so SSB/digital modes display the correct labelled width (#2197). |
| QSK | Lights amber when CW break-in (QSK) is active. Read-only; controlled via the CW applet Breakin button. | off (grey) | Read-only. |
| TX (badge) | Click to set this slice as the TX slice (calls slice->setTxSlice). | None | |
| Mode combo | Sets slice mode; reshapes filter and step presets for the new mode. Options: USB, LSB, CW, AM, SAM, FM, NFM, DFM, DIGU, DIGL, RTTY (+ RADE if HAVE_RADE). | USB | RADE option requires HAVE_RADE build flag. DSTR and FreeDV modes are filtered out when the model doesn't support them. Selecting a real radio mode tears down a running WFM software-demod overlay (WFM itself is toggled from the VFO-flag WFM button, not this combo). |
| Frequency label | Displays current VFO frequency with dotted grouping. Click to switch into edit mode. | 0.000.000 | |
| Frequency edit | Enter MHz and press Enter to tune and recenter; supports kHz/Hz auto-scaling. Escape cancels the entry, restores the previous frequency, and dismisses the editor (v0.9.0, #1954). Uses FreqLineEdit widget with "MHz" hint text. Entering a value above 54.0 MHz that includes a decimal point (e.g. "144.0") is now treated as an explicit MHz entry and allowed for VHF/UHF operation without requiring an XVTR antenna. | None | XVTR-aware: accepts up to 50000 MHz when slice is on an XVTR antenna. Entering a value above 54.0 MHz without a decimal point (e.g. "144000") is divided by 1e3 for kHz-to-MHz conversion. |
| STEP | `<` / `>` or mousewheel cycles through per-mode step sizes; emits stepSizeChanged and stepSizeChangedByUser. Step list depends on slice mode. | 100 Hz (index 2) | The stepSizeChangedByUser signal is emitted in addition to stepSizeChanged when the user manually changes the step size. |
| Filter width presets | Click to apply a preset filter width; right-click to save current width as a preset. The width readout uses mode-aware logic so SSB/digital modes display the correct labelled width. Keywords Widen/Narrow (if assigned to keyboard shortcuts) step through the per-mode preset list for mode-correct edge geometry. | Per-mode list | Buttons hidden for FM/NFM/DFM modes; presets are per-mode. CW presets now include 500 and 600 Hz options for finer shaping (#2208). The stepFilterWidth(direction) method walks the per-mode preset list for mode-correct widen/narrow (#2208). Filter preset buttons now use theme-aware tokenised stylesheets via ThemeManager, so they re-theme alongside the rest of the UI. |
| Filter passband widget | Drag the lo/hi edges to adjust filter passband; emits filterChanged (lo, hi). | None | |
| Tone mode (FM) | Selects CTCSS tone mode on FM/NFM/DFM. Visible only in FM family modes. | Off | Options: Off, CTCSS TX. |
| CTCSS tone value | Selects CTCSS tone frequency sent with transmit. Enabled only when Tone mode = CTCSS TX. | None | 41 standard EIA/TIA-603 tones (67.0 Hz to 254.1 Hz). |
| Offset (FM) | Sets FM repeater offset frequency in MHz. | 0.0 MHz | Range 0.0-100.0 MHz (step 0.1). |
| − (offset down) | Sets repeater offset direction to 'down' (TX below RX). | None | |
| Simplex | Sets repeater offset direction to simplex (TX = RX). | checked | |
| + (offset up) | Sets repeater offset direction to 'up' (TX above RX). | None | |
| REV / XFC | For FM repeater operation, REV inverts the TX offset sign to work a reversed repeater pair. On backends that support a transmit-frequency check, the button relabels to XFC: pressing it holds the transmit frequency check for the duration of the press, and while held it briefly forces the radio toward the transmit frequency to confirm coverage. | None | The button toggles REV (checkable) normally, or becomes a momentary XFC down-button when the connected radio backend advertises hasTransmitFrequencyCheck. The held XFC is released on hide, deactivate, capability change, or disconnect. |
| 🔊 / 🔇 (mute) | Single-click mutes/unmutes this slice (deferred by the platform click-discrimination interval, configurable in Radio Setup → Slice Controls). Double-click mutes/unmutes all owned slices via muteAllToggled signal. Icon flips when the radio acknowledges via SliceModel::audioMuteChanged. | 🔊 (unmuted) | Per the Radio-Authoritative Settings Policy (#2489), mute state is NOT saved/restored on reconnect — the radio is the source of truth for audio mute. The single-click is deferred by clickDiscriminationIntervalMs() (configurable in Radio Setup → Slice Controls, default platform double-click interval ~400 ms, #3009) so a double-click can override it. The double-click handler is in eventFilter and cancels the single-click timer. |
| AF gain | Adjusts slice audio output gain; emits afGainChanged. Displays current value as a percentage (e.g. "70%"). | 70 (70%) | Range 0-100. |
| L / R pan | Pans slice audio between left (0) and right (100) channels. Displays current pan position: "C" for centre, "L{n}" for left pan, "R{n}" for right pan. Double-click resets to 50 (C). The slider uses a CenterMarkSlider subclass that draws the fill from the centre outward, so only the (centre → handle) region is accented. A small centre-mark dot is painted on the groove as a visual landmark for the neutral position. | 50 (C) | Range 0-100. The CentreMarkSlider overpaints the left-half of the default sub-page fill with groove colour, then adds accent-colour fill from the centre to the handle. The handle pixel disc is clipped from the overpaint to prevent visual bleed. |
| SQL / AUTO | Three-way cycle button: each click steps Off → SQL (manual threshold) → AUTO (algorithm tracks the noise floor) → Off. In AUTO mode the button shows amber 'AUTO'; in manual mode green 'SQL'. Disabled (and auto-turned off) in RTTY and digital modes (DIGU, DIGL) where squelch would notch out FSK characters (#2504). | Off | Manual and Auto both turn the radio squelch on. The auto-squelch algorithm lives in the panadapter; the level is the dB margin above the measured noise floor. Mirrored by an identical button in the VFO panel's Audio tab. |
| Squelch level | In Manual mode adjusts the squelch threshold (takes effect only when squelch is on). In AUTO mode sets the dB margin above the measured noise floor where the gate opens, persisted to AutoSqlMarginDb. | 20 | In Manual mode the level is radio-authoritative per-slice (not persisted); in Auto mode the margin is persisted. Disabled in RTTY and digital modes and in Off mode. Right-click the AGC threshold slider for AGC-T noise calibration. |
| AGC mode | Sets the slice AGC mode. Options: Off, Slow, Med, Fast. Hidden in FM family modes. | Med | |
| AGC threshold | Sets AGC threshold (or AGC off-level when AGC mode is Off). Tooltip reflects which value is being adjusted and includes a note about right-click calibration. Right-click to open a context menu with a "Calibrate AGC-T against noise floor…" option, which emits calibrateAgcTRequested(sliceId). | 65 | Range 0-100. Tooltip examples: "AGC Threshold: 65\nRight-click to calibrate against the noise floor" or "AGC Off Level: 65\nRight-click to calibrate against the noise floor". |
| RIT | Toggles Receive Incremental Tuning on/off. | None | |
| RIT 0 | Zeroes the RIT offset. | None | |
| RIT offset | `<` / `>` or mousewheel adjusts RIT offset by 10 Hz steps. | +0 Hz | |
| XIT | Toggles Transmit Incremental Tuning on/off. | None | |
| XIT 0 | Zeroes the XIT offset. | None | |
| XIT offset | `<` / `>` or mousewheel adjusts XIT offset by 10 Hz steps. | +0 Hz | |

## Mode-dependent behaviour

### Squelch in digital and RTTY modes

Squelch is disabled and auto-turned off in the following modes to prevent notching out FSK characters and interfering with external decoders:
- **DIGU** (Digital Upper)
- **DIGL** (Digital Lower)
- **RTTY** (Radio Teletype)

When switching to any of these modes, the squelch is automatically turned off if it was on. The saved squelch state is preserved and will be restored when switching back to a mode where squelch is meaningful.

### Manual squelch is radio-authoritative

Since v26.8.4, the manual squelch threshold is radio-authoritative per slice. The previous client-side persistence of the manual squelch level (the `LastManualSquelchLevel` setting) has been removed (#4592); the applet no longer seeds its manual squelch level from application settings. The radio is the source of truth for the per-slice manual squelch level across mode cycles and application launches. The manual squelch level fallback defaults to 20 when no slice is attached.

### QSK visibility

The QSK indicator is only visible when the slice mode is set to **CW** or **CWL**.

### RADE mode handling

RADE mode is client