The diff shows only internal C++ infrastructure changes (new private class forward declaration, private member pointers, and an internal method added to `AppletPanel`). The `PhoneCwApplet` catalog entry has no controls changes. The current documentation already contains the ShackSwitch section added for v0.9.4. No user-visible documentation change is warranted.

# Phone/CW overview

The Phone/CW applet is a mode-aware transmit panel that provides microphone, processor, and monitor controls in voice modes, and automatically switches to CW controls when the active slice is in a CW mode. Open it to adjust transmit audio or set keying parameters.

## How it works

The applet is always present in the Applet Panel on the right sidebar. Toggle it using the **P/CW** tray button. It contains two sub-panels managed by a stacked layout:

- **Phone sub-panel** — visible when the active slice is in a voice mode (SSB, AM, FM, and similar).
- **CW sub-panel** — visible when the active slice is in a CW mode.

AetherSDR switches between sub-panels automatically as you change the slice mode. You do not switch them manually.

### Phone sub-panel

| Control        | Kind          | What it does                                                                                                                                                                                                                             |
|----------------|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Level          | Meter         | Shows microphone input peak level in dBFS. Suppressed to -150 when met_in_rx is off and not transmitting. Exception: when mic source is PC, the gauge uses client-side metering and is not suppressed by met_in_rx (#2086). |
| Compression    | Meter         | Shows speech compression amount in dB (reversed fill — higher compression fills left).                                                                                                                                                   |
| Mic profile    | Combo box     | Loads the named mic processing profile from the radio's profile list.                                                                                                                                                                    |
| Mic source     | Combo box     | Selects the microphone input source.                                                                                                                                                                                                     |
| Mic gain       | Slider        | Adjusts mic input level. When source is PC, the value is kept client-side because the radio always reports level 0 for PC sources.                                                                                                       |
| +ACC           | Toggle button | Enables the accessory mic input mix.                                                                                                                                                                                                     |
| PROC           | Toggle button | Toggles the speech processor.                                                                                                                                                                                                            |
| NOR/DX/DX+     | Slider        | Sets the speech processor level. Three positions: NOR (0), DX (1), DX+ (2).                                                                                                                                                             |
| DAX            | Toggle button | Enables DAX as the TX audio source.                                                                                                                                                                                                      |
| MON            | Toggle button | Enables the sideband TX monitor.                                                                                                                                                                                                         |
| Monitor volume | Slider        | Sets the sideband monitor volume.                                                                                                                                                                                                        |

### CW sub-panel

| Control | Kind | What it does | Default | Range / Options | Setting key |
|---|---|---|---|---|---|
| ALC | Meter | Shows the automatic level control reading. Red above 80. | — | 0–100 | — |
| Delay | Slider | Sets CW break-in delay in milliseconds. | — | 0–2000 ms (step 10) | — |
| Speed | Slider | Sets CW keying speed. | — | 5–100 WPM | — |
| Breakin | Toggle button | Toggles full break-in (QSK). | — | On / Off | — |
| Iambic | Toggle button | Toggles the iambic paddle keyer. | — | On / Off | — |
| Pitch < / > | Spin box | Steps the CW sidetone and decode pitch by 10 Hz. | 600 Hz | 100–6000 Hz (step 10) | — |
| Sidetone | Toggle button | Toggles both the radio CW sidetone monitor (DAX-fed) and the client-side low-latency CW sidetone generator in lockstep. On Windows, the sidetone stream now starts immediately on connect (#2105). | — | On / Off | — |
| Sidetone volume | Slider | Sets both the radio CW monitor volume (mon_gain_cw) and the client-side sidetone generator volume in lockstep. | — | 0–100 | — |
| L / R pan (CW) | Slider | CW monitor pan position. Applies constant-power pan to both the radio monitor and the local sidetone generator. Double-click to recenter. | 50 | 0–100 | — |

### Sidetone behaviour (v0.9.1+)

The **Sidetone** toggle and **Sidetone volume** slider control both the radio's DAX-fed monitor and the client-side low-latency CW sidetone generator (CwSidetoneGenerator, approximately 10 ms latency) in lockstep. There is no separate local sidetone toggle or volume slider. Pitch and pan always follow the radio's `cw_pitch` and `mon_pan_cw` settings automatically — no manual override is required or available.

The local sidetone is suitable for paddle, straight-key, and CWX-generated transmissions where network round-trip latency would make the radio's DAX-fed monitor unusable at higher speeds.

### VOX and keyboard shortcut behaviour (v0.9.3)

When VOX is toggled via a keyboard shortcut, the Phone panel now refreshes immediately to reflect the new VOX state (#2084). In earlier versions the panel did not update until some other UI event occurred.

## ShackSwitch applet (v0.9.4)

The Applet Panel now hosts a **ShackSwitch** applet alongside the existing applets. When a ShackSwitch device is detected, its button and applet become visible automatically. When the device is no longer present, they are hidden. No manual configuration is required to show or hide this applet — AetherSDR manages visibility through the `setShackSwitchVisible` method based on device presence.

## Tips

- The `PcMicGain` value is stored client-side only. If you switch mic source away from PC and back, AetherSDR restores the saved value rather than reading from the radio.
- When mic source is PC, the Level gauge uses client-side metering and appears immediately on connect, regardless of the met_in_rx setting.
- Because pitch and pan always follow the radio settings automatically, adjust CW pitch using the **Pitch < / >** spin box and pan using the **L / R pan (CW)** slider — both the radio monitor and the local sidetone update together.
- The **Sidetone** toggle enables or disables the local sidetone at the same time as the radio monitor. You cannot enable one independently of the other.

## Related

- [Pick a mic source (MIC, BAL, LINE, ACC, PC)](pick-a-mic-source-mic-bal-line-acc-pc.md)
- [Adjust mic gain and enable the accessory mix](adjust-mic-gain-and-enable-the-accessory-mix.md)
- [Select a mic profile for a specific microphone](select-a-mic-profile-for-a-specific-microphone.md)
- [Enable speech processor at NOR, DX, or DX+ level](enable-speech-processor-at-nor-dx-or-dx-level.md)
- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)
- [Set CW keying speed in WPM](set-cw-keying-speed-in-wpm.md)
- [Set CW break-in delay](set-cw-break-in-delay.md)
- [Enable iambic paddle keying](enable-iambic-paddle-keying.md)
- [Change CW pitch / sidetone frequency](change-cw-pitch-sidetone-frequency.md)
<!-- docmesh:llm version=v0.9.4 date=2026-05-01 -->