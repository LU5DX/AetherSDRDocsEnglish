# Phone/CW Applet

## Overview

The Phone/CW applet is a mode-aware transmit panel that shows microphone, processor, and monitor controls in voice modes, and automatically switches to CW controls (delay, speed, sidetone, iambic, pitch) when the active slice is in CW mode. In v0.9.8, the four CW value labels (Delay, Speed, Sidetone Volume, Pitch) are now QLineEdit widgets with QIntValidator — click any value and type a number directly (SmartSDR parity). The single Sidetone toggle and volume slider drive both the radio's DAX-fed monitor and the client-side low-latency sidetone (CwSidetoneGenerator, ~10 ms latency) in lockstep — pitch and pan always follow the radio's cw_pitch and mon_pan_cw settings automatically (v0.9.1+). In v0.9.7, the Compression gauge is now gated on the radio's interlock TRANSMITTING state (not meter flow), so it reads 0 during RX; Breakin now fully honors the radio's break_in setting — no auto-PTT envelope forces TX any more; the sidetone bus is shared with Quindar tones (mutually exclusive at the mode level).

## Phone Controls

| Control        | Kind          | Description                                                                   | Default | Range               |
|----------------|---------------|-------------------------------------------------------------------------------|---------|---------------------|
| Level          | Meter         | Microphone input peak level in dBFS. Suppressed to -150 when met_in_rx is off and not transmitting. | —       | -40 to +10 dBFS (red > 0) |
| Compression    | Meter         | Speech compression amount in dB (reversed fill). Gated on radio interlock TRANSMITTING state and speech processor enable; reads 0 dB during RX. | —       | -25 to 0 dB         |
| Mic profile    | Combo box     | Load named mic processing profile; calls TransmitModel::loadMicProfile.       | —       | Populated from radio micProfileList() |
| Mic source     | Combo box     | Select microphone input source; calls TransmitModel::setMicSelection.         | —       | MIC, BAL, LINE, ACC, PC (plus any from micInputList()) |
| Mic gain       | Slider        | Adjust mic input level. For 'PC' source uses local PcMicGain persistence (radio reports mic_level=0 when source=PC). | 50      | 0-100               |
| +ACC           | Toggle button | Enable the accessory mic input mix; calls TransmitModel::setMicAcc.          | —       | —                   |
| PROC           | Toggle button | Toggle the speech processor; calls TransmitModel::setSpeechProcessorEnable.   | —       | —                   |
| NOR/DX/DX+     | Slider        | Three-position processor level; calls TransmitModel::setSpeechProcessorLevel. | 0       | 0 (NOR), 1 (DX), 2 (DX+) |
| DAX            | Toggle button | Enable DAX as the TX audio source; calls TransmitModel::setDax.               | —       | —                   |
| MON            | Toggle button | Enable TX sidetone monitor; calls TransmitModel::setSbMonitor.                | —       | —                   |
| Monitor volume | Slider        | Set sideband monitor volume; calls TransmitModel::setMonGainSb.               | —       | 0-100               |

## CW Controls

