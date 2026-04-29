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

| Control                                       | Kind      | Behavior                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-----------------------------------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Autostart Container**                       | Button    | When active, AetherSDR starts the NVIDIA BNR container automatically on launch.                                                                                                                                                                                                                                                                                                                                                                 |
| **Start**                                     | Button    | Starts the NVIDIA BNR container immediately.                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Stop**                                      | Button    | Stops a running NVIDIA BNR container immediately.                                                                                                                                                                                                                                                                                                                                                                                               |
| **Check Status**                              | Button    | Queries the container state and updates the status dot.                                                                                                                                                                                                                                                                                                                                                                                         |
| NVIDIA BNR status dot                         | Indicator | Colored dot showing the container state: Running, Stopped, or Unknown.                                                                                                                                                                                                                                                                                                                                                                          |
| TX Follows Active Slice                       | Button    | TX follows the active slice. Mutually exclusive with **Active Slice Follows TX**. Disabled automatically during Split operation.                                                                                                                                                                                                                                                                                                                 |
| Active Slice Follows TX                       | Button    | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with **TX Follows Active Slice**.                                                                                                                                                                                                                                                                                                                   |
| Voice / CW / Digital filter sharpness sliders | Slider    | Sets filter sharpness (0=lowest latency to 3=sharpest) per mode. Slider is disabled when Auto is enabled. Commands sent as `radio filter_sharpness <mode> level=<N>`.                                                                                                                                                                                                                                                                           |
| Auto (Voice / CW / Digital)                   | Button    | Enables automatic filter-level selection for that mode and disables the manual sharpness slider. Commands sent as `radio filter_sharpness <mode> auto_level=1`.                                                                                                                                                                                                                                                                                  |
| Connect / Disconnect (TGXL)                   | Button    | Opens/closes direct TCP connection to the TGXL on port 9010. Saves IP and port to `TGXL_ManualIp` and `TGXL_ManualPort` on connect so AetherSDR auto-reconnects on startup. Required to recover TUNE on firmware 4.2+. When connected, the TUNE button sends the native `autotune` command directly to the TGXL instead of the radio-side path broken in firmware 4.2. If the IP field is empty and the radio has discovered the TGXL, the discovered IP is pre-filled. |
| Connect / Disconnect (PGXL)                   | Button    | Opens/closes direct TCP connection to the Power Genius XL (default port 9008). Saves IP and port to `PGXL_ManualIp` and `PGXL_ManualPort`.                                                                                                                                                                                                                                                                                                     |
| Connect / Disconnect (Antenna Genius)         | Button    | Opens/closes connection to the Antenna Genius (default port 9007). Saves IP and port to `AG_ManualIp` and `AG_ManualPort`.                                                                                                                                                                                                                                                                                                                      |

## Frequency calibration (RX tab)

In v0.9.2.1 the **RX** tab frequency calibration controls are available regardless of whether a GPSDO is installed. Previously, when a GPSDO was detected, the calibration fields were hidden and replaced with a message stating correction was not required. The tab now always shows the **Cal Frequency (MHz)** field and the **Start** button.

A status label appears beside **Start** and provides inline feedback throughout the calibration sequence:

| Status text     | Meaning                                                              |
|-----------------|----------------------------------------------------------------------|
| Starting...     | AetherSDR has sent the calibration commands to the radio.            |
| Busy            | The **Start** button is disabled; calibration is in progress.        |
| (error text)    | A problem was reported; check the value in **Cal Frequency (MHz)**.  |

When GPSDO hardware is present, the label at the top of the group reads "GPSDO installed. Manual frequency offset calibration available." (green). Without GPSDO the label reads "Manual frequency offset calibration available." (amber). In both cases the controls below the label behave identically.

### To calibrate frequency offset

1. Open `Settings > Radio Setup...`.
2. Click the **RX** tab.
3. Enter a known-accurate reference frequency in **Cal Frequency (MHz)** (for example, a WWV or WWVH carrier).
4. Verify the value is correct. If the field is empty, the status label shows "Enter cal frequency" and calibration does not start.
5. Click **Start**. The button label changes to **Busy** and is disabled until the calibration sequence completes.
6. Watch the status label for progress. When calibration finishes, the button re-enables and **Freq Offset (ppb)** reflects the measured correction.

### Notes

- Clicking **Start** resets `freq_error_ppb` to 0 before beginning the sweep, so any previously stored offset is cleared at the start of each run.
- Calibration state is tracked per dialog instance. Closing and reopening the dialog resets the status display; any in-progress radio-side calibration continues independently.

## Tips

- Click **Check Status** after clicking **Start** or **Stop** if the status dot does not update on its own, to confirm the container reached the expected state.
- If the **Start** button remains in the **Busy** state after an unexpected disconnect, close and reopen `Settings > Radio Setup...` to reset the button.

## Related

- [Choose PC input/output audio devices](choose-pc-input-output-audio-devices.md)
- [Pick Opus vs uncompressed audio for SmartLink](pick-opus-vs-uncompressed-audio-for-smartlink.md)
- [Turn on audio boost or enlarge the audio buffer for remote operation](turn-on-audio-boost-or-enlarge-the-audio-buffer-for-remote-operation.md)
- [Enable auto-record on TX and pick a save folder](enable-auto-record-on-tx-and-pick-a-save-folder.md)