# Set CW break-in delay

The CW break-in delay controls how long the radio waits after the last keypress before returning to receive. Adjusting this prevents choppy QSK switching while still allowing a fast return to RX between words or characters.

## Before you start

- AetherSDR must be connected to the radio. The Phone/CW applet shows controls only when a radio connection is active.
- The active slice must be in a CW mode. The CW sub-panel replaces the Phone sub-panel automatically when CW is selected on the active slice.

## Steps

1. Locate the **P/CW** tray button in the right sidebar and confirm the applet is visible. If the applet is not visible, click the **P/CW** tray button to show it.
2. Confirm the CW sub-panel is displayed. If the Phone controls are showing instead, switch the active slice to a CW mode using the mode selector in the main VFO area.
3. Locate the **Delay (CW)** slider in the CW sub-panel.
4. Drag the **Delay (CW)** slider left to decrease the delay or right to increase it. The value is applied to the radio immediately.

## What each control does

| Control    | Description                                                                                                   | Valid range         |
|------------|---------------------------------------------------------------------------------------------------------------|---------------------|
| Delay (CW) | Sets the CW break-in delay. The radio returns to receive this many milliseconds after the last keyed element. | 0–2000 ms (step 10) |
| Breakin    | Toggles full break-in (QSK). With **Breakin** ON, key edges trigger TX and the break-in delay holds the relay before returning to receive. With **Breakin** OFF, keyed characters are queued and the operator engages PTT manually. | On / Off |

## Tips

- A delay of 0 ms with **Breakin** enabled gives full QSK operation. Increase the delay to reduce relay wear during fast sending.
- The **Delay (CW)** slider steps in 10 ms increments. For fine adjustment, click the slider track and use the arrow keys (if keyboard shortcuts are enabled under `View > Keyboard Shortcuts`).

## Notes for v0.9.7

- **Breakin behavior corrected:** The **Breakin** toggle now fully controls whether the CW keyboard and MIDI keying paths trigger TX automatically. Previously, an internal auto-PTT envelope overrode the **Breakin OFF** state and suppressed QSK hang time. That envelope has been removed. With **Breakin** OFF, keys queue characters and PTT must be engaged manually; with **Breakin** ON, key edges trigger TX immediately and `break_in_delay` governs the relay hang time.
- **Compression gauge gated on transmit state:** The **Compression** gauge in the Phone sub-panel now reads 0 dB during receive. It only shows a non-zero value when the radio's interlock reports TRANSMITTING and the speech processor is enabled. This prevents stale readings from the TX chain appearing while you are listening.
- **Mic gain slider in RADE mode:** When RADE mode is active, the **Mic gain** slider acts as a client-side RADE gain control and uses the `PcMicGain` setting, the same key used for PC mic source. The slider value is no longer sent to the radio as `mic_level` while RADE is active, which would otherwise silently overwrite the hardware mic setting. When RADE mode is deactivated, the slider reverts to reflecting the radio's reported mic level.
- **Level gauge in RADE mode:** When RADE mode is active the **Level** gauge remains live during receive (it does not require `met_in_rx` to be set), consistent with the existing PC mic source behavior. When RADE mode is deactivated the gauge resets to −150 dBFS.

## Notes for v0.9.3

- **Level gauge (Phone panel):** When the mic source is set to **PC**, the Level gauge now appears immediately on connect without waiting for the radio's `met_in_rx` flag to be set. This is because PC mic metering runs client-side and is independent of `met_in_rx`. For all other mic sources the previous suppression behavior is unchanged: the gauge reads −150 dBFS when `met_in_rx` is off and the radio is not transmitting.
- **VOX / Phone panel refresh:** VOX setters now emit `phoneStateChanged`, so the Phone sub-panel updates instantly when VOX is toggled via a keyboard shortcut. No manual panel interaction is needed to see the current VOX state.
- **Sidetone on Windows:** The CW sidetone stream (low-latency `CwSidetoneGenerator`) now starts immediately on connect on Windows. If you previously had to toggle **Sidetone** off and on after connecting to hear the local sidetone, this workaround is no longer needed.

## Related

- [Enable iambic paddle keying](enable-iambic-paddle-keying.md)
- [Set CW keying speed in WPM](set-cw-keying-speed-in-wpm.md)
- [Change CW pitch / sidetone frequency](change-cw-pitch-sidetone-frequency.md)
- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)