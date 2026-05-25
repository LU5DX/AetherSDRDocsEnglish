# VFO Panel overview

The VFO Panel is a floating, per-slice control panel anchored to the VFO marker flag on the spectrum display. It gives you quick access to the most frequently used slice settings — mode, filter presets, antenna selection, audio controls, AGC, noise reduction, RIT/XIT, and DAX assignment — without leaving the spectrum view.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- At least one slice must be active on the panadapter.

## How it works

Click the VFO marker flag on the spectrum display for any slice. The panel appears anchored to the left of the marker and flips right automatically if it would be clipped by the window edge.

The panel is divided into tabs — **Mode**, **Audio**, **DSP**, **X/RIT**, and **DAX** — plus a header row that is always visible. Controls in the header row apply regardless of which tab is active.

When collapsed, the panel shrinks to a compact frequency-only strip. Scroll-wheel tuning still works in collapsed mode. Click anywhere on the collapsed strip to expand it again, or click the TX badge to toggle the transmit slice assignment.

### Header row

The header row sits above the tabs and is always visible.

| Control | What it does |
|---|---|
| RX antenna button | Opens the antenna selection menu for the receive antenna of this slice. Menu items display radio-provided labels alongside abbreviated names in parentheses. |
| TX antenna button | Opens the antenna selection menu for the transmit antenna of this slice. RX-only antenna ports are excluded. Menu items display radio-provided labels alongside abbreviated names in parentheses. |
| Frequency display | Shows the current slice frequency. Click once to begin direct frequency entry; type a value in MHz and press Enter or Tab to apply. Scroll-wheel over the frequency display tunes by the current step size. If the slice is locked, a visual LOCKED overlay is shown and scroll-wheel tuning is blocked. |
| Filter width label | Shows the current filter bandwidth. Click to cycle through the filter preset buttons in the Mode tab. Uses `RxApplet::formatFilterWidth` as the single source of truth, fixing a 0.1 kHz offset that affected SSB/digital mode readouts (v0.9.8). |
| TX badge | Shown in red when this slice is the active transmit slice. In collapsed mode, click the badge to toggle TX assignment. |
| SPLIT badge | Shown in amber when TX is assigned to a different slice than the active receive slice. |

### Mode tab

| Control | Default | Valid values | Persisted key |
|---|---|---|---|
| Mode combo | USB | USB, LSB, CW, CWL, AM, SAM, DIGU, DIGL, FM, NFM, DFM, RTTY | — |
| Filter preset buttons | — | — | `FilterPresets` |

Right-click a filter preset button to save the current filter width into that slot. Custom low and high filter edges can be saved per slot the same way.

When DIGU or DIGL is selected in the Mode combo, a digital data container appears in the tab. This container is taller than the other tab content. The VFO Panel now reports only the current tab's preferred size, preventing a gap from appearing when switching back to the Mode tab from the DSP tab.

### Audio tab

| Control | Default | Valid range | Persisted key |
|---|---|---|---|
| AF Gain slider | 100 | 0–100 | — |
| Pan slider | 50 | 0–100 | — |
| Mute button | off | — | — |
| Squelch button + slider | off | 0–100 | — |
| AGC combo | FAST | FAST, MED, SLOW, OFF | — |

The Pan slider center position (50) is stereo centre. Double-click the Pan slider to reset it to centre. Audio controls reflect live radio state and are not persisted by AetherSDR.

The squelch is disabled in digital, RTTY, and CW modes. In digital and RTTY modes the audio feeds external decoders via DAX, where squelch would gate weak FSK signals. In CW mode the radio locks squelch on at a fixed level and rejects changes. When entering one of these modes while squelch is enabled, squelch is automatically turned off and restored when leaving that mode.

### DSP tab

The DSP tab contains buttons for noise reduction and filtering algorithms supplied directly by the radio. Client-side DSP modules (NR2, NR4, MNR, BNR, DFNR, and RN2) can be accessed from the AetherDSP Settings dialog or the Aetherial Audio Channel Strip.

| Control | Default | Notes |
|---|---|---|
| NR / NR2 / RN2 / NR4 / MNR / DFNR / BNR / NRL / NRS / RNN / NRF buttons | off | Button availability depends on radio series and build. Right-click NR2, NR4, MNR, or DFNR to open the AetherDSP Settings dialog for that algorithm. |
| ADSP button | — | Opens the AetherDSP Settings dialog (client-side NR2 / NR4 / DFNR / RN2 / BNR / MNR). Same entry point as the Settings menu (v0.9.8). Styled like a radio-side DSP toggle but non-checkable. Click raises and focuses the modeless AetherDSP Settings dialog. |
| AetherVoice button | — | Opens the Aetherial Audio Channel Strip — the unified TX/RX DSP suite (v0.9.8). Spans 2 columns in the 4-column DSP grid. |

#### DSP level slider

A shared level slider appears below the button grid. It targets whichever leveled DSP button was most recently enabled — NR, NB, ANF, NRL, NRS, NRF, or ANFL. The label to the left of the slider shows the name of the current target. The numeric value is shown to the right.

The slider row remains in the layout at all times. When no leveled DSP is active (or only RNN, ANFT, or APF are on), the row fades out and does not respond to interaction. It becomes fully visible again as soon as a leveled DSP is turned on.

In v0.9.8, the level slider is also pushed to the shared stack when a leveled DSP state change arrives from the radio on startup. This ensures the slider appears for any DSP that was already enabled in the radio's saved profile.

