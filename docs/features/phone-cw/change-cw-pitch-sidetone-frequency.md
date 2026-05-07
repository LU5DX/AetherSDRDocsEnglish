# Phone/CW applet

The Phone/CW applet provides a mode-aware transmit control panel. When the active slice is in a voice mode (LSB, USB, AM, FM, etc.), it displays microphone, processor, and monitor controls. When the active slice switches to CW mode, the panel automatically switches to show CW controls including delay, speed, sidetone, iambic, and pitch settings.

In v0.9.8, the four CW value labels (Delay, Speed, Sidetone volume, Pitch) are now editable `QLineEdit` widgets with `QIntValidator`. Click any value field and type a number directly. When you press Enter or Tab, the value is validated and applied to both the slider and the radio. Sliding the control while the text field is not focused still updates the text immediately.

The single **Sidetone** toggle and **Sidetone volume** slider drive both the radio's DAX-fed monitor and the client-side low-latency sidetone generator (`CwSidetoneGenerator`, approximately 10 ms latency) in lockstep. Pitch and pan always follow the radio's `cw_pitch` and `mon_pan_cw` settings automatically.

In v0.9.7, the **Compression** gauge is now gated on the radio's interlock TRANSMITTING state (not meter flow), so it reads 0 during receive. **Breakin** now fully honors the radio's `break_in` setting — no auto-PTT envelope forces TX any more. The sidetone bus is shared with Quindar tones (mutually exclusive at the mode level).

## Before you start

- Connect to a FLEX-8600 radio. The Phone/CW applet requires an active radio connection.
- Set the active slice to a CW mode to see CW controls, or to a voice mode to see Phone controls. The applet switches automatically.
- Open the Phone/CW applet by clicking the **P/CW** tray button in the right sidebar if it is not already visible.

## Steps

### Change the radio CW pitch

1. Locate **Pitch < / >** in the CW sub-panel. It displays the current pitch value with **<** and **>** buttons on either side.
2. To type a value directly, click the numeric field, enter a value between 100 and 6000, and press Enter or Tab.
3. To adjust in 10 Hz steps, click **<** to decrease the pitch or **>** to increase it.
4. The new pitch is sent to the radio immediately. Default: 600 Hz.

The client-side sidetone generator always follows this pitch value automatically. There is no separate local pitch control.

### Adjust CW delay

1. Locate **Delay** in the CW sub-panel. It has a slider and an editable value field.
2. To type a value directly, click the numeric field, enter a value between 0 and 2000 (milliseconds), and press Enter or Tab. The slider moves to match.
3. Slide the control to adjust in 10 ms steps.
4. Default: 500 ms.

