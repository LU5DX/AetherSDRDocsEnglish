# Make your first QSO with AetherSDR

This page walks you through connecting to your FLEX-8600, tuning to a frequency, checking the antenna and power settings, and making a contact. Follow these steps in order the first time you use AetherSDR.

## Before you start

- Your FLEX-8600 is powered on and connected to the same LAN as your computer, or you have SmartLink credentials and a remote radio available.
- AetherSDR is installed and launched.
- You know which band and mode you want to operate (for example, 14.225 MHz USB).
- Your microphone or keyer is connected and configured in the radio.

## Steps

### 1. Connect to the radio

1. When no radio is connected, AetherSDR shows the **Connect to a Radio** panel in the main window. If you have already closed it, open it via `Settings > Connect to Radio...`.
2. The default mode is **Local**. If your radio is on the same LAN, leave this selected.
3. Wait a few seconds for the **Available radios** list to populate via automatic discovery. Your FLEX-8600 should appear by name.
4. Click your radio in the **Available radios** list to highlight it.
5. Click **Connect Selected Radio**.
6. The status label changes from "searching" through "connecting" to "connected". The main panadapter view opens when the connection succeeds.

If the list stays empty, click **Retry Discovery**. If the radio is on a different subnet, click **Connect by IP** and enter the radio's IP address in the **Radio IP address** field, then click **Connect by IP (manual)**. For a remote radio over the internet, click **Remote with SmartLink** instead and sign in.

### 2. Select the correct antenna

1. In the right sidebar, click the **RX** tray button to open the RX Controls applet (it is visible by default).
2. Find the blue-labelled antenna combo box (RX antenna, default **ANT1**). Click it and select the antenna port your receive antenna is connected to.
3. Find the red-labelled antenna combo box (TX antenna, default **ANT1**). Click it and select the antenna port your transmit antenna is connected to. RX-only ports are not listed here.

### 3. Set the operating mode and frequency

1. In the RX Controls applet, click the **Mode combo** and select your mode — for example, **USB** for upper sideband phone.
2. Click the **Frequency label** to switch it to edit mode (the **Frequency edit** field appears).
3. Type your target frequency in MHz (for example, `14.225`) and press **Enter**. The panadapter recenters on the new frequency. Press **Escape** to cancel without changing frequency.
4. Choose a filter width by clicking one of the **Filter width presets** buttons. For USB, the available presets are 1800, 2100, 2400, 2700, 2900, and 3300 Hz. 2700 Hz is a common starting point for SSB.

### 4. Set transmit power

1. Click the **TX** tray button in the right sidebar to open the TX Controls applet.
2. Drag the **RF Power** slider to your desired power level (default **100**, range 0–100). Watch the **RF Pwr** meter during a transmission to confirm actual output.
3. Check the **SWR** meter. A reading above 2.5 is shown in red; investigate your antenna system before transmitting if so.
4. If you want to run the internal ATU first, click **ATU** and wait for the cycle to complete. The **Success** indicator lights green when a match is found.

### 5. Check audio and gain

1. Back in the RX Controls applet, confirm the **AF gain** slider is at a comfortable listening level (default **70**, range 0–100).
2. Confirm the **AGC mode** combo is set to **Med** (the default) for SSB. Adjust to **Slow** or **Fast** if needed.
3. If you hear no audio, check that the mute toggle (🔊/🔇) shows the unmuted state.

### 6. Make the contact

1. Listen on frequency. When ready to call, key your microphone or keyer.
2. To transmit using software keying, click **MOX** in the TX Controls applet. The button turns red while transmitting. Click **MOX** again to return to receive.
3. Watch the **RF Pwr** meter to confirm output, and the **SWR** meter to confirm the antenna is matched.
4. When the QSO is complete, click **MOX** to ensure you are back in receive, or simply release your hardware PTT.

## Tips

- If the other station is slightly off frequency and you do not want to move your VFO, enable **RIT** in the RX Controls applet and use the **RIT offset** spinbox (10 Hz steps) to shift your receive frequency without changing transmit. Click **RIT 0** to zero it afterwards.
- To prevent accidentally retuning mid-QSO, click the 🔓 toggle in the RX Controls applet to lock the slice. The icon changes to 🔒.
- The **L / R pan** slider (default **50**, range 0–100) lets you position this slice's audio in the stereo field. Double-click it to reset to centre.
- If you operate split, use **XIT** in the RX Controls applet to offset your transmit frequency independently of the receive VFO.

## Troubleshooting

- **The Available radios list is empty** — Click **Retry Discovery**. Check that the radio is powered on and on the same network segment. Click **Open Network Diagnostics** to inspect the path. If the radio is on a different subnet, use **Connect by IP (manual)** instead.
- **No audio from the speaker** — Check that the mute toggle in the RX Controls applet shows the unmuted (🔊) state. Check that **AF gain** is above 0. Verify audio device configuration in your operating system.
- **MOX keys but the RF Pwr meter reads zero** — Confirm the correct TX antenna is selected in the red-labelled TX antenna combo box. Confirm **RF Power** is above 0 in the TX Controls applet.
- **SWR meter reads red (above 2.5)** — Do not continue transmitting at full power. Check antenna connections. Run the internal **ATU** to find a match, or reduce power until the issue is resolved.
- **Frequency edit does not accept the value** — Ensure you are entering a value in MHz within the valid range (0.001–54.000 MHz). Press **Escape** to cancel and restore the previous frequency.

## Related

- [Connect to a local LAN radio](../setup/connect-to-a-local-lan-radio.md)
- [Connect to a remote radio through SmartLink](../setup/connect-to-a-remote-radio-through-smartlink.md)
- [Connect by IP across a VPN or routed network](../setup/connect-by-ip-across-a-vpn-or-routed-network.md)
- [Retry discovery when no radios appear](../../features/connection/retry-discovery-when-no-radios-appear.md)
- [Change mode (USB, LSB, CW, AM, FM, etc.)](../../features/rx/change-mode-usb-lsb-cw-am-fm-etc.md)
- [Tune the radio to a frequency (type MHz in the readout)](../../features/rx/tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
- [Pick a filter width preset for the current mode](../../features/rx/pick-a-filter-width-preset-for-the-current-mode.md)
- [Select the RX or TX antenna for this slice](../../features/rx/select-the-rx-or-tx-antenna-for-this-slice.md)
- [Set RF output power](../../features/tx/set-rf-output-power.md)
- [Start a tune carrier to check SWR](../../features/tx/start-a-tune-carrier-to-check-swr.md)
- [Run the internal ATU](../../features/tx/run-the-internal-atu.md)
- [Toggle MOX to manually key the transmitter](../../features/tx/toggle-mox-to-manually-key-the-transmitter.md)
- [Use RIT to offset the receive frequency for a drifting station](../../features/rx/use-rit-to-offset-the-receive-frequency-for-a-drifting-station.md)
- [Use XIT to offset the transmit frequency without changing RX](../../features/rx/use-xit-to-offset-the-transmit-frequency-without-changing-rx.md)
- [Lock the slice to prevent accidental retuning](../../features/rx/lock-the-slice-to-prevent-accidental-retuning.md)
- [Understanding slices and VFOs](../concepts/understanding-slices.md)
