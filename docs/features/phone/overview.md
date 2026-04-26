# Phone overview

The Phone applet provides controls for voice transmit on the FLEX-8600: AM carrier level, voice-operated transmit (VOX), a downward expander noise gate (DEXP), and TX audio filter edge frequencies. Open it when you need to adjust how AetherSDR handles your transmitted audio.

## Before you start

- Connect to a FLEX-8600 radio. The Phone applet requires an active radio connection.
- The applet panel must be visible. If it is not, click `View > Applet Panel` to show it.

## How it works

The Phone applet is always present in the Applet Panel (right sidebar). Toggle its visibility with the `PHNE` tray button on the right sidebar.

The applet is organized into four functional areas:

**AM Carrier** sets the carrier power level used during AM transmit. The current value is shown as a number to the right of the slider.

**VOX** enables voice-operated transmit. When VOX is active, audio above the VOX level threshold keys the transmitter. The VOX level slider sets that threshold, and the Delay slider controls how long the radio stays in transmit after audio drops below the threshold (hang time).

**DEXP** is a downward expander that acts as a noise gate on the transmitted audio. The DEXP threshold slider sets the gate threshold. Both `DEXP` and `DEXP threshold` persist their values locally in AetherSDR settings. **Note:** Due to a firmware limitation in v1.4.0.0, the DEXP controls are non-functional — the radio returns an error when these commands are sent. The controls are present in the UI but have no effect on the radio until this is resolved.

**TX filter** sets the low-cut and high-cut edges of the transmitted audio passband. Use the `<` and `>` buttons on either side of the displayed frequency value, or scroll the mousewheel over the value, to step each edge in 50 Hz increments.

## What each control does

| Control | Kind | Default | Valid range | Persisted key |
|---|---|---|---|---|
| AM Carrier | Slider | — | 0–100 | — |
| VOX | Toggle button | — | On / Off | — |
| VOX level | Slider | — | 0–100 | — |
| Delay | Slider | — | 0–100 | — |
| DEXP | Toggle button | — | On / Off | `DexpEnabled` |
| DEXP threshold | Slider | 0 | 0–100 | `DexpLevel` |
| Low Cut `<` / `>` | Spinbox | 50 Hz | 0 Hz to (high cut − 50 Hz), step 50 Hz | — |
| High Cut `<` / `>` | Spinbox | 3300 Hz | (low cut + 50 Hz) to 10000 Hz, step 50 Hz | — |

## Tips

- The `DexpEnabled` and `DexpLevel` values are saved to AetherSDR's local settings even though the radio rejects the DEXP commands on firmware v1.4.0.0. Your settings will be preserved for when firmware support is added.
- The Delay slider controls VOX hang time only — it has no effect unless VOX is enabled.
- Low Cut and High Cut are linked: Low Cut cannot be set higher than (High Cut − 50 Hz), and High Cut cannot be set lower than (Low Cut + 50 Hz).

## Troubleshooting

- **DEXP toggle or threshold has no audible effect** — The radio firmware v1.4.0.0 does not support the DEXP protocol command and returns an error. The controls are visible but non-functional. No workaround is available at this firmware version.

## Related

- [Adjust AM carrier power for AM transmit](adjust-am-carrier-power-for-am-transmit.md)
- [Enable VOX and set trigger threshold](enable-vox-and-set-trigger-threshold.md)
- [Tune VOX hang time](tune-vox-hang-time.md)
- [Set the TX audio low-cut frequency](set-the-tx-audio-low-cut-frequency.md)
- [Set the TX audio high-cut frequency](set-the-tx-audio-high-cut-frequency.md)
