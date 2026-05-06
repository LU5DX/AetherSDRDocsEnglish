# Apply a filter width preset from the VFO panel

Filter preset buttons let you switch the receive filter width for a slice with a single click. Use them to move quickly between common bandwidths — for example, between a wide 3 kHz SSB filter and a narrow 500 Hz CW filter — without leaving the spectrum view.

## Before you start

- AetherSDR must be connected to the radio. The VFO panel requires an active radio connection.
- The VFO panel for the target slice must be open and expanded. If it is collapsed to a frequency-only strip, click anywhere on it to expand it first.

## Steps

1. Click the VFO marker flag on the spectrum display for the slice you want to adjust. The VFO panel opens, anchored to the left of the marker.
2. Click the **Mode** tab inside the VFO panel.
3. Click the filter preset button that corresponds to the bandwidth you want. The radio immediately applies that filter width to the slice.

To save the current filter width into a preset slot:

1. Set the filter to the bandwidth you want to save (see [Set a custom filter edge from the VFO panel](set-a-custom-filter-edge-from-the-vfo-panel.md)).
2. Right-click the preset button slot you want to overwrite.
3. The current filter width is saved into that slot.

## What each control does

| Control | Behavior | Default | Setting key |
|---|---|---|---|
| Filter preset buttons (Mode tab) | Each button applies a saved filter width preset to the slice. Left-click to apply; right-click to save the current filter width into that slot. Custom low and high filter edges can be stored per slot via right-click. | — | `FilterPresets` |
| Filter width label | Displays the current filter bandwidth. Click to cycle through the filter preset buttons in the Mode tab. | — | — |

## DSP tab changes in v0.9.7

The **DSP tab** now shows only radio-side noise reduction buttons. The following buttons have been removed from the VFO panel DSP tab:

- **NR2**
- **RN2**
- **BNR**
- **NR4**
- **MNR**
- **DFNR**

These client-side DSP modules are now accessed through the spectrum overlay menu and the AetherDSP applet. Toggle them there instead of from the VFO panel.

The buttons that remain in the DSP tab are arranged in a four-column grid:

| Position | Button |
|---|---|
| Row 1, col 1 | NR |
| Row 1, col 2 | NB |
| Row 1, col 3 | ANF |
| Row 1, col 4 | APF (visible in CW mode only) |
| Row 2, col 1 | NRL |
| Row 2, col 2 | NRS |
| Row 2, col 3 | RNN |
| Row 2, col 4 | NRF |
| Row 3, col 1 | ANFL |
| Row 3, col 2 | ANFT |

A shared **DSP level slider** row appears below the button grid. The slider retargets automatically to whichever leveled DSP button was most recently turned on. Its label shows the name of the current target (for example, **NR** or **NB**), and the value to the right of the slider shows the current level numerically. When no leveled DSP algorithm is active — or when only RNN, ANFT, or APF is on — the slider row is present in the layout but visually faded out. Clicking it while faded has no effect.

| Control | Behavior | Default | Setting key |
|---|---|---|---|
| NR / NB / ANF / APF / NRL / NRS / RNN / NRF / ANFL / ANFT buttons (DSP tab) | Enables the corresponding radio-side noise reduction or filtering algorithm for this slice. APF is visible in CW mode only. | off | — |
| DSP level slider (DSP tab) | Sets the processing level for the most recently activated leveled DSP algorithm. The label to the left identifies the current target. Hidden (faded) when no leveled algorithm is active. | — | — |

## Tips

- The filter width label in the VFO panel header shows the active bandwidth at all times. Click it directly to cycle through the preset buttons without switching to the Mode tab first.
- Preset slots are shared across all slices and modes. Overwriting a slot affects every slice that uses it.
- Filter edge lines on the spectrum panadapter reflect the active filter width. If the lines are hidden, enable them with the Filter edges button in the VFO panel. See [Hide or show filter edge lines on the spectrum](hide-or-show-filter-edge-lines-on-the-spectrum.md).
- To access NR2, RN2, BNR, NR4, MNR, or DFNR, right-click the spectrum overlay or open the AetherDSP applet.

## Related

- [Set a custom filter edge from the VFO panel](set-a-custom-filter-edge-from-the-vfo-panel.md)
- [Change mode from the VFO panel](change-mode-from-the-vfo-panel.md)
- [Hide or show filter edge lines on the spectrum](hide-or-show-filter-edge-lines-on-the-spectrum.md)
- [VFO Panel overview](overview.md)