### X/RIT tab

| Control | Default | Notes |
|---|---|---|
| RIT button + label | off | Enables receiver incremental tuning. The label shows the current offset. Scroll-wheel adjusts in 10 Hz steps. |
| XIT button + label | off | Enables transmitter incremental tuning. The label shows the current offset. Scroll-wheel adjusts in 10 Hz steps. |

### DAX tab

| Control | Default | Valid values | Persisted key |
|---|---|---|---|
| DAX channel combo | Off | Off, 1–8 | — |

### Display controls

These controls affect how the slice appears on the spectrum display. They are persisted individually per slice (where `{N}` is the slice number).

| Control | Default | Valid values | Persisted key |
|---|---|---|---|
| Marker thickness button | 1 px | Off, 1 px, 3 px | `Slice{N}_MarkerWidth` |
| Filter edges button | shown | shown / hidden | `Slice{N}_FilterEdgesHidden` |
| Collapse toggle | expanded | expanded / collapsed | `SliceFlagCollapsed_{N}` |

Clicking the slice badge in the header row collapses the panel. Clicking anywhere on the collapsed strip expands it.

## Antenna selection

The RX and TX antenna buttons open menus that display radio-provided labels (such as "ANT 1" or "RX ANT B") alongside abbreviated names in parentheses when they differ. The menus show:

- **RX antenna**: All available antenna ports for receive. Menu items include tooltips and status bar hints showing the full antenna name.
- **TX antenna**: Only antenna ports suitable for transmit (RX-only ports are excluded). Menu items include tooltips and status bar hints showing the full antenna name.

Both menus are populated from the radio's per-slice antenna list when available, falling back to the global antenna list. Antenna assignments apply immediately.

## Frequency entry

Click the frequency display to begin direct entry. The following rules apply:

- Type a frequency in MHz (e.g., `14.200` or `14200`). Press Enter or Tab to apply.
- On XVTR bands, frequencies up to 50000 MHz are accepted.
- On bands between 100-999 MHz (2m, 70cm), a bare integer like `1446` is interpreted as `144.6`, `14696` as `146.96`, and `144600` as `144.600`. This convenience does not apply above 1000 MHz (23cm and microwave bands), where a bare integer represents the frequency in MHz directly.
- If you explicitly enter a frequency above 54 MHz (e.g., `144.200`), the parser treats it as a valid MHz entry and accepts frequencies up to 50000 MHz, even if the slice is not on an XVTR band.

## Locked slice behavior

When a slice is locked:

- The lock button shows a lock icon. Click to unlock.
- Scroll-wheel tuning is blocked. If you attempt to tune a locked slice, a visual LOCKED overlay appears on the frequency display and any in-progress direct frequency entry is cancelled.
- The LOCKED overlay clears automatically when you unlock the slice.
- Direct frequency entry is prevented while locked — clicking the frequency display does not enter edit mode, and any active direct entry is cancelled immediately.

## Tips

- In collapsed mode, scroll-wheel anywhere over the strip tunes the slice by the current step size.
- Scroll-wheel tuning works in collapsed mode regardless of whether the slice is locked — if locked, the tune is blocked and the LOCKED overlay appears.
- Momentum (inertial) scroll events on macOS are ignored to prevent unintended tuning after a trackpad gesture ends.
- The panel flips to the right side of the marker automatically if displaying on the left would clip it at the window edge.
- Client-side noise reduction algorithms (NR2, NR4, MNR, BNR, DFNR, RN2) are accessed from the AetherDSP Settings dialog (ADSP button) or the Aetherial Audio Channel Strip (AetherVoice button), both in the DSP tab.
- Squelch is disabled in digital, RTTY, and CW modes. Digital and RTTY audio feeds external decoders via DAX channels, and squelch could gate weak FSK signals. CW mode locks squelch on at a fixed level.

## Related

- [Tune the radio by typing a frequency into the VFO panel](tune-the-radio-by-typing-a-frequency-into-the-vfo-panel.md)
- [Change mode from the VFO panel](change-mode-from-the-vfo-panel.md)
- [Apply a filter width preset from the VFO panel](apply-a-filter-width-preset-from-the-vfo-panel.md)
- [Set a custom filter edge from the VFO panel](set-a-custom-filter-edge-from-the-vfo-panel.md)
- [Adjust AF gain and pan from the VFO panel](adjust-af-gain-and-pan-from-the-vfo-panel.md)
- [Mute audio for a slice from the VFO panel](mute-audio-for-a-slice-from-the-vfo-panel.md)
- [Enable squelch from the VFO panel](enable-squelch-from-the-vfo-panel.md)
- [Enable noise reduction from the VFO panel](enable-noise-reduction-from-the-vfo-panel.md)
- [Enable RIT or XIT offset from the VFO panel](enable-rit-or-xit-offset-from-the-vfo-panel.md)
- [Assign a DAX channel from the VFO panel](assign-a-dax-channel-from-the-vfo-panel.md)
- [Change the VFO marker line thickness](change-the-vfo-marker-line-thickness.md)
- [Hide or show filter edge lines on the spectrum](hide-or-show-filter-edge-lines-on-the-spectrum.md)
- [Collapse the VFO panel to frequency-only view](collapse-the-vfo-panel-to-frequency-only-view.md)
- Lock a slice to prevent accidental tuning