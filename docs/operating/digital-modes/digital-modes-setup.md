# Setting up digital modes (FT8, WSJT-X, fldigi)

This page explains how to connect WSJT-X, fldigi, or other digital-mode software to your FLEX-8600 through AetherSDR. Two AetherSDR features are involved: DAX (audio routing) and CAT Control (frequency and mode control).

## Before you start

- AetherSDR is connected to your FLEX-8600 radio.
- The slice you intend to use for digital modes is already created and tuned to the correct band.
- WSJT-X, fldigi, or your preferred digital-mode application is installed.

## Steps

### Part 1 — Route audio with DAX

1. Click the **DAX** tray button on the right sidebar. The DAX Audio applet appears.
2. Click **Enable**. The button turns green. AetherSDR starts the DAX audio bridge and persists this as `AutoStartDAX`.
3. Locate the channel row (**DAX 1**, **DAX 2**, **DAX 3**, or **DAX 4**) whose slice-assignment indicator shows the slice you are using (for example, `Slice A`). If no slice is assigned yet, assign one from the radio's slice settings.
4. Note the DAX channel number. You will enter this channel as the audio device in your digital-mode software.
5. Drag the **DAX 1 gain+meter** (or whichever channel you chose) to set the RX gain. The default is `0.5`; valid range is `0.0`–`1.0`. Adjust until the digital software receives a clean signal level.
6. Drag the **TX gain+meter** to set the transmit audio level. Default is `0.5`; valid range is `0.0`–`1.0`.
7. In your digital-mode software, select the corresponding DAX channel as the audio input and output device. On Linux these appear as PipeWire or ALSA devices named for the DAX channel; on macOS they appear as CoreAudio devices.

### Part 2 — Connect CAT control

1. Click the **CAT** tray button on the right sidebar. The CAT Control applet appears.
2. Check the **Base** field. The default port is `4532`. Channels A through D bind to Base, Base+1, Base+2, and Base+3. Change the value only if port 4532 is already in use on your system; valid range is `1024`–`65535`. The value persists as `CatTcpPort`.
3. Click **Enable TCP**. The button turns green. AetherSDR starts rigctld-compatible TCP servers on the four ports.
4. On Linux or macOS, if your software requires a serial-style CAT port, click **Enable TTY** as well. Symlinks are created at `/tmp/AetherSDR-CAT-A` through `/tmp/AetherSDR-CAT-D`.
5. In your digital-mode software, configure the radio interface:
   - **Rig model:** select Hamlib NET rigctl (or equivalent).
   - **Network address:** `localhost` (or the machine running AetherSDR).
   - **Port:** the Base port for slice A (`4532` by default), or Base+1 for slice B, and so on.
   - Alternatively, point the software at the PTY path (for example `/tmp/AetherSDR-CAT-A`) if using **Enable TTY**.

### Part 3 — Connect WSJT-X spot decodes to the panadapter (optional)

1. Open `Settings > SpotHub...`.
2. Click the **WSJT-X** tab.
3. Set **Address:** and **Port:** to match what WSJT-X is configured to send UDP messages to (WSJT-X default is `224.0.0.1` multicast or `localhost`, port `2237`). These persist as `WsjtxAddress` and `WsjtxPort`.
4. Click **Start**. AetherSDR begins listening for WSJT-X UDP messages.
5. Enable the filters you want: check **CQ** to show only CQ calls, **CQ POTA** for POTA calls, or **Calling Me** to show only decodes addressed to your callsign. These persist as `WsjtxFilterCQ`, `WsjtxFilterPOTA`, and `WsjtxFilterCallingMe`.
6. Decoded transmissions appear in the **WSJT-X Decodes** console and as spots on the panadapter.
7. To keep the listener running across restarts, enable **Auto-start on startup (WSJT-X)**. This persists as `WsjtxAutoStart`.

## What each control does

### DAX Audio applet

