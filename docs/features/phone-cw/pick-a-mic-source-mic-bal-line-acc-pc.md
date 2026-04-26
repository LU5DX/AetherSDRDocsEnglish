# Pick a mic source (MIC, BAL, LINE, ACC, PC)

This page shows how to select the microphone input source for your FLEX-8600 in AetherSDR. The correct source must match the physical connector you are using before you transmit.

## Before you start

- AetherSDR must be connected to your FLEX-8600.
- The active slice must be in a phone mode (USB, LSB, AM, FM, or similar). The Phone panel is hidden when the active slice is in CW mode.
- Open the Phone/CW applet: click the **P/CW** tray button on the right sidebar if the applet is not already visible.

## Steps

1. Locate the **Mic source** drop-down in the Phone/CW applet. It is a narrow combo box (approximately 55 px wide) on the same row as the **Mic gain** slider and the **+ACC** button.
2. Click the **Mic source** drop-down.
3. Select one of the available sources: `MIC`, `BAL`, `LINE`, `ACC`, or `PC`. The selection is sent to the radio immediately.
4. If you selected `PC`, set the **Mic gain** slider to the desired level (0–100; default 50). The `PC` source keeps its gain value locally in `PcMicGain` because the radio always reports mic level as 0 for this source.
5. Watch the **Level** gauge (−40 to +10 dBFS). Speak or feed audio and confirm the needle moves. Aim to keep peaks below 0 dBFS (the gauge turns red above 0).

## What each control does

| Control | Kind | Default | Valid range | Setting key | Notes |
|---|---|---|---|---|---|
| Mic source | Combo box | — | MIC, BAL, LINE, ACC, PC | — | Sent to the radio on change. |
| Mic gain | Slider | 50 | 0–100 | `PcMicGain` (PC source only) | For non-PC sources, gain is stored on the radio. For PC, the value is kept client-side. |
| Level | Meter | — | −40 to +10 dBFS (red above 0) | — | Shows microphone input peak level. Reads −150 when not transmitting and mic monitoring is off. |

## Tips

- The `PC` source routes audio from your computer's sound input. The radio does not report the mic level for this source, so the `PcMicGain` value is stored in AetherSDR and applied locally.
- If you want to blend an accessory microphone with your selected source, enable **+ACC** on the same row after choosing your primary source.

## Troubleshooting

- **Level gauge shows no movement after selecting a source** — Confirm you are transmitting or that mic monitoring is active. The gauge is suppressed to −150 dBFS when neither condition is true.
- **PC source selected but Mic gain slider has no effect on the radio's reported level** — This is expected. The radio always reports mic_level=0 for the PC source. AetherSDR stores the gain in `PcMicGain` and applies it client-side.
- **Phone panel is not visible** — The applet switches to CW controls when the active slice is in a CW mode. Change the active slice to a phone mode to see the mic source controls.

## Related

- [Adjust mic gain and enable the accessory mix](adjust-mic-gain-and-enable-the-accessory-mix.md)
- [Select a mic profile for a specific microphone](select-a-mic-profile-for-a-specific-microphone.md)
- [Enable speech processor at NOR, DX, or DX+ level](enable-speech-processor-at-nor-dx-or-dx-level.md)
