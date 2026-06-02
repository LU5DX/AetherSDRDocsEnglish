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
| **RX antenna button**        | Opens antenna selection menu for the receive antenna of this slice. The menu uses the radio's reported RX antenna list when available. | Not persisted                                                                                                           |
| **TX antenna button**        | Opens antenna selection menu for the transmit antenna of this slice. Automatically skips RX-only antenna ports (those starting with "RX") and includes antennas whose name starts with "ANT", "TX", or "XVTR" as a fallback. | Not persisted                                                                                                           |
| **Frequency display**        | Shows the current slice frequency. Click once to begin direct frequency entry; type MHz and press Enter or Tab. On XVTR bands, bare integers of 4+ digits with the slice in the 100-999 MHz range automatically insert a decimal after the third digit (e.g., 1446 → 144.6). Above 1000 MHz, bare integers are treated as the direct MHz value. Maximum frequency entry: 50000 MHz. The frequency display shows a "LOCKED" overlay when the slice VFO is locked. | Not persisted                                                                                                           |
| **Filter width label**       | Shows current filter bandwidth. Click to cycle through filter preset buttons in the Mode tab. Uses `RxApplet::formatFilterWidth` as the single source of truth, fixing a 0.1 kHz offset that affected SSB/digital mode readouts. | Not persisted                                                                                                           |
| **AF Gain slider**           | 100                                                                                                                                     | Not persisted — reflects live radio state.                                                                              |
| **Pan slider**               | 50                                                                                                                                      | Not persisted                                                                                                           |
| **Mute button**              | off                                                                                                                                    | Not persisted                                                                                                           |
| **Squelch button + slider**  | off                                                                                                                                    | Not persisted                                                                                                           |
| **AGC combo**                | FAST                                                                                                                                   | Not persisted                                                                                                           |
| **NR / NR2 / RN2 / NR4 / MNR / DFNR / BNR / NRL / NRS / RNN / NRF buttons** | off                                                                                                                     | Not persisted                                                                                                           |
| **ADSP button**              | Opens the AetherDSP Settings dialog (client-side NR2 / NR4 / DFNR / RN2 / BNR / MNR). Same entry point as the Settings menu (v0.9.8). | Styled like a radio-side DSP toggle but non-checkable. Click raises and focuses the modeless AetherDSP Settings dialog. |
| **AetherVoice button**       | Toggles the Aetherial Audio Channel Strip — the unified TX/RX DSP suite (v0.9.8).                                                     | Spans 2 columns in the 4-column DSP grid. Matches the existing menu / chain entry points for the strip.              |
| **Mode combo**               | USB                                                                                                                                    | Not persisted                                                                                                           |
| **Filter preset buttons**    | Applies a saved filter width preset. Right-click to save the current filter width into that slot.                                     | `FilterPresets`                                                                                                         |
| **RIT / XIT buttons + labels** | off                                                                                                                                  | Not persisted                                                                                                           |
| **DAX channel combo**        | Off                                                                                                                                    | Not persisted                                                                                                           |
| **Marker thickness button**  | 1 px                                                                                                                                   | `Slice{N}_MarkerWidth`                                                                                                  |
| **Collapse toggle**          | expanded                                                                                                                               | `SliceFlagCollapsed_{N}`                                                                                                |

`{N}` is the slice number. Each slice stores its own value independently.

## Tips

- The setting is per-slice. Hiding filter edges on slice 0 does not affect slice 1 or any other slice.
- If you have collapsed the VFO panel to frequency-only view, expand it first by clicking the collapsed strip to access the **Filter edges button**.
- In v0.9.8, several noise reduction buttons that were previously in the DSP tab (NR2, RN2, BNR, NR4, MNR, and DFNR) have been moved out of the VFO panel. Those algorithms are now toggled from the spectrum overlay menu and the AetherDSP applet. If you do not see a button you used previously, look for it there.
- In v0.9.8, the **Filter width label** now uses `RxApplet::formatFilterWidth` as the single source of truth for formatting filter bandwidth. This fixes a 0.1 kHz offset that affected SSB/digital mode readouts. The displayed filter width now matches the RX applet's filter readout exactly.
- In v0.9.8, DSP toggle buttons (NB, NR, ANF, NRL, NRS, NRF, ANFL) now automatically push and pop the shared DSP-level slider stack when state changes arrive from the radio. This ensures the slider is present on launch for any DSP that was enabled in the radio's saved profile.
- In v26.5.1, squelch is disabled for RTTY modes in addition to digital and CW modes. This prevents squelch from gating weak FSK signals sent to external decoders via DAX.
- In v26.5.2.1, the RX and TX antenna menus now use the radio's reported per-slice antenna list when available. The TX antenna menu automatically filters out RX-only antenna ports. The frequency entry maximum for XVTR bands has been increased to 50000 MHz. The slice badge now supports HTML rendering (#2606).
- In v26.5.3, the VFO panel uses a custom `TabStack` widget that reports only the current tab's size hint, preventing a visual gap when switching between tabs of different heights. The frequency display shows a "LOCKED" overlay when the slice VFO is locked. Direct frequency entry is cancelled when the slice becomes locked. Scroll-wheel tuning on a locked VFO now notifies the user that tuning is blocked.
- In v26.6.1, the VFO panel's slider controls (AF Gain, Pan, Squelch threshold) now use theme-aware colour tokens for their groove and handle styling, ensuring consistent appearance with the spectrum and other themed elements. The **Pan slider** uses a centre-anchored fill that extends outward from the midpoint, with a small centre-mark dot to indicate the neutral position.
- In v26.6.1, the VFO panel has been assigned its own theming container scope (`spectrum/vfo`) that inherits spectrum overrides. This improves theme inspector coverage — clicking the VFO panel background, slice badge, or signal meter now surfaces the relevant theme tokens in the inspector.

## Related

- [Change the VFO marker line thickness](change-the-vfo-marker-line-thickness.md)
- [Collapse the VFO panel to frequency-only view](collapse-the-vfo-panel-to-frequency-only-view.md)
- [VFO Panel overview](overview.md)