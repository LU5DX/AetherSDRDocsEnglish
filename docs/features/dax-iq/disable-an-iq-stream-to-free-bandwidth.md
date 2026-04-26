# Disable an IQ stream to free bandwidth

Each active DAX IQ stream consumes bandwidth between AetherSDR and the radio. Disabling a stream you are not using releases that capacity for other tasks.

## Before you start

- AetherSDR must be connected to the radio. The DAX IQ applet requires an active radio connection.
- Open the DAX IQ applet by clicking the IQ tray button on the right sidebar. The applet is hidden by default.

## Steps

1. Locate the channel row you want to stop — IQ 1, IQ 2, IQ 3, or IQ 4.
2. Check that the toggle button for that row reads "On". If it already reads "Off", the stream is already inactive.
3. Click the "On" button. The button label changes to "Off", the button style dims, and the level meter resets to 0.

The radio tears down the stream immediately. The change is saved so that the stream does not re-enable automatically on the next connection.

## What each control does

| Control | Default | Valid values | Persisted setting key |
|---|---|---|---|
| IQ 1–4 Off/On | Off | Off, On | `DaxIqEnabled1` – `DaxIqEnabled4` |
| IQ 1–4 rate | 48k | 24k, 48k, 96k, 192k | `DaxIqRate1` – `DaxIqRate4` |
| IQ 1–4 meter | 0 | 0–100 (RMS × 200) | — |

## Tips

- The meter resets to 0 as soon as a stream is disabled. A non-zero meter reading confirms a stream is still active before you disable it.
- IQ streams are per-session on the radio side, but AetherSDR persists your On/Off choice. After reconnecting, any channel whose setting key is `"True"` will be re-enabled automatically after a short delay once the session is ready. Setting a channel to "Off" prevents that auto-restart.
- If you only need to reduce the data rate rather than stop the stream entirely, lower the rate combo to 24k instead of disabling the stream.

## Troubleshooting

- **Button returns to "On" shortly after you click "Off"** — Another application may be requesting the stream, or you reconnected to the radio while the persisted setting was still `"True"`. Click "Off" again; the setting will be saved as `"False"` and the stream will not restart on the next connection.
- **Meter stays at a non-zero value after disabling** — A brief delay between the disable request and the radio acknowledging it is normal. The meter resets to 0 once the radio confirms the stream is torn down.

## Related

- [Enable an IQ stream for external SDR software](enable-an-iq-stream-for-external-sdr-software.md)
- [Pick the IQ sample rate (24k/48k/96k/192k)](pick-the-iq-sample-rate-24k-48k-96k-192k.md)
- [Monitor the RMS level of each IQ stream](monitor-the-rms-level-of-each-iq-stream.md)
