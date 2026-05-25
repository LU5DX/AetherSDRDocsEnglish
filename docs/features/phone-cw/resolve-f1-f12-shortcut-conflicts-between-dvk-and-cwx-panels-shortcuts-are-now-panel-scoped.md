# Phone/CW Applet

The Phone/CW applet is a mode-aware transmit panel that shows microphone/processor/monitor controls in voice modes and automatically switches to CW controls (delay, speed, sidetone, iambic, pitch) when the active slice is in CW mode.

## Before you start

- The applet requires a connected FLEX-8600 radio running firmware 4.2
- The active slice must be in a voice mode (for Phone panel) or CW mode (for CW panel)

## Opening the applet

1. Click the **P/CW** tray button on the right sidebar to open the Phone/CW applet.
2. The applet automatically switches between Phone and CW panels based on the active slice mode.

## Phone controls

When the active slice is in a voice mode, the applet shows the Phone panel with the following controls:

| Control | Type | Range | Behavior |
|---------|------|-------|----------|
| Level | Meter | -40 to +10 dBFS | Shows microphone input peak level. Suppressed to -150 when met_in_rx is off and not transmitting. |
| Compression | Meter | -25 to 0 dB (reversed fill) | Shows speech compression amount. Gated on radio's interlock TRANSMITTING state and speech processor enable. Reads 0 dB during RX. In v26.5.3, the compression gauge now reads the raw COMPPEAK value (0–25 dB of compression) and inverts it for display: 0 dB = no compression, -25 dB = full compression. |
| Mic profile | Combo box | Populated from radio | Loads the named mic processing profile. |
| Mic source | Combo box | MIC, BAL, LINE, ACC, PC | Selects microphone input source. |
| Mic gain | Slider | 0–100 | Adjusts mic input level. For "PC" source uses local PcMicGain persistence. |
| +ACC | Toggle | On/Off | Enables the accessory mic input mix. |
| PROC | Toggle | On/Off | Toggles the speech processor. |
| NOR/DX/DX+ | Slider | 0 (NOR), 1 (DX), 2 (DX+) | Three-position processor level. |
| DAX | Toggle | On/Off | Enables DAX as the TX audio source. |
| MON | Toggle | On/Off | Enables TX sidetone monitor. |
| Monitor volume | Slider | 0–100 | Sets sideband monitor volume. |
| ALC (Phone panel) | Meter | -20 to 0 dBFS | Shows automatic level control from software ALC meter. Fills right-to-left. |

## CW controls

When the active slice is in CW mode, the applet shows the CW panel with the following controls:

| Control | Type | Range | Behavior |
|---------|------|-------|----------|
| Delay | Slider | 0–2000 ms (step 10) | Sets CW break-in delay. Adjacent QLineEdit accepts typed values (0–2000). |
| Speed | Slider | 5–100 WPM | Sets CW keying speed. Adjacent QLineEdit accepts typed values (5–100). |
| Sidetone | Toggle | On/Off | Toggles CW sidetone monitor. Controls both radio's DAX-fed monitor and client-side low-latency sidetone generator in lockstep. On v26.5.3, the CW sidetone routes to the user-selected audio output instead of the default output (#2899). |
| Sidetone volume | Slider | 0–100 | Sets CW monitor volume. Adjacent QLineEdit accepts typed values (0–100). |
| L / R pan | Slider | 0–100 | Sets CW monitor stereo pan. Double-click recenters to 50 (centre). |
| Breakin | Toggle | On/Off | Toggles full break-in (QSK). Fully honors the radio's break_in setting — no auto-PTT envelope forces TX. |
| Iambic | Toggle | On/Off | Toggles iambic paddle keyer. |
| Pitch < / > | Text field | 100–6000 Hz (step 10) | QLineEdit with < / > buttons. Type a value or click buttons to step by 10 Hz. |
| ALC (CW panel) | Meter | -20 to 0 dBFS | Mirrors the Phone-panel ALC gauge. Both read from MeterModel::swAlcChanged. |

## Common controls

| Control | Type | Range | Behavior |
|---------|------|-------|----------|
| ALC gauge | Meter | -20 to 0 dBFS (fill from right) | Shows automatic level control. Both Phone and CW panels display identical ALC readings. In v26.5.3, both ALC gauges now initialize to -20 dBFS (empty) instead of 0 dBFS (full) when the applet first opens. |

## F1-F12 shortcut scoping

- The embedded CWX panel scopes its F1-F12 shortcuts to panel visibility (#2464, #2469)
- DVK panel F-key bindings and CWX hotkeys no longer fire simultaneously
- CWX macros automatically release TX when the queue drains (#2450, #2507)

## Notes

- The level meter is now properly suppressed during receive when the user disables "Level Meter During Receive" (met_in_rx), regardless of mic source. The applyLevelMeterReceiveGate() method handles this consistently for all mic sources including PC and RADE paths.
- The compression gauge in v26.5.3 reads the raw COMPPEAK value (0–25 dB of compression) and inverts it for display: 0 dB = no compression, -25 dB = full compression. This provides a more accurate representation of the actual compression amount.
- Both ALC gauges now initialize to kAlcGaugeFloorDbfs (-20 dBFS) when the applet is first built, preventing the display of stale 0 dBFS readings during the initial rendering phase.