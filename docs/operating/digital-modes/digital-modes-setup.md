# Setting up digital modes (FT8, WSJT-X, fldigi)

This page explains how to configure AetherSDR so that digital-mode software such as WSJT-X or fldigi can receive audio from the radio, transmit audio back to it, and control the VFO. You need two bridges: DAX for audio, and CAT for frequency and mode control.

## Before you start

- AetherSDR is running and connected to your FLEX-8600.
- At least one slice is active on the panadapter.
- WSJT-X, fldigi, or your chosen digital-mode software is installed.

## Steps

### Part 1 — Enable DAX audio

1. Click the **DAX** tray button on the right sidebar. The DAX Audio applet appears.
2. Click **Enable**. The button turns green. AetherSDR starts the DAX audio bridge.
3. Note which channel row shows the slice you want to use. The slice-assignment indicator for that channel reads **Slice A** (or whichever letter applies). If it still shows **—**, assign a DAX channel to your slice in the radio's slice settings.
4. In the DAX applet, drag the **DAX 1 gain+meter** slider (or the channel matching your slice) to set the RX level. The default is 0.5; valid range is 0.0–1.0.
5. Drag the **TX gain+meter** slider to set the level for audio going back to the radio. Default is 0.5; valid range is 0.0–1.0.
6. In your digital-mode software, select the DAX RX channel as the audio input device and the DAX TX channel as the audio output device. The exact device name depends on your OS audio subsystem.

### Part 2 — Enable CAT control

1. Click the **CAT** tray button on the right sidebar. The CAT Control applet appears.
2. Check the **Base** field. The default port is `4532`. Channels A through D bind to port, port+1, port+2, port+3. Change the value only if another application is already using port 4532; valid range is 1024–65535.
3. Click **Enable TCP**. The button turns green. AetherSDR starts four rigctld-compatible TCP servers.
4. On Linux or macOS, click **Enable TTY** if your software requires a serial-style CAT port. Symlinks appear at `/tmp/AetherSDR-CAT-A`, `/tmp/AetherSDR-CAT-B`, `/tmp/AetherSDR-CAT-C`, and `/tmp/AetherSDR-CAT-D`.
5. In WSJT-X, fldigi, or your logging software, set the rig to **Hamlib NET rigctl** and point it at `localhost:4532` (or the port shown in the channel-A row). For the TTY path, enter the symlink shown in the channel row, for example `/tmp/AetherSDR-CAT-A`.

### Part 3 (optional) — Display WSJT-X decodes on the panadapter

1. Open `Settings > SpotHub...`.
2. Click the **WSJT-X** tab.
3. Confirm the **Address:** and **Port:** fields match the UDP multicast address and port configured in WSJT-X (WSJT-X default is `224.0.0.1`, port `2237`; adjust to match your WSJT-X settings).
4. Click **Start**. The status indicator changes to **Listening**.
5. Decoded calls appear in the **WSJT-X Decodes** console and as spots on the panadapter.
6. To filter what appears, check **CQ**, **CQ POTA**, or **Calling Me** as needed.

### Part 4 (optional) — Autostart on launch

- To start DAX automatically when AetherSDR opens, check `Settings > Autostart DAX with AetherSDR`. This persists as `AutoStartDAX`.
- To start CAT TCP and TTY servers automatically, check `Settings > Autostart CAT with AetherSDR`. This persists as `AutoStartCAT`.

## What each control does

