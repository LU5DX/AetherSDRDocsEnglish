# Setting up digital modes (FT8, WSJT-X, fldigi)

This page explains how to connect WSJT-X, fldigi, or similar digital-mode software to AetherSDR so they can receive audio from the radio, send audio back for TX, and control the VFO. You need two bridges running in AetherSDR: DAX (audio) and CAT (frequency and mode control).

## Before you start

- AetherSDR is connected to the FLEX-8600 and at least one slice is active.
- WSJT-X, fldigi, or your chosen digital-mode application is installed.
- You know which slice letter (A, B, C, …) you intend to use for digital modes.

## Steps

### Part 1 — Enable DAX audio

1. Click the **DAX** tray button on the right sidebar. The DAX Audio applet opens.
2. Click **Enable**. The button turns green. AetherSDR starts the DAX audio bridge and persists the setting as `AutoStartDAX`.
3. Note the slice shown in the **Slice-assignment status** indicator next to the DAX channel you want to use (e.g., "Slice A" next to **DAX 1:**). If it shows —, assign the slice to a DAX channel in your radio's slice settings before continuing.
4. Optionally adjust the **DAX 1 gain+meter** slider for your RX channel. Default is 0.5; valid range is 0.0–1.0. This is persisted as `DaxRxGain1` (or `DaxRxGain2`–`DaxRxGain4` for other channels).
5. Optionally adjust the **TX gain+meter** slider. Default is 0.5; valid range is 0.0–1.0. Persisted as `DaxTxGain`.
6. To start DAX automatically on every launch, go to `Settings > Autostart DAX with AetherSDR` and check that item.

### Part 2 — Enable CAT control

1. Click the **CAT** tray button on the right sidebar. The CAT Control applet opens.
2. Check the **Base** port field. Default is `4532`. Channels A–D bind to ports 4532, 4533, 4534, 4535. Valid range is 1024–65535. Change the value if another application already uses port 4532.
3. Click **Enable TCP**. The button turns green. All four rigctld-compatible TCP servers start.
4. On Linux or macOS, click **Enable TTY** if your application requires a serial-style port. PTY symlinks appear at `/tmp/AetherSDR-CAT-A`, `/tmp/AetherSDR-CAT-B`, `/tmp/AetherSDR-CAT-C`, `/tmp/AetherSDR-CAT-D`.
5. To start CAT automatically on every launch, go to `Settings > Autostart CAT with AetherSDR` and check that item.

### Part 3 — Configure your digital-mode application

**WSJT-X**

1. In WSJT-X, open **Settings > Radio**.
2. Set **Rig** to `Hamlib NET rigctl`.
3. Set **Network Server** to `localhost:4532` (or the port matching your chosen slice channel).
4. Open **Settings > Audio** and set the **Input** and **Output** devices to the DAX channel assigned to your slice (e.g., `DAX 1`).

**fldigi**

1. In fldigi, open **Configure > Rig Control > Hamlib**.
2. Set **Device** to `Net rigctl` and **Port/Address** to `localhost:4532`.
3. Open **Configure > Sound Card** and select the DAX channel for input and output.

## What each control does

| Control | Default | Range | Setting key |
|---|---|---|---|
| **Enable** (DAX) | off | on/off | `AutoStartDAX` |
| **DAX 1 gain+meter** | 0.5 | 0.0–1.0 | `DaxRxGain1` |
| **DAX 2 gain+meter** | 0.5 | 0.0–1.0 | `DaxRxGain2` |
| **DAX 3 gain+meter** | 0.5 | 0.0–1.0 | `DaxRxGain3` |
| **DAX 4 gain+meter** | 0.5 | 0.0–1.0 | `DaxRxGain4` |
| **TX gain+meter** | 0.5 | 0.0–1.0 | `DaxTxGain` |
| **Enable TCP** (CAT) | off | on/off | — |
| **Enable TTY** (CAT) | off | on/off | — |
| **Base** (CAT TCP port) | 4532 | 1024–65535 | `CatTcpPort` |

## Tips

- Each CAT channel (A/B/C/D) controls one slice. If you run two digital-mode programs simultaneously, point the second program at port 4533 and assign it to Slice B with a second DAX channel.
- If you enter an out-of-range value in the **Base** field, it resets to `4532` automatically.
- The per-channel TCP status indicator in the CAT applet shows how many clients are connected (e.g., `:4532 (1 client)`). Use this to confirm WSJT-X has connected successfully.

## Troubleshooting

- **WSJT-X reports "Rig not found" or connection refused** — Confirm **Enable TCP** is active (button is green) and the port in WSJT-X matches the **Base** value in AetherSDR. Check that no firewall is blocking localhost connections.
- **No audio decoded in WSJT-X / fldigi** — Confirm **Enable** in the DAX applet is active. Check that the slice-assignment status next to the DAX channel you selected shows your slice letter and not —. Verify the audio input device in your digital-mode application is set to the correct DAX channel.
- **TX audio not reaching the radio** — Check the **TX gain+meter** slider is not at 0.0. Confirm the TX slice indicator in the DAX applet shows your active slice.
- **PTY symlinks not appearing (Linux/macOS)** — Confirm **Enable TTY** is active. The paths `/tmp/AetherSDR-CAT-A` through `/tmp/AetherSDR-CAT-D` are created when TTY is enabled and the radio is connected.

## Related

- [DAX Audio overview](../../features/dax/overview.md)
- [Enable DAX to route slice audio to WSJT-X / FLDigi / other digital software](../../features/dax/enable-dax-to-route-slice-audio-to-wsjt-x-fldigi-other-digital-software.md)
- [CAT Control overview](../../features/cat-control/overview.md)
- [Enable CAT TCP so N1MM, Log4OM, WSJT-X can control the radio](../../features/cat-control/enable-cat-tcp-so-n1mm-log4om-wsjt-x-can-control-the-radio.md)
- [Enable CAT PTY so Linux/macOS apps can open a serial-style CAT port](../../features/cat-control/enable-cat-pty-so-linux-macos-apps-can-open-a-serial-style-cat-port.md)
- [Autostart DAX on launch](../../features/dax/autostart-dax-on-launch.md)
- [Autostart CAT servers with AetherSDR](../../features/cat-control/autostart-cat-servers-with-aethersdr.md)
- [Change the base TCP port](../../features/cat-control/change-the-base-tcp-port.md)
- [Set DAX RX gain per channel](../../features/dax/set-dax-rx-gain-per-channel.md)
- [Start WSJT-X UDP listener and filter for CQ, POTA or calls to me](../../features/dx-cluster/start-wsjt-x-udp-listener-and-filter-for-cq-pota-or-calls-to-me.md)
