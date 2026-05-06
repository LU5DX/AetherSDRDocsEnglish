# Pan the CW sidetone left or right

Use the L / R pan control in the Phone/CW applet to shift the CW sidetone to the left or right stereo channel. The pan setting applies to both the radio's DAX-fed monitor and the client-side low-latency sidetone simultaneously.

## Before you start

- AetherSDR must be connected to the radio.
- The active slice must be in a CW mode so the CW panel is visible in the Phone/CW applet.
- Sidetone must be enabled. If it is not, click Sidetone in the Phone/CW applet to enable it.

## Steps

1. Click the **P/CW** tray button on the right sidebar to open the Phone/CW applet if it is not already visible.
2. Confirm the applet shows the CW panel — the Sidetone, Delay, Speed, Breakin, Iambic, and Pitch controls must be visible. If the Phone panel is showing instead, switch the active slice to a CW mode.
3. Locate the **L / R pan (CW)** slider.
4. Drag the slider left to pan the sidetone toward the left channel, or right to pan toward the right channel.
5. To return to centre, double-click the **L / R pan (CW)** slider.

## What each control does

| Control        | Default     | Valid range |
|----------------|-------------|-------------|
| L / R pan (CW) | 50 (centre) | 0–100       |

## Tips

- The pan position always follows the radio's `mon_pan_cw` setting. If another client or the radio itself changes `mon_pan_cw`, the slider will update automatically.
- Double-clicking the slider is the fastest way to restore a centered sidetone without guessing the midpoint.

## RADE mode and the mic level slider (v0.9.7)

When RADE mode is active, the **Mic gain** slider acts as a client-side RADE gain control rather than sending `mic_level` to the radio. The slider value is stored in `PcMicGain` — the same setting used when the mic source is **PC** — and is not forwarded to the radio while RADE is active. This prevents the RADE gain adjustment from silently overwriting the hardware mic level setting on the radio.

The **Level** meter remains active during RX when RADE is in use, allowing you to monitor your input level before transmitting ("Level Meter During Receive" behavior). When RADE mode is deactivated, the Level gauge is suppressed and the slider reverts to showing the radio's reported mic level.

## Compression gauge behavior (v0.9.7)

The **Compression** gauge is gated on the radio's interlock TRANSMITTING state. During RX the gauge reads 0 dB regardless of any residual meter data from the TX chain. The gauge only shows a compression reading while the radio is actively transmitting with the speech processor enabled. This prevents stale or misleading readings from appearing when you are not on the air.

## Breakin behavior (v0.9.7)

The **Breakin** toggle now fully honors the radio's `break_in` setting:

- **Breakin ON (QSK):** key edges immediately trigger TX; the `break_in_delay` holds the relay open between elements and drops TX after the set delay.
- **Breakin OFF:** keyed characters are queued and sent only while PTT is held manually. The radio does not switch to TX automatically.

The previous auto-PTT envelope that forced TX regardless of the Breakin state and suppressed QSK hang time has been removed.

## Related

- [Enable the low-latency CW sidetone (Sidetone button drives both radio and local path)](enable-the-low-latency-cw-sidetone-sidetone-button-drives-both-radio-and-local-path.md)
- [Change CW pitch / sidetone frequency](change-cw-pitch-sidetone-frequency.md)
- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)