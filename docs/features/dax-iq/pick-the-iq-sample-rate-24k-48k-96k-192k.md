# Pick the IQ Sample Rate (24k/48k/96k/192k)

This page explains how to change the sample rate for any of the four DAX IQ channels. You would do this to match the rate expected by external SDR software receiving the IQ stream.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The DAX IQ applet does not function without an active radio connection.
- The DAX IQ applet must be visible. If it is not, click the **IQ** tray button on the right sidebar to show it.

## Steps

1. Open the DAX IQ applet by clicking the **IQ** tray button on the right sidebar if it is not already visible.
2. Locate the row for the channel you want to change: **IQ 1**, **IQ 2**, **IQ 3**, or **IQ 4**.
3. Click the rate combo box in that row. It shows the current rate (default: **48k**).
4. Select one of the available rates: **24k**, **48k**, **96k**, or **192k**.

The new rate takes effect immediately and is sent to the radio. If the stream for that channel is active, the combo box will reflect the rate reported back by the radio.

## What each control does

| Control | Description | Default | Valid values | Persisted setting |
|---|---|---|---|---|
| Rate combo box (IQ 1–4) | Sets the IQ sample rate for that channel in samples per second. | 48k (48000) | 24k (24000), 48k (48000), 96k (96000), 192k (192000) | `DaxIqRate1` – `DaxIqRate4` |
| Off/On toggle (IQ 1–4) | Enables or disables the IQ stream for that channel. | Off | Off, On | `DaxIqEnabled1` – `DaxIqEnabled4` |
| Level meter (IQ 1–4) | Displays the RMS level of the active IQ stream, scaled 0–100. | 0 | 0–100 | — |

## Tips

- The rate combo box is kept in sync with the radio. If the radio reports a different rate after the stream is established, the combo box updates automatically to match.
- Your selected rate is saved across sessions. When AetherSDR reconnects to the radio, it restores the rate you last chose for each channel.
- Higher sample rates capture more bandwidth but increase CPU and network load between the radio and the computer.

## Troubleshooting

- **The rate combo box snaps back to a different value after I change it** — The radio reported a different sample rate for that active stream. The combo box syncs to the radio-reported value when a stream is active. Disable the stream using the **Off/On** button, change the rate, then re-enable the stream.
- **The rate combo box is present but changes have no visible effect** — The stream for that channel may not be enabled. Click the **Off** button to toggle it to **On** so the radio opens the stream at the selected rate.

## Related

- [Enable an IQ stream for external SDR software](enable-an-iq-stream-for-external-sdr-software.md)
- [Disable an IQ stream to free bandwidth](disable-an-iq-stream-to-free-bandwidth.md)
- [Monitor the RMS level of each IQ stream](monitor-the-rms-level-of-each-iq-stream.md)
- [DAX IQ overview](overview.md)
