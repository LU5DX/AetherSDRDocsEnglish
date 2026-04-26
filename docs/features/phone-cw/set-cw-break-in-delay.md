# Set CW break-in delay

Set how long the radio waits after the last keypress before returning to receive. A longer delay prevents choppy RX switching during fast sending; a shorter delay (or full QSK) minimizes receive dead time.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- The active slice must be in a CW mode. The Phone/CW applet automatically switches to its CW sub-panel when CW mode is selected; the Delay slider is only visible there.

## Steps

1. If the Phone/CW applet is not visible, click the **P/CW** tray button on the right sidebar to open it.
2. Confirm the CW sub-panel is showing. If you see mic and processor controls instead, your active slice is not in CW mode — change the slice mode first.
3. Locate the **Delay** slider in the CW sub-panel.
4. Drag the **Delay** slider left to decrease the delay or right to increase it. The value updates the radio in real time.
5. To use full break-in (QSK) with no delay, click **Breakin** to toggle it on. When **Breakin** is active, the radio switches to receive immediately after each element.

## What each control does

| Control | Kind | Default | Valid range | Persisted setting |
|---|---|---|---|---|
| **Delay** | Slider | — | 0–2000 ms, step 10 | none |
| **Breakin** | Toggle button | — | On / Off | none |

**Delay** — Sets the CW break-in delay in milliseconds. At 0 ms the radio attempts to return to receive as quickly as possible between elements. At 2000 ms the radio holds transmit for two full seconds after the last key event.

**Breakin** — Enables full QSK operation. When on, the radio switches between transmit and receive within each inter-element gap.

## Tips

- Delay and Breakin work together. If **Breakin** is off, the **Delay** value determines hold time. If **Breakin** is on, the radio ignores the delay and goes full QSK.
- If relay switching noise or amplifier sequencing is a concern, set a longer delay rather than enabling **Breakin**.

## Related

- [Set CW keying speed in WPM](set-cw-keying-speed-in-wpm.md)
- [Enable iambic paddle keying](enable-iambic-paddle-keying.md)
- [Change CW pitch / sidetone frequency](change-cw-pitch-sidetone-frequency.md)
- [Enable the low-latency local CW sidetone (Local STn) for fast paddle / straight-key / CWX work](enable-the-low-latency-local-cw-sidetone-local-stn-for-fast-paddle-straight-key-cwx-work.md)
