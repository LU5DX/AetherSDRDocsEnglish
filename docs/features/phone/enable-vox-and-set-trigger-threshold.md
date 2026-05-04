# Phone Applet

The Phone applet provides voice TX controls for AM carrier level, VOX, DEXP noise gate, and TX filter cut-off frequencies. This page describes every control in the applet and how to use them.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. All Phone applet controls are inactive without a radio connection.
- The Phone applet must be visible in the Applet Panel. If it is not, click the PHNE tray button on the right sidebar.

## Opening the Phone applet

Click the PHNE tray button on the right sidebar. The Phone applet opens in the Applet Panel.

## What each control does

| Control | Kind | What it does |
|---|---|---|
| AM Carrier | Slider (0–100) | Sets the AM carrier power level. The current value is shown as a number next to the slider (for example, `48`). |
| VOX | Toggle button | Toggles voice-operated transmit. The button lights green when active. |
| VOX level | Slider (0–100) | Sets the audio threshold required to activate transmit. Move right to require a stronger signal; move left to key on quieter audio. |
| Delay | Slider (0–100) | Sets the VOX hang time before the radio returns to receive after audio drops below the threshold. |
| DEXP | Toggle button | Toggles the downward expander (noise gate). Persists to `DexpEnabled`. |
| DEXP threshold | Slider (0–100, default 0) | Sets the DEXP gate threshold. Persists to `DexpLevel`. |
| Low Cut < / > | < / > or mousewheel snaps TX filter low-cut to the next 50 Hz multiple in the chosen direction (e.g. at 87 Hz: up → 100, down → 50). | Snaps to multiples of 50 Hz rather than stepping by a fixed amount, so odd radio-reported values realign cleanly. |
| High Cut < / > | < / > or mousewheel snaps TX filter high-cut to the next 50 Hz multiple in the chosen direction (max 10000 Hz). | Same snap-to-multiple logic as Low Cut. |
## Enable VOX and set the trigger threshold

1. Open the Phone applet by clicking the PHNE tray button on the right sidebar.
2. Click **VOX** to enable voice-operated transmit. The button lights green when active.
3. Adjust the **VOX level** slider to set the activation threshold. Move it right to require a stronger audio signal before the radio keys; move it left to key on quieter audio. Valid range: 0–100.
4. Adjust the **Delay** slider to set how long the radio stays in transmit after audio drops below the threshold before returning to receive.

## Enable DEXP

> **Note:** DEXP is non-functional on firmware v1.4.0.0. The radio returns error `0x5000002D` when this feature is used on that firmware version.

1. Open the Phone applet.
2. Click **DEXP** to enable the downward expander noise gate.
3. Adjust the **DEXP threshold** slider to set the gate threshold. The value is stored in `DexpLevel` and persists across sessions.

## Set TX filter cut-off frequencies

Use **Low Cut < / >** and **High Cut < / >** to shape the transmitted audio bandwidth.

- Click `<` to decrease the value, click `>` to increase it. The mouse wheel also adjusts the value.
- The default low-cut is 50 Hz. The default high-cut is 3300 Hz.

### Filter cut stepping

From v0.9.5.1, the `<` and `>` buttons snap to the nearest multiple of 50 Hz in the chosen direction rather than adding or subtracting a fixed 50 Hz from the current value.

**Example:** If the low-cut is currently 87 Hz:
- Pressing `>` (increase) snaps to **100 Hz** (next multiple of 50 above 87).
- Pressing `<` (decrease) snaps to **50 Hz** (next multiple of 50 below 87).

This means the value always lands on a clean 50 Hz boundary regardless of its starting point. The radio accepts any integer Hz value; this is a UI convenience only.

## Tips

- If the radio keys up on background noise, increase the **VOX level** slider value so a stronger signal is required to trigger transmit.
- If VOX drops out mid-syllable, increase the **Delay** slider to extend the hang time.
- If DEXP is enabled and the noise gate is cutting your audio, lower the **DEXP threshold** slider value.

## Troubleshooting

- **Radio does not key when you speak** — VOX level may be set too high. Lower the **VOX level** slider so quieter audio triggers transmit.
- **Radio stays in transmit too long after you stop speaking** — Decrease the **Delay** slider to shorten the hang time.
- **DEXP toggle has no effect** — This is a known firmware limitation on v1.4.0.0. The radio returns error `0x5000002D`. No workaround is available at the firmware level.

## Related

- [Tune VOX hang time](tune-vox-hang-time.md)
- [Phone overview](overview.md)