# Enable RIT or XIT offset from the VFO panel

RIT (Receiver Incremental Tuning) and XIT (Transmitter Incremental Tuning) let you shift the receive or transmit frequency by a small offset without moving the main VFO. This is useful for working split-frequency contacts or compensating for a station that is slightly off your dial frequency.

## Before you start

- AetherSDR must be connected to the radio. The VFO panel requires a live radio connection.
- The VFO panel for the target slice must be open and expanded. If it is collapsed to the frequency-only strip, click anywhere on it to expand it.

## Steps

1. Click the VFO marker flag on the spectrum display for the slice you want to adjust. The VFO panel appears anchored to the marker.
2. Click the **X/RIT** tab inside the VFO panel.
3. To enable receiver offset, click the **RIT** button. The button activates and the label shows the current RIT offset.
4. To enable transmitter offset, click the **XIT** button. The button activates and the label shows the current XIT offset.
5. With RIT or XIT active, place the mouse pointer over the corresponding button and scroll the mouse wheel to adjust the offset. Each scroll step changes the offset by 10 Hz.
6. To disable RIT or XIT, click the active button again.

## What each control does

| Control                              | Kind              | Default   | Notes                                                                |
|--------------------------------------|-------------------|-----------|----------------------------------------------------------------------|
| RX antenna button                    | Push button       |           | Opens antenna selection menu for the receive antenna of this slice. |
| TX antenna button                    | Push button       |           | Opens antenna selection menu for the transmit antenna of this slice. |
| Frequency display                    | Indicator         |           | Shows the current slice frequency. Click once to begin direct frequency entry; type MHz and press Enter or Tab. |
| Filter width label                   | Indicator         |           | Shows current filter bandwidth. Click to cycle through filter preset buttons in the Mode tab. Uses RxApplet::formatFilterWidth as the single source of truth, fixing a 0.1 kHz offset that affected SSB/digital mode readouts (#2197, v0.9.8). |
| AF Gain slider (Audio tab)           | Slider            | 100       | Sets the audio output level for this slice. Not persisted — reflects live radio state. |
| Pan slider (Audio tab)               | Slider            | 50        | Sets left/right stereo pan for this slice. 50 = centre. |
| Mute button (Audio tab)              | Toggle button     | off       | Mutes audio output for this slice without changing the AF gain setting. |
| Squelch button + slider (Audio tab)  | Toggle button     | off       | Enables squelch for this slice. The adjacent slider sets the threshold. |
| AGC combo (Audio tab)                | Combo box         | FAST      | Sets the AGC attack/release speed for this slice. |
| NR / NR2 / RN2 / NR4 / MNR / DFNR / BNR / NRL / NRS / RNN / NRF / MN buttons (DSP tab) | Toggle button | off | Enables the corresponding noise reduction algorithm for this slice. Button availability depends on radio series and build. The MN (manual notch) button appears only on radios that support manual notch filtering. |
| ADSP button (DSP tab)                | Push button       |           | Opens the AetherDSP Settings dialog (client-side NR2 / NR4 / DFNR / RN2 / BNR / MNR). Styled like a radio-side DSP toggle but non-checkable. Click raises and focuses the modeless AetherDSP Settings dialog. |
| AetherVoice button (DSP tab)          | Push button       |           | Toggles the Aetherial Audio Channel Strip — the unified TX/RX DSP suite. Spans 2 columns in the 4-column DSP grid. |
| Mode combo (Mode tab)                | Combo box         | USB       | Sets the demodulation mode for this slice. |
| Filter preset buttons (Mode tab)     | Push button       |           | Applies a saved filter width preset. Right-click to save the current filter width into that slot. Persisted in FilterPresets. Custom lo/hi edges can be set per slot via right-click. |
| RIT / XIT buttons + labels (X/RIT tab) | Toggle button   | off       | Enables receiver (RIT) or transmitter (XIT) incremental tuning. The label shows the current offset; scroll-wheel adjusts in 10 Hz steps. |
| DAX channel combo (DAX tab)          | Combo box         | Off       | Assigns a DAX audio channel to this slice. |
| Marker thickness button              | Push button       | 1 px      | Cycles the VFO marker line through Off, 1 px, and 3 px. Persisted per slice. |
| Filter edges button                  | Toggle button     | shown     | Toggles the filter edge lines on the spectrum passband. Persisted per slice. |
| Collapse toggle                      | Toggle button     | expanded  | Collapses the VFO panel to a compact frequency-only strip. Persisted per slice. |
| TX badge                             | Indicator         |           | Shows TX (red) when this slice is the active transmit slice. Hidden otherwise. |
| SPLIT badge                          | Indicator         |           | Shows SPLIT (amber) when TX is assigned to a different slice than the active receive slice. Hidden otherwise. |

**RX antenna button** — Opens an antenna selection menu for the receive antenna of this slice. The menu now uses the per-slice `rxAntennaList()` property when available, falling back to the global antenna list. Menu items show a human-readable label alongside the internal antenna identifier.

**TX antenna button** — Opens an antenna selection menu for the transmit antenna of this slice. The menu filters out RX-only antenna ports. Uses the `txAntennaOptions()` helper to determine valid transmit antennas. Menu items show a human-readable label alongside the internal antenna identifier.

**Filter width label** — Shows the current filter bandwidth for the slice. Click to cycle through the filter preset buttons in the Mode tab. The label uses RxApplet::formatFilterWidth as the single source of truth, which fixes a 0.1 kHz offset that previously affected SSB and digital mode readouts (#2197, v0.9.8).

**NR / NR2 / RN2 / NR4 / MNR / DFNR / BNR / NRL / NRS / RNN / NRF / MN buttons (DSP tab)** — Enable the corresponding noise reduction algorithm for this slice. Button availability depends on radio series and build. The MN (manual notch) button appears only on radios that support manual notch filtering. Right-click NR2, NR4, MNR, or DFNR to open the AetherDSP Settings dialog for that algorithm.

**ADSP button (DSP tab)** — Opens the AetherDSP Settings dialog (client-side NR2 / NR4 / DFNR / RN2 / BNR / MNR). Same entry point as the Settings menu (v0.9.8). The button is styled like a radio-side DSP toggle but is non-checkable; clicking it raises and focuses the modeless AetherDSP Settings dialog.

**AetherVoice button (DSP tab)** — Toggles the Aetherial Audio Channel Strip — the unified TX/RX DSP suite (v0.9.8). The button spans 2 columns in the 4-column DSP grid and matches the existing menu and chain entry points for the strip.

**Marker thickness button** — Cycles the VFO marker line through Off, 1 px, and 3 px. Persisted per slice.

**Filter edges button** — Toggles the filter edge lines on the spectrum passband. Persisted per slice.

**Collapse toggle** — Collapses the VFO panel to a compact frequency-only strip. Persisted per slice.

**TX badge** — Shown when this slice is the active transmit slice. Displays a red TX indicator.

**SPLIT badge** — Shown when TX is assigned to a different slice than the active receive slice. Displays an amber SPLIT indicator.

**RIT / XIT buttons + labels** — Enable receiver (RIT) or transmitter (XIT) incremental tuning for this slice. When active, the label next to each button shows the current offset value. Scroll the mouse wheel over the button to adjust the offset in 10 Hz steps. Neither setting is persisted; state reflects live radio state.

**Squelch button + slider (Audio tab)** — Enables squelch for this slice. The adjacent slider sets the threshold. Squelch is automatically disabled when the slice mode is CW, digital, or RTTY, because in those modes audio feeds external decoders via DAX where squelch would gate weak FSK signals (#2504). The button and slider are greyed out in those modes.

## Tips

- RIT and XIT offsets are independent. You can enable both at the same time to offset receive and transmit independently.
- Scroll-wheel adjustment is 10 Hz per step. For larger offsets, scroll multiple notches.
- When a slice is locked, scroll-wheel tuning on the VFO panel is blocked. A notification appears indicating that tuning is blocked by the lock. Direct frequency entry is also canceled if it was in progress when the lock is applied.
- Right-click on the collapsed frequency strip to add a spot. The right-click context menu works even when the panel is collapsed to the frequency-only strip, and reports the VFO frequency correctly rather than the step-snapped cursor frequency from the spectrum display underneath (#4455).

## Changes in v26.8.4

### Manual notch (MN) filter support

A new **MN** (manual notch) button has been added to the DSP tab grid. This button is hidden by default and appears only on radios that report support for manual notch filtering (`hasManualNotch`). When available, the MN button toggles the manual notch filter for the slice, and the shared DSP-level slider adjusts the manual notch level when the MN button is the active filter.

The MN button uses a stable object name (`dspMNBtn`) for automation bridge addressing. All DSP toggle buttons now use stable object names based on their text (for example, `dspNRBtn`, `dspAPFBtn`) rather than prose-style accessible names. This ensures automation scripts that drive these controls continue to work even if the user-facing labels are reworded in the future.

### Squelch method rename

The internal squelch control method has been renamed from `setSquelch()` to `setManualSquelch()` to distinguish it from automatic squelch modes. The user-facing behavior is unchanged — the squelch button and slider in the Audio tab work exactly as before.

### Collapsed mode right-click spot fix

Right-click → **Add Spot** now works correctly when the VFO panel is collapsed to the frequency-only strip (#4455). Previously, clicks fell through to the SpectrumWidget underneath, which reported the cursor's step-snapped frequency instead of the VFO's actual frequency. The collapsed frequency label now intercepts events, so the spot is added at the VFO frequency.

### FM mode detection

The VFO panel now correctly identifies FM-related modes (FM, NFM, DFM, DSTR) for tone control purposes. FM tone controls are shown only for FM, NFM, and DFM modes.

## Changes in v26.7.4

### Elevation shadow rendering

The VFO flag now renders its elevation shadow using a dedicated `FlagShadow` widget, separate from the main `VfoWidget`. This means live meter repaints inside the VFO flag do not force the shadow to re-blur at animation rate, improving frame rate when a SmartMeter or other live-updating widget is embedded in the VFO flag area. The shadow uses a box-blur algorithm with a cached image that is rebuilt only when the widget size or device pixel ratio changes.

### Height-for-width forwarding for meter pages

The tab stack now forwards `heightForWidth()` from the current page. This allows a page that preserves an aspect ratio (such as a SmartMeter widget embedded via `SmartMtrWidget`) to drive the strip height; pages without height-for-width (such as the S-meter spacer) are unaffected.

### Adaptive filter controls

The VFO panel now includes support for adaptive filter controls via the new `AdaptiveFilterControls` class. When the radio provides adaptive filter signals (supported by certain FLEX-8600 firmware builds), the VFO panel displays controls for configuring the adaptive filter behavior on a per-slice basis.

## Changes in v26.6.3

### Tab buttons replaced with QPushButton

The tab labels in the tab bar have been replaced from QLabel to QPushButton. Each tab is now a flat, checkable button with keyboard focus support. Pressing Tab cycles through the tab buttons. Right-click on the Audio tab (speaker) button toggles mute directly without opening the tab.

### Accessible frequency announcements

When a screen reader or other accessibility tool is active, the frequency display emits an accessible value change event when the frequency changes. Duplicate announcements are suppressed — only distinct frequency texts trigger a new announcement.

### Reverse mouse wheel tuning support

Scroll-wheel tuning now respects the **Reverse mouse wheel** preference in `InteractionSettings`. When enabled, scrolling up decreases the frequency and scrolling down increases it.

## Changes in v26.6.1

### Theme-aware Pan slider

The Pan slider in the Audio tab now uses a centre-anchored fill. The slider groove fills from the centre outward — blue accent to the right of centre when the pan is right-heavy, and a background colour to the left of centre. When the pan is left-heavy, the groove fills from centre to the left in accent colour while the right side uses the background colour. This matches the behaviour of a stereo balance control where the meaningful zero is the midpoint. A small centre-mark dot is still painted on the