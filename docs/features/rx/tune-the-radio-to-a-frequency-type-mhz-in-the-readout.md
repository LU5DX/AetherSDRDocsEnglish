# Tune the radio to a frequency (type MHz in the readout)

Type a frequency directly into the RX Controls applet to move the active slice's VFO to any frequency within the radio's tuning range.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. If not, go to `Settings > Connect to Radio...`.
- The RX Controls applet must be visible. If it is not, click the **RX** tray button on the right sidebar.
- Make sure the slice you want to tune is not locked. If the lock icon shows 🔒, click it to unlock before proceeding (see [Lock the slice to prevent accidental retuning](lock-the-slice-to-prevent-accidental-retuning.md)).

## Steps

1. If you have more than one slice, click the appropriate slice tab (**A**, **B**, **C**, etc.) at the top of the RX Controls applet to select the slice you want to tune.
2. Click the **Frequency label** (the dotted readout, e.g. `0.000.000`). It switches into edit mode, becoming the **Frequency edit** field.
3. Type the desired frequency in MHz. For example, type `14.225` for 14.225 MHz.
4. Press **Enter**. The slice tunes to the entered frequency and the panadapter recenters on it.

To cancel without changing frequency, press **Escape**. The editor closes and the previous frequency is restored.

## What each control does

| Control | Behavior | Default |
|---------|----------|---------|
| **Slice tabs (A..H)** | Selects which slice the RX applet is bound to. Row hidden if the radio supports only one slice. | — |
| **Slice badge** | Displays the letter of the currently bound slice, coloured by slice identity. | A |
| **🔓 / 🔒** | Toggles tune-lock on the slice. Locked slices ignore frequency changes. | 🔓 (unlocked) |
| **ANT1 (RX antenna)** | Opens a menu listing available RX antennas. Selecting sets the slice receive antenna. | ANT1 |
| **ANT1 (TX antenna)** | Opens a menu listing TX-capable antennas. RX-only ports (prefix 'RX') are filtered out. | ANT1 |
| **2.7K (filter width)** | Shows the current filter bandwidth (e.g. 2.7K, 3.3K, 500). | 2.7K |
| **QSK** | Lights amber when CW break-in (QSK) is active. Read-only; controlled via the CW applet. | off (grey) |
| **TX (badge)** | Click to set this slice as the TX slice. | — |
| **Mode combo** | Sets the slice operating mode. Options vary by radio and build flags. | USB |
| **Frequency label** | Displays current VFO frequency with dotted grouping. Click to enter edit mode. | `0.000.000` |
| **Frequency edit** | Text field. Enter frequency in MHz and press Enter to tune and recenter. Escape cancels and restores the previous frequency. | — |
| **STEP** | Sets the step size used when nudging frequency with arrow buttons or mousewheel. Step list depends on mode. | 100 Hz |
| **Filter width presets** | Click a preset button to apply that filter bandwidth. Right-click to save current width into that slot. Hidden in FM/NFM/DFM modes. | — |
| **Filter passband widget** | Drag the lo/hi edges to adjust filter passband directly. | — |
| **Tone mode (FM)** | Selects CTCSS tone mode on FM/NFM/DFM. Visible only in FM family modes. | Off |
| **CTCSS tone value** | Selects the CTCSS tone frequency sent with transmit. Enabled only when Tone mode = CTCSS TX. | — |
| **Offset (FM)** | Sets FM repeater offset frequency in MHz (0.0–100.0 MHz, step 0.1). | 0.0 MHz |
| **− (offset down)** | Sets repeater offset direction to 'down' (TX below RX). | — |
| **Simplex** | Sets repeater offset direction to simplex (TX = RX). | checked |
| **+ (offset up)** | Sets repeater offset direction to 'up' (TX above RX). | — |
| **REV** | Inverts the TX offset sign to work a reversed repeater pair. | — |
| **🔊 / 🔇 (mute)** | Mutes or unmutes the slice audio output. | 🔊 (unmuted) |
| **AF gain** | Adjusts slice audio output gain (0–100). | 70 |
| **L / R pan** | Pans slice audio between left and right channels (0–100). Double-click resets to 50 (centre). | 50 |
| **SQL** | Enables the squelch at the current slider level. | — |
| **Squelch level** | Adjusts squelch threshold (0–100). Takes effect only when SQL is on. | 20 |
| **AGC mode** | Sets slice AGC mode: Off, Slow, Med, Fast. Hidden in FM family modes. | Med |
| **AGC threshold** | Sets AGC threshold (or AGC off-level when AGC mode is Off). | 65 |
| **RIT** | Toggles Receive Incremental Tuning on/off. | — |
| **RIT 0** | Zeroes the RIT offset. | — |
| **RIT offset** | Adjusts RIT offset by 10 Hz steps using arrow buttons or mousewheel. | +0 Hz |
| **XIT** | Toggles Transmit Incremental Tuning on/off. | — |
| **XIT 0** | Zeroes the XIT offset. | — |
| **XIT offset** | Adjusts XIT offset by 10 Hz steps using arrow buttons or mousewheel. | +0 Hz |

## Filter width stepping

