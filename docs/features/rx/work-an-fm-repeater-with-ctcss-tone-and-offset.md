# Work an FM repeater with CTCSS tone and +/- offset

Configure a slice for FM duplex operation with a repeater offset and a CTCSS access tone so you can both hear the repeater output and key it correctly on transmit.

## Before you start

- AetherSDR is connected to your FLEX-8600.
- The RX Controls applet is visible in the right sidebar. If it is not, click the RX tray button on the right sidebar.
- You know the repeater's output frequency, offset direction, offset magnitude, and CTCSS tone frequency.

## Steps

1. In the RX Controls applet, click the Mode combo and select **FM** (or **NFM** for narrow FM).
2. Click the Frequency label to open the Frequency edit field. Type the repeater's **output** (receive) frequency in MHz and press Enter.
3. In the **Offset (FM)** spinbox, set the offset magnitude in MHz. Use the spinbox arrows or type a value directly. Valid range is 0.0–100.0 MHz in 0.1 MHz steps. The default is 0.0 MHz.
4. Set the offset direction by clicking one of the three toggle buttons:
   - **−** — TX frequency is below the RX frequency.
   - **Simplex** — TX frequency equals the RX frequency (default).
   - **+** — TX frequency is above the RX frequency.
5. Click the **Tone mode (FM)** combo (default: **Off**) and select **CTCSS TX**.
6. Click the **CTCSS tone value** combo and select the tone frequency required by the repeater. The available tones follow the 41-tone EIA/TIA-603 standard, from 67.0 Hz to 254.1 Hz.
7. Confirm the squelch is set appropriately for the band. See [Turn on the squelch and set its threshold](turn-on-the-squelch-and-set-its-threshold.md) if needed.

## What each control does

| Control          | Default | Valid range / options                     |
|------------------|---------|-------------------------------------------|
| Mode combo       | USB     | FM, NFM, DFM (among others)               |
| Tone mode (FM)   | Off     | Off, CTCSS TX                             |
| CTCSS tone value | —       | 67.0 Hz – 254.1 Hz (41 EIA/TIA-603 tones) |
| Offset (FM)      | 0.0 MHz | 0.0 – 100.0 MHz, step 0.1                 |
| − (offset down)  | —       | toggle                                    |
| Simplex          | checked | toggle                                    |
| + (offset up)    | —       | toggle                                    |
| REV              | —       | toggle                                    |

## Tips

