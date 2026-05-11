# Select the RX or TX antenna for this slice

The RX Controls applet lets you choose which antenna port the FLEX-8600 uses for receiving and transmitting on each slice independently. Use this when you have multiple antennas connected and need to route a specific slice to a specific port.

## Before you start

- AetherSDR must be connected to the radio. The antenna controls are unavailable without a live connection.
- The antenna list is populated from the radio's own port configuration. Confirm your antennas are connected and recognized by the radio before changing these settings.

## Steps

1. Open the RX Controls applet. If it is not visible, click the **RX** tray button on the right sidebar.
2. If you have more than one slice, click the slice tab (A through H) for the slice you want to change.
3. **To change the RX antenna:** Click the blue antenna label near the top of the applet (shows the current RX antenna, e.g. **ANT1**). A menu appears listing all available antenna ports. Click the port you want. A checkmark shows the current selection.
4. **To change the TX antenna:** Click the red antenna label next to the RX antenna label (also shows the current TX antenna, e.g. **ANT1**). A menu appears listing TX-capable antenna ports. Click the port you want.

## What each control does

| Control                           | Default   | Valid values                                                                |
|-----------------------------------|-----------|-----------------------------------------------------------------------------|
| **ANT1** (RX antenna, blue label) | ANT1      | Antenna ports from the radio's ant_list                                     |
| **ANT1** (TX antenna, red label)  | ANT1      | TX-capable ports from the radio's ant_list                                  |
| **Slice tabs (A..H)**             | None      | 1–8 buttons (capped by hardware max slices)                                 |
| **Slice badge**                   | A         | A/B/C/D/E/F/G/H                                                             |
| **🔓 / 🔒**                         | 🔓         | Unlocked / locked                                                           |
| **Mode combo**                    | USB       | USB, LSB, CW, AM, SAM, FM, NFM, DFM, DIGU, DIGL, RTTY (+ RADE if HAVE_RADE) |
| **Frequency label**               | 0.000.000 | 0.001–54.000 MHz (450.000 MHz on XVTR)                                      |
| **Frequency edit**                | None      | 0.001–54.000 MHz (450.000 MHz on XVTR)                                      |
| **STEP**                          | 100 Hz    | Per-mode list of step sizes                                                 |
| **Filter width presets**          | None      | Per-mode preset widths                                                      |
| **Filter passband widget**        | None      | Drag lo/hi edges to adjust passband                                         |
| **Tone mode (FM)**                | Off       | Off, CTCSS TX                                                               |
| **CTCSS tone value**              | None      | 41 standard EIA/TIA-603 tones (67.0–254.1 Hz)                               |
| **Offset (FM)**                   | 0.0 MHz   | 0.0–100.0 MHz (step 0.1)                                                    |
| **− (offset down)**               | None      | Toggle                                                                      |
| **Simplex**                       | Checked   | Toggle                                                                      |
| **+ (offset up)**                 | None      | Toggle                                                                      |
| **REV**                           | None      | Toggle                                                                      |
| **🔊 / 🔇 (mute)**                  | 🔊         | Unmuted / muted                                                             |
| **AF gain**                       | 70        | 0–100                                                                       |
| **L / R pan**                     | 50        | 0–100                                                                       |
| **SQL**                           | None      | Toggle                                                                      |
| **Squelch level**                 | 20        | 0–100                                                                       |
| **AGC mode**                      | Med       | Off, Slow, Med, Fast                                                        |
| **AGC threshold**                 | 65        | 0–100                                                                       |
| **RIT**                           | None      | Toggle                                                                      |
| **RIT 0**                         | None      | Push button                                                                 |
| **RIT offset**                    | +0 Hz     | Step 10 Hz                                                                  |
| **XIT**                           | None      | Toggle                                                                      |
| **XIT 0**                         | None      | Push button                                                                 |
| **XIT offset**                    | +0 Hz     | Step 10 Hz                                                                  |
| **TX (badge)**                    | None      | Click to set as TX slice                                                    |
| **QSK**                           | None      | Amber when CW break-in active (read-only)                                   |
| **Filter width (indicator)**      | 2.7K      | Current filter bandwidth                                                    |

## Tips

