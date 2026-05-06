# Collapse the VFO panel to frequency-only view

When screen space is limited, you can collapse the VFO panel to a compact strip that shows only the slice frequency. The collapsed state is saved per slice so it persists across sessions.

## Before you start

- AetherSDR must be connected to the radio. The VFO panel requires a live radio connection.
- The VFO panel for the slice must be open. If it is not visible, click the VFO marker flag on the spectrum display for that slice.

## Steps

1. Locate the slice badge in the header area of the VFO panel. The badge shows the slice identifier (for example, **A** or **B**).
2. Click the slice badge. The panel collapses to a compact frequency-only strip.
3. To restore the full panel, click anywhere on the collapsed strip.

## What each control does

| Control | Default | Persisted setting |
|---|---|---|
| Collapse toggle | Expanded | `SliceFlagCollapsed_{N}` |

The `SliceFlagCollapsed_{N}` setting is stored per slice, where `{N}` is the slice number. Collapsing one slice does not affect other slices.

## DSP tab changes in v0.9.7

The DSP tab in the VFO panel now shows only the noise reduction and filtering algorithms supplied directly by the radio. The following buttons have been removed from the DSP tab grid:

- **NR2** (spectral noise reduction)
- **RN2** (RNNoise noise suppression)
- **BNR** (GPU neural denoising)
- **NR4** (spectral bleach noise reduction)
- **MNR** (macOS MMSE-Wiener noise reduction)
- **DFNR** (DeepFilterNet3 neural noise reduction)

These client-side processing algorithms are still available. Access them through the spectrum overlay menu or the AetherDSP applet.

The buttons that remain in the DSP tab grid are arranged in a four-column layout:

| Position | Button |
|---|---|
| Row 0, Col 0 | NR |
| Row 0, Col 1 | NB |
| Row 0, Col 2 | ANF |
| Row 0, Col 3 | APF (visible in CW mode only) |
| Row 1, Col 0 | NRL |
| Row 1, Col 1 | NRS |
| Row 1, Col 2 | RNN |
| Row 1, Col 3 | NRF |
| Row 2, Col 0 | ANFL |
| Row 2, Col 1 | ANFT |

### DSP level slider

A shared level slider row appears below the DSP button grid. The slider targets whichever leveled DSP algorithm was most recently enabled. The label to the left of the slider shows the name of the current target (for example, **NR** or **NB**), and the numeric value is shown to the right.

| Control | Range | Behavior |
|---|---|---|
| DSP level slider | 0–100 | Sets the level for the active DSP algorithm. Retargets automatically when you enable a different algorithm. |

The slider row remains in the layout at all times. When no compatible algorithm is active — or when only RNN, ANFT, or APF is on — the slider row fades out and does not respond to input. Enabling a supported algorithm fades the row back in and retargets the slider to that algorithm.

Algorithms that the level slider can target: NR, NB, ANF, NRL, NRS, NRF, ANFL.

## Tips

- In collapsed view, scrolling the mouse wheel over the strip tunes the slice frequency by the current step size — the same as scrolling over the frequency display in the full panel.
- In collapsed view, clicking the TX badge painted on the strip toggles the TX assignment for that slice. Clicking anywhere else on the strip expands the panel.
- The panel flips to the right side of the VFO marker automatically if expanding it would be clipped by the window edge. This behavior applies in both expanded and collapsed states.
- To access NR2, RN2, BNR, NR4, MNR, or DFNR, right-click the spectrum display to open the overlay menu, or open the AetherDSP applet.

## Related

- [VFO Panel overview](overview.md)
- [Tune the radio by typing a frequency into the VFO panel](tune-the-radio-by-typing-a-frequency-into-the-vfo-panel.md)
- [Change the VFO marker line thickness](change-the-vfo-marker-line-thickness.md)
- [Hide or show filter edge lines on the spectrum](hide-or-show-filter-edge-lines-on-the-spectrum.md)