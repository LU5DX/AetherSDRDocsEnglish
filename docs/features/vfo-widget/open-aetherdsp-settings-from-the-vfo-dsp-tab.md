# VFO Panel

The VFO Panel is a floating per-slice control panel anchored to the VFO marker on the spectrum display. It provides quick access to the most frequently used per-slice settings — mode, filter presets, antenna selection, AF gain, pan, squelch, AGC, RIT/XIT, DSP noise reduction buttons, and DAX assignment — without leaving the spectrum view. The panel can collapse to a compact frequency-only strip.

## Opening the VFO Panel

1. On the spectrum display, click the VFO marker flag (the small triangle or flag at the top of the VFO marker line).
2. The VFO Panel opens as a floating window anchored to the marker.

## Controls

The VFO Panel is organized into tabs: Audio, DSP, Mode, X/RIT, and DAX. Tab labels are now rendered as `QPushButton` for keyboard accessibility and consistent focus styling. Right-click the **Audio** tab label to toggle mute directly.

### Common Controls (always visible)

| Control | Type | Description |
|---------|------|-------------|
| RX antenna button | Push button | Opens antenna selection menu for the receive antenna of this slice. Shows the slice-specific RX antenna list when available; falls back to the radio's antenna list otherwise. |
| TX antenna button | Push button | Opens antenna selection menu for the transmit antenna of this slice. Filters out RX-only antenna ports. Shows the slice-specific TX antenna list when available; falls back to the radio's antenna list otherwise. |
| Frequency display | Indicator | Shows the current slice frequency. Click once to begin direct frequency entry; type MHz and press Enter or Tab. When the slice is locked, displays a "LOCKED" overlay and prevents direct frequency entry. On XVTR bands, bare integer entry in the 100-999 MHz range inserts a decimal after the third digit (e.g., 1446 → 144.6). Accessibility: the frequency text is announced via `QAccessibleValueChangeEvent` when it changes. |
| Filter width label | Indicator | Shows current filter bandwidth. Click to cycle through filter preset buttons in the Mode tab. Uses `RxApplet::formatFilterWidth` as the single source of truth, fixing a 0.1 kHz offset that affected SSB/digital mode readouts. |
| TX badge | Indicator | Shown (red) when this slice is the active transmit slice. Hidden otherwise. |
| SPLIT badge | Indicator | Shown (amber) when TX is assigned to a different slice than the active receive slice. Hidden otherwise. The badge text can be "SWAP" to indicate split operation; clicking performs a swap. Badge opacity has been increased for better visibility. |
| Marker thickness button | Push button | Cycles the VFO marker line through Off, 1 px, and 3 px. Setting is persisted per slice (`Slice{N}_MarkerWidth`). |
| Filter edges button | Toggle button | Toggles the filter edge lines on the spectrum passband. Setting is persisted per slice (`Slice{N}_FilterEdgesHidden`). Default: shown. |
| Collapse toggle | Toggle button | Collapses the VFO panel to a compact frequency-only strip. Setting is persisted per slice (`SliceFlagCollapsed_{N}`). Default: expanded. |
| Slice badge | Indicator | Shows the slice letter in a colored badge. Click to open the slice context menu. |

### Audio Tab

| Control | Type | Range | Description |
|---------|------|-------|-------------|
| AF Gain slider | Slider | 0-100 | Sets the audio output level for this slice. Default: 100. Not persisted — reflects live radio state. |
| Pan slider | Slider | 0-100 | Sets left/right stereo pan for this slice. 50 = centre. Default: 50. The slider fill anchors from the centre outward, with a centre-mark dot visible on the groove. |
| Mute button | Toggle button | On/Off | Mutes audio output for this slice without changing the AF gain setting. Default: off. Also accessible via right-click on the Audio tab label. |
| Squelch button + slider | Toggle button + slider | 0-100 | Enables squelch for this slice. The adjacent slider sets the threshold. Default: off. Squelch is automatically disabled in digital, RTTY, and CW modes. |
| AGC combo | Combo box | FAST, MED, SLOW, OFF | Sets the AGC attack/release speed for this slice. Default: FAST. |

### DSP Tab

| Control | Type | Description |
|---------|------|-------------|
| NR / NR2 / RN2 / NR4 / MNR / DFNR / BNR / NRL / NRS / RNN / NRF buttons | Toggle button | Enables the corresponding noise reduction algorithm for this slice. Button availability depends on radio series and build. Default: off. Right-click NR2, NR4, MNR, or DFNR to open the AetherDSP Settings dialog for that algorithm. |
| MN button | Toggle button | Enables the manual notch filter for this slice. Only shown on radios that support manual notch filtering. Default: off. Hidden otherwise. |
| ADSP button | Push button | Opens the AetherDSP Settings dialog (client-side NR2 / NR4 / DFNR / RN2 / BNR / MNR). Same entry point as the Settings menu. Click raises and focuses the modeless AetherDSP Settings dialog. Non-checkable; styled like a radio-side DSP toggle. |
| AetherVoice button | Push button | Toggles the Aetherial Audio Channel Strip — the unified TX/RX DSP suite. Spans 2 columns in the 4-column DSP grid. |

### Mode Tab

| Control | Type | Range | Description |
|---------|------|-------|-------------|
| Mode combo | Combo box | USB, LSB, CW, CWL, AM, SAM, DIGU, DIGL, FM, NFM, DFM, RTTY | Sets the demodulation mode for this slice. Default: USB. |
| Filter preset buttons | Push button | N/A | Applies a saved filter width preset. Right-click to save the current filter width into that slot. Persisted in `FilterPresets`. Custom lo/hi edges can be set per slot via right-click. |

### X/RIT Tab

