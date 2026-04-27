# Start/stop the NVIDIA BNR Container

The NVIDIA BNR (Broadcast Noise Removal) container applies AI-based noise suppression to your microphone audio. Use the controls on the Audio tab to start, stop, or check the state of the container without leaving AetherSDR.

## Before you start

- AetherSDR must be connected to the radio. The Audio tab is not accessible when disconnected.
- The NVIDIA Broadcast container must be installed on your system independently of AetherSDR. AetherSDR controls it but does not install it.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Audio** tab.
3. Locate the **NVIDIA BNR** section near the bottom of the tab.
4. To have the container start automatically each time AetherSDR launches, click **Autostart Container** so it is active.
5. To start the container immediately, click **Start**.
6. To stop a running container, click **Stop**.
7. To query the current state without changing it, click **Check Status**. The colored status dot next to the controls updates to reflect Running, Stopped, or Unknown.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Autostart Container** | Button | When active, AetherSDR starts the NVIDIA BNR container automatically on launch. |
| **Start** | Button | Starts the NVIDIA BNR container immediately. |
| **Stop** | Button | Stops a running NVIDIA BNR container immediately. |
| **Check Status** | Button | Queries the container state and updates the status dot. |
| NVIDIA BNR status dot | Indicator | Colored dot showing the container state: Running, Stopped, or Unknown. |

## Tips

- Click **Check Status** after clicking **Start** or **Stop** if the status dot does not update on its own, to confirm the container reached the expected state.

## Related

- [Choose PC input/output audio devices](choose-pc-input-output-audio-devices.md)
- [Pick Opus vs uncompressed audio for SmartLink](pick-opus-vs-uncompressed-audio-for-smartlink.md)
- [Turn on audio boost or enlarge the audio buffer for remote operation](turn-on-audio-boost-or-enlarge-the-audio-buffer-for-remote-operation.md)
- [Enable auto-record on TX and pick a save folder](enable-auto-record-on-tx-and-pick-a-save-folder.md)
