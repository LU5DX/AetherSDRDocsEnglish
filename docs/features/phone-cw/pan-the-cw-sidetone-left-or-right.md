# Phone/CW Applet

The Phone/CW applet displays transmit controls that are automatically selected based on the active slice mode. When the active slice is in a phone mode (AM, FM, SSB), the applet shows microphone and speech processor controls. When the active slice is in a CW mode, it automatically switches to CW controls (delay, speed, sidetone, iambic, pitch).

## Opening the Phone/CW applet

1. Click the **P/CW** tray button in the right sidebar.

The applet panel opens and displays the appropriate controls for the current slice mode.

## Phone panel controls

### Mic Level Meter

Shows the microphone input peak level in dBFS (-40 to +10 dBFS, red above 0 dBFS).

The meter is suppressed to -150 when `met_in_rx` is off and the radio is not transmitting.

### Compression Meter

Shows speech compression amount in dB (-25 to 0 dB, with reversed fill).

The gauge is gated on the radio's interlock TRANSMITTING state. During receive, the gauge reads 0 dB regardless of any residual meter data from the TX chain. The gauge only shows a compression reading while the radio is actively transmitting with the speech processor enabled. This prevents stale or misleading readings from appearing when you are not on the air.

### Mic Profile

Select the microphone processing profile. Click the combo box and choose a profile from the list, which is populated from the radio's available mic profiles.

### Mic Source

Select the microphone input source. Click the combo box and choose from MIC, BAL, LINE, ACC, PC, or any additional sources provided by the radio.

### Mic Gain

Adjust the microphone input level. Drag the slider to set the level from 0 to 100.

For the "PC" source, the value is stored locally in the `PcMicGain` setting. The radio always reports `mic_level=0` when the source is PC.

### +ACC

Enable or disable the accessory microphone input mix. Click **+ACC** to toggle.

### PROC

Enable or disable the speech processor. Click **PROC** to toggle.

### NOR/DX/DX+ Processor Level

Set the speech processor level. Drag the slider to one of three positions: 0 (NOR), 1 (DX), or 2 (DX+).

### DAX

Enable or disable DAX as the TX audio source. Click **DAX** to toggle.

### MON

Enable or disable the TX sidetone monitor. Click **MON** to toggle.

### Monitor Volume

Adjust the sideband monitor volume. Drag the slider to set the volume from 0 to 100.

### ALC Meter

Shows automatic level control reading on the CW panel. Range is 0 to 100, with red above 80.

## RADE mode and the mic level slider (v0.9.7)

When RADE mode is active, the **Mic gain** slider acts as a client-side RADE gain control rather than sending `mic_level` to the radio. The slider value is stored in `PcMicGain` — the same setting used when the mic source is **PC** — and is not forwarded to the radio while RADE is active. This prevents the RADE gain adjustment from silently overwriting the hardware mic level setting on the radio.

The **Level** meter remains active during RX when RADE is in use, allowing you to monitor your input level before transmitting ("Level Meter During Receive" behavior). When RADE mode is deactivated, the Level gauge is suppressed and the slider reverts to showing the radio's reported mic level.

## CW panel controls

### Delay

Set the CW break-in delay. Drag the slider or type a value directly in the adjacent text field:

- **Slider range:** 0 to 2000 ms (step 10)
- **Text field range:** 0 to 2000 ms (type a number and press Enter)
- **Default:** 500 ms

Click the text field, type the desired delay value, and press Enter. The slider updates to match the typed value.

> v0.9.8: The delay value field is now a QLineEdit with a QIntValidator (0–2000). The `setCwDelay` call was fixed to cache the value immediately so the radio emission doesn't snap the slider back (#2428).

### Speed

Set the CW keying speed. Drag the slider or type a value directly in the adjacent text field:

- **Slider range:** 5 to 100 WPM
- **Text field range:** 5 to 100 WPM (type a number and press Enter)
- **Default:** 20 WPM

Click the text field, type the desired speed value, and press Enter. The slider updates to match the typed value.

> v0.9.8: The speed value field is now a QLineEdit with a QIntValidator (5–100).

### Sidetone

Enable or disable the CW sidetone monitor. Click **Sidetone** to toggle.

This single button controls both the radio's DAX-fed monitor and the client-side low-latency CwSidetoneGenerator (~10 ms latency) in lockstep. Pitch and pan always follow the radio's `cw_pitch` and `mon_pan_cw` settings automatically.

### Sidetone Volume

Adjust the CW monitor volume. Drag the slider or type a value directly in the adjacent text field:

