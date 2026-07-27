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
3. Watch the **Compression** gauge. The reversed fill shows how many dB of compression is being applied (range: −25 to 0 dB). Keep the reading out of the far left to avoid over-processing. Hover over the gauge to see the exact compression value in dB.
4. Watch the **Level** gauge to confirm microphone input is reaching the processor. The range is −40 to +10 dBFS; the meter goes red above 0 dBFS. Hover over the gauge to see the exact mic peak level in dB.
5. Watch the **ALC** gauge (Phone panel) to confirm the post-software-ALC level is in the normal operating range (−20 to 0 dBFS). The gauge fills from the right; excessive ALC pins at 0 dBFS. Hover over the gauge to see the exact ALC level in dBFS.
6. To disable the processor, click **PROC** again. The button returns to its unlit state.

## What each control does

| Control           | Kind                                                                                                                                                              | Default                                                                                                                  |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| **PROC**          | Toggle button                                                                                                                                                     | Off                                                                                                                      |
| **NOR/DX/DX+**    | Slider                                                                                                                                                            | 0 (NOR)                                                                                                                  |
| **Level**         | Meter                                                                                                                                                             | —                                                                                                                        |
| **Compression**   | Meter                                                                                                                                                             | —                                                                                                                        |
| **ALC (Phone panel)** | Meter showing automatic level control reading from MeterModel::swAlcChanged (post-software-ALC SSB peak in dBFS). Fills right-to-left: empty at -20 dBFS, full at 0 dBFS. Hover for exact dBFS reading. | Rewired from HWALC (RCA voltage) to SW ALC meter in v26.5.1 (#2552). Mirrored by an identical gauge on the CW sub-panel. |
| **ALC (CW panel)**    | Meter mirroring the Phone-panel ALC gauge; both read from MeterModel::swAlcChanged for consistent readings across voice and CW. Fills right-to-left: empty at -20 dBFS, full at 0 dBFS. Hover for exact dBFS reading. | Added in v26.5.1 (#2552) as part of the SW ALC meter split. Uses HGauge::setFillFromRight mode.                          |

## All applet controls

| Control               | Kind          | Default | Valid range       | Behavior |
|-----------------------|---------------|---------|-------------------|----------|
| **Level**             | Meter         | —       | −40 to +10 dBFS (red > 0) | Shows microphone input peak level in dBFS. Suppressed to −150 when met_in_rx is off and not transmitting. Hover for exact dB reading (v26.7.4). |
| **Compression**       | Meter         | —       | −25 to 0 dB (reversed fill) | Shows speech compression amount in dB. In v0.9.7, gated on the radio's interlock TRANSMITTING state and speech processor enable: reads 0 dB during RX. Hover for exact dB reading (v26.7.4). |
| **Mic profile**       | Combo box     | —       | Populated from radio micProfileList() | Loads the named mic processing profile. |
| **Mic source**        | Combo box     | —       | MIC, BAL, LINE, ACC, PC (plus any from micInputList()) | Selects microphone input source. When host modulation is active (radio is modulated by AetherSDR), the combo box is disabled and shows only "PC" with an explanatory tooltip. |
| **Mic gain**          | Slider        | 50      | 0–100           | Adjusts mic input level. For 'PC' source uses local PcMicGain persistence. |
| **+ACC**              | Toggle button | —       | —               | Enables the accessory mic input mix. |
| **PROC**              | Toggle button | —       | —               | Toggles the speech processor. |
| **NOR/DX/DX+**        | Slider        | 0       | 0 (NOR), 1 (DX), 2 (DX+) | Three-position processor level. |
| **DAX**               | Toggle button | —       | —               | Enables DAX as the TX audio source. |
| **MON**               | Toggle button | —       | —               | Enables TX sidetone monitor. |
| **Monitor volume**    | Slider        | —       | 0–100           | Sets sideband monitor volume. |
| **ALC (Phone panel)** | Meter         | —       | −20 to 0 dBFS (red > −3) | Shows automatic level control reading from MeterModel::swAlcChanged. Fills right-to-left. Hover for exact dBFS reading (v26.7.4). |
| **ALC (CW panel)**    | Meter         | —       | −20 to 0 dBFS (red > −3) | Mirrors the Phone-panel ALC gauge. Fills right-to-left. Hover for exact dBFS reading (v26.7.4). |
| **Delay (CW)**        | Slider + edit | 500     | 0–2000 ms        | Sets CW break-in delay. The adjacent QLineEdit accepts typed values (0–2000). |
| **Speed (CW)**        | Slider + edit | 20      | 5–100 WPM        | Sets CW keying speed. The adjacent QLineEdit accepts typed values (5–100). |
| **Sidetone**          | Toggle button | —       | —               | Toggles CW sidetone monitor. Also enables/disables the client-side low-latency CwSidetoneGenerator in lockstep. |
| **Sidetone volume**   | Slider + edit | 50      | 0–100           | Sets CW monitor volume. Also sets the local sidetone generator volume in lockstep. The adjacent QLineEdit accepts typed values (0–100). |
| **L / R pan (CW)**    | Slider        | 50      | 0–100           | Sets CW monitor stereo pan. Double-click recenters to 50 (centre). |
| **Breakin**           | Toggle button | —       | —               | Toggles full break-in (QSK). In v0.9.7, fully honors the radio's break_in setting. |
| **Iambic**            | Toggle button | —       | —               | Toggles iambic paddle keyer. |
| **Pitch < / >**       | Text + buttons| 600     | 100–6000 Hz      | QLineEdit with < / > buttons. Type a value (100–6000) or click the buttons to step by 10 Hz. |

## Tips

- Set your mic gain before enabling the processor. A healthy **Level** reading before enabling **PROC** gives the processor useful signal to work with. See [Adjust mic gain and enable the accessory mix](adjust-mic-gain-and-enable-the-accessory-mix.md).
- Start at **NOR** and move to **DX** or **DX+** only if signal reports warrant it. Heavy processing on strong signals sounds distorted to the receiving station.
- The **Compression** gauge reads 0 dB (no fill) when **PROC** is off, when the radio is not transmitting, or when no audio is present.
- Both **ALC** gauges (Phone and CW panels) use the same software ALC meter source. For SSB operation, target −10 to −5 dBFS on the ALC gauge for optimal transmit audio quality.
- Hover over any gauge (**Level**, **Compression**, or either **ALC** gauge) to see the exact numeric reading in a popup (v26.7.4). This allows you to read the precise value without having to estimate the gauge's fill position.

## Troubleshooting

- **PROC button is not visible** — The applet is showing the CW panel. The Phone panel, including **PROC**, appears only when the active slice is in a phone mode, not CW.
- **Compression gauge shows 0 dB with PROC on** — In v0.9.7 and later the **Compression** gauge is gated on the radio's interlock TRANSMITTING state: it intentionally reads 0 dB during receive to prevent stale readings from the TX chain. If the gauge still reads 0 dB while transmitting, the radio is not receiving audio from the selected mic source. Check the **Level** gauge and the **Mic source** setting. If **Mic source** is **PC**, the radio always reports mic level as 0; use the **Level** gauge in the applet instead.
- **NOR/DX/DX+ slider snaps back** — The slider has three valid positions (0, 1, 2). Dragging between snap points causes it to land on the nearest integer; this is expected behavior.
- **Mic source combo box is disabled and shows only "PC"** — This occurs when the radio is in host modulation mode (modulated by AetherSDR). The PC microphone is the only available input in this mode; other sources are FlexRadio jacks that do not apply. A tooltip explains this.
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
- Adjusting **Sidetone volume** sets both `mon_gain_cw` on the radio and