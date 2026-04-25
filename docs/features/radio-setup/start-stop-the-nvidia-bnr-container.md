# Start/stop the NVIDIA BNR container

This page explains how to start, stop, and check the status of the NVIDIA Broadcast noise-removal (BNR) container from within AetherSDR. Use BNR to apply GPU-accelerated noise reduction to your received or transmitted audio.

## Before you start

- AetherSDR must be connected to a radio. The Audio tab in Radio Setup is not accessible without a radio connection.
- The NVIDIA Broadcast container runtime must already be installed on your system. AetherSDR does not install it.
- A supported NVIDIA GPU must be present and recognized by your system.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Audio** tab.
3. Scroll to the **NVIDIA BNR** section at the bottom of the tab.
4. To start the container, click **Start**.
5. To stop the container, click **Stop**.
6. To confirm the container state without changing it, click **Check Status**.
7. To have AetherSDR start the container automatically each time it connects to the radio, click **Autostart Container** so it is active.

The colored status dot next to the NVIDIA BNR controls updates to reflect the current container state: running, stopped, or unknown.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Autostart Container** | Button | When active, AetherSDR starts the BNR container automatically on radio connection. |
| **Start** | Button | Starts the NVIDIA BNR container immediately. |
| **Stop** | Button | Stops the NVIDIA BNR container immediately. |
| **Check Status** | Button | Queries the container state and updates the status dot without changing the container. |
| Status dot | Indicator | Colored dot showing Running, Stopped, or Unknown. |

## Troubleshooting

- **Status dot shows Unknown after clicking Start** — The container runtime may not be installed or the GPU is not accessible. Verify your NVIDIA Broadcast installation and GPU driver outside of AetherSDR, then click **Check Status** again.
- **Start and Stop have no effect** — AetherSDR launches the container as a subprocess. If the required runtime binary is not on the system PATH, the command will silently fail. Confirm the NVIDIA Broadcast runtime is installed and accessible from a terminal before using these controls.

## Related

- [Choose PC input/output audio devices](choose-pc-input-output-audio-devices.md)
- [Pick Opus vs uncompressed audio for SmartLink](pick-opus-vs-uncompressed-audio-for-smartlink.md)
- [Turn on audio boost or enlarge the audio buffer for remote operation](turn-on-audio-boost-or-enlarge-the-audio-buffer-for-remote-operation.md)
- [Enable auto-record on TX and pick a save folder](enable-auto-record-on-tx-and-pick-a-save-folder.md)