From v0.9.8, the applet supports precise mode-correct filter-width stepping through the per-mode preset list. The `stepFilterWidth()` method walks the preset list for the current mode, finds the nearest preset to the current filter width, and applies the next or previous preset in the direction chosen.

This means:

- Widen and narrow shortcuts produce filter widths that match the current mode's preset list (SSB, CW, AM, digital, etc.).
- The filter width update uses `applyFilterPreset()`, which calculates correct low-edge and high-edge geometry for the mode (USB, LSB, CWL, CZU, DIGL, DIGU, RTTY, AM, SAM, etc.).
- No filter change occurs if the slice has no filter widths configured or if the current width already equals the target width.

The filter width readout (shared with VfoWidget via `RxApplet::formatFilterWidth`) uses mode-aware logic so SSB and digital modes display the correct labelled width.

## Slice tab and badge colors

From v0.9.3, slice tab buttons and the **Slice badge** indicator take their border, active background, and text color from the SliceColorManager singleton rather than a fixed color table. Colors are configurable per slice, persist across sessions, and are reflected consistently in the slice tab buttons, the Slice badge, VFO widgets, and meter strips.

## Slice tab row behavior on reconnect

From v0.9.5.1, the slice tab row is rebuilt correctly whenever the number of available slices changes — for example, after a disconnect and reconnect or when the radio reports a different slice count. The previous implementation skipped rebuilding if any tab buttons already existed, which could leave stale buttons on screen.

The updated behavior works as follows:

- If the new slice count matches the number of existing tab buttons, the row is left unchanged.
- If the counts differ, the existing tab buttons are torn down (`clearSliceButtons()`) before new buttons are created.
- On teardown, the tab row is hidden and the static **Slice badge** is restored.
- The signal connection that maps button clicks to `sliceActivationRequested` is established only once per applet instance, regardless of how many times the tab row is rebuilt. This prevents duplicate signal handlers accumulating across reconnects.

No user action is required to take advantage of this fix. The tab row updates automatically.

## Filter width preset storage format

From v0.9.5.1, filter width presets can store either a plain bandwidth value or an explicit low-edge/high-edge pair. This matches the storage format used by VfoWidget and allows presets saved from VfoWidget to be loaded correctly in the RX Controls applet.

The `FilterPresets` setting for each mode (stored under the key `FilterPresets_<mode>`, e.g. `FilterPresets_USB`) accepts a comma-separated list of entries in either of the following formats:

| Format | Example | Meaning |
|--------|---------|---------|
| `width` | `2700` | Bandwidth in Hz; edges are calculated from the mode's default alignment. |
| `lo:hi` | `-1350:1350` | Explicit passband edges in Hz relative to the carrier. Both values must be integers and `hi` must be greater than `lo`. |

Entries that do not conform to either format, or where `hi <= lo`, are silently skipped. The applet loads at most six presets per mode.

You do not normally need to edit these values by hand. Right-clicking a **Filter width presets** button saves the current filter width into that slot using the appropriate format automatically.

## NT mode

v0.9.3 adds the **NT** mode to the mode selector. NT behaves as a digital mode in the following ways:

- It uses the same filter width presets and step sizes as DIGU and DIGL.
- Filter width is calculated from the high-edge value (same as USB, DIGU, and FDV).
- The **SQL** button and squelch level slider are disabled while NT is active, and any active squelch is turned off automatically (same behavior as DIGU and DIGL).

## Tips

- You do not need to type trailing zeros. `14.2` is interpreted as 14.200 MHz.
- To move frequency in small steps without retyping, use the `<` and `>` buttons next to **STEP**, or scroll the mouse wheel over the **Frequency label** after tuning.
- The step size list changes when you switch modes. Changing the **Mode combo** resets the step presets to values appropriate for that mode.
- Filter-width widen and narrow shortcuts walk the per-mode preset list from v0.9.8, giving mode-correct filter geometry with every step.

## Troubleshooting

- **The Frequency edit field does not appear when I click the readout** — The slice may be locked. Check whether the lock icon shows 🔒. If so, click it to unlock, then click the frequency readout again.
- **The frequency I typed was ignored** — You may have pressed Escape instead of Enter, or entered a value outside the valid range (0.001–54.000 MHz on a standard antenna, up to 450.000 MHz on a transverter antenna). Re-enter the value and press Enter.
- **The panadapter did not follow the new frequency** — Check that `View > Pan Follows VFO` is enabled.
- **The SQL button is greyed out after switching to NT mode** — This is expected. NT is a digital mode; squelch is disabled automatically, the same as for DIGU and DIGL.
- **Slice tab buttons show the wrong slices after reconnecting** — This was a known issue in versions before v0.9.5.1. Update to v0.9.5.1 or later; the tab row now rebuilds itself automatically when the slice count changes.

## Related

- [Lock the slice to prevent accidental retuning](lock-the-slice-to-prevent-accidental-retuning.md)
- [Change mode (USB, LSB, CW, AM, FM, etc.)](change-mode-usb-lsb-cw-am-fm-etc.md)
- [Pick a filter width preset for the current mode](pick-a-filter-width-preset-for-the-current-mode.md)
- [Switch between multiple slices using the A..H tab row](switch-between-multiple-slices-using-the-a-h-tab-row.md)
- [Understanding slices and VFOs](../../getting-started/concepts/understanding-slices.md)