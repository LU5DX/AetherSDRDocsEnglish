# Change mode from the VFO panel

Use the VFO panel's Mode tab to switch the demodulation mode for any slice — for example, from USB to CW or FM — without leaving the spectrum view.

## Before you start

- AetherSDR must be connected to the radio. The VFO panel requires an active radio connection.
- The VFO panel must be open. If it is not visible, click the VFO marker flag on the spectrum display for the slice you want to change.

## Steps

1. Click the VFO marker flag on the spectrum display for the target slice. The VFO panel opens, anchored to the left of the marker.
2. Click the **Mode** tab inside the VFO panel.
3. Click the **Mode combo** and select the desired mode from the list.

## What each control does

| Control                      | Default                                                                                                                               | Valid values                                                                                                            |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Mode combo                   | USB                                                                                                                                   | USB, LSB, CW, CWL, AM, SAM, DIGU, DIGL, FM, NFM, DFM, RTTY                                                              |
| Filter preset buttons        | —                                                                                                                                     | Saved filter width presets                                                                                              |
| ADSP button (DSP tab)        | Opens the AetherDSP Settings dialog (client-side NR2 / NR4 / DFNR / RN2 / BNR / MNR). Same entry point as the Settings menu (v0.9.8). | Styled like a radio-side DSP toggle but non-checkable. Click raises and focuses the modeless AetherDSP Settings dialog. |
| AetherVoice button (DSP tab) | Toggles the Aetherial Audio Channel Strip — the unified TX/RX DSP suite (v0.9.8).                                                     | Spans 2 columns in the 4-column DSP grid. Matches the existing menu / chain entry points for the strip.                 |
| RX antenna button            | —                                                                                                                                     | Opens antenna selection menu for the receive antenna of this slice.                                                     |
| TX antenna button            | —                                                                                                                                     | Opens antenna selection menu for the transmit antenna of this slice.                                                    |
| Frequency display            | —                                                                                                                                     | Shows the current slice frequency. Click once to begin direct frequency entry; type MHz and press Enter or Tab.         |
| Filter width label           | —                                                                                                                                     | Shows current filter bandwidth. Click to cycle through filter preset buttons. Uses RxApplet::formatFilterWidth.        |
| AF Gain slider (Audio tab)   | 100                                                                                                                                   | 0-100. Sets the audio output level for this slice.                                                                      |
| Pan slider (Audio tab)       | 50                                                                                                                                    | 0-100. Sets left/right stereo pan for this slice. 50 = centre.                                                          |
| Mute button (Audio tab)      | off                                                                                                                                   | Toggle. Mutes audio output for this slice without changing the AF gain setting.                                         |
| Squelch button + slider (Audio tab) | off                                                                                                                           | 0-100. Enables squelch for this slice. The adjacent slider sets the threshold.                                          |
| AGC combo (Audio tab)        | FAST                                                                                                                                  | FAST, MED, SLOW, OFF. Sets the AGC attack/release speed for this slice.                                                 |
| RIT / XIT buttons + labels (X/RIT tab) | off                                                                                                                           | Toggle. Enables receiver (RIT) or transmitter (XIT) incremental tuning. Scroll-wheel adjusts in 10 Hz steps.            |
| DAX channel combo (DAX tab)  | Off                                                                                                                                   | Off, 1-8. Assigns a DAX audio channel to this slice.                                                                    |
| Marker thickness button      | 1 px                                                                                                                                  | Off, 1 px, 3 px. Cycles the VFO marker line thickness. Persisted per slice.                                             |
| Filter edges button          | shown                                                                                                                                | Toggle. Hides or shows the filter edge lines on the spectrum passband. Persisted per slice.                             |
| Collapse toggle              | expanded                                                                                                                              | Toggle. Collapses the VFO panel to a compact frequency-only strip. Persisted per slice.                                 |

**Mode combo** — sets the demodulation mode for the slice. Selecting a new mode takes effect immediately on the radio.

**Filter preset buttons** — appear on the same Mode tab. Each button applies a saved filter width. Right-click a button to save the current filter width into that slot. Presets are persisted in `FilterPresets`.

