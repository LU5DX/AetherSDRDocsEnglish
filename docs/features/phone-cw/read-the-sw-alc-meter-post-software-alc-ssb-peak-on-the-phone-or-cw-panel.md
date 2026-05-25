# Read the SW ALC meter (post-software-ALC SSB peak) on the Phone or CW panel

This page shows you how to monitor the software Automatic Level Control (ALC) meter, which reads the post-software-ALC SSB peak in dBFS. This meter helps you set your microphone gain or CW keying envelope so you transmit at an appropriate level without overdriving the audio chain.

## Before you start

- Ensure your FLEX-8600 is connected and the active slice is in a voice mode (Phone) or CW mode.
- The Phone/CW applet must be visible in the right sidebar — toggle it on using the **P/CW** tray button if needed.

## Steps

1. Locate the **ALC** gauge on either the Phone or CW sub-panel. It reads **-20 to 0 dBFS**, filling from right to left.
2. Key the transmitter (or, for CW, begin sending).
3. Watch the ALC gauge needle while you adjust your microphone gain with the **Mic gain** slider:
   - The meter is empty (at **-20 dBFS**) when no ALC is applied.
   - The gauge fills toward **0 dBFS** as ALC increases.
   - The red zone begins at **-3 dBFS** (marked on the gauge).
4. For CW, the same ALC gauge appears on the CW sub-panel — it is identical and driven by the same meter source.

## What each control does

| Control | Label | Behavior | Valid range | Default | Setting key |
|---------|-------|----------|-------------|---------|-------------|
| ALC gauge (Phone panel) | **ALC** | Shows automatic level control reading from the software ALC meter (post-software-ALC SSB peak in dBFS). Fills right-to-left: empty at -20 dBFS, full at 0 dBFS. Red zone above -3 dBFS. Initialised to -20 dBFS on construction. | -20 to 0 dBFS | — | None |
| ALC gauge (CW panel) | **ALC** | Mirrors the Phone-panel ALC gauge; both read from the same software ALC meter for consistent readings across voice and CW. Initialised to -20 dBFS on construction. | -20 to 0 dBFS | — | None |

## What each Phone/CW control does

| Control | Label | Behavior | Valid range | Default | Setting key |
|---------|-------|----------|-------------|---------|-------------|
| Level meter | **Level** | Shows microphone input peak level in dBFS (Phone panel). Suppressed to -150 when **Level Meter During Receive** is off and not transmitting. | -40 to +10 dBFS (red > 0) | — | None |
| Compression meter | **Compression** | Shows speech compression amount in dB (Phone panel). Gated on the radio's interlock TRANSMITTING state and speech processor enable: reads 0 dB during RX. Conversion: MeterModel exposes COMPPEAK as positive 0..25 dB, the gauge displays reversed -25..0 dB. | -25 to 0 dB (reversed fill) | — | None |
| Mic profile | **Mic profile** | Loads a named mic processing profile from the radio. | Populated from radio micProfileList() | — | None |
| Mic source | **Mic source** | Selects the microphone input source. | MIC, BAL, LINE, ACC, PC (plus any from micInputList()) | — | None |
| Mic gain | **Mic gain** | Adjusts mic input level. For 'PC' source uses local PcMicGain persistence. | 0-100 | 50 | PcMicGain |
| +ACC | **+ACC** | Enables the accessory mic input mix. | — | — | None |
| PROC | **PROC** | Toggles the speech processor. | — | — | None |
| NOR/DX/DX+ | **NOR/DX/DX+** | Three-position processor level. | 0 (NOR), 1 (DX), 2 (DX+) | 0 | None |
| DAX | **DAX** | Enables DAX as the TX audio source. | — | — | None |
| MON | **MON** | Enables TX sidetone monitor. | — | — | None |
| Monitor volume | **Monitor volume** | Sets sideband monitor volume. | 0-100 | — | None |
| ALC gauge (Phone panel) | **ALC** | Shows automatic level control reading from MeterModel::swAlcChanged (post-software-ALC SSB peak in dBFS). Fills right-to-left: empty at -20 dBFS, full at 0 dBFS. Initialised to -20 dBFS on construction. | -20 to 0 dBFS (red > -3) | — | None |
| Delay (CW) | **Delay (CW)** | Sets CW break-in delay. The adjacent QLineEdit accepts typed values (0–2000). | 0-2000 ms (step 10) | 500 | None |
| Speed (CW) | **Speed (CW)** | Sets CW keying speed. The adjacent QLineEdit accepts typed values (5–100). | 5-100 WPM | 20 | None |
| Sidetone | **Sidetone** | Toggles CW sidetone monitor and the client-side low-latency CwSidetoneGenerator in lockstep. Routes to the user-selected audio output. | — | — | None |
| Sidetone volume | **Sidetone volume** | Sets CW monitor volume. Controls both radio-side (mon_gain_cw) and client-side sidetone volumes. The adjacent QLineEdit accepts typed values (0–100). | 0-100 | 50 | None |
| L / R pan (CW) | **L / R pan (CW)** | Sets CW monitor stereo pan. Applies constant-power pan to the local sidetone generator. Double-click recenters to 50 (centre). | 0-100 | 50 | None |
| Breakin | **Breakin** | Toggles full break-in (QSK). With Breakin ON key edges trigger TX; with Breakin OFF keys are queued and the operator engages PTT manually. | — | — | None |
| Iambic | **Iambic** | Toggles iambic paddle keyer. | — | — | None |
| Pitch < / > | **Pitch < / >** | QLineEdit with < / > buttons. Type a value (100–6000) or click the buttons to step by 10 Hz. | 100-6000 Hz (step 10) | 600 | None |
| ALC gauge (CW panel) | **ALC** | Mirrors the Phone-panel ALC gauge; driven from the same software ALC meter. Initialised to -20 dBFS on construction. | -20 to 0 dBFS (red > -3) | — | None |

## Notes

- In v26.5.3 both ALC gauges are initialised to -20 dBFS on construction, preventing a momentary full-scale reading at startup.
- The Compression gauge in v26.5.3 uses the MeterModel COMPPEAK value (positive 0..25 dB) and inverts it for the reversed -25..0 dB gauge display.
- The level meter suppression logic has been refactored in v26.5.3 into a dedicated `applyLevelMeterReceiveGate()` method, called when transmit state changes or the RADE active state changes.

## Related

- [Adjust mic gain and enable the accessory mix](adjust-mic-gain-and-enable-the-accessory-mix.md)
- [Set CW keying speed in WPM](set-cw-keying-speed-in-wpm.md)