- If you need to listen on the repeater's input frequency to check whether the channel is busy before transmitting, click **REV** to swap the offset direction temporarily.
- FM family modes hide the filter width preset buttons. This is expected; filter width for FM is fixed by the mode itself.
- Slice tab buttons and the slice badge are color-coded per slice using SliceColorManager (v0.9.3+). The colors persist across sessions and are reflected in the slice tabs, the slice badge, VFO widgets, and meter strips.
- When the radio reports a different number of available slices than the tab row was built for, AetherSDR now tears down the existing slice tab buttons and rebuilds them for the new count before reconnecting click handlers (v0.9.5.1, #2254). This prevents stale buttons appearing after a reconnect or a change in hardware configuration.
- Filter width presets are stored in the format `lo:hi` (passband edges in Hz) or as a plain width value, depending on whether the preset was saved with explicit edge positions. Both formats are read correctly when you reopen the applet or switch modes (#2259).
- The filter width readout is shared with the VFO panel via `RxApplet::formatFilterWidth()`. In v0.9.8+, this method is now a public static function so both widgets produce identical, mode-aware formatting for SSB, digital, and AM modes (#2197).
- The widen/narrow shortcuts (e.g. Ctrl+Shift+W, Ctrl+Shift+N) call `stepFilterWidth(int direction)`, which walks the per-mode filter preset list to find the next valid width and applies it with correct edge geometry for the current mode (#2208).
- The slice badge now supports rich text formatting (HTML) for the slice letter display (#2606).
- Antenna selection for both RX and TX now prioritizes the slice's own antenna list when available. The menu shows antenna labels with tooltips and status tips, with actual antenna data stored separately from display text. TX antenna menus filter out ports with the "RX" prefix and include only antennas matching patterns like "ANT", "TX", or "XVTR".
- By default, AetherSDR uses an Auto squelch algorithm that clobbers the slice's squelchLevel with algorithm-suggested values. The last user-chosen Manual squelch threshold is now persisted client-side in the `LastManualSquelchLevel` setting and restored between sessions and mode cycles.
- The mute button uses a deferred single-click mechanism to avoid conflicts with double-click actions. A single-click mutes or unmutes the current slice. A double-click mutes or unmutes all owned slices. The icon updates only when the radio acknowledges the mute state change, ensuring the displayed state always matches the radio's actual state.
- When entering a frequency in the Frequency edit field, AetherSDR uses `FrequencyEntryParser` to normalize the input. If you type a value above 54 MHz without being on an XVTR antenna, the parser checks whether it was entered as an explicit MHz value. If so, the maximum allowed frequency is raised to 50000 MHz, allowing entry of VHF/UHF frequencies above the normal 54 MHz limit without switching to an XVTR antenna first (e.g., typing 146.520 MHz on a non-XVTR antenna).
- The offset direction buttons and REV button are part of an exclusive button group; selecting one automatically deselects the others.
- The L/R pan slider now paints its fill from the centre outward. This provides a visual indication of the neutral (centre) position at a glance. The centre mark is a small dot painted on the groove.
- The filter preset buttons and other styled buttons now use tokenised stylesheet colours through ThemeManager. This means the button appearance updates automatically when you switch themes, consistent with the rest of the UI (v26.6.1).

## Troubleshooting

- **Repeater does not respond to your transmissions** — Confirm the CTCSS tone value matches what the repeater expects, and that Tone mode is set to **CTCSS TX** rather than **Off**.
- **TX frequency appears wrong** — Check that the offset direction button (**−**, **Simplex**, or **+**) matches the repeater's published offset direction, and that the Offset (FM) value is set to the correct magnitude (e.g. 0.6 MHz for a typical 2 m repeater).
- **Tone mode and CTCSS controls are not visible** — The slice mode must be **FM**, **NFM**, or **DFM**. These controls are hidden in all other modes.
- **Squelch controls are greyed out** — Squelch is disabled automatically when the slice mode is **DIGU**, **DIGL**, **NT**, **RTTY**, **CW**, or **CWL**. Switch to an FM or SSB mode to enable the squelch controls.
- **Slice tab buttons appear incorrect after reconnecting** — If the slice tab row shows the wrong number of buttons or a stale layout after the radio reconnects, disconnect and reconnect manually. In v0.9.5.1 this is corrected automatically: the applet calls `clearSliceButtons()` to remove the old buttons and restore the static slice badge before rebuilding the tab row for the new slice count (#2254).
- **Filter preset button does not change passband** — If the current width is not a standard preset value, the widen/narrow step may not change the passband. This is expected behavior; click a specific filter preset button or type a frequency to change the passband, then the widen/narrow shortcuts will work from the new width.
- **Mute icon does not change on click** — The mute icon is updated only when the radio acknowledges the mute state change. If the icon does not change, the radio may not have confirmed the new state. This is expected per the Radio-Authoritative Settings Policy (#2489).

## NT mode and RTTY mode notes

The **NT** and **RTTY** modes are treated as digital modes in the RX Controls applet (v0.9.3+ for NT, v26.5.1 for RTTY). This has the following effects:

- NT and RTTY use the same filter width presets and step sizes as DIGU and DIGL.
- The filter width indicator calculates bandwidth the same way as USB (using the upper passband edge).
- Squelch is disabled while NT or RTTY is active. If squelch was on when you switched to NT or RTTY, it is turned off automatically and restored when you leave the mode.
- For RTTY mode specifically, squelch is disabled because it would notch out FSK characters and break decoding (#2504).

## Related

- [Change mode (USB, LSB, CW, AM, FM, etc.)](change-mode-usb-lsb-cw-am-fm-etc.md)
- [Tune the radio to a frequency (type MHz in the readout)](tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
- [Turn on the squelch and set its threshold](turn-on-the-squelch-and-set-its-threshold.md)
- [Select the RX or TX antenna for this slice](select-the-rx-or-tx-antenna-for-this-slice.md)