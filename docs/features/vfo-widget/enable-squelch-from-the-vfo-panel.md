# Enable squelch from the VFO panel

Squelch mutes audio for a slice when the received signal falls below a set threshold. Use this to silence background noise on FM, AM, or digital modes when no signal is present.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- The VFO panel for the target slice must be open. If it is not, click the VFO marker flag on the spectrum display for that slice.
- If the VFO panel is collapsed to the frequency-only strip, click it once to expand it.

## Steps

1. Open the VFO panel by clicking the VFO marker flag on the spectrum display for the slice you want to configure.
2. Click the **Audio** tab inside the VFO panel.
3. Click the **Squelch button** to enable squelch. The button activates and squelch is applied to the slice immediately.
4. Drag the adjacent squelch slider left or right to set the threshold. The valid range is 0–100.

To disable squelch, click the **Squelch button** again.

## What each control does

| Control                      | Default                                                                                                                               | Valid range                                                                                                             |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| RX antenna button            | Radio default                                                                                                                         | Radio antenna list                                                                                                      |
| TX antenna button            | Radio default                                                                                                                         | Radio antenna list (RX-only ports excluded)                                                                             |
| Frequency display            | Current slice frequency                                                                                                               | 0.001–50000 MHz                                                                                                         |
| Filter width label           | Current filter bandwidth                                                                                                              | Per mode filter presets                                                                                                 |
| AF Gain slider (Audio tab)   | 100                                                                                                                                   | 0–100                                                                                                                   |
| Pan slider (Audio tab)       | 50                                                                                                                                    | 0–100                                                                                                                   |
| Mute button (Audio tab)      | Off                                                                                                                                   | On / Off                                                                                                                |
| Squelch button (Audio tab)   | Off                                                                                                                                   | On / Off                                                                                                                |
| Squelch slider (Audio tab)   | —                                                                                                                                     | 0–100                                                                                                                   |
| AGC combo (Audio tab)        | FAST                                                                                                                                  | FAST / MED / SLOW / OFF                                                                                                 |
| Mode combo (Mode tab)        | USB                                                                                                                                   | USB / LSB / CW / CWL / AM / SAM / DIGU / DIGL / FM / NFM / DFM / RTTY                                                    |
| Filter preset buttons (Mode tab) | —                                                                                                                                | Per saved preset                                                                                                        |
| RIT / XIT buttons (X/RIT tab) | Off                                                                                                                                   | On / Off                                                                                                                |
| DAX channel combo (DAX tab)  | Off                                                                                                                                   | Off / 1–8                                                                                                               |
| Marker thickness button      | 1 px                                                                                                                                  | Off / 1 px / 3 px                                                                                                      |
| Filter edges button          | Shown                                                                                                                                 | On / Off                                                                                                                |
| Collapse toggle              | Expanded                                                                                                                              | On / Off                                                                                                                |
| ADSP button (DSP tab)        | Opens the AetherDSP Settings dialog (client-side NR2 / NR4 / DFNR / RN2 / BNR / MNR). Same entry point as the Settings menu (v0.9.8). | Styled like a radio-side DSP toggle but non-checkable. Click raises and focuses the modeless AetherDSP Settings dialog. |
| AetherVoice button (DSP tab) | Toggles the Aetherial Audio Channel Strip — the unified TX/RX DSP suite (v0.9.8).                                                     | Spans 2 columns in the 4-column DSP grid. Matches the existing menu / chain entry points for the strip.                 |

Neither the button state nor the slider position is persisted as an AetherSDR AppSettings key — both reflect live radio state.

## Tips

- Set the slider just above the noise floor to prevent the audio from cutting in and out on weak signals.
- The squelch threshold interacts with the AGC setting. If you change the AGC mode using the **AGC combo**, you may need to readjust the squelch slider.

## DSP tab changes in v0.9.8

The **DSP tab** of the VFO panel received two new launcher buttons in v0.9.8:

| New button | Behavior |
|---|---|
| ADSP button | Opens the AetherDSP Settings dialog (client-side NR2 / NR4 / DFNR / RN2 / BNR / MNR). Same entry point as the Settings menu. Non-checkable button styled like a radio-side DSP toggle. |
| AetherVoice button | Toggles the Aetherial Audio Channel Strip — the unified TX/RX DSP suite. Spans 2 columns in the 4-column DSP grid. Non-checkable button. |

Both buttons are placed at the end of the DSP button grid. ADSP occupies 1 column, and AetherVoice occupies the adjacent 2 columns.

### Startup DSP level synchronization

