# Setting up digital modes (FT8, WSJT-X, fldigi)

This page explains how to connect WSJT-X, fldigi, or other digital-mode software to AetherSDR so that audio and radio control flow correctly. You need to route receive audio out of the radio (via DAX) and give your digital software a way to control frequency and mode (via CAT).

## Before you start

- AetherSDR is connected to a FLEX-8600 radio.
- At least one slice is active on the band you want to operate.
- Your digital software (WSJT-X, fldigi, etc.) is installed and not yet running.

## Steps

### 1. Enable the DAX audio bridge

1. Click the **DAX** tray button on the right sidebar to open the DAX Audio applet.
2. Click **Enable**. The button turns green. This starts the audio bridge for all DAX channels.
3. Note which channel shows your slice in the slice-assignment indicator (e.g. "Slice A"). That is the channel number to use in your digital software's audio device settings.
4. If the audio level is too low or too high, drag the meter/slider for that channel left or right. The default gain is 0.5 (range 0.0–1.0); the value persists as `DaxRxGain1` through `DaxRxGain4`.
5. For transmit audio, drag the **TX** meter/slider to set the DAX TX gain. Default is 0.5; persists as `DaxTxGain`.

### 2. Enable CAT control

1. Click the **CAT** tray button on the right sidebar to open the CAT Control applet.
2. Choose how your digital software will connect:

   - **TCP (all platforms):** Click **Enable TCP**. AetherSDR starts four rigctld-compatible TCP servers. Channel A listens on the base port, B on base+1, C on base+2, D on base+3. The default base port is `4532`, persisted as `CatTcpPort`.
   - **PTY virtual serial port (Linux/macOS only):** Click **Enable TTY**. AetherSDR creates symlinks at `/tmp/AetherSDR-CAT-A`, `/tmp/AetherSDR-CAT-B`, `/tmp/AetherSDR-CAT-C`, and `/tmp/AetherSDR-CAT-D`.

3. Confirm that the channel row matching your slice shows a port or PTY path and a client count.

### 3. Configure your digital software

#### WSJT-X

