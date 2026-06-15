# Assign a DAX channel from the VFO panel

DAX (Digital Audio Exchange) routes a slice's received audio to a named audio channel on your computer. Use this procedure to assign or change the DAX channel for any slice directly from its VFO panel.

## Before you start

- AetherSDR must be connected to the radio. The VFO panel requires an active radio connection.
- The DAX audio bridge must be running. If it is not, enable it via `Settings > Autostart DAX with AetherSDR` and restart AetherSDR, or start it manually.
- The VFO panel for the target slice must be open and expanded. If it is collapsed to the frequency-only strip, click anywhere on it to expand it.

## Steps

1. Click the VFO marker flag on the spectrum display for the slice you want to configure. The VFO panel opens, anchored to the left of the marker.
2. Click the **DAX** tab inside the VFO panel.
3. Click the **DAX channel combo** and select a channel from the drop-down list.
4. To disable DAX routing for this slice, select **Off**.

## What each control does

| Control                      | Default                                                                                                                               | Valid values                                                                                                            |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| DAX channel combo            | Off                                                                                                                                   | Off, 1–8                                                                                                                |
| ADSP button (DSP tab)        | Opens the AetherDSP Settings dialog (client-side NR2 / NR4 / DFNR / RN2 / BNR / MNR). Same entry point as the Settings menu (v0.9.8). | Styled like a radio-side DSP toggle but non-checkable. Click raises and focuses the modeless AetherDSP Settings dialog. |
| AetherVoice button (DSP tab) | Opens the Aetherial Audio Channel Strip — the unified TX/RX DSP suite (v0.9.8).                                                       | Spans 2 columns in the 4-column DSP grid. Matches the existing menu / chain entry points for the strip.                 |

The DAX channel combo assigns a DAX audio channel to the current slice. Selecting a numbered channel routes the slice's received audio to that DAX channel. Selecting **Off** removes the assignment. This setting reflects live radio state and is not persisted locally by AetherSDR.

## Squelch behavior by mode

The squelch button and slider are automatically disabled in modes where squelch is not meaningful or supported. Starting in v26.5.1:

