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

## Troubleshooting

- **Repeater does not respond to your transmissions** — Confirm the CTCSS tone value matches what the repeater expects, and that Tone mode is set to **CTCSS TX** rather than **Off**.
- **TX frequency appears wrong** — Check that the offset direction button (**−**, **Simplex**, or **+**) matches the repeater's published offset direction, and that the Offset (FM) value is set to the correct magnitude (e.g. 0.6 MHz for a typical 2 m repeater).
- **Tone mode and CTCSS controls are not visible** — The slice mode must be **FM**, **NFM**, or **DFM**. These controls are hidden in all other modes.
- **Squelch controls are greyed out** — Squelch is disabled automatically when the slice mode is **DIGU**, **DIGL**, **NT**, **CW**, or **CWL**. Switch to an FM or SSB mode to enable the squelch controls.
- **Slice tab buttons appear incorrect after reconnecting** — If the slice tab row shows the wrong number of buttons or a stale layout after the radio reconnects, disconnect and reconnect manually. In v0.9.5.1 this is corrected automatically: the applet calls `clearSliceButtons()` to remove the old buttons and restore the static slice badge before rebuilding the tab row for the new slice count (#2254).
- **Filter preset button does not change passband** — If the current width is not a standard preset value, the widen/narrow step may not change the passband. This is expected behavior; click a specific filter preset button or type a frequency to change the passband, then the widen/narrow shortcuts will work from the new width.

## NT mode notes

The **NT** mode is treated as a digital mode in the RX Controls applet (v0.9.3+). This has the following effects:

- NT uses the same filter width presets and step sizes as DIGU and DIGL.
- The filter width indicator calculates bandwidth the same way as USB (using the upper passband edge).
- Squelch is disabled while NT is active. If squelch was on when you switched to NT, it is turned off automatically and restored when you leave the mode.

## Related

- [Change mode (USB, LSB, CW, AM, FM, etc.)](change-mode-usb-lsb-cw-am-fm-etc.md)
- [Tune the radio to a frequency (type MHz in the readout)](tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
- [Turn on the squelch and set its threshold](turn-on-the-squelch-and-set-its-threshold.md)
- [Select the RX or TX antenna for this slice](select-the-rx-or-tx-antenna-for-this-slice.md)