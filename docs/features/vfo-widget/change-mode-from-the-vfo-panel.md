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

| Control | Default | Valid values | Persisted setting |
|---|---|---|---|
| Mode combo | USB | USB, LSB, CW, CWL, AM, SAM, DIGU, DIGL, FM, NFM, DFM, RTTY | — |
| Filter preset buttons | — | Saved filter width presets | `FilterPresets` |

**Mode combo** — sets the demodulation mode for the slice. Selecting a new mode takes effect immediately on the radio.

**Filter preset buttons** — appear on the same Mode tab. Each button applies a saved filter width. Right-click a button to save the current filter width into that slot. Presets are persisted in `FilterPresets`.

## DSP tab controls

The DSP tab shows buttons for noise reduction and filtering algorithms supplied directly by the radio. The following buttons are available:

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

All buttons default to off and toggle the corresponding algorithm on or off for the active slice.

> **Note:** The client-side noise reduction modules NR2, NR4, MNR, BNR, DFNR, and RN2 are no longer accessible from the DSP tab. Toggle those algorithms from the spectrum overlay menu or from the AetherDSP applet.

### DSP level slider

When one or more leveled DSP algorithms (NR, NB, ANF, NRL, NRS, or NRF) are active, a level slider appears below the DSP button grid. The slider label shows which algorithm is currently targeted — the most recently enabled leveled DSP. The numeric value is displayed to the right of the slider.

- Range: 0–100.
- The slider retargets automatically when you enable a different leveled DSP button.
- When no leveled DSP is active, or when only RNN, ANFT, or APF is on, the slider row fades out. It remains in the layout at all times to prevent the button grid from shifting.

## Tips

- Changing mode may alter the active filter passband. Check the filter width label in the header row after switching modes, and apply a filter preset if needed.
- The filter width label in the VFO panel header shows the current bandwidth. Click it to cycle through the filter preset buttons on the Mode tab.
- To access NR2, NR4, MNR, BNR, DFNR, or RN2, right-click the spectrum display and open the overlay menu, or open the AetherDSP applet.

## Related

- [Apply a filter width preset from the VFO panel](apply-a-filter-width-preset-from-the-vfo-panel.md)
- [Set a custom filter edge from the VFO panel](set-a-custom-filter-edge-from-the-vfo-panel.md)
- [VFO Panel overview](overview.md)