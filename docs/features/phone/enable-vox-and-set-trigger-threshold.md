# Phone Applet

The Phone applet provides voice TX controls for AM carrier level, VOX, DEXP noise gate, and TX filter cut-off frequencies. This page describes every control in the applet and how to use them.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. All Phone applet controls are inactive without a radio connection.
- The Phone applet must be visible in the Applet Panel. If it is not, click the PHNE tray button on the right sidebar.

## Opening the Phone applet

Click the PHNE tray button on the right sidebar. The Phone applet opens in the Applet Panel.

## What each control does

| Control        | Kind                                                                                                                                                                                                                           | What it does                                                                                                                                                                    |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AM Carrier     | Slider (0–100)                                                                                                                                                                                                                 | Sets the AM carrier power level. The current value is shown as a percentage next to the slider (for example, `48%`).                                                            |
| VOX            | Toggle button                                                                                                                                                                                                                  | Toggles voice-operated transmit. The button lights green when active.                                                                                                           |
| VOX level      | Slider (0–100)                                                                                                                                                                                                                 | Sets the audio threshold required to activate transmit. Move right to require a stronger signal; move left to key on quieter audio. The current value is shown as a percentage. |
| Delay          | Slider (0–100)                                                                                                                                                                                                                 | Sets the VOX hang time before the radio returns to receive after audio drops below the threshold.                                                                               |
| DEXP           | Toggle button                                                                                                                                                                                                                  | Toggles the downward expander (noise gate).                                                                                                                                     |
| DEXP threshold | Slider (0–100, default 0)                                                                                                                                                                                                      | Sets the DEXP gate threshold. The current value is shown as a percentage.                                                                                                       |
| Low Cut < / >  | < / > or mousewheel adjusts the TX filter low-cut by 50 Hz. Double-click the value to type an exact Hz value, which is honored on radios that accept it while the radio's own readback is preserved elsewhere (#3627, #5064).  | A typed number is treated as a request for that exact value, whereas the step buttons clamp to the radio's step grid.                                                           |
| High Cut < / > | < / > or mousewheel adjusts the TX filter high-cut by 50 Hz. Double-click the value to type an exact Hz value, which is honored on radios that accept it while the radio's own readback is preserved elsewhere (#3627, #5064). | A typed number is treated as a request for that exact value, whereas the step buttons clamp to the radio's step grid.                                                           |

### TX filter stepping with discrete edges

Some radios report a discrete set of valid filter edge values rather than accepting any integer Hz. When such a radio is connected, the `<` and `>` buttons move to the nearest valid edge in the chosen direction instead of snapping to a 50 Hz multiple. Typed values are likewise rejected if they are not in the radio's reported edge set.

## Enable VOX and set the trigger threshold

1. Open the Phone applet by clicking the PHNE tray button on the right sidebar.
2. Click **VOX** to enable voice-operated transmit. The button lights green when active.
3. Adjust the **VOX level** slider to set the activation threshold. Move it right to require a stronger audio signal before the radio keys; move it left to key on quieter audio. Valid range: 0–100. The current percentage is displayed next to the slider.
4. Adjust the **Delay** slider to set how long the radio stays in transmit after audio drops below the threshold before returning to receive.

## Enable DEXP

1. Open the Phone applet.
2. Click **DEXP** to enable the downward expander noise gate.
3. Adjust the **DEXP threshold** slider to set the gate threshold. The current percentage is displayed next to the slider.

## Set TX filter cut-off frequencies

Use **Low Cut < / >** and **High Cut < / >** to shape the transmitted audio bandwidth.

- Click `<` to decrease the value, click `>` to increase it. The mouse wheel also adjusts the value.
- The default low-cut is 50 Hz. The default high-cut is 3300 Hz.

### Filter cut stepping

The `<` and `>` buttons snap to the nearest valid value in the chosen direction rather than adding or subtracting a fixed 50 Hz from the current value.

**Example (radio accepting any integer Hz):** If the low-cut is currently 87 Hz:
- Pressing `>` (increase) snaps to **100 Hz** (next multiple of 50 above 87).
- Pressing `<` (decrease) snaps to **50 Hz** (next multiple of 50 below 87).

**Example (radio with discrete edges):** If the radio reports valid low-cut edges of 0, 50, 100, 200, and 300 Hz, and the current value is 100 Hz:
- Pressing `>` (increase) moves to **200 Hz**.
- Pressing `<` (decrease) moves to **50 Hz**.

### Typing an exact value

Double-click the low-cut or high-cut value to type an exact Hz number. The value is accepted only if it is within the valid range and, on radios reporting discrete edges, is one of the reported edges. Out-of-range values are rejected with the previous value restored.

## Tips

- If the radio keys up on background noise, increase the **VOX level** slider value so a stronger signal is required to trigger transmit.
- If VOX drops out mid-syllable, increase the **Delay** slider to extend the hang time.
- If DEXP is enabled and the noise gate is cutting your audio, lower the **DEXP threshold** slider value.

## Troubleshooting

- **Radio does not key when you speak** — VOX level may be set too high. Lower the **VOX level** slider so quieter audio triggers transmit.
- **Radio stays in transmit too long after you stop speaking** — Decrease the **Delay** slider to shorten the hang time.
- **Typed filter value is rejected** — The value may be outside the valid range or, on radios reporting discrete edges, not a valid edge for that filter. Use the step buttons to move to a valid value.

## Related

- [Tune VOX hang time](tune-vox-hang-time.md)
- [Phone overview](overview.md)