| Control | Type | Description |
|---------|------|-------------|
| RIT button + label | Toggle button + indicator | Enables receiver incremental tuning. The label shows the current offset; scroll-wheel adjusts in 10 Hz steps. Default: off. |
| XIT button + label | Toggle button + indicator | Enables transmitter incremental tuning. The label shows the current offset; scroll-wheel adjusts in 10 Hz steps. Default: off. |

### DAX Tab

| Control | Type | Range | Description |
|---------|------|-------|-------------|
| DAX channel combo | Combo box | Off, 1-8 | Assigns a DAX audio channel to this slice. Default: Off. |

## Frequency Entry Behavior

### Direct Frequency Entry

1. Click the frequency display once. The display switches to an editable field showing the current frequency.
2. Type the desired frequency and press Enter or Tab to apply it. The system parses input flexibly:
   - **MHz entry**: Type a value in MHz (e.g., "14.225", "14.225.000", "14225", "14225.0"). Dots beyond the first are automatically removed.
   - **kHz entry**: On HF bands, bare integers greater than 54000 are treated as Hz; otherwise they are treated as kHz. For example, "14225" becomes 14.225 MHz (kHz interpretation), while "14225000" becomes 14.225 MHz (Hz interpretation).
   - **XVTR band entry**: On XVTR bands, values above 54 MHz are accepted. A bare integer in the 100-999 range inserts a decimal after the third digit (e.g., "1446" → 144.6 MHz).

The frequency edit field now uses `FreqLineEdit` with hint text "MHz (e.g. 14.225)" instead of placeholder text.

### Explicit MHz Entry

When you explicitly type a value with a decimal and it exceeds 54 MHz, the system treats it as a MHz value rather than attempting Hz/kHz conversion. This allows direct entry of VHF/UHF/SHF frequencies in MHz without ambiguity.

### Locked Slice Behavior

When a slice is frequency-locked:
- The frequency display shows a "LOCKED" overlay.
- Clicking the frequency display does not initiate direct entry.
- Scroll-wheel tuning is blocked, even in collapsed mode.
- An audible notification indicates the tuning attempt was blocked.

## Mouse Wheel Behavior

The mouse wheel tuning direction respects the **Reverse mouse wheel** setting in the Interaction settings. When enabled, the tuning direction is reversed, and zoom direction in the panadapter is also reversed. The setting `reverseMouseWheel()` is checked in the VFO widget's `wheelEvent`.

## Squelch Behavior

Squelch is automatically disabled in digital, RTTY, and CW modes:
- **Digital and RTTY**: Audio feeds external decoders via DAX; squelch is not meaningful and can gate weak FSK signals.
- **CW**: The radio locks squelch on at a fixed level and rejects changes from the client.

When switching to a mode where squelch is disabled while squelch is active, the system saves the squelch state and turns it off. When switching back to a mode where squelch is allowed, the previous squelch state is restored.

The squelch control has been split into explicit methods — `setManualSquelch()` for manual control and separate handling for auto squelch modes — clarifying the distinction between user-set thresholds and radio-managed auto squelch.

## Pan Slider Behavior

The Pan slider in the Audio tab uses centre-anchored fill painting. When the handle is left of centre, the groove is filled from the handle to centre in accent colour; when the handle is at or right of centre, the fill is not shown. A small centre-mark dot is always visible on the groove so you can see the neutral position at a glance.

## VFO Flag Elevation Shadow

The VFO flag now has a lightweight elevation shadow rendered by a dedicated `FlagShadow` widget. The shadow is kept separate from the VFO Panel so that live meter repaints (e.g., S-meter updates) do not re-blur the entire flag at animation rate. The shadow widget:
- Uses `WA_TransparentForMouseEvents` so it does not intercept clicks.
- Uses a fast box-blur algorithm with high-performance lookups.
- Automatically adapts to device pixel ratio (DPR) for sharp rendering on high-DPI displays.
- Rebuilds the shadow image only when the flag geometry or DPR changes, preventing unnecessary CPU usage.

## Open AetherDSP Settings from the VFO DSP tab

Open the AetherDSP Settings dialog from the VFO Panel's DSP tab to adjust advanced noise reduction parameters for NR2, NR4, DFNR, or MNR algorithms.

### Before you start

- A slice must be active and connected to a radio.
- The VFO Panel must be open for the slice you want to configure (click the VFO marker flag on the spectrum display).

### Steps

1. In the VFO Panel, click the **DSP** tab label to show the noise reduction controls.
2. Click the **ADSP** button.  
   The AetherDSP Settings dialog opens as a modeless window; it can stay open while you continue operating the radio.

Alternatively, you can right-click any of the NR2, NR4, MNR, or DFNR toggle buttons in the DSP tab to open the AetherDSP Settings dialog for that specific algorithm.

### Tips

- The AetherDSP Settings dialog can also be opened from `Settings > AetherDSP Settings...` in the main menu.
- Right-clicking a noise reduction button (NR2, NR4, MNR, or DFNR) opens the dialog focused on that algorithm's controls.

### Related

- [Enable noise reduction from the VFO panel](enable-noise-reduction-from-the-vfo-panel.md)
- Frequency locking

## DSP Button Accessibility

The DSP tab noise reduction buttons now use stable object names (e.g., `dspNR2Btn`, `dspDFNRBtn`) for automation and scripting. These names are separate from accessible names used by screen readers and are guaranteed not to change with UI text rewording. This ensures automation scripts can reliably address the DSP toggles.

## Collapsed Mode Right-Click

When the VFO Panel is collapsed to the compact frequency-only strip, right-clicking the frequency label opens the slice context menu using the VFO's actual frequency rather than the step-snapped cursor frequency. This ensures spot reports and other frequency-dependent actions use the correct tuned frequency.