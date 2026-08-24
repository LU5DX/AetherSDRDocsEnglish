# Phone overview

The Phone applet provides voice TX controls for AM, VOX, noise gating, and TX audio filtering. Use it to configure how AetherSDR handles your transmitted audio before it reaches the FLEX-8600.

## Before you start

- Connect to a FLEX-8600 radio. The Phone applet requires an active radio connection.
- Open the Applet Panel if it is not already visible. Use `View > Applet Panel` to show it, then click the **PHNE** tray button to display the Phone applet.

## How it works

The Phone applet is organized into four functional areas:

**AM carrier level** sets the carrier power for AM transmit mode. The **AM Carrier** slider runs 0–100 and displays its current value as a percentage label (e.g., "48") to the right of the slider.

**VOX (voice-operated transmit)** has three controls. The **VOX** toggle button enables or disables VOX. When VOX is on, the **VOX level** slider (0–100) sets the audio threshold that triggers transmit, displayed as a percentage label. The **Delay** slider (0–100) sets the hang time — how long the radio stays in transmit after your voice drops below the threshold before returning to receive.

**DEXP (downward expander / noise gate)** suppresses background noise during transmit pauses. The **DEXP** toggle button enables or disables it. The **DEXP threshold** slider (0–100, default 0) sets the gate threshold, displayed as a percentage label. DEXP commands are sent directly to the radio; no local persistence is used. Note that DEXP is non-functional on firmware v1.4.0.0 — the radio returns error 0x5000002D when a DEXP command is issued.

**TX audio filter** shapes the transmitted audio passband. **Low Cut** adjusts the low-frequency cutoff of the TX filter (default 50 Hz, range 0 Hz up to 50 Hz below the current high-cut value, in 50 Hz steps). **High Cut** adjusts the high-frequency cutoff (default 3300 Hz, range 50 Hz above the current low-cut value up to 10000 Hz, in 50 Hz steps). Use the **<** and **>** buttons on each control or the mouse wheel to step the value.

Each step snaps to the nearest multiple of 50 Hz in the chosen direction rather than adding or subtracting 50 Hz from the current value. For example, if the current low-cut value is 87 Hz, pressing **>** moves it to 100 Hz and pressing **<** moves it to 50 Hz. This means a single button press will correct a non-multiple-of-50 value to the grid before continuing to step along it. When the radio publishes an explicit edge list for the filter steps, the step buttons honor that list instead.

## What each control does

| Control        | Kind                                                                                                                                | Default                                                     |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| AM Carrier     | Slider — sets AM carrier power level, 0–100.                                                                                        | —                                                           |
| VOX            | Toggle button — enables or disables voice-operated transmit.                                                                        | —                                                           |
| VOX level      | Slider — sets VOX activation threshold, 0–100.                                                                                      | —                                                           |
| Delay          | Slider — sets VOX hang time before returning to receive, 0–100.                                                                     | —                                                           |
| DEXP           | Toggle button — enables or disables downward expander (noise gate).                                                                 | —                                                           |
| DEXP threshold | Slider — sets DEXP gate threshold, 0–100.                                                                                           | 0                                                           |
| Low Cut < / >  | Text field — < / > or mousewheel adjusts the TX filter low-cut by 50 Hz (or along the radio's published step grid). | 50 Hz                                                      |
| High Cut < / > | Text field — < / > or mousewheel adjusts the TX filter high-cut by 50 Hz (or along the radio's published step grid). | 3300 Hz                                                    |

### Direct numeric entry

Double-click the **Low Cut** or **High Cut** value to open an editable text field and type an exact Hz value. The field accepts any integer within the bounds the radio reports for that filter edge.

- A typed value is treated as a request for that exact value, not a step. If you type an out-of-range value, it is rejected and the previous value is restored — the field never clamps a typed number.
- Step buttons, by contrast, always clamp at the range boundary, because a step is a request to move by one increment and stopping at the bound is the only sensible result.
- On radios that publish a discrete step grid, a typed value must be on that grid; off-grid entries are rejected. On radios that accept continuous Hz values, any integer within range is accepted.
- If you type a value that would cross the opposite filter edge (for example, typing a low cut above the current high cut), the entry is rejected rather than pushing the other edge out of the way. This keeps the step buttons as the only way to deliberately move a passband edge.

## Tips

- The **AM Carrier**, **VOX level**, and **DEXP threshold** sliders display their current value as a numeric label (e.g., "48" for AM Carrier, "70" for VOX level, "30" for DEXP threshold) to the right of the slider.
- You can adjust **Low Cut** and **High Cut** with the mouse wheel when hovering over the value display, in addition to using the **<** and **>** buttons.
- Because the **<** and **>** buttons snap to the 50 Hz grid, pressing a button once from an off-grid value corrects to the grid rather than moving a full step beyond it. This is expected behavior.
- Direct numeric entry is the way to request an exact filter frequency. The step buttons snap to the grid, so they may land on a slightly different value than the one you intended to request.
- The Phone applet now respects the active theme for its colors. Slider and button styling follows the primary and accent colors defined in your chosen theme. AM Carrier slider tracks and VOX level, Delay, and VOX level sliders all use the primary accent color for their handles.

## Related

- [Adjust AM carrier power for AM transmit](adjust-am-carrier-power-for-am-transmit.md)
- [Enable VOX and set trigger threshold](enable-vox-and-set-trigger-threshold.md)
- [Tune VOX hang time](tune-vox-hang-time.md)
- [Set the TX audio low-cut frequency](set-the-tx-audio-low-cut-frequency.md)
- [Set the TX audio high-cut frequency](set-the-tx-audio-high-cut-frequency.md)