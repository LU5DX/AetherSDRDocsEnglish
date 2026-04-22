# RX Controls overview

The RX Controls applet gives you per-slice receive settings: mode, frequency, antenna selection, filter width, AGC, audio, squelch, RIT/XIT, and FM repeater options. Open it to adjust any receive parameter for the currently selected slice.

## How it works

RX Controls lives in the Applet Panel on the right sidebar. Toggle it with the RX tray button. When your radio supports more than one slice, a row of slice tabs (A through H) appears at the top; click a tab to bind the applet to that slice. All controls below then apply to that slice only.

The applet is organized into functional groups, described below.

### Slice identification and header row

| Control | What it does | Default |
|---|---|---|
| Slice badge | Shows the letter (A–H) of the bound slice. Color-coded by slice identity. | A |
| 🔓 / 🔒 | Toggles tune-lock. When locked (🔒), the slice ignores frequency changes. | 🔓 (unlocked) |
| ANT1 (blue) | Opens the RX antenna menu. Select any antenna from the radio's antenna list. | ANT1 |
| ANT1 (red) | Opens the TX antenna menu. RX-only ports (prefixed "RX") are excluded. | ANT1 |
| 2.7K | Read-only indicator showing current filter bandwidth. Updates when a preset is applied. | Reflects active filter |
| QSK | Amber when CW full break-in is active. Read-only; controlled from the CW applet. | Off (grey) |
| TX (badge) | Click to designate this slice as the TX slice. | — |

### Mode and frequency

| Control | What it does | Default |
|---|---|---|
| Mode combo | Sets the slice mode. Reshapes filter and step presets for the new mode. | USB |
| Frequency label | Displays the current VFO frequency with dotted grouping. Click to enter edit mode. | 0.000.000 |
| Frequency edit | Type a frequency in MHz and press Enter to tune and re-center. Accepts up to 54.000 MHz (450.000 MHz when the slice is on an XVTR antenna). | — |
| STEP | Cycles through per-mode step sizes using the < / > buttons or the mouse wheel. | 100 Hz |

Available modes: USB, LSB, CW, AM, SAM, FM, NFM, DFM, DIGU, DIGL, RTTY. RADE is available in builds that include HAVE_RADE support.

### Filter width

| Control | What it does | Setting key |
|---|---|---|
| Filter width presets | Buttons for common bandwidths for the current mode. Click to apply; right-click to save the current width as a preset. Hidden in FM, NFM, and DFM modes. | `FilterPresets` |
| Filter passband widget | Drag the low or high edge to set a custom passband. | — |

Per-mode preset ranges:

- **USB / LSB:** 1800, 2100, 2400, 2700, 2900, 3300 Hz
- **AM / SAM:** 5600, 6000, 8000, 10000, 12000, 14000 Hz
- **CW:** 50, 100, 250, 400 Hz
- **DIGU / DIGL:** 100, 300, 600, 1000, 1500, 2000 Hz
- **RTTY:** 250, 300, 350, 400, 500, 1000 Hz
- **FM / NFM / DFM:** no presets

### Audio

| Control | What it does | Default | Range |
|---|---|---|---|
| 🔊 / 🔇 (mute) | Mutes the slice audio output. | 🔊 (unmuted) | — |
| AF gain | Adjusts slice audio output level. | 70 | 0–100 |
| L / R pan | Pans slice audio between left (0) and right (100) channels. Double-click to reset to centre. | 50 | 0–100 |

### Squelch

| Control | What it does | Default | Range |
|---|---|---|---|
| SQL | Enables squelch at the current slider level. | Off | — |
| Squelch level | Sets the squelch threshold. Has no effect unless SQL is on. | 20 | 0–100 |

### AGC

Hidden in FM, NFM, and DFM modes.

| Control | What it does | Default | Range |
|---|---|---|---|
| AGC mode | Sets the AGC mode. | Med | Off, Slow, Med, Fast |
| AGC threshold | Sets the AGC threshold. When AGC mode is Off, this sets the AGC off-level instead. | 65 | 0–100 |

### RIT and XIT

| Control | What it does | Default |
|---|---|---|
| RIT | Toggles Receive Incremental Tuning on/off. | Off |
| RIT 0 | Zeroes the RIT offset immediately. | — |
| RIT offset | < / > or mouse wheel adjusts RIT offset in 10 Hz steps. | +0 Hz |
| XIT | Toggles Transmit Incremental Tuning on/off. | Off |
| XIT 0 | Zeroes the XIT offset immediately. | — |
| XIT offset | < / > or mouse wheel adjusts XIT offset in 10 Hz steps. | +0 Hz |

### FM repeater settings

These controls appear only when the slice mode is FM, NFM, or DFM.

| Control | What it does | Default | Range |
|---|---|---|---|
| Tone mode | Selects CTCSS tone mode. | Off | Off, CTCSS TX |
| CTCSS tone value | Selects the CTCSS tone frequency transmitted. Active only when Tone mode is CTCSS TX. | — | 67.0–254.1 Hz (41 standard EIA/TIA-603 tones) |
| Offset | Sets the FM repeater offset in MHz. | 0.0 MHz | 0.0–100.0 MHz (step 0.1) |
| − | Sets offset direction to down (TX below RX). | — | — |
| Simplex | Sets offset direction to simplex (TX equals RX). | Checked | — |
| + | Sets offset direction to up (TX above RX). | — | — |
| REV | Inverts the TX offset sign to work a reversed repeater pair. | Off | — |

## Related

- [Understanding slices and VFOs](../../getting-started/concepts/understanding-slices.md)
- [Tune the radio to a frequency (type MHz in the readout)](tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
- [Change mode (USB, LSB, CW, AM, FM, etc.)](change-mode-usb-lsb-cw-am-fm-etc.md)
- [Pick a filter width preset for the current mode](pick-a-filter-width-preset-for-the-current-mode.md)
- [Select the RX or TX antenna for this slice](select-the-rx-or-tx-antenna-for-this-slice.md)
- [Turn on the squelch and set its threshold](turn-on-the-squelch-and-set-its-threshold.md)
- [Use RIT to offset the receive frequency for a drifting station](use-rit-to-offset-the-receive-frequency-for-a-drifting-station.md)
- [Use XIT to offset the transmit frequency without changing RX](use-xit-to-offset-the-transmit-frequency-without-changing-rx.md)
- [Work an FM repeater with CTCSS tone and +/- offset](work-an-fm-repeater-with-ctcss-tone-and-offset.md)
- [Lock the slice to prevent accidental retuning](lock-the-slice-to-prevent-accidental-retuning.md)
- [Switch between multiple slices using the A..H tab row](switch-between-multiple-slices-using-the-a-h-tab-row.md)
