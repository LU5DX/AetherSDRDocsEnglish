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

| Control | Default | Valid values | Persisted setting key |
|---|---|---|---|
| DAX channel combo | Off | Off, 1–8 | — |

The DAX channel combo assigns a DAX audio channel to the current slice. Selecting a numbered channel routes the slice's received audio to that DAX channel. Selecting **Off** removes the assignment. This setting reflects live radio state and is not persisted locally by AetherSDR.

## DSP tab controls

Starting in v0.9.7, the DSP tab in the VFO panel contains only radio-supplied noise reduction buttons. The client-side algorithms that were previously shown here — NR2, RN2, NR4, MNR, BNR, and DFNR — have been moved to the spectrum overlay menu and the AetherDSP applet. Toggle those algorithms from either of those locations.

The following buttons remain in the DSP tab grid:

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

### DSP level slider

A shared level slider row appears below the button grid. The slider adjusts the strength of whichever leveled DSP button was most recently turned on. The label to the left of the slider shows the active target (for example, **NR** or **NB**). The numeric value is shown to the right.

The slider range is 0–100. When no leveled DSP is active — or when only RNN, ANFT, or APF is on — the slider row is dimmed and does not respond to input. The row remains in place at all times; it does not shift the button grid when its target changes.

Algorithms that support the level slider: NR, NB, ANF, NRL, NRS, NRF, ANFL.

## Tips

- Each DAX channel can be assigned to only one slice at a time. If you assign a channel that is already in use by another slice, the radio will move the assignment.
- If the VFO panel would be clipped by the window edge, it flips to the right side of the marker automatically.
- To access NR2, RN2, NR4, MNR, BNR, or DFNR, right-click the spectrum display to open the overlay menu, or open the AetherDSP applet.

## Troubleshooting

- **DAX channel combo has no effect / audio does not appear on the host** — Confirm the DAX audio bridge is running. Check `Settings > Autostart DAX with AetherSDR`. On macOS and PipeWire systems, the bridge must be active for DAX channels to appear as audio devices.
- **DAX tab is not visible** — The VFO panel may be collapsed. Click the collapsed strip to expand it, then select the DAX tab.
- **NR2, RN2, NR4, MNR, BNR, or DFNR buttons are not visible in the DSP tab** — These buttons were removed from the VFO panel in v0.9.7. Use the spectrum overlay menu or the AetherDSP applet to enable those algorithms.
- **DSP level slider is dimmed** — No leveled DSP algorithm is currently active, or only RNN, ANFT, or APF is enabled. Turn on NR, NB, ANF, NRL, NRS, NRF, or ANFL to activate the slider.

## Related

- [VFO Panel overview](overview.md)
- [Adjust AF gain and pan from the VFO panel](adjust-af-gain-and-pan-from-the-vfo-panel.md)
- [Mute audio for a slice from the VFO panel](mute-audio-for-a-slice-from-the-vfo-panel.md)
- [Collapse the VFO panel to frequency-only view](collapse-the-vfo-panel-to-frequency-only-view.md)