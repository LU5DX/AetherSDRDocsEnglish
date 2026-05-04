# Show or hide TX signal in the waterfall during transmit

The Transmit Model controls whether your transmitted signal is visible in the waterfall display while the radio is keyed. Use the MOX toggle to key the radio manually and observe the TX signal overlay in real time.

## Steps

1. Open the TX applet in AetherSDR.
2. Click **MOX** to toggle manual transmit on. The button turns red immediately. The TX signal appears in the waterfall while MOX is active.
3. Click **MOX** again to return to receive. The TX signal overlay disappears from the waterfall.

## What each control does

| Control | Behavior | Notes |
|---|---|---|
| **MOX** | Toggles manual transmit on or off. Sends `xmit 1` or `xmit 0` to the radio. The button turns red immediately before the radio confirms the TX state. While active, the TX signal is visible in the waterfall. |  |
| **RF Power:** | Sets the radio's RF transmit power as a percentage of maximum (0–100). Affects the strength of the TX signal shown in the waterfall. Default: 100. |  |
| **TUNE** | Starts or stops a tune carrier. Label changes to **TUNING...** and turns red while a tune is in progress. The tune carrier is also visible in the waterfall during this time. |  |
## Tips

- The MOX button uses an optimistic update — it turns red before the radio confirms TX state, so the waterfall overlay may appear a moment before the radio is fully keyed.
- If you only want to observe the TX signal briefly, use **TUNE** with a low **Tune Pwr:** setting to minimize RF output while checking waterfall visibility.
- Two-tone tune mode is available via the `two_tone_tune` keyboard shortcut and also shows in the waterfall during the tune cycle.

## Related

- [transmit-model.md](transmit-model.md)
- [waterfall-display.md](waterfall-display.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
