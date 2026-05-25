# RX Controls Applet (v26.5.3)

The RX Controls applet provides per-slice receive controls including mode selection, frequency tuning, RX/TX antenna selection, filter width, AGC, AF gain/pan, squelch, RIT/XIT, and FM repeater duplex settings. Single-click the mute button mutes this slice; double-click mutes/unmutes all owned slices. The filter-width formatter is shared with the VFO panel for consistent readouts (#2197), and the stepFilterWidth() method walks per-mode preset lists so widen/narrow shortcuts produce mode-correct edge geometry. Switching to RTTY or digital modes (DIGU, DIGL) auto-disables squelch, which would otherwise notch out FSK characters and break decoding (#2504). When switching out of RADE mode via the mode combo, the applet emits radeActivated(false) only if the slice was actually in RADE (#2376), preventing stale deactivate signals when changing modes on a non-RADE slice.

## Before you start

- Ensure the RX applet is visible in the Applet Panel. If it is not, click the **RX** tray button on the right sidebar.
- The controls displayed depend on the currently selected slice and its mode.

## What each control does

| Control | Behavior | Default | Notes |
|---------|----------|---------|-------|
| Slice tabs (A..H) | Selects which slice the RX applet is bound to; emits sliceActivationRequested. | Row hidden if maxSlices <= 1 | clearSliceButtons() tears down all generated tab buttons and restores the static slice badge on disconnect (v0.9.5.1, #2254). Slice button click connections are guarded against duplicate signal handlers across reconnects. |
| Slice badge | Displays the letter of the currently bound slice. Shown at all times; the only slice indicator visible when the tab row is hidden. Supports rich text formatting for the slice letter (#2606). | A | Coloured by slice identity. |
| 🔓 / 🔒 | Toggles tune-lock on the slice; locked slice ignores frequency changes. | 🔓 (unlocked) | Icon flips between open and closed padlock. |
| ANT1 (RX antenna) | Opens a menu listing available antennas; selecting sets slice->setRxAntenna. Populated from the radio's ant_list or the slice's rxAntennaList. Menu items display with optional port number labels for clarity. | ANT1 | Blue-coloured label. Menu items show both the antenna token and a human-readable label (e.g. "ANT1 - 1"). |
| ANT1 (TX antenna) | Opens a menu listing TX-capable antennas; sets slice->setTxAntenna. RX-only antenna ports (prefix 'RX') are filtered out. Menu items display with optional port number labels for clarity. | ANT1 | Red-coloured label. Menu items show both the antenna token and a human-readable label. The txAntennaOptions() method returns all ANT*, TX*, and XVTR ports, excluding RX-only ports. |
| 2.7K (filter width) | Shows current filter width in kHz. Updates when filter preset is applied. | 2.7K | The width readout uses mode-aware logic so SSB/digital modes display the correct labelled width (#2197). |
| QSK | Lights amber when CW break-in (QSK) is active. Read-only; controlled via the CW applet Breakin button. | off (grey) | Read-only. |
| TX (badge) | Click to set this slice as the TX slice (calls slice->setTxSlice). | None | |
| Mode combo | Sets slice mode; reshapes filter and step presets for the new mode. Options: USB, LSB, CW, AM, SAM, FM, NFM, DFM, DIGU, DIGL, RTTY (+ RADE if HAVE_RADE). | USB | RADE option requires HAVE_RADE build flag. |
| Frequency label | Displays current VFO frequency with dotted grouping. Click to switch into edit mode. | 0.000.000 | |
| Frequency edit | Enter MHz and press Enter to tune and recenter; supports kHz/Hz auto-scaling. Escape cancels the entry, restores the previous frequency, and dismisses the editor (v0.9.0, #1954). Entering a value above 54.0 MHz that includes a decimal point (e.g. "144.0") is now treated as an explicit MHz entry and allowed for VHF/UHF operation without requiring an XVTR antenna. | None | XVTR-aware: accepts up to 50000 MHz when slice is on an XVTR antenna. Entering a value above 54.0 MHz without a decimal point (e.g. "144000") is divided by 1e3 for kHz-to-MHz conversion. |
| STEP | `<` / `>` or mousewheel cycles through per-mode step sizes; emits stepSizeChanged. Step list depends on slice mode. | 100 Hz (index 2) | |
| Filter width presets | Click to apply a preset filter width; right-click to save current width as a preset. The width readout uses mode-aware logic so SSB/digital modes display the correct labelled width. Keywords Widen/Narrow (if assigned to keyboard shortcuts) step through the per-mode preset list for mode-correct edge geometry. | Per-mode list | Buttons hidden for FM/NFM/DFM modes; presets are per-mode. The stepFilterWidth(direction) method walks the per-mode preset list for mode-correct widen/narrow (#2208). |
| Filter passband widget | Drag the lo/hi edges to adjust filter passband; emits filterChanged (lo, hi). | None | |
| Tone mode (FM) | Selects CTCSS tone mode on FM/NFM/DFM. Visible only in FM family modes. | Off | |
| CTCSS tone value | Selects CTCSS tone frequency sent with transmit. Enabled only when Tone mode = CTCSS TX. | None | 41 standard EIA/TIA-603 tones (67.0 Hz to 254.1 Hz). |
| Offset (FM) | Sets FM repeater offset frequency in MHz. | 0.0 MHz | Range 0.0-100.0 MHz (step 0.1). |
| − (offset down) | Sets repeater offset direction to 'down' (TX below RX). | None | |
| Simplex | Sets repeater offset direction to simplex (TX = RX). | checked | |
| + (offset up) | Sets repeater offset direction to 'up' (TX above RX). | None | |
| REV | Inverts the TX offset sign to work a reversed repeater pair. | None | |
| 🔊 / 🔇 (mute) | Single-click mutes/unmutes this slice (deferred by the platform double-click interval). Double-click mutes/unmutes all owned slices via muteAllToggled signal. Icon flips when the radio acknowledges via SliceModel::audioMuteChanged. | 🔊 (unmuted) | Per the Radio-Authoritative Settings Policy (#2489), mute state is NOT saved/restored on reconnect — the radio is the source of truth for audio mute. The single-click is deferred by clickDiscriminationIntervalMs() (default platform double-click interval, ~400 ms) so a double-click can override it. The button is no longer checkable; the icon update is driven by the radio acknowledgment, not the click event. |
| AF gain | Adjusts slice audio output gain; emits afGainChanged. Displays current value as a percentage (e.g. "70%"). | 70 (70%) | Range 0-100. |
| L / R pan | Pans slice audio between left (0) and right (100) channels. Displays current pan position: "C" for centre, "L{n}" for left pan, "R{n}" for right pan. Double-click resets to 50 (C). | 50 (C) | Range 0-100. |
| SQL | Enables the squelch at the current slider level. Disabled (and auto-turned off) in RTTY and digital modes (DIGU, DIGL) where squelch would notch out FSK characters (#2504). | None | |
| Squelch level | Adjusts squelch threshold; takes effect only when SQL is on. Disabled in RTTY and digital modes. The manual squelch level is persisted client-side as the setting `LastManualSquelchLevel` (default 20). | 20 | Range 0-100. The last user-chosen manual squelch threshold is saved across sessions and restored on launch, because auto mode clobbers the slice's squelchLevel with algorithm-suggested values. |
| AGC mode | Sets the slice AGC mode. Options: Off, Slow, Med, Fast. Hidden in FM family modes. | Med | |
| AGC threshold | Sets AGC threshold (or AGC off-level when AGC mode is Off). Tooltip reflects which value is being adjusted. | 65 | Range 0-100. |
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

When switching to any of these modes, the squelch is automatically turned off if it was on. The saved squelch state is preserved and will be restored when switching back to a mode where squelch is meaningful. The manual squelch level is persisted client-side as the setting `LastManualSquelchLevel` and restored on application launch, because auto mode clobbers the slice's squelchLevel with algorithm-suggested values.

### QSK visibility

The QSK indicator is only visible when the slice mode is set to **CW** or **CWL**.

### RADE mode handling

RADE mode is client-side only — the radio echoes back the real mode (DIGL/DIGU) immediately. When switching out of RADE mode via the mode combo, the applet emits `radeActivated(false)` only if the slice was actually in RADE (#2376), preventing stale deactivate signals when changing modes on a non-RADE slice. When entering RADE mode, the applet emits `radeActivated(true, sliceId)` and does not call the radio's `setMode()` since RADE is client-side only.

## Slider readout labels

The AF gain and Pan sliders now display their current values as text labels next to the slider controls (v26.5.3):

- **AF gain** — Displays the current value as a percentage (e.g. "70%" for a value of 70).
- **L / R pan** — Displays the current pan position:
  - "C" when the slider is at centre (value 50).
  - "L{n}" when panned left, where {n} is the difference from centre (e.g. "L20" for value 30).
  - "R{n}" when panned right, where {n} is the difference from centre (e.g. "R30" for value 80).

## Frequency entry enhancements

The frequency edit field includes several enhancements for VHF/UHF operation (v26.5.3):

- Entering a value above 54.0 MHz that includes a decimal point (e.g. "144.0" or "432.100") is now treated as an explicit MHz entry and allowed without requiring an XVTR antenna. This enables direct tuning to VHF/UHF frequencies.
- Entering a value above 54.0 MHz without a decimal point (e.g. "144000") is divided by 1e3 for kHz-to-MHz conversion.
- The maximum allowed frequency when not on an XVTR antenna is 50000 MHz when an explicit MHz entry above 54.0 is detected.
- XVTR operation still allows entering up to 50000 MHz and includes the 3-digit-band convenience feature (e.g. "1446" → 144.6 MHz) for 2m/70cm bands.

## Antenna selection

### RX antenna menu

The RX antenna menu displays all available antennas from either the panadapter's `ant_list` or the slice's `rxAntennaList()` (if available). Menu items show both the antenna token and a human-readable label (e.g. "ANT1 - 1") for clarity. The selected antenna is set via `slice->setRxAntenna()` using the underlying token value, not the display label.

### TX antenna menu

The TX antenna menu filters out RX-only ports (those starting with "RX"). The `txAntennaOptions()` method returns only antenna tokens that start with "ANT", "TX", or equal "XVTR". Menu items show both the antenna token and a human-readable label (e.g. "ANT1 - 1") for clarity. The selected antenna is set via `slice->setTxAntenna()` using the underlying token value, not the display label.

## Mute button behaviour

The mute button (🔊 / 🔇) has updated behaviour (v26.5.3):

- **Single-click**