# VFO Panel

The VFO panel is a floating per-slice control panel anchored to the VFO marker on the spectrum display. It provides quick access to the most frequently used per-slice settings — mode, filter presets, antenna selection, AF gain, pan, squelch, AGC, RIT/XIT, DSP noise reduction buttons, and DAX assignment — without leaving the spectrum view. The panel collapses to a compact frequency-only strip.

## Before you start

- AetherSDR must be connected to the radio.
- The slice you want to adjust must have a VFO marker visible on the spectrum display.

## Opening the VFO panel

Click the VFO marker flag on the spectrum display for the target slice. The VFO panel opens anchored to the marker.

## Hiding or showing filter edge lines on the spectrum

1. Click the VFO marker flag on the spectrum display for the target slice. The VFO panel opens anchored to the marker.
2. Locate the **Filter edges button** in the VFO panel.
3. Click **Filter edges button** to toggle the filter edge lines off. Click it again to restore them.

The state is saved immediately. When you reopen AetherSDR, the setting is restored to whichever state you left it in for that slice.

## What each control does

| Control | Default | Persisted setting | Behavior |
|---------|---------|-------------------|----------|
| **RX antenna button** | — | Not persisted | Opens antenna selection menu for the receive antenna of this slice. |
| **TX antenna button** | — | Not persisted | Opens antenna selection menu for the transmit antenna of this slice. |
| **Frequency display** | — | Not persisted | Shows the current slice frequency. Click once to begin direct frequency entry; type MHz and press Enter or Tab. |
| **Filter width label** | — | Not persisted | Shows current filter bandwidth. Click to cycle through filter preset buttons in the Mode tab. Uses `RxApplet::formatFilterWidth` as the single source of truth, fixing a 0.1 kHz offset that affected SSB/digital mode readouts. |
| **AF Gain slider (Audio tab)** | 100 | Not persisted — reflects live radio state | Sets the audio output level for this slice. |
| **Pan slider (Audio tab)** | 50 | Not persisted | Sets left/right stereo pan for this slice. 50 = centre. |
| **Mute button (Audio tab)** | off | Not persisted | Mutes audio output for this slice without changing the AF gain setting. |
| **Squelch button + slider (Audio tab)** | off | Not persisted | Enables squelch for this slice. The adjacent slider sets the threshold. |
| **AGC combo (Audio tab)** | FAST | Not persisted | Sets the AGC attack/release speed for this slice. |
| **NR / NR2 / RN2 / NR4 / MNR / DFNR / BNR / NRL / NRS / RNN / NRF / MN buttons (DSP tab)** | off | Not persisted | Enables the corresponding noise reduction algorithm for this slice. Button availability depends on radio series and build. The **MN** button is shown only on radios that support manual notch filtering. Right-click NR2, NR4, MNR, DFNR, or MN to open the AetherDSP Settings dialog for that algorithm. |
| **ADSP button (DSP tab)** | — | Not persisted | Opens the AetherDSP Settings dialog (client-side NR2 / NR4 / DFNR / RN2 / BNR / MNR). Same entry point as the Settings menu. Styled like a radio-side DSP toggle but non-checkable. Click raises and focuses the modeless AetherDSP Settings dialog. |
| **AetherVoice button (DSP tab)** | — | Not persisted | Toggles the Aetherial Audio Channel Strip — the unified TX/RX DSP suite. Spans 2 columns in the 4-column DSP grid. |
| **Mode combo (Mode tab)** | USB | Not persisted | Sets the demodulation mode for this slice. |
| **Filter preset buttons (Mode tab)** | — | `FilterPresets` | Applies a saved filter width preset. Right-click to save the current filter width into that slot. Custom lo/hi edges can be set per slot via right-click. |
| **RIT / XIT buttons + labels (X/RIT tab)** | off | Not persisted | Enables receiver (RIT) or transmitter (XIT) incremental tuning. The label shows the current offset; scroll-wheel adjusts in 10 Hz steps. |
| **DAX channel combo (DAX tab)** | Off | Not persisted | Assigns a DAX audio channel to this slice. |
| **Marker thickness button** | 1 px | `Slice{N}_MarkerWidth` | Cycles the VFO marker line through Off, 1 px, and 3 px. Persisted per slice. |
| **Filter edges button** | Shown (edges visible) | `Slice{N}_FilterEdgesHidden` | Toggles the filter edge lines on the spectrum passband. Persisted per slice. |
| **Collapse toggle** | expanded | `SliceFlagCollapsed_{N}` | Collapses the VFO panel to a compact frequency-only strip. Persisted per slice. |

