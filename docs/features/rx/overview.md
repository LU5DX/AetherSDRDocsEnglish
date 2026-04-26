# RX Controls overview

The RX Controls applet gives you per-slice control over every receive parameter: mode, frequency, filter, AGC, audio, squelch, RIT/XIT, and FM repeater settings. All of these controls act on whichever slice is currently selected in the applet.

## How it works

The RX Controls applet is always visible in the right-side Applet Panel. Toggle it with the `RX` tray button on the right sidebar. When more than one slice is active, a row of slice tabs (A through H) appears at the top of the applet; clicking a tab binds the applet to that slice. All controls below then read from and write to that slice only.

The applet is organized into functional groups, top to bottom:

**Header row** — slice identity, locking, antenna selection, and status indicators.

**Frequency and mode row** — VFO readout, mode selector, and tune-step control.

**Filter row** — preset buttons, a draggable passband widget, and the current filter width indicator.

**Audio row** — mute, AF gain, and stereo pan.

**Squelch row** — squelch enable and threshold.

**AGC row** — AGC mode and threshold. Hidden in FM family modes.

**RIT/XIT row** — incremental tuning offsets for RX and TX independently.

**FM repeater row** — CTCSS tone, repeater offset, and direction controls. Visible only in FM, NFM, and DFM modes.

## What each control does

### Header row

| Control | Default | Valid range / options | Persisted key | Behavior |
|---|---|---|---|---|
| Slice tabs (A..H) | — | 1–8 tabs, capped by hardware | — | Selects which slice the applet is bound to. Row hidden when only one slice is available. |
| Slice badge | A | A–H | — | Displays the letter of the currently bound slice, coloured by slice identity. |
| 🔓 / 🔒 | 🔓 (unlocked) | — | — | Toggles tune-lock. A locked slice ignores frequency changes from the panadapter or frequency entry. |
| ANT1 (RX antenna) | ANT1 | From radio's antenna list | — | Opens a menu of available antennas; selecting one sets the RX antenna for this slice. Label is blue. |
| ANT1 (TX antenna) | ANT1 | From radio's antenna list, excluding RX-only ports | — | Opens a menu of TX-capable antennas; selecting one sets the TX antenna for this slice. Label is red. Ports whose names begin with `RX` are filtered out. |
| 2.7K (filter width) | 2.7K | — | — | Read-only indicator. Shows the current filter bandwidth. Updates when a preset is applied or the passband is dragged. |
| QSK | off (grey) | off (grey) / on (amber) | — | Read-only. Lights amber when CW full break-in is active. Controlled via the CW applet. |
| TX (badge) | — | — | — | Click to designate this slice as the TX slice. |

### Frequency and mode row

| Control | Default | Valid range / options | Persisted key | Behavior |
|---|---|---|---|---|
| Mode combo | USB | USB, LSB, CW, AM, SAM, FM, NFM, DFM, DIGU, DIGL, RTTY | — | Sets the slice mode. Reshapes filter preset buttons and step-size list for the new mode. |
| Frequency label | 0.000.000 | — | — | Displays the current VFO frequency with dotted grouping. Click to enter edit mode. |
| Frequency edit | — | 0.001–54.000 MHz (up to 450.000 MHz on a transverter antenna) | — | Type a frequency in MHz and press Enter to tune and re-centre the panadapter. Press Escape to cancel and restore the previous frequency. |
| STEP | 100 Hz | Per-mode list (e.g. SSB: 1, 10, 50, 100, 500, 1000, 2000, 3000 Hz) | — | Click `<` / `>` or use the mouse wheel to cycle through step sizes. The available steps change with mode. |

### Filter row

| Control | Default | Valid range / options | Persisted key | Behavior |
|---|---|---|---|---|
| Filter width presets | — | USB/LSB: 1800–3300 Hz; AM/SAM: 5600–14000 Hz; CW: 50–400 Hz; DIGU/DIGL: 100–2000 Hz; RTTY: 250–1000 Hz | `FilterPresets` | Click a button to apply that filter width. Right-click a button to save the current filter width as that preset. Buttons are hidden in FM, NFM, and DFM modes. Presets are stored per mode. |
| Filter passband widget | — | — | — | Drag the low or high edge to adjust the filter passband boundaries directly. |

