# Make your first QSO with AetherSDR

This page walks you through connecting to your FLEX-8600, tuning to a frequency, and making a voice contact. Follow the steps in order the first time.

## Before you start

- AetherSDR is installed and running on your computer.
- Your FLEX-8600 is powered on and reachable — either on the same LAN or through SmartLink.
- An antenna is connected to the radio.
- You know the frequency and mode of the station you want to work.

## Steps

### 1. Connect to the radio

1. The "Connect to a Radio" screen appears automatically in the main window when no radio is connected. If it does not appear, choose `Settings > Connect to Radio...`.
2. The default mode is **Local**. If your radio is on the same network, it will appear in the **Available radios** list within a few seconds.
3. Highlight your radio in the list.
4. Click **Connect Selected Radio**.
5. If no radio appears, click **Retry Discovery** and wait. If the radio is still not found, see [Retry discovery when no radios appear](../../features/connection/retry-discovery-when-no-radios-appear.md).

### 2. Open the RX Controls applet

1. The **RX** tray button is in the right sidebar (Applet Panel). Click it if the RX Controls panel is not already visible.

### 3. Set the mode

1. In the RX Controls applet, find the **Mode combo** (shows **USB** by default).
2. Click it and select the mode that matches the contact — for example, **USB** for a 20 m SSB contact or **LSB** for 40 m/80 m.

### 4. Tune to the frequency

1. Click the **Frequency label** (the large dotted readout, e.g. `0.000.000`). It switches to an editable field.
2. Type the frequency in MHz — for example:
   ```
   14.225
   ```
3. Press **Enter**. The radio tunes to that frequency and the panadapter recenters.

### 5. Set a filter width

1. In the RX Controls applet, click one of the **Filter width presets** buttons to choose a receive bandwidth suitable for the mode. For SSB, 2700 Hz is a common starting point.

### 6. Check receive audio

1. Confirm the **AF gain** slider is not at zero (default is 70).
2. Confirm the 🔊 / 🔇 mute toggle is in the unmuted state (🔊).
3. Listen for signals on the panadapter and in audio.

### 7. Open the TX Controls applet

1. Click the **TX** tray button in the right sidebar to open the TX Controls applet.

### 8. Set transmit power

1. Adjust the **RF Power** slider to your desired output level (default is 100; valid range 0–100).

### 9. Check that this slice is the TX slice

1. In the RX Controls applet, confirm the **TX (badge)** indicator is lit for slice **A** (the default slice). If it is not, click the **TX (badge)** button to make this slice the transmit slice.

### 10. Verify the TX antenna

1. In the RX Controls applet, confirm the red **ANT1 (TX antenna)** combo box shows the antenna you want to transmit on. Click it to change if needed.

### 11. Check SWR before transmitting (recommended)

1. In the TX Controls applet, click **TUNE**. The button label changes to **TUNING...** and a carrier is transmitted at the **Tune Pwr** level (default 10).
2. Watch the **SWR** meter. A reading well below 2.5 is acceptable. Red starts above 2.5.
3. Click **TUNE** again (or wait for it to complete) to stop the carrier.
4. If SWR is high, check your antenna connection or run the internal ATU — see [Run the internal ATU](../../features/tx/run-the-internal-atu.md).

### 12. Transmit

1. Key your microphone normally (VOX, footswitch, or PTT) to transmit. Alternatively, click **MOX** in the TX Controls applet to key the transmitter manually — the button turns red while transmitting.
2. Speak, then release PTT or click **MOX** again to return to receive.

### 13. Confirm the contact

1. Log the QSO in your preferred logging application.

## Tips

- The **AF gain** slider default is 70 and the **L / R pan** slider default is 50 (centre). Double-clicking the pan slider resets it to centre.
- The **AGC mode** combo defaults to **Med**. If signals are very strong or very weak, try **Slow** or **Fast**.
- If you accidentally retune the VFO while transmitting or logging, click the 🔓 toggle in the RX Controls applet to lock the slice frequency. The icon changes to 🔒 when locked.
- The **RF Power** slider sets power as a percentage of the radio's full output, not directly in watts. Watch the **RF Pwr** meter in the TX Controls applet for actual forward power.

## Troubleshooting

- **No radio appears in the Available radios list** — The radio may not be on the same subnet, or discovery has not completed. Click **Retry Discovery**. If still absent, try connecting by IP instead: see [Connect by IP across a VPN or routed network](../setup/connect-by-ip-across-a-vpn-or-routed-network.md).
- **No receive audio** — Check that the mute toggle shows 🔊 (unmuted) and the **AF gain** slider is above zero. Also verify your system audio output is configured correctly.
- **MOX keys the radio but SWR is very high** — Stop transmitting immediately. Verify the antenna is connected and the correct **ANT1 (TX antenna)** port is selected. Run the ATU if fitted.
- **Frequency label does not accept keyboard input** — Click directly on the frequency readout to enter edit mode, then type the MHz value and press **Enter**.

## Related

- [Connect to a local LAN radio](../setup/connect-to-a-local-lan-radio.md)
- [Connect to a remote radio through SmartLink](../setup/connect-to-a-remote-radio-through-smartlink.md)
- [Tune the radio to a frequency (type MHz in the readout)](../../features/rx/tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
- [Change mode (USB, LSB, CW, AM, FM, etc.)](../../features/rx/change-mode-usb-lsb-cw-am-fm-etc.md)
- [Pick a filter width preset for the current mode](../../features/rx/pick-a-filter-width-preset-for-the-current-mode.md)
- [Set RF output power](../../features/tx/set-rf-output-power.md)
- [Start a tune carrier to check SWR](../../features/tx/start-a-tune-carrier-to-check-swr.md)
- [Run the internal ATU](../../features/tx/run-the-internal-atu.md)
- [Toggle MOX to manually key the transmitter](../../features/tx/toggle-mox-to-manually-key-the-transmitter.md)
- [Lock the slice to prevent accidental retuning](../../features/rx/lock-the-slice-to-prevent-accidental-retuning.md)