- **Rig:** Select "Hamlib NET rigctl".
- **Network server:** `localhost:4532` (or the port matching your slice's channel).
- **Audio input:** Select the DAX RX virtual audio device for the channel noted in step 1.
- **Audio output:** Select the DAX TX virtual audio device.
- **PTT method:** Set to "CAT" or "RTS" depending on your preference; CAT PTT works over the same rigctld connection.

#### fldigi

- **Rig control:** Select "hamlib" and set the rig to "Hamlib NET rigctl" at `localhost:4532`.
- **Audio capture/playback:** Select the DAX channel device matching your slice.

### 4. (Optional) Configure WSJT-X spot display on the panadapter

1. Open `Settings > SpotHub...`.
2. Click the **WSJT-X** tab.
3. Set **Address:** and **Port:** to match the UDP multicast address and port configured in WSJT-X (WSJT-X default is `224.0.0.1`, port `2237`; values persist as `WsjtxAddress` and `WsjtxPort`).
4. Click **Start**. The button changes to **Stop** when the listener is active.
5. Use the **CQ**, **CQ POTA**, and **Calling Me** checkboxes to filter which decodes appear as spots on the panadapter.
6. To keep the listener running automatically, enable **Auto-start on startup (WSJT-X)**; persists as `WsjtxAutoStart`.

### 5. (Optional) Autostart DAX and CAT on every launch

- To start DAX automatically: `Settings > Autostart DAX with AetherSDR`. Persists as `AutoStartDAX`.
- To start CAT TCP automatically: `Settings > Autostart rigctld with AetherSDR`. Persists as `AutoStartRigctld` (Linux/macOS only for TTY: `Settings > Autostart CAT with AetherSDR`, persists as `AutoStartCAT`).

## What each control does

| Control | Where | Default | Range | Setting key |
|---|---|---|---|---|
| **Enable** (DAX master) | DAX applet | Off | On/Off | `AutoStartDAX` |
| DAX 1–4 gain+meter | DAX applet | 0.5 | 0.0–1.0 | `DaxRxGain1`–`DaxRxGain4` |
| TX gain+meter | DAX applet | 0.5 | 0.0–1.0 | `DaxTxGain` |
| Slice-assignment indicator | DAX applet | — | — or Slice A–H | (none) |
| **Enable TCP** | CAT applet | Off | On/Off | (none; base port: `CatTcpPort`) |
| **Enable TTY** | CAT applet | Off | On/Off | (none) |
| **Base** (TCP port) | CAT applet | 4532 | 1024–65535 | `CatTcpPort` |
| **Start / Stop** (WSJT-X UDP) | SpotHub > WSJT-X tab | — | — | (none) |
| **Address:** (WSJT-X) | SpotHub > WSJT-X tab | — | — | `WsjtxAddress` |
| **Port:** (WSJT-X) | SpotHub > WSJT-X tab | — | 1–65535 | `WsjtxPort` |
| **Auto-start on startup (WSJT-X)** | SpotHub > WSJT-X tab | — | On/Off | `WsjtxAutoStart` |
| **CQ** filter | SpotHub > WSJT-X tab | — | On/Off | `WsjtxFilterCQ` |
| **CQ POTA** filter | SpotHub > WSJT-X tab | — | On/Off | `WsjtxFilterPOTA` |
| **Calling Me** filter | SpotHub > WSJT-X tab | — | On/Off | `WsjtxFilterCallingMe` |
| **Spot Life:** | SpotHub > WSJT-X tab | — | — | `WsjtxSpotLife` |

## Tips

- Each CAT channel (A–D) is independent. If you run two digital programs simultaneously, point the second at port `4533` (or `/tmp/AetherSDR-CAT-B`) and route its audio to DAX channel 2.
- The per-channel TCP status indicator shows "(stopped)", ":\<port\> (1 client)", or ":\<port\> (N clients)". Confirm your software has connected before calling CQ.
- Out-of-range values entered in the **Base** field snap back to `4532` automatically.

## Troubleshooting

- **WSJT-X shows "Rig not responding"** — Confirm **Enable TCP** is active (button lit green) in the CAT applet and that the port in WSJT-X matches the **Base** value (default `4532`). Check that no firewall blocks localhost TCP connections.
- **No audio decoded in WSJT-X or fldigi** — Confirm **Enable** is active in the DAX applet. Check the slice-assignment indicator on the correct DAX channel shows your active slice, not "—". Adjust the DAX RX gain slider if the level meter is not moving.
- **PTY path not appearing** — **Enable TTY** is available on Linux and macOS only. Confirm AetherSDR has permission to create files under `/tmp`.
- **WSJT-X decodes not appearing on panadapter** — Verify the **Start / Stop** button in SpotHub shows the listener as started, and that the **Address:** and **Port:** match the UDP reporting settings inside WSJT-X.

## Related

- [Enable DAX to route slice audio to WSJT-X / FLDigi / other digital software](../../features/dax/enable-dax-to-route-slice-audio-to-wsjt-x-fldigi-other-digital-software.md)
- [Enable CAT TCP so N1MM, Log4OM, WSJT-X can control the radio](../../features/cat-control/enable-cat-tcp-so-n1mm-log4om-wsjt-x-can-control-the-radio.md)
- [Enable CAT PTY so Linux/macOS apps can open a serial-style CAT port](../../features/cat-control/enable-cat-pty-so-linux-macos-apps-can-open-a-serial-style-cat-port.md)
- [Start WSJT-X UDP listener and filter for CQ, POTA or calls to me](../../features/dx-cluster/start-wsjt-x-udp-listener-and-filter-for-cq-pota-or-calls-to-me.md)
- [Set DAX RX gain per channel](../../features/dax/set-dax-rx-gain-per-channel.md)
- [Set DAX TX gain](../../features/dax/set-dax-tx-gain.md)
- [Autostart DAX on launch](../../features/dax/autostart-dax-on-launch.md)
- [Autostart CAT servers with AetherSDR](../../features/cat-control/autostart-cat-servers-with-aethersdr.md)
- [Change the base
