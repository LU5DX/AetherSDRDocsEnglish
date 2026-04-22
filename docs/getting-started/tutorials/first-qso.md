# Make your first QSO with AetherSDR

This tutorial walks you through connecting to your FLEX-8600, tuning to a frequency, and making a voice contact using AetherSDR for the first time.

## Before you start

- AetherSDR is installed and launched.
- Your FLEX-8600 is powered on and reachable on the local network, or you have SmartLink credentials for remote access.
- A microphone and headphones are connected and configured in your operating system.

## Steps

### 1. Connect to the radio

1. The **Connect to a Radio** panel appears automatically in the main window when no radio is connected. If it is not visible, click `Settings > Connect to Radio...`.
2. Click **Local** if your radio is on the same LAN. AetherSDR runs mDNS discovery; your FLEX-8600 appears in the **Available radios** list within a few seconds.
3. If the list is empty, click **Retry Discovery** and wait a moment.
4. Highlight your radio in the **Available radios** list.
5. Click **Connect Selected Radio**.

The status label updates as the connection progresses. When it shows a connected state the main window panadapter becomes active.

### 2. Open the RX Controls applet

Click the **RX** tray button on the right sidebar to open the RX Controls applet. The applet shows slice **A** by default.

### 3. Choose a mode

In the **Mode combo** box, select the mode that matches the contact you want to make — for example, **USB** for a phone QSO on HF above 10 MHz, or **LSB** below 10 MHz.

### 4. Tune to a frequency

1. Click the **Frequency label** (showing the current VFO readout, e.g. `0.000.000`). It switches to an editable field.
2. Type the frequency in MHz — for example, `14.225` for 20 m SSB phone.
3. Press **Enter**. The radio tunes and the panadapter recenters on the new frequency.

To step the frequency up or down, use the **STEP** spinbox arrow buttons or scroll the mouse wheel over it. The default step size is 100 Hz; the available steps for SSB are 1, 10, 50, 100, 500, 1000, 2000, and 3000 Hz.

### 5. Set a filter width

Click one of the **Filter width presets** buttons to apply a standard passband. For USB or LSB the available presets are 1800, 2100, 2400, 2700, 2900, and 3300 Hz. The **2.7K** preset is a reasonable starting point for a phone QSO.

### 6. Adjust receive audio

- Set the **AF gain** slider to a comfortable listening level. The default is 70 (range 0–100).
- Set the **AGC mode** combo to **Med** (the default) for typical phone operation.
- If you hear interference on one ear, center the **L / R pan** slider at 50. Double-click the slider to reset it to center instantly.

### 7. Listen before transmitting

Monitor the frequency for activity. Use the panadapter to watch for signals. If a station calls CQ or you want to answer one, proceed to the next step.

### 8. Open the TX Controls applet

Click the **TX** tray button on the right sidebar to open the TX Controls applet.

### 9. Set transmit power

Move the **RF Power** slider to your desired output level. The default is 100 (range 0–100). Watch the **RF Pwr** meter and **SWR** meter when you transmit; SWR should stay well below 2.5 for normal operation.

### 10. Select a TX profile

If you have transmit profiles configured, choose one from the **TX Profile** combo box that matches your operating mode (for example, a profile set up for SSB phone).

### 11. Confirm the TX slice

In the RX Controls applet, check that the **TX** badge is lit on slice **A** (or whichever slice you are using). If it is not, click the **TX** badge to set this slice as the transmit slice.

### 12. Transmit

Key your microphone and click **MOX** in the TX Controls applet. The MOX button turns red while transmitting. Watch the **RF Pwr** meter confirm output power. Click **MOX** again to return to receive when you finish speaking.

### 13. Complete the QSO

Return to receive, copy the other station's report, and exchange signal reports as usual. When the contact is finished, click **MOX** if you need to transmit again, or simply stay in receive.

## Tips

- If the SWR meter reads above 2.5, stop transmitting and check your antenna system before continuing. The red zone on the SWR gauge begins at 2.5.
- The **Tune Pwr** slider (default 10, range 0–100) controls carrier power during antenna tuning. Use it with the **TUNE** button to check SWR at reduced power before a QSO.
- If you accidentally move the VFO, click the 🔓 toggle button in the RX Controls applet to lock the slice and prevent further retuning.
- Double-clicking the **L / R pan** slider resets it to center (50).

## Troubleshooting

- **"No local radios found yet" appears and the list stays empty** — Verify the radio is powered on and on the same network segment. Click **Retry Discovery**. If the problem persists, click **Open Network Diagnostics** for more detail.
- **MOX goes red but the RF Pwr meter shows no output** — Confirm the correct TX antenna is selected in the **ANT1 (TX antenna)** combo box in the RX Controls applet. Also verify that the audio input device is active in your operating system.
- **Received audio is very quiet or absent** — Check the **AF gain** slider (default 70) and confirm the slice is not muted (the 🔊 / 🔇 toggle button should show 🔊).

## Related

- [Connect to a local LAN radio](../setup/connect-to-a-local-lan-radio.md)
- [Connect to a remote radio through SmartLink](../setup/connect-to-a-remote-radio-through-smartlink.md)
- [Retry discovery when no radios appear](../../features/connection/retry-discovery-when-no-radios-appear.md)
- [Tune the radio to a frequency (type MHz in the readout)](../../features/rx/tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
- [Change mode (USB, LSB, CW, AM, FM, etc.)](../../features/rx/change-mode-usb-lsb-cw-am-fm-etc.md)
- [Pick a filter width preset for the current mode](../../features/rx/pick-a-filter-width-preset-for-the-current-mode.md)
- [Set RF output power](../../features/tx/set-rf-output-power.md)
- [Start a tune carrier to check SWR](../../features/tx/start-a-tune-carrier-to-check-swr.md)
- [Toggle MOX to manually key the transmitter](../../features/tx/toggle-mox-to-manually-key-the-transmitter.md)
- [Select the RX or TX antenna for this slice](../../features/rx/select-the-rx-or-tx-antenna-for-this-slice.md)
- [Lock the slice to prevent accidental retuning](../../features/rx/lock-the-slice-to-prevent-accidental-retuning.md)
- [Understanding slices and VFOs](../concepts/understanding-slices.md)
