# Tune the radio by typing a frequency into the VFO panel

Direct frequency entry lets you jump to an exact frequency without clicking around the panadapter. Type a value in MHz into the VFO panel's frequency display and press Enter.

## Before you start

- AetherSDR must be connected to your FLEX-8600 radio.
- The VFO panel for the target slice must be open. If it is not visible, click the VFO marker flag for that slice on the spectrum display.
- The slice must not be locked. A locked slice ignores tune commands.

## Steps

1. Click the **Frequency display** once. The display enters direct entry mode.
2. Type the desired frequency in MHz.
3. Press **Enter** or **Tab** to apply. The slice retunes immediately.

### What happens when you start typing on a locked slice

If you click the **Frequency display** while the slice is locked, AetherSDR immediately exits direct entry mode without applying the frequency. The display shows a brief **LOCKED** overlay, and the slice remains on its current frequency. Unlock the slice first, then enter the frequency.

## What each control does

| Control                        | Behavior                                                                                                                                                                                                 |
|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **RX antenna button**          | Opens antenna selection menu for the receive antenna of this slice. Menu items use the slice's dedicated RX antenna list when available, falling back to the global antenna list. Right-click available. |
| **TX antenna button**          | Opens antenna selection menu for the transmit antenna of this slice. Filters out RX-only antenna ports. Menu items use the slice's dedicated TX antenna options when available. Right-click available.   |
| **Frequency display**          | Shows the current slice frequency. Click once to begin direct entry; type MHz and press Enter or Tab to apply. Uses `FreqLineEdit` for enhanced accessibility. Scroll the mouse wheel over the display to step-tune up or down by the current step size. |
| **Slice badge**                | Shows the slice letter (e.g., A, B, C) in a colored badge. Supports rich text formatting for HTML rendering (#2606). Right-click opens the slice color picker.                                          |
| **Filter width label**         | Shows current filter bandwidth. Click to cycle through filter preset buttons in the Mode tab. Uses `RxApplet::formatFilterWidth` as the single source of truth, fixing a 0.1 kHz offset that affected SSB/digital mode readouts (#2197, v0.9.8). |
| **AF Gain slider (Audio tab)** | Sets the audio output level for this slice. Default: 100. Range: 0-100. Not persisted — reflects live radio state.                                                                                      |
| **Pan slider (Audio tab)**     | Sets left/right stereo pan for this slice. Default: 50. Range: 0-100. 50 = centre. The slider fill anchors from the centre outward, showing a centre-mark dot on the groove at the neutral position.   |
| **Mute button (Audio tab)**    | Toggle button. Mutes audio output for this slice without changing the AF gain setting. Default: off. Right-click the Audio tab label to toggle mute directly.                                            |
| **Squelch button + slider (Audio tab)** | Toggle button. Enables squelch for this slice. The adjacent slider sets the threshold. Default: off. Range: 0-100.                                                                             |
| **AGC combo (Audio tab)**      | Sets the AGC attack/release speed for this slice. Options: FAST, MED, SLOW, OFF. Default: FAST.                                                                                                          |
| **Mode combo (Mode tab)**      | Sets the demodulation mode for this slice. Options: USB, LSB, CW, CWL, AM, SAM, DIGU, DIGL, FM, NFM, DFM, RTTY. Default: USB.                                                                            |
| **Filter preset buttons (Mode tab)** | Applies a saved filter width preset. Right-click to save the current filter width into that slot. Custom lo/hi edges can be set per slot via right-click. Persisted in `FilterPresets`.         |
| **RIT / XIT buttons + labels (X/RIT tab)** | Toggle buttons. Enables receiver (RIT) or transmitter (XIT) incremental tuning. The label shows the current offset; scroll-wheel adjusts in 10 Hz steps. Default: off.                         |
| **DAX channel combo (DAX tab)** | Assigns a DAX audio channel to this slice. Options: Off, 1-8. Default: Off.                                                                                                                            |
| **Marker thickness button**    | Cycles the VFO marker line through Off, 1 px, and 3 px. Persisted per slice in `Slice{N}_MarkerWidth`.                                                                                                  |
| **Filter edges button**        | Toggle button. Toggles the filter edge lines on the spectrum passband. Persisted per slice in `Slice{N}_FilterEdgesHidden`. Default: shown.                                                               |
| **Collapse toggle**            | Collapses the VFO panel to a compact frequency-only strip. In collapsed mode, scrolling anywhere on the strip tunes by the current step size. Persisted per slice in `SliceFlagCollapsed_{N}`.           |

## DSP tab controls

The DSP tab contains toggle buttons for noise reduction and filtering algorithms supplied by the radio, plus client-side launcher buttons. The following buttons are available in the VFO panel DSP grid:

| Button | Description |
|---|---|
| **NR** | Noise reduction. |
| **NB** | Noise blanker. |
| **ANF** | Automatic notch filter. |
| **APF** | Audio peak filter. Visible only when the slice is in CW mode. |
| **NR2 / NR4 / RN2 / BNR / MNR / DFNR / NRL / NRS / RNN / NRF** | Various noise reduction algorithms. Button availability depends on radio series and build. Right-click NR2, NR4, MNR, or DFNR to open the AetherDSP Settings dialog for that algorithm. |
| **ADSP** | Push button. Opens the AetherDSP Settings dialog (client-side NR2 / NR4 / DFNR / RN2 / BNR / MNR). Same entry point as the Settings menu (v0.9.8). Styled like a radio-side DSP toggle but non-checkable. |
| **AetherVoice** | Push button. Toggles the Aetherial Audio Channel Strip — the unified TX/RX DSP suite (v0.9.8). Spans 2 columns in the 4-column DSP grid. |

All radio-side DSP buttons default to off.

### DSP level slider

When one or more radio-side DSP algorithms that support a level control are active, a level slider appears below the DSP button grid. The slider label shows the name of the most recently enabled algorithm that supports leveling (for example, **NR**, **NB**, **ANF**, **NRL**, **NRS**, **NRF**, or **ANFL**). The adjacent numeric readout shows the current value.

- Drag the slider to set the level for the targeted algorithm (0–100).
- The slider retargets automatically when you enable a different leveled algorithm.
- When no leveled algorithm is active, the slider row fades out but remains in position so the button grid does not shift.
- In v0.9.8, the slider is now present on launch for any DSP that was saved as enabled in the radio's profile, without requiring manual toggling.

### Right-click actions on DSP buttons

Right-click any of the following buttons to open the AetherDSP Settings dialog for that algorithm:
- **NR2**, **NR4**, **MNR**, **DFNR** (accessible via ADSP button)

## S-meter and Smart Meter

The VFO panel displays an S-meter below the frequency display (or below the RADE info row, if RADE is active). The S-meter uses a stacked approach, with a spacer widget that adapts to the meter height.

When the Smart Meter feature is enabled (via `SmartMeterEnabled` in `DisplaySettings`), the S-meter is replaced by a `SmartMtrWidget`. This widget maintains an aspect ratio to drive the overall strip height via `heightForWidth()`. The elevation shadow for the VFO flag is rendered by a separate `FlagShadow` widget to avoid re-blurring on live meter repaints.

- **S-meter**: Shows signal strength in S-units and dB over S9. The spacer widget prevents layout shifts when meter height varies.
- **Smart Meter**: A graphical meter with configurable scales and averaging. Enable it in `DisplaySettings`. The meter controls the VFO panel strip height to maintain its aspect ratio.

## Adaptive filter controls

When the **Adaptive Filters** feature is available (e.g., for KiwiSDR or certain DSP modes), `AdaptiveFilterControls` are shown below the mode/filter presets area. These controls allow real-time adjustment of adaptive filter parameters and are integrated into the VFO panel layout.

## Tab bar

The VFO panel uses a tab bar with the following labels: **Audio** (default), **Mode**, **DSP**, **X/RIT**, and **DAX**. Click a tab label to switch to that tab's content.

- Tab labels are now implemented as `QPushButton` buttons with keyboard focus support. Use Tab/Shift+Tab to navigate between tabs.
- The active tab is highlighted with a cyan underline (`#00b4d8`). Inactive tabs have a transparent underline and use muted color `#6888a0`.
- Right-click the **Audio** tab label to toggle mute for the current slice.

## RADE info row

When RADE (Radio Aided Direction Finding Engine) is active, an information row appears below the frequency display and above the S-meter. It shows:

| Element | Description |
|---|---|
| **Callsign** | The callsign of the station RADE is tracking. |
| **SNR** | Signal-to-noise ratio for the tracked station. |
| **Offset** | Frequency offset from the slice center frequency. |

The RADE info row is hidden when RADE is inactive. This feature is only available in builds compiled with RADE support.

## Indicators

| Indicator | States | Meaning |
|---|---|---|
| **TX badge** | TX (red), hidden | Shown when this slice is the active transmit slice. |
| **SPLIT badge** | SPLIT (amber), hidden | Shown when TX is assigned to a different slice than the active receive slice. The badge text changes to **SWAP** when the split pair can be exchanged. |

The SPLIT badge uses increased contrast for better visibility: default color `rgba(255,255,255,120)`, hover color `rgba(255,255,255,180)`.

## Antenna selection

The RX and TX antenna buttons show the currently selected antenna for each path. Click either button to open a menu of available antenna selections.

### RX antenna menu

- Uses the slice's dedicated RX antenna list when available (for example, on radios that provide separate RX antenna ports per slice).
- Falls back to the global antenna list when no slice-specific list is available.
- Each menu item shows a human-readable label with antenna numbers extracted from the raw identifier.
- Tooltips show the raw antenna identifier.

### TX antenna menu

- Filters out RX-only antenna ports automatically.
- Uses the slice's dedicated TX antenna options when available.
- TX antenna detection looks for identifiers starting with "ANT", "TX", or "XVTR", and excludes identifiers starting with "RX".
- Each menu item shows a human-readable label with antenna numbers extracted from the raw identifier.
- Tooltips show the raw antenna identifier.

## Frequency entry on XVTR bands

When operating on transverter (XVTR) bands, the frequency entry logic adapts automatically:

- **3-digit band convenience**: On 2m/70cm bands (100-999 MHz range), a bare integer like 1446 is interpreted as 144.6 MHz. The decimal is inserted after the third digit.
- **Microwave bands**: For 23cm and higher bands (1000+ MHz), a bare integer is treated as the frequency in MHz directly (e.g., 1296 means 1296 MHz, not 129.6 MHz).
- **Explicit MHz entry on non-XVTR bands**: If you type a frequency in MHz that is above 54 MHz (for example, typing "146.520"), AetherSDR now detects the explicit MHz entry and treats the value as MHz rather than attempting kHz/Hz fallback parsing. This allows direct frequency entry for VHF/UHF bands even when the radio profile does not report an XVTR antenna.
- The maximum allowed frequency is 50000 MHz for XVTR bands and for explicit MHz entries above 54 MHz. For all other entries, the maximum is 54 MHz.

## Frequency entry parsing details

When you type a frequency value, AetherSDR parses it as follows:

- **Periods in the input**: Multiple periods (e.g., "14.225.000") are normalized to a single decimal point. The value is then interpreted as MHz.
- **Values ≤ 54 MHz (HF bands)**:
  - Values > 54000 are treated as Hz and divided by 1,000,000.
  - Values > 54 are treated as kHz and divided by 1000.
  - Values ≤ 54 are treated as MHz directly.
- **Values > 54 MHz (VHF/UHF/SHF bands)**:
  - If you explicitly typed MHz (by including a decimal point or using the "14.225.000" format), the value is used as MHz directly.
  - If you typed a bare integer, 3-digit-band convenience parsing applies (see above).
  - The maximum allowed value is 50000 MHz.

## Mouse wheel tuning

The scroll wheel tunes the slice when the pointer is over the **Frequency display**, stepping by the slice's current step size. The wheel direction follows the **Reverse mouse wheel** setting in Interaction Settings (#3302). When enabled, scrolling up decreases frequency