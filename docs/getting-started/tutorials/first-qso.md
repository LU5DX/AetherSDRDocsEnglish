# Make your first QSO with AetherSDR

This page walks you through connecting to your FLEX-8600, tuning to a frequency, checking your transmit settings, and making a contact. Follow the steps in order the first time.

## Before you start

- AetherSDR is installed and running.
- Your FLEX-8600 is powered on and reachable — either on the same LAN, via SmartLink, or by a known IP address.
- Your microphone and headphones are configured in the radio's audio settings.
- You know the frequency and mode of the station you want to work.

## Steps

### 1. Connect to your radio

1. The **Connect to a Radio** panel appears in the main window. If it does not, go to `Settings > Connect to Radio...`.
2. Select **Local** if the radio is on your LAN. Wait a few seconds for the **Available radios** list to populate.
3. Highlight your radio in the **Available radios** list.
4. Click **Connect Selected Radio**.

The status label updates through "searching" and "connecting" and then shows "connected" when the link is established. The applet panel becomes active on the right side.

> If the list stays empty, click **Retry Discovery**. If the radio is on a different subnet or VPN, click **Connect by IP** instead and see [Connect by IP across a VPN or routed network](../setup/connect-by-ip-across-a-vpn-or-routed-network.md).

### 2. Open the RX Controls applet

Click the **RX** tray button on the right sidebar to expand the RX Controls applet. Slice **A** is selected by default.

### 3. Set the operating mode

In the **Mode combo**, select the mode that matches the contact you want to make — for example, **USB** for most HF phone, **LSB** for 40/80/160 m phone, or **CW** for Morse.

The filter presets below the frequency display update automatically for the chosen mode.

### 4. Tune to the frequency

1. Click the **Frequency label** (showing a dotted readout such as `0.000.000`). It switches to an edit field.
2. Type the frequency in MHz — for example, `14.225` for 14.225 MHz.
3. Press **Enter**. The radio tunes and the panadapter recenters on the new frequency.

If you need to cancel without changing frequency, press **Escape**.

### 5. Pick a filter width

Click one of the **Filter width presets** buttons to select a suitable bandwidth for your mode. For SSB the choices are 1800, 2100, 2400, 2700, 2900, and 3300 Hz. The current filter width is shown in the **Filter width label** (for example, `2.7K`).

### 6. Check the RX antenna

Confirm the **ANT1 (RX antenna)** combo shows the antenna you want to receive on. Change it if needed.

### 7. Set AF gain

Adjust the **AF gain** slider so you can hear comfortably. The default is 70 (range 0–100).

### 8. Open the TX Controls applet

Click the **TX** tray button on the right sidebar to expand the TX Controls applet.

### 9. Set transmit power

Move the **RF Power** slider to your intended output level. The default is 100 (range 0–100). Watch the **RF Pwr** meter and the **SWR** meter during the next step.

### 10. Verify the TX antenna

Back in the RX Controls applet, confirm the **ANT1 (TX antenna)** combo shows the correct transmit antenna for this band.

### 11. Check SWR with a tune carrier (optional but recommended)

1. In the TX Controls applet, set the **Tune Pwr** slider to a low level (default is 10).
2. Click **TUNE**. The button label changes to **TUNING...** with a red background while the carrier is active.
3. Read the **SWR** meter. When satisfied, click **TUNE** again to stop.

A good SWR reading (below 2.0) means your antenna system is ready.

### 12. Make the contact

When the frequency is clear and the other station is ready:

1. Key your microphone or paddle. The radio will go to transmit.
2. To manually key the transmitter for testing, click **MOX** in the TX Controls applet. The button turns red while transmit is active. Click **MOX** again to return to receive.
3. Watch the **RF Pwr** meter to confirm power output and the **SWR** meter to confirm the antenna is behaving.

## Tips

- If you are working a station that is slightly off your receive frequency, enable **RIT** in the RX Controls applet and use the **RIT offset** spinbox to shift receive without moving your transmit frequency. Click **RIT 0** to zero it when done.
- If you hear feedback from your own transmission, reduce **AF gain** while transmitting or use headphones.
- The **RF Power** and **Tune Pwr** sliders, **TX Profile** combo, and antenna selectors keep their state between sessions for the same radio.
- To prevent accidentally retuning the slice during a QSO, click the 🔓 toggle button in the RX Controls applet to lock the frequency. It changes to 🔒 when locked.

## Troubleshooting

- **"No local radios found yet" appears and the list stays empty** — Click **Retry Discovery**. Check that the radio is powered on and on the same network segment. If it is on a different subnet, use **Connect by IP** or SmartLink instead.
- **MOX keys the radio but RF Pwr meter shows zero** — Check the **RF Power** slider is above 0 and that the correct TX antenna is selected in the **ANT1 (TX antenna)** combo.
- **SWR reads red (above 2.5)** — Check your coax and antenna connections. Run the internal ATU if your setup includes one: click **ATU** in the TX Controls applet.
- **Audio is very quiet or absent on receive** — Check the **AF gain** slider (default 70) and confirm the 🔊 / 🔇 mute toggle is in the unmuted (🔊) state.

## Related

- [Connect to a local LAN radio](../setup/connect-to-a-local-lan-radio.md)
- [Connect to a remote radio through SmartLink](../setup/connect-to-a-remote-radio-through-smartlink.md)
- [Connect by IP across a VPN or routed network](../setup/connect-by-ip-across-a-vpn-or-routed-network.md)
- [Tune the radio to a frequency (type MHz in the readout)](../../features/rx/tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
- [Change mode (USB, LSB, CW, AM, FM, etc.)](../../features/rx/change-mode-usb-lsb-cw-am-fm-etc.md)
- [Pick a filter width preset for the current mode](../../features/rx/pick-a-filter-width-preset-for-the-current-mode.md)
- [Select the RX or TX antenna for this slice](../../features/rx/select-the-rx-or-tx-antenna-for-this-slice.md)
- [Start a tune carrier to check SWR](../../features/tx/start-a-tune-carrier-to-check-swr.md)
- [Set RF output power](../../features/tx/set-rf-output-power.md)
- [Run the internal ATU](../../features/tx/run-the-internal-atu.md)
- [Use RIT to offset the receive frequency for a drifting station](../../features/rx/use-rit-to-offset-the-receive-frequency-for-a-drifting-station.md)
- [Lock the slice to prevent accidental retuning](../../features/rx/lock-the-slice-to-prevent-accidental-retuning.md)
- [Retry discovery when no radios appear](../../features/connection/retry-discovery-when-no-radios-appear.md)
