# Apply a filter width preset from the VFO panel

Filter preset buttons let you switch the receive filter width for a slice with a single click. Use them to move quickly between common bandwidths — for example, between a wide 3 kHz SSB filter and a narrow 500 Hz CW filter — without leaving the spectrum view.

## Before you start

- AetherSDR must be connected to the radio. The VFO panel requires an active radio connection.
- The VFO panel for the target slice must be open and expanded. If it is collapsed to a frequency-only strip, click anywhere on it to expand it first.

## Steps

1. Click the VFO marker flag on the spectrum display for the slice you want to adjust. The VFO panel opens, anchored to the left of the marker.
2. Click the **Mode** tab inside the VFO panel.
3. Click the filter preset button that corresponds to the bandwidth you want. The radio immediately applies that filter width to the slice.

To save the current filter width into a preset slot:

1. Set the filter to the bandwidth you want to save (see [Set a custom filter edge from the VFO panel](set-a-custom-filter-edge-from-the-vfo-panel.md)).
2. Right-click the preset button slot you want to overwrite.
3. The current filter width is saved into that slot.

## What each control does

| Control                          | Behavior                                                                                                                                                                                                                                       | Default                                                                                                                 |
|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Filter preset buttons (Mode tab) | Each button applies a saved filter width preset to the slice. Left-click to apply; right-click to save the current filter width into that slot. Custom low and high filter edges can be stored per slot via right-click.                       | —                                                                                                                       |
| Filter width label               | Shows current filter bandwidth. Click to cycle through filter preset buttons in the Mode tab. Uses RxApplet::formatFilterWidth as the single source of truth, fixing a 0.1 kHz offset that affected SSB/digital mode readouts (#2197, v0.9.8). |                                                                                                                         |
| ADSP button (DSP tab)            | Opens the AetherDSP Settings dialog (client-side NR2 / NR4 / DFNR / RN2 / BNR / MNR). Same entry point as the Settings menu (v0.9.8).                                                                                                          | Styled like a radio-side DSP toggle but non-checkable. Click raises and focuses the modeless AetherDSP Settings dialog. |
| AetherVoice button (DSP tab)     | Toggles the Aetherial Audio Channel Strip — the unified TX/RX DSP suite (v0.9.8).                                                                                                                                                              | Spans 2 columns in the 4-column DSP grid. Matches the existing menu / chain entry points for the strip.                 |
| Lock VFO button                  | Toggles frequency lock for this slice. When locked, the frequency display shows a "LOCKED" indicator and scroll-wheel tuning is blocked. Direct frequency entry is also blocked. Unlock clears the overlay.                                    | off                                                                                                                     |

## DSP tab changes in v0.9.8

The **DSP tab** now shows only radio-side noise reduction buttons. The following buttons have been removed from the VFO panel DSP tab:

- **NR2**
- **RN2**
- **BNR**
- **NR4**
- **MNR**
- **DFNR**

These client-side DSP modules are now accessed through the spectrum overlay menu and the AetherDSP applet. Toggle them there instead of from the VFO panel.

The buttons that remain in the DSP tab are arranged in a four-column grid, followed by the ADSP and AetherVoice launcher buttons:

| Position | Button |
|---|---|
| Row 1, col 1 | NR |
| Row 1, col 2 | NB |
| Row 1, col 3 | ANF |
| Row 1, col 4 | APF (visible in CW mode only) |
| Row 2, col 1 | NRL |
| Row 2, col 2 | NRS |
| Row 2, col 3 | RNN |
| Row 2, col 4 | NRF |
| Row 3, col 1 | ANFL |
| Row 3, col 2 | ANFT |
| Row 4, col 1 | ADSP |
| Row 4, cols 2–3 | AetherVoice |

A shared **DSP level slider** row appears below the button grid. The slider retargets automatically to whichever leveled DSP button was most recently turned on. In v0.9.8, when a DSP level state change arrives from the radio (for example, when the radio's saved profile has NR enabled on startup), the slider appears immediately without requiring manual re-toggle. Its label shows the name of the current target (for example, **NR** or **NB**), and the value to the right of the slider shows the current level numerically. When no leveled DSP algorithm is active — or when only RNN, ANFT, or APF is on — the slider row is present in the layout but visually faded out. Clicking it while faded has no effect.

| Control | Behavior | Default | Setting key |
|---|---|---|---|
| NR / NB / ANF / APF / NRL / NRS / RNN / NRF / ANFL / ANFT buttons (DSP tab) | Enables the corresponding radio-side noise reduction or filtering algorithm for this slice. APF is visible in CW mode only. | off | — |
| DSP level slider (DSP tab) | Sets the processing level for the most recently activated leveled DSP algorithm. The label to the left identifies the current target. Automatically activates on startup if the radio's saved profile has a leveled DSP enabled. Hidden (faded) when no leveled algorithm is active. | — | — |
| ADSP button (DSP tab) | Opens the AetherDSP Settings dialog (client-side NR2 / NR4 / DFNR / RN2 / BNR / MNR). Non-checkable push button. | — | — |
| AetherVoice button (DSP tab) | Opens the Aetherial Audio Channel Strip — the unified TX/RX DSP suite. Non-checkable push button. Spans 2 columns in the 4-column DSP grid. | — | — |

## Squelch behavior changes (v26.5.1)

The squelch control in the **Audio tab** is now disabled for RTTY and digital modes, in addition to CW mode. This prevents the squelch from gating weak FSK signals that are fed to external decoders via DAX (#2504).

When you switch a slice to DIGU, DIGL, or RTTY mode:

- The Squelch button and slider become disabled.
- If squelch was active, it is automatically turned off. The previous state is saved internally and restored if you switch back to a voice mode.

This matches the existing behavior for CW mode, where the radio locks squelch on at a fixed level and rejects user changes.

## Antenna selection changes (v26.5.2.1)

The **RX antenna** and **TX antenna** buttons now use improved menus:

- The RX antenna menu uses the slice's `rxAntennaList()` when available, falling back to the global antenna list for legacy compatibility.
- The TX antenna menu intelligently filters out RX-only antenna ports by checking for "RX" prefixes, "ANT" prefixes, "TX" prefixes, or "XVTR" as fallback tokens.
- Menu items now store the antenna identifier as data, allowing selection by internal name rather than displayed label.
- Each menu item includes a tooltip and status tip showing the antenna identifier.

### Frequency entry improvements (v26.5.2.1)

The frequency entry logic has been updated to better handle transverter (XVTR) bands:

- The maximum XVTR frequency has been increased from 450 MHz to 50000 MHz to support microwave bands.
- The "three-digit band" convenience parsing (inserting a decimal after the third digit for bare integers like 1446 → 144.6 MHz) now only activates when the slice frequency is between 100 MHz and 999 MHz. For 23 cm and microwave bands (above 1000 MHz), a bare integer like 1296 is treated as 1296 MHz directly.

### Frequency entry improvements (v26.5.3)

The frequency entry logic now uses the `FrequencyEntryParser` utility class for consistent parsing across the application:

- Explicit MHz entry (typing a frequency greater than 54 MHz) is now recognized on HF bands as well, allowing direct MHz entry without being on an XVTR band.
- The `normalizedMhzText()` method handles multi-dot formats like "14.225.000" by removing dots beyond the first, ensuring consistent parsing.
- Direct frequency entry is blocked when the slice is locked. Attempting to enter a frequency while locked produces no action.

### Slice badge rendering (v26.5.2.1)

The slice letter badge now renders as Qt Rich Text (`Qt::RichText`), fixing an issue where certain slice letters displayed incorrectly (#2606). The badge styling remains the same.

| Control | Behavior | Default | Setting key |
|---|---|---|---|
| RX antenna button | Opens an antenna selection menu for the receive antenna of this slice. Uses slice-specific antenna list when available. Menu items display tooltip and status tip. | — | — |
| TX antenna button | Opens an antenna selection menu for the transmit antenna of this slice. Automatically filters out RX-only antenna ports. Menu items display tooltip and status tip. | — | — |

## Lock VFO behavior (v26.5.3)

The VFO lock button now fully blocks all tuning operations when engaged:

- Scroll-wheel tuning is blocked, and a `tuneBlockedByLock` notification is sent to the slice, which cancels any in-progress direct frequency entry.
- The lock state is reflected in the frequency display label, which shows a "LOCKED" overlay when locked.
- Unlocking the VFO clears the overlay and restores normal tuning behavior.
- When the VFO is locked, the lock button shows a lock emoji (🔒); when unlocked, it shows an unlocked emoji (🔓).

| Control | Behavior | Default | Setting key |
|---|---|---|---|
| Lock VFO button | Toggles frequency lock for this slice. When locked, scroll-wheel tuning and direct frequency entry are blocked. | off | — |

## Tab layout improvements (v26.5.3)

The VFO panel tab stack has been improved to eliminate layout gaps:

- The `TabStack` class now overrides `sizeHint()` and `minimumSizeHint()` to report only the current page's preferred size, rather than the maximum across all pages.
- This fixes an issue where a gap appeared in the Mode tab when the DSP tab was taller (due to the digContainer being visible in DIGU/DIGL modes).

## Tips

- The filter width label in the VFO panel header shows the active bandwidth at all times. Click it directly to cycle through the preset buttons without switching to the Mode tab first.
- Preset slots are shared across all slices and modes. Overwriting a slot affects every slice that uses it.
- Filter edge lines on the spectrum panadapter reflect the active filter width. If the lines are hidden, enable them with the Filter edges button in the VFO panel. See [Hide or show filter edge lines on the spectrum](hide-or-show-filter-edge-lines-on-the-spectrum.md).
- To access NR2, RN2, BNR, NR4, MNR, or DFNR, right-click the spectrum overlay or open the AetherDSP applet.
- The DSP level slider now appears immediately on startup for any leveled DSP that was saved in the radio's profile, without requiring manual toggling.
- The RX antenna menu now uses the slice's specific antenna list when available, which may differ from the global antenna list in multi-radio configurations.
- When entering a frequency on a VHF/UHF band (100-999 MHz), bare integers with 4+ digits will have a decimal inserted after the third digit (e.g., 14696 → 146.96 MHz). For microwave bands above 1000 MHz, bare integers are treated as MHz directly.
- When the VFO is locked, click the lock button again to unlock and restore normal tuning.
- Explicit MHz entry (e.g., "14225") is now recognized on HF bands, allowing direct frequency entry without the XVTR band context.

## Related

- [Set a custom filter edge from the VFO panel](set-a-custom-filter-edge-from-the-vfo-panel.md)
- [Change mode from the VFO panel](change-mode-from-the-vfo-panel.md)
- [Hide or show filter edge lines on the spectrum](hide-or-show-filter-edge-lines-on-the-spectrum.md)
- [VFO Panel overview](overview.md)