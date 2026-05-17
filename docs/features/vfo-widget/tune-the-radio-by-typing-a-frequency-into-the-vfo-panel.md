# Tune the radio by typing a frequency into the VFO panel

Direct frequency entry lets you jump to an exact frequency without clicking around the panadapter. Type a value in MHz into the VFO panel's frequency display and press Enter.

## Before you start

- AetherSDR must be connected to your FLEX-8600 radio.
- The VFO panel for the target slice must be open. If it is not visible, click the VFO marker flag for that slice on the spectrum display.

## Steps

1. Click the **Frequency display** once. The display enters direct entry mode.
2. Type the desired frequency in MHz.
3. Press **Enter** or **Tab** to apply. The slice retunes immediately.

## What each control does

| Control                      | Behavior                                                                                                                                                                                                 |
|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **RX antenna button**        | Opens antenna selection menu for the receive antenna of this slice. Menu items use the slice's dedicated RX antenna list when available, falling back to the global antenna list. Right-click available. |
| **TX antenna button**        | Opens antenna selection menu for the transmit antenna of this slice. Filters out RX-only antenna ports. Menu items use the slice's dedicated TX antenna options when available. Right-click available.   |
| **Frequency display**        | Shows the current slice frequency. Click once to begin direct entry; type MHz and press Enter or Tab to apply. Scroll the mouse wheel over the display to step-tune up or down by the current step size. |
| **Slice badge**              | Shows the slice letter (e.g., A, B, C) in a colored badge. Supports rich text formatting for HTML rendering (#2606). Right-click opens the slice color picker.                                          |
| **Filter width label**       | Shows current filter bandwidth. Click to cycle through filter preset buttons in the Mode tab. Uses `RxApplet::formatFilterWidth` as the single source of truth, fixing a 0.1 kHz offset that affected SSB/digital mode readouts (#2197, v0.9.8). |
| **AF Gain slider (Audio tab)** | Sets the audio output level for this slice. Default: 100. Range: 0-100. Not persisted — reflects live radio state.                                                                                      |
| **Pan slider (Audio tab)**   | Sets left/right stereo pan for this slice. Default: 50. Range: 0-100. 50 = centre.                                                                                                                       |
| **Mute button (Audio tab)**  | Toggle button. Mutes audio output for this slice without changing the AF gain setting. Default: off.                                                                                                     |
| **Squelch button + slider (Audio tab)** | Toggle button. Enables squelch for this slice. The adjacent slider sets the threshold. Default: off. Range: 0-100.                                                                             |
| **AGC combo (Audio tab)**    | Sets the AGC attack/release speed for this slice. Options: FAST, MED, SLOW, OFF. Default: FAST.                                                                                                          |
| **Mode combo (Mode tab)**    | Sets the demodulation mode for this slice. Options: USB, LSB, CW, CWL, AM, SAM, DIGU, DIGL, FM, NFM, DFM, RTTY. Default: USB.                                                                            |
| **Filter preset buttons (Mode tab)** | Applies a saved filter width preset. Right-click to save the current filter width into that slot. Custom lo/hi edges can be set per slot via right-click. Persisted in `FilterPresets`.         |
| **RIT / XIT buttons + labels (X/RIT tab)** | Toggle buttons. Enables receiver (RIT) or transmitter (XIT) incremental tuning. The label shows the current offset; scroll-wheel adjusts in 10 Hz steps. Default: off.                         |
| **DAX channel combo (DAX tab)** | Assigns a DAX audio channel to this slice. Options: Off, 1-8. Default: Off.                                                                                                                            |
| **Marker thickness button**  | Cycles the VFO marker line through Off, 1 px, and 3 px. Persisted per slice in `Slice{N}_MarkerWidth`.                                                                                                  |
| **Filter edges button**      | Toggle button. Toggles the filter edge lines on the spectrum passband. Persisted per slice in `Slice{N}_FilterEdgesHidden`. Default: shown.                                                               |
| **Collapse toggle**          | Collapses the VFO panel to a compact frequency-only strip. In collapsed mode, scrolling anywhere on the strip tunes by the current step size. Persisted per slice in `SliceFlagCollapsed_{N}`.           |

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
| **SPLIT badge** | SPLIT (amber), hidden | Shown when TX is assigned to a different slice than the active receive slice. |

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
- The maximum allowed frequency on XVTR bands is 50000 MHz.

## Tips

- If the panel is collapsed to the frequency-only strip, click anywhere on it to expand it so the **Frequency display** is accessible for direct entry.
- The scroll wheel also tunes the slice when the pointer is over the **Frequency display**, stepping by the slice's current step size. On macOS, inertial scroll events are ignored to prevent unintended tuning after a gesture ends.
- Right-click the slice badge to change its color.

## Troubleshooting

- **Typing has no effect** — Check that the slice is not locked. A locked slice ignores tune commands. Unlock it before entering a frequency.
- **The VFO panel is not visible** — Click the VFO marker flag for the desired slice on the spectrum display to open the panel.
- **NR2, NR4, MNR, BNR, DFNR, or RN2 buttons are missing from the DSP tab** — These client-side modules were moved out of the VFO panel in v0.9.7. Toggle them from the spectrum overlay menu, the ADSP button on the DSP tab, or the AetherDSP applet.
- **The DSP level slider is faded and does not respond to clicks** — The slider is inactive when no radio-side DSP algorithm that supports leveling is currently enabled. Enable NR, NB, ANF, NRL, NRS, NRF, or ANFL to activate the slider.
- **The DSP level slider is missing on launch even though a DSP was enabled in the radio's saved profile** — This issue was fixed in v0.9.8. Update to the latest version.
- **RADE info row does not appear** — Verify your build includes RADE support. The row only compiles when `HAVE_RADE` is defined.
- **Antenna menu shows duplicate or confusing labels** — The menu now uses human-readable labels extracted from raw antenna identifiers. The raw identifier is still available in the tooltip.

## Related

- [VFO Panel overview](overview.md)
- [Collapse the VFO panel to frequency-only view](collapse-the-vfo-panel-to-frequency-only-view.md)
- [Change mode from the VFO panel](change-mode-from-the-vfo-panel.md)
- [Enable RIT or XIT offset from the VFO panel](enable-rit-or-xit-offset-from-the-vfo-panel.md)