# RX Controls overview

The RX Controls applet gives you per-slice receive control: frequency tuning, mode, filter width, antenna selection, AGC, audio output, squelch, RIT/XIT, and FM repeater settings. Everything that affects how a single slice receives and presents audio lives here.

## Before you start

- Connect to a FLEX-8600 radio. The applet requires an active radio connection.
- The RX applet is always visible in the Applet Panel (right sidebar). If the panel is hidden, show it with View > Applet Panel, or click the RX tray button on the right sidebar.

## How it works

The applet is bound to one slice at a time. When your radio has more than one slice active, a row of tabs labelled A through H appears at the top of the applet. Click any tab to rebind the applet to that slice. All controls then reflect and operate on that slice only.

Changes made in the applet are sent immediately to the radio over the SmartSDR protocol. There is no Apply or Save step for most controls. The one exception is filter width presets: your customised preset widths are saved to the `FilterPresets` AppSettings key and persist across sessions.

## What each control does

### Slice selection and header

| Control | Default | Behavior |
|---|---|---|
| Slice tabs (A..H) | — | Selects which slice the applet controls. The tab row is hidden when only one slice is active. |
| Slice badge | A | Displays the letter of the currently bound slice. Color reflects slice identity. |
| 🔓 / 🔒 | 🔓 (unlocked) | Toggles tune-lock. A locked slice ignores frequency changes from clicks, scroll, or external control. |
| ANT1 (RX antenna) | ANT1 | Opens a menu of available antennas. Select one to set the RX antenna for this slice. Label is blue. |
| ANT1 (TX antenna) | ANT1 | Opens a menu of TX-capable antennas (RX-only ports are excluded). Select one to set the TX antenna for this slice. Label is red. |
| Filter width label | 2.7K | Read-only indicator showing the current filter bandwidth. Updates when a preset is applied or the passband is dragged. |
| QSK | off (grey) | Lights amber when CW full break-in is active. Read-only; controlled from the CW applet. |
| TX (badge) | — | Click to designate this slice as the TX slice. |

### Mode and frequency

| Control | Default | Behavior |
|---|---|---|
| Mode combo | USB | Sets the slice mode. Available modes: USB, LSB, CW, AM, SAM, FM, NFM, DFM, DIGU, DIGL, RTTY. Changing mode reshapes the filter and step presets. |
| Frequency label | 0.000.000 | Displays the current VFO frequency with dotted grouping. Click to enter edit mode. |
| Frequency edit | — | Type a frequency in MHz and press Enter to tune and re-center the panadapter. Accepts values from 0.001 to 54.000 MHz (up to 450.000 MHz on a transverter antenna). |
| STEP | 100 Hz | Sets the tuning step size. Click < or > or use the scroll wheel to cycle through the per-mode step list. Step options depend on the active mode (example for SSB: 1, 10, 50, 100, 500, 1000, 2000, 3000 Hz). |

### Filter

| Control | Default | Behavior |
|---|---|---|
| Filter width presets | — | Buttons apply a preset filter width for the current mode. Right-click a preset button to save the current filter width to that slot. Hidden in FM, NFM, and DFM modes. Presets are stored in `FilterPresets`. |
| Filter passband widget | — | Drag the low or high edge of the passband display to set a custom filter boundary. |

### AGC

| Control | Default | Valid range | Behavior |
|---|---|---|---|
| AGC mode | Med | Off, Slow, Med, Fast | Sets the AGC mode. Hidden in FM family modes. |
| AGC threshold | 65 | 0–100 | Sets the AGC threshold. When AGC mode is Off, adjusts the AGC off-level instead. |

### Audio output

| Control | Default | Valid range | Behavior |
|---|---|---|---|
| 🔊 / 🔇 (mute) | 🔊 (unmuted) | — | Mutes or unmutes the slice audio output. |
| AF gain | 70 | 0–100 | Adjusts the slice audio output level. |
| L / R pan | 50 | 0–100 | Pans the slice audio between left (0) and right (100). Double-click resets to 50 (centre). |
| SQL | off | — | Enables squelch at the current slider level. |
| Squelch level | 20 | 0–100 | Sets the squelch threshold. Has no effect when SQL is off. |

### RIT and XIT

| Control | Default | Behavior |
|---|---|---|
| RIT | off | Toggles Receive Incremental Tuning. When on, the slice receive frequency shifts by the RIT offset without moving the VFO. |
| RIT 0 | — | Zeroes the RIT offset immediately. |
| RIT offset | +0 Hz | Adjusts the RIT offset in 10 Hz steps. Use < / > or the scroll wheel. |
| XIT | off | Toggles Transmit Incremental Tuning. When on, the TX frequency shifts by the XIT offset without changing RX. |
| XIT 0 | — | Zeroes the XIT offset immediately. |
| XIT offset | +0 Hz | Adjusts the XIT offset in 10 Hz steps. Use < / > or the scroll wheel. |

### FM repeater controls

These controls are visible only when the slice mode is FM, NFM, or DFM.

| Control | Default | Valid range | Behavior |
|---|---|---|---|
| Tone mode (FM) | Off | Off, CTCSS TX | Selects whether a CTCSS tone is transmitted. |
| CTCSS tone value | — | 67.0 Hz to 254.1 Hz (41 standard EIA/TIA-603 tones) | Selects the CTCSS tone frequency. Enabled only when Tone mode is set to CTCSS TX. |
| Offset (FM) | 0.0 MHz | 0.0–100.0 MHz (step 0.1) | Sets the FM repeater offset frequency. |
| − (offset down) | — | — | Sets the repeater TX offset direction to down (TX below RX). |
| Simplex | checked | — | Sets the repeater offset to simplex (TX equals RX). |
| + (offset up) | — | — | Sets the repeater TX offset direction to up (TX above RX). |
| REV | — | — | Inverts the TX offset sign to work a reversed repeater pair. |

## Tips

- The L / R pan slider has a small centre-mark dot on its groove. Double-click it to snap back to centre (50) without guessing.
- Filter width presets are per-mode. Customised preset widths you save in one mode do not affect other modes.
- RX-only antenna ports (those whose names begin with "RX") are automatically excluded from the TX antenna menu.

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
