# VFO Panel

The VFO Panel is a floating per-slice control panel anchored to the VFO marker on the spectrum display. It provides quick access to the most frequently used per-slice settings — mode, filter presets, antenna selection, AF gain, pan, squelch, AGC, RIT/XIT, DSP noise reduction buttons, and DAX assignment — without leaving the spectrum view. It can collapse to a compact frequency-only strip.

## Opening the VFO Panel

1. Click the VFO marker flag on the spectrum display for the slice you want to adjust. The VFO panel opens anchored to the marker.
2. The panel opens in its expanded state. If it is collapsed to a frequency-only strip, click anywhere on it to expand it.

## Controls

The VFO Panel is organized into tabs. Each tab contains related controls.

### General controls

These controls appear on the main area of the VFO Panel, above the tabs.

| Control | Default | Behavior |
|---------|---------|----------|
| **RX antenna button** | N/A | Opens antenna selection menu for the receive antenna of this slice. |
| **TX antenna button** | N/A | Opens antenna selection menu for the transmit antenna of this slice. |
| **Frequency display** | N/A | Shows the current slice frequency. Click once to begin direct frequency entry; type MHz and press Enter or Tab. |
| **Filter width label** | N/A | Shows current filter bandwidth. Click to cycle through filter preset buttons in the Mode tab. Uses RxApplet::formatFilterWidth as the single source of truth, fixing a 0.1 kHz offset that affected SSB/digital mode readouts (#2197, v0.9.8). |
| **Marker thickness button** | 1 px | Cycles the VFO marker line through Off, 1 px, and 3 px. Persisted per slice (`Slice{N}_MarkerWidth`). |
| **Filter edges button** | shown | Toggles the filter edge lines on the spectrum passband. Persisted per slice (`Slice{N}_FilterEdgesHidden`). |
| **Collapse toggle** | expanded | Collapses the VFO panel to a compact frequency-only strip. Persisted per slice (`SliceFlagCollapsed_{N}`). |

### Audio tab

| Control | Default | Valid range | Behavior |
|---------|---------|-------------|----------|
| **AF Gain slider** | 100 | 0–100 | Sets the audio output level for this slice. Not persisted — reflects live radio state. |
| **Pan slider** | 50 | 0–100 | Sets left/right stereo pan for this slice. 50 = centre. The slider fill anchors from the centre outward, with a centre-mark dot painted on the groove to indicate the neutral position. |
| **Mute button** | off | — | Mutes audio output for this slice without changing the AF gain setting. |
| **Squelch button + slider** | off | 0–100 | Enables squelch for this slice. The adjacent slider sets the threshold. |
| **AGC combo** | FAST | FAST / MED / SLOW / OFF | Sets the AGC attack/release speed for this slice. |

### DSP tab

| Control | Default | Behavior |
|---------|---------|----------|
| **NR / NR2 / RN2 / NR4 / MNR / DFNR / BNR / NRL / NRS / RNN / NRF** | off | Enables the corresponding noise reduction algorithm for this slice. Button availability depends on radio series and build. |
| **ADSP button** | N/A | Opens the AetherDSP Settings dialog (client-side NR2 / NR4 / DFNR / RN2 / BNR / MNR). Same entry point as the Settings menu (v0.9.8). Styled like a radio-side DSP toggle but non-checkable. Click raises and focuses the modeless AetherDSP Settings dialog. |
| **AetherVoice button** | N/A | Toggles the Aetherial Audio Channel Strip — the unified TX/RX DSP suite (v0.9.8). Spans 2 columns in the 4-column DSP grid. Matches the existing menu / chain entry points for the strip. |

**DSP level slider:** When one or more leveled DSP algorithms are active, a shared level slider appears below the button grid. The slider label shows which algorithm it currently targets — it retargets automatically to the most recently enabled leveled algorithm. The numeric value is shown to the right of the slider. The slider is always present in the layout. When no leveled algorithm is active (or only RNN, or APF are on), the slider row fades out and does not respond to input.

Algorithms that expose the level slider: NR, NRL, NRS, NRF.

### Mode tab

| Control | Default | Valid range | Behavior |
|---------|---------|-------------|----------|
| **Mode combo** | USB | USB / LSB / CW / CWL / AM / SAM / DIGU / DIGL / FM / NFM / DFM / RTTY | Sets the demodulation mode for this slice. |
| **Filter preset buttons** | N/A | N/A | Applies a saved filter width preset. Right-click to save the current filter width into that slot. Persisted in `FilterPresets`. Custom lo/hi edges can be set per slot via right-click. |

### X/RIT tab

| Control | Default | Behavior |
|---------|---------|----------|
| **RIT / XIT buttons + labels** | off | Enables receiver (RIT) or transmitter (XIT) incremental tuning. The label shows the current offset; scroll-wheel adjusts in 10 Hz steps. |

### DAX tab

| Control | Default | Valid range | Behavior |
|---------|---------|-------------|----------|
| **DAX channel combo** | Off | Off / 1–8 | Assigns a DAX audio channel to this slice. |

## Indicators

| Indicator | States | Meaning |
|-----------|--------|---------|
| **TX badge** | TX (red) / hidden | Shown when this slice is the active transmit slice. |
| **SPLIT badge** | SPLIT (amber) / hidden | Shown when TX is assigned to a different slice than the active receive slice. |

## Frequency entry

The frequency display supports several entry formats:

- MHz format: `14.225`, `14.225.000`, `14225`, `14225.0`
- kHz format (HF only): `14225` (interprets bare integers as kHz when below 54000)
- Hz format (HF only): `14225000` (interprets as Hz when above 54000)
- Explicit MHz entry: any entry with a dot is treated as MHz. If the value exceeds 54 MHz, it is accepted as a VHF/UHF frequency even without an XVTR antenna.

On XVTR bands, bare integers like `145` are treated as MHz (3-digit-band convenience).

## Notes about squelch

Squelch is disabled (button and slider become non-functional) when the slice is in the following modes:
- Digital modes (DIGU, DIGL)
- RTTY
- CW modes (CW, CWL)

If squelch was active when switching to one of these modes, it is automatically turned off. The saved state is restored when switching back to a supported mode.

## Notes about VFO lock

When a slice is locked:
- The lock button shows a lock icon. Clicking it again unlocks the slice.
- Scrolling over the collapsed VFO panel or frequency display shows a LOCKED overlay and blocks frequency changes. The scroll event is consumed but the frequency does not change.
- Direct frequency entry is cancelled if initiated while the slice is locked.
- Unlocking the slice clears the LOCKED overlay.

### Theming support (v26.6.1)

The VFO Panel now uses the theme system for its visual styling:

- **Container scope:** The panel lives under the `spectrum/vfo` theme container scope, so its colour tokens inherit from the spectrum display overrides but can be customised independently.
- **Inspector coverage:** The following tokens are declared for inspection — clicking on the VFO flag, callsign badge, or signal meter strip in Inspect mode will surface these tokens in the hit list:
  - `color.background.0`
  - `color.background.1`
  - `color.background.2`
  - `color.text.primary`
  - `color.text.label`
  - `color.accent`
  - `color.accent.bright`
- **Pan slider:** The Pan slider uses a centre-anchored fill that paints from the centre outward in the accent colour. The groove fill on the opposite side of the handle uses the background colour. This matches the visual behaviour of L/R balance controls. A centre-mark dot at the neutral position helps the operator see the midpoint.
- **Mini button styling:** The mini (antenna) buttons use themed colours via `{{color.background.1}}` and `{{color.accent}}` tokens instead of hard-coded hex values.

## Tips

- Multiple noise reduction buttons can be active at the same time.
- You can open the AetherDSP applet from `Settings > AetherDSP Settings...` to configure client-side noise reduction algorithms.
- Right-click NR2, NR4, MNR, or DFNR to open the AetherDSP Settings dialog for that algorithm.

## Related

- [VFO Panel overview](overview.md)
- [Enable squelch from the VFO panel](enable-squelch-from-the-vfo-panel.md)