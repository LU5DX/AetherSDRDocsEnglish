# Work an FM repeater with CTCSS tone and +/- offset

Set up AetherSDR to access an FM repeater: select FM mode, enter the repeater's output frequency, configure the TX offset direction and magnitude, and add a CTCSS tone so the repeater opens its squelch.

## Before you start

- AetherSDR is connected to the radio. The RX Controls applet is visible in the Applet Panel. If it is not, click the RX tray button on the right sidebar.
- You know the repeater's output (listen) frequency, offset direction (+/−), offset size in MHz, and CTCSS tone frequency in Hz.

## Steps

1. In the RX Controls applet, select the slice you want to use by clicking the appropriate tab (A through H) in the slice tab row.
2. Click the Mode combo and select **FM** (or **NFM** for narrow FM).
3. Click the Frequency label to open the Frequency edit field. Type the repeater's output frequency in MHz and press Enter. The radio tunes to that frequency.
4. Set the repeater offset direction:
   - Click **−** if the repeater transmits below its output frequency (TX below RX).
   - Click **+** if the repeater transmits above its output frequency (TX above RX).
   - Click **Simplex** if no offset is needed (TX = RX).
5. Set the Offset spinbox to the offset magnitude. Click the **<** or **>** arrows, or use the mouse wheel, to reach the correct value in MHz (range 0.0–100.0 MHz, step 0.1). For example, a standard 2 m offset is 0.6 MHz; a standard 70 cm offset is 5.0 MHz.
6. Set the Tone mode combo to **CTCSS TX**.
7. Set the CTCSS tone value combo to the tone frequency required by the repeater (67.0 Hz to 254.1 Hz, 41 standard EIA/TIA-603 tones).
8. To confirm the offset is correct before transmitting, click **REV** to listen on the repeater's input frequency and verify the channel is clear, then click **REV** again to return to normal operation.

## What each control does

| Control | Default | Valid range / values | Behavior |
|---|---|---|---|
| Mode combo | USB | USB, LSB, CW, AM, SAM, **FM**, **NFM**, **DFM**, DIGU, DIGL, RTTY | Sets the slice demodulation mode. Select FM or NFM for repeater operation. |
| Tone mode (FM) | Off | Off, CTCSS TX | Enables CTCSS tone generation on transmit. Visible only in FM family modes. |
| CTCSS tone value | — | 67.0 Hz – 254.1 Hz (41 EIA/TIA-603 tones) | Selects the subaudible tone sent during TX. Active only when Tone mode is CTCSS TX. |
| Offset (FM) | 0.0 MHz | 0.0–100.0 MHz, step 0.1 | Sets the magnitude of the repeater TX offset. |
| − (offset down) | — | toggle | Sets TX frequency below the RX frequency by the Offset amount. |
| Simplex | checked | toggle | Sets TX frequency equal to RX frequency (no offset). |
| + (offset up) | — | toggle | Sets TX frequency above the RX frequency by the Offset amount. |
| REV | — | toggle | Inverts the offset sign. Use to listen on the repeater input before transmitting. |

## Tips

- Filter width preset buttons are hidden in FM, NFM, and DFM modes. The filter width is fixed by the mode; do not expect preset buttons to appear.
- If you cannot hear the repeater's courtesy tone or other traffic, check that the Mode combo shows FM or NFM, not USB or another SSB mode.
- Double-clicking the L / R pan slider resets audio pan to centre (50).

## Troubleshooting

- **Repeater does not respond to your transmission** — Confirm Tone mode is set to **CTCSS TX** and the CTCSS tone value matches the repeater's requirement. Confirm the Offset spinbox value and direction (+ or −) are correct for the repeater.
- **REV appears to do nothing** — REV only has a visible effect when the Offset spinbox is non-zero and a direction (+ or −) is selected. Verify Offset is not 0.0 MHz and that Simplex is not active.
- **TX goes to the wrong frequency** — Check which direction button is active. Only one of −, Simplex, or + should be selected at a time. Click the correct one to deselect the others.

## Related

- [Change mode (USB, LSB, CW, AM, FM, etc.)](change-mode-usb-lsb-cw-am-fm-etc.md)
- [Tune the radio to a frequency (type MHz in the readout)](tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
- [Turn on the squelch and set its threshold](turn-on-the-squelch-and-set-its-threshold.md)
- [Select the RX or TX antenna for this slice](select-the-rx-or-tx-antenna-for-this-slice.md)
