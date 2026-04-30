# Enable the low-latency CW sidetone for fast paddle / straight-key / CWX work

The CW sidetone in AetherSDR operates at approximately 10 ms latency. As of v0.9.2.1, the local client-side sidetone is no longer a separate subsystem with its own controls. Instead, the single **Sidetone** button and **Sidetone volume** slider on the CW sub-panel control both the radio's DAX-fed monitor and the client-side low-latency tone generator (CwSidetoneGenerator) in lockstep. Pitch and pan always follow the radio's `cw_pitch` and `mon_pan_cw` settings automatically.

Use this feature when the radio's sidetone path introduces too much delay for comfortable paddle, straight-key, or CWX operation.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- The active slice must be in a CW mode. The Phone/CW applet automatically switches to its CW sub-panel when a CW slice is active.
- The Phone/CW applet must be visible in the Applet Panel. If it is not, click the **P/CW** tray button on the right sidebar.

## Steps

1. Open the Phone/CW applet by clicking the **P/CW** tray button on the right sidebar. The CW sub-panel appears automatically when the active slice is in CW mode.
2. Click **Sidetone** to enable the sidetone. Both the radio's DAX-fed monitor and the client-side low-latency tone generator are enabled together.
3. Adjust the **Sidetone volume** slider to a comfortable listening level (0–100). Both the radio-side monitor gain (`mon_gain_cw`) and the local sidetone generator volume change together.
4. To adjust stereo placement, drag the **L / R pan (CW)** slider (0–100, default 50 = centre). Double-click the slider to return it to centre. The pan value is applied to both the radio monitor and the local sidetone generator using constant-power panning.
5. To change the sidetone pitch, use the **Pitch < / >** spinbox (100–6000 Hz, step 10 Hz). Pitch always follows the radio's `cw_pitch` setting automatically.

## What each control does

| Control             | Default | Valid range           |
|---------------------|---------|-----------------------|
| **Sidetone**        | Off     | On / Off              |
| **Sidetone volume** | —       | 0–100                 |
| **L / R pan (CW)**  | 50      | 0–100                 |
| **Pitch < / >**     | 600 Hz  | 100–6000 Hz (step 10) |

## Tips

- The local sidetone works for CWX-generated text as well as paddle and straight-key input. No separate configuration is needed for CWX.
- Because pitch and pan follow the radio settings automatically, changing the **Pitch < / >** spinbox or `mon_pan_cw` on the radio always keeps the local sidetone in sync. There is no manual pitch override or follow toggle.
- The **Delay (CW)** slider (0–2000 ms, step 10) controls CW break-in delay and is independent of sidetone behaviour.

## Troubleshooting

- **Sidetone button is not visible** — The CW sub-panel only appears when the active slice is in a CW mode. Switch the slice mode to CW and the applet will update automatically.
- **No audio from the sidetone despite Sidetone being enabled** — Check that your system audio output device is configured and not muted. The local sidetone plays through the client system's audio, not the radio's speaker output. On Windows, if the sidetone does not start immediately after connecting, verify that no other application is holding exclusive access to the audio device; this initialization ordering issue was fixed in v0.9.3 (#2105).
- **Sidetone pitch is not what you expect** — Pitch follows the radio's `cw_pitch` setting. Adjust the **Pitch < / >** spinbox to change it.
- **Level gauge does not appear on connect** — If your mic source is set to **PC**, the Level gauge now appears immediately on connect as of v0.9.3 (#2086). If the gauge is still missing, confirm that the mic source is set to **PC** in the **Mic source** selector and that AetherSDR is connected to the radio.

## Related

- [Change CW pitch / sidetone frequency](change-cw-pitch-sidetone-frequency.md)
- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)
- [Enable iambic paddle keying](enable-iambic-paddle-keying.md)