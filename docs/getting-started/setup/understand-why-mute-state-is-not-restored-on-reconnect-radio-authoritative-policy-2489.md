# RX Controls (RxApplet)

Per-slice receive controls: mode, frequency tuning, RX/TX antenna selection, filter width, AGC, AF gain/pan, squelch, RIT/XIT, and FM repeater duplex settings. Single-click the mute button mutes this slice; double-click mutes/unmutes all owned slices. The filter-width formatter is shared with the VFO panel for consistent readouts (#2197), and the stepFilterWidth() method walks per-mode preset lists so widen/narrow shortcuts produce mode-correct edge geometry. Switching to RTTY or digital modes (DIGU, DIGL) auto-disables squelch, which would otherwise notch out FSK characters and break decoding (#2504). When switching out of RADE mode via the mode combo, the applet emits radeActivated(false) only if the slice was actually in RADE (#2376), preventing stale deactivate signals when changing modes on a non-RADE slice.

## Slice tabs

| Control | Label | Default | Valid range | Behavior | Notes |
|---------|-------|---------|-------------|----------|-------|
| Slice tabs | A..H | none | 1-8 buttons (capped by hardware max slices) | Selects which slice the RX applet is bound to; emits sliceActivationRequested. | Row hidden if maxSlices <= 1. clearSliceButtons() tears down all generated tab buttons and restores the static slice badge on disconnect (v0.9.5.1, #2254). Slice button click connections are guarded against duplicate signal handlers across reconnects. |
| Slice badge | A | A/B/C/D/E/F/G/H | none | Displays the letter of the currently bound slice. | Coloured by slice identity. |

## Frequency tuning

| Control | Label | Default | Valid range | Behavior | Notes |
|---------|-------|---------|-------------|----------|-------|
| Tune lock | 🔓 / 🔒 | 🔓 (unlocked) | none | Toggles tune-lock on the slice; locked slice ignores frequency changes. | Icon flips between open and closed padlock. |
| Frequency label | 0.000.000 | none | Displays current VFO frequency with dotted grouping. | Click to switch into edit mode. |
| Frequency edit | none | 0.001-54.000 MHz (up to 50000 MHz on XVTR) | Enter MHz and press Enter to tune and recenter; supports kHz/Hz auto-scaling. Escape cancels the entry, restores the previous frequency, and dismisses the editor (v0.9.0, #1954). | XVTR-aware: accepts up to 50,000 MHz when the slice is on an XVTR antenna. 3-digit band convenience: on 2m/70cm (100-999 MHz) a digit insertion formats 1446 as 144.6. |
| STEP | 100 Hz (index 2) | per-mode list (e.g. SSB: 1, 10, 50, 100, 500, 1000, 2000, 3000 Hz) | < / > or mousewheel cycles through per-mode step sizes; emits stepSizeChanged. | Step list depends on slice mode. |

## Antenna selection

| Control | Label | Default | Valid range | Behavior | Notes |
|---------|-------|---------|-------------|----------|-------|
| RX antenna | ANT1 | from ant_list, plus assigned KiwiSDR virtual-antenna tokens | Opens a menu listing available antennas; selecting sets slice->setRxAntenna, or routes to an assigned KiwiSDR receiver profile when a virtual antenna token is chosen. | Populated from the radio's antenna list plus any KiwiSDR virtual-antenna tokens from the Kiwi manager; blue-coloured label. Falls back to ANT1/ANT2 when the list is empty. |
| TX antenna | ANT1 | from ant_list, excluding RX-only ports | Opens a menu listing TX-capable antennas; sets slice->setTxAntenna. | Red-coloured label; RX-only antenna ports (prefix 'RX') are filtered out. |

## Mode and filter

| Control | Label | Default | Valid range | Behavior | Notes |
|---------|-------|---------|-------------|----------|-------|
| Mode combo | USB | USB, LSB, CW, AM, SAM, FM, NFM, DFM, DSTR, DIGU, DIGL, RTTY (+ RADE if HAVE_RADE; WFM via VFO-flag button) | Sets slice mode; reshapes filter and step presets for the new mode. | RADE option requires HAVE_RADE build flag. DSTR and FreeDV modes are filtered out when the model doesn't support them. Selecting a real radio mode tears down a running WFM software-demod overlay (WFM itself is toggled from the VFO-flag WFM button, not this combo). |
| Filter width | 2.7K | none | Shows current filter width in kHz. | Updates when filter preset is applied. |
| Filter width presets | none | USB/LSB: 1800/2100/2400/2700/2900/3300 Hz; AM/SAM: 5600-14000 Hz; CW: 50/100/250/400 Hz; DIG: 100-2000 Hz; RTTY: 250-1000 Hz | Click to apply a preset filter width; right-click to save current width as a preset. | Buttons hidden for FM/NFM/DFM modes; presets are per-mode. The width readout (shared with VfoWidget via RxApplet::formatFilterWidth) uses mode-aware logic so SSB/digital modes display the correct labelled width (#2197). The stepFilterWidth(direction) method walks the per-mode preset list for mode-correct widen/narrow (#2208). |
| Filter passband widget | none | none | Drag the lo/hi edges to adjust filter passband; emits filterChanged (lo, hi). | none |

## CW break-in indicator

| Control | Label | Default | Behavior | Notes |
|---------|-------|---------|----------|-------|
| QSK indicator | QSK | none | Lights amber when CW break-in (QSK) is active. | Read-only; controlled via the CW applet Breakin button. |

## TX slice selection

| Control | Label | Behavior | Notes |
|---------|-------|----------|-------|
| TX badge | TX | Click to set this slice as the TX slice (calls slice->setTxSlice). | none |

## Audio controls

| Control | Label | Default | Valid range | Behavior | Notes |
|---------|-------|---------|-------------|----------|-------|
| Mute toggle | 🔊 / 🔇 | 🔊 (unmuted) | none | Single-click mutes/unmutes this slice (deferred by the platform click-discrimination interval, configurable in Radio Setup → Slice Controls). Double-click mutes/unmutes all owned slices via muteAllToggled signal. Icon flips when the radio acknowledges via SliceModel::audioMuteChanged. | Per the Radio-Authoritative Settings Policy (#2489), mute state is NOT saved/restored on reconnect — the radio is the source of truth for audio mute. The single-click is deferred by clickDiscriminationIntervalMs() (configurable in Radio Setup → Slice Controls, default platform double-click interval ~400 ms, #3009) so a double-click can override it. The double-click handler is in eventFilter and cancels the single-click timer. |
| AF gain | 70 | 0-100 | Adjusts slice audio output gain; emits afGainChanged. | none |
| L / R pan | 50 | 0-100 | Pans slice audio between left (0) and right (100) channels. | Double-click resets to 50 (centre). |

## Squelch

| Control | Label | Default | Valid range | Behavior | Notes |
|---------|-------|---------|-------------|----------|-------|
| SQL / AUTO | Off | Off, SQL (Manual), AUTO | Three-way cycle button: each click steps Off → SQL (manual threshold) → AUTO (algorithm tracks the noise floor) → Off. In AUTO mode the button shows amber 'AUTO'; in manual mode green 'SQL'. Disabled (and auto-turned off) in RTTY and digital modes (DIGU, DIGL) where squelch would notch out FSK characters (#2504). | Manual and Auto both turn the radio squelch on. The auto-squelch algorithm lives in the panadapter; the level is the dB margin above the measured noise floor. Mirrored by an identical button in the VFO panel's Audio tab. |
| Squelch level | 20 | Manual: 0-100 (or 0-99 on Kiwi replacement receive); Auto: 5-20 dB margin | In Manual mode adjusts the squelch threshold (takes effect only when squelch is on). In AUTO mode sets the dB margin above the measured noise floor where the gate opens, persisted to AutoSqlMarginDb. | In Manual mode the level is radio-authoritative per-slice (not persisted); in Auto mode the margin is persisted. Disabled in RTTY and digital modes and in Off mode. Right-click the AGC threshold slider for AGC-T noise calibration. |

## AGC controls

| Control | Label | Default | Valid range | Behavior | Notes |
|---------|-------|---------|-------------|----------|-------|
| AGC mode | Med | Off, Slow, Med, Fast | Sets the slice AGC mode. | Hidden in FM family modes. |
| AGC threshold | 65 | 0-100 | Sets AGC threshold (or AGC off-level when AGC mode is Off). | Tooltip reflects which value is being adjusted. Right-click opens a 'Calibrate AGC-T against noise floor…' command that starts the AGC-T noise calibration dialog (disabled while a Kiwi replacement receive is active). |

## RIT/XIT

| Control | Label | Default | Valid range | Behavior | Notes |
|---------|-------|---------|-------------|----------|-------|
| RIT toggle | RIT | none | none | Toggles Receive Incremental Tuning on/off. | none |
| RIT zero | RIT 0 | none | none | Zeroes the RIT offset. | none |
| RIT offset | +0 Hz | step 10 Hz | < / > or mousewheel adjusts RIT offset by 10 Hz steps. | none |
| XIT toggle | XIT | none | none | Toggles Transmit Incremental Tuning on/off. | none |
| XIT zero | XIT 0 | none | none | Zeroes the XIT offset. | none |
| XIT offset | +0 Hz | step 10 Hz | < / > or mousewheel adjusts XIT offset by 10 Hz steps. | none |

## FM repeater settings

| Control | Label | Default | Valid range | Behavior | Notes |
|---------|-------|---------|-------------|----------|-------|
| Tone mode | Off | Off, CTCSS TX | Selects CTCSS tone mode on FM/NFM/DFM. | Visible only in FM family modes. |
| CTCSS tone | none | 41 standard EIA/TIA-603 tones (67.0 Hz to 254.1 Hz) | Selects CTCSS tone frequency sent with transmit. | Enabled only when Tone mode = CTCSS TX. |
| Offset | 0.0 MHz | 0.0-100.0 MHz (step 0.1) | Sets FM repeater offset frequency in MHz. | none |
| Offset down | − | none | none | Sets repeater offset direction to 'down' (TX below RX). | none |
| Simplex | Simplex | checked | none | Sets repeater offset direction to simplex (TX = RX). | none |
| Offset up | + | none | none | Sets repeater offset direction to 'up' (TX above RX). | none |
| REV / XFC | REV | none | REV (toggle) or XFC (momentary) | For FM repeater operation, REV inverts the TX offset sign to work a reversed repeater pair. On backends that support a transmit-frequency check, the button relabels to XFC: pressing it holds the transmit frequency check for the duration of the press, and while held it briefly forces the radio toward the transmit frequency to confirm coverage. | The button toggles REV (checkable) normally, or becomes a momentary XFC down-button when the connected radio backend advertises hasTransmitFrequencyCheck. The held XFC is released on hide, deactivate, capability change, or disconnect. |

---

# Mute state is not restored on reconnect (radio-authoritative policy #2489)

When you mute a slice using the mute button in the RX Controls applet, the mute state is not saved or restored after a radio disconnection and reconnection. This is by design: AetherSDR treats the radio as the authoritative source for audio mute state.

## Steps

1. Click the mute button (🔊 / 🔇) in the RX Controls applet to mute or unmute the slice.
2. Disconnect and reconnect to the radio — the mute button returns to its default unmuted (🔊) state.

## What each control does

| Control     | Label                                                                                                                                                                                                                                                                                                                                                    | Default                                                                                                                                                                                                                                    |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Mute toggle | 🔊 / 🔇                                                                                                                                                                                                                                                                                                                                                    | 🔊 (unmuted)                                                                                                                                                                                                                                |
| REV / XFC   | For FM repeater operation, REV inverts the TX offset sign to work a reversed repeater pair. On backends that support a transmit-frequency check, the button relabels to XFC: pressing it holds the transmit frequency check for the duration of the press, and while held it briefly forces the radio toward the