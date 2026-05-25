# Widen or narrow the filter using the mode-correct shortcut (all modes, including LSB/CWL/DIGL/RTTY)

Use the widen/narrow shortcut to step through per-mode filter width presets — one press widens the filter, the other narrows it. The shortcut always applies filter widths appropriate to the current slice mode, so you never get a CW-width filter in SSB or a broadcast-width filter in RTTY.

## Before you start

- A radio must be connected.
- The RX Controls applet must be visible (tray button **RX** on the right sidebar).

## Steps

1. In the RX Controls applet, click the **Mode combo** and select the mode you intend to use (USB, LSB, CW, AM, SAM, DIGU, DIGL, RTTY, FM, etc.). The filter preset list and step sizes update for that mode.
2. Click the left-pointing triangle button (◀) next to the filter width indicator to narrow the filter, or the right-pointing triangle button (▶) to widen it.

Each click moves through the mode's preset list. The current filter width is shown on the **2.7K** (filter width) indicator.

## What each control does

| Control                          | Default        | Behavior                                                                       |
|----------------------------------|----------------|--------------------------------------------------------------------------------|
| **Filter width presets (◀ / ▶)** | See below      | Steps through per-mode filter widths in descending (◀) or ascending (▶) order. |
| **2.7K (filter width)**          | Mode-dependent | Displays the current slice filter bandwidth.                                   |
## Filter width presets by mode

| Mode | Presets (Hz) |
|------|-------------|
| USB, LSB | 1800, 2100, 2400, 2700, 2900, 3300 |
| AM, SAM | 5600, 6000, 8000, 10000, 12000, 14000 |
| CW | 50, 100, 250, 400 |
| DIGU, DIGL | 100, 300, 600, 1000, 1500, 2000 |
| RTTY | 250, 300, 350, 400, 500, 1000 |
| FM, NFM, DFM | No filter presets (buttons hidden) |

## Related

- [Pick a filter width preset for the current mode](pick-a-filter-width-preset-for-the-current-mode.md)
- [Change mode (USB, LSB, CW, AM, FM, etc.)](change-mode-usb-lsb-cw-am-fm-etc.md)

# RX Controls applet

The RX Controls applet provides per-slice receive controls. It appears when you click the **RX** tray button on the right sidebar.

## Controls

