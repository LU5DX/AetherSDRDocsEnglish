# Mute audio for a slice from the VFO panel

Silence the audio output of a single slice without changing its AF Gain setting. Use this when you want to suppress a slice temporarily and restore its previous volume with one click.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- The VFO panel for the target slice must be open. If it is collapsed to a frequency-only strip, click anywhere on it to expand it first.

## Steps

1. Click the VFO marker flag on the spectrum display for the slice you want to mute. The VFO panel opens anchored to the marker.
2. Click **Audio** to select the Audio tab inside the VFO panel.
3. Click **Mute**. The button activates, and audio output for the slice stops. The AF Gain slider value is not changed.
4. To restore audio, click **Mute** again. The button deactivates and audio resumes at the previous AF Gain level.

## What each control does

| Control | Kind | Default | Behavior | Notes |
|---------|------|---------|----------|-------|
| RX antenna button | Push button | — | Opens antenna selection menu for the receive antenna of this slice. | |
| TX antenna button | Push button | — | Opens antenna selection menu for the transmit antenna of this slice. | |
| Frequency display | Indicator | — | Shows the current slice frequency. Click once to begin direct frequency entry; type MHz and press Enter or Tab. | |
| Filter width label | Indicator | — | Shows current filter bandwidth. Click to cycle through filter preset buttons in the Mode tab. Uses `RxApplet::formatFilterWidth` as the single source of truth. | Fixes a 0.1 kHz offset that affected SSB/digital mode readouts (#2197, v0.9.8). |
| AF Gain slider (Audio tab) | Slider | 100 | Sets the audio output level for this slice. | Not persisted — reflects live radio state. |
| Pan slider (Audio tab) | Slider | 50 | Sets left/right stereo pan for this slice. 50 = centre. | |
| Mute button (Audio tab) | Toggle button | Off | Mutes audio output for this slice without changing the AF gain setting. | |
| Squelch button + slider (Audio tab) | Toggle button | Off | Enables squelch for this slice. The adjacent slider sets the threshold. | Squelch is disabled in digital, RTTY, and CW modes. In digital and RTTY modes, audio feeds external decoders via DAX and squelch is not meaningful — it also gates weak FSK signals. In CW mode, the radio locks squelch on at a fixed level and rejects changes. |
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
| Collapse toggle | Toggle button | Expanded | Collapses the VFO panel to a compact frequency-only strip. | Persisted per slice in `SliceFlagCollapsed_{N}`. |

## DSP tab changes in v0.9.7 (refined in v0.9.8)

The DSP tab now shows only radio-supplied noise reduction algorithms. The buttons for NR2, RN2, BNR, NR4, MNR, and DFNR have been removed from the VFO panel. Those algorithms are client-side modules; access them through the spectrum overlay menu or the AetherDSP applet.

The buttons present in the DSP tab are:

| Button | Algorithm |
|---|---|
| NR | Noise reduction |
| NB | Noise blanker |
| ANF | Automatic notch filter |
| APF | Audio peaking filter (CW mode only) |
| NRL | Noise reduction level |
| NRS | Spectral subtraction |
| RNN | RNN noise reduction |
| NRF | Spectral noise filter |
| ANFL | LMS notch filter |
| ANFT | FFT notch filter |

A shared **DSP Level** row appears below the button grid. It contains a slider and a numeric readout. The slider retargets automatically to whichever leveled DSP algorithm was most recently enabled. The label to the left of the slider shows the active target (for example, **NR** or **NB**). When no leveled DSP algorithm is active — or when only RNN, ANFT, or APF is on — the row fades out and slider interaction has no effect. The row remains in the layout at all times; it does not shift the button grid when it fades in or out.

Algorithms that support a level via this slider: NR, NB, ANF, NRL, NRS, NRF, ANFL.

**Note:** In v0.9.8, the DSP level slider now appears on launch for any DSP algorithm that was enabled in the radio's saved profile. Previously, it was missing until the user manually toggled the DSP button.

## Squelch behavior by mode

The squelch button and slider are automatically disabled in certain modes:

- **Digital modes (DIGU, DIGL):** Squelch is disabled because audio feeds external decoders via DAX — squelch is not meaningful and gates weak FSK signals.
- **RTTY:** Squelch is disabled for the same reasons as digital modes, resolving an issue where squelch would gate weak FSK signals (#2504).
- **CW:** Squelch is disabled because the radio locks squelch on at a fixed level and rejects changes.

When squelch is disabled and was previously enabled, the system automatically turns squelch off for the slice and saves its state. When you switch back to a voice mode, squelch may be restored.

## Tips

- Muting a slice does not reset the AF Gain slider. When you unmute, audio returns at the same level it was before.
- If you want to silence a slice permanently rather than temporarily, drag the AF Gain slider to 0 instead.
- To access NR2, RN2, BNR, NR4, MNR, or DFNR, right-click the spectrum display to open the overlay menu, or open the AetherDSP applet.
- The ADSP and AetherVoice buttons in the DSP tab are client-side launchers. They are styled like radio-side DSP toggles but are not checkable.
- Use the **ADSP** button to open the AetherDSP Settings dialog for client-side noise reduction algorithms.
- Use the **AetherVoice** button to open the Aetherial Audio Channel Strip for unified TX/RX DSP.
- Squelch is automatically disabled in digital, RTTY, and CW modes. If you switch to one of these modes while squelch is on, the system will turn it off and save its state for restoration when you return to a voice mode.

## Related

- [Adjust AF gain and pan from the VFO panel](adjust-af-gain-and-pan-from-the-vfo-panel.md)
- [Enable squelch from the VFO panel](enable-squelch-from-the-vfo-panel.md)
- [Collapse the VFO panel to frequency-only view](collapse-the-vfo-panel-to-frequency-only-view.md)