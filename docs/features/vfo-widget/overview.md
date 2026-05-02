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
| RX antenna button | Opens the antenna selection menu for the receive antenna of this slice. |
| TX antenna button | Opens the antenna selection menu for the transmit antenna of this slice. |
| Frequency display | Shows the current slice frequency. Click once to begin direct frequency entry; type a value in MHz and press Enter or Tab to apply. Scroll-wheel over the frequency display tunes by the current step size. |
| Filter width label | Shows the current filter bandwidth. Click to cycle through the filter preset buttons in the Mode tab. |
| TX badge | Shown in red when this slice is the active transmit slice. In collapsed mode, click the badge to toggle TX assignment. |
| SPLIT badge | Shown in amber when TX is assigned to a different slice than the active receive slice. |

### Mode tab

| Control | Default | Valid values | Persisted key |
|---|---|---|---|
| Mode combo | USB | USB, LSB, CW, CWL, AM, SAM, DIGU, DIGL, FM, NFM, DFM, RTTY | — |
| Filter preset buttons | — | — | `FilterPresets` |

Right-click a filter preset button to save the current filter width into that slot. Custom low and high filter edges can be saved per slot the same way.

### Audio tab

| Control | Default | Valid range | Persisted key |
|---|---|---|---|
| AF Gain slider | 100 | 0–100 | — |
| Pan slider | 50 | 0–100 | — |
| Mute button | off | — | — |
| Squelch button + slider | off | 0–100 | — |
| AGC combo | FAST | FAST, MED, SLOW, OFF | — |

The Pan slider center position (50) is stereo centre. Double-click the Pan slider to reset it to centre. Audio controls reflect live radio state and are not persisted by AetherSDR.

### DSP tab

| Control | Default | Notes |
|---|---|---|
| NR / NR2 / RN2 / NR4 / MNR / DFNR / BNR / NRL / NRS / RNN / NRF buttons | off | Button availability depends on radio series and build. Right-click NR2, NR4, MNR, or DFNR to open the AetherDSP Settings dialog for that algorithm. |

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

## Tips

- In collapsed mode, scroll-wheel anywhere over the strip tunes the slice by the current step size.
- Momentum (inertial) scroll events on macOS are ignored to prevent unintended tuning after a trackpad gesture ends.
- The panel flips to the right side of the marker automatically if displaying on the left would clip it at the window edge.

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
