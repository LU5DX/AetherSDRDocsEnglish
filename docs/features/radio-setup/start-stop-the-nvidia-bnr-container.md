# Start/stop the NVIDIA BNR container

This page explains how to start, stop, and check the status of the NVIDIA Broadcast noise-removal (BNR) container from within AetherSDR. Use this feature to apply AI-based background noise removal to your received or transmitted audio.

## Before you start

- You must be connected to a FLEX-8600 radio. The Audio tab is not available without an active radio connection.
- The NVIDIA BNR container must already be installed on your system. AetherSDR controls the container but does not install it.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Audio** tab.
3. Locate the **NVIDIA BNR** section near the bottom of the tab.
4. To have the container start automatically each time AetherSDR connects, click **Autostart Container**.
5. To start the container immediately, click **Start**.
6. To stop the container, click **Stop**.
7. To query the current state of the container, click **Check Status**.

## What each control does

| Control | Behavior |
|---|---|
| **Autostart Container** | Starts the NVIDIA BNR container automatically when AetherSDR connects to the radio. |
| **Start** | Starts the container immediately. |
| **Stop** | Stops the container immediately. |
| **Check Status** | Queries the container and updates the status indicator. |
| NVIDIA BNR status dot | Colored dot showing the current container state: Running, Stopped, or Unknown. |

## Troubleshooting

- **Status dot shows Unknown after clicking Check Status** — The container runtime may not be reachable. Verify that the NVIDIA container runtime is installed and that your user has permission to manage containers. Click **Check Status** again after resolving any permission issues.
- **Start has no effect** — Confirm the NVIDIA BNR container image is present on your system. AetherSDR cannot install the container itself.

## Related

- [Choose PC input/output audio devices](choose-pc-input-output-audio-devices.md)
- [Pick Opus vs uncompressed audio for SmartLink](pick-opus-vs-uncompressed-audio-for-smartlink.md)
- [Turn on audio boost or enlarge the audio buffer for remote operation](turn-on-audio-boost-or-enlarge-the-audio-buffer-for-remote-operation.md)
- [Enable auto-record on TX and pick a save folder](enable-auto-record-on-tx-and-pick-a-save-folder.md)
