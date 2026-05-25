# Enable speech processor at NOR, DX, or DX+ level

Turn on the FLEX-8600's built-in speech processor and choose how aggressively it compresses your transmitted audio. NOR gives mild compression; DX and DX+ increase processing for weaker-signal contacts.

## Before you start

- AetherSDR must be connected to the radio.
- The active slice must be in a phone mode (USB, LSB, AM, etc.). The Phone/CW applet shows Phone controls only when the active slice is not in CW mode.
- Open the Phone/CW applet by clicking the **P/CW** tray button on the right sidebar if it is not already visible.

## Steps

1. In the Phone/CW applet, click **PROC** to enable the speech processor. The button lights green when active.
2. Drag the **NOR/DX/DX+** slider to the desired compression level:
   - Position 0 — **NOR** (normal, least compression)
   - Position 1 — **DX**
   - Position 2 — **DX+** (most compression)
3. Watch the **Compression** gauge. The reversed fill shows how many dB of compression is being applied (range: −25 to 0 dB). Keep the reading out of the far left to avoid over-processing.
4. Watch the **Level** gauge to confirm microphone input is reaching the processor. The range is −40 to +10 dBFS; the meter goes red above 0 dBFS.
5. Watch the **ALC** gauge (Phone panel) to confirm the post-software-ALC level is in the normal operating range (−20 to 0 dBFS). The gauge fills from the right; excessive ALC pins at 0 dBFS.
6. To disable the processor, click **PROC** again. The button returns to its unlit state.

## What each control does

