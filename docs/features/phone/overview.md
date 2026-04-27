# Phone overview

The Phone applet provides voice TX controls for AM, VOX, noise gating, and TX audio filtering. Use it to configure how AetherSDR handles your transmitted audio before it reaches the FLEX-8600.

## Before you start

- Connect to a FLEX-8600 radio. The Phone applet requires an active radio connection.
- Open the Applet Panel if it is not already visible. Use `View > Applet Panel` to show it, then click the **PHNE** tray button to display the Phone applet.

## How it works

The Phone applet is organized into four functional areas:

**AM carrier level** sets the carrier power for AM transmit mode. The **AM Carrier** slider runs 0–100 and displays its current value as a number to the right of the slider.

**VOX (voice-operated transmit)** has three controls. The **VOX** toggle button enables or disables VOX. When VOX is on, the **VOX level** slider (0–100) sets the audio threshold that triggers transmit. The **Delay** slider (0–100) sets the hang time — how long the radio stays in transmit after your voice drops below the threshold before returning to receive.

**DEXP (downward expander)** is a noise gate intended to suppress background noise during transmit pauses. The **DEXP** toggle button enables or disables it, persisted as `DexpEnabled`. The **DEXP threshold** slider (0–100, default 0) sets the gate threshold, persisted as `DexpLevel`. **Note:** Both DEXP controls are non-functional on firmware v1.4.0.0 — the radio returns error 0x5000002D. The controls are present in the UI but have no effect until a firmware update resolves the issue.

**TX audio filter** shapes the transmitted audio passband. **Low Cut** adjusts the low-frequency cutoff of the TX filter (default 50 Hz, range 0 Hz up to 50 Hz below the current high-cut value, in 50 Hz steps). **High Cut** adjusts the high-frequency cutoff (default 3300 Hz, range 50 Hz above the current low-cut value up to 10000 Hz, in 50 Hz steps). Use the **<** and **>** buttons on each control or the mouse wheel to step the value.

## What each control does

| Control | Kind | Default | Range | Persisted key |
|---|---|---|---|---|
| AM Carrier | Slider | — | 0–100 | — |
| VOX | Toggle button | — | On/Off | — |
| VOX level | Slider | — | 0–100 | — |
| Delay | Slider | — | 0–100 | — |
| DEXP | Toggle button | — | On/Off | `DexpEnabled` |
| DEXP threshold | Slider | 0 | 0–100 | `DexpLevel` |
| Low Cut < / > | Spinbox | 50 Hz | 0 to (high-cut − 50 Hz), step 50 Hz | — |
| High Cut < / > | Spinbox | 3300 Hz | (low-cut + 50 Hz) to 10000 Hz, step 50 Hz | — |

## Tips

- The **DEXP** and **DEXP threshold** controls persist their values locally via `DexpEnabled` and `DexpLevel` even though the radio rejects the commands on firmware v1.4.0.0. The saved values will apply automatically if a future firmware version resolves the error.
- You can adjust **Low Cut** and **High Cut** with the mouse wheel when hovering over the value display, in addition to using the **<** and **>** buttons.

## Troubleshooting

- **DEXP toggle has no effect** — Firmware v1.4.0.0 returns error 0x5000002D for DEXP commands. This is a known firmware limitation. No workaround is available at this time.

## Related

- [Adjust AM carrier power for AM transmit](adjust-am-carrier-power-for-am-transmit.md)
- [Enable VOX and set trigger threshold](enable-vox-and-set-trigger-threshold.md)
- [Tune VOX hang time](tune-vox-hang-time.md)
- [Set the TX audio low-cut frequency](set-the-tx-audio-low-cut-frequency.md)
- [Set the TX audio high-cut frequency](set-the-tx-audio-high-cut-frequency.md)
