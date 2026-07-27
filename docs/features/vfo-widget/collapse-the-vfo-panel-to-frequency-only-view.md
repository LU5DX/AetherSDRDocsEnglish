# Collapse the VFO panel to frequency-only view

When screen space is limited, you can collapse the VFO panel to a compact strip that shows only the slice frequency. The collapsed state is saved per slice so it persists across sessions.

## Before you start

- AetherSDR must be connected to the radio. The VFO panel requires a live radio connection.
- The VFO panel for the slice must be open. If it is not visible, click the VFO marker flag on the spectrum display for that slice.

## Steps

1. Locate the slice badge in the header area of the VFO panel. The badge shows the slice identifier (for example, **A** or **B**).
2. Click the slice badge. The panel collapses to a compact frequency-only strip.
3. To restore the full panel, click anywhere on the collapsed strip.

## What each control does

| Control | Default | Persisted setting |
|---|---|---|
| Collapse toggle | Expanded | `SliceFlagCollapsed_{N}` |
| RX antenna button | Opens antenna selection menu for the receive antenna of this slice. Uses the slice's `rxAntennaList` when available; otherwise falls back to the radio antenna list. | None |
| TX antenna button | Opens antenna selection menu for the transmit antenna of this slice. Filters out RX-only antenna ports. Uses the slice's `txAntennaList` when available. | None |
| Frequency display | Shows the current slice frequency. Click once to begin direct frequency entry; type MHz and press Enter or Tab. | None |
| Filter width label | Shows current filter bandwidth. Click to cycle through filter preset buttons in the Mode tab. Uses `RxApplet::formatFilterWidth` as the single source of truth, fixing a 0.1 kHz offset that affected SSB/digital mode readouts (#2197, v0.9.8). | None |
| Slice badge | Shows the slice letter. Click to collapse the panel. Displays HTML-formatted text (#2606). | None |
| AF Gain slider (Audio tab) | 100 | None — reflects live radio state. |
| Pan slider (Audio tab) | 50 | None |
| Mute button (Audio tab) | Off | None |
| Squelch button + slider (Audio tab) | Off | None |
| AGC combo (Audio tab) | FAST | None |
| NR / NR2 / RN2 / NR4 / MNR / DFNR / BNR / NRL / NRS / RNN / NRF buttons (DSP tab) | Off | None |
| ADSP button (DSP tab) | Opens the AetherDSP Settings dialog (client-side NR2 / NR4 / DFNR / RN2 / BNR / MNR). Same entry point as the Settings menu (v0.9.8). | Styled like a radio-side DSP toggle but non-checkable. Click raises and focuses the modeless AetherDSP Settings dialog. |
| AetherVoice button (DSP tab) | Toggles the Aetherial Audio Channel Strip — the unified TX/RX DSP suite (v0.9.8). | Spans 2 columns in the 4-column DSP grid. Matches the existing menu / chain entry points for the strip. |
| Mode combo (Mode tab) | USB | None |
| Filter preset buttons (Mode tab) | Applies a saved filter width preset. Right-click to save the current filter width into that slot. | `FilterPresets` |
| RIT / XIT buttons + labels (X/RIT tab) | Off | None |
| DAX channel combo (DAX tab) | Off | None |
| Marker thickness button | 1 px | `Slice{N}_MarkerWidth` |
| Filter edges button | Shown | `Slice{N}_FilterEdgesHidden` |

The `SliceFlagCollapsed_{N}` setting is stored per slice, where `{N}` is the slice number. Collapsing one slice does not affect other slices.

## DSP tab changes in v0.9.7

The DSP tab in the VFO panel now shows only the noise reduction and filtering algorithms supplied directly by the radio. The following buttons have been removed from the DSP tab grid:

- **NR2** (spectral noise reduction)
- **RN2** (RNNoise noise suppression)
- **BNR** (GPU neural denoising)
- **NR4** (spectral bleach noise reduction)
- **MNR** (macOS MMSE-Wiener noise reduction)
- **DFNR** (DeepFilterNet3 neural noise reduction)

These client-side processing algorithms are still available. Access them through the spectrum overlay menu or the AetherDSP applet.

The buttons that remain in the DSP tab grid are now arranged in a four-column layout with all client-side DSP buttons present:

| Position | Button |
|---|---|
| Row 0, Col 0 | NR / NR2 / RN2 / NR4 / MNR / DFNR / BNR |
| Row 0, Col 1 | NRL |
| Row 0, Col 2 | NRS |
| Row 0, Col 3 | RNN |
| Row 1, Col 0 | NRF |
| Row 1, Cols 1-3 | (empty) |
| Row 2, Col 0 | ADSP |
| Row 2, Cols 1-2 | AetherVoice (spans 2 columns) |

Note: The NR button entry in the grid now represents a group of noise reduction buttons (NR, NR2, RN2, NR4, MNR, DFNR, BNR). The specific buttons shown depend on radio series and build configuration. Right-click NR2, NR4, MNR, or DFNR to open the AetherDSP Settings dialog for that algorithm.

### DSP level slider

A shared level slider row appears below the DSP button grid. The slider targets whichever leveled DSP algorithm was most recently enabled. The label to the left of the slider shows the name of the current target (for example, **NR** or **NB**), and the numeric value is shown to the right.

| Control | Range | Behavior |
|---|---|---|
| DSP level slider | 0–100 | Sets the level for the active DSP algorithm. Retargets automatically when you enable a different algorithm. |

The slider row remains in the layout at all times. When no compatible algorithm is active — or when only RNN, ANFT, or APF is on — the slider row fades out and does not respond to input. Enabling a supported algorithm fades the row back in and retargets the slider to that algorithm.

Algorithms that the level slider can target: NR, NB, ANF, NRL, NRS, NRF, ANFL.

The level slider now properly reflects the radio state on initial connection. When a leveled DSP algorithm is already active in the radio's saved profile, the slider appears immediately rather than requiring a manual toggle (#startup-slider, v0.9.8).

### Squelch behavior in RTTY mode

As of v26.5.1, the squelch button and slider are disabled in RTTY mode. The radio squelch gates weak FSK signals, which interferes with external decoders that expect a continuous audio stream via DAX. If squelch was enabled when switching to RTTY mode, it is automatically turned off. The saved squelch state is restored when switching back to a voice mode.

## Frequency entry on XVTR bands

When entering a frequency on XVTR bands (100–999 MHz range), the VFO panel applies a convenience conversion: a bare integer entry like `1446` is interpreted as `144.6 MHz` by inserting a decimal after the third digit. This only applies when:
- The slice is tuned to an XVTR band (frequency above 54 MHz or using an antenna starting with `XVT`)
- The current frequency is in the 100–999 MHz range (three-digit band)
- The entered value is above 450 MHz and does not contain a decimal point

For frequencies on 23cm and microwave bands (above 1000 MHz), a bare integer is interpreted as MHz directly (e.g., `1296` means `1296 MHz`, not `129.6 MHz`).

The frequency entry accepts values up to 50000 MHz on XVTR bands.

### Explicit MHz entry recognition

As of v26.5.3, the frequency entry parser now explicitly recognizes values entered in MHz format. If you enter a frequency above 54 MHz using an explicit MHz notation (for example, `144.000` or `432.100`), the parser treats it as a direct MHz entry rather than attempting Hz or kHz conversion. This allows you to enter VHF/UHF frequencies directly without requiring an XVTR antenna or pre-existing frequency above 54 MHz.

The parser normalizes multiple dots (for example, `14.225.000` becomes `14.225000`) using `FrequencyEntryParser::normalizedMhzText()` before attempting to parse. The explicit MHz entry flag lets the parser skip Hz/kHz conversion logic for values above 54 MHz that were clearly entered as MHz.

## Scrolling behavior on locked slices

When a slice is VFO-locked, mouse wheel scrolling over the VFO panel does not change the frequency. Instead, the frequency display briefly shows a **LOCKED** overlay to indicate that tuning is blocked. This applies in both collapsed and expanded views. The notification is provided by `SliceModel::notifyTuneBlockedByLock()`.

## Tab stack height optimization

As of v26.5.3, the VFO panel uses a `TabStack` widget (a subclass of `QStackedWidget`) that reports only the current tab's preferred size. This prevents excessive vertical space when switching between tabs of different heights — for example, when the DSP tab is taller than the Mode tab due to the digital mode sub-container appearing in DIGU/DIGL modes. No visual behavior changes; the panel now uses space more efficiently.

## Theme support improvements in v26.6.1

The VFO panel now participates fully in the AetherSDR theme system. The panel is assigned a `spectrum/vfo` theme container scope so that inspector clicks on the VFO panel are correctly reported under the VFO scope rather than bubbling up to the spectrum display.

The following theme tokens are declared for the VFO panel:
- `color.background.0`
- `color.background.1`
- `color.background.2`
- `color.text.primary`
- `color.text.label`
- `color.accent`
- `color.accent.bright`

These tokens are used by raw `QPainter` calls for the signal meter, slice badge, and background rendering. When using the theme inspector, clicking on the VFO flag, callsign badge, or signal meter strip surfaces these tokens in the hit list.

### Center-mark slider appearance

The Pan slider in the Audio tab uses a `CenterMarkSlider` that paints a center-mark dot to indicate the neutral (50) position. As of v26.6.1, the slider fill is anchored from the centre outward — the left side of the groove is filled with background colour, and the right side from centre to handle is filled with the accent colour. This provides a visual indication of pan/balance offset from the midpoint. The centre dot is painted at the midpoint of the slider groove.

### Button theming

The VFO panel action buttons now use theme-aware stylesheets instead of hardcoded colours. The pressed state uses `{{color.accent}}` and the background uses `{{color.background.1}}`. This ensures consistent appearance across all themes.

## TX and SPLIT badges

| Indicator | States | Meaning |
|---|---|---|
| TX badge | TX (red) or hidden | Shown when this slice is the active transmit slice. |
| SPLIT badge | SPLIT (amber) or hidden | Shown when TX is assigned to a different slice than the active receive slice. |

## Tab bar improvements in v26.6.3

The VFO panel tab bar has been updated for accessibility and usability. The tab buttons are now `QPushButton` instances instead of `QLabel` elements, providing native keyboard focus support.

- Press **Tab** to navigate through the tab buttons. A focus indicator (blue bottom border) appears on the focused tab.
- **Enter** or **Space** activates the focused tab.
- The Audio tab now supports a right-click context menu. Right-click the **Speaker** tab to toggle mute for the current slice directly without switching tabs.

## Frequency display accessibility in v26.6.3

The VFO frequency display now uses a `FreqLineEdit` widget with accessibility support. When assistive technology is active, the frequency updates the accessibility tree to announce frequency changes. This ensures screen readers announce the current frequency value as it changes.

The frequency entry field uses `setHintText()` instead of `setPlaceholderText()` for the MHz entry hint.

## Mouse wheel tuning direction in v26.6.3

The VFO panel now respects the reverse mouse wheel setting from `InteractionSettings`. When reverse mouse wheel is enabled, scrolling the mouse wheel over the VFO panel tunes the frequency in the opposite direction. This applies to both collapsed and expanded views.

## Tip

- In collapsed view, scrolling the mouse wheel over the strip tunes the slice frequency by the current step size — the same as scrolling over the frequency display in the full panel.
- In collapsed view, clicking the TX badge painted on the strip toggles the TX assignment for that slice. Clicking anywhere else on the strip expands the panel.
- The panel flips to the right side of the VFO marker automatically if expanding it would be clipped by the window edge. This behavior applies in both expanded and collapsed states.
- To access NR2, RN2, BNR, NR4, MNR, or DFNR, right-click the spectrum display to open the overlay menu, or open the AetherDSP applet.
- Right-click the Speaker tab to toggle mute without switching tabs.

## Related

- [VFO Panel overview](overview.md)
- [Tune the radio by typing a frequency into the VFO panel](tune-the