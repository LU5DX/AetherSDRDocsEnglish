# Adjust mic gain and enable the accessory mix

Use this page to set the microphone input level and mix in the accessory input alongside the primary mic source in Phone mode.

## Before you start

- AetherSDR must be connected to the radio. The Phone/CW applet requires an active radio connection.
- The active slice must be in a voice mode (USB, LSB, AM, FM) so the Phone sub-panel is visible. If the slice is in CW mode, the CW sub-panel is shown instead. CWU and CWL modes are also recognized as CW modes on radios that report them.

## Steps

1. Open the Phone/CW applet in the Applet Panel on the right sidebar. If it is not visible, click the **P/CW** tray button.
2. Locate the **Mic source** combo box. Confirm the source you want to adjust is selected (for example, MIC, BAL, LINE, ACC, or PC).
   - When host modulation is active, the combo box is disabled and shows only "PC". The radio is modulated by AetherSDR, so the PC microphone is the only available input.
3. Drag the **Mic gain** slider left or right to set the input level. The numeric readout to the right of the slider updates as you drag. The valid range is 0–100; the default is 50.
   - When **Mic source** is set to PC, the value is stored client-side as `PcMicGain`. The radio always reports `mic_level=0` for the PC source; AetherSDR retains the value locally.
   - When RADE mode is active, the slider also acts as a client-side RADE gain control and is stored under the same `PcMicGain` key. The slider value is not sent to the radio in this state.
4. Watch the **Level** gauge above the controls. Aim for peaks between −20 and −10 dBFS during normal speech. Hover over the gauge to see the exact dB reading. The gauge turns red above 0 dBFS.
5. To mix in the accessory input alongside the active mic source, click **+ACC** so it is lit. Click it again to disable the mix.

## What each control does

| Control               | What it does                                                                                                                                                                                                                                                                      | Default                                                                                                                  |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| **Mic gain**          | Sets the microphone input level. When Mic source is PC or RADE mode is active, the value is persisted locally as `PcMicGain` and is not sent to the radio.                                                                                                                        | 50                                                                                                                       |
| **+ACC**              | Enables the accessory mic input mix alongside the selected primary source.                                                                                                                                                                                                        | —                                                                                                                        |
| **Level** gauge       | Shows microphone input peak level in dBFS. Hover over the gauge to see the exact dB reading with one decimal place. Turns red above 0 dBFS. When the radio cannot provide a mic level meter (for example, on radios where the client controls the input), the gauge is hidden. | —                                                                                                                        |
| **Compression** gauge | Shows the amount of speech compression being applied. Fill is reversed (full left = 0 dB, no compression; full right = -25 dB, maximum compression). Hover over the gauge to see the compression amount in dB with one decimal place. In v0.9.7, the gauge is gated on the radio's interlock TRANSMITTING state and speech processor enable: it reads 0 dB during RX to prevent stale readings from the TX chain. In v26.5.3, the meter value is inverted from the previous display: MeterModel exposes compression as a positive 0–25 dB amount, and the gauge converts it to the reversed display (0 at the right edge, -25 at the left edge). | —                                                                                                                        |
| **ALC (Phone panel)** | Shows automatic level control reading from MeterModel::swAlcChanged (post-software-ALC SSB peak in dBFS). Fills right-to-left: empty at -20 dBFS, full at 0 dBFS. Hover over the gauge to see the exact dBFS reading with one decimal place. In v26.5.3, the gauge is initialized to -20 dBFS at construction and immediately set to its floor value to prevent transient display flicker. | —                                                                                                                        |
| **ALC (CW panel)**    | Mirrors the Phone-panel ALC gauge; both read from MeterModel::swAlcChanged for consistent readings across voice and CW. Hover over the gauge to see the exact dBFS reading with one decimal place. In v26.5.3, the gauge is initialized to -20 dBFS at construction and immediately set to its floor value to prevent transient display flicker. | —                                                                                                                        |

## CW sidetone controls

When the active slice is in CW mode (including CWU and CWL on radios that report them), the CW sub-panel replaces the Phone sub-panel. The following controls govern CW sidetone behavior.

### How the sidetone works (v0.9.1 and later)

A single **Sidetone** toggle and **Sidetone volume** slider control both the radio's DAX-fed monitor and the client-side low-latency sidetone generator (`CwSidetoneGenerator`, approximately 10 ms latency) in lockstep. Enabling or disabling **Sidetone** enables or disables both simultaneously. Moving **Sidetone volume** sets both `mon_gain_cw` on the radio and the local generator volume at the same time.

Pitch and stereo pan always follow the radio's `cw_pitch` and `mon_pan_cw` settings automatically. There are no separate local pitch or follow controls.

The sidetone bus is shared with Quindar tones; sidetone and Quindar tones are mutually exclusive at the mode level.

### v0.9.2.1 change: separate local sidetone controls removed

Prior to v0.9.2.1, the CW sub-panel included a separate **Local STn** toggle, a local volume slider, a **Follow** pitch-follow toggle, and a manual pitch slider. These controls are removed in v0.9.2.1. The **Sidetone** toggle and **Sidetone volume** slider now drive both the radio-side and client-side sidetone together, and pitch and pan always follow the radio automatically.

If you previously used the **Local STn** button independently of the main **Sidetone** toggle, use the **Sidetone** toggle going forward. The local low-latency generator remains available and active whenever **Sidetone** is on.

### v0.9.8 changes: QLineEdit value fields