`{N}` is the slice number. Each slice stores its own value independently.

## Indicators

| Indicator | States | Meaning |
|-----------|--------|---------|
| **TX badge** | TX (red), hidden | Shown when this slice is the active transmit slice. |
| **SPLIT badge** | SPLIT (amber), hidden | Shown when TX is assigned to a different slice than the active receive slice. |

## Tips

- The filter edges setting is per-slice. Hiding filter edges on slice 0 does not affect slice 1 or any other slice.
- If you have collapsed the VFO panel to frequency-only view, expand it first by clicking the collapsed strip to access the **Filter edges button**.
- The VFO panel uses a custom `TabStack` widget that reports only the current tab's size hint, preventing a visual gap when switching between tabs of different heights.
- Tab labels in the VFO panel are implemented as `QPushButton`, making them keyboard-navigable with Tab. Use Tab to move focus between tabs, then press Enter or Space to activate the selected tab. Right-click the speaker tab (first tab) to toggle audio mute directly.
- Scroll-wheel tuning respects the reverse mouse wheel setting from InteractionSettings. Enable the reverse mouse wheel setting in Preferences to invert the scroll direction for VFO frequency tuning.
- The frequency display uses `FreqLineEdit` for direct frequency entry, with a hint showing "MHz (e.g. 14.225)". Direct frequency entry is cancelled when the slice becomes locked. Scroll-wheel tuning on a locked VFO notifies the user that tuning is blocked. The frequency display shows a **LOCKED** overlay when the slice VFO is locked.
- On XVTR bands, bare integers of 4+ digits with the slice in the 100-999 MHz range automatically insert a decimal after the third digit (e.g., 1446 → 144.6). Above 1000 MHz, bare integers are treated as the direct MHz value. Maximum frequency entry: 50000 MHz.
- Squelch is disabled for RTTY modes in addition to digital and CW modes. This prevents squelch from gating weak FSK signals sent to external decoders via DAX.
- Right-click the collapsed frequency strip to add a DX spot for the slice's VFO frequency. The spot is added at the VFO's actual frequency, not the cursor's step-snapped frequency.
- The **MN** (manual notch) DSP button appears only when the connected radio reports manual notch support. On radios without this capability, the button is hidden.

## Version history

- In v0.9.8, the **Filter width label** now uses `RxApplet::formatFilterWidth` as the single source of truth for formatting filter bandwidth, fixing a 0.1 kHz offset that affected SSB/digital mode readouts.
- In v0.9.8, several noise reduction buttons that were previously in the DSP tab (NR2, RN2, BNR, NR4, MNR, and DFNR) have been moved out of the VFO panel. Those algorithms are now toggled from the spectrum overlay menu and the AetherDSP applet.
- In v0.9.8, DSP toggle buttons (NB, NR, ANF, NRL, NRS, NRF, ANFL) now automatically push and pop the shared DSP-level slider stack when state changes arrive from the radio.
- In v26.5.1, squelch is disabled for RTTY modes.
- In v26.5.2.1, RX and TX antenna menus use the radio's reported per-slice antenna list when available. TX antenna menu filters out RX-only antenna ports. Frequency entry maximum for XVTR bands increased to 50000 MHz.
- In v26.5.3, the VFO panel uses a custom `TabStack` widget. Frequency display shows "LOCKED" overlay when slice VFO is locked.
- In v26.6.1, slider controls use theme-aware colour tokens. Pan slider uses centre-anchored fill. VFO panel assigned its own theming container scope (`spectrum/vfo`).
- In v26.6.3, tab labels implemented as `QPushButton` for keyboard navigation. Scroll-wheel tuning respects reverse mouse wheel setting. Frequency display uses `FreqLineEdit`. Accessibility support improved.
- In v26.7.4, the VFO panel shadow is rendered by a dedicated `FlagShadow` widget, keeping the shadow separate from live meter repaints to avoid re-blurring the entire flag at animation rate.
- In v26.8.4, the **MN** (manual notch) DSP toggle button was added to the DSP tab, shown only on radios that support manual notch filtering. Each DSP toggle button now has a stable object name for automation bridge compatibility. Right-clicking the collapsed frequency strip adds a DX spot for the slice's VFO frequency, using the actual VFO frequency instead of the cursor's step-snapped frequency.

## Related

- [Change the VFO marker line thickness](change-the-vfo-marker-line-thickness.md)
- [Collapse the VFO panel to frequency-only view](collapse-the-vfo-panel-to-frequency-only-view.md)
- [VFO Panel overview](overview.md)