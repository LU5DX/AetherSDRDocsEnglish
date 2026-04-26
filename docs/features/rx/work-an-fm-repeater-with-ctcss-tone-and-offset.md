# Work an FM repeater with CTCSS tone and +/- offset

Set up a slice for FM repeater operation: select FM mode, dial in the repeater's input offset, and add a CTCSS access tone so the repeater opens.

## Before you start

- AetherSDR must be connected to your FLEX-8600 radio. If not, use `Settings > Connect to Radio...` to connect.
- You need to know the repeater's output frequency, offset direction (+ or −), offset amount in MHz, and CTCSS tone frequency (if required).

## Steps

1. Open the RX Controls applet. It is always visible in the Applet Panel (right sidebar). If the panel is hidden, click the RX tray button on the right sidebar.
2. If you have more than one slice active, click the correct slice tab (A through H) at the top of the applet.
3. Click the Mode combo and select **FM**, **NFM**, or **DFM** to match the repeater's emission type.
4. Click the Frequency label to enter edit mode. Type the repeater's **output** (receive) frequency in MHz and press Enter.
5. Set the offset amount: click the Offset (FM) spinbox and adjust to the repeater's offset value in MHz. Valid range is 0.0–100.0 MHz in 0.1 MHz steps. For example, type `0.6` for a standard 2 m offset.
6. Set the offset direction:
   - Click `+` (offset up) if the repeater's input is above its output.
   - Click `−` (offset down) if the repeater's input is below its output.
   - Click Simplex if you are working simplex (TX = RX). Simplex is the default.
7. If the repeater requires a CTCSS access tone:
   1. Click the Tone mode (FM) combo and select **CTCSS TX**.
   2. Click the CTCSS tone value combo and select the required tone frequency. The list contains all 41 standard EIA/TIA-603 tones from 67.0 Hz to 254.1 Hz.
8. If you need to listen on the repeater's input frequency to check if it is in use, click REV. Click REV again to return to normal operation.

## What each control does

| Control | Default | Valid range / options | Behavior |
|---|---|---|---|
| Mode combo | USB | FM, NFM, DFM (among others) | Sets the slice to an FM family mode; hides filter width presets. |
| Offset (FM) | 0.0 MHz | 0.0–100.0 MHz, step 0.1 | Sets the repeater TX offset amount. |
| − (offset down) | — | toggle | Sets TX frequency below RX frequency by the offset amount. |
| Simplex | checked | toggle | Sets TX frequency equal to RX frequency (no offset). |
| + (offset up) | — | toggle | Sets TX frequency above RX frequency by the offset amount. |
| REV | — | toggle | Inverts the offset direction to monitor the repeater's input. |
| Tone mode (FM) | Off | Off, CTCSS TX | Selects whether a CTCSS tone is sent on transmit. |
| CTCSS tone value | — | 67.0–254.1 Hz (41 EIA/TIA-603 tones) | Selects the CTCSS tone frequency. Active only when Tone mode is CTCSS TX. |

## Tips

- Filter width preset buttons are not shown in FM, NFM, or DFM modes. The `FilterPresets` setting does not apply in these modes.
- Double-click the L / R pan slider to reset it to centre (50) if the audio balance has been changed.
- To enable the squelch so the audio opens only when the repeater is active, see [Turn on the squelch and set its threshold](turn-on-the-squelch-and-set-its-threshold.md).

## Troubleshooting

- **Repeater does not respond to your transmission** — Confirm the CTCSS tone value matches the repeater's published access tone and that Tone mode is set to CTCSS TX, not Off.
- **TX frequency appears to be on the wrong side of the repeater output** — Check that you have selected the correct offset direction (`+` or `−`). Use REV temporarily to confirm which side the input is on.
- **Offset (FM) spinbox is not visible** — The offset controls appear only when the slice mode is FM, NFM, or DFM. Verify the Mode combo shows one of those options.

## Related

- [Change mode (USB, LSB, CW, AM, FM, etc.)](change-mode-usb-lsb-cw-am-fm-etc.md)
- [Turn on the squelch and set its threshold](turn-on-the-squelch-and-set-its-threshold.md)
- [Tune the radio to a frequency (type MHz in the readout)](tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
- [Select the RX or TX antenna for this slice](select-the-rx-or-tx-antenna-for-this-slice.md)
