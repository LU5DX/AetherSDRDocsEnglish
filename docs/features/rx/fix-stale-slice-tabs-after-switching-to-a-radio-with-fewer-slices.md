# RX Controls Applet (v26.5.1)

The RX Controls applet provides per-slice receive controls including mode selection, frequency tuning, RX/TX antenna selection, filter width, AGC, AF gain/pan, squelch, RIT/XIT, and FM repeater duplex settings.

## Before you start

- Ensure the RX applet is visible in the Applet Panel. If it is not, click the **RX** tray button on the right sidebar.
- The controls displayed depend on the currently selected slice and its mode.

## What each control does

| Control | Behavior | Default | Notes |
|---------|----------|---------|-------|
| Slice tabs (A..H) | Selects which slice the RX applet is bound to; emits sliceActivationRequested. | Row hidden if maxSlices <= 1 | clearSliceButtons() tears down all generated tab buttons and restores the static slice badge on disconnect (v0.9.5.1, #2254). Slice button click connections are guarded against duplicate signal handlers across reconnects. |
| Slice badge | Displays the letter of the currently bound slice. Shown at all times; the only slice indicator visible when the tab row is hidden. | A | Coloured by slice identity. |
| 🔓 / 🔒 | Toggles tune-lock on the slice; locked slice ignores frequency changes. | 🔓 (unlocked) | Icon flips between open and closed padlock. |
| ANT1 (RX antenna) | Opens a menu listing available antennas; selecting sets slice->setRxAntenna. Populated from the radio's ant_list. | ANT1 | Blue-coloured label. |
| ANT1 (TX antenna) | Opens a menu listing TX-capable antennas; sets slice->setTxAntenna. RX-only antenna ports (prefix 'RX') are filtered out. | ANT1 | Red-coloured label. |
| 2.7K (filter width) | Shows current filter width in kHz. Updates when filter preset is applied. | 2.7K | The width readout uses mode-aware logic so SSB/digital modes display the correct labelled width (#2197). |
| QSK | Lights amber when CW break-in (QSK) is active. Read-only; controlled via the CW applet Breakin button. | off (grey) | Read-only. |
| TX (badge) | Click to set this slice as the TX slice (calls slice->setTxSlice). | None | |
| Mode combo | Sets slice mode; reshapes filter and step presets for the new mode. Options: USB, LSB, CW, AM, SAM, FM, NFM, DFM, DIGU, DIGL, RTTY (+ RADE if HAVE_RADE). | USB | RADE option requires HAVE_RADE build flag. |
| Frequency label | Displays current VFO frequency with dotted grouping. Click to switch into edit mode. | 0.000.000 | |
| Frequency edit | Enter MHz and press Enter to tune and recenter; supports kHz/Hz auto-scaling. Escape cancels the entry, restores the previous frequency, and dismisses the editor (v0.9.0, #1954). | None | XVTR-aware: accepts up to 450 MHz when slice is on an XVTR antenna. |
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
| 🔊 / 🔇 (mute) | Mutes the slice audio output. | 🔊 (unmuted) | |
| AF gain | Adjusts slice audio output gain; emits afGainChanged. | 70 | Range 0-100. |
| L / R pan | Pans slice audio between left (0) and right (100) channels. Double-click resets to 50 (centre). | 50 | Range 0-100. |
| SQL | Enables the squelch at the current slider level. Disabled (and auto-turned off) in RTTY, digital modes (DIGU, DIGL), and CW modes where squelch would notch out FSK characters (#2504). | | |
| Squelch level | Adjusts squelch threshold; takes effect only when SQL is on. Disabled in RTTY, digital, and CW modes. | 20 | Range 0-100. |
| AGC mode | Sets the slice AGC mode. Options: Off, Slow, Med, Fast. Hidden in FM family modes. | Med | |
| AGC threshold | Sets AGC threshold (or AGC off-level when AGC mode is Off). Tooltip reflects which value is being adjusted. | 65 | Range 0-100. |
| RIT | Toggles Receive Incremental Tuning on/off. | None | |
| RIT 0 | Zeroes the RIT offset. | None | |
| RIT offset | `<` / `>` or mousewheel adjusts RIT offset by 10 Hz steps. | +0 Hz | |
| XIT | Toggles Transmit Incremental Tuning on/off. | None | |
| XIT 0 | Zeroes the XIT offset. | None | |
| XIT offset | `<` / `>` or mousewheel adjusts XIT offset by 10 Hz steps. | +0 Hz | |

## Mode-dependent behaviour

### Squelch in digital, RTTY, and CW modes

Squelch is disabled and auto-turned off in the following modes to prevent notching out FSK characters and interfering with external decoders:
- **DIGU** (Digital Upper)
- **DIGL** (Digital Lower)
- **RTTY** (Radio Teletype)
- **NT** (Narrowband Telegraphy)
- **CW** (Morse code)
- **CWL** (Morse code, lower sideband)

When switching to any of these modes, the squelch is automatically turned off if it was on. The saved squelch state is preserved and will be restored when switching back to a mode where squelch is meaningful.

### QSK visibility

The QSK indicator is only visible when the slice mode is set to **CW** or **CWL**.

### RADE mode handling

When **RADE** mode is selected and the build includes `HAVE_RADE`, the slice mode is set first before emitting the `radeActivated` signal. When switching away from RADE to another mode, the deactivation signal is only emitted if the slice was actually in RADE mode, preventing spurious deactivations across slice rebinds, external activations, and multi-pan scenarios.

## Tips

- The **Widen** and **Narrow** keyboard shortcuts (or equivalent MIDI/GPIO actions) step the active slice's filter passband through the per-mode preset list via `stepFilterWidth()`. This ensures all modes produce mode-correct edge geometry.
- The filter width readout uses mode-aware logic so SSB/digital modes display the correct labelled width (#2197).
- RX-only antenna ports (with prefix 'RX') are filtered out of the TX antenna selection menu.

## Troubleshooting

- **Filter width readout appears incorrect after mode change** — Try cycling through filter presets to refresh the displayed value.
- **Squelch seems non-functional** — Check that you are not in a digital, RTTY, or CW mode where squelch is disabled.
- **RADE mode not appearing** — The RADE option requires a build with the `HAVE_RADE` flag.
- **Stale slice tabs remain after reconnecting** — Disconnect using `Settings > Connect to Radio...`, wait for the slice badge to reappear, then reconnect.

## Related

- [Switch between multiple slices using the A..H tab row](switch-between-multiple-slices-using-the-a-h-tab-row.md)
- [RX Controls overview](overview.md)
- [Understanding slices and VFOs](../../getting-started/concepts/understanding-slices.md)