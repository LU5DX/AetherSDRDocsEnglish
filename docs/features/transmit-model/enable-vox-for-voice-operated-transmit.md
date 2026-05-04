# Enable VOX for voice-operated transmit

The Transmit Model controls VOX (voice-operated transmit), which keys the radio automatically when your microphone audio exceeds a set threshold. Use these controls to enable VOX and tune its hang time to suit your operating style.

## Steps

1. In the TX panel, click the **VOX** toggle button to turn it on. The button activates and the Phone panel refreshes immediately.
2. Adjust the **Delay:** slider to set how long the radio stays in transmit after your audio drops below the threshold. The default is 50 (1000 ms); slide left for a shorter hang time or right for a longer one.

## What each control does

| Control | Behavior |
|---|---|
| **VOX** | Enables voice-operated transmit. The radio keys TX automatically when audio exceeds the VOX level threshold. Default: off. |
| **Delay:** | Sets the VOX hang time before the radio returns to receive after audio drops below threshold. Range: 0–100 (actual milliseconds = value × 20). Default: 50 (1000 ms). |

## Tips

- If the radio drops back to receive too quickly between words, increase **Delay:** to give yourself more time between syllables.
- If you also want to suppress background noise during speech pauses, enable **DEXP** (downward expander) in the same TX panel. Note: DEXP commands return error 0x5000002D on firmware v1.4.0.0.
- VOX and **MOX** are independent — you can switch to manual transmit at any time by clicking **MOX** without disabling VOX.

## Related

- [transmit-settings.md](transmit-settings.md)
- [dexp-noise-gate.md](dexp-noise-gate.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
