# DAX IQ Overview

The DAX IQ applet lets you enable and monitor up to four independent IQ data streams from the FLEX-8600. Use these streams to feed raw IQ samples to external SDR software at a sample rate you choose.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The DAX IQ applet is disabled when no radio connection is present.
- The applet panel must be visible. If it is not, select `View > Applet Panel` to show it.

## How it works

The FLEX-8600 supports four simultaneous DAX IQ channels. Each channel is an independent stream of complex (I and Q) samples that external software can consume via the DAX interface. Streams are per-session: the radio does not persist them across disconnects. When AetherSDR reconnects, it waits for the session to stabilize and then re-enables any channels you had previously turned on.

To open the DAX IQ applet, click the **IQ** tray button on the right sidebar. The applet is hidden by default.

Each of the four channels — labeled **IQ 1** through **IQ 4** — has three controls on a single row:

- A rate selector to set the sample rate for that channel.
- A level meter showing the current RMS output of the stream.
- A toggle button to enable or disable the stream.

The rate combo syncs back to the radio-reported rate whenever a stream is active, so the displayed value always reflects what the radio is actually using.

When AetherSDR disconnects from the radio, all toggle buttons reset to **Off** and all meters reset to 0.

## What each control does

| Control | Description | Default | Valid values | Persisted key |
|---|---|---|---|---|
| IQ 1–4 rate | Sets the sample rate for the channel. | `48k` | `24k` (24000), `48k` (48000), `96k` (96000), `192k` (192000) | `DaxIqRate1` – `DaxIqRate4` |
| IQ 1–4 meter | Displays the RMS level of the stream, scaled 0–100. Resets to 0 on disconnect or when the stream is disabled. | 0 | 0–100 | — |
| IQ 1–4 Off/On | Toggles the IQ stream on or off. Shows **Off** when inactive, **On** when active. | Off | Off / On | `DaxIqEnabled1` – `DaxIqEnabled4` |

## Tips

- The rate combo and enable state for each channel are persisted locally. On reconnect, AetherSDR restores previously enabled channels automatically after a short delay to allow the radio session to finish setting up.
- Scrolling the applet panel will not accidentally change rate combos or other controls; the panel's controls lock while you scroll.

## Related

- [Enable an IQ stream for external SDR software](enable-an-iq-stream-for-external-sdr-software.md)
- [Pick the IQ sample rate (24k/48k/96k/192k)](pick-the-iq-sample-rate-24k-48k-96k-192k.md)
- [Monitor the RMS level of each IQ stream](monitor-the-rms-level-of-each-iq-stream.md)
- [Disable an IQ stream to free bandwidth](disable-an-iq-stream-to-free-bandwidth.md)
