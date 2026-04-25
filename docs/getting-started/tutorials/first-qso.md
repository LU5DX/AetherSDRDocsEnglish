# Make your first QSO with AetherSDR

This page walks you through connecting to your FLEX-8600, tuning to a frequency, and making a voice contact using AetherSDR for the first time.

## Before you start

- Your FLEX-8600 is powered on and connected to the same LAN as your computer, or you have SmartLink credentials for remote access.
- AetherSDR is installed and launched.
- Your microphone and headphone/speaker audio are configured in the radio's audio settings.

## Steps

### 1. Connect to the radio

1. The ConnectionPanel appears in the main window when no radio is connected. If it is not visible, click `Settings > Connect to Radio...`.
2. Click `Local` to search for radios on your LAN. Wait a few seconds for the `Available radios` list to populate.
3. If the list remains empty and the `No local radios found yet` indicator appears, click `Retry Discovery`.
4. Click your FLEX-8600 in the `Available radios` list to highlight it.
5. Click `Connect Selected Radio`.

The status label at the bottom of the ConnectionPanel changes from "searching" through "connecting" to "connected" when the link is established. The main window panadapter becomes active.

### 2. Open the RX Controls applet

1. Click the `RX` tray button on the right sidebar to open the RX Controls applet.
2. If the radio has more than one slice configured, click the slice tab (`A`, `B`, etc.) you want to use. Slice A is the default starting slice.

### 3. Set the mode

1. In the RX Controls applet, locate the `Mode combo`.
2. Click it and select `USB` for a typical SSB phone contact (or `LSB` for 40 m and below).

### 4. Tune to a frequency

1. Click the `Frequency label` in the RX Controls applet. It switches to an editable field.
2. Type the frequency in MHz — for example:
   ```
   14.225
   ```
3. Press `Enter`. The radio tunes to that frequency and the panadapter recenters.

### 5. Choose a filter width

1. Look at the filter width preset buttons in the RX Controls applet.
2. Click `2700` (2700 Hz) for a standard SSB passband, or choose a narrower preset if the band is crowded. The `2.7K` indicator updates to confirm the active width.

### 6. Set receive audio level

1. Confirm the mute toggle shows 🔊 (unmuted).
2. Adjust the `AF gain` slider so the incoming audio is comfortable. Default is 70 (range 0–100).

### 7. Open the TX Controls applet

1. Click the `TX` tray button on the right sidebar to open the TX Controls applet.

### 8. Set transmit power

1. Set the `RF Power` slider to your desired output level. Default is 100 (range 0–100).
2. Check the `Tune Pwr` slider — default is 10 (range 0–100). Leave it at 10 for a brief ATU tune if needed.

### 9. Check the antenna

1. In the RX Controls applet, confirm the TX antenna combo (the red-labelled antenna selector) shows the correct antenna port for your band.
2. In the TX Controls applet, watch the `SWR` meter when you transmit. A reading above 2.5 lights the red zone; run the ATU if needed.

### 10. Make the contact

1. To key the transmitter manually, click `MOX` in the TX Controls applet. The button turns red while TX is active. Speak into your microphone.
2. Click `MOX` again to return to receive.
3. Watch the `RF Pwr` meter to confirm power is reaching the antenna while you transmit.

## Tips

- The `STEP` spinbox in the RX Controls applet controls how far each click or mouse-wheel movement tunes the VFO. For SSB, 100 Hz (the default) is a good starting step.
- The `L / R pan` slider defaults to 50 (center). Double-click it to reset to center if you have moved it.
- If you accidentally move the frequency, click the 🔓 / 🔒 toggle in the RX Controls applet to lock the slice against further retuning.
- The `AGC mode` combo defaults to `Med`. If signals are very strong and causing distortion, try `Slow`.

## Troubleshooting

- **`No local radios found yet` and `Retry Discovery` does not help** — Verify the radio and the computer are on the same subnet. Click `Open Network Diagnostics` in the ConnectionPanel for more detail.
- **MOX keys the radio but the `RF Pwr` meter stays at zero** — Confirm the TX antenna combo in the RX Controls applet is not set to an RX-only port (ports prefixed with "RX" are filtered out of the TX list, but verify the selection is correct for your setup).
- **SWR reads very high immediately on transmit** — Run the internal ATU before making a contact. Click `ATU` in the TX Controls applet and wait for the `Success` indicator to light green.

## Related

- [Connect to a local LAN radio](../setup/connect-to-a-local-lan-radio.md)
- [Retry discovery when no radios appear](../../features/connection/retry-discovery-when-no-radios-appear.md)
- [Tune the radio to a frequency (type MHz in the readout)](../../features/rx/tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
- [Change mode (USB, LSB, CW, AM, FM, etc.)](../../features/rx/change-mode-usb-lsb-cw-am-fm-etc.md)
- [Pick a filter width preset for the current mode](../../features/rx/pick-a-filter-width-preset-for-the-current-mode.md)
- [Select the RX or TX antenna for this slice](../../features/rx/select-the-rx-or-tx-antenna-for-this-slice.md)
- [Set RF output power](../../features/tx/set-rf-output-power.md)
- [Run the internal ATU](../../features/tx/run-the-internal-atu.md)
- [Toggle MOX to manually key the transmitter](../../features/tx/toggle-mox-to-manually-key-the-transmitter.md)
- [Lock the slice to prevent accidental retuning](../../features/rx/lock-the-slice-to-prevent-accidental-retuning.md)
- [Connect to a remote radio through SmartLink](../setup/connect-to-a-remote-radio-through-smartlink.md)