| Control | Location | Default | Range | Setting key |
|---|---|---|---|---|
| **Enable** (DAX master) | DAX applet | Off | On/Off | `AutoStartDAX` |
| **DAX 1 gain+meter** | DAX applet | 0.5 | 0.0–1.0 | `DaxRxGain1` |
| **DAX 2 gain+meter** | DAX applet | 0.5 | 0.0–1.0 | `DaxRxGain2` |
| **DAX 3 gain+meter** | DAX applet | 0.5 | 0.0–1.0 | `DaxRxGain3` |
| **DAX 4 gain+meter** | DAX applet | 0.5 | 0.0–1.0 | `DaxRxGain4` |
| **TX gain+meter** | DAX applet | 0.5 | 0.0–1.0 | `DaxTxGain` |
| Slice-assignment indicator | DAX applet | — | — or Slice A–H | — |
| **Enable TCP** | CAT applet | Off | On/Off | — |
| **Enable TTY** | CAT applet | Off | On/Off | — |
| **Base** (TCP port) | CAT applet | 4532 | 1024–65535 | `CatTcpPort` |
| **Address:** (WSJT-X UDP) | SpotHub, WSJT-X tab | — | — | `WsjtxAddress` |
| **Port:** (WSJT-X UDP) | SpotHub, WSJT-X tab | — | 1–65535 | `WsjtxPort` |
| **Start / Stop** (WSJT-X) | SpotHub, WSJT-X tab | — | — | — |
| **CQ** filter | SpotHub, WSJT-X tab | — | On/Off | `WsjtxFilterCQ` |
| **CQ POTA** filter | SpotHub, WSJT-X tab | — | On/Off | `WsjtxFilterPOTA` |
| **Calling Me** filter | SpotHub, WSJT-X tab | — | On/Off | `WsjtxFilterCallingMe` |
| **Spot Life:** | SpotHub, WSJT-X tab | — | — | `WsjtxSpotLife` |

## Tips

- Each CAT channel controls one slice. Channel A maps to the first slice, B to the second, and so on. If you run two digital-mode instances simultaneously, point each one to a different port (4532 and 4533).
- If you change the **Base** port while **Enable TCP** is active, AetherSDR restarts all four servers on the new ports automatically.
- WSJT-X decodes appear in the panadapter spot overlay only while the SpotHub WSJT-X listener is running. If the panadapter is clear, verify the listener shows **Listening** and that WSJT-X is configured to send UDP status messages to the same address and port.

## Troubleshooting

- **DAX RX channel shows "—" and no audio reaches the software** — The slice has not been assigned to that DAX channel. Assign a DAX channel to the slice using the radio's slice controls, then confirm the indicator updates to show **Slice A** (or the appropriate letter).
- **WSJT-X reports "Hamlib error" or cannot connect** — Confirm **Enable TCP** is active (button is green) and that WSJT-X is pointed at the correct port. Verify no firewall rule blocks localhost TCP on port 4532.
- **Enable TTY is absent or greyed out** — PTY symlinks are only available on Linux and macOS. On Windows, use TCP only.
- **Base port reverts to 4532** — The value you entered was outside the 1024–65535 range. Enter a valid port number and press Enter to confirm.

## Related

- [Enable DAX to route slice audio to WSJT-X / FLDigi / other digital software](../../features/dax/enable-dax-to-route-slice-audio-to-wsjt-x-fldigi-other-digital-software.md)
- [Enable CAT TCP so N1MM, Log4OM, WSJT-X can control the radio](../../features/cat-control/enable-cat-tcp-so-n1mm-log4om-wsjt-x-can-control-the-radio.md)
- [Enable CAT PTY so Linux/macOS apps can open a serial-style CAT port](../../features/cat-control/enable-cat-pty-so-linux-macos-apps-can-open-a-serial-style-cat-port.md)
- [Start WSJT-X UDP listener and filter for CQ, POTA or calls to me](../../features/dx-cluster/start-wsjt-x-udp-listener-and-filter-for-cq-pota-or-calls-to-me.md)
- [Set DAX RX gain per channel](../../features/dax/set-dax-rx-gain-per-channel.md)
- [Set DAX TX gain](../../features/dax/set-dax-tx-gain.md)
- [Autostart DAX on launch](../../features/dax/autostart-dax-on-launch.md)
- [Autostart CAT servers with AetherSDR](../../features/cat-control/autostart-cat-servers-with-aethersdr.md)
- [Change the base TCP port](../../features/cat-control/change-the-base-tcp-port.md)
