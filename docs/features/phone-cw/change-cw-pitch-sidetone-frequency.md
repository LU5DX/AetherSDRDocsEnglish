# Change CW pitch / sidetone frequency

The CW pitch control sets the tone frequency used for sidetone monitoring and CW decode. In v0.9.2.1, the separate local sidetone controls (Local STn button, local volume slider, Follow pitch button, and local pitch slider) have been removed. The single **Sidetone** toggle and **Sidetone volume** slider now drive both the radio's DAX-fed monitor and the client-side low-latency sidetone generator in lockstep. Pitch and pan always follow the radio's `cw_pitch` and `mon_pan_cw` settings automatically.

## Before you start

- Connect to a FLEX-8600 radio. The Phone/CW applet requires an active radio connection.
- Set the active slice to a CW mode. The CW sub-panel is only visible when the active slice is in CW mode; the Phone sub-panel is shown otherwise.
- Open the Phone/CW applet by clicking the **P/CW** tray button in the right sidebar if it is not already visible.

## Steps

### Change the radio CW pitch

1. Locate **Pitch < / >** in the CW sub-panel. It is a spinbox with two arrow buttons.
2. Click **<** to decrease the pitch by 10 Hz, or **>** to increase it by 10 Hz.
3. The new pitch is sent to the radio immediately. Valid range: 100–6000 Hz, step 10 Hz. Default: 600 Hz.

The client-side sidetone generator always follows this pitch value automatically. There is no separate local pitch control.

### Enable or disable the sidetone

1. Click **Sidetone** in the CW sub-panel to toggle it on or off.
2. Both the radio's DAX-fed monitor and the client-side low-latency sidetone generator are enabled or disabled together by this single button.

On Windows, the sidetone stream now starts immediately on connect (v0.9.3, #2105).

### Adjust sidetone volume

1. Move the **Sidetone volume** slider to the desired level. Valid range: 0–100.
2. The slider sets both the radio monitor volume (`mon_gain_cw`) and the client-side sidetone generator volume simultaneously.

## What each control does

| Control             | Default | Valid range           |
|---------------------|---------|-----------------------|
| **Pitch < / >**     | 600 Hz  | 100–6000 Hz (step 10) |
| **Sidetone**        | —       | On / Off              |
| **Sidetone volume** | —       | 0–100                 |
| **L / R pan (CW)**  | 50      | 0–100                 |

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
- With **Breakin** off, keys are queued and the radio does not go to TX until you engage PTT manually. With **Breakin** on (QSK), key edges trigger TX immediately and the break-in delay holds the relay open between elements. There is no longer an automatic PTT envelope that overrides this setting.

## Troubleshooting

- **No sidetone is audible** — Confirm **Sidetone** is enabled and **Sidetone volume** is above zero. Both the radio monitor and the client-side generator are controlled by these two controls.
- **Sidetone does not start on connect (Windows)** — This was resolved in v0.9.3 (#2105). Ensure you are running v0.9.3 or later.
- **Level gauge does not appear on connect** — If **Mic source** is set to **PC** or RADE mode is active, the gauge should appear immediately on connect. For other mic sources without RADE, the gauge is suppressed when `met_in_rx` is off and the radio is not transmitting.
- **Compression gauge shows 0 dB during receive** — This is expected behavior from v0.9.7 onward. The gauge is gated on the radio's interlock TRANSMITTING state and only shows a value while transmitting with the speech processor enabled.
- **Breakin does not engage QSK** — Confirm **Breakin** is enabled in the CW sub-panel. From v0.9.7, the keyboard and MIDI keying paths fully honor this setting; no automatic PTT envelope overrides it.
- **Pitch change has no effect** — Confirm the active slice is in a CW mode. The CW sub-panel and its pitch control are only active in CW modes.
- **CW sub-panel is not visible** — The active slice is not in a CW mode. Switch the slice to CW; the applet switches automatically.
- **Mic gain slider does not update the radio in RADE mode** — This is correct. In RADE mode the slider controls client-side RADE gain only and stores the value in `PcMicGain`. The radio's mic level setting is not affected.

## Related

- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)