| Control | Kind | Default | Behavior |
|---------|------|---------|----------|
| **Slice tabs (A..H)** | tab | — | Selects which slice the RX applet is bound to. Row hidden if maxSlices ≤ 1. |
| **Slice badge** | indicator | A | Displays the letter of the currently bound slice. Coloured by slice identity. The slice letter may be rendered as HTML (#2606). |
| **🔓 / 🔒** | toggle_button | 🔓 (unlocked) | Toggles tune-lock on the slice; locked slice ignores frequency changes. |
| **ANT1 (RX antenna)** | combo_box | ANT1 | Opens a menu listing available antennas; items use the antenna's numeric identifier or the next available label when the slice's own antenna list is empty. Selecting sets slice→setRxAntenna. Blue-coloured label. |
| **ANT1 (TX antenna)** | combo_box | ANT1 | Opens a menu listing TX-capable antennas; RX-only ports (prefix 'RX') are filtered out, and items whose token starts with 'ANT', 'TX', or equals 'XVTR' are shown as fallback. Selecting sets slice→setTxAntenna. Red-coloured label. |
| **2.7K (filter width)** | indicator | 2.7K | Shows current filter width in kHz. Updates when filter preset is applied. |
| **QSK** | indicator | off (grey) | Lights amber when CW break-in (QSK) is active. Read-only; controlled via the CW applet Breakin button. |
| **TX (badge)** | toggle_button | — | Click to set this slice as the TX slice. |
| **Mode combo** | combo_box | USB | Sets slice mode. Options: USB, LSB, CW, AM, SAM, FM, NFM, DFM, DIGU, DIGL, RTTY (+ RADE if HAVE_RADE). RADE option requires HAVE_RADE build flag. |
| **Frequency label** | indicator | 0.000.000 | Displays current VFO frequency with dotted grouping. Click to switch into edit mode. |
| **Frequency edit** | text_field | — | Enter MHz and press Enter to tune and recenter. Uses `FrequencyEntryParser` for normalized text processing. Supports kHz/Hz auto-scaling. Escape cancels entry, restores previous frequency, and dismisses editor. XVTR-aware: accepts up to 50000 MHz when on an XVTR antenna or when the entered value explicitly exceeds 54 MHz. |
| **STEP** | spinbox | 100 Hz (index 2) | Cycles through per-mode step sizes. |
| **Filter width presets** | push_button | — | Click to apply a preset filter width; right-click to save current width as a preset. Buttons hidden for FM/NFM/DFM modes. The width readout uses mode-aware logic so SSB/digital modes display the correct labelled width (#2197). The stepFilterWidth(direction) method walks the per-mode preset list for mode-correct widen/narrow (#2208). |
| **Filter passband widget** | drag_handle | — | Drag the lo/hi edges to adjust filter passband. |
| **Tone mode (FM)** | combo_box | Off | Selects CTCSS tone mode on FM/NFM/DFM. Visible only in FM family modes. |
| **CTCSS tone value** | combo_box | — | Selects CTCSS tone frequency. 41 standard EIA/TIA-603 tones (67.0 Hz to 254.1 Hz). Enabled only when Tone mode = CTCSS TX. |
| **Offset (FM)** | spinbox | 0.0 Mhz | Sets FM repeater offset frequency in MHz. Range 0.0-100.0 MHz (step 0.1). |
| **− (offset down)** | toggle_button | — | Sets repeater offset direction to 'down' (TX below RX). |
| **Simplex** | toggle_button | checked | Sets repeater offset direction to simplex (TX = RX). |
| **+ (offset up)** | toggle_button | — | Sets repeater offset direction to 'up' (TX above RX). |
| **REV** | toggle_button | — | Inverts the TX offset sign to work a reversed repeater pair. |
| **🔊 / 🔇 (mute)** | push_button | 🔊 (unmuted) | Single-click mutes/unmutes this slice (deferred by the platform click-discrimination interval). Double-click mutes/unmutes all owned slices via muteAllToggled signal. Icon flips when the radio acknowledges via SliceModel::audioMuteChanged. Per the Radio-Authoritative Settings Policy (#2489), mute state is NOT saved/restored on reconnect — the radio is the source of truth for audio mute. |
| **AF gain** | slider | 70 | Adjusts slice audio output gain. Range 0-100. |
| **L / R pan** | slider | 50 | Pans slice audio between left (0) and right (100) channels. Double-click resets to 50 (centre). |
| **SQL** | toggle_button | — | Enables the squelch at the current slider level. Disabled (and auto-turned off) in RTTY, digital modes (DIGU, DIGL), and CW modes where squelch would interfere with decoding. |
| **Squelch level** | slider | 20 | Adjusts squelch threshold. Disabled in RTTY, digital, and CW modes. The last user-chosen manual squelch level is persisted across sessions in the `LastManualSquelchLevel` setting, so it survives mode cycles and application restarts. |
| **AGC mode** | combo_box | Med | Sets the slice AGC mode. Options: Off, Slow, Med, Fast. Hidden in FM family modes. |
| **AGC threshold** | slider | 65 | Sets AGC threshold (or AGC off-level when AGC mode is Off). |
| **RIT** | toggle_button | — | Toggles Receive Incremental Tuning on/off. |
| **RIT 0** | push_button | — | Zeroes the RIT offset. |
| **RIT offset** | spinbox | +0 Hz | Adjusts RIT offset by 10 Hz steps. |
| **XIT** | toggle_button | — | Toggles Transmit Incremental Tuning on/off. |
| **XIT 0** | push_button | — | Zeroes the XIT offset. |
| **XIT offset** | spinbox | +0 Hz | Adjusts XIT offset by 10 Hz steps. |

## Squelch behavior in digital and RTTY modes

Squelch is automatically disabled in the following modes:

- **RTTY**
- **DIGU, DIGL**
- **NT** (Narrow-band Digital)
- **CW, CWL**

When switching to any of these modes, the squelch is turned off and the SQL button and slider are disabled. This prevents squelch from gating weak FSK signals and breaking decoding, particularly in RTTY and digital modes where squelch would notch out FSK characters (#2504). The saved squelch state is restored when switching to a non-digital mode. The manual squelch level is preserved across mode switches via the `LastManualSquelchLevel` client-side setting, which remains independent of the radio's automatic squelch levels.

## RADE mode behavior (if enabled)

When RADE mode (Radar Detection) is available (requires HAVE_RADE build flag), selecting RADE from the Mode combo activates the radar detection subsystem for the current slice. The RADE mode is client-side only — the radio echoes back the real mode (DIGL/DIGU) immediately after setting RADE, so the slice's mode() will never be "RADE" after the radio responds. Switching away from RADE on the slice that is currently in RADE mode deactivates radar detection. The system correctly handles mode changes across slice rebinds, VFO combo changes, and profile loads.

## Frequency entry details

When entering a frequency in the **Frequency edit** text field:

- The text is normalized using `FrequencyEntryParser::normalizedMhzText()` to strip separator dots.
- If the entered value explicitly exceeds 54 MHz (detected via `FrequencyEntryParser::isExplicitMhzEntry()`), the frequency is treated as a high-VHF/UHF entry even without an XVTR antenna.
- When on an XVTR antenna or when the entered value exceeds 54 MHz, the maximum allowed frequency is 50000 MHz.
- For non-XVTR entries under 54 MHz, standard auto-scaling applies: values above 54000 are divided by 1e6, values above 54 are divided by 1e3.
- The entry emits `directEntryCommitted(freqMhz, "rx-direct-entry")` for consistency with other frequency entry paths.

## Mute button behavior

The **🔊 / 🔇 (mute)** button uses a push_button (non-checkable) with click discrimination:

- **Single-click**: Toggles mute for this slice only. The action is deferred by the platform double-click interval (typically ~400 ms) so a double-click can override it.
- **Double-click**: Toggles mute for all owned slices via the `muteAllToggled` signal. The second click cancels the single-click timer.
- The icon (🔊/🔇) updates only when the radio acknowledges the mute state change through `SliceModel::audioMuteChanged`, ensuring the displayed state matches the radio's actual state.
- Mute state is not saved or restored on reconnect — the radio is always the source of truth.