**Filter width label** — shows the current filter bandwidth. Click it to cycle through the filter preset buttons on the Mode tab. Uses `RxApplet::formatFilterWidth` as the single source of truth, fixing a 0.1 kHz offset that affected SSB/digital mode readouts (#2197, v0.9.8).

## DSP tab controls

The DSP tab shows buttons for noise reduction and filtering algorithms supplied directly by the radio, plus client-side launcher buttons. The following buttons are available:

| Button | Description |
|---|---|
| NR | Noise reduction |
| NB | Noise blanker |
| ANF | Automatic notch filter |
| APF | Audio peak filter (visible in CW mode only) |
| NRL | Noise reduction level |
| NRS | Spectral subtraction |
| RNN | RNN noise reduction |
| NRF | Spectral noise filter |
| ANFL | LMS notch filter |
| ANFT | FFT notch filter |
| NR2 | Opens the NR2 algorithm in the AetherDSP Settings dialog (right-click) |
| NR4 | Opens the NR4 algorithm in the AetherDSP Settings dialog (right-click) |
| MNR | Opens the MNR algorithm in the AetherDSP Settings dialog (right-click) |
| DFNR | Opens the DFNR algorithm in the AetherDSP Settings dialog (right-click) |
| BNR | Opens the BNR algorithm in the AetherDSP Settings dialog (right-click) |
| RN2 | Opens the RN2 algorithm in the AetherDSP Settings dialog (right-click) |
| ADSP | Opens the AetherDSP Settings dialog (same entry point as the Settings menu) |
| AetherVoice | Toggles the Aetherial Audio Channel Strip — the unified TX/RX DSP suite |

All radio-side buttons default to off and toggle the corresponding algorithm on or off for the active slice.

> **Note:** The client-side noise reduction modules NR2, NR4, MNR, BNR, DFNR, and RN2 are accessible via right-click on the DSP tab to open the AetherDSP Settings dialog, or from the spectrum overlay menu and the AetherDSP applet.

### DSP level slider

When one or more leveled DSP algorithms (NR, NB, ANF, NRL, NRS, NRF, or ANFL) are active, a level slider appears below the DSP button grid. The slider label shows which algorithm is currently targeted — the most recently enabled leveled DSP. The numeric value is displayed to the right of the slider.

- Range: 0–100.
- The slider retargets automatically when you enable a different leveled DSP button.
- When no leveled DSP is active, or when only RNN, ANFT, or APF is on, the slider row fades out. It remains in the layout at all times to prevent the button grid from shifting.
- On launch, any DSP enabled in the radio's saved profile now properly shows the level slider without requiring manual toggling (#startup-slider, v0.9.8).

## Squelch behavior by mode

The squelch button and slider in the Audio tab are automatically disabled in certain modes where squelch is not meaningful:

- **Digital modes (DIGU, DIGL)** — Audio feeds external decoders via DAX. Squelch is disabled.
- **RTTY mode** — Like digital modes, audio feeds external decoders. Squelch is disabled to prevent gating weak FSK signals (#2504, v26.5.1).
- **CW mode** — The radio locks squelch on at a fixed level and rejects changes. Squelch is disabled.

When squelch is disabled and was previously enabled, it is automatically turned off to avoid a stuck squelch state. The `m_savedSquelchOn` flag preserves the previous state so it can be restored when switching back to a voice mode.

## Tips

- Changing mode may alter the active filter passband. Check the filter width label in the header row after switching modes, and apply a filter preset if needed.
- The filter width label in the VFO panel header shows the current bandwidth. Click it to cycle through the filter preset buttons on the Mode tab.
- To access NR2, NR4, MNR, BNR, DFNR, or RN2, right-click the DSP tab button for that algorithm, or right-click the spectrum display and open the overlay menu, or open the AetherDSP applet.
- The marker thickness and filter edges buttons are persisted per slice in `Slice{N}_MarkerWidth` and `Slice{N}_FilterEdgesHidden` settings keys.
- Press the collapse toggle next to the frequency display to reduce the panel to a compact frequency-only strip. The state is persisted per slice.

## Related

- [Apply a filter width preset from the VFO panel](apply-a-filter-width-preset-from-the-vfo-panel.md)
- [Set a custom filter edge from the VFO panel](set-a-custom-filter-edge-from-the-vfo-panel.md)
- [VFO Panel overview](overview.md)