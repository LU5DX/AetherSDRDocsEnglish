# Set a custom filter edge from the VFO panel

The VFO panel's filter preset buttons let you save and recall filter widths quickly. Right-clicking a preset button opens a dialog where you can set exact low and high filter edge values for that slot. Use this when the built-in preset widths do not match your operating needs.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- The VFO panel must be open. If it is not visible, click the VFO marker flag on the spectrum display for the slice you want to adjust.
- The VFO panel must not be collapsed. If it shows only a frequency strip, click anywhere on it to expand it.
- Open the **Mode** tab inside the VFO panel so the filter preset buttons are visible.

## Steps

1. Click the VFO marker flag on the spectrum display to open the VFO panel for the target slice.
2. In the VFO panel, click the **Mode** tab to show the mode selector and filter preset buttons.
3. Right-click the filter preset button whose edges you want to customize. A context menu or dialog appears.
4. Enter the desired low edge and high edge values in the fields provided.
5. Confirm the entry to save the custom edges into that preset slot.

The preset button now applies your custom filter edges when clicked. The values are persisted in `FilterPresets`.

## What each control does

| Control                          | Behavior                                                                                                                                                                                                                                       | Default                                                                                                                 |
|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| RX antenna button                | Opens antenna selection menu for the receive antenna of this slice. Now uses per-slice antenna list from the radio when available; falls back to the global antenna list if empty. Each menu item shows its internal antenna name as a tooltip and status tip. | —                                                                                                                       |
| TX antenna button                | Opens antenna selection menu for the transmit antenna of this slice. Automatically filters out RX-only antenna ports. Uses `txAntennaOptions()` to determine available antennas. Each menu item shows its internal antenna name as a tooltip and status tip. | —                                                                                                                       |
| Frequency display                | Shows the current slice frequency. Click once to begin direct frequency entry; type MHz and press Enter or Tab. On XVTR bands, accepts frequencies up to 50000 MHz. For 2m/70cm (100–999 MHz range), a bare integer like 1446 is automatically converted to 144.6 MHz. On 23cm and microwave bands (≥1000 MHz), a bare integer is treated as MHz directly. | —                                                                                                                       |
| Filter width label               | Shows current filter bandwidth. Click to cycle through filter preset buttons in the Mode tab. Uses RxApplet::formatFilterWidth as the single source of truth, fixing a 0.1 kHz offset that affected SSB/digital mode readouts (#2197, v0.9.8). | —                                                                                                                       |
| Slice badge                      | Shows the slice letter (e.g., A, B) in a colored badge. Now supports HTML rendering for the slice letter (#2606). Click to select this slice.                                                                                                  | —                                                                                                                       |
| AF Gain slider (Audio tab)       | Sets the audio output level for this slice (0–100). Not persisted — reflects live radio state.                                                                                                                                                 | 100                                                                                                                     |
| Pan slider (Audio tab)           | Sets left/right stereo pan for this slice. 50 = centre.                                                                                                                                                                                        | 50                                                                                                                      |
| Mute button (Audio tab)          | Mutes audio output for this slice without changing the AF gain setting.                                                                                                                                                                        | off                                                                                                                     |
| Squelch button + slider (Audio tab) | Enables squelch for this slice. The adjacent slider sets the threshold (0–100). Squelch is disabled and forced off when the slice mode is DIGU, DIGL, RTTY, or any CW mode, as it is not meaningful for digital/RTTY audio fed via DAX or for CW where the radio locks squelch on (#2504). | off |
| AGC combo (Audio tab)            | Sets the AGC attack/release speed for this slice: FAST, MED, SLOW, or OFF.                                                                                                                                                                    | FAST                                                                                                                    |
| NR / NR2 / RN2 / NR4 / MNR / DFNR / BNR / NRL / NRS / RNN / NRF buttons (DSP tab) | Enables the corresponding noise reduction algorithm for this slice. Button availability depends on radio series and build. Right-click NR2, NR4, MNR, or DFNR to open the AetherDSP Settings dialog for that algorithm. | off |
| ADSP button (DSP tab)            | Opens the AetherDSP Settings dialog (client-side NR2 / NR4 / DFNR / RN2 / BNR / MNR). Same entry point as the Settings menu (v0.9.8). Styled like a radio-side DSP toggle but non-checkable. Click raises and focuses the modeless AetherDSP Settings dialog. | — |
| AetherVoice button (DSP tab)     | Toggles the Aetherial Audio Channel Strip — the unified TX/RX DSP suite (v0.9.8). Spans 2 columns in the 4-column DSP grid. Matches the existing menu / chain entry points for the strip. | — |
| Mode combo (Mode tab)            | Sets the demodulation mode for this slice: USB, LSB, CW, CWL, AM, SAM, DIGU, DIGL, FM, NFM, DFM, RTTY.                                                                                                                                       | USB                                                                                                                    |
| Filter preset buttons (Mode tab) | Applies a saved filter width preset when clicked. Right-click to save the current filter width or set custom lo/hi edges for that slot. Persisted in FilterPresets.                                                                            | —                                                                                                                       |
| RIT / XIT buttons + labels (X/RIT tab) | Enables receiver (RIT) or transmitter (XIT) incremental tuning. The label shows the current offset; scroll-wheel adjusts in 10 Hz steps.                                                                                                | off                                                                                                                     |
| DAX channel combo (DAX tab)      | Assigns a DAX audio channel to this slice: Off or 1–8.                                                                                                                                                                                        | Off                                                                                                                     |
| Marker thickness button          | Cycles the VFO marker line through Off, 1 px, and 3 px. Persisted per slice.                                                                                                                                                                  | 1 px                                                                                                                    |
| Filter edges button              | Toggles the filter edge lines on the spectrum passband display. Persisted per slice.                                                                                                                                                           | shown                                                                                                                   |
| Collapse toggle                  | Collapses the VFO panel to a compact frequency-only strip. Persisted per slice.                                                                                                                                                                | expanded                                                                                                                |

### Indicators

| Label        | States                | Meaning                                                                 |
|--------------|-----------------------|-------------------------------------------------------------------------|
| TX badge     | TX (red) / hidden     | Shown when this slice is the active transmit slice.                     |
| SPLIT badge  | SPLIT (amber) / hidden | Shown when TX is assigned to a different slice than the active receive slice. |

### DSP tab buttons

Starting in v0.9.7, the **DSP tab** shows only radio-supplied noise reduction buttons. The client-side algorithms (NR2, NR4, MNR, BNR, DFNR, RN2) have moved to the spectrum overlay menu and the AetherDSP applet; toggle them there.

The buttons available in the DSP tab are:

| Button | Algorithm |
|---|---|
| NR | Noise reduction |
| NB | Noise blanker |
| ANF | Automatic notch filter |
| APF | Audio peak filter (CW mode only) |
| NRL | Noise reduction level |
| NRS | Spectral subtraction |
| RNN | RNN noise reduction |
| NRF | Spectral noise filter |
| ANFL | LMS notch filter |
| ANFT | FFT notch filter |
| ADSP | Opens the AetherDSP Settings dialog (client-side algorithms) |
| AetherVoice | Opens the Aetherial Audio Channel Strip (unified TX/RX DSP suite) |

#### DSP level slider

When one or more radio-side DSP functions that support a level control are enabled, a shared level slider appears below the button grid. The slider label and value update to reflect the most recently enabled function. The slider is always present in the layout but fades out when no supported DSP function is active. Drag the slider to set the level (0–100) for the targeted function.

Functions that the level slider can target: NR, NB, ANF, NRL, NRS, NRF, ANFL.

Functions that do not target the level slider: RNN, ANFT, APF.

## Tips

- To verify the active filter edges on the spectrum, confirm that the filter edges button is in its default shown state. If the edge lines are hidden, toggle the filter edges button to make them visible again.
- Right-clicking a preset button saves the *current* filter width into that slot as an alternative to typing edge values manually. Use this for a quick capture of a filter you have already dialed in.
- To access NR2, NR4, MNR, BNR, DFNR, or RN2, right-click the spectrum display to open the overlay menu, or open the AetherDSP applet.
- The ADSP button and AetherVoice button are placed in the DSP tab button grid alongside the radio-side DSP toggles. They are non-checkable — clicking ADSP raises the AetherDSP Settings dialog, and clicking AetherVoice opens the Aetherial Audio Channel Strip.
- Squelch is automatically disabled and forced off when you switch to DIGU, DIGL, RTTY, or any CW mode. To re-enable squelch, switch to a voice mode (USB, LSB, AM, SAM, FM, NFM, DFM).

## Related

- [Apply a filter width preset from the VFO panel](apply-a-filter-width-preset-from-the-vfo-panel.md)
- [Hide or show filter edge lines on the spectrum](hide-or-show-filter-edge-lines-on-the-spectrum.md)
- [Change mode from the VFO panel](change-mode-from-the-vfo-panel.md)