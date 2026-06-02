# Adjust AF gain and pan from the VFO panel

Use the Audio tab in the VFO panel to set the audio output level and stereo pan position for any receive slice independently of other slices.

## Before you start

- AetherSDR must be connected to the radio. The VFO panel requires an active radio connection.
- The VFO panel for the target slice must be open. If it is collapsed to a frequency-only strip, click anywhere on the collapsed strip to expand it.

## Steps

1. Click the VFO marker flag on the spectrum display for the slice you want to adjust. The VFO panel opens anchored to the marker.
2. Click the **Audio** tab inside the VFO panel.
3. To set the audio output level, drag the **AF Gain slider** left or right. The default is 100; the valid range is 0–100.
4. To set the stereo position, drag the **Pan slider** left or right. The default is 50 (centre); the valid range is 0–100. A value below 50 moves audio toward the left channel; above 50 toward the right.

## What each control does

| Control | Default | Range |
|---|---|---|
| AF Gain slider (Audio tab) | 100 | 0–100 |
| Pan slider (Audio tab) | 50 | 0–100 |
| Mute button (Audio tab) | off | — |
| Squelch button + slider (Audio tab) | off | 0–100 |
| AGC combo (Audio tab) | FAST | FAST \| MED \| SLOW \| OFF |
| ADSP button (DSP tab) | Opens the AetherDSP Settings dialog (client-side NR2 / NR4 / DFNR / RN2 / BNR / MNR). Same entry point as the Settings menu (v0.9.8). | Styled like a radio-side DSP toggle but non-checkable. Click raises and focuses the modeless AetherDSP Settings dialog. |
| AetherVoice button (DSP tab) | Toggles the Aetherial Audio Channel Strip — the unified TX/RX DSP suite (v0.9.8). | Spans 2 columns in the 4-column DSP grid. Matches the existing menu / chain entry points for the strip. |
| NR / NR2 / RN2 / NR4 / MNR / DFNR / BNR / NRL / NRS / RNN / NRF buttons (DSP tab) | off | Enables the corresponding noise reduction algorithm for this slice. Button availability depends on radio series and build. Right-click NR2, NR4, MNR, or DFNR to open the AetherDSP Settings dialog for that algorithm. |
| RX antenna button | — | Opens antenna selection menu for the receive antenna of this slice. |
| TX antenna button | — | Opens antenna selection menu for the transmit antenna of this slice. |
| Frequency display | — | Shows the current slice frequency. Click once to begin direct frequency entry; type MHz and press Enter or Tab. |
| Filter width label | — | Shows current filter bandwidth. Click to cycle through filter preset buttons in the Mode tab. Uses RxApplet::formatFilterWidth as the single source of truth, fixing a 0.1 kHz offset that affected SSB/digital mode readouts (#2197, v0.9.8). |
| Mode combo (Mode tab) | USB | USB \| LSB \| CW \| CWL \| AM \| SAM \| DIGU \| DIGL \| FM \| NFM \| DFM \| RTTY |
| Filter preset buttons (Mode tab) | — | Applies a saved filter width preset. Right-click to save the current filter width into that slot. Persisted in FilterPresets. Custom lo/hi edges can be set per slot via right-click. |
| RIT / XIT buttons + labels (X/RIT tab) | off | Enables receiver (RIT) or transmitter (XIT) incremental tuning. The label shows the current offset; scroll-wheel adjusts in 10 Hz steps. |
| DAX channel combo (DAX tab) | Off | Off \| 1–8 |
| Marker thickness button | 1 px | Off \| 1 px \| 3 px. Cycles the VFO marker line through these options. Persisted per slice. |
| Filter edges button | shown | Toggles the filter edge lines on the spectrum passband. Persisted per slice. |
| Collapse toggle | expanded | Collapses the VFO panel to a compact frequency-only strip. Persisted per slice. |
| TX badge | — | Shown (red) when this slice is the active transmit slice. |
| SPLIT badge | — | Shown (amber) when TX is assigned to a different slice than the active receive slice. |

## Tips

- Double-clicking either slider resets it to its default value: 100 for AF Gain, 50 for Pan.
- AF gain is per-slice. Adjusting one slice does not affect any other slice.
- To silence a slice without moving the AF Gain slider, use the **Mute button** on the Audio tab instead. Muting does not change the stored gain value.

## Pan slider centre mark (v26.6.1)

The Pan slider now paints a centre-mark dot on the groove and fills the groove from the centre outward when the handle is off-centre. This provides a clear visual indication of the neutral position. The fill uses the theme's accent colour on the side toward which the handle is moved, and the background colour on the opposite side.

## Filter width label changes in v0.9.8

The filter width label now uses `RxApplet::formatFilterWidth` as its single source of truth. This fixes a 0.1 kHz offset that previously affected SSB and digital mode readouts (#2197, v0.9.8). The label now stays in sync with the filter readout in the RX applet.

## Squelch behavior for RTTY mode (v26.5.1)

The squelch button and slider are now disabled in RTTY mode, in addition to digital and CW modes. This prevents squelch from gating weak FSK signals when the audio feeds external decoders via DAX (#2504).

## DSP tab changes in v0.9.7

The DSP tab in the VFO panel shows the following noise reduction buttons when available from the radio:

| Button | Algorithm |
|---|---|
| NR | Noise reduction |
| NB | Noise blanker |
| ANF | Automatic notch filter |
| APF | Audio peaking filter (CW mode only) |
| NRL | Noise reduction level |
| NRS | Spectral subtraction |
| RNN | RNN noise reduction |
| NRF | Spectral noise filter |
| ANFL | LMS notch filter |
| ANFT | FFT notch filter |

Right-click NR2, NR4, MNR, or DFNR to open the AetherDSP Settings dialog for that algorithm.

### ADSP button (v0.9.8)

The DSP tab now includes an **ADSP button** that opens the AetherDSP Settings dialog. This button provides the same entry point as the Settings menu. It is styled like a radio-side DSP toggle but is non-checkable. Click it to raise and focus the modeless AetherDSP Settings dialog.

### AetherVoice button (v0.9.8)

The DSP tab also includes an **AetherVoice button** that toggles the Aetherial Audio Channel Strip — the unified TX/RX DSP suite. This button spans 2 columns in the 4-column DSP grid and matches existing menu and chain entry points for the strip.

### DSP level slider

A shared level slider now appears below the DSP button grid. The slider retargets automatically to whichever leveled DSP algorithm was most recently enabled. The label to the left of the slider shows the name of the currently targeted algorithm, and the numeric value is shown to the right.

Important change in v0.9.8: The DSP level slider now properly appears on startup for any DSP that was enabled in the radio's saved profile. Previously the slider was missing until manually toggling the algorithm (#startup-slider). This affects NB, NR, ANF, NRL, NRS, NRF, and ANFL.

The slider row remains laid out at all times. When no leveled algorithm is active — or when only RNN, ANFT, or APF is on — the slider row fades out and does not respond to clicks.

| Control | Range | Behavior |
|---|---|---|
| DSP level slider | 0–100 | Sets the level for the most recently enabled leveled DSP algorithm. Retargets automatically when you switch algorithms. Hidden (faded) when no leveled algorithm is active. |

## Antenna selection (v26.5.2.1)

The RX antenna and TX antenna buttons open context menus showing available antenna ports for the current slice.

- The RX antenna menu displays antennas from the slice's dedicated RX antenna list when available, falling back to the global antenna list.
- The TX antenna menu automatically filters out RX-only antenna ports. Antenna ports starting with "RX" are excluded from the TX selection.
- Each menu entry shows the antenna name. The currently selected antenna is marked with a checkmark.

## VFO panel indicators

The VFO panel includes two indicators that appear when certain conditions are met:

- **TX badge (red)**: Shown when this slice is the active transmit slice.
- **SPLIT badge (amber)**: Shown when TX is assigned to a different slice than the active receive slice.

The slice badge displays the slice letter and uses rich text format for proper rendering.

## Frequency entry for XVTR bands (v26.5.2.1)

When entering frequencies on XVTR bands (slice frequency above 54 MHz or RX antenna starting with "XVT"):

- The maximum accepted frequency is 50000 MHz.
- For slices in the 100–999 MHz range (2m/70cm bands), bare integers are automatically formatted with a decimal after the third digit. For example, entering 1446 becomes 144.6, 14696 becomes 146.96, and 144600 becomes 144.600.
- For microwave bands (23cm and above, 1000 MHz and higher), bare integers are treated as the exact MHz value. For example, 1296 becomes 1296 MHz.

## Frequency entry with explicit MHz (v26.5.3)

When entering frequencies, the VFO panel uses `FrequencyEntryParser` for accurate parsing. If you enter a frequency explicitly in MHz (e.g., 146.520 or 144.390), the input is accepted as MHz even if the value exceeds 54 MHz. This allows direct MHz entry for VHF and UHF frequencies without requiring XVTR band detection.

## Locked slice behavior (v26.5.3)

When a slice is locked:
- The **Lock VFO button** in the VFO panel shows a lock icon. Clicking the button toggles the lock state.
- When locked, the frequency display shows a locked overlay indicator.
- Scroll-wheel tuning is blocked. If you attempt to scroll while locked, the slice emits a "tune blocked by lock" notification.
- Direct frequency entry is blocked. Any in-progress direct entry is cancelled when the slice is locked.
- The VFO panel updates the frequency label to show the locked state.

## Theming and button styling (v26.6.1)

- The VFO panel uses the `spectrum/vfo` theming container. This keeps VFO flags on their own theming surface, separate from the main spectrum scope.
- The **Marker thickness button** now uses theme-aware colours for its background and pressed states: `color.background.1` for normal and hover backgrounds, `color.accent` for the pressed state.

## Tab stack height fix (v26.5.3)

The VFO panel tab content now properly sizes itself to the current tab's contents. This fixes a gap that could appear inside the Mode tab when the DSP tab was taller (e.g., when the DIGU/DIGL sub-mode was visible). The tab stack now reports only the current page's preferred size rather than the maximum of all pages.

## Related

- [Mute audio for a slice from the VFO panel](mute-audio-for-a-slice-from-the-vfo-panel.md)
- [Enable squelch from the VFO panel](enable-squelch-from-the-vfo-panel.md)
- [Collapse the VFO panel to frequency-only view](collapse-the-vfo-panel-to-frequency-only-view.md)
- [VFO Panel overview](overview.md)