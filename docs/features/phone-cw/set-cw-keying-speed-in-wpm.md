# Set CW keying speed in WPM

Use this page to adjust how fast AetherSDR keys the radio in CW mode. Speed is set in words per minute (WPM) and sent directly to the FLEX-8600.

## Before you start

- AetherSDR must be connected to the radio. The P/CW applet requires an active radio connection.
- The active slice must be in a CW mode. The Phone/CW applet automatically switches to the CW sub-panel when the slice is in CW mode; the Speed slider is only visible there.

## Steps

1. Click the **P/CW** tray button in the right sidebar to open the Phone/CW applet, if it is not already visible.
2. Confirm the CW sub-panel is showing. If the active slice is in CW mode, the applet displays CW controls including **Speed (CW)**, **Delay (CW)**, and **ALC**. If you see the microphone controls instead, switch the active slice to a CW mode first.
3. Drag the **Speed (CW)** slider to the desired WPM value. The valid range is 5–100 WPM.

## What each control does

| Control | Kind | Default | Range | Persisted key |
|---|---|---|---|---|
| Speed (CW) | Slider | — | 5–100 WPM | — |

The **Speed (CW)** slider sets the CW keying speed on the radio. Changes take effect immediately and apply to paddle, straight key, and CWX transmissions.

## Tips

- The Speed slider has no persisted setting key. The value is held by the radio firmware; AetherSDR reads it back from the radio on reconnect.
- If you use the local sidetone (**Local STn**), it tracks the radio keying speed automatically — no separate adjustment is needed.

## Troubleshooting

- **CW sub-panel is not visible** — The applet shows Phone controls when the active slice is not in CW mode. Switch the slice mode to CW, and the applet will automatically display the CW controls including **Speed (CW)**.
- **Slider appears but does not respond** — Verify the radio connection is active. The P/CW applet requires a live radio connection to send speed changes.

## Related

- [Set CW break-in delay](set-cw-break-in-delay.md)
- [Enable iambic paddle keying](enable-iambic-paddle-keying.md)
- [Change CW pitch / sidetone frequency](change-cw-pitch-sidetone-frequency.md)
- [Enable the low-latency local CW sidetone (Local STn) for fast paddle / straight-key / CWX work](enable-the-low-latency-local-cw-sidetone-local-stn-for-fast-paddle-straight-key-cwx-work.md)
- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)
