# Setting up digital modes (FT8, WSJT-X, fldigi)

This page explains how to configure AetherSDR so that digital mode programs such as WSJT-X and fldigi can receive audio from and control the FLEX-8600. It covers enabling the DAX audio bridge and the CAT control servers.

## Before you start

- AetherSDR is connected to your FLEX-8600 (the radio connection indicator shows active).
- The slice you want to use for digital modes is already created and tuned to the correct frequency and mode.
- WSJT-X, fldigi, or your other digital mode software is installed.

## Steps

### 1. Enable DAX audio routing

1. Click the **DAX** tray button on the right sidebar. The DAX Audio applet appears.
2. Click **Enable**. The button turns green. AetherSDR starts the DAX audio bridge and persists this state as `AutoStartDAX`.
3. Check the slice-assignment indicator next to the DAX channel you intend to use (for example, **DAX 1**). It shows either **—** (unassigned) or **Slice A..H**. Assign the correct slice to a DAX channel from the radio's slice settings if needed.
4. Drag the **DAX 1 gain+meter** slider to set the RX gain for that channel. The default is 0.5; the valid range is 0.0–1.0. This value is persisted as `DaxRxGain1`.
5. If your software also transmits (FT8 in WSJT-X, for example), drag the **TX gain+meter** slider to set the DAX TX level. Default is 0.5; valid range 0.0–1.0. Persisted as `DaxTxGain`.

### 2. Enable CAT control

1. Click the **CAT** tray button on the right sidebar. The CAT Control applet appears.
2. To use a TCP connection (required for WSJT-X and most digital software on all platforms): click **Enable TCP**. The button turns green. AetherSDR starts four rigctld-compatible TCP servers on ports **Base** through **Base+3** (default base port: **4532**, persisted as `CatTcpPort`).
3. On Linux or macOS, if your software expects a serial port device: click **Enable TTY**. AetherSDR creates PTY symlinks at `/tmp/AetherSDR-CAT-A`, `/tmp/AetherSDR-CAT-B`, `/tmp/AetherSDR-CAT-C`, and `/tmp/AetherSDR-CAT-D`.
4. To change the base TCP port, edit the **Base** field and press Enter. Valid range: 1024–65535. Out-of-range values revert to 4532. Running servers restart automatically on the new port.

### 3. Configure your digital mode software