In v0.9.8, the `setCwDelay` method was fixed to cache the value immediately so the radio emission does not snap the slider back (#2428).

### Adjust CW speed

1. Locate **Speed** in the CW sub-panel. It has a slider and an editable value field.
2. To type a value directly, click the numeric field, enter a value between 5 and 100 (WPM), and press Enter or Tab. The slider moves to match.
3. Slide the control to adjust in steps.
4. Default: 20 WPM.

### Enable or disable the sidetone

1. Click **Sidetone** in the CW sub-panel to toggle it on or off.
2. Both the radio's DAX-fed monitor and the client-side low-latency sidetone generator are enabled or disabled together by this single button.

### Adjust sidetone volume

1. Locate **Sidetone volume** in the CW sub-panel. It has a slider and an editable value field.
2. To type a value directly, click the numeric field, enter a value between 0 and 100, and press Enter or Tab. The slider moves to match.
3. Slide the control to adjust the volume.
4. Default: 50.
5. The slider sets both the radio monitor volume (`mon_gain_cw`) and the client-side sidetone generator volume simultaneously.

### Adjust CW monitor pan

1. Locate **L / R pan (CW)** in the CW sub-panel. It is a slider from 0 (full left) to 100 (full right).
2. Slide to the desired stereo position.
3. Double-click the slider to recenter to 50 (centre).
4. Default: 50.

### Toggle break-in (QSK)

1. Click **Breakin** in the CW sub-panel. When enabled (full break-in, QSK), key edges trigger TX immediately and the break-in delay holds the relay open between elements.
2. When break-in is off, keys are queued and the radio does not go to TX until you engage PTT manually. The previous auto-PTT envelope that masked Breakin OFF has been removed (v0.9.7).

### Toggle iambic keyer

1. Click **Iambic** in the CW sub-panel to enable or disable the iambic paddle keyer.

### Adjust microphone controls (Phone panel)

1. Select a mic profile from the **Mic profile** combo box to load the named mic processing profile.
2. Select the mic source from the **Mic source** combo box (MIC, BAL, LINE, ACC, PC, plus any from the radio's mic input list).
3. Adjust the **Mic gain** slider (0–100, default 50) to set the microphone input level. When the source is set to **PC**, the value is stored client-side in `PcMicGain` and the radio ignores it.
4. Click **+ACC** to enable the accessory microphone input mix.
5. Click **PROC** to toggle the speech processor on or off.
6. Use the **NOR/DX/DX+** slider to select the processor level (0 = NOR, 1 = DX, 2 = DX+).
7. Click **DAX** to enable DAX as the TX audio source.
8. Click **MON** to enable the sideband monitor.
9. Adjust the **Monitor volume** slider (0–100) to set the sideband monitor volume.

### Read the meters

- **Level** gauge: Shows microphone input peak level in dBFS (-40 to +10 dBFS, red above 0 dBFS). Suppressed to -150 when `met_in_rx` is off and not transmitting.
- **Compression** gauge: Shows speech compression amount in dB (-25 to 0 dB, reversed fill). Gated on the radio's interlock TRANSMITTING state and speech processor enable. Reads 0 dB during receive (v0.9.7).
- **ALC** gauge (CW sub-panel): Shows automatic level control reading (0–100, red above 80).

## What each control does

### Phone controls

| Control             | Default | Valid range       |
|---------------------|---------|-------------------|
| **Mic profile**     | —       | From radio list   |
| **Mic source**      | —       | MIC, BAL, LINE, ACC, PC |
| **Mic gain**        | 50      | 0–100             |
| **+ACC**            | —       | On / Off          |
| **PROC**            | —       | On / Off          |
| **NOR/DX/DX+**      | 0       | 0, 1, 2           |
| **DAX**             | —       | On / Off          |
| **MON**             | —       | On / Off          |
| **Monitor volume**  | —       | 0–100             |

### CW controls

| Control             | Default | Valid range           |
|---------------------|---------|-----------------------|
| **Delay (CW)**      | 500 ms  | 0–2000 ms (step 10)   |
| **Speed (CW)**      | 20 WPM  | 5–100 WPM             |
| **Sidetone**        | —       | On / Off              |
| **Sidetone volume** | 50      | 0–100                 |
| **L / R pan (CW)**  | 50      | 0–100                 |
| **Breakin**         | —       | On / Off              |
| **Iambic**          | —       | On / Off              |
| **Pitch < / >**     | 600 Hz  | 100–6000 Hz (step 10) |

## RADE mode and the mic level slider

When RADE mode is active, the **Mic gain** slider acts as a client-side RADE gain control rather than sending a mic level command to the radio. This mirrors the behavior of the **PC** mic source, where the radio does not use the mic level value. Both cases store their gain in `PcMicGain`.

While RADE is active:

- The **Mic gain** slider reads from and saves to `PcMicGain` and does not send `mic_level` commands to the radio.
- The **Level** gauge remains active during receive. RADE provides client-side metering independent of the radio's `met_in_rx` setting, so you can monitor your audio level before transmitting.
- When RADE mode is turned off, the slider reverts to reflecting the radio's mic level, and the **Level** gauge returns to its normal suppression behavior when `met_in_rx` is off and the radio is not transmitting.

## Tips

- The **Pitch < / >** control affects both the audible sidetone on the radio and the frequency used by the CW decoder. Adjust it to match your personal pitch preference. The client-side sidetone always tracks it automatically.
- Because pitch and pan follow the radio settings automatically, you only need to adjust **Pitch < / >** and **L / R pan (CW)** in one place — both the radio monitor and the local generator update together.
- The client-side sidetone generator operates at approximately 10 ms latency and works with paddle, straight key, and CWX-generated transmissions. If you are not hearing a sidetone at all, verify that **Sidetone** is enabled.
- When **Mic source** is set to **PC**, the **Level** gauge reflects client-side metering and remains active regardless of the radio's `met_in_rx` setting. The same applies when RADE mode is active.
- The **Compression** gauge reads 0 dB during receive. It only shows a value while the radio's interlock reports TRANSMITTING and the speech processor is enabled. This prevents stale readings from appearing between transmissions.
- With **Breakin** off, keys are queued and the radio does not go to TX until you engage PTT manually. With **Breakin** on (QSK), key edges trigger TX immediately and the break-in delay holds the relay open between elements. There is no longer an automatic PTT envelope that overrides this setting (v0.9.7).
- For CW value fields (**Delay**, **Speed**, **Sidetone volume**, **Pitch**), click the numeric field, type your value, and press Enter or Tab. The value is validated and applied to both the slider and the radio (v0.9.8).

## Troubleshooting

- **No sidetone is audible** — Confirm **Sidetone** is enabled and **Sidetone volume** is above zero. Both the radio monitor and the client-side generator are controlled by these two controls.
- **Sidetone does not start on connect (Windows)** — This was resolved in v0.9.3 (#2105). Ensure you are running v0.9.3 or later.
- **Level gauge does not appear on connect** — If **Mic source** is set to **PC** or RADE mode is active, the gauge should appear immediately on connect. For other mic sources without RADE, the gauge is suppressed when `met_in_rx` is off and the radio is not transmitting.
- **Compression gauge shows 0 dB during receive** — This is expected behavior from v0.9.7 onward. The gauge is gated on the radio's interlock TRANSMITTING state and only shows a value while transmitting with the speech processor enabled.
- **Breakin does not engage QSK** — Confirm **Breakin** is enabled in the CW sub-panel. From v0.9.7, the keyboard and MIDI keying paths fully honor this setting; no automatic PTT envelope overrides it.
- **Pitch change has no effect** — Confirm the active slice is in a CW mode. The CW sub-panel and its pitch control are only active in CW modes.
- **CW sub-panel is not visible** — The active slice is not in a CW mode. Switch the slice to CW; the applet switches automatically.
- **CW delay slider snaps back when adjusting** — This was resolved in v0.9.8 (#2428). Ensure you are running v0.9.8 or later.
- **Typed CW value does not apply** — Press Enter or Tab after typing the value in the editable field. The value is validated and applied when `editingFinished` fires.
- **Mic gain slider does not update the radio in RADE mode** — This is correct. In RADE mode the slider controls client-side RADE gain only and stores the value in `PcMicGain`. The radio's mic level setting is not affected.

## Related

- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)