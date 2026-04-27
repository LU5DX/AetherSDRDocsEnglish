# Enable iambic paddle keying

Enable the radio's built-in iambic keyer so that a dual-lever paddle connected to the FLEX-8600 keys CW using the iambic mode. This lets you set keying speed and break-in behavior from within AetherSDR.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- The active slice must be in a CW mode. The Phone/CW applet automatically switches to the CW sub-panel when a CW slice is active.
- A dual-lever paddle must be physically connected to the FLEX-8600's key jack.

## Steps

1. Click the **P/CW** tray button in the right sidebar to open the Phone/CW applet. If the applet is already visible, skip this step.
2. Confirm the CW sub-panel is showing. If the active slice is in CW mode, the applet displays CW controls including **Iambic**, **Speed (CW)**, **Delay (CW)**, and **Breakin**.
3. Click **Iambic** to enable the iambic paddle keyer. The button highlights when active.

## What each control does

| Control | Description | Default | Valid range | Setting key |
|---|---|---|---|---|
| **Iambic** | Toggles the iambic paddle keyer on the radio. | — | On / Off | — |
| **Speed (CW)** | Sets CW keying speed. | — | 5–100 WPM | — |
| **Delay (CW)** | Sets CW break-in delay. | — | 0–2000 ms (step 10) | — |
| **Breakin** | Toggles full break-in (QSK). | — | On / Off | — |
| **Pitch < / >** | Steps the CW sidetone and decode pitch by 10 Hz. | 600 Hz | 100–6000 Hz | — |

## Tips

- For low-latency sidetone feedback when using a paddle, enable **Local STn** in the same CW sub-panel. The client-side sidetone has approximately 10 ms latency, which is significantly less than the radio's DAX-fed monitor path. See [Enable the low-latency local CW sidetone (Local STn) for fast paddle / straight-key / CWX work](enable-the-low-latency-local-cw-sidetone-local-stn-for-fast-paddle-straight-key-cwx-work.md).
- Adjust **Speed (CW)** before enabling **Iambic** to avoid sending at an unexpected rate. See [Set CW keying speed in WPM](set-cw-keying-speed-in-wpm.md).
- If you want full QSK operation, also enable **Breakin**. To set a hang time instead, disable **Breakin** and set **Delay (CW)** to a non-zero value. See [Set CW break-in delay](set-cw-break-in-delay.md).

## Troubleshooting

- **The CW sub-panel is not visible, only Phone controls appear** — The active slice is not in a CW mode. Switch the slice mode to CW or CW-USB/CW-LSB on the radio or in AetherSDR; the applet will switch automatically.
- **Iambic button is present but the paddle does not key** — Verify the paddle is connected to the correct key jack on the FLEX-8600. The iambic keyer is a radio-side function; AetherSDR sends the enable command but physical keying depends on the hardware connection.

## Related

- [Set CW keying speed in WPM](set-cw-keying-speed-in-wpm.md)
- [Set CW break-in delay](set-cw-break-in-delay.md)
- [Enable the low-latency local CW sidetone (Local STn) for fast paddle / straight-key / CWX work](enable-the-low-latency-local-cw-sidetone-local-stn-for-fast-paddle-straight-key-cwx-work.md)
- [Change CW pitch / sidetone frequency](change-cw-pitch-sidetone-frequency.md)
- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)
