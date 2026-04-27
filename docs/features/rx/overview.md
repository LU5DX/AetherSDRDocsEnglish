# RX Controls overview

The RX Controls applet gives you per-slice control over every receive parameter: mode, frequency, antenna selection, filter width, AGC, audio, squelch, RIT/XIT, and FM repeater settings. Open it whenever you need to configure how a slice receives or transmits.

## How it works

The RX applet is always present in the Applet Panel (right sidebar). Toggle its visibility with the RX tray button. When the radio supports more than one slice, a row of slice tabs (A through H) appears at the top; clicking a tab binds the applet to that slice. All controls below the tab row affect the currently selected slice only.

Filter width presets are the one setting that persists across sessions, stored under the `FilterPresets` key. Every other control reflects live radio state and is not independently saved by AetherSDR.

## What each control does

### Slice selection and identity

| Control | Default | Behavior |
|---|---|---|
| Slice tabs (A..H) | — | Select which slice the applet controls. The tab row is hidden when the radio has only one slice. |
| Slice badge | A | Displays the letter of the active slice, coloured by slice identity. Read-only. |
| 🔓 / 🔒 | 🔓 (unlocked) | Toggles tune-lock. A locked slice ignores frequency changes from the panadapter and other sources. |
| TX (badge) | — | Click to designate this slice as the TX slice. |

### Frequency and mode

| Control | Default | Valid range | Behavior |
|---|---|---|---|
| Mode combo | USB | USB, LSB, CW, AM, SAM, FM, NFM, DFM, DIGU, DIGL, RTTY | Sets slice mode. Changing mode reshapes filter and step presets automatically. |
| Frequency label | 0.000.000 | — | Displays the current VFO frequency with dotted grouping. Click to enter edit mode. |
| Frequency edit | — | 0.001–54.000 MHz (up to 450.000 MHz on XVTR) | Type a frequency in MHz and press Enter to tune and re-center. Press Escape to cancel and restore the previous frequency. |
| STEP | 100 Hz | Per-mode list (e.g. SSB: 1, 10, 50, 100, 500, 1000, 2000, 3000 Hz) | Click the left/right triangle buttons or use the mouse wheel to cycle through step sizes. The available steps change with mode. |

### Antenna selection

| Control | Default | Behavior |
|---|---|---|
| ANT1 (RX antenna) | ANT1 | Opens a menu of available antennas from the radio's antenna list. Select to set the RX antenna for this slice. Label is blue. |
| ANT1 (TX antenna) | ANT1 | Opens a menu of TX-capable antennas. RX-only ports (names starting with `RX`) are excluded. Label is red. |

### Filter

| Control | Default / range | Setting key | Behavior |
|---|---|---|---|
| Filter width presets | USB/LSB: 1800/2100/2400/2700/2900/3300 Hz; CW: 50/100/250/400 Hz; AM/SAM: 5600–14000 Hz; DIG: 100–2000 Hz; RTTY: 250–1000 Hz | `FilterPresets` | Click a button to apply that width. Right-click to save the current filter width as a preset. Buttons are hidden in FM, NFM, and DFM modes. |
| Filter width label | 2.7K | — | Shows the current filter bandwidth. Updates when a preset is applied or the passband is dragged. Read-only. |
| Filter passband widget | — | — | Drag the low or high edge to set a custom filter passband. |

### AGC

| Control | Default | Valid range | Behavior |
|---|---|---|---|
| AGC mode | Med | Off, Slow, Med, Fast | Sets the AGC response speed. Hidden in FM family modes. |
| AGC threshold | 65 | 0–100 | Sets the AGC threshold. When AGC mode is Off, adjusts the AGC off-level instead. |

### Audio

| Control | Default | Valid range | Behavior |
|---|---|---|---|
| 🔊 / 🔇 (mute) | 🔊 (unmuted) | — | Mutes or unmutes the slice audio output. |
| AF gain | 70 | 0–100 | Adjusts the slice audio output level. |
| L / R pan | 50 | 0–100 | Pans audio between left (0) and right (100) channels. Double-click to reset to centre (50). |
| SQL | — | — | Enables squelch at the level set by the squelch slider. |
| Squelch level | 20 | 0–100 | Sets the squelch threshold. Takes effect only when SQL is on. |

### RIT and XIT

| Control | Default | Behavior |
|---|---|---|
| RIT | off | Toggles Receive Incremental Tuning on or off. |
| RIT 0 | — | Zeroes the RIT offset immediately. |
| RIT offset | +0 Hz | Adjust with the left/right buttons or mouse wheel in 10 Hz steps. |
| XIT | off | Toggles Transmit Incremental Tuning on or off. |
| XIT 0 | — | Zeroes the XIT offset immediately. |
| XIT offset | +0 Hz | Adjust with the left/right buttons or mouse wheel in 10 Hz steps. |

### Indicators

| Indicator | States | Meaning |
|---|---|---|
| QSK | Grey / amber | Lights amber when CW full break-in is active. Controlled from the CW applet; read-only here. |

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
| REV | — | — | Inverts the offset direction to work a reversed repeater pair. |

## Tips

- The L / R pan slider has a centre-mark dot on the groove to help you find 50 by eye. Double-clicking always resets it to 50 regardless of the current position.
- Right-clicking a filter preset button saves the current filter width into that slot, letting you customise presets per mode. These are stored in `FilterPresets` and survive application restarts.
- The Frequency edit field accepts kHz and Hz auto-scaling, so you do not need to type leading zeros for sub-MHz values.

## Related

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
- [Understanding slices and VFOs](../../getting-started/concepts/understanding-slices.md)