In v0.9.8 the four CW value labels (Delay, Speed, Sidetone Volume, and Pitch) are now editable text fields. Click any value and type a number directly. The slider moves to match when you press Enter or tab away. This matches SmartSDR behavior.

### v26.5.3 changes: sidetone audio output routing

In v26.5.3, the CW sidetone now routes to the user-selected audio output instead of the default output (#2899). This ensures the sidetone is heard on the same device you have selected for other audio streams, rather than always using the system default audio output.

### v26.6.1 changes: theme support

In v26.6.1, the Phone/CW applet fully adopts the AetherSDR theme system. All visual elements — including slider grooves and handles, label text, and push button backgrounds — now use theme colors instead of hardcoded values. The applet container itself is styled with the `applet/digi` theme class, ensuring consistent appearance across all supported themes.

### v26.7.4 changes: hover value popups on gauges

In v26.7.4, all four gauges in the Phone/CW applet (Level, Compression, ALC Phone, and ALC CW) display exact numeric readouts when you hover the mouse over them. This allows you to read precise values without having to estimate against the scale (#3936).

- **Level gauge**: Hover to see the exact microphone peak level in dB with one decimal place (for example, "-15.3 dB").
- **Compression gauge**: Hover to see the compression amount in dB with one decimal place (for example, "8.2 dB"). The value shown is the absolute amount of compression (positive), not the negative offset used for display.
- **ALC gauges (Phone and CW)**: Hover to see the exact dBFS reading with one decimal place (for example, "-6.3 dBFS").

### v26.7.4 changes: host modulation detection

In v26.7.4, when host modulation is active (the radio is modulated by AetherSDR), the **Mic source** combo box is disabled and shows only "PC" as the available source. A tooltip explains that the other sources are FlexRadio jacks and are not available when host modulation is active.

### v26.8.4 changes: capability-aware mic source handling

In v26.8.4, the **Mic source** combo box behavior is now capability-aware. When the radio's input selection cannot be controlled from this client (for example, when the radio takes transmit audio from the computer via the network connection), the combo box is rebuilt to show only "PC" as the selectable option. This prevents the misleading appearance of a disabled MIC entry that might suggest a radio mic input is available when it is not.

When the combo box is narrowed to only "PC", the tooltip explains: "This radio takes transmit audio from this computer. Its own input selection is made on the radio." The model is also updated to report "PC" as the active selection, so any downstream diagnostics (such as radiocert) reflect the actual audio path.

### CW sub-panel controls

| Control | What it does | Default | Range / Values | Setting key |
|---|---|---|---|---|
| **Delay (CW)** | Sets the CW break-in delay. Drag the slider or click the value field and type a number (0–2000). In v0.9.8, the value is cached immediately when typed so the radio emission doesn't snap the slider back (#2428). | 500 ms | 0–2000 ms (step 10) | — |
| **Speed (CW)** | Sets the CW keying speed in words per minute. Drag the slider or click the value field and type a number (5–100). | 20 WPM | 5–100 WPM | — |
| **Sidetone** | Toggles CW sidetone. Enables/disables both the radio's DAX-fed monitor and the client-side low-latency generator in lockstep. On Windows, the sidetone stream starts immediately on connect (v0.9.3, #2105). The sidetone bus is shared with Quindar tones (mutually exclusive at the mode level). In v26.5.3, the sidetone routes to the user-selected audio output (#2899). | — | On / Off | — |
| **Sidetone volume** | Sets CW monitor volume. Controls both `mon_gain_cw` on the radio and the local sidetone generator volume simultaneously. Drag the slider or click the value field and type a number (0–100). | 50 | 0–100 | — |
| **L / R pan (CW)** | Sets CW monitor stereo pan. Applies to both the radio-side monitor and the local sidetone generator. Double-click to recenter. | 50 | 0–100 | — |
| **Pitch < / >** | Sets the CW sidetone and decode pitch. Type a value (100–6000) in the text field or click the < and > buttons to step by 10 Hz. Pitch is also followed automatically from the radio's `cw_pitch` setting. | 600 Hz | 100–6000 Hz (step 10) | — |
| **Breakin** | Toggles full break-in (QSK). In v0.9.7, the CW keyboard and MIDI paths fully honor this setting: with Breakin ON (QSK) key edges trigger TX and the break-in delay holds the relay; with Breakin OFF keys are queued and the operator engages PTT manually. The previous auto-PTT envelope that masked Breakin OFF and eliminated QSK hang time has been removed. | — | On / Off | — |
| **Iambic** | Toggles the iambic paddle keyer. | — | On / Off | — |
| **ALC (CW panel)** | Shows automatic level control reading from MeterModel::swAlcChanged (post-software-ALC SSB peak in dBFS). Fills right-to-left: empty at -20 dBFS, full at 0 dBFS. Hover over the gauge to see the exact dBFS reading with one decimal place. Mirrors the Phone-panel ALC gauge. In v26.5.3, the gauge is initialized to -20 dBFS at construction and immediately set to its floor value to prevent transient display flicker. | — | -20 to 0 dBFS (red > -3 dBFS) | — |

## Tips

- The **Level** gauge is suppressed to −150 dBFS when the radio is not transmitting and monitor-in-receive is off. This is normal; the gauge becomes active when you transmit. When **Mic source** is set to PC, the gauge uses client-side metering and is not subject to this suppression — it appears immediately on connect (v0.9.3, #2086). When RADE mode is active, the gauge also uses client-side metering and is active during RX.
- The **Compression** gauge reads 0 dB whenever the radio is not in the TRANSMITTING interlock state (v0.9.7). This prevents stale TX chain readings from appearing