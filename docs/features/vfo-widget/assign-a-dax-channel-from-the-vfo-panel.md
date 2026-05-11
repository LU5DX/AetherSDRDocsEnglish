# Assign a DAX channel from the VFO panel

DAX (Digital Audio Exchange) routes a slice's received audio to a named audio channel on your computer. Use this procedure to assign or change the DAX channel for any slice directly from its VFO panel.

## Before you start

- AetherSDR must be connected to the radio. The VFO panel requires an active radio connection.
- The DAX audio bridge must be running. If it is not, enable it via `Settings > Autostart DAX with AetherSDR` and restart AetherSDR, or start it manually.
- The VFO panel for the target slice must be open and expanded. If it is collapsed to the frequency-only strip, click anywhere on it to expand it.

## Steps

1. Click the VFO marker flag on the spectrum display for the slice you want to configure. The VFO panel opens, anchored to the left of the marker.
2. Click the **DAX** tab inside the VFO panel.
3. Click the **DAX channel combo** and select a channel from the drop-down list.
4. To disable DAX routing for this slice, select **Off**.

## What each control does

| Control                      | Default                                                                                                                               | Valid values                                                                                                            |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| DAX channel combo            | Off                                                                                                                                   | Off, 1–8                                                                                                                |
| ADSP button (DSP tab)        | Opens the AetherDSP Settings dialog (client-side NR2 / NR4 / DFNR / RN2 / BNR / MNR). Same entry point as the Settings menu (v0.9.8). | Styled like a radio-side DSP toggle but non-checkable. Click raises and focuses the modeless AetherDSP Settings dialog. |
| AetherVoice button (DSP tab) | Opens the Aetherial Audio Channel Strip — the unified TX/RX DSP suite (v0.9.8).                                                       | Spans 2 columns in the 4-column DSP grid. Matches the existing menu / chain entry points for the strip.                 |

The DAX channel combo assigns a DAX audio channel to the current slice. Selecting a numbered channel routes the slice's received audio to that DAX channel. Selecting **Off** removes the assignment. This setting reflects live radio state and is not persisted locally by AetherSDR.

## Squelch behavior by mode

The squelch button and slider are automatically disabled in modes where squelch is not meaningful or supported. Starting in v26.5.1:

- **Squelch is disabled** in **Digital**, **RTTY**, and **CW** modes.
  - **Digital / RTTY**: Audio feeds external decoders via DAX; squelch is not meaningful and can gate weak FSK signals (issue #2504).
  - **CW**: The radio locks squelch on at a fixed level and rejects changes.
- If squelch was enabled when switching into one of these modes, the radio turns it off automatically. The saved squelch state is preserved and will be restored if you switch back to a supported mode.

## DSP tab controls

The DSP tab in the VFO panel contains radio-supplied noise reduction buttons and two client-side launcher buttons.

### Radio-side DSP buttons

The following radio-side DSP buttons appear in the DSP tab grid:

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

### Client-side launcher buttons

Two client-side launcher buttons appear at the end of the DSP grid:

| Button | Behavior |
|---|---|
| **ADSP** | Opens the AetherDSP Settings dialog (client-side NR2 / NR4 / DFNR / RN2 / BNR / MNR). Styled like a radio-side DSP toggle but non-checkable. Click raises and focuses the modeless AetherDSP Settings dialog. |
| **AetherVoice** | Toggles the Aetherial Audio Channel Strip — the unified TX/RX DSP suite. Spans 2 columns in the 4-column DSP grid. Matches the existing menu / chain entry points for the strip. |

### DSP level slider

A shared level slider row appears below the button grid. The slider adjusts the strength of whichever leveled DSP button was most recently turned on. The label to the left of the slider shows the active target (for example, **NR** or **NB**). The numeric value is shown to the right.

The slider range is 0–100. When no leveled DSP is active — or when only RNN, ANFT, or APF is on — the slider row is dimmed and does not respond to input. The row remains in place at all times; it does not shift the button grid when its target changes.

Algorithms that support the level slider: NR, NB, ANF, NRL, NRS, NRF, ANFL.

Starting in v0.9.8, when a leveled DSP algorithm is enabled from the radio's saved profile on startup, the level slider is automatically populated without requiring a manual toggle.

### Filter width label

The filter width label shows the current filter bandwidth. Click to cycle through filter preset buttons in the Mode tab. Starting in v0.9.8, this label uses `RxApplet::formatFilterWidth` as the single source of truth, fixing a 0.1 kHz offset that affected SSB/digital mode readouts.

## Tips

- Each DAX channel can be assigned to only one slice at a time. If you assign a channel that is already in use by another slice, the radio will move the assignment.
- If the VFO panel would be clipped by the window edge, it flips to the right side of the marker automatically.
- To access NR2, RN2, NR4, MNR, BNR, or DFNR, right-click the spectrum display to open the overlay menu, or open the AetherDSP applet.

## Troubleshooting

- **DAX channel combo has no effect / audio does not appear on the host** — Confirm the DAX audio bridge is running. Check `Settings > Autostart DAX with AetherSDR`. On macOS and PipeWire systems, the bridge must be active for DAX channels to appear as audio devices.
- **DAX tab is not visible** — The VFO panel may be collapsed. Click the collapsed strip to expand it, then select the DAX tab.
- **DSP level slider is dimmed** — No leveled DSP algorithm is currently active, or only RNN, ANFT, or APF is enabled. Turn on NR, NB, ANF, NRL, NRS, NRF, or ANFL to activate the slider.
- **DSP level slider is missing on startup** — If a leveled DSP algorithm was enabled in the radio's saved profile, the slider is now automatically populated. If it still appears missing, toggle the algorithm off and on again.
- **Squelch button is disabled** — You are in Digital, RTTY, or CW mode. Squelch is not available in these modes (digital and RTTY route audio through DAX; CW has radio-locked fixed squelch). Switch to a supported mode such as USB or AM to enable squelch controls.

## Related

- [VFO Panel overview](overview.md)
- [Adjust AF gain and pan from the VFO panel](adjust-af-gain-and-pan-from-the-vfo-panel.md)
- [Mute audio for a slice from the VFO panel](mute-audio-for-a-slice-from-the-vfo-panel.md)
- [Collapse the VFO panel to frequency-only view](collapse-the-vfo-panel-to-frequency-only-view.md)