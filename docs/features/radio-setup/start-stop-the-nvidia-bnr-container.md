# Start/stop the NVIDIA BNR Container

The NVIDIA BNR (Broadcast Noise Removal) container provides AI-based noise suppression for your microphone audio. Use this page to start, stop, and check the status of that container from within AetherSDR.

## Before you start

- AetherSDR must be connected to the radio. The Audio tab is not functional without an active radio connection.
- The NVIDIA BNR container runtime must be installed and accessible on your system before AetherSDR can start it.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Audio** tab.
3. Scroll to the **NVIDIA BNR** section at the bottom of the tab.
4. To start the container, click **Start**.
5. To stop the container, click **Stop**.
6. To check whether the container is currently running, click **Check Status**. The colored status dot next to the controls updates to reflect Running, Stopped, or Unknown.
7. To have the container start automatically each time AetherSDR connects to the radio, click **Autostart Container** so it is active.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Autostart Container** | Button | Enables automatic container startup when AetherSDR connects to the radio. |
| **Start** | Button | Starts the NVIDIA BNR container. |
| **Stop** | Button | Stops the NVIDIA BNR container. |
| **Check Status** | Button | Queries the container and updates the status dot. |
| NVIDIA BNR status dot | Indicator | Colored dot showing the container state: Running, Stopped, or Unknown. |

## Tips

- After clicking **Start**, click **Check Status** to confirm the container reached the Running state before transmitting.
- If you do not need BNR on every session, leave **Autostart Container** inactive and start the container manually only when needed.

## Troubleshooting

- **Status dot shows Unknown after clicking Start** — The container runtime may not be installed or may not be on the system PATH. Verify the NVIDIA Broadcast runtime is correctly installed and retry.
- **Start has no effect** — Confirm AetherSDR is connected to the radio. The Audio tab controls are inactive without a live radio connection.

## Related

- [Choose PC input/output audio devices](choose-pc-input-output-audio-devices.md)
- [Pick Opus vs uncompressed audio for SmartLink](pick-opus-vs-uncompressed-audio-for-smartlink.md)
- [Turn on audio boost or enlarge the audio buffer for remote operation](turn-on-audio-boost-or-enlarge-the-audio-buffer-for-remote-operation.md)
- [Enable auto-record on TX and pick a save folder](enable-auto-record-on-tx-and-pick-a-save-folder.md)
