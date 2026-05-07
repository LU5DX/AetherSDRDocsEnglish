# Fix stale slice tabs after switching to a radio with fewer slices

When you disconnect from one radio and connect to another that has fewer slices, the RX applet's slice tab row (buttons A through H) may still show tabs from the previous session. This page explains how to clear those stale tabs and restore a clean state.

## Before you start

- You have already disconnected from the first radio and are connected to, or are about to connect to, a second radio with fewer available slices.
- The RX applet is visible in the Applet Panel. If it is not, click the **RX** tray button on the right sidebar.

## Steps

1. Disconnect from the current radio if you have not already done so. Use `Settings > Connect to Radio...` to open the connection dialog, then close or cancel the existing connection.
2. Observe the slice tab row at the top of the RX applet. If tabs (for example A, B, C, D) from the previous radio are still shown, they are stale.
3. Connect to the new radio using `Settings > Connect to Radio...` and select the target radio.
4. Once the new connection is established, AetherSDR calls `clearSliceButtons()` internally on disconnect, which tears down all generated slice tab buttons and restores the static slice badge. The slice tab row will then be repopulated to match the new radio's maximum slice count.
5. Confirm that the slice tab row now shows only the correct number of tabs (capped at the new radio's hardware maximum). If the new radio supports only one slice, the tab row is hidden entirely and only the slice badge is shown.

## What each control does

| Control | Behavior | Default |
|---------|----------|---------|
| Slice tabs (A..H) | Selects which slice the RX applet is bound to; emits sliceActivationRequested. | Row hidden if maxSlices <= 1. clearSliceButtons() tears down all generated tab buttons and restores the static slice badge on disconnect (v0.9.5.1, #2254). Slice button click connections are guarded against duplicate signal handlers across reconnects. |
| Slice badge | Displays the letter of the currently bound slice. Shown at all times; the only slice indicator visible when the tab row is hidden. | A |
| 🔓 / 🔒 | Toggles tune-lock on the slice; locked slice ignores frequency changes. | 🔓 (unlocked) |
| ANT1 (RX antenna) | Opens a menu listing available antennas; selecting sets slice->setRxAntenna. Populated from the radio's ant_list. | ANT1 |
| ANT1 (TX antenna) | Opens a menu listing TX-capable antennas; sets slice->setTxAntenna. RX-only antenna ports (prefix 'RX') are filtered out. | ANT1 |
| 2.7K (filter width) | Shows current filter width in kHz. Updates when filter preset is applied. | 2.7K |
| QSK | Lights amber when CW break-in (QSK) is active. Read-only; controlled via the CW applet Breakin button. | off (grey) |
| TX (badge) | Click to set this slice as the TX slice (calls slice->setTxSlice). | None |
| Mode combo | Sets slice mode; reshapes filter and step presets for the new mode. Options: USB, LSB, CW, AM, SAM, FM, NFM, DFM, DIGU, DIGL, RTTY (+ RADE if HAVE_RADE). | USB |
| Frequency label | Displays current VFO frequency with dotted grouping. Click to switch into edit mode. | 0.000.000 |
| Frequency edit | Enter MHz and press Enter to tune and recenter; supports kHz/Hz auto-scaling. Escape cancels the entry, restores the previous frequency, and dismisses the editor. | None |
| STEP | `<` / `>` or mousewheel cycles through per-mode step sizes; emits stepSizeChanged. Step list depends on slice mode. | 100 Hz (index 2) |
| Filter width presets | Click to apply a preset filter width; right-click to save current width as a preset. The width readout uses mode-aware logic so SSB/digital modes display the correct labelled width. Keywords Widen/Narrow (if assigned to keyboard shortcuts) step through the per-mode preset list for mode-correct edge geometry. | Per-mode list |
| Filter passband widget | Drag the lo/hi edges to adjust filter passband; emits filterChanged (lo, hi). | None |
| Tone mode (FM) | Selects CTCSS tone mode on FM/NFM/DFM. Visible only in FM family modes. | Off |
| CTCSS tone value | Selects CTCSS tone frequency sent with transmit. Enabled only when Tone mode = CTCSS TX. | None |
| Offset (FM) | Sets FM repeater offset frequency in MHz. | 0.0 MHz |
| − (offset down) | Sets repeater offset direction to 'down' (TX below RX). | None |
| Simplex | Sets repeater offset direction to simplex (TX = RX). | checked |
| + (offset up) | Sets repeater offset direction to 'up' (TX above RX). | None |
| REV | Inverts the TX offset sign to work a reversed repeater pair. | None |
| 🔊 / 🔇 (mute) | Mutes the slice audio output. | 🔊 (unmuted) |
| AF gain | Adjusts slice audio output gain; emits afGainChanged. | 70 |
| L / R pan | Pans slice audio between left (0) and right (100) channels. Double-click resets to 50 (centre). | 50 |
| SQL | Enables the squelch at the current slider level. | None |
| Squelch level | Adjusts squelch threshold; takes effect only when SQL is on. | 20 |
| AGC mode | Sets the slice AGC mode. Options: Off, Slow, Med, Fast. Hidden in FM family modes. | Med |
| AGC threshold | Sets AGC threshold (or AGC off-level when AGC mode is Off). Tooltip reflects which value is being adjusted. | 65 |
| RIT | Toggles Receive Incremental Tuning on/off. | None |
| RIT 0 | Zeroes the RIT offset. | None |
| RIT offset | `<` / `>` or mousewheel adjusts RIT offset by 10 Hz steps. | +0 Hz |
| XIT | Toggles Transmit Incremental Tuning on/off. | None |
| XIT 0 | Zeroes the XIT offset. | None |
| XIT offset | `<` / `>` or mousewheel adjusts XIT offset by 10 Hz steps. | +0 Hz |

## Tips

- Slice tab buttons are capped by the connected radio's hardware maximum. A radio that supports two slices will never show more than two tabs, regardless of what the previous radio had.
- Duplicate signal handler connections are guarded across reconnects, so reconnecting to the same radio multiple times will not multiply the tab click responses.
- The **Widen** and **Narrow** keyboard shortcuts (or equivalent MIDI/GPIO actions) step the active slice's filter passband through the per-mode preset list via `stepFilterWidth()`. This ensures all modes (LSB, CWL, DIGL, RTTY, AM, CW, USB) produce mode-correct edge geometry.

## Troubleshooting

- **Stale tabs remain after reconnecting** — This can occur if the disconnect event did not fire cleanly. Disconnect again using `Settings > Connect to Radio...`, wait for the slice badge to reappear in place of the tabs, then reconnect.
- **Tab row is missing entirely after connecting** — If the new radio reports a maximum slice count of 1 or fewer, the tab row is intentionally hidden. Only the slice badge is shown. This is expected behavior.
- **Filter width readout appears incorrect after mode change** — The filter width formatter (`formatFilterWidth()`) is shared with the VFO panel and uses mode-aware logic. If the readout seems wrong, try cycling through filter presets to refresh the displayed value.

## Related

- [Switch between multiple slices using the A..H tab row](switch-between-multiple-slices-using-the-a-h-tab-row.md)
- [RX Controls overview](overview.md)
- [Understanding slices and VFOs](../../getting-started/concepts/understanding-slices.md)