# Start/stop the NVIDIA BNR Container

The NVIDIA BNR (Broadcast Noise Removal) container applies AI-based noise reduction to your transmitted audio. Use this page to start, stop, and check the status of the container from within AetherSDR.

## Before you start

- AetherSDR must be connected to the radio. The Audio tab is only accessible while connected.
- NVIDIA BNR requires a compatible NVIDIA GPU and the container runtime installed on your system. Confirm the container environment is functional outside AetherSDR before proceeding.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Audio** tab.
3. Locate the **NVIDIA BNR** group near the bottom of the tab.
4. To start the container, click **Start**.
5. To stop the container, click **Stop**.
6. To enable automatic startup, click **Autostart Container** so it activates each time AetherSDR connects to the radio.
7. To check the current state, click **Check Status**. The colored status dot next to the controls updates to reflect Running, Stopped, or Unknown.

## What each control does

| Control | Description |
|---|---|
| **Autostart Container** | Starts the BNR container automatically each time AetherSDR connects to the radio. |
| **Start** | Starts the NVIDIA BNR container immediately. |
| **Stop** | Stops the NVIDIA BNR container immediately. |
| **Check Status** | Queries the container state and updates the status dot. |
| Status dot | Colored indicator showing the container state: Running, Stopped, or Unknown. |

## Tips

- If you use BNR regularly, enable **Autostart Container** so you do not need to start it manually each session.
- After clicking **Start** or **Stop**, click **Check Status** to confirm the state has changed as expected.

## Troubleshooting

- **Status dot shows Unknown after clicking Start** — The container runtime may not be installed or accessible. Verify the NVIDIA container runtime is correctly installed on your system and that the required container image is present.
- **Start has no effect** — Confirm your system has a supported NVIDIA GPU and that the container engine (e.g. Docker or Podman with NVIDIA support) is running before launching AetherSDR.

## Related

- [Choose PC input/output audio devices](choose-pc-input-output-audio-devices.md)
- [Pick Opus vs uncompressed audio for SmartLink](pick-opus-vs-uncompressed-audio-for-smartlink.md)
- [Turn on audio boost or enlarge the audio buffer for remote operation](turn-on-audio-boost-or-enlarge-the-audio-buffer-for-remote-operation.md)
- [Enable auto-record on TX and pick a save folder](enable-auto-record-on-tx-and-pick-a-save-folder.md)
