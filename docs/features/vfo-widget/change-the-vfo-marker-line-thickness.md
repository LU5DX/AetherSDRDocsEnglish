# Change the VFO Marker Line Thickness

Use the marker thickness button to control how prominent the VFO marker line appears on the spectrum display, or to hide it entirely. The setting is saved per slice.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- The VFO panel must be open for the slice you want to adjust. If it is not visible, click the VFO marker flag for that slice on the spectrum display.

## Steps

1. Open the VFO panel for the target slice by clicking its VFO marker flag on the spectrum display.
2. Locate the **Marker thickness button** in the VFO panel.
3. Click the button to cycle through the available values: **Off**, **1 px**, and **3 px**.
4. Stop clicking when the desired thickness is shown. The marker on the spectrum display updates immediately.

## What each control does

| Control                      | Default                                                                                                                               | Valid values                                            |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| Marker thickness button      | 1 px                                                                                                                                  | Off, 1 px, 3 px                                         |
| ADSP button (DSP tab)        | Opens the AetherDSP Settings dialog (client-side NR2 / NR4 / DFNR / RN2 / BNR / MNR). Same entry point as the Settings menu (v0.9.8). | Styled like a radio-side DSP toggle but non-checkable. Click raises and focuses the modeless AetherDSP Settings dialog. |
| AetherVoice button (DSP tab) | Toggles the Aetherial Audio Channel Strip — the unified TX/RX DSP suite (v0.9.8).                                                     | Spans 2 columns in the 4-column DSP grid. Matches the existing menu / chain entry points for the strip.                 |

Each click advances to the next value in the cycle: **Off** → **1 px** → **3 px** → **Off**. The setting is persisted per slice, so slice 1 and slice 2 can have different thicknesses.

## Tips

- Setting the marker to **Off** hides the vertical line entirely. The VFO panel and flag remain visible and functional.
- If you run multiple slices on the same panadapter, increasing one marker to **3 px** can help distinguish it from adjacent slices.

## DSP tab changes in v0.9.8

The DSP tab in the VFO panel now shows only radio-supplied noise reduction buttons. The following buttons have been removed from the VFO panel DSP tab:

| Removed button | Where to find it now |
|---|---|
| NR2 | Spectrum overlay menu or AetherDSP applet |
| RN2 | Spectrum overlay menu or AetherDSP applet |
| BNR | Spectrum overlay menu or AetherDSP applet |
| NR4 | Spectrum overlay menu or AetherDSP applet |
| MNR | Spectrum overlay menu or AetherDSP applet |
| DFNR | Spectrum overlay menu or AetherDSP applet |

The remaining DSP tab buttons are arranged in a four-column grid:

| Row | Col 0 | Col 1 | Col 2 | Col 3 |
|---|---|---|---|---|
| 0 | NR | NB | ANF | APF |
| 1 | NRL | NRS | RNN | NRF |
| 2 | ANFL | ANFT | ADSP | AetherVoice (2 cols) |

The APF button remains hidden unless the slice is in a CW mode.

Two new client-side launcher buttons appear in row 2 of the grid:
- **ADSP** — Opens the AetherDSP Settings dialog (client-side NR2 / NR4 / DFNR / RN2 / BNR / MNR). This button is styled like a radio-side DSP toggle but is non-checkable. Click raises and focuses the modeless AetherDSP Settings dialog.
- **AetherVoice** — Toggles the Aetherial Audio Channel Strip — the unified TX/RX DSP suite (v0.9.8). This button spans 2 columns in the 4-column DSP grid. Matches the existing menu / chain entry points for the strip.

### DSP Level slider

A shared level slider row appears below the DSP button grid. The slider retargets automatically to whichever leveled DSP button was most recently enabled. The row label updates to show the active target (for example, **NR** or **NB**). The numeric value is shown to the right of the slider.

The row is always present in the layout. When no leveled DSP is active — or when only RNN, ANFT, or APF is on — the row fades to transparent. It becomes fully visible again as soon as a leveled DSP is turned on.

