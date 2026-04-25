# Disable an IQ stream to free bandwidth

Each active IQ stream consumes radio bandwidth and processing resources. Use this procedure to turn off a stream you no longer need.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- The DAX IQ applet must be visible. If it is not, click the **IQ** tray button on the right sidebar to show it.
- Identify which channel (IQ 1–4) you want to disable by checking which toggle button shows **On**.

## Steps

1. Locate the row for the channel you want to disable (IQ 1, IQ 2, IQ 3, or IQ 4).
2. Click the **On** button at the right end of that row.
3. The button label changes to **Off**, the button style dims, and the level meter resets to 0.

The stream is now torn down on the radio. The radio does not persist stream state between sessions; AetherSDR records your choice in `DaxIqEnabled1` through `DaxIqEnabled4` so it can restore the same state when you reconnect.

## What each control does

| Control | Default | Behavior |
|---|---|---|
| **IQ 1..4 Off/On** (toggle button) | Off | Clicking while **On** emits a disable request to the radio, resets the label to **Off**, and clears the level meter. |
| **IQ 1..4 meter** (level meter) | 0 | Displays the RMS level of the stream (0–100). Resets to 0 when the stream is disabled or the radio disconnects. |
| **IQ 1..4 rate** (combo box) | 48k | Selects sample rate: 24k, 48k, 96k, or 192k. Syncs back to the radio-reported rate while a stream is active. Persisted per channel in `DaxIqRate1` through `DaxIqRate4`. |

## Tips

- Disabling a stream does not change its saved sample rate. The rate you had selected will still be set when you re-enable the stream.
- If you disconnect and reconnect, AetherSDR waits briefly before re-enabling any streams that were active. If you want a stream to stay off after reconnect, ensure its button shows **Off** before disconnecting — the `DaxIqEnabled1`–`DaxIqEnabled4` settings control which streams are restored.
- Disabling unused streams before changing sample rates on active streams reduces the chance of the radio rejecting the rate change.

## Troubleshooting

- **Button shows Off but the external SDR application still reports a stream** — The radio-side stream may not have been removed yet. Disconnect and reconnect to the radio to force a clean session state.
- **Button reverts to On immediately after clicking Off** — The radio rejected the disable request. Check your network connection and verify no other SmartSDR client has locked the stream.

## Related

- [Enable an IQ stream for external SDR software](enable-an-iq-stream-for-external-sdr-software.md)
- [Pick the IQ sample rate (24k/48k/96k/192k)](pick-the-iq-sample-rate-24k-48k-96k-192k.md)
- [Monitor the RMS level of each IQ stream](monitor-the-rms-level-of-each-iq-stream.md)
- [DAX IQ overview](overview.md)
