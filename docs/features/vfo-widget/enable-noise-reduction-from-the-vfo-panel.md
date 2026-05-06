# Enable noise reduction from the VFO panel

Use the DSP tab in the VFO panel to switch on one or more noise reduction algorithms for a slice. Each algorithm targets a different noise type; you can enable them independently.

## Before you start

- AetherSDR must be connected to the radio. The VFO panel requires an active radio connection.
- The VFO panel for the slice must be open and expanded. If it is collapsed to a frequency-only strip, click anywhere on it to expand it.

## Steps

1. Click the VFO marker flag on the spectrum display for the slice you want to adjust. The VFO panel opens anchored to the marker.
2. Click the **DSP** tab inside the VFO panel.
3. Click the button for the noise reduction algorithm you want to enable: **NR**, **NB**, **ANF**, **NRL**, **NRS**, **RNN**, or **NRF**. The button highlights when active.
4. To disable noise reduction, click the same button again. The highlight clears.

## What each control does

| Control | Default | Behavior |
|---|---|---|
| **NR** | off | Enables the standard noise reduction algorithm for this slice. |
| **NB** | off | Enables the noise blanker for this slice. |
| **ANF** | off | Enables the automatic notch filter for this slice. |
| **NRL** | off | Enables the NRL noise reduction algorithm for this slice. |
| **NRS** | off | Enables spectral subtraction for this slice. |
| **RNN** | off | Enables the RNN noise reduction algorithm for this slice. |
| **NRF** | off | Enables the spectral noise filter for this slice. |
| **ANFL** | off | Enables the LMS notch filter for this slice. |
| **ANFT** | off | Enables the FFT notch filter for this slice. |

The **APF** button is also present but is only visible when the slice is in a CW mode.

## DSP level slider

When one or more leveled DSP algorithms are active, a shared level slider appears below the button grid. The slider label shows which algorithm it currently targets — it retargets automatically to the most recently enabled leveled algorithm. The numeric value is shown to the right of the slider.

The slider is always present in the layout. When no leveled algorithm is active (or only RNN, ANFT, or APF are on), the slider row fades out and does not respond to input.

| Algorithms that expose the level slider |
|---|
| NR, NB, ANF, NRL, NRS, NRF, ANFL |

## Client-side noise reduction algorithms

The algorithms **NR2**, **RN2**, **NR4**, **MNR**, **BNR**, and **DFNR** are no longer in the VFO panel DSP tab. These client-side processing modules are available from the spectrum overlay menu and from the AetherDSP applet. Access them there to keep the VFO panel focused on radio-supplied DSP.

## Tips

- Multiple noise reduction buttons can be active at the same time.
- You can open the AetherDSP applet from `Settings > AetherDSP Settings...` to configure client-side noise reduction algorithms.

## Related

- [VFO Panel overview](overview.md)
- [Enable squelch from the VFO panel](enable-squelch-from-the-vfo-panel.md)