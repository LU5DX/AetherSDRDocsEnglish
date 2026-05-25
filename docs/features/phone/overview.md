# Phone overview

The Phone applet provides voice TX controls for AM, VOX, noise gating, and TX audio filtering. Use it to configure how AetherSDR handles your transmitted audio before it reaches the FLEX-8600.

## Before you start

- Connect to a FLEX-8600 radio. The Phone applet requires an active radio connection.
- Open the Applet Panel if it is not already visible. Use `View > Applet Panel` to show it, then click the **PHNE** tray button to display the Phone applet.

## How it works

The Phone applet is organized into four functional areas:

**AM carrier level** sets the carrier power for AM transmit mode. The **AM Carrier** slider runs 0–100 and displays its current value as a percentage label (e.g., "48%") to the right of the slider.

**VOX (voice-operated transmit)** has three controls. The **VOX** toggle button enables or disables VOX. When VOX is on, the **VOX level** slider (0–100) sets the audio threshold that triggers transmit, displayed as a percentage label. The **Delay** slider (0–100) sets the hang time — how long the radio stays in transmit after your voice drops below the threshold before returning to receive.

**DEXP (downward expander)** is a noise gate intended to suppress background noise during transmit pauses. The **DEXP** toggle button enables or disables it, persisted as `DexpEnabled`. The **DEXP threshold** slider (0–100, default 0) sets the gate threshold, displayed as a percentage label, persisted as `DexpLevel`. **Note:** Both DEXP controls are non-functional on firmware v1.4.0.0 — the radio returns error 0x5000002D. The controls are present in the UI but have no effect until a firmware update resolves the issue.

**TX audio filter** shapes the transmitted audio passband. **Low Cut** adjusts the low-frequency cutoff of the TX filter (default 50 Hz, range 0 Hz up to 50 Hz below the current high-cut value, in 50 Hz steps). **High Cut** adjusts the high-frequency cutoff (default 3300 Hz, range 50 Hz above the current low-cut value up to 10000 Hz, in 50 Hz steps). Use the **<** and **>** buttons on each control or the mouse wheel to step the value.

Each step snaps to the nearest multiple of 50 Hz in the chosen direction rather than adding or subtracting 50 Hz from the current value. For example, if the current low-cut value is 87 Hz, pressing **>** moves it to 100 Hz and pressing **<** moves it to 50 Hz. This means a single button press will correct a non-multiple-of-50 value to the grid before continuing to step along it.

## What each control does

| Control        | Kind          | Default  |
|----------------|---------------|----------|
| AM Carrier     | Slider        | —        |
| VOX            | Toggle button | —        |
| VOX level      | Slider        | —        |
| Delay          | Slider        | —        |
| DEXP           | Toggle button | —        |
| DEXP threshold | Slider        | 0        |
| Low Cut < / >  | Spinbox       | 50 Hz    |
| High Cut < / > | Spinbox       | 3300 Hz  |

## Tips

- The **AM Carrier**, **VOX level**, and **DEXP threshold** sliders display their current value as a percentage label (e.g., "48%" for AM Carrier, "70%" for VOX level, "30%" for DEXP threshold) to the right of the slider.
- The **DEXP** and **DEXP threshold** controls persist their values locally via `DexpEnabled` and `DexpLevel` even though the radio rejects the commands on firmware v1.4.0.0. The saved values will apply automatically if a future firmware version resolves the error.
- You can adjust **Low Cut** and **High Cut** with the mouse wheel when hovering over the value display, in addition to using the **<** and **>** buttons.
- Because the **<** and **>** buttons snap to the 50 Hz grid, pressing a button once from an off-grid value corrects to the grid rather than moving a full step beyond it. This is expected behavior.

## Troubleshooting

- **DEXP toggle has no effect** — Firmware v1.4.0.0 returns error 0x5000002D for DEXP commands. This is a known firmware limitation. No workaround is available at this time.

## Related

- [Adjust AM carrier power for AM transmit](adjust-am-carrier-power-for-am-transmit.md)
- [Enable VOX and set trigger threshold](enable-vox-and-set-trigger-threshold.md)
- [Tune VOX hang time](tune-vox-hang-time.md)
- [Set the TX audio low-cut frequency](set-the-tx-audio-low-cut-frequency.md)
- [Set the TX audio high-cut frequency](set-the-tx-audio-high-cut-frequency.md)