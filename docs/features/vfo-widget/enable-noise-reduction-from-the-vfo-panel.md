# Enable noise reduction from the VFO panel

Use the DSP tab in the VFO panel to switch on one or more noise reduction algorithms for a slice. Each algorithm targets a different noise type; you can enable them independently.

## Before you start

- AetherSDR must be connected to the radio. The VFO panel requires an active radio connection.
- The VFO panel for the slice must be open and expanded. If it is collapsed to a frequency-only strip, click anywhere on it to expand it.

## Steps

1. Click the VFO marker flag on the spectrum display for the slice you want to adjust. The VFO panel opens anchored to the marker.
2. Click the **DSP** tab inside the VFO panel.
3. Click the button for the noise reduction algorithm you want to enable: **NR**, **NR2**, **RN2**, **NR4**, **MNR**, **DFNR**, **BNR**, **NRL**, **NRS**, **RNN**, or **NRF**. The button highlights when active.
4. To disable noise reduction, click the same button again. The highlight clears.

## What each control does

| Control | Default | Behavior |
|---|---|---|
| **NR** | off | Enables the standard noise reduction algorithm for this slice. |
| **NR2** | off | Enables the NR2 noise reduction algorithm. Right-click to open AetherDSP Settings for NR2. |
| **RN2** | off | Enables the RN2 noise reduction algorithm. |
| **NR4** | off | Enables the NR4 noise reduction algorithm. Right-click to open AetherDSP Settings for NR4. |
| **MNR** | off | Enables the MNR noise reduction algorithm. Right-click to open AetherDSP Settings for MNR. |
| **DFNR** | off | Enables the DFNR noise reduction algorithm. Right-click to open AetherDSP Settings for DFNR. |
| **BNR** | off | Enables the BNR noise reduction algorithm. |
| **NRL** | off | Enables the NRL noise reduction algorithm. |
| **NRS** | off | Enables the NRS noise reduction algorithm. |
| **RNN** | off | Enables the RNN noise reduction algorithm. |
| **NRF** | off | Enables the NRF noise reduction algorithm. |

Not all buttons may be present; availability depends on radio series and build.

## Tips

- Right-clicking **NR2**, **NR4**, **MNR**, or **DFNR** opens the AetherDSP Settings dialog, where you can tune advanced parameters for that algorithm. You can also open this dialog from `Settings > AetherDSP Settings...`.
- Multiple noise reduction buttons can be active at the same time.

## Related

- [VFO Panel overview](overview.md)
- [Enable squelch from the VFO panel](enable-squelch-from-the-vfo-panel.md)
