# Waveforms overview

The Waveforms dialog mirrors the SmartSDR File > Waveforms panel, letting you view the WFP (Waveform Processor) status and manage installed waveforms on your FLEX-8600 radio. Use it to check whether the waveform processor is powered and ready, see its IP address, and restart or remove individual waveforms.

## How it works

The dialog connects directly to the radio's FlexWaveformModel for live status updates. It shows WFP power state, readiness, and IP address at the top, followed by a list of installed waveforms with per-row controls.

## What each control does

| Control | Behavior | Notes |
|---|---|---|
| **WFP Status** | Displays waveform processor power status, ready state, and IP address. | New in v26.5.2.1. |
| **Installed Waveforms** | Lists installed waveforms with **Restart** and **Remove/Uninstall** buttons per row. | Connects to FlexWaveformModel for live status. |

## How to open

**File > Waveforms...**

## Requirements

- A radio connection must be active (the dialog requires radio connectivity).

## Tips

- The dialog is non-modal, so you can keep it open while operating the radio.
- Use the **Restart** button to reload a waveform without removing and reinstalling it.
- Use **Remove/Uninstall** to delete an unwanted waveform from the radio.
- The dialog applies the current theme's styling for waveforms windows, ensuring visual consistency with other dialogs.

## Related

- Radio Setup... — Configure radio connection, audio, antenna, and band settings.