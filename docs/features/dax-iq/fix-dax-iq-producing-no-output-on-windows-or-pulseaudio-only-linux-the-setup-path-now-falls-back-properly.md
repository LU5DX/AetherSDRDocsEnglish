# Fix DAX IQ producing no output on Windows or PulseAudio-only Linux

Starting with AetherSDR v26.5.1, the DAX IQ audio setup path properly initializes on Windows and Linux systems using PulseAudio only (without PipeWire). Previously, the stream setup would silently return without initializing, resulting in no IQ output on those platforms.

## Before you start

- Ensure you have AetherSDR v26.5.1 or later installed.
- If you are running Linux with **only PulseAudio** (no PipeWire), this fix applies to you automatically.

## Steps

No user action is required. The fix is applied on the application side:

1. Launch AetherSDR and connect to your FLEX-8600 radio.
2. Enable a DAX IQ channel using the `IQ` tray button, then click the toggle button for the desired channel (IQ 1–4) to set it to **On**.
3. If you previously had IQ streams enabled but saw no output, simply toggle the affected channel(s) **Off** then **On** again to trigger the corrected setup path.

## What each control does

| Control | Label | Default | Notes |
|---------|-------|---------|-------|
| Toggle button | IQ 1–4 **On**/**Off** | **Off** | Click to enable or disable the IQ stream. When toggling **On**, the audio setup now correctly falls back to PulseAudio on Windows and Linux without PipeWire. |
| Combo box | IQ 1–4 rate | **48k** | Choose 24k, 48k, 96k, or 192k sample rate. Changing the rate emits `iqRateChanged(channel, rate)`. Syncs back to the radio-reported rate when a stream is active. |
| Meter | IQ 1–4 meter | 0 | Shows the RMS level of the IQ stream, scaled 0-100 (RMS × 200). Resets to 0 on disconnect or disable. |

## Visual changes in v26.6.1

The DAX IQ applet now uses theme-aware styling. Instead of hard-coded colors, the meter progress bar backgrounds and chunks adapt to the current theme. This ensures consistent appearance across light and dark themes.

## Tips

- If DAX IQ still produces no output after upgrading, try restarting AetherSDR completely, then re-enabling the IQ stream.
- The fix only applies at stream setup time — streams that were already enabled before the upgrade may need to be toggled off and on again.

## Troubleshooting

- **No audio output on Windows or PulseAudio-only Linux after upgrade** — Toggle the affected IQ channel **Off**, then **On** again. This triggers the corrected setup path that properly initializes the audio stream.
- **Still no output after toggling** — Verify your external SDR software (e.g., HDSDR, SDR Console) is configured to receive audio from the correct DAX IQ device. The fix addresses the AetherSDR internal setup; your receiver must still be pointed at the right virtual audio device.
- **Meter shows no activity** — Ensure the stream is set to **On** and the selected sample rate matches what your external SDR software expects.

## Related

- [DAX IQ overview](overview.md)
- [Enable an IQ stream for external SDR software](enable-an-iq-stream-for-external-sdr-software.md)
- [Pick the IQ sample rate (24k/48k/96k/192k)](pick-the-iq-sample-rate-24k-48k-96k-192k.md)