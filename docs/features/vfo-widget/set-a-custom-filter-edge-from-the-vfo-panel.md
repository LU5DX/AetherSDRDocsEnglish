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

| Control | Behavior | Default | Setting key |
|---|---|---|---|
| Filter preset buttons (Mode tab) | Applies a saved filter width preset when clicked. Right-click to save the current filter width or set custom lo/hi edges for that slot. | — | `FilterPresets` |
| Filter width label | Shows the current filter bandwidth. Click to cycle through filter preset buttons in the Mode tab. | — | — |
| Filter edges button | Toggles the filter edge lines on the spectrum passband display. | shown | `Slice{N}_FilterEdgesHidden` |

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

#### DSP level slider

When one or more radio-side DSP functions that support a level control are enabled, a shared level slider appears below the button grid. The slider label and value update to reflect the most recently enabled function. The slider is always present in the layout but fades out when no supported DSP function is active. Drag the slider to set the level (0–100) for the targeted function.

Functions that the level slider can target: NR, NB, ANF, NRL, NRS, NRF, ANFL.

Functions that do not target the level slider: RNN, ANFT, APF.

## Tips

- To verify the active filter edges on the spectrum, confirm that the filter edges button is in its default shown state. If the edge lines are hidden, toggle the filter edges button to make them visible again.
- Right-clicking a preset button saves the *current* filter width into that slot as an alternative to typing edge values manually. Use this for a quick capture of a filter you have already dialed in.
- To access NR2, NR4, MNR, BNR, DFNR, or RN2, right-click the spectrum display to open the overlay menu, or open the AetherDSP applet.

## Related

- [Apply a filter width preset from the VFO panel](apply-a-filter-width-preset-from-the-vfo-panel.md)
- [Hide or show filter edge lines on the spectrum](hide-or-show-filter-edge-lines-on-the-spectrum.md)
- [Change mode from the VFO panel](change-mode-from-the-vfo-panel.md)