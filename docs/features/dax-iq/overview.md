# DAX IQ Overview

The DAX IQ applet lets you enable up to four independent IQ data streams from your FLEX-8600, set each stream's sample rate, and monitor each stream's signal level in real time. Use these streams to feed external SDR software with raw IQ data from the radio.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The DAX IQ applet requires an active radio connection.
- The applet panel must be visible. If it is not, click `View > Applet Panel` to show it.

## How it works

The DAX IQ applet provides four independent IQ stream channels, labeled IQ 1 through IQ 4. Each channel is controlled entirely within a single row of the applet. Streams are per-session: the radio does not persist stream state across disconnections, but AetherSDR saves each channel's enabled state and sample rate locally, and re-enables any previously active channels approximately 1.5 seconds after a successful reconnection.

When you toggle a channel on, AetherSDR requests the stream from the radio. When the radio confirms the stream is active, the channel's toggle button updates to reflect the live state. If the radio rejects or removes a stream, the button and meter reset automatically.

The applet is hidden by default. Toggle it open or closed using the IQ tray button on the right sidebar.

## What each control does

| Control | What it does | Default | Valid values | Persisted setting key |
|---|---|---|---|---|
| IQ 1..4 rate | Sets the sample rate for that IQ channel. The combo syncs back to the radio-reported rate when a stream is active. | 48k | 24k (24000), 48k (48000), 96k (96000), 192k (192000) | `DaxIqRate1` – `DaxIqRate4` |
| IQ 1..4 meter | Shows the RMS level of the IQ stream on a 0–100 scale (scaled from RMS × 200). Resets to 0 on disconnect or disable. | 0 | 0–100 | — |
| IQ 1..4 Off/On | Toggles the IQ stream for that channel. Displays "Off" when inactive and "On" when active. | Off | Off, On | `DaxIqEnabled1` – `DaxIqEnabled4` |

## Tips

- Changing the sample rate while a stream is active sends the new rate to the radio immediately. If the radio reports a different rate back, the combo will sync to the radio-reported value.
- On reconnect, AetherSDR waits 1.5 seconds before re-enabling persisted channels to allow the radio session to fully initialize before stream requests are sent.
- Scrolling the applet panel will not accidentally change rate combos or other controls; the applet panel locks sidebar controls during scroll.

## Troubleshooting

- **Channel shows "On" but resets to "Off" immediately** — The radio rejected the stream request, likely because the session was not fully ready. Disconnect and reconnect, or wait a moment and toggle the channel again.
- **Rate combo shows a different value than what you selected** — The radio reported a different sample rate for the active stream. The combo syncs to the radio-reported value; this is expected behavior.
- **Meter stays at 0 while a channel is "On"** — No IQ data is being received. Confirm that external software is connected to the stream and that the radio is actively processing audio on the associated slice.

## Related

- [Enable an IQ stream for external SDR software](enable-an-iq-stream-for-external-sdr-software.md)
- [Pick the IQ sample rate (24k/48k/96k/192k)](pick-the-iq-sample-rate-24k-48k-96k-192k.md)
- [Monitor the RMS level of each IQ stream](monitor-the-rms-level-of-each-iq-stream.md)
- [Disable an IQ stream to free bandwidth](disable-an-iq-stream-to-free-bandwidth.md)