The slider controls the level for these targets:

| Target label | DSP controlled |
|---|---|
| NR | Noise reduction level |
| NB | Noise blanker level |
| ANF | Automatic notch filter level |
| NRL | Noise reduction level (NRL) |
| NRS | Spectral subtraction level |
| NRF | Spectral noise filter level |
| ANFL | LMS notch filter level |

## Squelch control behavior

The squelch button and slider in the Audio tab are disabled in digital, RTTY, and CW modes. Digital and RTTY modes feed audio to external decoders via DAX, where squelch is not meaningful and can gate weak FSK signals. The radio locks squelch on at a fixed level in CW mode and rejects changes. When switching into one of these modes while squelch is enabled, squelch is automatically disabled and the saved state is retained in the radio for when you switch back to a voice mode.

## DSP startup behavior (v0.9.8)

When AetherSDR connects to the radio, any DSP that was enabled in the radio's saved profile now immediately pushes its level into the shared DSP level slider. Previously, the slider would be missing on launch for these DSPs until the user manually toggled them. This fix ensures the slider is always present and active when a leveled DSP is already enabled on the radio.

## Filter width label fix (v0.9.8)

The filter width label in the VFO panel now uses a single source of truth (`RxApplet::formatFilterWidth`) to generate its readout. This fixes a 0.1 kHz offset that affected SSB and digital mode readouts, and ensures the VFO panel and RX applet display identical filter width values.

## Antenna selection improvements (v26.5.2.1)

The RX and TX antenna buttons now use per-slice antenna lists when available, falling back to the global antenna list. The TX antenna menu excludes RX-only ports by checking specific naming patterns.

### RX antenna selection

1. Open the VFO panel for the target slice.
2. Click the **RX antenna button**. A menu opens showing available receive antennas.
3. Select an antenna from the menu. The slice immediately uses the selected antenna for receive.

The menu shows the per-slice receive antenna list if one is available. Each entry has a tooltip showing the full antenna port identifier.

### TX antenna selection

1. Open the VFO panel for the target slice.
2. Click the **TX antenna button**. A menu opens showing antennas that can be used for transmit.
3. Select an antenna from the menu. The slice immediately uses the selected antenna for transmit.

The menu filters out antenna ports that start with "RX" to prevent selecting RX-only ports for transmit. Each entry has a tooltip showing the full antenna port identifier.

## Frequency entry improvements (v26.5.3)

### Direct frequency entry behavior when slice is locked

When a slice is locked, attempting to begin direct frequency entry by clicking the frequency display is blocked. The direct entry field does not appear. If a direct entry is already in progress when the slice is locked, the entry is cancelled and the display returns to showing the locked frequency. A visual "LOCKED" overlay is displayed centrally through the slice model.

### Frequency entry on XVTR bands (v26.5.2.1)

When entering frequencies on transverter (XVTR) bands, the maximum supported frequency has been increased from 450 MHz to 50,000 MHz. The automatic decimal insertion logic now only applies to three-digit bands (100–999 MHz) when the entered value exceeds 450 MHz. For higher bands (1,000 MHz and above), bare integers are interpreted as MHz without decimal insertion.

### Explicit MHz entry on HF bands (v26.5.3)

When entering a frequency on HF bands, entering a value greater than 54 MHz with an explicit decimal point (for example, "144.200") is now interpreted as MHz rather than being automatically divided by 1,000 (kHz) or 1,000,000 (Hz). This allows direct MHz entry for VHF/UHF frequencies even when not on an XVTR band.

## Collapsed mode scroll wheel tuning (v26.5.3)

In collapsed mode, the scroll wheel now tunes the slice even when the slice is locked. When the locked slice is scrolled, a visual "LOCKED" notification is displayed to indicate that tuning was blocked. Previously, collapsed mode would ignore scroll events when the slice was locked.

## Tab stack height fix (v26.5.3)

The VFO panel's tab content area now reports only the current tab page's preferred size, rather than the maximum of all pages. This fixes a height gap that occurred when the DSP tab was taller than the Mode tab (for example, when the digital sub-mode container was visible in DIGU or DIGL mode).

