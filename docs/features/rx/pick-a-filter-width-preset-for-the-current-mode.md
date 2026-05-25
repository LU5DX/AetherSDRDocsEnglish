# Pick a filter width preset for the current mode

Use the filter width preset buttons in the RX Controls applet to quickly apply a standard passband width for the active mode. Presets are saved per mode in `FilterPresets`.

## Before you start

- AetherSDR must be connected to the radio. The RX Controls applet requires an active radio connection.
- Select the slice you want to adjust using the slice tabs (A..H) if more than one slice is active.
- Set the slice mode first. Preset values differ by mode, and presets are not shown for FM, NFM, or DFM modes.

## Steps

1. Open the RX Controls applet. If it is not visible, click the RX tray button on the right sidebar.
2. If the slice tab row is visible, click the tab (A through H) for the slice you want to adjust.
3. Confirm the mode shown in the Mode combo is correct. Filter presets change when the mode changes.
4. Click any of the filter width preset buttons to apply that bandwidth immediately. The current filter width shown in the filter width label (for example, `2.7K`) updates to reflect the applied preset.
5. To save the current filter passband as a preset, right-click any filter width preset button and choose to save the current width. The value is stored in `FilterPresets`.

## What each control does

| Control                | Behavior                                                                                                                                                                | Default presets by mode                                                                                                                                                                                                                                                                                                                 |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter width presets   | Click to apply a preset filter width; right-click to save current width as a preset.                                                                                    | Buttons hidden for FM/NFM/DFM modes; presets are per-mode. The width readout (shared with VfoWidget via RxApplet::formatFilterWidth) uses mode-aware logic so SSB/digital modes display the correct labelled width (#2197). The stepFilterWidth(direction) method walks the per-mode preset list for mode-correct widen/narrow (#2208). |
| Filter width label     | Read-only indicator showing the current filter bandwidth (for example, `2.7K`, `500`, `6.0K`). Updates when a preset is applied or when the passband edges are dragged. | —                                                                                                                                                                                                                                                                                                                                       |
| Filter passband widget | Drag the low or high edge to set a custom passband. Use presets for standard widths.                                                                                    | —                                                                                                                                                                                                                                                                                                                                       |
| Mode                   | Preset widths (Hz)                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                         |
| ---                    | ---                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                         |
| USB, LSB               | 1800, 2100, 2400, 2700, 2900, 3300                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                         |
| AM, SAM                | 5600, 6000, 8000, 10000, 12000, 14000                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                         |
| CW                     | 50, 100, 250, 400                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                         |
| DIGU, DIGL, NT         | 100, 300, 600, 1000, 1500, 2000                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                         |
| RTTY                   | 250, 300, 350, 400, 500, 1000                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                         |
| FM, NFM, DFM           | No presets (buttons hidden)                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                         |
| RADE                   | No presets (client-side only, radio echoes back real mode)                                                                                                              |                                                                                                                                                                                                                                                                                                                                         |
## Narrowing and widening the filter passband via step

The `stepFilterWidth(direction)` method lets you walk through the per-mode preset list from any application shortcut or key binding. Pass `+1` to widen the passband to the next larger preset, or `-1` to narrow to the next smaller preset. Because `stepFilterWidth` routes through `applyFilterPreset`, all modes — including LSB, CWL, DIGL, RTTY, AM, and CW — use the correct edge geometry for that mode rather than a symmetric assumption.

Internally, the method finds the preset whose width is closest to the current slice's passband, then moves to the next or previous entry in the list (clamped to valid bounds). If the current width already equals the nearest preset and the step would move beyond the list, the operation is ignored.

## Filter preset storage format (v0.9.5.1)

Starting in v0.9.5.1, filter presets stored in `FilterPresets` can represent either a plain bandwidth or a fully specified passband with explicit low and high edge offsets. Both formats are accepted when loading saved presets.

- **Width-only format** — A single integer representing bandwidth in Hz (for example, `2700`). When applied, the radio positions the passband symmetrically around the carrier according to the mode's default offset rules.
- **Lo:Hi format** — Two integers separated by a colon representing the low and high passband edge offsets in Hz (for example, `300:3000`). The width is derived as `hi − lo`. The `hi` value must be greater than the `lo` value or the entry is ignored.

Entries in either format may appear in the same saved preset list for a given mode. The list is comma-separated. Up to six entries are loaded for the RX Controls applet (matching the maximum number of preset buttons displayed).

If a saved preset list is changed externally or a reconnect causes the radio to report a different slice count, the preset buttons are rebuilt automatically to reflect the stored values.

## Noise reduction and DSP filter button visibility

The following table summarises which noise-reduction and DSP filter buttons are visible based on radio series and mode.

| Button | 6000-series | 8000-series (extended DSP) | Hidden when |
|--------|-------------|---------------------------|-------------|
| NR     | Yes         | Yes                       | FM mode     |
| NR2    | Yes         | Yes                       | FM mode     |
| NB     | Yes         | Yes                       | FM mode     |
| NRL    | Yes         | Yes                       | FM mode     |
| NRS    | No          | Yes                       | FM mode     |
| RNN    | No          | Yes                       | CW or FM mode |
| NRF    | No          | Yes                       | FM mode     |

Prior to V0.9.4, the NRL button was only shown on 8000-series radios (extended DSP). Starting in V0.9.4, NRL is also available on 6000-series radios. NRS, RNN, and NRF remain 8000-series only.

## Slice tab and badge colors (v0.9.3)

Starting in v0.9.3, slice tab buttons and the slice badge use per-slice colors managed by the `SliceColorManager` singleton rather than a fixed color table. The active border, background highlight on the tab buttons, and the badge background all reflect the color assigned to that slice. Colors persist across sessions and are also reflected in VFO widgets and meter strips. No action is required; the colors update automatically when a slice is connected.

## Slice tab behavior on reconnect (v0.9.5.1)

When AetherSDR disconnects from the radio and reconnects, or when the number of available slices changes, the slice tab row is rebuilt correctly. Specifically:

- If the number of slices reported by the radio differs from the number of tab buttons currently shown, `clearSliceButtons()` tears down all existing tab buttons and the row is reconstructed from scratch.
- While the tab row is torn down, the static slice badge is restored so the applet continues to show which slice is bound.
- Signal connections from the tab buttons to the slice activation handler are established only once per applet instance, preventing duplicate handlers from accumulating across reconnects.

No user action is required. If the slice count changes (for example, after a disconnect and reconnect cycle), the tab row updates automatically.

## RX antenna selection improvements (v26.5.2.1)

In v26.5.2.1, the RX antenna selection menu was improved to show the slice's dedicated RX antenna list when available, rather than the global antenna list from the panadapter status. If the slice has an RX antenna list, the menu displays those entries; otherwise it falls back to the global antenna list. Each menu item now:

- Uses the antenna identifier as its underlying data value (`act->setData(ant)`)
- Shows a human-readable label via `antennaMenuLabel()`
- Shows the raw antenna identifier in the tooltip and status tip

The TX antenna selection menu was also updated to use the `txAntennaOptions()` method and `antennaMenuLabel()`. Both menus now use `sel->data().toString()` when setting the antenna, so the label text is secondary to the antenna identifier.

No configuration is needed. The menus update automatically when reconnected to the radio.

## RADE mode deactivation logic change (v26.5.2.1)

In v26.5.2.1, the RADE mode deactivation signal behavior was corrected. Previously, when switching out of RADE mode via the mode combo, the applet checked `m_slice->mode() == "RADE"` before emitting `radeActivated(false)`. This check no longer works correctly because RADE is a client-side only mode — the radio echoes back the real mode (DIGL/DIGU) immediately, so `mode()` never returns "RADE" at the point of the check. The stale check has been removed.

The RADE option remains available in the mode combo only when `HAVE_RADE` is defined at build time.

## Manual squelch level persistence (v26.5.2.1)

Starting in v26.5.2.1, the manual squelch threshold is saved and restored across sessions via the application settings key `LastManualSquelchLevel`. This prevents the value from being clobbered by auto-mode squelch logic that the radio applies. The threshold is recalled when the RX Controls applet is constructed.

## Mute button behavior (v26.5.3)

In v26.5.3, the mute button behavior was updated. The mute button is no longer a checkable toggle button — it is a plain push button. Single-clicking the button mutes/unmutes the current slice using a deferred timer. Double-clicking the button mutes/unmutes all owned slices. The visual icon (🔊/🔇) updates only when the radio acknowledges the mute state change via `SliceModel::audioMuteChanged`, not on the click itself.

The mute state is NOT saved or restored on reconnect — the radio is the source of truth for audio mute.

## Frequency entry improvements (v26.5.3)

In v26.5.3, the frequency entry parser was updated. The `FrequencyEntryParser` utility handles normalisation of MHz text input. The frequency entry now supports explicit MHz entries above 54 MHz even when not on an XVTR antenna — if the user enters a value with an explicit decimal point and the value is above 54 MHz, the system treats it as a valid MHz entry (up to 50000 MHz) rather than applying kHz scaling.

The 3-digit-band convenience feature (for example, typing `1446` to tune to 144.6 MHz) continues to work on XVTR antennas only.

When a valid frequency is entered and committed, the applet emits `directEntryCommitted(freqMhz, "rx-direct-entry")` instead of calling `tuneAndRecenter()` directly.

## Tips

- If you need a width that does not match any preset, drag the edges of the filter passband widget to set an arbitrary value, then right-click a preset button to save that width for future use.
- When saving a preset by right-clicking a preset button, the passband is stored in lo:hi format if the current passband edges have been set explicitly, or in width-only format otherwise. Both formats are loaded correctly on all subsequent sessions.
- Presets are per mode. Switching modes reshapes the filter and displays the preset buttons for the new mode.
- NT and RTTY modes use the same filter presets and squelch behavior as DIGU and DIGL. Squelch is disabled in NT, DIGU, DIGL, and RTTY modes, and squelch off is sent to the radio automatically if squelch was previously enabled. RTTY mode was added to the auto-disable list in v26.5.1 to prevent squelch from notching out FSK characters (#2504).
- Use the `stepFilterWidth` method from key bindings or macro scripts to widen and narrow the filter passband without clicking the preset buttons directly. The method always lands on a mode-appropriate preset.

## Troubleshooting

- **Preset buttons are not visible** — The active mode is FM, NFM, or DFM. These modes do not expose filter presets. Change the mode using the Mode combo to a mode that supports presets (for example, USB or CW).
- **Right-click on a preset button does nothing visible** — Confirm the slice is connected to the radio. The RX applet requires an active radio connection to save preset values.
- **NRL button is not visible on a 6000-series radio** — Confirm you are running V0.9.4 or later. Earlier versions restricted NRL to 8000-series radios only.
- **Squelch controls are greyed out** — The active mode is DIGU, DIGL, NT, RTTY, CW, or CWL. Squelch is disabled in these modes. In digital modes (including NT and RTTY) squelch is turned off automatically; in CW modes the radio manages squelch state directly.
- **Slice tab row is blank after reconnecting** — This could occur on versions prior to v0.9.5.1. Upgrade to