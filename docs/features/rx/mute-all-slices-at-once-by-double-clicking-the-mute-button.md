# Mute all slices at once by double-clicking the mute button

Mute or unmute every slice you own in one action, without muting each slice individually.

## Before you start

- You must have more than one active slice (tabs A through H are visible in the RX Controls applet).
- The mute button is the speaker icon (🔊 / 🔇) in the RX Controls applet.

## Steps

1. In the RX Controls applet, double-click the mute button (🔊 when unmuted, 🔇 when muted).
2. All slices you own are muted or unmuted together, matching the new state of the button.

## What each control does

| Control | Label | Default |
|---------|-------|---------|
| Slice tabs (A..H) | A..H | None |
| Slice badge | A | A |
| Tune lock | 🔓 / 🔒 | 🔓 (unlocked) |
| RX antenna | ANT1 | ANT1 |
| TX antenna | ANT1 | ANT1 |
| Filter width | 2.7K | 2.7K |
| QSK | QSK | Off (grey) |
| TX badge | TX | None |
| Mode combo | USB | USB |
| Frequency label | 0.000.000 | 0.000.000 |
| Frequency edit | (text field) | None |
| STEP | (spinbox) | 100 Hz (index 2) |
| Filter width presets | (buttons) | Per mode |
| Filter passband widget | (drag handles) | None |
| Tone mode (FM) | Off | Off |
| CTCSS tone value | (combo) | None |
| Offset (FM) | 0.0 MHz | 0.0 MHz |
| Offset down | − | None |
| Simplex | Simplex | Checked |
| Offset up | + | None |
| REV | REV | None |
| Mute button | 🔊 / 🔇 | 🔊 (unmuted) |
| AF gain | (slider) | 70 |
| L / R pan | (slider) | 50 |
| SQL | SQL | None |
| Squelch level | (slider) | 20 |
| AGC mode | Med | Med |
| AGC threshold | (slider) | 65 |
| RIT | RIT | None |
| RIT 0 | RIT 0 | None |
| RIT offset | +0 Hz | +0 Hz |
| XIT | XIT | None |
| XIT 0 | XIT 0 | None |
| XIT offset | +0 Hz | +0 Hz |

## Tips

- The single-click action is deferred by the platform's double-click discrimination interval (~400 ms) so a double-click cancels the single-click timer and triggers the all-slice action instead.
- Mute state is not saved or restored on reconnect — the radio is the source of truth for audio mute.
- The filter width readout is shared with the VFO panel for consistent formatting. The `stepFilterWidth()` method walks per-mode preset lists so widen/narrow shortcuts produce mode-correct edge geometry.
- Switching to RTTY or digital modes (DIGU, DIGL) automatically disables squelch, which would otherwise notch out FSK characters and break decoding.
- When switching out of RADE mode via the mode combo, the applet emits `radeActivated(false)` only if the slice was actually in RADE, preventing stale deactivate signals when changing modes on a non-RADE slice.
- The RX antenna menu now includes virtual antenna tokens from a connected KiwiSDR if the KiwiSDR manager is active. Selecting a KiwiSDR virtual antenna emits `kiwiRxAntennaSelected(sliceId, profileId)` instead of calling `setRxAntenna()` directly.

## Related

- [RX Controls overview](overview.md)
- [Switch between multiple slices using the A..H tab row](switch-between-multiple-slices-using-the-a-h-tab-row.md)
- [Understand why mute state is not restored on reconnect (radio-authoritative policy #2489)](../../getting-started/setup/understand-why-mute-state-is-not-restored-on-reconnect-radio-authoritative-policy-2489.md)