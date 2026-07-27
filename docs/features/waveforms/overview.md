# Waveforms overview

The Waveforms dialog mirrors the SmartSDR File > Waveforms panel, letting you view the WFP (Waveform Processor) status and manage installed waveforms on your FLEX-8600 radio. Use it to check whether the waveform processor is powered and ready, see its IP address, and restart or remove individual waveforms.

## How it works

The dialog connects directly to the radio's FlexWaveformModel for live status updates. It shows WFP power state, readiness, and IP address at the top, followed by a list of installed waveforms with per-row controls. A **WFP Support** pill indicates whether the connected radio has Waveform Processor hardware. The dialog also includes local digital-voice service configuration controls (available only when `kShowLocalDigitalVoiceControls` is enabled).

## What each control does

| Control | Behavior | Notes |
|---|---|---|
| **WFP Status** | Displays waveform processor power status, ready state, and IP address. | New in v26.5.2.1. Shows "WFP ON / READY", "WFP OFF / NOT READY", etc. |
| **WFP Support** | Indicates whether the connected radio has Waveform Processor hardware. Displays "Supported" (green) or "Not supported" (gray). Shows "No radio" when disconnected and "Checking" while waiting for radio identification. | Based on actual hardware capability, not the "wfp" license feature (#4210). |
| **Installed Waveforms** | Lists installed waveforms with **Restart** and **Remove/Uninstall** buttons per row. | Connects to FlexWaveformModel for live status. |
| **Install** | Launches a file dialog to select a Docker waveform image (.tar or .tgz file) for installation on the radio. Gated by the radio's connection state and WFP runtime status. | Disabled when no radio is connected, the platform does not support Docker deployment, or the WFP runtime status is unknown. |
| **Local Digital Voice Controls** | Configures local digital-voice services (D-Star, etc.) for AetherModem. Only shown when `kShowLocalDigitalVoiceControls` is enabled in the build configuration. | Not visible by default. |

## How to open

**File > Waveforms...**

## Requirements

- A radio connection must be active (the dialog requires radio connectivity) unless you are only viewing local waveform information.

## Docker waveform installation

The **Install** button is gated by the following conditions (checked in order):

1. **Radio connected**: You must be connected to a radio.
2. **Platform support**: The radio platform must support on-radio Docker waveform deployment (not a 6000-series Microburst/DeepEddy platform).
3. **WFP runtime status**: The Waveform Processor must be powered on and ready (WFP ON, READY).

If any condition fails, the button is disabled and a tooltip explains the reason.

## Connection status indicators

- **WFP Powered**: Shows whether the Waveform Processor power is on.
- **WFP Ready**: Shows whether the Waveform Processor is ready to accept waveform images.
- **WFP IP address**: Displays the Waveform Processor's IP address when available.

## Tips

- The dialog is non-modal, so you can keep it open while operating the radio.
- Use the **Restart** button to reload a waveform without removing and reinstalling it.
- Use **Remove/Uninstall** to delete an unwanted waveform from the radio.
- The dialog applies the current theme's styling for waveforms windows, ensuring visual consistency with other dialogs.
- The **WFP Support** indicator updates automatically when connecting to or disconnecting from a radio. If it shows "Checking" for more than a few seconds, try reconnecting to the radio.
- The Docker installation gate policy (implemented in `WaveformInstallGate.h`) uses only the radio's live WFP runtime state and platform capability — not the "wfp" license feature — so the **Install** button's enabled state matches actual hardware readiness.

## Related

- Radio Setup... — Configure radio connection, audio, antenna, and band settings.