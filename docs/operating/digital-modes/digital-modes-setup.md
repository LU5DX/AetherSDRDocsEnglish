# Setting up digital modes (FT8, WSJT-X, fldigi)

This page explains how to connect AetherSDR to digital-mode software such as WSJT-X or fldigi. You need two things working together: DAX to carry audio between the radio and the external program, and CAT control so the external program can read and set frequency and mode.

## Before you start

- AetherSDR is connected to your FLEX-8600 (the radio icon in the title bar shows a live connection).
- WSJT-X, fldigi, or your other digital-mode software is installed and closed for now. Configure AetherSDR first, then start the external program.
- Decide which slice you will use for digital modes and note its letter (A, B, C, or D).

## Steps

### 1. Enable DAX audio

1. Click the **DAX** tray button on the right sidebar. The DAX Audio applet appears.
2. Click **Enable**. The button turns green. AetherSDR starts the DAX audio bridge and saves `AutoStartDAX` = `True`.
3. Check the slice-assignment indicator next to **DAX 1** (or whichever channel you plan to use). It should read **Slice A** (or the letter matching your digital slice). If it shows **—**, assign the slice to that DAX channel in your radio's slice settings.
4. If the receive audio level in your external program is too low or too high, drag the **DAX 1 gain+meter** slider left or right. The default is 0.5 (range 0.0–1.0); the value persists as `DaxRxGain1`.
5. If you need to transmit audio (FT8, fldigi), adjust the **TX gain+meter** slider to taste. Default is 0.5 (range 0.0–1.0); persists as `DaxTxGain`.

### 2. Enable CAT control

1. Click the **CAT** tray button on the right sidebar. The CAT Control applet appears.
2. Check the **Base** field. The default port is `4532`. Channels bind to port, port+1, port+2, port+3 (so channel A = 4532, B = 4533, and so on). Change this only if another program is already using port 4532; the value persists as `CatTcpPort`.
3. Click **Enable TCP**. The button turns green. AetherSDR starts four rigctld-compatible TCP servers.
4. On Linux or macOS, if your software expects a serial port rather than a TCP connection, also click **Enable TTY**. PTY symlinks appear at `/tmp/AetherSDR-CAT-A`, `/tmp/AetherSDR-CAT-B`, `/tmp/AetherSDR-CAT-C`, and `/tmp/AetherSDR-CAT-D`.

### 3. Configure your external software

**WSJT-X**

- In WSJT-X, open **File > Settings > Radio**.
- Set **Rig** to `rigctld (rigctld)` or `Hamlib NET rigctl`.
- Set **Network Server** to `localhost` and **Port** to `4532` (or the base port you set in step 2, offset by the channel letter you are using).
- In WSJT-X **Audio**, set **Input** to the DAX RX virtual audio device for channel 1 and **Output** to the DAX TX virtual audio device.

**fldigi**

- In fldigi, open **Configure > Rig Control > hamlib**.
- Set **Rig** to `Hamlib NET rigctl` and **Device** to `localhost:4532`.
- In **Configure > Sound Card**, select the DAX channel 1 virtual audio device for capture and playback.

> The exact names of the DAX virtual audio devices depend on your operating system and audio subsystem. On Linux with PipeWire they appear as AetherSDR DAX entries in your system audio mixer.

### 4. Optionally receive WSJT-X decodes as panadapter spots

1. Open **Settings > SpotHub...**.
2. Click the **WSJT-X** tab.
3. Confirm or set the **Address:** and **Port:** fields to match WSJT-X's multicast settings (`WsjtxAddress`, `WsjtxPort`).
4. Click **Start**. AetherSDR begins receiving decoded transmissions and displays them on the panadapter.
5. Enable **Auto-start on startup (WSJT-X)** to start the listener automatically; persists as `WsjtxAutoStart`.

### 5. Autostart on future launches

- To start the DAX bridge automatically: **Settings > Autostart DAX with AetherSDR** (saves `AutoStartDAX`).
- To start the CAT servers automatically: **Settings > Autostart CAT with AetherSDR** (saves `AutoStartCAT`).

## What each control does

| Control | Location | Default | Range | Setting key |
|---|---|---|---|---|
| **Enable** (DAX) | DAX applet | Off | On/Off | `AutoStartDAX` |
| **DAX 1 gain+meter** | DAX applet | 0.5 | 0.0–1.0 | `DaxRxGain1` |
| **DAX 2 gain+meter** | DAX applet | 0.5 | 0.0–1.0 | `DaxRxGain2` |
| **DAX 3 gain+meter** | DAX applet | 0.5 | 0.0–1.0 | `DaxRxGain3` |
| **DAX 4 gain+meter** | DAX applet | 0.5 | 0.0–1.0 | `DaxRxGain4` |
| **TX gain+meter** | DAX applet | 0.5 | 0.0–1.0 | `DaxTxGain` |
| **Enable TCP** | CAT applet | Off | On/Off | — |
| **Enable TTY** | CAT applet | Off | On/Off | — |
| **Base** (port) | CAT applet | 4532 | 1024–65535 | `CatTcpPort` |
| **Start / Stop** (WSJT-X) | SpotHub > WSJT-X tab | — | — | — |
| **Auto-start on startup (WSJT-X)** | SpotHub > WSJT-X tab | — | On/Off | `WsjtxAutoStart` |

## Tips

- The slice-assignment indicator next to each DAX channel shows **—** when no slice is routed there and **Slice A**–**Slice H** when one is. Confirm the correct slice is assigned before starting your external program.
- Out-of-range values in the **Base** port field snap back to `4532` automatically.
- If you run multiple digital programs simultaneously, assign each to a different DAX channel and a different CAT channel (A, B, C, or D) using the corresponding port offset.
- The WSJT-X spot filter checkboxes — **CQ**, **CQ POTA**, and **Calling Me** — let you restrict which decodes appear on the panadapter. These persist as `WsjtxFilterCQ`, `WsjtxFilterPOTA`, and `WsjtxFilterCallingMe`.

## Troubleshooting

- **WSJT-X reports "Rig control error"** — Confirm **Enable TCP** is active (button is green) in the CAT applet and that the port in WSJT-X matches the **Base** value (default `4532`). Check that no firewall is blocking localhost TCP connections.
- **No audio in WSJT-X** — Confirm **Enable** in the DAX applet is green and that the slice-assignment indicator next to DAX 1 shows your digital slice, not **—**. Also verify WSJT-X is pointed at the correct DAX virtual audio device.
- **TX audio not reaching the radio** — Check the **TX gain+meter** slider is not at 0.0 and that your digital slice holds TX privileges (the TX assignment indicator in the DAX applet shows your slice letter, not **—**).
- **CAT TTY ports not appearing** — **Enable TTY** is only available on Linux and macOS. On Windows, use TCP (`localhost:4532`) instead.

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
- [DAX Audio
