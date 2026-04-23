# Start/stop the NVIDIA BNR Container

This page explains how to start, stop, and check the status of the NVIDIA Broadcast Noise Removal (BNR) container from within AetherSDR. Use this feature to apply GPU-accelerated noise removal to your received or transmitted audio.

## Before you start

- AetherSDR must be connected to the radio. The Audio tab is unavailable without an active radio connection.
- The NVIDIA BNR container must be installed on your system separately. AetherSDR controls the container but does not install it.
- Open Radio Setup: `Settings > Radio Setup...`, then click the **Audio** tab.

## Steps

1. Go to `Settings > Radio Setup...`.
2. Click the **Audio** tab.
3. Locate the **NVIDIA BNR** section near the bottom of the tab.
4. To have the container start automatically each time AetherSDR connects to the radio, click **Autostart Container**.
5. To start the container immediately, click **Start**.
6. To stop a running container, click **Stop**.
7. To query the current state of the container without changing it, click **Check Status**.
8. Read the colored status dot next to the NVIDIA BNR controls to confirm the result: the dot indicates Running, Stopped, or Unknown.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Autostart Container** | Button | Toggles automatic container startup whenever AetherSDR connects to the radio. |
| **Start** | Button | Starts the NVIDIA BNR container immediately. |
| **Stop** | Button | Stops a running NVIDIA BNR container immediately. |
| **Check Status** | Button | Queries the container state and updates the status dot without changing the container. |
| NVIDIA BNR status dot | Indicator | Colored dot showing the container state: Running, Stopped, or Unknown. |

## Tips

- Use **Check Status** after clicking **Start** or **Stop** if the status dot does not update immediately. The container may take a moment to change state.
- **Autostart Container** is useful for remote or unattended operation where you want noise removal active without manual steps each session.

## Troubleshooting

- **Status dot shows Unknown after clicking Start** — The container may not be installed or may not be reachable. Verify the NVIDIA BNR container is installed and that your system meets the GPU requirements, then click **Check Status** again.
- **Stop has no effect** — The container may have been started outside of AetherSDR. Stop it from the system level, then click **Check Status** to confirm.

## Related

- [Choose PC input/output audio devices](choose-pc-input-output-audio-devices.md)
- [Pick Opus vs uncompressed audio for SmartLink](pick-opus-vs-uncompressed-audio-for-smartlink.md)
- [Turn on audio boost or enlarge the audio buffer for remote operation](turn-on-audio-boost-or-enlarge-the-audio-buffer-for-remote-operation.md)
- [Enable auto-record on TX and pick a save folder](enable-auto-record-on-tx-and-pick-a-save-folder.md)
