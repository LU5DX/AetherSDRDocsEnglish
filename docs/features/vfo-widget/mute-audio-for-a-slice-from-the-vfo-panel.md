# Mute audio for a slice from the VFO panel

Silence the audio output of a single slice without changing its AF Gain setting. Use this when you want to suppress a slice temporarily and restore its previous volume with one click.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- The VFO panel for the target slice must be open. If it is collapsed to a frequency-only strip, click anywhere on it to expand it first.

## Steps

1. Click the VFO marker flag on the spectrum display for the slice you want to mute. The VFO panel opens anchored to the marker.
2. Click **Audio** to select the Audio tab inside the VFO panel. Alternatively, right-click the Audio tab button to toggle mute directly without opening the tab.
3. Click **Mute**. The button activates, and audio output for the slice stops. The AF Gain slider value is not changed.
4. To restore audio, click **Mute** again. The button deactivates and audio resumes at the previous AF Gain level.

## What each control does

| Control | Kind | Default | Behavior | Notes |
|---------|------|---------|----------|-------|
| RX antenna button | Push button | — | Opens antenna selection menu for the receive antenna of this slice. | |
| TX antenna button | Push button | — | Opens antenna selection menu for the transmit antenna of this slice. | |
| Frequency display | Indicator | — | Shows the current slice frequency. Click once to begin direct frequency entry; type MHz and press Enter or Tab. On XVTR bands, bare integer entry inserts a decimal after the third digit for 2m/70cm bands (100-999 MHz range). For 23cm and microwave bands, bare integers are treated as full MHz values. Frequency entries with explicit decimal points above 54 MHz are accepted as MHz values on any band. | Accessibility: the frequency label emits `QAccessibleValueChangeEvent` when the frequency changes via radio update, so screen readers can announce the new value. |
| Filter width label | Indicator | — | Shows current filter bandwidth. Click to cycle through filter preset buttons in the Mode tab. Uses `RxApplet::formatFilterWidth` as the single source of truth. | Fixes a 0.1 kHz offset that affected SSB/digital mode readouts (#2197, v0.9.8). |
| AF Gain slider (Audio tab) | Slider | 100 | Sets the audio output level for this slice. | Not persisted — reflects live radio state. |
| Pan slider (Audio tab) | Slider | 50 | Sets left/right stereo pan for this slice. 50 = centre. The slider fill anchors from the centre outward, with a small centre-mark dot painted on the groove to show the neutral position. | |
| Mute button (Audio tab) | Toggle button | Off | Mutes audio output for this slice without changing the AF gain setting. | Right-click the Audio tab label to toggle mute directly. |
| Squelch button + slider (Audio tab) | Toggle button | Off | Enables squelch for this slice. The adjacent slider sets the threshold. | Squelch is disabled in digital, RTTY, and CW modes. In digital and RTTY modes, audio feeds external decoders via DAX and squelch is not meaningful — it also gates weak FSK signals. In CW mode, the radio locks squelch on at a fixed level and rejects changes. Uses `setManualSquelch` API (v26.8.4). |
| AGC combo (Audio tab) | Combo box | FAST | Sets the AGC attack/release speed for this slice. | |
| NR / NR2 / RN2 / NR4 / MNR / DFNR / BNR / NRL / NRS / RNN / NRF buttons (DSP tab) | Toggle button | Off | Enables the corresponding noise reduction algorithm for this slice. Button availability depends on radio series and build. | Right-click NR2, NR4, MNR, or DFNR to open the AetherDSP Settings dialog for that algorithm. |
| ADSP button (DSP tab) | Push button | — | Opens the AetherDSP Settings dialog (client-side NR2 / NR4 / DFNR / RN2 / BNR / MNR). Same entry point as the Settings menu (v0.9.8). | Styled like a radio-side DSP toggle but non-checkable. Click raises and focuses the modeless AetherDSP Settings dialog. |
| AetherVoice button (DSP tab) | Push button | — | Toggles the Aetherial Audio Channel Strip — the unified TX/RX DSP suite (v0.9.8). | Spans 2 columns in the 4-column DSP grid. Matches the existing menu / chain entry points for the strip. |
| Mode combo (Mode tab) | Combo box | USB | Sets the demodulation mode for this slice. | |
| Filter preset buttons (Mode tab) | Push button | — | Applies a saved filter width preset. Right-click to save the current filter width into that slot. | Persisted in `FilterPresets`. Custom lo/hi edges can be set per slot via right-click. |
| RIT / XIT buttons + labels (X/RIT tab) | Toggle button | Off | Enables receiver (RIT) or transmitter (XIT) incremental tuning. The label shows the current offset; scroll-wheel adjusts in 10 Hz steps. | |
| DAX channel combo (DAX tab) | Combo box | Off | Assigns a DAX audio channel to this slice. | |
| Marker thickness button | Push button | 1 px | Cycles the VFO marker line through Off, 1 px, and 3 px. | Persisted per slice in `Slice{N}_MarkerWidth`. |
| Filter edges button | Toggle button | Shown | Toggles the filter edge lines on the spectrum passband. | Persisted per slice in `Slice{N}_FilterEdgesHidden`. |
| Collapse toggle | Toggle button | Expanded | Collapses the VFO panel to a compact frequency-only strip. | Persisted per slice in `SliceFlagCollapsed_{N}`. Right-click on the collapsed frequency label opens the Add Spot context menu using the VFO's own frequency (v26.8.4). |

## DSP tab changes in v26.8.4

The DSP tab now includes a **Manual notch filter (MN)** button. This button appears only when the connected radio reports support for manual notch filtering (`hasManualNotch`). It is hidden on radios that do not support this feature.

The MN button:

- Is a toggle button in the DSP button grid, positioned in row 3, column 2.
- Uses the same `kDspToggle` styling as other DSP buttons.
- Has an accessible name of **"Manual notch filter"**.
- Opens a related DSP level control targeting `MN` when enabled (the shared DSP Level slider retargets to it).
- Right-clicking opens the AetherDSP Settings dialog for the manual notch algorithm, consistent with other notch filter buttons.

All DSP buttons now have stable object names (`dspNRBtn`, `dspNBBtn`, `dspMNBtn`, etc.) in addition to their accessible names. This provides a fixed contract for automation and scripting tools to address the buttons reliably, regardless of any future rewording of the accessible names.

## DSP tab changes in v0.9.7 (refined in v0.9.8)

The DSP tab now shows only radio-supplied noise reduction algorithms. The buttons for NR2, RN2, BNR, NR4, MNR, and DFNR have been removed from the VFO panel. Those algorithms are client-side modules; access them through the spectrum overlay menu or the AetherDSP applet.

The buttons present in the DSP tab are:

| Button | Algorithm |
|--------|-----------|
| NR | Noise reduction |
| NB | Noise blanker |
| ANF | Automatic notch filter |
| APF | Audio peaking filter (CW mode only) |
| MN | Manual notch filter (only on radios that support it) |
| NRL | Noise reduction level |
| NRS | Spectral subtraction |
| RNN | RNN noise reduction |
| NRF | Spectral noise filter |
| ANFL | LMS notch filter |
| ANFT | FFT notch filter |

A shared **DSP Level** row appears below the button grid. It contains a slider and a numeric readout. The slider retargets automatically to whichever leveled DSP algorithm was most recently enabled. The label to the left of the slider shows the active target (for example, **NR** or **NB**). When no leveled DSP algorithm is active — or when only RNN, ANFT, or APF is on — the row fades out and slider interaction has no effect. The row remains in the layout at all times; it does not shift the button grid when it fades in or out.

Algorithms that support a level via this slider: NR, NB, ANF, NRL, NRS, NRF, ANFL, MN.

**Note:** In v0.9.8, the DSP level slider now appears on launch for any DSP algorithm that was enabled in the radio's saved profile. Previously, it was missing until the user manually toggled the DSP button.

## Squelch behavior by mode

The squelch button and slider are automatically disabled in certain modes:

- **Digital modes (DIGU, DIGL):** Squelch is disabled because audio feeds external decoders via DAX — squelch is not meaningful and gates weak FSK signals.
- **RTTY:** Squelch is disabled for the same reasons as digital modes, resolving an issue where squelch would gate weak FSK signals (#2504).
- **CW:** Squelch is disabled because the radio locks squelch on at a fixed level and rejects changes.
- **FM modes (FM, NFM, DFM):** FM tone controls (CTCSS/DCS) are available; squelch works normally in these modes.

When squelch is disabled and was previously enabled, the system automatically turns squelch off for the slice and saves its state. When you switch back to a voice mode, squelch may be restored.

## VFO panel layout changes in v26.5.3

The stacked tab widget inside the VFO panel now uses a custom `QStackedWidget` subclass (`TabStack`) that reports only the current tab's preferred size. This fixes a visual gap that occurred when switching from the Mode tab (which has a shorter content height) to the DSP tab (which is taller when the digital sub-container is visible). The VFO panel no longer over-allocates height based on the tallest tab. The panel now adjusts its height cleanly as you switch between tabs.

## VFO panel layout changes in v26.7.4

The `TabStack` widget now additionally forwards `hasHeightForWidth()` and `heightForWidth()` from the current page. This allows pages that maintain an aspect ratio (such as the SmartMtrWidget meter) to drive the strip height correctly. Pages without height-for-width (such as the S-meter spacer) are unaffected. The VFO flag also now includes a lightweight elevation shadow rendered by a separate `FlagShadow` widget. The shadow is kept on a separate surface so that live meter repaints do not re-blur the entire flag at animation rate.

## Tab navigation changes in v26.6.3

The tab labels in the VFO panel have been changed from `QLabel` to `QPushButton`. This improves accessibility by making the tab buttons keyboard-focusable with Tab key navigation. Each tab button now has a focus indicator (outline) shown when focused via keyboard.

**Audio tab:** Right-click the Audio tab button to toggle the mute state for that slice directly, without opening the Audio tab.

**Frequency entry:** The frequency input field has been replaced with a `FreqLineEdit` widget that shows hint text instead of placeholder text, improving the visual appearance of direct frequency entry.

**Wheel event refinement:** The frequency scroll wheel now respects the `reverseMouseWheel` setting from `InteractionSettings`. If you have configured reverse mouse wheel in the settings, scrolling the VFO panel's frequency will invert direction accordingly (#3302).

## Theming changes in v26.6.1

The VFO panel now uses the AetherSDR theming system. All slider and button styles are derived from theme color tokens instead of hard-coded values, ensuring the panel matches the active color theme. The key visual changes are:

- **Pan slider:** The centre-anchored fill now uses the theme's accent colour (`color.accent`) for the (centre → handle) region. The groove background uses the theme's background colour (`color.background.1`). A centre-mark dot remains visible at the neutral position.
- **Small toggle buttons (TX badge, RX badge, etc.):** These now inherit background and accent colours from the theme via `{{color.background.1}}` and `{{color.accent}}` tokens, replacing the previous hard-coded `#1a2a3a` and `#00b4d8` values.
- **Theme scope:** The VFO panel is placed under the `spectrum/vfo` container scope so inspector clicks on VFO components display their theming tokens without bubbling up to the spectrum display.
- **Inspector coverage:** The widget declares its read token list (`color.background.0`, `color.background.1`, `color.background.2`, `color.text.primary`, `color.text.label`, `color.accent`, `color.accent.bright`) so Inspect-mode clicks produce meaningful hit lists for the background, signal meter, and badge areas.

## Tips

- Muting a slice does not reset the AF Gain slider. When you unmute, audio returns at the same level it was before.
- Right-click the **Audio** tab label to toggle mute directly without switching to the Audio tab.
- If you want to silence a slice permanently rather than temporarily, drag the AF