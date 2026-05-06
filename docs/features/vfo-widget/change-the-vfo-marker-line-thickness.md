# Change the VFO Marker Line Thickness

Use the marker thickness button to control how prominent the VFO marker line appears on the spectrum display, or to hide it entirely. The setting is saved per slice.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- The VFO panel must be open for the slice you want to adjust. If it is not visible, click the VFO marker flag for that slice on the spectrum display.

## Steps

1. Open the VFO panel for the target slice by clicking its VFO marker flag on the spectrum display.
2. Locate the **Marker thickness button** in the VFO panel.
3. Click the button to cycle through the available values: **Off**, **1 px**, and **3 px**.
4. Stop clicking when the desired thickness is shown. The marker on the spectrum display updates immediately.

## What each control does

| Control | Default | Valid values | Persisted setting |
|---|---|---|---|
| Marker thickness button | 1 px | Off, 1 px, 3 px | `Slice{N}_MarkerWidth` |

Each click advances to the next value in the cycle: **Off** → **1 px** → **3 px** → **Off**. The setting is persisted per slice, so slice 1 and slice 2 can have different thicknesses.

## Tips

- Setting the marker to **Off** hides the vertical line entirely. The VFO panel and flag remain visible and functional.
- If you run multiple slices on the same panadapter, increasing one marker to **3 px** can help distinguish it from adjacent slices.

## DSP tab changes in v0.9.7

The DSP tab in the VFO panel now shows only radio-supplied noise reduction buttons. The following buttons have been removed from the VFO panel DSP tab:

| Removed button | Where to find it now |
|---|---|
| NR2 | Spectrum overlay menu or AetherDSP applet |
| RN2 | Spectrum overlay menu or AetherDSP applet |
| BNR | Spectrum overlay menu or AetherDSP applet |
| NR4 | Spectrum overlay menu or AetherDSP applet |
| MNR | Spectrum overlay menu or AetherDSP applet |
| DFNR | Spectrum overlay menu or AetherDSP applet |

The remaining DSP tab buttons are arranged in a four-column grid:

| Row | Col 0 | Col 1 | Col 2 | Col 3 |
|---|---|---|---|---|
| 0 | NR | NB | ANF | APF |
| 1 | NRL | NRS | RNN | NRF |
| 2 | ANFL | ANFT | — | — |

The APF button remains hidden unless the slice is in a CW mode.

### DSP Level slider

A shared level slider row appears below the DSP button grid. The slider retargets automatically to whichever leveled DSP button was most recently enabled. The row label updates to show the active target (for example, **NR** or **NB**). The numeric value is shown to the right of the slider.

The row is always present in the layout. When no leveled DSP is active — or when only RNN, ANFT, or APF is on — the row fades to transparent. It becomes fully visible again as soon as a leveled DSP is turned on.

The slider controls the level for these targets:

| Target label | DSP controlled |
|---|---|
| NR | Noise reduction level |
| NB | Noise blanker level |
| ANF | Automatic notch filter level |
| NRL | Noise reduction level (NRL) |
| NRS | Spectral subtraction level |
| NRF | Spectral noise filter level |
| ANFL | LMS notch filter level |

## Related

- [Hide or show filter edge lines on the spectrum](hide-or-show-filter-edge-lines-on-the-spectrum.md)
- [Collapse the VFO panel to frequency-only view](collapse-the-vfo-panel-to-frequency-only-view.md)
- [VFO Panel overview](overview.md)