| Control               | Kind          | Description                                                                                                                               | Default | Range               |
|------------------------|---------------|-------------------------------------------------------------------------------------------------------------------------------------------|---------|---------------------|
| ALC                   | Meter         | Automatic level control reading.                                                                                                         | —       | 0-100 (red > 80)    |
| Delay (CW)            | Slider + QLineEdit | Set CW break-in delay. Click the value and type a number directly (0–2000). Calls TransmitModel::setCwDelay. In v0.9.8, setCwDelay caches the value immediately. | 500     | 0-2000 ms (step 10) |
| Speed (CW)            | Slider + QLineEdit | Set CW keying speed. Click the value and type a number directly (5–100). Calls TransmitModel::setCwSpeed.                              | 20      | 5-100 WPM           |
| Sidetone              | Toggle button  | Toggle CW sidetone monitor. Also enables/disables the client-side low-latency CwSidetoneGenerator in lockstep (v0.9.1+). Both the radio's DAX-fed monitor and the local PortAudio sidetone are controlled by this single button. Pitch and pan follow radio's cw_pitch and mon_pan_cw automatically. | —       | —                   |
| Sidetone volume        | Slider + QLineEdit | Set CW monitor volume. One slider controls both the radio-side (mon_gain_cw) and client-side sidetone volumes. Click the value and type a number directly (0–100). | 50      | 0-100               |
| L / R pan (CW)        | Slider        | Set CW monitor stereo pan. Also applies constant-power pan to the local sidetone generator (v0.9.1+). Double-click recenters to 50 (centre). | 50      | 0-100               |
| Breakin               | Toggle button  | Toggle full break-in (QSK). In v0.9.7, fully honors the radio's break_in setting: with Breakin ON key edges trigger TX and break_in_delay holds the relay; with Breakin OFF keys are queued and operator engages PTT manually. | —       | —                   |
| Iambic                | Toggle button  | Toggle iambic paddle keyer; calls TransmitModel::setCwIambic.                                                                             | —       | —                   |
| Pitch < / >           | QLineEdit with buttons | QLineEdit with < / > buttons (CwTriBtn). Type a value (100–6000) or click the buttons to step by 10 Hz. Calls TransmitModel::setCwPitch (v0.9.8, #2429). | 600     | 100-6000 Hz (step 10) |

## Indicators

| Indicator        | States         | Meaning                         |
|------------------|----------------|---------------------------------|
| Level gauge      | -40 .. +10 dBFS| Microphone peak level.          |
| Compression gauge| -25 .. 0 dB    | Speech compression amount (reversed fill). |
| ALC gauge        | 0..100         | Automatic level control (CW sub-panel).    |

# Enable iambic paddle keying

Enable the radio's built-in iambic keyer so that a dual-lever paddle connected to the FLEX-8600 keys CW using the iambic mode. This lets you set keying speed and break-in behavior from within AetherSDR.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- The active slice must be in a CW mode. The Phone/CW applet automatically switches to the CW sub-panel when a CW slice is active.
- A dual-lever paddle must be physically connected to the FLEX-8600's key jack.

## Steps

1. Click the **P/CW** tray button in the right sidebar to open the Phone/CW applet. If the applet is already visible, skip this step.
2. Confirm the CW sub-panel is showing. If the active slice is in CW mode, the applet displays CW controls including **Iambic**, **Speed (CW)**, **Delay (CW)**, and **Breakin**.
3. Click **Iambic** to enable the iambic paddle keyer. The button highlights when active.

## Tips

- For low-latency sidetone feedback when using a paddle, enable **Sidetone** in the CW sub-panel. The single **Sidetone** button and **Sidetone volume** slider control both the radio's DAX-fed monitor and the client-side low-latency sidetone (approximately 10 ms latency) in lockstep. Pitch and pan follow the radio's `cw_pitch` and `mon_pan_cw` settings automatically. On Windows, the sidetone stream now starts immediately on connect (v0.9.3, fix #2105). See [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md).
- Adjust **Speed (CW)** before enabling **Iambic** to avoid sending at an unexpected rate. See [Set CW keying speed in WPM](set-cw-keying-speed-in-wpm.md).
- If you want full QSK operation, also enable **Breakin**. In v0.9.7, **Breakin** is fully honored: with **Breakin** on, key edges trigger TX and `break_in_delay` holds the relay; with **Breakin** off, keys are queued and you engage PTT manually. The previous auto-PTT envelope that masked **Breakin** off and killed QSK hang time has been removed. To set a hang time instead, disable **Breakin** and set **Delay (CW)** to a non-zero value. See [Set CW break-in delay](set-cw-break-in-delay.md).
- In v0.9.8, the Delay (CW), Speed (CW), Sidetone volume, and Pitch values are now editable QLineEdit widgets. Click any value and type a number directly. The sliders update automatically when you finish editing, and vice versa.

## Troubleshooting

- **The CW sub-panel is not visible, only Phone controls appear** — The active slice is not in a CW mode. Switch the slice mode to CW or CW-USB/CW-LSB on the radio or in AetherSDR; the applet will switch automatically.
- **Iambic button is present but the paddle does not key** — Verify the paddle is connected to the correct key jack on the FLEX-8600. The iambic keyer is a radio-side function; AetherSDR sends the enable command but physical keying depends on the hardware connection.
- **The Level gauge does not appear after connecting with mic source set to PC** — In v0.9.3 the Level gauge appears immediately on connect when the mic source is PC (#2086). If the gauge is missing, confirm the mic source is set to **PC** in the **Mic source** selector and that you are running v0.9.3 or later. When the source is PC, the meter uses client-side metering and is not suppressed by the `met_in_rx` setting. The same client-side metering applies when RADE mode is active, and the Level gauge remains visible during RX in that case.
- **The Compression gauge shows a non-zero reading during receive** — In v0.9.7, the Compression gauge is gated on the radio's interlock TRANSMITTING state. It reads 0 dB during RX. If you see a non-zero reading at rest, confirm you are running v0.9.7 or later.
- **Breakin OFF does not queue keys correctly; PTT drops unexpectedly** — The auto-PTT envelope that previously overrode the **Breakin** setting was removed in v0.9.7. If you observe this behavior, confirm you are running v0.9.7 or later and that the radio's `break_in` setting matches the **Breakin** button state in the applet.

## Related

- [Set CW keying speed in WPM](set-cw-keying-speed-in-wpm.md)
- [Set CW break-in delay](set-cw-break-in-delay.md)
- [Change CW pitch / sidetone frequency](change-cw-pitch-sidetone-frequency.md)
- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)