# Work an FM repeater with CTCSS tone and +/- offset

Configure a slice for FM repeater operation by setting the mode, repeater offset frequency and direction, and an optional CTCSS tone to open the repeater's squelch.

## Before you start

- AetherSDR must be connected to the FLEX-8600 radio.
- The RX Controls applet must be visible. If it is not, click the RX tray button on the right sidebar to show it.
- Know your repeater's output frequency, offset direction, offset magnitude, and CTCSS tone (if required).

## Steps

1. In the RX Controls applet, select the slice you want to use by clicking the appropriate tab (A through H) if more than one slice is available.
2. Click the Mode combo and select **FM**, **NFM**, or **DFM** as appropriate for the repeater.
3. Click the Frequency label to enter edit mode. Type the repeater's **output** (receive) frequency in MHz and press Enter.
4. In the Offset (FM) spinbox, set the repeater offset magnitude. The valid range is 0.0–100.0 MHz in 0.1 MHz steps. For example, enter `0.6` for a standard 2 m offset.
5. Click the offset direction button that matches the repeater:
   - Click **+** if the repeater input (your transmit frequency) is above the output.
   - Click **−** if the repeater input is below the output.
   - Click **Simplex** to cancel any offset (TX = RX). Simplex is the default.
6. If the repeater requires a CTCSS tone, click the Tone mode (FM) combo and select **CTCSS TX**.
7. Click the CTCSS tone value combo and select the tone frequency required by the repeater. The 41 standard EIA/TIA-603 tones are available, from 67.0 Hz to 254.1 Hz.
8. To verify the radio is transmitting on the correct frequency before a QSO, you can click **REV** to swap the offset direction temporarily and listen on the repeater input. Click REV again to return to normal operation.

## What each control does

| Control | Default | Valid range | Behavior |
|---|---|---|---|
| Mode combo | USB | FM, NFM, DFM (among others) | Sets the slice to an FM family mode. Filter width presets are hidden in FM modes. |
| Offset (FM) | 0.0 MHz | 0.0–100.0 MHz, step 0.1 | Sets the repeater offset magnitude in MHz. |
| − (offset down) | — | — | Sets TX frequency below the RX frequency by the offset amount. |
| Simplex | checked | — | Sets TX frequency equal to RX frequency (no offset). |
| + (offset up) | — | — | Sets TX frequency above the RX frequency by the offset amount. |
| REV | — | — | Inverts the current offset direction. Useful for listening on the repeater input. |
| Tone mode (FM) | Off | Off, CTCSS TX | Selects whether a CTCSS tone is transmitted. Visible only in FM family modes. |
| CTCSS tone value | — | 67.0 Hz–254.1 Hz (41 tones) | Selects the CTCSS tone frequency. Active only when Tone mode is set to CTCSS TX. |

## Tips

- The filter width presets row is hidden automatically when the mode is FM, NFM, or DFM. This is normal.
- If you want to prevent accidental retuning while monitoring a busy repeater, click the 🔓 button in the header row to lock the slice. The icon changes to 🔒 when locked.
- To mute audio while you configure the slice, click the 🔊 / 🔇 button. Click it again to restore audio.
- Set the squelch to reduce noise between transmissions: click SQL to enable it, then adjust the Squelch level slider. A starting value of 20 (the default) is a reasonable baseline for FM.

## Troubleshooting

- **Tone mode (FM) and CTCSS tone value controls are not visible** — The slice mode is not set to FM, NFM, or DFM. These controls appear only in FM family modes. Change the Mode combo to FM, NFM, or DFM.
- **TX frequency is wrong after setting the offset** — Confirm the offset direction button (+, −, or Simplex) matches the repeater's specification. Use REV to listen on the repeater input and verify which direction is correct.
- **Repeater does not respond to transmissions** — Confirm the CTCSS tone value matches the repeater's required tone exactly, and that Tone mode (FM) is set to CTCSS TX rather than Off.

## Related

- [Change mode (USB, LSB, CW, AM, FM, etc.)](change-mode-usb-lsb-cw-am-fm-etc.md)
- [Tune the radio to a frequency (type MHz in the readout)](tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
- [Turn on the squelch and set its threshold](turn-on-the-squelch-and-set-its-threshold.md)
- [Lock the slice to prevent accidental retuning](lock-the-slice-to-prevent-accidental-retuning.md)