## Slice badge HTML support (v26.5.2.1)

The slice badge that displays the slice letter can now render rich text. This allows future enhancements where non-ASCII characters or styled text may be used for slice identification.

## Pan slider center-mark visual (v26.6.1)

The Pan slider in the Audio tab now fills its groove from the centre outward instead of from the left edge. A small centre-mark dot is painted on the groove at the neutral position (50) so the operator can see the midpoint at a glance.

This change corrects the visual reading of the L/R pan control — the filled portion now accurately represents the amount of pan away from centre, matching operator expectation for centre-anchored controls.

## VFO Panel overview

The VFO panel is a floating per-slice control panel anchored to the VFO marker on the spectrum display. It provides quick access to the most frequently used per-slice settings without leaving the spectrum view.

### Controls

| Control | Type | Default | Behavior |
|---|---|---|---|
| RX antenna button | push_button | - | Opens antenna selection menu for the receive antenna of this slice. |
| TX antenna button | push_button | - | Opens antenna selection menu for the transmit antenna of this slice. |
| Frequency display | indicator | - | Shows the current slice frequency. Click once to begin direct frequency entry; type MHz and press Enter or Tab. Direct entry is blocked when the slice is locked. |
| Filter width label | indicator | - | Shows current filter bandwidth. Click to cycle through filter preset buttons in the Mode tab. Uses a single source of truth (`RxApplet::formatFilterWidth`) to generate its readout. |
| AF Gain slider (Audio tab) | slider | 100 | Sets the audio output level for this slice. Range 0-100. |
| Pan slider (Audio tab) | slider | 50 | Sets left/right stereo pan for this slice. 50 = centre. Range 0-100. Groove fills from centre outward with a centre-mark dot at the neutral position. |
| Mute button (Audio tab) | toggle_button | off | Mutes audio output for this slice without changing the AF gain setting. |
| Squelch button + slider (Audio tab) | toggle_button | off | Enables squelch for this slice. The adjacent slider sets the threshold. Range 0-100. |
| AGC combo (Audio tab) | combo_box | FAST | Sets the AGC attack/release speed for this slice. Options: FAST, MED, SLOW, OFF. |
| NR / NR2 / RN2 / NR4 / MNR / DFNR / BNR / NRL / NRS / RNN / NRF buttons (DSP tab) | toggle_button | off | Enables the corresponding noise reduction algorithm for this slice. Button availability depends on radio series and build. Right-click NR2, NR4, MNR, or DFNR to open the AetherDSP Settings dialog for that algorithm. |
| ADSP button (DSP tab) | push_button | - | Opens the AetherDSP Settings dialog (client-side NR2 / NR4 / DFNR / RN2 / BNR / MNR). Same entry point as the Settings menu (v0.9.8). Styled like a radio-side DSP toggle but non-checkable. Click raises and focuses the modeless AetherDSP Settings dialog. |
| AetherVoice button (DSP tab) | push_button | - | Toggles the Aetherial Audio Channel Strip — the unified TX/RX DSP suite (v0.9.8). Spans 2 columns in the 4-column DSP grid. |
| Mode combo (Mode tab) | combo_box | USB | Sets the demodulation mode for this slice. Options: USB, LSB, CW, CWL, AM, SAM, DIGU, DIGL, FM, NFM, DFM, RTTY. |
| Filter preset buttons (Mode tab) | push_button | - | Applies a saved filter width preset. Right-click to save the current filter width into that slot. Persisted in `FilterPresets`. |
| RIT / XIT buttons + labels (X/RIT tab) | toggle_button | off | Enables receiver (RIT) or transmitter (XIT) incremental tuning. Scroll-wheel adjusts in 10 Hz steps. |
| DAX channel combo (DAX tab) | combo_box | Off | Assigns a DAX audio channel to this slice. Options: Off, 1-8. |
| Marker thickness button | push_button | 1 px | Cycles the VFO marker line through Off