# Toggle MOX for manual transmit

The **MOX** button lets you key the transmitter manually, independent of VOX or CAT control. Use it when you need direct, on-demand control of the TX state for your connected radio.

## Steps

1. Open the Transmit panel.
2. Click **MOX** to start transmitting. The button turns red immediately while the radio confirms the TX state.
3. Click **MOX** again to return to receive.

## What each control does

| Control | Behavior | Notes |
|---|---|---|
| **MOX** | Toggles manual transmit on or off. Sends `xmit 1` or `xmit 0` to the radio. Default: off. The button turns red immediately before the radio confirms the TX state (optimistic update). |  |
## Tips

- MOX overrides receive regardless of VOX or other keying sources — remember to click it off before walking away from the radio.
- If you also use VOX, disabling **VOX** before pressing **MOX** avoids conflicting keying signals.
- To key the radio for antenna tuning instead, use the **TUNE** button, which manages carrier power separately via the **Tune Pwr:** slider.

## Related

- [transmit-panel.md](transmit-panel.md)
- [tune-antenna.md](tune-antenna.md)
- [enable-vox.md](enable-vox.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
