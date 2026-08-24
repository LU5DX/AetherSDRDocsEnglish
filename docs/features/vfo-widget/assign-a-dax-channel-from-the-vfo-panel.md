# VFO Panel Reference

The VFO panel is a floating per-slice control panel anchored to the VFO marker on the spectrum display. It provides quick access to the most frequently used per-slice settings — mode, filter presets, antenna selection, AF gain, pan, squelch, AGC, RIT/XIT, DSP noise reduction buttons, and DAX assignment — without leaving the spectrum view. Collapses to a compact frequency-only strip.

## Before you start

- AetherSDR must be connected to the radio. The VFO panel requires an active radio connection.
- The DAX audio bridge must be running. If it is not, enable it via `Settings > Autostart DAX with AetherSDR` and restart AetherSDR, or start it manually.
- The VFO panel for the target slice must be open and expanded. If it is collapsed to the frequency-only strip, click anywhere on it to expand it.

## Opening the VFO panel

Click the VFO marker flag on the spectrum display for the slice you want to configure. The VFO panel opens, anchored to the left of the marker.

## VFO panel controls

| Control | Location | Default | Valid values | Behavior |
|---|---|---|---|---|
| RX antenna button | Header | — | — | Opens antenna selection menu for the receive antenna of this slice. |
| TX antenna button | Header | — | — | Opens antenna selection menu for the transmit antenna of this slice. |
| Frequency display | Header | — | — | Shows the current slice frequency. Click once to begin direct frequency entry; type MHz and press Enter or Tab. |
| Filter width label | Header | — | — | Shows current filter bandwidth. Click to cycle through filter preset buttons in the Mode tab. Uses `RxApplet::formatFilterWidth` as the single source of truth, fixing a 0.1 kHz offset that affected SSB/digital mode readouts (#2197, v0.9.8). |
| Collapse toggle | Header | expanded | — | Collapses the VFO panel to a compact frequency-only strip. Persisted per slice as `SliceFlagCollapsed_{N}`. Right-click → Add Spot works in collapsed mode too. |
| Marker thickness button | Header | 1 px | Off, 1 px, 3 px | Cycles the VFO marker line through Off, 1 px, and 3 px. Persisted per slice as `Slice{N}_MarkerWidth`. |
| Filter edges button | Header | shown | — | Toggles the filter edge lines on the spectrum passband. Persisted per slice as `Slice{N}_FilterEdgesHidden`. |
| AF Gain slider | Audio tab | 100 | 0–100 | Sets the audio output level for this slice. Not persisted — reflects live radio state. |
| Pan slider | Audio tab | 50 | 0–100 | Sets left/right stereo pan for this slice. 50 = centre. |
| Mute button | Audio tab | off | — | Mutes audio output for this slice without changing the AF gain setting. |
| Squelch button + slider | Audio tab | off | 0–100 | Enables squelch for this slice. The adjacent slider sets the threshold. |
| AGC combo | Audio tab | FAST | FAST, MED, SLOW, OFF | Sets the AGC attack/release speed for this slice. |
| Mode combo | Mode tab | USB | USB, LSB, CW, CWL, AM, SAM, DIGU, DIGL, FM, NFM, DFM, RTTY | Sets the demodulation mode for this slice. |
| Filter preset buttons | Mode tab | — | — | Applies a saved filter width preset. Right-click to save the current filter width into that slot. Persisted in `FilterPresets`. Custom lo/hi edges can be set per slot via right-click. |
| RIT / XIT buttons + labels | X/RIT tab | off | — | Enables receiver (RIT) or transmitter (XIT) incremental tuning. The label shows the current offset; scroll-wheel adjusts in 10 Hz steps. |
| DAX channel combo | DAX tab | Off | Off, 1–8 | Assigns a DAX audio channel to this slice. |
| DSP buttons | DSP tab | off | — | Enables the corresponding noise reduction algorithm for this slice. Button availability depends on radio series and build. Right-click NR2, NR4, MNR, or DFNR to open the AetherDSP Settings dialog for that algorithm. |
| ADSP button | DSP tab | — | — | Opens the AetherDSP Settings dialog (client-side NR2 / NR4 / DFNR / RN2 / BNR / MNR). Same entry point as the Settings menu (v0.9.8). Styled like a radio-side DSP toggle but non-checkable. Click raises and focuses the modeless AetherDSP Settings dialog. |
| AetherVoice button | DSP tab | — | — | Toggles the Aetherial Audio Channel Strip — the unified TX/RX DSP suite (v0.9.8). Spans 2 columns in the 4-column DSP grid. |

## Indicators

| Indicator | States | Meaning |
|---|---|---|
| TX badge | TX (red), hidden | Shown when this slice is the active transmit slice. |
| SPLIT badge | SPLIT (amber), hidden | Shown when TX is assigned to a different slice than the active receive slice. |

## Assigning a DAX channel

1. Click the **DAX** tab inside the VFO panel.
2. Click the **DAX channel combo** and select a channel from the drop-down list.
3. To disable DAX routing for this slice, select **Off**.

The DAX channel combo assigns a DAX audio channel to the current slice. Selecting a numbered channel routes the slice's received audio to that DAX channel. Selecting **Off** removes the assignment. This setting reflects live radio state and is not persisted locally by AetherSDR.

## Squelch behavior by mode

The squelch button and slider are automatically disabled in modes where squelch is not meaningful or supported:

- **Squelch is disabled** in **Digital**, **RTTY**, and **CW** modes.
  - **Digital / RTTY**: Audio feeds external decoders via DAX; squelch is not meaningful and can gate weak FSK signals.
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
| MN | Manual notch filter (only shown on radios that support it) |

### Client-side launcher buttons

Two client-side launcher buttons appear at the end of the DSP grid:

| Button | Behavior |
|---|---|
| **ADSP** | Opens the AetherDSP Settings dialog (client-side NR2 / NR4 / DFNR / RN2 / BNR / MNR). Same entry point as the Settings menu (v0.9.8). Styled like a radio-side DSP toggle but non-checkable. Click raises and focuses the modeless AetherDSP Settings dialog. |
| **AetherVoice** | Toggles the Aetherial Audio Channel Strip — the unified TX/RX DSP suite (v0.9.8). Spans 2 columns in the 4-column DSP grid. |

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

Algorithms that support the level slider: NR, NB, ANF, NRL, NRS, NRF, ANFL, MN.

When a leveled DSP algorithm is enabled from the radio's saved profile on startup, the level slider is automatically populated without requiring a manual toggle.

## Filter width label

The filter width label shows the current filter bandwidth. Click to cycle through filter preset buttons in the Mode tab. The label uses `RxApplet::formatFilterWidth` as the single source of truth, fixing a 0.1 kHz offset that affected SSB/digital mode readouts (#2197, v0.9.8).

## RX and TX antenna menus

The **RX antenna button** opens a menu to select the receive antenna for this slice. The **TX antenna button** opens a menu to select the transmit antenna. These menus use the slice's radio-provided antenna list when available, falling back to the global antenna list. TX antenna options automatically exclude RX-only antenna ports. Each menu item shows its raw antenna name as a tooltip.

## Marker controls

The **Marker thickness button** cycles the VFO marker line through Off, 1 px, and 3 px. The setting is persisted per slice as `Slice{N}_MarkerWidth`.

The **Filter edges button** toggles the filter edge lines on the spectrum passband. The setting is persisted per slice as `Slice{N}_FilterEdgesHidden`.

## Collapse toggle

The **Collapse toggle** collapses the VFO panel to a compact frequency-only strip. The setting is persisted per slice as `SliceFlagCollapsed_{N}`.

Right-click → Add Spot works in collapsed mode too. The collapsed frequency label installs an event filter to ensure clicks are handled by the VFO panel, not the spectrum widget underneath, so the cursor's step-snapped frequency is never reported instead of the VFO's (#4455).

## Slice badge

The slice badge shows the slice letter. The badge supports rich text formatting, allowing special characters.

## Frequency entry

Click the frequency display to begin direct frequency entry. Type the frequency in MHz and press Enter or Tab.

- On XVTR bands, the frequency range is extended to 50000.0 MHz.
- For 2m/70cm bands (100-999 MHz range), a bare integer like 1446 is automatically interpreted as 144.6 MHz by inserting a decimal after the third digit.
- For 23cm and microwave bands, a bare integer represents MHz directly.
- When you explicitly enter a frequency above 54 MHz (e.g., typing "144.225"), the parser correctly treats it as MHz even without an XVTR slice, allowing direct VHF/UHF entry.

If you attempt a direct frequency entry while the VFO is locked, the entry is cancelled and the LOCKED overlay is shown instead of accepting the new frequency. Scroll-wheel tuning on a locked VFO triggers the same feedback — the slice model notifies `tuneBlockedByLock`, which cancels any in-progress frequency entry and repaints the LOCKED indicator.

The frequency entry field uses a custom `FreqLineEdit` widget. The hint text reads "MHz (e.g. 14.225)". The frequency display also provides accessibility announcements when the frequency changes, ensuring screen reader compatibility.

## VFO lock behavior

The **Lock VFO button** toggles the locked state of the VFO. When locked:
- Scroll-wheel tuning is blocked — the slice model shows feedback via `tuneBlockedByLock`.
- Direct frequency entry is cancelled when attempting to begin or during an active entry.
- The frequency display shows a LOCKED overlay (🔒 symbol) instead of the frequency value during direct entry attempts.

Unlocking clears the LOCKED overlay centrally in the SliceModel.

## Tab layout

The VFO panel tab stack reports only the current tab's preferred size. This fixes a visual gap inside the Mode tab when the DSP tab is taller (due to the digContainer being visible in DIGU/DIGL modes). The tab content no longer over-allocates height from the maximum of all pages.

### Tab navigation

The VFO panel tabs are implemented as `QPushButton` widgets instead of `QLabel` widgets. This change provides proper keyboard focus support:

- Each tab button is focusable via the Tab key (`Qt::TabFocus` policy).
- Focused tabs show a subtle bottom border outline using the tab label colour.
- **Right-click on the speaker tab (first tab)** toggles the audio mute state directly — a convenient shortcut to mute the slice without opening the Audio tab.

The tab buttons use flat, checkable style with the same