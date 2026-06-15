# DAX IQ Applet

## Purpose

The DAX IQ applet provides per-channel DAX IQ stream controls: enable/disable each of four IQ streams, select a sample rate, and monitor real-time level. The applet is available when connected to a FLEX-8600 radio.

## Accessing the DAX IQ Applet

1. Launch AetherSDR and connect to your FLEX-8600 radio.
2. Click the **IQ** tray button to open the DAX IQ applet.
3. Use the controls below to manage individual IQ streams.

## Controls

| Control | Label | Default | Valid Range | Notes |
|---------|-------|---------|-------------|-------|
| Toggle button | IQ 1–4 **On**/**Off** | **Off** | - | Click to enable or disable the IQ stream. Button text and style switch between "Off" and "On". Streams are per-session and not persisted by the radio. |
| Combo box | IQ 1–4 rate | **48k** | 24k (24000), 48k (48000), 96k (96000), 192k (192000) | Select the sample rate for the IQ stream. Changing the rate emits `iqRateChanged(channel, rate)`. The combo box syncs back to the radio-reported rate when a stream is active. |
| Meter | IQ 1–4 meter | 0 | 0–100 (scaled from RMS × 200) | Shows the RMS level of the IQ stream. Resets to 0 on disconnect, disable, or when the stream is not bound to a panadapter. |

## Behavior Details

### Enabling/Disabling IQ Streams

- Click the toggle button to switch a stream **On** or **Off**.
- When enabling, the applet applies the currently selected sample rate to the radio stream. If you changed the rate while the stream was off, that rate is used when enabling.
- When disabling, the meter resets to 0 and the button shows **Off**.

### Sample Rate Selection

- The combo box holds your intended rate. When a stream is active and not rate-settling, the combo box syncs to the radio-reported rate.
- During rate-settling (when the radio is applying a new rate), the combo box preserves your selection until the stream rate stabilizes.
- When a stream is disabled, the combo box retains the rate you selected, ready for the next enable.

### Meter Behavior

- The meter shows the RMS level of the IQ stream only when the stream is actively bound to a panadapter.
- If the stream is off, or if it is enabled but not bound to a panadapter (pan address is `0x0` or empty), the meter shows 0.
- This prevents the meter from freezing at the last value when a stream loses its panadapter binding.

## Visual Changes

The DAX IQ applet uses theme-aware styling. Meter progress bar backgrounds and chunks adapt to the current theme for consistent appearance across light and dark themes.

## Platform-Specific Notes

- **Windows and Linux (PulseAudio only, without PipeWire):** Starting with AetherSDR v26.5.1, the DAX IQ audio setup path properly initializes on these platforms. If you previously had IQ streams enabled with no output, toggle the affected channel(s) **Off** then **On** again.
- **Linux with PipeWire:** No special action required. The DAX IQ applet works natively.

## Persistence

IQ stream enable/disable state is persisted per-session in application settings. On reconnection to the radio, the applet restores the state of previously enabled channels after a short delay (approximately 1.5 seconds) to allow session and stream setup to complete.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| **No audio output on Windows or PulseAudio-only Linux after upgrade** | Toggle the affected IQ channel **Off**, then **On** again. This triggers the corrected setup path. |
| **Still no output after toggling** | Verify your external SDR software (e.g., HDSDR, SDR Console) is configured to receive audio from the correct DAX IQ device. |
| **Meter shows no activity** | Ensure the stream is set to **On**, the selected sample rate matches your external software, and the stream is bound to a panadapter. |
| **Stream does not restore after reconnecting** | Make sure the stream was enabled (set to **On**) before disconnecting. The applet only restores channels that were explicitly enabled. |

## Related

- [DAX IQ overview](overview.md)
- [Enable an IQ stream for external SDR software](enable-an-iq-stream-for-external-sdr-software.md)
- [Pick the IQ sample rate (24k/48k/96k/192k)](pick-the-iq-sample-rate-24k-48k-96k-192k.md)