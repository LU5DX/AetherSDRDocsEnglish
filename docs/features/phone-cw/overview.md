# Phone/CW overview

The Phone/CW applet is a mode-aware transmit panel that provides microphone, processor, and monitor controls in voice modes, and automatically switches to CW controls when the active slice is in a CW mode. Open it to adjust transmit audio or set keying parameters.

## How it works

The applet is always present in the Applet Panel on the right sidebar. Toggle it using the **P/CW** tray button. It contains two sub-panels managed by a stacked layout:

- **Phone sub-panel** — visible when the active slice is in a voice mode (SSB, AM, FM, and similar).
- **CW sub-panel** — visible when the active slice is in a CW mode.

AetherSDR switches between sub-panels automatically as you change the slice mode. You do not switch them manually.

### Phone sub-panel

| Control           | Kind         | What it does                                                                                                                                                                                                                                                                                                                                             |
|-------------------|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Level             | Meter        | Shows microphone input peak level in dBFS. Suppressed to -150 when met_in_rx is off and not transmitting.                                                                                                                                                                                                                                                |
| Compression       | Meter        | Shows speech compression amount in dB. Gated on the radio's interlock TRANSMITTING state and speech processor enable: reads 0 dB during RX to prevent confusing stale readings from the TX chain. In v26.5.3, the meter range is reversed: 0 = no compression, -25 = full compression.                                                                   |
| Mic profile       | Combo box    | Loads the named mic processing profile from the radio's profile list.                                                                                                                                                                                                                                                                                    |
| Mic source        | Combo box    | Selects the microphone input source.                                                                                                                                                                                                                                                                                                                     |
| Mic gain          | Slider       | Adjusts mic input level. When source is PC, the value is kept client-side (stored as `PcMicGain`).                                                                                                                                                                                                                                                        |
| +ACC              | Toggle button| Enables the accessory mic input mix.                                                                                                                                                                                                                                                                                                                     |
| PROC              | Toggle button| Toggles the speech processor.                                                                                                                                                                                                                                                                                                                            |
| NOR/DX/DX+        | Slider       | Sets the speech processor level. Three positions: NOR (0), DX (1), DX+ (2).                                                                                                                                                                                                                                                                              |
| DAX               | Toggle button| Enables DAX as the TX audio source.                                                                                                                                                                                                                                                                                                                      |
| MON               | Toggle button| Enables the sideband TX monitor.                                                                                                                                                                                                                                                                                                                         |
| Monitor volume    | Slider       | Sets the sideband monitor volume.                                                                                                                                                                                                                                                                                                                        |
| ALC (Phone panel) | Meter        | Shows automatic level control reading from MeterModel::swAlcChanged (post-software-ALC SSB peak in dBFS, range -20 to 0 dBFS, red above -3). Fills right-to-left: empty at -20 dBFS, full at 0 dBFS. Rewired from HWALC (RCA voltage) to SW ALC meter in v26.5.1 (#2552). In v26.5.3, the gauge initializes to -20 dBFS on construction. Mirrored by an identical gauge on the CW sub-panel. |

### CW sub-panel

| Control           | Kind          | What it does                                                                                                                                                                                                                                                                                                                          | Default  | Range / Options        | Setting key |
|-------------------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|------------------------|-------------|
| ALC (CW panel)    | Meter         | Shows automatic level control reading from MeterModel::swAlcChanged (post-software-ALC SSB peak in dBFS, range -20 to 0 dBFS, red above -3). Fills right-to-left: empty at -20 dBFS, full at 0 dBFS. In v26.5.3, the gauge initializes to -20 dBFS on construction. Mirrors the Phone-panel ALC gauge identically.                      | —        | -20 to 0 dBFS          | —           |
| Delay             | Slider        | Sets CW break-in delay in milliseconds. The adjacent QLineEdit accepts typed values (0–2000). When you type a value and press Enter, the slider updates to match. The slider does not snap back unexpectedly because the value is cached immediately (v0.9.8, #2428).                                                                    | 500      | 0–2000 ms (step 10)    | —           |
| Speed             | Slider        | Sets CW keying speed. The adjacent QLineEdit accepts typed values (5–100). When you type a value and press Enter, the slider updates to match.                                                                                                                                                                                         | 20       | 5–100 WPM              | —           |
| Breakin           | Toggle button | Toggles full break-in (QSK). With Breakin ON, key edges trigger TX and the break-in delay holds the relay. With Breakin OFF, keys are queued and the operator engages PTT manually. The previous auto-PTT envelope that masked Breakin OFF and interfered with QSK hang time has been removed in v0.9.7.                               | —        | On / Off               | —           |
| Iambic            | Toggle button | Toggles the iambic paddle keyer.                                                                                                                                                                                                                                                                                                      | —        | On / Off               | —           |
| Pitch < / >       | Text field    | QLineEdit with < / > buttons (CwTriBtn). Type a value (100–6000) or click the buttons to step by 10 Hz. Steps the CW sidetone and decode pitch.                                                                                                                                                                                        | 600 Hz   | 100–6000 Hz (step 10)  | —           |
| Sidetone          | Toggle button | Toggles both the radio CW sidetone monitor (DAX-fed) and the client-side low-latency CW sidetone generator in lockstep. In v26.5.3, the sidetone routes to the user-selected audio output instead of the default output (#2899). On Windows, the sidetone stream starts immediately on connect (#2105).                         | —        | On / Off               | —           |
| Sidetone volume   | Slider        | Sets both the radio CW monitor volume (mon_gain_cw) and the client-side sidetone generator volume in lockstep. The adjacent QLineEdit accepts typed values (0–100). When you type a value and press Enter, the slider updates to match.                                                                                                | 50       | 0–100                  | —           |
| L / R pan (CW)    | Slider        | CW monitor pan position. Applies constant-power pan to both the radio monitor and the local sidetone generator. Double-click to recenter.                                                                                                                                                                                              | 50       | 0–100                  | —           |

### Inline value editing (v0.9.8)

In v0.9.8 the four CW value labels (Delay, Speed, Sidetone Volume, Pitch) are now QLineEdit widgets with QIntValidator. Click any value and type a number directly, then press Enter. The slider or control updates to match the typed value. This provides SmartSDR parity for direct numeric entry. The editable fields are:

- **Delay (CW)** — accepts 0–2000
- **Speed (CW)** — accepts 5–100
- **Sidetone volume** — accepts 0–100
- **Pitch < / >** — accepts 100–6000

When you are actively editing a field, the slider stops updating that field's text until you finish editing, preventing visual conflicts.

### Sidetone behaviour (v0.9.1+)

The **Sidetone** toggle and **Sidetone volume** slider control both the radio's DAX-fed monitor and the client-side low-latency CW sidetone generator (CwSidetoneGenerator, approximately 10 ms latency) in lockstep. In v26.5.3, the local sidetone routes to the user-selected audio output instead of the default output (#2899). There is no separate local sidetone toggle or volume slider. Pitch and pan always follow the radio's `cw_pitch` and `mon_pan_cw` settings automatically — no manual override is required or available.

The local sidetone is suitable for paddle, straight-key, and CWX-generated transmissions where network round-trip latency would make the radio's DAX-fed monitor unusable at higher speeds.

The sidetone bus is shared with Quindar tones. Sidetone and Quindar tones are mutually exclusive at the mode level.

### Break-in behaviour (v0.9.7)

The CW keyboard and MIDI paths now fully honor the radio's `break_in` setting. With **Breakin** ON (QSK), key edges trigger TX and the break-in delay holds the relay open between elements. With **Breakin** OFF, keyed characters are queued and you engage PTT manually before sending. An auto-PTT envelope present in earlier versions that masked the Breakin OFF state and eliminated QSK hang time has been removed.

### Level meter receive gate (v26.5.3)

In v26.5.3, the Level gauge suppression logic during receive was refactored into the dedicated `applyLevelMeterReceiveGate()` method. When `met_in_rx` is off and the radio is not transmitting, the Level gauge is suppressed to -150 dBFS regardless of the mic source. This method is called whenever the transmit state or MOX state changes, and also when RADE mode activates or deactivates.

### ALC gauge initialization (v26.5.3)

In v26.5.3, both the Phone panel and CW panel ALC gauges now initialize to -20 dBFS on construction using `setValueImmediate()`. This ensures the gauges start empty when the applet first appears, rather than showing an undefined state until the first meter update arrives from the radio.

### Compression gauge update (v26.5.3)

In v26.5.3, the Compression gauge interpretation was corrected. The MeterModel exposes COMPPEAK as a positive 0..25 dB compression amount. The P/CW gauge face is reversed: 0 = no compression, -25 = full compression. The gauge displays the negative of the compression value, so the needle or bar moves downwards as compression increases.

### RADE mode interaction (v0.9.7)

When RADE mode is active, the **Mic gain** slider acts as a client-side RADE gain control rather than sending a mic level command to the radio. The slider value is stored under the `PcMicGain` setting, shared with the PC mic source path. The radio's mic level setting is not overwritten while RADE is active.

The **Level** gauge continues to show signal level during RX when RADE is active, regardless of the `met_in_rx` setting. When RADE deactivates, the gauge reverts to normal suppression behavior and is reset to -150 dBFS immediately.

### VOX and keyboard shortcut behaviour (v0.9.3)

When VOX is toggled via a keyboard shortcut, the Phone panel now refreshes immediately to reflect the new VOX state (#2084). In earlier versions the panel did not update until some other UI event occurred.

### CWX panel (v0.9.7)

The embedded CWX panel scopes its F1-F12 shortcuts to panel visibility (#2464, #2469) so DVK panel F-key bindings and CWX hotkeys no longer fire simultaneously. CWX macros also release TX automatically when the queue drains (#2450, #2507).

## Tips

- The `PcMicGain` value is stored client-side only. It is used both when mic source is PC and when RADE mode is active. If you switch mic source away from PC and back, AetherSDR restores the saved value rather than reading from the radio.
- When mic source is PC, or when RADE mode is active, the Level gauge uses client-side metering and appears immediately on connect, regardless of the `met_in_rx` setting.
- The **Compression** gauge reads 0 dB during RX. This is intentional — it prevents stale TX chain readings from being displayed while receiving.
- Because pitch and pan always follow the radio settings automatically, adjust CW pitch using the **Pitch < / >** text field and pan using the **L / R pan (CW)** slider — both the radio monitor and the local sidetone update together.
- To type a CW value directly, click the number, type a value, and press Enter. The slider moves to match.
- The **Sidetone** toggle enables or disables the local sidetone at the same time as the radio monitor. You cannot enable one independently of the other.
- With **Breakin** OFF, key presses are queued but TX is not triggered automatically. Engage PTT manually before beginning to send.
- The ALC gauges start empty (-20 dBFS) when the applet first appears, so do not be concerned if they show no reading until the first transmit event.

## Related

- [Pick a mic source (MIC, BAL, LINE, ACC, PC)](pick-a-mic-source-mic-bal-line-acc-pc.md)
- [Adjust mic gain and enable the accessory mix](adjust-mic-gain-and-enable-the-accessory-mix.md)
- [Select a mic profile for a specific microphone](select-a-mic-profile-for-a-specific-microphone.md)
- [Enable speech processor at NOR, DX, or DX+ level](enable-speech-processor-at-nor-dx-or-dx-level.md)
- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)
- [Set CW keying speed in WPM](set-cw-keying-speed-in-wpm.md)
- [Set CW break-in delay](set-cw-break-in-delay.md)
- [Enable iambic paddle key