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

| Control | Default | Valid range | Behavior |
|---|---|---|---|
| L / R pan (CW) | 50 (centre) | 0–100 | Sets the stereo pan position for the CW sidetone. Applies constant-power pan to both the radio-side monitor (`mon_pan_cw`) and the client-side sidetone generator in lockstep. Double-click recenters to 50. |

## Tips

- The pan position always follows the radio's `mon_pan_cw` setting. If another client or the radio itself changes `mon_pan_cw`, the slider will update automatically.
- Double-clicking the slider is the fastest way to restore a centered sidetone without guessing the midpoint.

## Related

- [Enable the low-latency CW sidetone (Sidetone button drives both radio and local path)](enable-the-low-latency-cw-sidetone-sidetone-button-drives-both-radio-and-local-path.md)
- [Change CW pitch / sidetone frequency](change-cw-pitch-sidetone-frequency.md)
- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)