### Audio row

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| 🔊 / 🔇 (mute) | 🔊 (unmuted) | — | — | Mutes or unmutes the slice audio output. |
| AF gain | 70 | 0–100 | — | Adjusts the slice audio output level. |
| L / R pan | 50 | 0 (full left) – 100 (full right) | — | Pans the slice audio between left and right channels. Double-click resets to 50 (centre). |

### Squelch row

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| SQL | off | — | — | Enables the squelch at the current slider level. |
| Squelch level | 20 | 0–100 | — | Sets the squelch threshold. Has no effect while SQL is off. |

### AGC row

| Control | Default | Valid range / options | Persisted key | Behavior |
|---|---|---|---|---|
| AGC mode | Med | Off, Slow, Med, Fast | — | Sets the slice AGC mode. Hidden in FM family modes. |
| AGC threshold | 65 | 0–100 | — | Sets the AGC threshold. When AGC mode is Off, this controls the manual RF gain level instead. The tooltip reflects which value is being set. |

### RIT / XIT row

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| RIT | off | — | — | Toggles Receive Incremental Tuning on or off. |
| RIT 0 | — | — | — | Zeroes the RIT offset immediately. |
| RIT offset | +0 Hz | Step: 10 Hz | — | Click `<` / `>` or use the mouse wheel to adjust the RIT offset in 10 Hz steps. |
| XIT | off | — | — | Toggles Transmit Incremental Tuning on or off. |
| XIT 0 | — | — | — | Zeroes the XIT offset immediately. |
| XIT offset | +0 Hz | Step: 10 Hz | — | Click `<` / `>` or use the mouse wheel to adjust the XIT offset in 10 Hz steps. |

### FM repeater row (FM, NFM, DFM modes only)

| Control | Default | Valid range / options | Persisted key | Behavior |
|---|---|---|---|---|
| Tone mode (FM) | Off | Off, CTCSS TX | — | Selects whether a CTCSS tone is sent on transmit. |
| CTCSS tone value | — | 41 standard tones, 67.0–254.1 Hz (EIA/TIA-603) | — | Selects the CTCSS tone frequency. Enabled only when Tone mode is CTCSS TX. |
| Offset (FM) | 0.0 MHz | 0.0–100.0 MHz, step 0.1 | — | Sets the FM repeater offset frequency. |
| − (offset down) | — | — | — | Sets the TX frequency below the RX frequency by the offset amount. |
| Simplex | checked | — | — | Sets TX frequency equal to RX frequency (no offset). |
| + (offset up) | — | — | — | Sets the TX frequency above the RX frequency by the offset amount. |
| REV | — | — | — | Inverts the TX offset direction to work a reversed repeater pair. |

## Tips

- Filter preset values are saved per mode under `FilterPresets`. If you right-click a preset button and store a custom width, it persists across sessions for that mode.
- The L / R pan slider has a centre-mark dot on the groove. Double-click anywhere on the slider to snap back to centre (50) instantly.
- The AGC threshold tooltip changes its label depending on whether AGC mode is Off or active, so you always know which parameter you are adjusting.
- The 🔓 / 🔒 tune-lock button is the fastest way to prevent a slice from being retuned accidentally while clicking around the panadapter.

## Related

- [Understanding slices and VFOs](../../getting-started/concepts/understanding-slices.md)
- [Switch between multiple slices using the A..H tab row](switch-between-multiple-slices-using-the-a-h-tab-row.md)
- [Tune the radio to a frequency (type MHz in the readout)](tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
- [Change mode (USB, LSB, CW, AM, FM, etc.)](change-mode-usb-lsb-cw-am-fm-etc.md)
- [Pick a filter width preset for the current mode](pick-a-filter-width-preset-for-the-current-mode.md)
- [Select the RX or TX antenna for this slice](select-the-rx-or-tx-antenna-for-this-slice.md)
