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

| Control         | Description                                      | Default |
|-----------------|--------------------------------------------------|---------|
| **Iambic**      | Toggles the iambic paddle keyer on the radio.    | —       |
| **Speed (CW)**  | Sets CW keying speed.                            | —       |
| **Delay (CW)**  | Sets CW break-in delay.                          | —       |
| **Breakin**     | Toggles full break-in (QSK).                     | —       |
| **Pitch < / >** | Steps the CW sidetone and decode pitch by 10 Hz. | 600 Hz  |

## Tips

- For low-latency sidetone feedback when using a paddle, enable **Sidetone** in the CW sub-panel. The single **Sidetone** button and **Sidetone volume** slider control both the radio's DAX-fed monitor and the client-side low-latency sidetone (approximately 10 ms latency) in lockstep. Pitch and pan follow the radio's `cw_pitch` and `mon_pan_cw` settings automatically. On Windows, the sidetone stream now starts immediately on connect (v0.9.3, fix #2105). See [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md).
- Adjust **Speed (CW)** before enabling **Iambic** to avoid sending at an unexpected rate. See [Set CW keying speed in WPM](set-cw-keying-speed-in-wpm.md).
- If you want full QSK operation, also enable **Breakin**. To set a hang time instead, disable **Breakin** and set **Delay (CW)** to a non-zero value. See [Set CW break-in delay](set-cw-break-in-delay.md).

## Troubleshooting

- **The CW sub-panel is not visible, only Phone controls appear** — The active slice is not in a CW mode. Switch the slice mode to CW or CW-USB/CW-LSB on the radio or in AetherSDR; the applet will switch automatically.
- **Iambic button is present but the paddle does not key** — Verify the paddle is connected to the correct key jack on the FLEX-8600. The iambic keyer is a radio-side function; AetherSDR sends the enable command but physical keying depends on the hardware connection.
- **The Level gauge does not appear after connecting with mic source set to PC** — In v0.9.3 the Level gauge appears immediately on connect when the mic source is PC (#2086). If the gauge is missing, confirm the mic source is set to **PC** in the **Mic source** selector and that you are running v0.9.3 or later. When the source is PC, the meter uses client-side metering and is not suppressed by the `met_in_rx` setting.

## Related

- [Set CW keying speed in WPM](set-cw-keying-speed-in-wpm.md)
- [Set CW break-in delay](set-cw-break-in-delay.md)
- [Change CW pitch / sidetone frequency](change-cw-pitch-sidetone-frequency.md)
- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)