In v0.9.8, the DSP level slider synchronization was improved. When radio-side DSP buttons (NR, NB, ANF, NRL, NRS, NRF, ANFL) are enabled in the radio's saved profile, the corresponding DSP level slider is now pushed onto the shared level stack at startup. Previously, the level slider was missing until the user manually toggled the DSP button. This fixes issue #startup-slider.

### DSP level slider

A shared **DSP level slider** row appears below the DSP button grid. The slider targets whichever leveled DSP button was most recently turned on. The label to the left of the slider shows the active target (for example, **NR** or **NB**). The numeric value is shown to the right.

The slider row is always present in the layout. When no leveled DSP is active — or when only RNN, ANFT, or APF is on — the row fades out and does not respond to interaction. It becomes fully visible again as soon as a compatible DSP button is enabled.

Leveled DSP targets supported by the slider:

| Target | Controlled by |
|---|---|
| NR | `setNrLevel` |
| NB | `setNbLevel` |
| ANF | `setAnfLevel` |
| NRL | `setNrlLevel` |
| NRS | `setNrsLevel` |
| NRF | `setNrfLevel` |
| ANFL | `setAnflLevel` |

The slider range is 0–100. The level value is not persisted as an AetherSDR AppSettings key — it reflects live radio state.

## Filter width label fix in v0.9.8

The **Filter width label** in the VFO panel now uses `RxApplet::formatFilterWidth` as its single source of truth. This fixes a 0.1 kHz offset that previously affected SSB and digital mode filter readouts (issues #794, #1225, #2197). The label now stays in sync with the RX applet's filter display.

## Squelch behavior for RTTY mode (v26.5.1)

Starting in v26.5.1, squelch is also disabled when the slice is set to RTTY mode. This change addresses issue #2504, where squelch was gating weak FSK signals used by external decoders via DAX. The squelch button and slider are automatically disabled when RTTY mode is active, matching the existing behavior for digital and CW modes.

If squelch was enabled when switching to RTTY mode, AetherSDR saves the squelch state and restores it when you switch back to a voice or FM mode.

## Antenna selection changes in v26.5.2.1

Starting in v26.5.2.1, the RX and TX antenna selection menus in the VFO panel have been improved:

| Change | Description |
|---|---|
| RX antenna menu | Now uses the slice's `rxAntennaList()` when available, falling back to the radio's master antenna list. Each menu item stores the antenna name as data, and the item text is generated by `antennaMenuLabel()` for consistent formatting. |
| TX antenna menu | Uses the `txAntennaOptions()` method to build the list, which automatically excludes RX-only antenna ports. Antennas with names starting with "RX" are filtered out. The `likelyTxAntennaFallbackToken()` helper determines which antennas are likely TX-capable when a dedicated TX antenna list is not available. |
| Tooltip and status tip | Each menu item now shows the raw antenna name as a tooltip and status tip, providing full name visibility when the formatted label is truncated. |

### TX antenna filtering logic

The TX antenna menu uses the following logic to determine which antennas to show:

1. If a dedicated TX antenna list is available from the radio, use it directly.
2. Otherwise, filter the master antenna list to exclude ports that start with "RX".
3. The `likelyTxAntennaFallbackToken()` helper identifies TX-capable antennas by checking if they start with "ANT", "TX", or equal "XVTR".

## Frequency entry changes in v26.5.2.1

The frequency entry logic for XVTR bands has been updated in v26.5.2.1:

| Change | Description |
|---|---|
| Maximum frequency limit | Increased from 450 MHz to 50000 MHz to support microwave bands. |
| 3-digit band convenience | The automatic decimal insertion (e.g., 1446 → 144.6) now only applies when the slice is in a 100–999 MHz band. For 23cm and higher bands, a bare integer is interpreted as the full MHz value (e.g., 1296 means 1296 MHz, not 129.6 MHz). |

### Frequency entry rules for XVTR bands

When entering frequencies on XVTR bands:

- **100–999 MHz band**: Enter a bare integer with at least 4 digits to have the decimal automatically inserted after the 3rd digit (e.g., 144600 → 144.600, 14696 → 146.96).
- **1000 MHz and above**: Enter the full MHz value directly (e.g., 1296 for 23cm means 1296.000 MHz).
- You can always enter a decimal point manually to bypass the automatic insertion.

## Related

- [Adjust AF gain and pan from the VFO panel](adjust-af-gain-and-pan-from-the-vfo-panel.md)
- [Mute audio for a slice from the VFO panel](mute-audio-for-a-slice-from-the-vfo-panel.md)
- [VFO Panel overview](overview.md)