| Control | Default | Range | Setting key | What it does |
|---|---|---|---|---|
| Enable | Off | On/Off | `AutoStartDAX` | Starts the DAX audio bridge. Master switch for all RX and TX streams. |
| DAX 1–4 gain+meter | `0.5` | `0.0`–`1.0` | `DaxRxGain1`–`DaxRxGain4` | Sets RX gain on each DAX channel. Drag to adjust. |
| TX gain+meter | `0.5` | `0.0`–`1.0` | `DaxTxGain` | Sets the transmit audio level for the DAX TX stream. |
| Slice-assignment indicator | — | `—` or `Slice A`–`H` | — | Shows which slice is routed to each DAX channel. |

### CAT Control applet

| Control | Default | Range | Setting key | What it does |
|---|---|---|---|---|
| Enable TCP | Off | On/Off | — | Starts all four rigctld TCP servers on Base through Base+3. |
| Enable TTY | Off | On/Off | — | Creates PTY symlinks at `/tmp/AetherSDR-CAT-A` through `-D` (Linux/macOS only). |
| Base | `4532` | `1024`–`65535` | `CatTcpPort` | Base TCP port. Out-of-range values snap back to `4532`. Servers restart automatically if already running. |

### SpotHub — WSJT-X tab

| Control | Default | Setting key | What it does |
|---|---|---|---|
| Address: | — | `WsjtxAddress` | UDP bind address for WSJT-X messages. |
| Port: | — | `WsjtxPort` | UDP port for WSJT-X messages. |
| Auto-start on startup (WSJT-X) | — | `WsjtxAutoStart` | Starts the listener automatically when AetherSDR launches. |
| CQ | — | `WsjtxFilterCQ` | Shows only CQ calls from WSJT-X decodes. |
| CQ POTA | — | `WsjtxFilterPOTA` | Shows CQ POTA calls. |
| Calling Me | — | `WsjtxFilterCallingMe` | Shows only decodes addressed to your callsign. |
| Spot Life: | — | `WsjtxSpotLife` | Seconds WSJT-X spots remain visible on the panadapter. |

## Tips

- To have DAX start automatically every time AetherSDR opens, use `Settings > Autostart DAX with AetherSDR` instead of clicking **Enable** each session.
- To have CAT servers start automatically, use `Settings > Autostart CAT with AetherSDR`.
- The channel-row indicators in the CAT Control applet show how many clients are connected (for example, `:4532 (1 client)`). Use this to confirm WSJT-X or fldigi has connected successfully.
- Each digital-mode application should use a different DAX channel and a different CAT channel (A, B, C, or D) if you run more than one simultaneously.

## Troubleshooting

- **Digital software receives no audio** — Confirm **Enable** is active in the DAX Audio applet (button is green). Check that the slice-assignment indicator on the correct DAX channel shows your slice rather than `—`. Verify the software is using the correct DAX device.
- **CAT software cannot connect** — Confirm **Enable TCP** is active. Check that the port configured in the external software matches the **Base** value (or Base+N for the correct channel). Ensure no firewall is blocking the port on localhost.
- **PTY path not found** — **Enable TTY** is only available on Linux and macOS. Confirm the button is active. The symlinks appear at `/tmp/AetherSDR-CAT-A` through `/tmp/AetherSDR-CAT-D`.
- **No WSJT-X decodes appear on the panadapter** — Confirm **Start** was clicked in `Settings > SpotHub... > WSJT-X`. Verify the **Address:** and **Port:** in AetherSDR match the UDP destination configured in WSJT-X.

## Related

- [Enable DAX to route slice audio to WSJT-X / FLDigi / other digital software](../../features/dax/enable-dax-to-route-slice-audio-to-wsjt-x-fldigi-other-digital-software.md)
- [Enable CAT TCP so N1MM, Log4OM, WSJT-X can control the radio](../../features/cat-control/enable-cat-tcp-so-n1mm-log4om-wsjt-x-can-control-the-radio.md)
- [Enable CAT PTY so Linux/macOS apps can open a serial-style CAT port](../../features/cat-control/enable-cat-pty-so-linux-macos-apps-can-open-a-serial-style-cat-port.md)
- [Start WSJT-X UDP listener and filter for CQ, POTA or calls to me](../../features/dx-cluster/start-wsjt-x-udp-listener-and-filter-for-cq-pota-or-calls-to-me.md)
- [Autostart DAX on launch](../../features/dax/autostart-dax
