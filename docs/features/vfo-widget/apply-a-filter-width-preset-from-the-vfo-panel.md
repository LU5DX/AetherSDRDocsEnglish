# Apply a filter width preset from the VFO panel

Filter preset buttons let you switch the receive filter width for a slice with a single click. Use them to move quickly between common bandwidths — for example, between a wide 3 kHz SSB filter and a narrow 500 Hz CW filter — without leaving the spectrum view.

## Before you start

- AetherSDR must be connected to the radio. The VFO panel requires an active radio connection.
- The VFO panel for the target slice must be open and expanded. If it is collapsed to a frequency-only strip, click anywhere on it to expand it first.

## Steps

1. Click the VFO marker flag on the spectrum display for the slice you want to adjust. The VFO panel opens, anchored to the left of the marker.
2. Click the **Mode** tab inside the VFO panel.
3. Click the filter preset button that corresponds to the bandwidth you want. The radio immediately applies that filter width to the slice.

To save the current filter width into a preset slot:

1. Set the filter to the bandwidth you want to save (see [Set a custom filter edge from the VFO panel](set-a-custom-filter-edge-from-the-vfo-panel.md)).
2. Right-click the preset button slot you want to overwrite.
3. The current filter width is saved into that slot.

## What each control does

| Control                          | Behavior                                                                                                                                                                                                                                       | Default                                                                                                                 |
|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| RX antenna button                | Opens an antenna selection menu for the receive antenna of this slice. Uses slice-specific antenna list when available. Menu items display tooltip and status tip.                                                                                | —                                                                                                                       |
| TX antenna button                | Opens an antenna selection menu for the transmit antenna of this slice. Automatically filters out RX-only antenna ports. Menu items display tooltip and status tip.                                                                               | —                                                                                                                       |
| Frequency display                | Shows the current slice frequency. Click once to begin direct frequency entry; type MHz and press Enter or Tab. Direct entry is blocked when the slice is locked.                                                                                 | —                                                                                                                       |
| Filter width label               | Shows current filter bandwidth. Click to cycle through filter preset buttons in the Mode tab. Uses RxApplet::formatFilterWidth as the single source of truth, fixing a 0.1 kHz offset that affected SSB/digital mode readouts (#2197, v0.9.8). |                                                                                                                         |
| AF Gain slider (Audio tab)       | Sets the audio output level for this slice (0-100).                                                                                                                                                                                              | 100                                                                                                                     |
| Pan slider (Audio tab)           | Sets left/right stereo pan for this slice (0-100). 50 = centre. The slider fill anchors from the centre outward, with a centre-mark dot on the groove showing the neutral position.                                                              | 50                                                                                                                      |
| Mute button (Audio tab)          | Mutes audio output for this slice without changing the AF gain setting. Right-click the Audio tab button to toggle mute directly.                                                                                                                 | off                                                                                                                     |
| Squelch button + slider (Audio tab) | Enables squelch for this slice. The adjacent slider sets the threshold (0-100). Disabled for RTTY and digital modes (DIGU, DIGL).                                                                                                                 | off                                                                                                                     |
| AGC combo (Audio tab)            | Sets the AGC attack/release speed for this slice. Options: FAST, MED, SLOW, OFF.                                                                                                                                                                | FAST                                                                                                                    |
| NR / NB / ANF / APF / NRL / NRS / RNN / NRF / ANFL / ANFT buttons (DSP tab) | Enables the corresponding radio-side noise reduction or filtering algorithm for this slice. APF is visible in CW mode only.                                                                                           | off                                                                                                                     |
| DSP level slider (DSP tab)       | Sets the processing level for the most recently activated leveled DSP algorithm. The label to the left identifies the current target. Automatically activates on startup if the radio's saved profile has a leveled DSP enabled. Hidden (faded) when no leveled algorithm is active. | —                                                                                                                       |
| ADSP button (DSP tab)            | Opens the AetherDSP Settings dialog (client-side NR2 / NR4 / DFNR / RN2 / BNR / MNR). Non-checkable push button. Click raises and focuses the modeless dialog.                                                                                   | —                                                                                                                       |
| AetherVoice button (DSP tab)     | Opens the Aetherial Audio Channel Strip — the unified TX/RX DSP suite. Non-checkable push button. Spans 2 columns in the 4-column DSP grid.                                                                                                      | —                                                                                                                       |
| Mode combo (Mode tab)            | Sets the demodulation mode for this slice. Options: USB, LSB, CW, CWL, AM, SAM, DIGU, DIGL, FM, NFM, DFM, RTTY.                                                                                                                                | USB                                                                                                                     |
| Filter preset buttons (Mode tab) | Each button applies a saved filter width preset to the slice. Left-click to apply; right-click to save the current filter width into that slot. Custom low and high filter edges can be stored per slot via right-click.                          | —                                                                                                                       |
| RIT / XIT buttons + labels (X/RIT tab) | Enables receiver (RIT) or transmitter (XIT) incremental tuning. The label shows the current offset; scroll-wheel adjusts in 10 Hz steps.                                                                                                       | off                                                                                                                     |
| DAX channel combo (DAX tab)      | Assigns a DAX audio channel to this slice. Options: Off, 1-8.                                                                                                                                                                                   | Off                                                                                                                     |
| Marker thickness button          | Cycles the VFO marker line through Off, 1 px, and 3 px. Persisted per slice.                                                                                                                                                                    | 1 px                                                                                                                    |
| Filter edges button              | Toggles the filter edge lines on the spectrum passband. Persisted per slice.                                                                                                                                                                    | shown                                                                                                                   |
| Collapse toggle                  | Collapses the VFO panel to a compact frequency-only strip. Persisted per slice.                                                                                                                                                                 | expanded                                                                                                                |

## DSP tab layout (v0.9.8)

The **DSP tab** shows radio-side noise reduction and filtering buttons arranged in a four-column grid, followed by the ADSP and AetherVoice launcher buttons:

| Position | Button |
|---|---|
| Row 1, col 1 | NR |
| Row 1, col 2 | NB |
| Row 1, col 3 | ANF |
| Row 1, col 4 | APF (visible in CW mode only) |
| Row 2, col 1 | NRL |
| Row 2, col 2 | NRS |
| Row 2, col 3 | RNN |
| Row 2, col 4 | NRF |
| Row 3, col 1 | ANFL |
| Row 3, col 2 | ANFT |
| Row 4, col 1 | ADSP |
| Row 4, cols 2–3 | AetherVoice |

A shared **DSP level slider** row appears below the button grid. The slider retargets automatically to whichever leveled DSP button was most recently turned on. In v0.9.8, when a DSP level state change arrives from the radio (for example, when the radio's saved profile has NR enabled on startup), the slider appears immediately without requiring manual re-toggle. Its label shows the name of the current target (for example, **NR** or **NB**), and the value to the right of the slider shows the current level numerically. When no leveled DSP algorithm is active — or when only RNN, ANFT, or APF is on — the slider row is present in the layout but visually faded out. Clicking it while faded has no effect.

The following client-side DSP modules have been removed from the VFO panel DSP tab in v0.9.8: **NR2**, **RN2**, **BNR**, **NR4**, **MNR**, **DFNR**. Toggle them from the spectrum overlay menu or the AetherDSP applet instead.

## Tab button changes (v26.6.3)

The VFO panel tab labels (Audio, DSP, Mode, X/RIT, DAX) have been changed from `QLabel` to `QPushButton` widgets. This change provides:

- **Keyboard accessibility**: Tab buttons are now reachable via the Tab key. Press Tab to navigate between tabs and press Enter or Space to activate the focused tab.
- **Focus indicator**: The focused tab button displays a visible focus ring (bottom border) using the theme's label text colour (`#6880a0`), making keyboard navigation visible.
- **Right-click on Audio tab**: Right-click the **Audio** tab button to toggle the mute state directly, without needing to open the Audio tab and click the Mute button.

## Frequency scroll direction (v26.6.3)

The mouse wheel scroll direction for frequency tuning in the VFO panel now respects the **Reverse mouse wheel** setting found in `Settings > Interaction`. When this setting is enabled, scrolling the mouse wheel upward decreases the frequency and scrolling downward increases it. Previously, the scroll direction was always fixed regardless of this setting.

## Squelch behavior changes (v26.5.1)

The squelch control in the **Audio tab** is now disabled for RTTY and digital modes, in addition to CW mode. This prevents the squelch from gating weak FSK signals that are fed to external decoders via DAX (#2504).

When you switch a slice to DIGU, DIGL, or RTTY mode:

- The Squelch button and slider become disabled.
- If squelch was active, it is automatically turned off. The previous state is saved internally and restored if you switch back to a voice mode.

This matches the existing behavior for CW mode, where the radio locks squelch on at a fixed level and rejects user changes.

## Antenna selection changes (v26.5.2.1)

The **RX antenna** and **TX antenna** buttons now use improved menus:

- The RX antenna menu uses the slice's `rxAntennaList()` when available, falling back to the global antenna list for legacy compatibility.
- The TX antenna menu intelligently filters out RX-only antenna ports by checking for "RX" prefixes, "ANT" prefixes, "TX" prefixes, or "XVTR" as fallback tokens.
- Menu items now store the antenna identifier as data, allowing selection by internal name rather than displayed label.
- Each menu item includes a tooltip and status tip showing the antenna identifier.

## Frequency entry improvements (v26.5.2.1)

The frequency entry logic has been updated to better handle transverter (XVTR) bands:

- The maximum XVTR frequency has been increased from 450 MHz to 50000 MHz to support microwave bands.
- The "three-digit band" convenience parsing (inserting a decimal after the third digit for bare integers like 1446 → 144.6 MHz) now only activates when the slice frequency is between 100 MHz and 999 MHz. For 23 cm and microwave bands (above 1000 MHz), a bare integer like 1296 is treated as 1296 MHz directly.

## Frequency entry improvements (v26.5.3)

The frequency entry logic now uses the `FrequencyEntryParser` utility class for consistent parsing across the application:

- Explicit MHz entry (typing a frequency greater than 54 MHz) is now recognized on HF bands as well, allowing direct MHz entry without being on an XVTR band.
- The `normalizedMhzText()` method handles multi-dot formats like "14.225.000" by removing dots beyond the first, ensuring consistent parsing.
- Direct frequency entry is blocked when the slice is locked. Attempting to enter a frequency while locked produces no action.

## Slice badge rendering (v26.5.2.1)

The slice letter badge now renders as Qt Rich Text (`Qt::RichText`), fixing an issue where certain slice letters displayed incorrectly (#2606). The badge styling remains the same.

## Pan slider visual improvements (v26.6.1)

The **Pan slider** in the **Audio tab** now paints its fill from the centre outward, with a small centre-mark dot on the groove. This makes the neutral (50%) position visible at a glance, and the fill direction matches operator expectations for a left/right balance control.

Previously, the slider fill painted from the left edge to the handle position, which was misleading for a centre-anchored control where the meaningful zero is the midpoint. The new rendering uses the `CenterMarkSlider` class that over-paints the default Qt sub-page fill: it erases the unwanted half of the sub-page with the groove background colour, then adds the desired centre-to-handle fill in the accent colour.

## Theme update (v26.6.1)

The VFO panel now uses the theme system for all visual elements:

- The VFO panel container is registered under the `spectrum/vfo` theme scope, allowing theme files to target VFO-specific styling separately from the spectrum display.
- The `CenterMarkSlider` and `MiniBadgeButton` classes use `ThemeManager` color tokens (`color.background.1`, `color.accent`, etc.) for their custom paint operations.
- The MiniBadge button stylesheet uses the `applyStyleSheet()` method with theme template variables (e.g., `{{color.background.1}}`, `{{color.accent}}`) instead of hardcoded hex colours.
- The Inspector tool (Inspect mode click) on the VFO panel now surfaces the theme tokens it reads: `color.background.0`, `color.background.1`, `color.background.2`, `color.text.primary`, `color.text.label`, `color.accent`, and `color.accent.bright`.

## Accessibility improvements (v26.6.3)

The VFO panel now provides accessibility support for the frequency display:

- **Value change events**: When the slice frequency changes, an accessible value change event is fired for the