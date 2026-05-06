# Tune the radio by typing a frequency into the VFO panel

Direct frequency entry lets you jump to an exact frequency without clicking around the panadapter. Type a value in MHz into the VFO panel's frequency display and press Enter.

## Before you start

- AetherSDR must be connected to your FLEX-8600 radio.
- The VFO panel for the target slice must be open. If it is not visible, click the VFO marker flag for that slice on the spectrum display.

## Steps

1. Click the **Frequency display** once. The display enters direct entry mode.
2. Type the desired frequency in MHz.
3. Press **Enter** or **Tab** to apply. The slice retunes immediately.

## What each control does

| Control | Behavior | Default | Persisted key |
|---|---|---|---|
| **Frequency display** | Shows the current slice frequency. Click once to begin direct entry; type MHz and press Enter or Tab to apply. Scroll the mouse wheel over the display to step-tune up or down by the current step size. | — | — |
| **Collapse toggle** | Collapses the VFO panel to a compact frequency-only strip. In collapsed mode, scrolling anywhere on the strip tunes by the current step size. | Expanded | `SliceFlagCollapsed_{N}` |

## DSP tab controls

The DSP tab contains toggle buttons for noise reduction and filtering algorithms supplied by the radio. The following buttons are available in the VFO panel DSP grid:

| Button | Description |
|---|---|
| **NR** | Noise reduction. |
| **NB** | Noise blanker. |
| **ANF** | Automatic notch filter. |
| **APF** | Audio peak filter. Visible only when the slice is in CW mode. |
| **NRL** | Noise reduction level. |
| **NRS** | Spectral subtraction. |
| **RNN** | RNN noise reduction. |
| **NRF** | Spectral noise filter. |
| **ANFL** | LMS notch filter. |
| **ANFT** | FFT notch filter. |

All buttons default to off.

Client-side noise reduction modules — NR2, NR4, MNR, BNR, DFNR, and RN2 — are no longer shown in the VFO panel DSP grid. Access those algorithms from the spectrum overlay menu or the AetherDSP applet.

### DSP level slider

When one or more radio-side DSP algorithms that support a level control are active, a level slider appears below the DSP button grid. The slider label shows the name of the most recently enabled algorithm that supports leveling (for example, **NR**, **NB**, **ANF**, **NRL**, **NRS**, **NRF**, or **ANFL**). The adjacent numeric readout shows the current value.

- Drag the slider to set the level for the targeted algorithm (0–100).
- The slider retargets automatically when you enable a different leveled algorithm.
- When no leveled algorithm is active, the slider row fades out but remains in position so the button grid does not shift.

## Tips

- If the panel is collapsed to the frequency-only strip, click anywhere on it to expand it so the **Frequency display** is accessible for direct entry.
- The scroll wheel also tunes the slice when the pointer is over the **Frequency display**, stepping by the slice's current step size. On macOS, inertial scroll events are ignored to prevent unintended tuning after a gesture ends.

## Troubleshooting

- **Typing has no effect** — Check that the slice is not locked. A locked slice ignores tune commands. Unlock it before entering a frequency.
- **The VFO panel is not visible** — Click the VFO marker flag for the desired slice on the spectrum display to open the panel.
- **NR2, NR4, MNR, BNR, DFNR, or RN2 buttons are missing from the DSP tab** — These client-side modules were moved out of the VFO panel in v0.9.7. Toggle them from the spectrum overlay menu or the AetherDSP applet.
- **The DSP level slider is faded and does not respond to clicks** — The slider is inactive when no radio-side DSP algorithm that supports leveling is currently enabled. Enable NR, NB, ANF, NRL, NRS, NRF, or ANFL to activate the slider.

## Related

- [VFO Panel overview](overview.md)
- [Collapse the VFO panel to frequency-only view](collapse-the-vfo-panel-to-frequency-only-view.md)
- [Change mode from the VFO panel](change-mode-from-the-vfo-panel.md)
- [Enable RIT or XIT offset from the VFO panel](enable-rit-or-xit-offset-from-the-vfo-panel.md)