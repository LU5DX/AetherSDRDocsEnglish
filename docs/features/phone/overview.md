# Phone overview

The Phone applet groups all voice transmit controls in one place: AM carrier level, VOX, a downward expander noise gate (DEXP), and TX audio filter cutoffs. Open it whenever you need to adjust how your transmitted audio is shaped or when you want to configure voice-operated transmit.

## Before you start

- AetherSDR must be connected to the radio. The Phone applet requires an active radio connection.
- The applet is visible in the Applet Panel (right sidebar). If the panel is hidden, click the PHNE tray button on the right sidebar, or enable it via `View > Applet Panel`.

## How it works

The Phone applet is always present in the Applet Panel. Toggle its visibility with the PHNE tray button. Controls are sent directly to the radio in real time; the applet reflects current radio state when a connection is active.

**DEXP limitation:** The DEXP toggle and DEXP threshold slider are present in the UI, but on firmware v1.4.0.0 (SmartSDR protocol v1.4.0.0), the radio returns an error when these commands are sent. DEXP settings (`DexpEnabled`, `DexpLevel`) are persisted locally by AetherSDR but do not take effect on the radio until this firmware limitation is resolved.

## What each control does

| Control | Kind | Default | Valid range | Persisted key | What it does |
|---|---|---|---|---|---|
| AM Carrier | Slider | — | 0–100 | — | Sets the AM carrier power level. The current value appears as a number to the right of the slider (e.g. `48`). |
| VOX | Toggle button | — | On / Off | — | Enables or disables voice-operated transmit. When checked, audio above the VOX level threshold triggers TX. |
| VOX level | Slider | — | 0–100 | — | Sets the VOX activation threshold. Higher values require louder audio to trigger transmit. |
| Delay | Slider | — | 0–100 | — | Sets the VOX hang time — how long the radio stays in TX after audio drops below the threshold before returning to receive. |
| DEXP | Toggle button | — | On / Off | `DexpEnabled` | Toggles the downward expander noise gate. Non-functional on firmware v1.4.0.0. |
| DEXP threshold | Slider | 0 | 0–100 | `DexpLevel` | Sets the DEXP gate threshold. Non-functional on firmware v1.4.0.0. |
| Low Cut `<` / `>` | Spinbox | 50 Hz | 0 to (high cut − 50 Hz), step 50 Hz | — | Adjusts the TX audio filter low-cut frequency. Click `<` or `>`, or use the mouse wheel. |
| High Cut `<` / `>` | Spinbox | 3300 Hz | (low cut + 50 Hz) to 10000 Hz, step 50 Hz | — | Adjusts the TX audio filter high-cut frequency. Click `<` or `>`, or use the mouse wheel. |

## Tips

- The Low Cut and High Cut spinboxes enforce a minimum 50 Hz gap between the two values. Adjusting one limit toward the other will stop at that boundary.
- `DexpEnabled` and `DexpLevel` are saved to AetherSDR's local settings whenever you change them, so your intended values are preserved for when firmware support becomes available.

## Troubleshooting

- **DEXP toggle or threshold has no effect on the radio** — This is a known firmware limitation on v1.4.0.0. The radio returns error 0x5000002D for these commands. Your settings are stored locally but are not applied to the radio.
- **Phone applet is not visible** — Click the PHNE tray button on the right sidebar, or check that `View > Applet Panel` is enabled.

## Related

- [Adjust AM carrier power for AM transmit](adjust-am-carrier-power-for-am-transmit.md)
- [Enable VOX and set trigger threshold](enable-vox-and-set-trigger-threshold.md)
- [Tune VOX hang time](tune-vox-hang-time.md)
- [Set the TX audio low-cut frequency](set-the-tx-audio-low-cut-frequency.md)
- [Set the TX audio high-cut frequency](set-the-tx-audio-high-cut-frequency.md)