- **Squelch is disabled** in **Digital**, **RTTY**, and **CW** modes.
  - **Digital / RTTY**: Audio feeds external decoders via DAX; squelch is not meaningful and can gate weak FSK signals (issue #2504).
  - **CW**: The radio locks squelch on at a fixed level and rejects changes.
- If squelch was enabled when switching into one of these modes, the radio turns it off automatically. The saved squelch state is preserved and will be restored if you switch back to a supported mode.

## DSP tab controls

The DSP tab in the VFO panel contains radio-supplied noise reduction buttons and two client-side launcher buttons.

### Radio-side DSP buttons

The following radio-side DSP buttons appear in the DSP tab grid:

| Button | Algorithm |
|---|---|
| NR | Noise reduction |
| NB | Noise blanker |
| ANF | Automatic notch filter |
| APF | Audio peaking filter (CW mode only) |
| NRL | Noise reduction level |
| NRS | Spectral subtraction |
| RNN | RNN noise reduction |
| NRF | Spectral noise filter |
| ANFL | LMS notch filter |
| ANFT | FFT notch filter |

### Client-side launcher buttons

Two client-side launcher buttons appear at the end of the DSP grid:

| Button | Behavior |
|---|---|
| **ADSP** | Opens the AetherDSP Settings dialog (client-side NR2 / NR4 / DFNR / RN2 / BNR / MNR). Styled like a radio-side DSP toggle but non-checkable. Click raises and focuses the modeless AetherDSP Settings dialog. |
| **AetherVoice** | Toggles the Aetherial Audio Channel Strip — the unified TX/RX DSP suite. Spans 2 columns in the 4-column DSP grid. Matches the existing menu / chain entry points for the strip. |

### Client-side noise reduction toggles

The following client-side noise reduction buttons appear in the DSP tab when enabled by the radio series and build:

| Button | Algorithm |
|---|---|
| NR2 | Client-side noise reduction algorithm 2 |
| NR4 | Client-side noise reduction algorithm 4 |
| RN2 | Client-side noise reduction algorithm RN2 |
| MNR | Client-side noise reduction algorithm MNR |
| DFNR | Client-side noise reduction algorithm DFNR |
| BNR | Client-side noise reduction algorithm BNR |
| NRL | Noise reduction level |
| NRS | Spectral subtraction |
| RNN | RNN noise reduction |
| NRF | Spectral noise filter |

Right-click NR2, NR4, MNR, or DFNR to open the AetherDSP Settings dialog for that algorithm.

### DSP level slider

A shared level slider row appears below the button grid. The slider adjusts the strength of whichever leveled DSP button was most recently turned on. The label to the left of the slider shows the active target (for example, **NR** or **NB**). The numeric value is shown to the right.

The slider range is 0–100. When no leveled DSP is active — or when only RNN, ANFT, or APF is on — the slider row is dimmed and does not respond to input. The row remains in place at all times; it does not shift the button grid when its target changes.

Algorithms that support the level slider: NR, NB, ANF, NRL, NRS, NRF, ANFL.

Starting in v0.9.8, when a leveled DSP algorithm is enabled from the radio's saved profile on startup, the level slider is automatically populated without requiring a manual toggle.

### Filter width label

The filter width label shows the current filter bandwidth. Click to cycle through filter preset buttons in the Mode tab. Starting in v0.9.8, this label uses `RxApplet::formatFilterWidth` as the single source of truth, fixing a 0.1 kHz offset that affected SSB/digital mode readouts.

### RX and TX antenna menus

The **RX antenna button** opens a menu to select the receive antenna for this slice. The **TX antenna button** opens a menu to select the transmit antenna. Starting in v26.5.2, these menus use the slice's radio-provided antenna list when available, falling back to the global antenna list. TX antenna options automatically exclude RX-only antenna ports. Each menu item shows its raw antenna name as a tooltip.

### Marker controls

The **Marker thickness button** cycles the VFO marker line through Off, 1 px, and 3 px. The setting is persisted per slice as `Slice{N}_MarkerWidth`.

The **Filter edges button** toggles the filter edge lines on the spectrum passband. The setting is persisted per slice as `Slice{N}_FilterEdgesHidden`.

### Collapse toggle

The **Collapse toggle** collapses the VFO panel to a compact frequency-only strip. The setting is persisted per slice as `SliceFlagCollapsed_{N}`.

### Slice badge

The slice badge shows the slice letter. Starting in v26.5.2, the badge supports rich text formatting, allowing special characters (issue #2606).

### Frequency entry

Click the frequency display to begin direct frequency entry. Type the frequency in MHz and press Enter or Tab. Starting in v26.5.2, on XVTR bands the frequency range is extended to 50000.0 MHz. For 2m/70cm bands (100-999 MHz range), a bare integer like 1446 is automatically interpreted as 144.6 MHz by inserting a decimal after the third digit. For 23cm and microwave bands, a bare integer represents MHz directly.

Starting in v26.5.3, frequency entry parsing is improved with context-aware handling. When you explicitly enter a frequency above 54 MHz (e.g., typing "144.225"), the parser correctly treats it as MHz even without an XVTR slice, allowing direct VHF/UHF entry. The `FrequencyEntryParser::normalizedMhzText` function normalizes input formats like "14.225.000" by removing extra dots. The `FrequencyEntryParser::isExplicitMhzEntry` function detects when you have typed a MHz value explicitly. On XVTR bands, the 3-digit band convenience (bare integer like 1446 = 144.6 MHz) continues to work.

If you attempt a direct frequency entry while the VFO is locked, the entry is cancelled and the LOCKED overlay is shown instead of accepting the new frequency (issue #2983). The frequency display also indicates when tune is blocked by lock. Scroll-wheel tuning on a locked VFO triggers the same feedback — the slice model notifies `tuneBlockedByLock`, which cancels any in-progress frequency entry and repaints the LOCKED indicator.

### Frequency entry improvements (v26.6.3)

Starting in v26.6.3, the frequency entry field uses a custom `FreqLineEdit` widget with improved placeholder text. The hint text reads "MHz (e.g. 14.225)" — note that this is the actual widget hint text, not a placeholder. The frequency display also provides accessibility announcements when the frequency changes, ensuring screen reader compatibility.

### VFO lock behavior

The **Lock VFO button** toggles the locked state of the VFO. When locked:
- Scroll-wheel tuning is blocked — the slice model shows feedback via `tuneBlockedByLock`.
- Direct frequency entry is cancelled when attempting to begin or during an active entry.
- The frequency display shows a LOCKED overlay (🔒 symbol) instead of the frequency value during direct entry attempts.

Unlocking clears the LOCKED overlay centrally in the SliceModel (issue #2983).

### Tab layout improvement

Starting in v26.5.3, the VFO panel tab stack uses a custom `TabStack` widget that reports only the current tab's preferred size. This fixes a visual gap inside the Mode tab when the DSP tab is taller (due to the digContainer being visible in DIGU/DIGL modes). The tab content no longer over-allocates height from the maximum of all pages.

### Tab navigation improvements (v26.6.3)

Starting in v26.6.3, the VFO panel tabs are implemented as `QPushButton` widgets instead of `QLabel` widgets. This change provides proper keyboard focus support:

- Each tab button is focusable via the Tab key (`Qt::TabFocus` policy).
- Focused tabs show a subtle bottom border outline using the tab label colour.
- **Right-click on the speaker tab (first tab)** toggles the audio mute state directly — a convenient shortcut to mute the slice without opening the Audio tab.

The tab buttons use flat, checkable style with the same visual appearance as before. The active tab is styled with the accent colour (#00b4d8) and a bottom border.

### VFO lock behaviour with scroll wheel (v26.6.3)

Starting in v26.6.3, the scroll wheel direction in the VFO panel respects the **Reverse mouse wheel** setting. If you have enabled reverse mouse wheel in `Settings > Audio/Radio > Tuning`, scrolling the VFO panel wheel will tune in the opposite direction. This setting is checked via the `InteractionSettings` model and applied to all VFO panel wheel events.

### Scroll wheel accessibility (v26.6.3)

Starting in v26.6.3, the scroll wheel behaviour is fully integrated with the `InteractionSettings` configuration. If you reverse the mouse wheel in settings, the VFO panel scroll direction reverses accordingly. This applies to all wheel events on the VFO panel, including the frequency display area and the RIT/XIT offset labels.

### Accessibility improvements (v26.6.3)

Starting in v26.6.3, the VFO panel provides accessibility announcements for frequency changes. When the frequency changes while an accessibility client (screen reader) is active, an `QAccessibleValueChangeEvent` is posted for the frequency label widget. This ensures screen readers announce the new frequency value. The accessibility timer is single-shot and fires after a brief delay to avoid flooding the accessibility layer during rapid tuning.

### Slider theming (v26.6.1)

Starting in v26.6.1, the VFO panel uses themed slider styling throughout. The Pan slider is painted with centre-anchored fill: the groove section from the handle to the midpoint is filled with the accent colour, while the opposite side uses the background colour. This makes the centre (neutral) position immediately visible. The slider handle is drawn by the default Qt style.

All other sliders (AF Gain, squelch threshold, DSP level) follow the same theming rules. The style is driven by the active colour theme rather than hard-coded colours.

### VFO panel theming (v26.6.1)

Starting in v26.6.1, the VFO panel uses a dedicated theming container scope `spectrum/vfo`. This ensures that inspector clicks on the VFO panel surface (including the frequency badge, callsign badge, and signal meter) resolve to VFO-specific theme tokens rather than falling back to the spectrum scope. The VFO panel declares the following theme tokens for inspector coverage:

- `color.background.0`
- `color.background.1`
- `color.background.2`
- `color.text.primary`
- `color.text.label`
- `color.accent`
- `color.accent.bright`

These tokens are painted directly via `QPainter` calls and are surfaced correctly in inspect mode.

### SPLIT badge appearance (v26.6.3)

Starting in v26.