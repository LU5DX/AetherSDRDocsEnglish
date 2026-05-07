# Enable VOX for voice-operated transmit

The Transmit Model controls all transmit state for the connected radio. VOX lets the radio key TX automatically when your audio exceeds a set threshold, so you do not need to press MOX or a PTT switch.

## Steps

1. In the TX applet, click the **VOX** toggle button to turn it on. The button lights up when VOX is active.
2. Adjust the **Delay:** slider to set how long the radio stays in transmit after your audio drops below the threshold. The default is 50 (1000 ms). Move the slider left for a shorter hang time, right for a longer one.

## What each control does

| Control | Behavior |
|---|---|
| **VOX** | Enables voice-operated transmit. The radio keys TX automatically when audio exceeds the VOX level threshold. Default: off. |
| **Delay:** | Sets the VOX hang time before the radio returns to receive after audio drops below threshold. Range: 0–100 (actual milliseconds = value × 20). Default: 50 (1000 ms). |
| **DEXP** | Enables the downward expander (noise gate) to suppress background noise during pauses in speech. Default: off. |

## Tips

- If the radio keys up on background noise, enable **DEXP** to apply a noise gate and reduce unwanted triggering.
- If the radio drops out of TX too quickly between words, increase the **Delay:** value to extend the hang time.
- VOX applies an optimistic update — the Phone panel refreshes immediately when you toggle **VOX**, before the radio confirms the new state.
- To transmit manually without VOX, use the **MOX** toggle button instead.

## Related

- [transmit-model.md](transmit-model.md)
- [manual-transmit-mox.md](manual-transmit-mox.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
