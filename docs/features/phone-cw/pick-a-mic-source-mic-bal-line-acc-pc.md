# Pick a mic source (MIC, BAL, LINE, ACC, PC)

This page explains how to select the microphone input source for the active transmit slice. Use this when you want to switch between a front-panel mic, balanced input, line-level input, accessory connector, or PC audio.

## Before you start

- AetherSDR must be connected to a Flex radio.
- The active slice must be in a voice mode (Phone panel must be visible in the P/CW applet). The mic source controls are not shown when the slice is in CW mode.

## Steps

1. Locate the **P/CW** tray button on the right sidebar and confirm the Phone panel is showing.
2. Find the **Mic source** combo box. It appears to the left of the mic gain slider, directly below the **Mic profile** combo box.
3. Click the **Mic source** combo box and select one of the available sources: `MIC`, `BAL`, `LINE`, `ACC`, or `PC`.
4. The radio switches to the selected input immediately.
5. If you selected `PC`, adjust the **Mic gain** slider to your preferred level. The radio does not report a gain value for the PC source — AetherSDR stores this value locally as `PcMicGain`.

## What each control does

| Control | Kind | Valid values | Default | Setting key | Notes |
|---|---|---|---|---|---|
| **Mic source** | Combo box | `MIC`, `BAL`, `LINE`, `ACC`, `PC` | — | — | Sends the selected source to the radio immediately. Additional sources may appear if the radio reports them. |
| **Mic gain** | Slider | 0–100 | 50 | `PcMicGain` (PC source only) | When source is `PC`, the radio always reports `mic_level=0`; AetherSDR keeps the value client-side using `PcMicGain`. For all other sources the value is stored on the radio. |

## Tips

- The **Level** gauge (−40 to +10 dBFS, red above 0) gives immediate feedback after you change source. Watch it while speaking to confirm signal is arriving from the new input.
- If you also want to mix in the accessory connector alongside another primary source, use the **+ACC** toggle button rather than selecting `ACC` as the sole source.

## Troubleshooting

- **Level gauge shows no movement after selecting a new source** — confirm the physical connection to that input on the radio. The Level gauge is suppressed when the radio is not transmitting and met_in_rx is off; key the radio briefly to verify input.
- **Mic gain slider has no effect when source is PC** — this is expected. The radio ignores the gain value for the PC source; AetherSDR applies the `PcMicGain` value locally. Adjust the slider and the stored value will update.

## Related

- [Adjust mic gain and enable the accessory mix](adjust-mic-gain-and-enable-the-accessory-mix.md)
- [Select a mic profile for a specific microphone](select-a-mic-profile-for-a-specific-microphone.md)
- [Enable speech processor at NOR, DX, or DX+ level](enable-speech-processor-at-nor-dx-or-dx-level.md)