- The RX antenna label is shown in blue; the TX antenna label is shown in red. This is the only visual distinction between the two controls, as they appear side by side in the header row.
- Antenna ports whose names begin with `RX` are filtered out of the TX antenna menu. They will still appear in the RX antenna menu.
- Each slice has its own independent RX and TX antenna assignment. Changing the antenna on slice A does not affect slice B.
- From v0.9.3, the slice tab buttons and the slice badge use per-slice colors managed by SliceColorManager. These colors persist across sessions and are also reflected in VFO widgets and meter strips. The colors are not configurable from the antenna controls page; they apply applet-wide.
- The filter width indicator shares mode-aware formatting logic with the VFO panel (`RxApplet::formatFilterWidth`), ensuring consistent readouts across both locations (#2197).
- The `stepFilterWidth()` method walks the per-mode filter preset list so widen/narrow keyboard shortcuts produce mode-correct edge geometry (#2208). For example, widening from a 2.7 kHz USB filter selects the next larger preset (e.g. 2.9 kHz) with proper edge placement for USB mode rather than a symmetrical passband.

## Slice tab behavior

In v0.9.5.1, the slice tab row gained more robust lifecycle management to fix issues seen across radio reconnects (#2254).

- When the radio reports a different number of slices than the current tab row contains, AetherSDR tears down all existing tab buttons (`clearSliceButtons()`) before rebuilding the row. Previously, the row was only built once per session.
- `clearSliceButtons()` removes all generated tab buttons, hides the tab row, and restores the static slice badge. This is also the state shown when the radio is disconnected.
- The signal connection between the button group and `sliceActivationRequested` is now created only once per session, regardless of how many times the tab row is rebuilt. This prevents duplicate signal handlers accumulating across reconnects.

## Filter preset storage format

From v0.9.5.1, filter presets saved via right-clicking a **Filter width presets** button can store either a plain width or a specific passband edge pair (#2259). This matches the format used by VfoWidget.

- A **plain width** entry is stored as a single integer (e.g. `2700`). When applied, the radio places the passband symmetrically according to the current mode.
- A **lo:hi edge** entry is stored as two integers separated by a colon (e.g. `300:3000`). When applied, AetherSDR sets the low and high passband edges exactly as saved.

Both formats can coexist in the same preset list for a given mode. The setting key is `FilterPresets_<mode>` (e.g. `FilterPresets_USB`). Up to six presets are shown in the RX Controls applet for each mode.

If a saved entry is malformed or has a high edge that does not exceed the low edge, AetherSDR skips that entry silently when loading presets.

## NT mode and RTTY mode behavior

NT and RTTY are digital modes. Their behavior within the RX Controls applet matches other digital modes (DIGU/DIGL) in the following ways:

- **Filter presets** — NT and RTTY use the same filter preset widths as DIGU and DIGL (100–2000 Hz).
- **Filter width display** — The filter width indicator derives its value from the high edge of the passband, the same calculation used for USB, DIGU, and FDV modes.
- **Squelch** — The **SQL** button and squelch level slider are disabled in NT mode and RTTY mode. If squelch was active when you switched into NT or RTTY mode, AetherSDR turns squelch off automatically and restores it when you switch back. This matches the behavior for DIGU and DIGL; CW mode is handled differently because the radio manages its squelch state directly. RTTY squelch disabling prevents gating weak FSK signals that would otherwise be notched out (#2504).

## RADE mode activation

From v26.5.1, RADE mode activation and deactivation logic is improved to prevent spurious deactivation signals in certain scenarios:

- Switching to RADE mode from any other mode correctly activates RADE on the current slice.
- When switching away from RADE mode, AetherSDR only emits a RADE deactivation signal if the slice was actually in RADE mode before the change. This prevents spurious deactivations when:
  - Changing modes on a non-RADE slice
  - Rebinding a slice via the slice tabs
  - Loading profiles that set a non-RADE mode
- The previous behavior could emit false deactivation signals in multi-pan setups or when rapidly switching modes, which has been resolved.

## Troubleshooting

- **An expected antenna port does not appear in the menu** — The list comes directly from the radio's ant_list. Verify the port is configured and recognized in the radio's own settings. AetherSDR cannot add ports that the radio has not reported.
- **The TX antenna menu is missing a port that appears in the RX antenna menu** — Ports whose names begin with `RX` are intentionally excluded from the TX antenna menu because the radio treats them as receive-only.
- **Both labels are greyed out or unresponsive** — AetherSDR is not connected to the radio. Reconnect via `Settings > Connect to Radio...`.
- **SQL button is greyed out after switching to NT or RTTY mode** — NT and RTTY are digital modes. AetherSDR disables squelch in all digital modes (DIGU, DIGL, NT, RTTY) because audio is routed via DAX and squelch has no meaningful effect. Switch to a non-digital mode to re-enable squelch.
- **Slice tab row shows wrong tabs after reconnecting** — In earlier versions, the tab row was built only once and could become stale after a reconnect. From v0.9.5.1, AetherSDR rebuilds the tab row whenever the number of slices changes. If the row still appears incorrect, disconnect and reconnect via `Settings > Connect to Radio...`.
- **A filter preset applies a different passband than expected** — Presets saved before v0.9.5.1 are stored as plain widths and remain valid. Presets saved from v0.9.5.1 onward may store exact lo:hi edges. If a preset behaves unexpectedly, right-click the preset button to overwrite it with the current passband.

## Related

- [RX Controls overview](overview.md)
- [Switch between multiple slices using the A..H tab row](switch-between-multiple-slices-using-the-a-h-tab-row.md)
- [Understanding slices and VFOs](../../getting-started/concepts/understanding-slices.md)