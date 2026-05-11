# VFO Panel

The VFO Panel is a floating per-slice control panel anchored to the VFO marker on the spectrum display. It provides quick access to the most frequently used per-slice settings — mode, filter presets, antenna selection, AF gain, pan, squelch, AGC, RIT/XIT, DSP noise reduction buttons, and DAX assignment — without leaving the spectrum view. The panel can collapse to a compact frequency-only strip.

## Opening the VFO Panel

1. On the spectrum display, click the VFO marker flag (the small triangle or flag at the top of the VFO marker line).
2. The VFO Panel opens as a floating window anchored to the marker.

## Controls

The VFO Panel is organized into tabs: Audio, DSP, Mode, X/RIT, and DAX.

### Common Controls (always visible)

| Control | Type | Description |
|---------|------|-------------|
| RX antenna button | Push button | Opens antenna selection menu for the receive antenna of this slice. |
| TX antenna button | Push button | Opens antenna selection menu for the transmit antenna of this slice. |
| Frequency display | Indicator | Shows the current slice frequency. Click once to begin direct frequency entry; type MHz and press Enter or Tab. |
| Filter width label | Indicator | Shows current filter bandwidth. Click to cycle through filter preset buttons in the Mode tab. Uses a consistent formatting method to ensure accurate readouts. |
| TX badge | Indicator | Shown (red) when this slice is the active transmit slice. Hidden otherwise. |
| SPLIT badge | Indicator | Shown (amber) when TX is assigned to a different slice than the active receive slice. Hidden otherwise. |
| Marker thickness button | Push button | Cycles the VFO marker line through Off, 1 px, and 3 px. Setting is persisted per slice. |
| Filter edges button | Toggle button | Toggles the filter edge lines on the spectrum passband. Setting is persisted per slice. Default: shown. |
| Collapse toggle | Toggle button | Collapses the VFO panel to a compact frequency-only strip. Setting is persisted per slice. Default: expanded. |

### Audio Tab

| Control | Type | Range | Description |
|---------|------|-------|-------------|
| AF Gain slider | Slider | 0-100 | Sets the audio output level for this slice. Default: 100. Not persisted — reflects live radio state. |
| Pan slider | Slider | 0-100 | Sets left/right stereo pan for this slice. 50 = centre. Default: 50. |
| Mute button | Toggle button | On/Off | Mutes audio output for this slice without changing the AF gain setting. Default: off. |
| Squelch button + slider | Toggle button + slider | 0-100 | Enables squelch for this slice. The adjacent slider sets the threshold. Default: off. Squelch is automatically disabled in digital, RTTY, and CW modes. |
| AGC combo | Combo box | FAST, MED, SLOW, OFF | Sets the AGC attack/release speed for this slice. Default: FAST. |

### DSP Tab

| Control | Type | Description |
|---------|------|-------------|
| NR / NR2 / RN2 / NR4 / MNR / DFNR / BNR / NRL / NRS / RNN / NRF buttons | Toggle button | Enables the corresponding noise reduction algorithm for this slice. Button availability depends on radio series and build. Default: off. Right-click NR2, NR4, MNR, or DFNR to open the AetherDSP Settings dialog for that algorithm. |
| ADSP button | Push button | Opens the AetherDSP Settings dialog (client-side NR2 / NR4 / DFNR / RN2 / BNR / MNR). Same entry point as the Settings menu. Click raises and focuses the modeless AetherDSP Settings dialog. |
| AetherVoice button | Push button | Toggles the Aetherial Audio Channel Strip — the unified TX/RX DSP suite. Spans 2 columns in the 4-column DSP grid. |

### Mode Tab

| Control | Type | Range | Description |
|---------|------|-------|-------------|
| Mode combo | Combo box | USB, LSB, CW, CWL, AM, SAM, DIGU, DIGL, FM, NFM, DFM, RTTY | Sets the demodulation mode for this slice. Default: USB. |
| Filter preset buttons | Push button | N/A | Applies a saved filter width preset. Right-click to save the current filter width into that slot. Persisted in FilterPresets. |

### X/RIT Tab

| Control | Type | Description |
|---------|------|-------------|
| RIT button + label | Toggle button + indicator | Enables receiver incremental tuning. The label shows the current offset; scroll-wheel adjusts in 10 Hz steps. Default: off. |
| XIT button + label | Toggle button + indicator | Enables transmitter incremental tuning. The label shows the current offset; scroll-wheel adjusts in 10 Hz steps. Default: off. |

### DAX Tab

| Control | Type | Range | Description |
|---------|------|-------|-------------|
| DAX channel combo | Combo box | Off, 1-8 | Assigns a DAX audio channel to this slice. Default: Off. |

## Squelch Behavior

Squelch is automatically disabled in digital, RTTY, and CW modes:
- **Digital and RTTY**: Audio feeds external decoders via DAX; squelch is not meaningful and can gate weak FSK signals.
- **CW**: The radio locks squelch on at a fixed level and rejects changes from the client.

When switching to a mode where squelch is disabled while squelch is active, the system saves the squelch state and turns it off. When switching back to a mode where squelch is allowed, the previous squelch state is restored.

## Open AetherDSP Settings from the VFO DSP tab

Open the AetherDSP Settings dialog from the VFO Panel's DSP tab to adjust advanced noise reduction parameters for NR2, NR4, DFNR, or MNR algorithms.

### Before you start

- A slice must be active and connected to a radio.
- The VFO Panel must be open for the slice you want to configure (click the VFO marker flag on the spectrum display).

### Steps

1. In the VFO Panel, click the **DSP** tab label to show the noise reduction controls.
2. Click the **ADSP** button.  
   The AetherDSP Settings dialog opens as a modeless window; it can stay open while you continue operating the radio.

Alternatively, you can right-click any of the NR2, NR4, MNR, or DFNR toggle buttons in the DSP tab to open the AetherDSP Settings dialog for that specific algorithm.

### Tips

- The AetherDSP Settings dialog can also be opened from `Settings > AetherDSP Settings...` in the main menu.
- Right-clicking a noise reduction button (NR2, NR4, MNR, or DFNR) opens the dialog focused on that algorithm's controls.

### Related

- [Enable noise reduction from the VFO panel](enable-noise-reduction-from-the-vfo-panel.md)