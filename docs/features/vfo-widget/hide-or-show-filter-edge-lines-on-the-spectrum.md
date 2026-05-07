# Hide or show filter edge lines on the spectrum

The VFO panel gives you a per-slice toggle to hide or show the vertical lines that mark the edges of the receive filter passband on the spectrum display. Hiding them reduces visual clutter when you want a cleaner panadapter view.

## Before you start

- AetherSDR must be connected to the radio.
- The slice you want to adjust must have a VFO marker visible on the spectrum display.

## Steps

1. Click the VFO marker flag on the spectrum display for the target slice. The VFO panel opens anchored to the marker.
2. Locate the **Filter edges button** in the VFO panel.
3. Click **Filter edges button** to toggle the filter edge lines off. Click it again to restore them.

The state is saved immediately. When you reopen AetherSDR, the setting is restored to whichever state you left it in for that slice.

## What each control does

| Control                      | Default                                                                                                                               | Persisted setting                                                                                                       |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| **Filter edges button**      | Shown (edges visible)                                                                                                                 | `Slice{N}_FilterEdgesHidden`                                                                                            |
| ADSP button (DSP tab)        | Opens the AetherDSP Settings dialog (client-side NR2 / NR4 / DFNR / RN2 / BNR / MNR). Same entry point as the Settings menu (v0.9.8). | Styled like a radio-side DSP toggle but non-checkable. Click raises and focuses the modeless AetherDSP Settings dialog. |
| AetherVoice button (DSP tab) | Toggles the Aetherial Audio Channel Strip — the unified TX/RX DSP suite (v0.9.8).                                                     | Spans 2 columns in the 4-column DSP grid. Matches the existing menu / chain entry points for the strip.                 |

`{N}` is the slice number. Each slice stores its own value independently.

## Tips

- The setting is per-slice. Hiding filter edges on slice 0 does not affect slice 1 or any other slice.
- If you have collapsed the VFO panel to frequency-only view, expand it first by clicking the collapsed strip to access the **Filter edges button**.
- In v0.9.8, several noise reduction buttons that were previously in the DSP tab (NR2, RN2, BNR, NR4, MNR, and DFNR) have been moved out of the VFO panel. Those algorithms are now toggled from the spectrum overlay menu and the AetherDSP applet. If you do not see a button you used previously, look for it there.
- In v0.9.8, the **Filter width label** now uses `RxApplet::formatFilterWidth` as the single source of truth for formatting filter bandwidth. This fixes a 0.1 kHz offset that affected SSB/digital mode readouts. The displayed filter width now matches the RX applet's filter readout exactly.
- In v0.9.8, DSP toggle buttons (NB, NR, ANF, NRL, NRS, NRF, ANFL) now automatically push and pop the shared DSP-level slider stack when state changes arrive from the radio. This ensures the slider is present on launch for any DSP that was enabled in the radio's saved profile.

## Related

- [Change the VFO marker line thickness](change-the-vfo-marker-line-thickness.md)
- [Collapse the VFO panel to frequency-only view](collapse-the-vfo-panel-to-frequency-only-view.md)
- [VFO Panel overview](overview.md)