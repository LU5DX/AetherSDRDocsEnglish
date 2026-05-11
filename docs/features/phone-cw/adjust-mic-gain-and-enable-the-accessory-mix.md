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
   - When RADE mode is active, the slider also acts as a client-side RADE gain control and is stored under the same `PcMicGain` key. The slider value is not sent to the radio in this state.
4. Watch the **Level** gauge above the controls. Aim for peaks between −20 and −10 dBFS during normal speech. The gauge turns red above 0 dBFS.
5. To mix in the accessory input alongside the active mic source, click **+ACC** so it is lit. Click it again to disable the mix.

## What each control does

| Control               | What it does                                                                                                                                                                                                                                                                      | Default                                                                                                                  |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| **Mic gain**          | Sets the microphone input level. When Mic source is PC or RADE mode is active, the value is persisted locally as `PcMicGain` and is not sent to the radio.                                                                                                                        | 50                                                                                                                       |
| **+ACC**              | Enables the accessory mic input mix alongside the selected primary source.                                                                                                                                                                                                        | —                                                                                                                        |
| **Level** gauge       | Shows microphone input peak level in dBFS. Turns red above 0 dBFS.                                                                                                                                                                                                                | —                                                                                                                        |
| **Compression** gauge | Shows the amount of speech compression being applied. Fill is reversed (full right = no compression). In v0.9.7, the gauge is gated on the radio's interlock TRANSMITTING state and speech processor enable: it reads 0 dB during RX to prevent stale readings from the TX chain. | —                                                                                                                        |
| **ALC (Phone panel)** | Shows automatic level control reading from MeterModel::swAlcChanged (post-software-ALC SSB peak in dBFS). Fills right-to-left: empty at -20 dBFS, full at 0 dBFS.                                                                                                                 | Rewired from HWALC (RCA voltage) to SW ALC meter in v26.5.1 (#2552). Mirrored by an identical gauge on the CW sub-panel. |
| **ALC (CW panel)**    | Mirrors the Phone-panel ALC gauge; both read from MeterModel::swAlcChanged for consistent readings across voice and CW.                                                                                                                                                           | Added in v26.5.1 (#2552) as part of the SW ALC meter split. Uses HGauge::setFillFromRight mode.                          |

## CW sidetone controls

When the active slice is in CW mode, the CW sub-panel replaces the Phone sub-panel. The following controls govern CW sidetone behavior.

### How the sidetone works (v0.9.1 and later)

A single **Sidetone** toggle and **Sidetone volume** slider control both the radio's DAX-fed monitor and the client-side low-latency sidetone generator (`CwSidetoneGenerator`, approximately 10 ms latency) in lockstep. Enabling or disabling **Sidetone** enables or disables both simultaneously. Moving **Sidetone volume** sets both `mon_gain_cw` on the radio and the local generator volume at the same time.

Pitch and stereo pan always follow the radio's `cw_pitch` and `mon_pan_cw` settings automatically. There are no separate local pitch or follow controls.

The sidetone bus is shared with Quindar tones; sidetone and Quindar tones are mutually exclusive at the mode level.

### v0.9.2.1 change: separate local sidetone controls removed

Prior to v0.9.2.1, the CW sub-panel included a separate **Local STn** toggle, a local volume slider, a **Follow** pitch-follow toggle, and a manual pitch slider. These controls are removed in v0.9.2.1. The **Sidetone** toggle and **Sidetone volume** slider now drive both the radio-side and client-side sidetone together, and pitch and pan always follow the radio automatically.

If you previously used the **Local STn** button independently of the main **Sidetone** toggle, use the **Sidetone** toggle going forward. The local low-latency generator remains available and active whenever **Sidetone** is on.

### v0.9.8 changes: QLineEdit value fields

In v0.9.8 the four CW value labels (Delay, Speed, Sidetone Volume, and Pitch) are now editable text fields. Click any value and type a number directly. The slider moves to match when you press Enter or tab away. This matches SmartSDR behavior.

### CW sub-panel controls

| Control | What it does | Default | Range / Values | Setting key |
|---|---|---|---|---|
| **Delay (CW)** | Sets the CW break-in delay. Drag the slider or click the value field and type a number (0–2000). In v0.9.8, the value is cached immediately when typed so the radio emission doesn't snap the slider back (#2428). | 500 ms | 0–2000 ms (step 10) | — |
| **Speed (CW)** | Sets the CW keying speed in words per minute. Drag the slider or click the value field and type a number (5–100). | 20 WPM | 5–100 WPM | — |
| **Sidetone** | Toggles CW sidetone. Enables/disables both the radio's DAX-fed monitor and the client-side low-latency generator in lockstep. On Windows, the sidetone stream starts immediately on connect (v0.9.3, #2105). The sidetone bus is shared with Quindar tones (mutually exclusive at the mode level). | — | On / Off | — |
| **Sidetone volume** | Sets CW monitor volume. Controls both `mon_gain_cw` on the radio and the local sidetone generator volume simultaneously. Drag the slider or click the value field and type a number (0–100). | 50 | 0–100 | — |
| **L / R pan (CW)** | Sets CW monitor stereo pan. Applies to both the radio-side monitor and the local sidetone generator. Double-click to recenter. | 50 | 0–100 | — |
| **Pitch < / >** | Sets the CW sidetone and decode pitch. Type a value (100–6000) in the text field or click the < and > buttons to step by 10 Hz. Pitch is also followed automatically from the radio's `cw_pitch` setting. | 600 Hz | 100–6000 Hz (step 10) | — |
| **Breakin** | Toggles full break-in (QSK). In v0.9.7, the CW keyboard and MIDI paths fully honor this setting: with Breakin ON (QSK) key edges trigger TX and the break-in delay holds the relay; with Breakin OFF keys are queued and the operator engages PTT manually. The previous auto-PTT envelope that masked Breakin OFF and eliminated QSK hang time has been removed. | — | On / Off | — |
| **Iambic** | Toggles the iambic paddle keyer. | — | On / Off | — |
| **ALC (CW panel)** | Shows automatic level control reading from MeterModel::swAlcChanged (post-software-ALC SSB peak in dBFS). Fills right-to-left: empty at -20 dBFS, full at 0 dBFS. Mirrors the Phone-panel ALC gauge. | — | -20 to 0 dBFS (red > -3 dBFS) | — |

## Tips

- The **Level** gauge is suppressed to −150 dBFS when the radio is not transmitting and monitor-in-receive is off. This is normal; the gauge becomes active when you transmit. When **Mic source** is set to PC, the gauge uses client-side metering and is not subject to this suppression — it appears immediately on connect (v0.9.3, #2086). When RADE mode is active, the gauge also uses client-side metering and is active during RX.
- The **Compression** gauge reads 0 dB whenever the radio is not in the TRANSMITTING interlock state (v0.9.7). This prevents stale TX chain readings from appearing during RX. The gauge becomes active as soon as you transmit with the speech processor enabled.
- If you use the PC source, note that the `PcMicGain` value is not sent to the radio — it is managed entirely by AetherSDR. Switching away from the PC source and back restores the saved value. RADE mode shares this same `PcMicGain` setting.
- With **Breakin** off in v0.9.7, key presses are queued and TX is not engaged automatically. Engage PTT manually before sending. If you expect full QSK operation, confirm **Breakin** is lit before keying.
- The client-side sidetone generator provides approximately 10 ms latency, which is useful at higher CW speeds where the radio's round-trip DAX latency becomes noticeable. Because both are controlled by the single **Sidetone** toggle, there is no risk of one being active without the other.
- Double-click **L / R pan (CW)** to return the pan position to center (50).
- In v0.9.8, the Delay, Speed, Sidetone Volume, and Pitch value fields accept direct numeric input. Type a value and press Enter or tab away — the slider moves to match. The fields validate input and enforce the valid range automatically.
- In v26.5.1, the ALC gauge on both the Phone and CW panels was updated to use the software ALC meter (post-software-ALC SSB peak dBFS) instead of the previous HWALC (RCA voltage) path. Both gauges now read from the same MeterModel::swAlcChanged source, so the reading is consistent across voice and CW modes. The range is -20 to 0 dBFS, with the gauge filling from right to left. Values outside this range pin at the nearest end.

## Troubleshooting

- **Mic gain slider snaps back or reads 0 after adjusting** — You are using the PC source and the radio is reporting `mic_level=0`. This is expected behavior; AetherSDR holds the value in `PcMicGain` and does not write it to the radio. The slider position is correct.
- **Mic gain slider does not update the radio when RADE mode is active** — This is expected. In RADE mode the slider acts as a client-side gain control stored in `PcMicGain`. Sending the value to the radio would overwrite the hardware mic setting. The slider will resume normal radio-side behavior when RADE mode is deactivated.
- **+ACC has no effect** — Confirm the radio is in a voice mode and the Phone sub-panel is active. The +ACC control is only present in the Phone sub-panel; it is not available when CW mode is active.
- **Level gauge shows no movement while speaking** — If Mic source is not PC and RADE mode is not active, the gauge suppresses to −150 dBFS when not transmitting and monitor-in-receive is off. Key the radio or enable the TX monitor to see live levels. If Mic source is PC or RADE mode is active, the gauge should be active immediately; if it is not, verify the audio device is selected and AetherSDR is connected to the radio.
- **Compression gauge always shows 0 dB** — The Compression gauge is gated on the radio's interlock TRANSMITTING state (v0.9.7). It will only show a non-zero reading while the radio is actively transmitting and the speech processor (**PROC**) is enabled. Confirm **PROC** is lit and that you are transmitting.
- **Breakin OFF has no effect — radio still keys on CW input** — This was a bug resolved in v0.9.7. The previous auto-PTT envelope forced TX regardless of the Breakin setting. Update to v0.9.7 or later. After updating, with **Breakin** off, engage PTT manually before sending CW.
- **Phone panel does not refresh when VOX is toggled via keyboard shortcut** — This was resolved in v0.9.3 (#2084). Update to v0.9.3 or later.
- **Sidetone not audible immediately after connecting on Windows** — This was resolved in v0.9.3 (#2105) by fixing the AudioEngine initialization order. Update to v0.9.3 or later.
- **Local STn / Follow controls are