**WSJT-X:**
- Set the radio interface to **Hamlib NET rigctl**, host `localhost`, port `4532` (or whichever port matches the slice's channel row in the CAT applet).
- Set the audio input device to the DAX RX channel you assigned (for example, **DAX 1** in your system audio device list).
- Set the audio output device to the DAX TX device.

**fldigi:**
- Under audio settings, select the DAX channel as the audio capture and playback device.
- For rig control, use **Hamlib**, select **NET rigctl**, and enter `localhost:4532`.

### 4. (Optional) Show WSJT-X decodes on the panadapter

1. Open `Settings > SpotHub...`.
2. Click the **WSJT-X** tab.
3. Enter the UDP bind address in **Address:** and the port in **Port:** to match what WSJT-X is configured to broadcast on (persisted as `WsjtxAddress` and `WsjtxPort`).
4. Click **Start**. The listener state changes to **Listening**.
5. Enable **Auto-start on startup** to have AetherSDR start the listener automatically on next launch (persisted as `WsjtxAutoStart`).
6. Use the **CQ**, **CQ POTA**, and **Calling Me** checkboxes to filter which decodes appear as spots on the panadapter (persisted as `WsjtxFilterCQ`, `WsjtxFilterPOTA`, `WsjtxFilterCallingMe`).

### 5. (Optional) Autostart DAX and CAT on launch

- To start DAX automatically: `Settings > Autostart DAX with AetherSDR`.
- To start CAT TCP automatically: `Settings > Autostart rigctld with AetherSDR`.
- To start CAT TTY automatically (Linux/macOS): `Settings > Autostart CAT with AetherSDR`.

## What each control does

| Control | Default | Range | Persisted key | Description |
|---|---|---|---|---|
| **Enable** (DAX) | Off | On/Off | `AutoStartDAX` | Master switch for the DAX audio bridge. |
| **DAX 1 gain+meter** | 0.5 | 0.0–1.0 | `DaxRxGain1` | RX gain for DAX channel 1. |
| **DAX 2 gain+meter** | 0.5 | 0.0–1.0 | `DaxRxGain2` | RX gain for DAX channel 2. |
| **DAX 3 gain+meter** | 0.5 | 0.0–1.0 | `DaxRxGain3` | RX gain for DAX channel 3. |
| **DAX 4 gain+meter** | 0.5 | 0.0–1.0 | `DaxRxGain4` | RX gain for DAX channel 4. |
| **TX gain+meter** | 0.5 | 0.0–1.0 | `DaxTxGain` | TX gain for the DAX TX stream. |
| **Enable TCP** | Off | On/Off | — | Starts all four rigctld TCP servers. |
| **Enable TTY** | Off | On/Off | — | Creates PTY symlinks (Linux/macOS only). |
| **Base** | 4532 | 1024–65535 | `CatTcpPort` | Base TCP port; channels use Base, Base+1, Base+2, Base+3. |

## Tips

- DAX channel assignment (which slice feeds which DAX channel) is visible in the slice-assignment indicator next to each channel row. It shows **—** when unassigned or **Slice A–H** when active.
- The per-channel TCP status in the CAT applet shows how many clients are connected (for example, `:4532 (1 client)`), which is useful for confirming that WSJT-X has successfully connected.
- If you run more than one digital program simultaneously, assign each to a different DAX channel and a different CAT channel (Base+1, Base+2, etc.).

## Troubleshooting

- **WSJT-X reports "Hamlib error" or cannot connect** — Confirm **Enable TCP** is active (button is green) in the CAT applet. Verify the port in WSJT-X matches the **Base** value. Check that no firewall is blocking `localhost` connections.
- **No audio received in WSJT-X or fldigi** — Confirm **Enable** is active in the DAX applet and that the slice-assignment indicator for the channel shows the correct slice rather than **—**. Verify the application is using the correct DAX audio device.
- **PTY symlinks not appearing** — **Enable TTY** is only available on Linux and macOS. Confirm the button is active. Symlinks appear at `/tmp/AetherSDR-CAT-A` through `/tmp/AetherSDR-CAT-D`.
- **WSJT-X decodes not appearing on panadapter** — Confirm the SpotHub WSJT-X listener is in **Listening** state and that the UDP address and port match the "Reporting" settings in WSJT-X.

## Related

- [Enable DAX to route slice audio to WSJT-X / FLDigi / other digital software](../../features/dax/enable-dax-to-route-slice-audio-to-wsjt-x-fldigi-other-digital-software.md)
- [Enable CAT TCP so N1MM, Log4OM, WSJT-X can control the radio](../../features/cat-control/enable-cat-tcp-so-n1mm-log4om-wsjt-x-can-control-the-radio.md)
- [Enable CAT PTY so Linux/macOS apps can open a serial-style CAT port](../../features/cat-control/enable-cat-pty-so-linux-macos-apps-can-open-a-serial-style-cat-port.md)
- [Start WSJT-X UDP listener and filter for CQ, POTA or calls to me](../../features/dx-cluster/start-wsjt-x-udp-listener-and-filter-for-cq-pota-or-calls-to-me.md)
- [Autostart DAX on launch](../../features/dax/autostart-dax-on-launch.md)
- [Autostart CAT servers with AetherSDR](../../features/cat-control/autostart-cat-servers-with-aethersdr.md)
- [Set DAX RX gain per channel](../../features/dax/set-dax-rx-gain-per-channel.md)
- [Set DAX TX gain](../../features/dax/set-dax-tx-gain.md)
- [Change the base TCP port](../../features/cat-control/change-the-base-tcp-port.md)
