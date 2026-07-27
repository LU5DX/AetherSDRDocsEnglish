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
| Filter width label                   | Indicator         |           | Shows current filter bandwidth. Click to cycle through filter preset buttons in the Mode tab. Uses RxApplet::formatFilterWidth as the single source of truth. |
| AF Gain slider (Audio tab)           | Slider            | 100       | Sets the audio output level for this slice. Not persisted — reflects live radio state. |
| Pan slider (Audio tab)               | Slider            | 50        | Sets left/right stereo pan for this slice. 50 = centre. |
| Mute button (Audio tab)              | Toggle button     | off       | Mutes audio output for this slice without changing the AF gain setting. |
| Squelch button + slider (Audio tab)  | Toggle button     | off       | Enables squelch for this slice. The adjacent slider sets the threshold. |
| AGC combo (Audio tab)                | Combo box         | FAST      | Sets the AGC attack/release speed for this slice. |
| NR / NR2 / RN2 / NR4 / MNR / DFNR / BNR / NRL / NRS / RNN / NRF buttons (DSP tab) | Toggle button | off | Enables the corresponding noise reduction algorithm for this slice. Button availability depends on radio series and build. |
| ADSP button (DSP tab)                | Push button       |           | Opens the AetherDSP Settings dialog (client-side NR2 / NR4 / DFNR / RN2 / BNR / MNR). |
| AetherVoice button (DSP tab)          | Push button       |           | Toggles the Aetherial Audio Channel Strip — the unified TX/RX DSP suite. Spans 2 columns in the 4-column DSP grid. |
| Mode combo (Mode tab)                | Combo box         | USB       | Sets the demodulation mode for this slice. |
| Filter preset buttons (Mode tab)     | Push button       |           | Applies a saved filter width preset. Right-click to save the current filter width into that slot. Persisted in FilterPresets. |
| RIT / XIT buttons + labels (X/RIT tab) | Toggle button   | off       | Enables receiver (RIT) or transmitter (XIT) incremental tuning. The label shows the current offset; scroll-wheel adjusts in 10 Hz steps. |
| DAX channel combo (DAX tab)          | Combo box         | Off       | Assigns a DAX audio channel to this slice. |
| Marker thickness button              | Push button       | 1 px      | Cycles the VFO marker line through Off, 1 px, and 3 px. Persisted per slice. |
| Filter edges button                  | Toggle button     | shown     | Toggles the filter edge lines on the spectrum passband. Persisted per slice. |
| Collapse toggle                      | Toggle button     | expanded  | Collapses the VFO panel to a compact frequency-only strip. Persisted per slice. |
| TX badge                             | Indicator         |           | Shows TX (red) when this slice is the active transmit slice. Hidden otherwise. |
| SPLIT badge                          | Indicator         |           | Shows SPLIT (amber) when TX is assigned to a different slice than the active receive slice. Hidden otherwise. |

**RX antenna button** — Opens an antenna selection menu for the receive antenna of this slice. The menu now uses the per-slice `rxAntennaList()` property when available, falling back to the global antenna list. Menu items show a human-readable label alongside the internal antenna identifier.

**TX antenna button** — Opens an antenna selection menu for the transmit antenna of this slice. The menu filters out RX-only antenna ports. Uses the `txAntennaOptions()` helper to determine valid transmit antennas. Menu items show a human-readable label alongside the internal antenna identifier.

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

The Pan slider in the Audio tab now uses a centre-anchored fill. The slider groove fills from the centre outward — blue accent to the right of centre when the pan is right-heavy, and a background colour to the left of centre. When the pan is left-heavy, the groove fills from centre to the left in accent colour while the right side uses the background colour. This matches the behaviour of a stereo balance control where the meaningful zero is the midpoint. A small centre-mark dot is still painted on the groove at the midpoint.

### Theme support for buttons and badges

All VFO panel buttons and badges now honour the current theme. The button stylesheet has been updated to use theme tokens instead of hardcoded colours. The following tokens are declared for inspector coverage:
- `color.background.0`
- `color.background.1`
- `color.background.2`
- `color.text.primary`
- `color.text.label`
- `color.accent`
- `color.accent.bright`

The VFO panel is registered as a separate theming container under the `spectrum/vfo` scope. This means theme colour selections can be applied specifically to the VFO panel without affecting the rest of the spectrum display.

## Changes in v26.5.3

### Locked slice tuning behavior

When a slice is locked, the following tuning interactions on the VFO panel are now blocked:

- **Scroll-wheel tuning**: Scrolling the mouse wheel over the collapsed or expanded VFO panel no longer changes the frequency. A `tuneBlockedByLock` notification is shown.
- **Direct frequency entry**: If you are in the middle of typing a frequency and the slice becomes locked, the direct entry is canceled and the display reverts to the locked frequency.

The lock overlay (padlock icon) is managed centrally by `SliceModel` and clears automatically when the slice is unlocked (#2983).

### XVTR band direct entry improvements

When entering a frequency directly on the VFO panel, the parser now correctly handles explicit MHz entries above 54 MHz even when not on an XVTR band. If you type a value in MHz format (e.g., `144.200`), it is accepted up to 50,000 MHz without being misinterpreted as kHz or Hz. The 3-digit-band convenience insertion for bare integers on 2m/70cm bands still applies only when the slice frequency is between 100 MHz and 999 MHz.

### Tab height optimization

The VFO panel tab stack now uses a custom `TabStack` widget that reports only the current page's preferred size. Previously, when the DSP tab was taller than the Mode tab (e.g., when the digital filter container was visible in DIGU/DIGL mode), the VFO panel would overallocate height, causing a gap inside the Mode tab. This is now resolved.

## Changes in v26.5.2.1

### XVTR band frequency handling

When the slice is on an XVTR band, the maximum accepted frequency during direct entry has been increased from 450 MHz to 50,000 MHz to support microwave bands. The 3-digit-band insertion behavior (automatically inserting a decimal after the third digit for bare integers on 2m/70cm) now only fires when the slice frequency is between 100 MHz and 999 MHz. For bands like 23cm (1296 MHz), bare integers are interpreted as the frequency in MHz directly.

### Antenna menu improvements

Both the RX and TX antenna buttons now display a human-readable label in the menu alongside the internal antenna identifier. The menu uses `data()` internally for selection, matching on the full antenna string rather than the display label. Menu items also include tooltip and status tip text showing the raw antenna identifier.

### Slice badge rich text support

The slice badge now supports rich text format (`Qt::RichText`), allowing HTML formatting in certain cases (#2606).

## Changes in v26.5.1

### Squelch disabled in RTTY mode

The squelch button and slider are now automatically disabled when the slice is in a RTTY mode, in addition to the existing digital and CW mode restrictions. When the mode is RTTY, the squelch button is greyed out and cannot be toggled, and the squelch slider is greyed out and cannot be adjusted. If squelch was previously enabled, it is automatically turned off when switching to RTTY mode. This prevents squelch from gating weak FSK signals that external RTTY decoders need to receive via DAX (#2504).

## Changes in v