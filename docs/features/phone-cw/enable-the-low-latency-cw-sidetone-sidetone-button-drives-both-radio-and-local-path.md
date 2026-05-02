# Enable the low-latency CW sidetone (Sidetone button drives both radio and local path)

Turning on the CW sidetone in AetherSDR enables two paths at once: the radio's DAX-fed monitor and a client-side tone generator with approximately 10 ms latency. A single button and a single volume slider control both in lockstep, so you hear a consistent tone regardless of network jitter.

## Before you start

- AetherSDR must be connected to the radio. The Phone/CW applet requires an active radio connection.
- The active slice must be in a CW mode. The applet panel automatically switches from the Phone sub-panel to the CW sub-panel when CW mode is detected.

## Steps

1. If the Phone/CW applet is not visible, click the **P/CW** tray button on the right sidebar to open it.
2. Confirm the CW sub-panel is displayed. If the Phone sub-panel is showing, switch the active slice to a CW mode on the radio; the panel switches automatically.
3. Click **Sidetone** to enable the sidetone. The button lights up when active.
4. Adjust the **Sidetone volume** slider to a comfortable level. The slider controls both the radio-side monitor volume and the client-side tone generator volume simultaneously.
5. Optionally, adjust **Pitch < / >** to set the sidetone frequency. The pitch follows the radio's `cw_pitch` setting automatically, but you can step it in 10 Hz increments using the **<** and **>** controls.

## What each control does

| Control | Kind | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|---|
| Sidetone | Toggle button | — | On / Off | — | Enables or disables the CW sidetone. Controls both the radio's DAX-fed monitor and the local low-latency tone generator in lockstep. |
| Sidetone volume | Slider | — | 0–100 | — | Sets the volume for both the radio-side monitor (`mon_gain_cw`) and the client-side tone generator simultaneously. |
| Pitch < / > | Spinbox | 600 Hz | 100–6000 Hz (step 10) | — | Steps the sidetone and decode pitch by 10 Hz. Automatically follows the radio's `cw_pitch` setting. |
| L / R pan (CW) | Slider | 50 (centre) | 0–100 | — | Sets stereo pan for both the radio-side monitor and the local tone generator. Double-click recenters to 50. |

## Tips

- The client-side tone generator pitch and pan always follow the radio's `cw_pitch` and `mon_pan_cw` settings automatically. You do not need to configure them separately for the local path.
- Double-clicking the **L / R pan (CW)** slider resets it to centre (50).

## Troubleshooting

- **No tone heard despite Sidetone being enabled** — Confirm the **Sidetone volume** slider is above 0. Also check that your system audio output device is correctly configured, as the client-side generator uses the local audio path.
- **Sidetone button is not visible** — The CW sub-panel only appears when the active slice is in CW mode. Switch the active slice to CW on the radio; the applet panel switches automatically.
- **Pitch does not match expectation** — Pitch follows the radio's `cw_pitch` setting. Adjust it using **Pitch < / >** in the applet, which updates the radio setting in 10 Hz steps.

## Related

- [Change CW pitch / sidetone frequency](change-cw-pitch-sidetone-frequency.md)
- [Pan the CW sidetone left or right](pan-the-cw-sidetone-left-or-right.md)
- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)
- [Set CW keying speed in WPM](set-cw-keying-speed-in-wpm.md)
- [Set CW break-in delay](set-cw-break-in-delay.md)
