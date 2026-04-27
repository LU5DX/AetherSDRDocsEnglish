# Adjust mic gain and enable the accessory mix

Use this page to set the microphone input level and mix in the accessory input alongside the primary mic source in Phone mode.

## Before you start

- AetherSDR must be connected to the radio. The Phone/CW applet requires an active radio connection.
- The active slice must be in a voice mode (USB, LSB, AM, FM) so the Phone sub-panel is visible. If the slice is in CW mode, the CW sub-panel is shown instead.

## Steps

1. Open the Phone/CW applet in the Applet Panel on the right sidebar. If it is not visible, click the **P/CW** tray button.
2. Locate the **Mic source** combo box. Confirm the source you want to adjust is selected (for example, MIC, BAL, LINE, ACC, or PC).
3. Drag the **Mic gain** slider left or right to set the input level. The numeric readout to the right of the slider updates as you drag. The valid range is 0–100; the default is 50.
   - When **Mic source** is set to PC, the value is stored client-side as `PcMicGain`. The radio always reports `mic_level=0` for the PC source; AetherSDR retains the value locally.
4. Watch the **Level** gauge above the controls. Aim for peaks between −20 and −10 dBFS during normal speech. The gauge turns red above 0 dBFS.
5. To mix in the accessory input alongside the active mic source, click **+ACC** so it is lit. Click it again to disable the mix.

## What each control does

| Control | What it does | Default | Range / Values | Setting key |
|---|---|---|---|---|
| **Mic gain** | Sets the microphone input level. When Mic source is PC, the value is persisted locally. | 50 | 0–100 | `PcMicGain` (PC source only) |
| **+ACC** | Enables the accessory mic input mix alongside the selected primary source. | — | On / Off | — |
| **Level** gauge | Shows microphone input peak level in dBFS. Turns red above 0 dBFS. | — | −40 to +10 dBFS | — |
| **Compression** gauge | Shows the amount of speech compression being applied. Fill is reversed (full right = no compression). | — | −25 to 0 dB | — |

## Tips

- The **Level** gauge is suppressed to −150 dBFS when the radio is not transmitting and monitor-in-receive is off. This is normal; the gauge becomes active when you transmit.
- If you use the PC source, note that the `PcMicGain` value is not sent to the radio — it is managed entirely by AetherSDR. Switching away from the PC source and back restores the saved value.

## Troubleshooting

- **Mic gain slider snaps back or reads 0 after adjusting** — You are using the PC source and the radio is reporting `mic_level=0`. This is expected behavior; AetherSDR holds the value in `PcMicGain` and does not write it to the radio. The slider position is correct.
- **+ACC has no effect** — Confirm the radio is in a voice mode and the Phone sub-panel is active. The +ACC control is only present in the Phone sub-panel; it is not available when CW mode is active.
- **Level gauge shows no movement while speaking** — The gauge suppresses to −150 dBFS when not transmitting and monitor-in-receive is off. Key the radio or enable the TX monitor to see live levels.

## Related

- [Pick a mic source (MIC, BAL, LINE, ACC, PC)](pick-a-mic-source-mic-bal-line-acc-pc.md)
- [Select a mic profile for a specific microphone](select-a-mic-profile-for-a-specific-microphone.md)
- [Enable speech processor at NOR, DX, or DX+ level](enable-speech-processor-at-nor-dx-or-dx-level.md)
- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)
