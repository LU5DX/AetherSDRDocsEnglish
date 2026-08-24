# Choose PC input/output audio devices

This page explains how to select which PC audio devices AetherSDR uses for radio receive audio output and microphone input. You need to do this when you first set up AetherSDR or when you change headsets, speakers, or audio interfaces.

## Before you start

- The radio must be connected. Radio Setup controls are unavailable without an active radio connection.
- Know which audio input and output devices your PC exposes (check your OS audio settings if unsure).

## Steps

1. Click `Settings > Radio Setup...` to open the Radio Setup dialog.
2. Click the **Audio** tab.
3. Under **PC Audio Devices:**, click the **Input:** drop-down and select the device you want to use for microphone or audio input.
4. Click the **Output:** drop-down and select the device you want to use for receive audio playback.
5. Close the dialog. The selections take effect immediately.

## What each control does

| Control | What it does |
|---------|---------------|
| **Input:** (PC Audio Devices) | Selects the host audio input device used for microphone or line-in audio. |
| **Output:** (PC Audio Devices) | Selects the host audio output device used for receive audio playback. |
| **Audio Boost:** | Toggle that enables extra gain on the client audio path. Stored in AppSettings as `AudioBoost`. |
| **Audio Buffer:** | Text field (default 200, range 50–1000 ms) that increases the audio buffer to compensate for VPN/SmartLink jitter. Stored as `AudioBufferMs` and applied to the audio engine's RX buffer cap. |
| **Prevent system sleep while connected** | Checkbox (default off) that keeps the OS awake while the radio is connected to prevent audio/TCP/UDP stream drops during idle periods. Stored as `InhibitSleepWhileConnected`. |
| **Recording: Radio Side / Client Side** | Toggle that selects whether recordings are made on the radio (SmartSDR) or on the client PC. Stored as `RecordingMode`. |
| **Save to:** | Text field setting the folder for client-side recordings. Defaults to Documents/AetherSDR/Recordings. Stored as `QsoRecordingDir`. |
| **...** (browse) | Opens a folder picker for the recording directory. |
| **Auto-record on TX** | Checkbox (default off) that starts recording automatically when transmitting. Stored as `QsoRecordingAutoRecord`. |
| **Idle timeout:** | Spinbox (default 120, range 10–3600 seconds) that stops recording after this many seconds of silence. Stored as `QsoRecordingIdleTimeout`. |
| **Line Out:** | Slider controlling line-out gain. |
| **Mute (Line Out)** | Button that mutes the line-out. |
| **Headphone:** | Slider controlling headphone gain. |
| **Mute (Headphone)** | Button that mutes the headphone output. |
| **Front Speaker: / Mute** | Button that mutes the front speaker (model-specific). |
| **Audio Compression (SmartLink): Auto / Uncompressed / Opus** | Selects the audio codec for SmartLink/LAN connections. Stores in `AudioCompression`. |
| **NVIDIA BNR: Autostart Container / Start / Stop / Check Status** | Controls the NVIDIA Broadcast noise-removal container. A status dot indicates Running/Stopped/Unknown. |

## Calibration tab

The **Calibration** tab is new in v26.8.4. It provides manual frequency calibration for radios that cannot calibrate their own oscillator (such as the HL2). The tab is hidden unless the connected radio's backend reports `hostFrequencyCalibration` capability — for example, it does not appear on FLEX-8000 radios, which calibrate via the RX tab's GPSDO controls.

| Control | What it does |
|---------|---------------|
| **Cal Frequency (MHz):** | Spinbox setting the frequency used for manual calibration. Requires the radio to be on this frequency. |
| **Start** | Begins the frequency calibration sweep. |
| **Freq Offset (ppb):** | Manual frequency offset in parts per billion, shown after the sweep completes. |
| **Trim** | Applies the measured offset to the radio's host clock. |

The stored calibration value is re-read whenever the dialog is shown and whenever the radio connection changes, so a Trim press cannot commit a previous radio's calibration by mistake.