- **Slider range:** 0 to 100
- **Text field range:** 0 to 100 (type a number and press Enter)
- **Default:** 50

Click the text field, type the desired volume value, and press Enter. The slider updates to match the typed value.

One slider controls both the radio-side (`mon_gain_cw`) and client-side sidetone volumes in lockstep.

> v0.9.8: The sidetone volume value field is now a QLineEdit with a QIntValidator (0–100).

### L / R pan (CW)

Pan the CW sidetone left or right in the stereo field. Drag the slider to adjust panning:

- **Range:** 0 (full left) to 100 (full right)
- **Default:** 50 (centre)
- **Double-click** the slider to recenter to 50.

The pan setting applies to both the radio's DAX-fed monitor and the client-side low-latency sidetone simultaneously. The pan position always follows the radio's `mon_pan_cw` setting. If another client or the radio itself changes `mon_pan_cw`, the slider updates automatically.

#### Steps to adjust pan

1. Open the Phone/CW applet if it is not already visible.
2. Confirm the applet shows the CW panel — the Sidetone, Delay, Speed, Breakin, Iambic, and Pitch controls must be visible. If the Phone panel is showing instead, switch the active slice to a CW mode.
3. Locate the **L / R pan (CW)** slider.
4. Drag the slider left to pan toward the left channel, or right to pan toward the right channel.
5. To return to centre, double-click the slider.

### Breakin

Toggle full break-in (QSK). Click **Breakin** to toggle.

The toggle now fully honors the radio's `break_in` setting:

- **Breakin ON (QSK):** key edges immediately trigger TX; the `break_in_delay` holds the relay open between elements and drops TX after the set delay.
- **Breakin OFF:** keyed characters are queued and sent only while PTT is held manually. The radio does not switch to TX automatically.

The previous auto-PTT envelope that forced TX regardless of the Breakin state and suppressed QSK hang time has been removed (v0.9.7).

### Iambic

Toggle iambic paddle keyer mode. Click **Iambic** to toggle.

### Pitch

Set the CW sidetone pitch. Type a value directly in the text field, or use the **<** and **>** buttons to adjust:

- **Text field range:** 100 to 6000 Hz (type a number and press Enter)
- **Step buttons:** Click **<** or **>** to decrease or increase by 10 Hz per click
- **Default:** 600 Hz

> v0.9.8: The pitch value field is now a QLineEdit with a QIntValidator (100–6000), with adjacent **<** and **>** buttons (CwTriBtn).

## Indicator reference

| Indicator | Reading range | Meaning |
|-----------|---------------|---------|
| Level gauge | -40 to +10 dBFS | Microphone peak level |
| Compression gauge | -25 to 0 dB reversed fill | Speech compression amount |
| ALC gauge | 0 to 100 | Automatic level control (CW) |

## What each control does

| Control | Default | Valid range |
|---------|---------|-------------|
| Level meter | — | -40 to +10 dBFS (red > 0) |
| Compression meter | — | -25 to 0 dB (reversed fill) |
| Mic profile | — | populated from radio micProfileList() |
| Mic source | — | MIC, BAL, LINE, ACC, PC |
| Mic gain | 50 | 0–100 |
| +ACC | — | toggle |
| PROC | — | toggle |
| NOR/DX/DX+ | 0 | 0 (NOR), 1 (DX), 2 (DX+) |
| DAX | — | toggle |
| MON | — | toggle |
| Monitor volume | — | 0–100 |
| ALC meter | — | 0–100 (red > 80) |
| Delay (CW) | 500 | 0–2000 ms (step 10) |
| Speed (CW) | 20 | 5–100 WPM |
| Sidetone | — | toggle |
| Sidetone volume | 50 | 0–100 |
| L / R pan (CW) | 50 | 0–100 |
| Breakin | — | toggle |
| Iambic | — | toggle |
| Pitch < / > | 600 | 100–6000 Hz (step 10) |

## Tips

- The applet panel automatically switches between Phone and CW views based on the active slice mode. If you do not see the expected controls, check the active slice mode.
- The sidetone bus is shared with Quindar tones (mutually exclusive at the mode level).
- The Compression gauge only shows readings while the radio is actively transmitting with the speech processor enabled.
- When RADE mode is active, the Mic gain slider controls client-side RADE gain, not the radio's mic level.

## Related

- [Enable the low-latency CW sidetone (Sidetone button drives both radio and local path)](enable-the-low-latency-cw-sidetone-sidetone-button-drives-both-radio-and-local-path.md)
- [Change CW pitch / sidetone frequency](change-cw-pitch-sidetone-frequency.md)
- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)