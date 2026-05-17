# Use the VFO panel

The VFO panel is a floating per-slice control panel anchored to the VFO marker on the spectrum display. It provides quick access to the most frequently used per-slice settings — mode, filter presets, antenna selection, AF gain, pan, squelch, AGC, RIT/XIT, DSP noise reduction buttons, and DAX assignment — without leaving the spectrum view.

## Before you start

- Ensure the radio is connected and at least one slice is active.

## Open the VFO panel

Click the VFO marker flag on the spectrum display for the target slice. The VFO panel opens in expanded mode.

## Collapse or expand the VFO panel

Click the **Collapse toggle** button (arrow icon) at the right edge of the VFO panel title bar to collapse it to a compact frequency-only strip. Click again to expand.

## Use the tabs

The VFO panel contains several tabs:

- **Audio** tab — AF gain, pan, mute, squelch, and AGC controls
- **DSP** tab — noise reduction algorithm buttons (NR, NR2, RN2, NR4, MNR, DFNR, BNR, NRL, NRS, RNN, NRF), ADSP button, and AetherVoice button
- **Mode** tab — mode selection and filter preset buttons
- **X/RIT** tab — RIT and XIT incremental tuning
- **DAX** tab — DAX audio channel assignment

## What each control does

| Control | Tab | Label | Default | Valid range | Behavior |
|---------|-----|-------|---------|-------------|----------|
| RX antenna button | — | **RX** (icon) | — | — | Opens antenna selection menu for the receive antenna of this slice. The menu shows the radio's RX antenna list when available; otherwise falls back to the general antenna list. |
| TX antenna button | — | **TX** (icon) | — | — | Opens antenna selection menu for the transmit antenna of this slice. Only antennas suitable for transmission (not RX-only ports) are shown. |
| Frequency display | — | (frequency readout) | — | — | Shows the current slice frequency. Click once to begin direct frequency entry; type the frequency in MHz and press Enter or Tab. On XVTR bands, the maximum supported frequency is 50000 MHz. On 2m/70cm bands (100-999 MHz range), bare integers with 4-6 digits automatically insert a decimal after the third digit (e.g., 1446 → 144.6, 14696 → 146.96, 144600 → 144.600). On microwave bands a bare integer is interpreted directly as MHz. |
| Slice badge | — | (coloured badge with slice letter) | — | — | Shows the slice letter in a coloured badge. Supports rich text formatting for HTML rendering (#2606). Click to toggle focus on the corresponding slice. |
| Filter width label | — | (bandwidth readout) | — | — | Shows current filter bandwidth. Click to cycle through filter preset buttons in the Mode tab. Uses RxApplet::formatFilterWidth as the single source of truth. |
| AF Gain slider | Audio | — | 100 | 0-100 | Sets the audio output level for this slice. Not persisted. |
| Pan slider | Audio | — | 50 | 0-100 | Sets left/right stereo pan for this slice (50 = centre). |
| Mute button | Audio | **Mute** | off | — | Mutes audio output for this slice without changing the AF gain setting. |
| Squelch toggle button | Audio | **Squelch** | off | — | Enables or disables squelch for this slice. Disabled in DIGU, DIGL, CW, CWL, and RTTY modes. |
| Squelch slider | Audio | (adjacent to Squelch button) | — | 0-100 | Sets the squelch threshold. |
| AGC combo | Audio | **FAST** | FAST | FAST, MED, SLOW, OFF | Sets the AGC attack/release speed for this slice. |
| NR button | DSP | **NR** | off | — | Enables the corresponding noise reduction algorithm. Availability depends on radio series and build. |
| NR2 button | DSP | **NR2** | off | — | Enables the NR2 noise reduction algorithm. Right-click to open AetherDSP Settings. |
| RN2 button | DSP | **RN2** | off | — | Enables the RN2 noise reduction algorithm. |
| NR4 button | DSP | **NR4** | off | — | Enables the NR4 noise reduction algorithm. Right-click to open AetherDSP Settings. |
| MNR button | DSP | **MNR** | off | — | Enables the MNR noise reduction algorithm. Right-click to open AetherDSP Settings. |
| DFNR button | DSP | **DFNR** | off | — | Enables the DFNR noise reduction algorithm. Right-click to open AetherDSP Settings. |
| BNR button | DSP | **BNR** | off | — | Enables the BNR noise reduction algorithm. |
| NRL button | DSP | **NRL** | off | — | Enables the NRL noise reduction algorithm. |
| NRS button | DSP | **NRS** | off | — | Enables the NRS noise reduction algorithm. |
| RNN button | DSP | **RNN** | off | — | Enables the RNN noise reduction algorithm. |
| NRF button | DSP | **NRF** | off | — | Enables the NRF noise reduction algorithm. |
| ADSP button | DSP | **ADSP** | — | — | Opens the AetherDSP Settings dialog. Non-checkable. |
| AetherVoice button | DSP | **AetherVoice** | off (not checkable) | — | Toggles the Aetherial Audio Channel Strip. |
| Mode combo | Mode | **USB** | USB | USB, LSB, CW, CWL, AM, SAM, DIGU, DIGL, FM, NFM, DFM, RTTY | Sets the demodulation mode for this slice. |
| Filter preset buttons | Mode | **1**, **2**, **3**, **4** | — | — | Applies a saved filter width preset. Right-click to save the current filter width into that slot. |
| RIT toggle | X/RIT | **RIT** | off | — | Enables receiver incremental tuning. Scroll-wheel adjusts offset in 10 Hz steps. |
| XIT toggle | X/RIT | **XIT** | off | — | Enables transmitter incremental tuning. Scroll-wheel adjusts offset in 10 Hz steps. |
| RIT/XIT offset label | X/RIT | (offset readout) | — | — | Shows the current RIT or XIT offset. |
| DAX channel combo | DAX | **Off** | Off | Off, 1-8 | Assigns a DAX audio channel to this slice. |
| Marker thickness button | — | (line thickness icon) | 1 px | Off, 1 px, 3 px | Cycles the VFO marker line thickness. Persisted per slice. |
| Filter edges button | — | (filter edge icon) | shown | — | Toggles the filter edge lines on the spectrum passband. Persisted per slice. |
| Collapse toggle | — | (arrow icon) | expanded | — | Collapses the VFO panel to a compact frequency-only strip. Persisted per slice. |

## Indicators

| Indicator | States | Meaning |
|-----------|--------|---------|
| TX badge | TX (red), hidden | Shown when this slice is the active transmit slice. |
| SPLIT badge | SPLIT (amber), hidden | Shown when TX is assigned to a different slice than the active receive slice. |

---

# Open the Aetherial Audio Channel Strip from the VFO DSP tab

Opens the Aetherial Audio Channel Strip — the unified TX/RX DSP suite — directly from the VFO panel without navigating through menus.

## Before you start

- Ensure the radio is connected and at least one slice is active.
- The VFO panel must be visible on the spectrum display (click the VFO marker flag if collapsed).

## Steps

1. Click the VFO marker flag on the spectrum display for the target slice to open the VFO panel.
2. Locate the **AetherVoice** button on the DSP tab of the VFO panel.
3. Click **AetherVoice**. The Aetherial Audio Channel Strip appears.

## What each control does

| Control | Label | Default | Behavior |
|---------|-------|---------|----------|
| AetherVoice button | **AetherVoice** | off (not checkable) | Toggles the Aetherial Audio Channel Strip — the unified TX/RX DSP suite. Spans 2 columns in the 4-column DSP grid. |

## Related

- [Open AetherDSP Settings from the VFO DSP tab](open-aetherdsp-settings-from-the-vfo-dsp-tab.md)

---

# Open AetherDSP Settings from the VFO DSP tab

Opens the AetherDSP Settings dialog (client-side noise reduction algorithms) directly from the VFO panel without navigating through menus.

## Before you start

- Ensure the radio is connected and at least one slice is active.
- The VFO panel must be visible on the spectrum display (click the VFO marker flag if collapsed).

## Steps

1. Click the VFO marker flag on the spectrum display for the target slice to open the VFO panel.
2. Locate the **ADSP** button on the DSP tab of the VFO panel.
3. Click **ADSP**. The AetherDSP Settings dialog appears.

## What each control does

| Control | Label | Default | Behavior |
|---------|-------|---------|----------|
| ADSP button | **ADSP** | n/a | Opens the AetherDSP Settings dialog (client-side NR2 / NR4 / DFNR / RN2 / BNR / MNR). Non-checkable. Click raises and focuses the modeless dialog. |

## Notes

- Right-click the **NR2**, **NR4**, **MNR**, or **DFNR** buttons to open the AetherDSP Settings dialog for that specific algorithm.

## Related

- [Open Aetherial Audio Channel Strip from the VFO DSP tab](open-aetherial-audio-channel-strip-from-the-vfo-dsp-tab.md)

---

# Use squelch on a VFO panel

Enables or disables squelch for a slice and adjusts the squelch threshold from the VFO panel on the spectrum display.

## Before you start

- Ensure the radio is connected and at least one slice is active.
- The VFO panel must be visible on the spectrum display (click the VFO marker flag if collapsed).

## Steps

1. Click the VFO marker flag on the spectrum display for the target slice to open the VFO panel.
2. Click the **Audio** tab.
3. Click the **Squelch** toggle button to enable squelch for this slice.
4. Drag the adjacent slider to set the squelch threshold (0-100).

## Important notes

- Squelch is automatically disabled in **DIGU**, **DIGL**, **CW**, **CWL**, and **RTTY** modes. In digital, RTTY, and CW modes, audio feeds external decoders via DAX, where squelch is not meaningful and can gate weak signals. In CW mode, the radio also locks squelch on at a fixed level and rejects client-side changes.
- When switching to a mode where squelch is disabled, the squelch state is saved and restored when switching back to a voice or FM mode.
- Squelch settings are not persisted and reflect live radio state only.

## What each control does

| Control | Label | Default | Valid range | Behavior |
|---------|-------|---------|-------------|----------|
| Squelch toggle button | **Squelch** | off | — | Enables or disables squelch for this slice. |
| Squelch slider | (adjacent to Squelch button) | — | 0-100 | Sets the squelch threshold. |