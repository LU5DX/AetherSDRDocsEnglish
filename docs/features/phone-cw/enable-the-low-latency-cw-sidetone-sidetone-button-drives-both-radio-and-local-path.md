# Enable the low-latency CW sidetone (Sidetone button drives both radio and local path)

Turning on the CW sidetone in AetherSDR enables two paths at once: the radio's DAX-fed monitor and a client-side tone generator with approximately 10 ms latency. A single button and a single volume slider control both in lockstep, so you hear a consistent tone regardless of network jitter.

## Before you start

- AetherSDR must be connected to the radio. The Phone/CW applet requires an active radio connection.
- The active slice must be in a CW mode. The applet panel automatically switches from the Phone sub-panel to the CW sub-panel when CW mode is detected.

## Steps

1. If the Phone/CW applet is not visible, click the **P/CW** tray button on the right sidebar to open it.
2. Confirm the CW sub-panel is displayed. If the Phone sub-panel is showing, switch the active slice to a CW mode on the radio; the panel switches automatically.
3. Click **Sidetone** to enable the sidetone. The button lights up when active.
4. Adjust the **Sidetone volume** slider to a comfortable level. The slider controls both the radio-side monitor volume and the client-side tone generator volume simultaneously.
5. Optionally, adjust **Pitch < / >** to set the sidetone frequency. The pitch follows the radio's `cw_pitch` setting automatically, but you can step it in 10 Hz increments using the **<** and **>** controls.

## What each control does

| Control         | Kind          | Default     |
|-----------------|---------------|-------------|
| Sidetone        | Toggle button | —           |
| Sidetone volume | Slider        | —           |
| Pitch < / >     | Spinbox       | 600 Hz      |
| L / R pan (CW)  | Slider        | 50 (centre) |

## RADE mode and the mic level slider

When RADE mode is active, the **Mic gain** slider operates as a client-side gain control rather than sending a mic level command to the radio. The slider value is stored under `PcMicGain` (the same setting used when the mic source is PC) and is not written to the radio's `mic_level` property while RADE is active. This prevents RADE mode from silently overwriting your hardware mic setting on the radio.

- The **Level** meter remains active during RX when RADE is enabled, so you can monitor input level without transmitting.
- When RADE mode is deactivated, the slider reverts to reflecting the radio's `mic_level` and the Level meter returns to its normal suppression behaviour (hidden during RX unless `met_in_rx` is on).

## Tips

- The client-side tone generator pitch and pan always follow the radio's `cw_pitch` and `mon_pan_cw` settings automatically. You do not need to configure them separately for the local path.
- Double-clicking the **L / R pan (CW)** slider resets it to centre (50).
- The **Compression** gauge reads 0 dB during RX. It only shows a non-zero value when the radio's interlock reports the TRANSMITTING state and the speech processor (**PROC**) is enabled. This prevents stale readings from the TX chain being displayed while you are receiving.
- With **Breakin** off, key presses are queued and TX must be engaged manually with PTT. With **Breakin** on (QSK), key edges trigger TX directly and `break_in_delay` controls the relay hang time. No automatic PTT envelope overrides this behaviour.

## Troubleshooting

- **No tone heard despite Sidetone being enabled** — Confirm the **Sidetone volume** slider is above 0. Also check that your system audio output device is correctly configured, as the client-side generator uses the local audio path.
- **Sidetone button is not visible** — The CW sub-panel only appears when the active slice is in CW mode. Switch the active slice to CW on the radio; the applet panel switches automatically.
- **Pitch does not match expectation** — Pitch follows the radio's `cw_pitch` setting. Adjust it using **Pitch < / >** in the applet, which updates the radio setting in 10 Hz steps.
- **Compression gauge always shows 0** — This is expected during RX. The gauge is gated on the radio's interlock TRANSMITTING state. It will show compression only while you are transmitting with **PROC** enabled.
- **Breakin OFF does not hold TX between characters** — With **Breakin** off, AetherSDR no longer applies an automatic PTT envelope. Engage PTT manually before sending and release it when finished.
- **Mic gain slider has no effect in RADE mode** — In RADE mode the slider sets client-side gain stored as `PcMicGain` and does not send commands to the radio. Adjust the slider to the desired level; it takes effect on the local RADE audio path.

## Related

- [Change CW pitch / sidetone frequency](change-cw-pitch-sidetone-frequency.md)
- [Pan the CW sidetone left or right](pan-the-cw-sidetone-left-or-right.md)
- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)
- [Set CW keying speed in WPM](set-cw-keying-speed-in-wpm.md)
- [Set CW break-in delay](set-cw-break-in-delay.md)