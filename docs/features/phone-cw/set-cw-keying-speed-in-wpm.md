# Set CW keying speed in WPM

Use the Speed slider in the Phone/CW applet to set how fast the radio keys CW, measured in words per minute. This controls the radio's internal keyer and affects paddle, straight-key, and CWX transmissions.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- The active slice must be in a CW mode. The Phone/CW applet shows the CW sub-panel only when the active slice is in CW mode; otherwise the Phone panel is displayed.
- Open the Phone/CW applet by clicking the P/CW tray button in the right sidebar, or confirm it is already visible.

## Steps

1. Verify that the active slice is in a CW mode. The applet automatically switches to the CW sub-panel when CW mode is active.
2. Locate the **Speed (CW)** slider in the CW sub-panel.
3. Drag the **Speed (CW)** slider left to decrease WPM or right to increase WPM. The valid range is 5–100 WPM.
4. Alternatively, click the numeric value adjacent to the slider and type a value directly (5–100) using your keyboard. The slider updates to match your typed value.

## What each control does

| Control           | Description                                                                                                                                                       | Default                                                                                                                  |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| Speed (CW)        | Sets CW keying speed; calls TransmitModel::setCwSpeed. The adjacent QLineEdit accepts typed values (5–100) (v0.9.8, #2429).                                       | 20 WPM                                                                                                                   |
| ALC (Phone panel) | Shows automatic level control reading from MeterModel::swAlcChanged (post-software-ALC SSB peak in dBFS). Fills right-to-left: empty at -20 dBFS, full at 0 dBFS. | Rewired from HWALC (RCA voltage) to SW ALC meter in v26.5.1 (#2552). Mirrored by an identical gauge on the CW sub-panel. |
| ALC (CW panel)    | Mirrors the Phone-panel ALC gauge; both read from MeterModel::swAlcChanged for consistent readings across voice and CW.                                           | Added in v26.5.1 (#2552) as part of the SW ALC meter split. Uses HGauge::setFillFromRight mode.                          |

## Tips

- The Speed (CW) slider operates the radio's keyer speed. Changes take effect immediately and apply to the paddle, straight key, and any CWX text transmissions.
- The four CW value labels (Delay, Speed, Sidetone Volume, Pitch) are now QLineEdit widgets with QIntValidator. Click any value and type a number directly for SmartSDR parity (v0.9.8).
- The **Sidetone** toggle and **Sidetone volume** slider control both the radio's DAX-fed monitor and the client-side low-latency sidetone in lockstep. Adjusting speed does not affect sidetone pitch; pitch always follows the radio's `cw_pitch` setting automatically.
- The **Level** gauge appears immediately on connect when the mic source is set to PC, or when RADE mode is active. In both cases the gauge uses client-side metering and is not suppressed by the `met_in_rx` setting, even when not transmitting. When RADE mode is active, the gauge continues to show level during RX.
- The **Compression** gauge reads 0 dB during RX. It only shows a non-zero value while the radio's interlock reports a TRANSMITTING state and the speech processor is enabled, preventing stale TX-chain readings from appearing during receive (v0.9.7).
- The **Mic gain** slider behaves differently when RADE mode is active: it acts as client-side RADE gain and stores its value under `PcMicGain` rather than sending a mic level command to the radio. This prevents silently overwriting the hardware mic setting. The same `PcMicGain` setting is shared between PC source mode and RADE mode.
- The **Breakin** toggle fully controls whether CW keyboard and MIDI key edges trigger TX. With Breakin on (QSK), key edges trigger TX and the break-in delay holds the relay. With Breakin off, keys are queued and you engage PTT manually. No automatic PTT envelope overrides this behavior (v0.9.7).
- The **Delay (CW)** slider value is cached immediately when changed, preventing the radio emission from snapping the slider back (v0.9.8, #2428).
- The sidetone bus is shared with Quindar tones (mutually exclusive at the mode level).
- The ALC gauge appears on both the Phone and CW sub-panels. Both gauges read from the same MeterModel::swAlcChanged source, so SSB operators watching mic gain see the same indicator CW operators use to verify clean keying envelope shape (v26.5.1, #2552). The previous HWALC meter (RCA voltage path) has been removed.

## Related

- [Set CW break-in delay](set-cw-break-in-delay.md)
- [Enable iambic paddle keying](enable-iambic-paddle-keying.md)
- [Change CW pitch / sidetone frequency](change-cw-pitch-sidetone-frequency.md)
- [Set sidetone volume](set-sidetone-volume.md)
- [Toggle CW sidetone](toggle-cw-sidetone.md)