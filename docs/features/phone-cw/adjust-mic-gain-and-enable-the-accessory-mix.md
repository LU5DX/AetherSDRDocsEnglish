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

## CW sidetone controls

When the active slice is in CW mode, the CW sub-panel replaces the Phone sub-panel. The following controls govern CW sidetone behavior.

### How the sidetone works (v0.9.1 and later)

A single **Sidetone** toggle and **Sidetone volume** slider control both the radio's DAX-fed monitor and the client-side low-latency sidetone generator (`CwSidetoneGenerator`, approximately 10 ms latency) in lockstep. Enabling or disabling **Sidetone** enables or disables both simultaneously. Moving **Sidetone volume** sets both `mon_gain_cw` on the radio and the local generator volume at the same time.

Pitch and stereo pan always follow the radio's `cw_pitch` and `mon_pan_cw` settings automatically. There are no separate local pitch or follow controls.

### v0.9.2.1 change: separate local sidetone controls removed

Prior to v0.9.2.1, the CW sub-panel included a separate **Local STn** toggle, a local volume slider, a **Follow** pitch-follow toggle, and a manual pitch slider. These controls are removed in v0.9.2.1. The **Sidetone** toggle and **Sidetone volume** slider now drive both the radio-side and client-side sidetone together, and pitch and pan always follow the radio automatically.

If you previously used the **Local STn** button independently of the main **Sidetone** toggle, use the **Sidetone** toggle going forward. The local low-latency generator remains available and active whenever **Sidetone** is on.

### CW sub-panel controls

| Control | What it does | Default | Range / Values | Setting key |
|---|---|---|---|---|
| **Delay (CW)** | Sets the CW break-in delay. | — | 0–2000 ms (step 10) | — |
| **Speed (CW)** | Sets the CW keying speed in words per minute. | — | 5–100 WPM | — |
| **Sidetone** | Toggles CW sidetone. Enables/disables both the radio's DAX-fed monitor and the client-side low-latency generator in lockstep. | — | On / Off | — |
| **Sidetone volume** | Sets CW monitor volume. Controls both `mon_gain_cw` on the radio and the local sidetone generator volume simultaneously. | — | 0–100 | — |
| **L / R pan (CW)** | Sets CW monitor stereo pan. Applies to both the radio-side monitor and the local sidetone generator. Double-click to recenter. | 50 | 0–100 | — |
| **Pitch < / >** | Steps the CW sidetone and decode pitch by 10 Hz. Pitch is also followed automatically from the radio's `cw_pitch` setting. | 600 Hz | 100–6000 Hz (step 10) | — |
| **Breakin** | Toggles full break-in (QSK). | — | On / Off | — |
| **Iambic** | Toggles the iambic paddle keyer. | — | On / Off | — |
| **ALC** gauge | Shows the automatic level control reading. Turns red above 80. | — | 0–100 | — |

## Tips

- The **Level** gauge is suppressed to −150 dBFS when the radio is not transmitting and monitor-in-receive is off. This is normal; the gauge becomes active when you transmit.
- If you use the PC source, note that the `PcMicGain` value is not sent to the radio — it is managed entirely by AetherSDR. Switching away from the PC source and back restores the saved value.
- The client-side sidetone generator provides approximately 10 ms latency, which is useful at higher CW speeds where the radio's round-trip DAX latency becomes noticeable. Because both are controlled by the single **Sidetone** toggle, there is no risk of one being active without the other.
- Double-click **L / R pan (CW)** to return the pan position to center (50).

## Troubleshooting

- **Mic gain slider snaps back or reads 0 after adjusting** — You are using the PC source and the radio is reporting `mic_level=0`. This is expected behavior; AetherSDR holds the value in `PcMicGain` and does not write it to the radio. The slider position is correct.
- **+ACC has no effect** — Confirm the radio is in a voice mode and the Phone sub-panel is active. The +ACC control is only present in the Phone sub-panel; it is not available when CW mode is active.
- **Level gauge shows no movement while speaking** — The gauge suppresses to −150 dBFS when not transmitting and monitor-in-receive is off. Key the radio or enable the TX monitor to see live levels.
- **Local STn / Follow controls are missing after upgrading to v0.9.2.1** — These controls were removed in v0.9.2.1. Use the **Sidetone** toggle and **Sidetone volume** slider; they now control both the radio-side and local sidetone together. Pitch and pan follow the radio automatically and no longer require a separate follow toggle.

## Related

- [Pick a mic source (MIC, BAL, LINE, ACC, PC)](pick-a-mic-source-mic-bal-line-acc-pc.md)
- [Select a mic profile for a specific microphone](select-a-mic-profile-for-a-specific-microphone.md)
- [Enable speech processor at NOR, DX, or DX+ level](enable-speech-processor-at-nor-dx-or-dx-level.md)
- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)