| Control           | Kind                                                                                                                                                              | Default                                                                                                                  |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| **PROC**          | Toggle button                                                                                                                                                     | Off                                                                                                                      |
| **NOR/DX/DX+**    | Slider                                                                                                                                                            | 0 (NOR)                                                                                                                  |
| **Level**         | Meter                                                                                                                                                             | —                                                                                                                        |
| **Compression**   | Meter                                                                                                                                                             | —                                                                                                                        |
| **ALC (Phone panel)** | Meter showing automatic level control reading from MeterModel::swAlcChanged (post-software-ALC SSB peak in dBFS). Fills right-to-left: empty at -20 dBFS, full at 0 dBFS. | Rewired from HWALC (RCA voltage) to SW ALC meter in v26.5.1 (#2552). Mirrored by an identical gauge on the CW sub-panel. |
| **ALC (CW panel)**    | Meter mirroring the Phone-panel ALC gauge; both read from MeterModel::swAlcChanged for consistent readings across voice and CW. Fills right-to-left: empty at -20 dBFS, full at 0 dBFS. | Added in v26.5.1 (#2552) as part of the SW ALC meter split. Uses HGauge::setFillFromRight mode.                          |

## Tips

- Set your mic gain before enabling the processor. A healthy **Level** reading before enabling **PROC** gives the processor useful signal to work with. See [Adjust mic gain and enable the accessory mix](adjust-mic-gain-and-enable-the-accessory-mix.md).
- Start at **NOR** and move to **DX** or **DX+** only if signal reports warrant it. Heavy processing on strong signals sounds distorted to the receiving station.
- The **Compression** gauge reads 0 dB (no fill) when **PROC** is off, when the radio is not transmitting, or when no audio is present.
- Both **ALC** gauges (Phone and CW panels) use the same software ALC meter source. For SSB operation, target −10 to −5 dBFS on the ALC gauge for optimal transmit audio quality.

## Troubleshooting

- **PROC button is not visible** — The applet is showing the CW panel. The Phone panel, including **PROC**, appears only when the active slice is in a phone mode, not CW.
- **Compression gauge shows 0 dB with PROC on** — In v0.9.7 and later the **Compression** gauge is gated on the radio's interlock TRANSMITTING state: it intentionally reads 0 dB during receive to prevent stale readings from the TX chain. If the gauge still reads 0 dB while transmitting, the radio is not receiving audio from the selected mic source. Check the **Level** gauge and the **Mic source** setting. If **Mic source** is **PC**, the radio always reports mic level as 0; use the **Level** gauge in the applet instead.
- **NOR/DX/DX+ slider snaps back** — The slider has three valid positions (0, 1, 2). Dragging between snap points causes it to land on the nearest integer; this is expected behavior.
- **Level gauge does not appear on connect** — If **Mic source** is **PC**, the **Level** gauge appears immediately on connect without requiring a transmit or `met_in_rx` to be active (v0.9.3, fix #2086). When RADE mode is active, the **Level** gauge also appears during receive (see [Level gauge behavior](#level-gauge-behavior-v093)). If the gauge is still absent, verify that **Mic source** is set to **PC** and that AetherSDR has finished connecting to the radio.
- **Phone panel does not refresh when VOX is toggled by keyboard shortcut** — This was resolved in v0.9.3 (#2084). Update to v0.9.3 or later if the Phone panel fails to update immediately when VOX is toggled via a keyboard shortcut.
- **ALC gauge shows unexpected values** — The ALC meters now read from the software ALC meter (MeterModel::swAlcChanged) in dBFS ranges. Values outside −20 to 0 dBFS are not displayed; the gauge simply pins at the nearest end. This replaces the previous HWALC path that produced meaningless readings.

## CW panel controls (v0.9.8)

In v0.9.8, the four value labels for CW parameters were replaced with QLineEdit widgets. The adjacent sliders and buttons remain unchanged. Click any value and type a number directly to set it. Values are clamped to the valid range when you press Enter or Tab.

| Control               | Kind          | Default | Valid range       |
|-----------------------|---------------|---------|-------------------|
| **Delay (CW)**        | Slider + edit | 500     | 0–2000 ms         |
| **Speed (CW)**        | Slider + edit | 20      | 5–100 WPM         |
| **Sidetone volume**   | Slider + edit | 50      | 0–100             |
| **Pitch < / >**       | Text + buttons| 600     | 100–6000 Hz       |

- The **Delay (CW)**, **Speed (CW)**, and **Sidetone volume** QLineEdit widgets use `QIntValidator` to restrict input to the valid range.
- The **Pitch < / >** widget (CwTriBtn) allows typing a value (100–6000) or clicking the < / > buttons to step by 10 Hz.
- The **Delay (CW)** slider was fixed in v0.9.8 (#2428) so that `setCwDelay` caches the value immediately, preventing the radio emission from snapping the slider back.
- The **Sidetone volume** slider controls both the radio-side (`mon_gain_cw`) and client-side sidetone generator volumes in lockstep.

## CW sidetone behavior (v0.9.1 and later)

The **Sidetone** toggle and **Sidetone volume** slider in the CW panel control both the radio's DAX-fed monitor and the client-side low-latency sidetone generator in lockstep. There is no longer a separate **Local STn** button, separate local volume slider, or **Follow** pitch toggle. Those controls have been removed.

- Enabling **Sidetone** turns on both the radio-side monitor and the client-side generator simultaneously.
- Adjusting **Sidetone volume** sets both `mon_gain_cw` on the radio and the local generator volume to the same value.
- Pitch and stereo pan always follow the radio's `cw_pitch` and `mon_pan_cw` settings automatically. No manual override or follow toggle is needed.
- On Windows, the sidetone audio stream now starts immediately on connect rather than requiring a manual action (v0.9.3, fix #2105).
- The sidetone bus is shared with Quindar tones. Sidetone and Quindar tones are mutually exclusive at the mode level.
- In v26.5.3, the CW sidetone routes to the user-selected audio output device instead of the default output device (#2899). No user action is required; the sidetone automatically follows the audio output selection in the application's audio settings.

If you have settings from a previous version that reference `CwLocalSidetoneEnabled`, `CwLocalSidetoneVolume`, `CwLocalSidetonePitchFollow`, or `CwLocalSidetonePitchHz`, those keys are no longer read or written by AetherSDR and can be ignored.

## Break-in behavior (v0.9.7)

The **Breakin** toggle now fully honors the radio's `break_in` setting.

- With **Breakin** on (QSK mode), key edges from the CW keyboard or MIDI keyer trigger transmit immediately; the `break_in_delay` value holds the relay open between characters as expected.
- With **Breakin** off, keyed characters are queued and the operator engages PTT manually. The previous auto-PTT envelope that forced transmit regardless of this setting, and that eliminated QSK hang time, has been removed.

## ALC gauge behavior (v26.5.1)

Starting with v26.5.1 (#2552), both the Phone panel and CW panel ALC gauges read from the software ALC meter (MeterModel::swAlcChanged) rather than the hardware ALC (HWALC) RCA voltage path. The HWALC path produced meaningless readings; the new path provides meaningful post-software-ALC SSB peak values in dBFS.

- Both gauges display a range of −20 to 0 dBFS.
- The fill direction is right-to-left: the gauge appears empty at −20 dBFS and fills toward the left as the level increases, reaching full at 0 dBFS.
- Excessive ALC pins at 0 dBFS.
- The gauges are mirrored: adjusting mic gain affects both gauges identically when operating in the respective mode.
- The gauges use `HGauge::setFillFromRight(true)` for proper visual rendering.

## Level gauge behavior (v0.9.3)

When **Mic source** is set to **PC**, the **Level** gauge uses client-side metering and is not suppressed by the radio's `met_in_rx` flag. The gauge appears immediately on connect and shows the PC microphone input level whether or not the radio is transmitting.

When RADE mode is active, the **Level** gauge behaves the same way: it uses client-side metering and is not suppressed by `met_in_rx`, so it shows the RADE input level during receive as well as transmit.

For all other mic sources with RADE inactive, the gauge is suppressed to −150 dBFS when `met_in_rx` is off and the radio is not transmitting.

## Level gauge behavior (v26.5.3)

In v26.5.3, the logic that suppresses the **Level** gauge during receive has been refactored into a dedicated `applyLevelMeterReceiveGate()` method. This replaces the inline suppression check in `updateMeters()`. The behavior is functionally identical to previous versions:

- When `met_in_rx` is off and the radio is not transmitting, the **Level** gauge is set to −150 dBFS regardless of the mic source. The previous exception for PC mic source and RADE mode has been removed — those sources are now also suppressed during receive when the level meter during receive is disabled.
- To show the **Level** gauge during receive for PC mic source or RADE mode, enable **Level Meter During Receive** in the radio's settings or the applet's settings.

## RADE mode behavior (v0.9.7)

When AetherSDR activates RADE mode, the Phone/CW applet adjusts several behaviors automatically. No manual steps are required.

- The **Mic gain** slider acts as a client-side RADE gain control. Its value is stored in `PcMicGain` and is not sent to the radio as `mic_level`. This prevents the slider from silently overwriting the hardware mic setting on the radio.
- The `PcMicGain` setting is shared between PC mic source and RADE mode. Both paths are client-authoritative; the radio does not report a mic level for either.
- The **Level** gauge shows RADE input level during receive (client-side metering, not gated by `met_in_rx`).
- When RADE mode deactivates, the applet resynchronizes the **Mic gain** slider from the radio's reported value, and the **Level** gauge reverts to standard suppression behavior for the active mic source.

## Compression gauge behavior (v26.5.3)

In v26.5.3, the **Compression** gauge calculation was updated to correctly interpret the raw COMPPEAK meter value from MeterModel. The gauge now expects a positive value (0–25 dB compression) and inverts it for the reversed-fill gauge display.

- The **Compression