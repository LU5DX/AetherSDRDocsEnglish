# DAX IQ overview

The DAX IQ applet lets you enable up to four independent IQ data streams from the FLEX-8600, set the sample rate for each, and monitor the real-time signal level. Use these streams to feed external SDR software with raw IQ data from the radio.

## Before you start

- AetherSDR must be connected to the radio. The DAX IQ applet requires an active radio connection.
- The applet is hidden by default. Click the **IQ** tray button on the right sidebar to show it.

## How it works

The FLEX-8600 supports four simultaneous DAX IQ channels. Each channel is independent: you can run them at different sample rates, enable only the ones you need, and monitor each one's signal level separately.

IQ streams are per-session. The radio does not persist stream state across connections. When AetherSDR reconnects, it waits for the radio session to settle, then re-enables any channels that were marked enabled when you last disconnected. Each channel's last-used sample rate is saved locally and restored on the next session.

When a stream is active, the rate combo box syncs to the rate reported by the radio, which may differ from the locally saved value if the radio rejects the requested rate.

Meters reset to zero when a stream is disabled or the radio disconnects.

## What each control does

Each of the four rows (labeled **IQ 1:** through **IQ 4:**) contains three controls:

| Control | What it does | Default | Valid values | Persisted key |
|---|---|---|---|---|
| Rate combo box | Sets the IQ sample rate for that channel. | `48k` | `24k` (24000), `48k` (48000), `96k` (96000), `192k` (192000) | `DaxIqRate1` – `DaxIqRate4` |
| Level meter | Displays the RMS level of the IQ stream, scaled 0–100. | 0 | 0–100 | — |
| **Off** / **On** toggle | Enables or disables the IQ stream for that channel. | **Off** | **Off**, **On** | `DaxIqEnabled1` – `DaxIqEnabled4` |

The toggle button label switches between **Off** and **On** to reflect the current stream state. The radio confirms stream creation or removal; if the radio rejects the request, the button state updates to match the radio-reported state.

## Tips

- Enabling a channel at a higher sample rate (96k or 192k) increases network and CPU load. Enable only the channels you are actively using.
- If you close AetherSDR with a channel marked **On**, it will be re-enabled automatically about 1.5 seconds after the next successful connection.
- To prevent a channel from re-enabling on reconnect, click its toggle to **Off** before disconnecting.

## Troubleshooting

- **Toggle shows "On" but resets to "Off" immediately after connecting** — The radio rejected the stream request. This can happen if the session has not fully initialized. AetherSDR waits 1.5 seconds after connect before re-enabling streams; if the radio is still busy, try toggling the channel manually after a few more seconds.
- **Rate combo shows a different value than selected** — The radio has overridden the requested rate. The combo syncs back to the radio-reported rate when a stream is active. Select the rate again if needed.
- **Meter stays at zero with the stream enabled** — No IQ data is flowing. Confirm your receiving application has opened the IQ stream on the correct channel number.

## Related

- [Enable an IQ stream for external SDR software](enable-an-iq-stream-for-external-sdr-software.md)
- [Pick the IQ sample rate (24k/48k/96k/192k)](pick-the-iq-sample-rate-24k-48k-96k-192k.md)
- [Monitor the RMS level of each IQ stream](monitor-the-rms-level-of-each-iq-stream.md)
- [Disable an IQ stream to free bandwidth](disable-an-iq-stream-to-free-bandwidth.md)
