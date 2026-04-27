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

| Control | Default | Valid range / options | Notes |
|---|---|---|---|
| Mode combo | USB | FM, NFM, DFM (among others) | Filter width presets are hidden for all FM family modes. |
| Tone mode (FM) | Off | Off, CTCSS TX | Visible only when mode is FM, NFM, or DFM. |
| CTCSS tone value | — | 67.0 Hz – 254.1 Hz (41 EIA/TIA-603 tones) | Enabled only when Tone mode is set to CTCSS TX. |
| Offset (FM) | 0.0 MHz | 0.0 – 100.0 MHz, step 0.1 | Sets the magnitude of the repeater offset. |
| − (offset down) | — | toggle | TX frequency is placed below the RX frequency. |
| Simplex | checked | toggle | TX and RX frequencies are equal. |
| + (offset up) | — | toggle | TX frequency is placed above the RX frequency. |
| REV | — | toggle | Inverts the configured offset sign; use to listen on a reversed repeater pair. |

## Tips

- If you need to listen on the repeater's input frequency to check whether the channel is busy before transmitting, click **REV** to swap the offset direction temporarily.
- FM family modes hide the filter width preset buttons. This is expected; filter width for FM is fixed by the mode itself.

## Troubleshooting

- **Repeater does not respond to your transmissions** — Confirm the CTCSS tone value matches what the repeater expects, and that Tone mode is set to **CTCSS TX** rather than **Off**.
- **TX frequency appears wrong** — Check that the offset direction button (**−**, **Simplex**, or **+**) matches the repeater's published offset direction, and that the Offset (FM) value is set to the correct magnitude (e.g. 0.6 MHz for a typical 2 m repeater).
- **Tone mode and CTCSS controls are not visible** — The slice mode must be **FM**, **NFM**, or **DFM**. These controls are hidden in all other modes.

## Related

- [Change mode (USB, LSB, CW, AM, FM, etc.)](change-mode-usb-lsb-cw-am-fm-etc.md)
- [Tune the radio to a frequency (type MHz in the readout)](tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
- [Turn on the squelch and set its threshold](turn-on-the-squelch-and-set-its-threshold.md)
- [Select the RX or TX antenna for this slice](select-the-rx-or-tx-antenna-for-this-slice.md)
