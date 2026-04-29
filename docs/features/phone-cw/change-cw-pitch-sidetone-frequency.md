# Change CW pitch / sidetone frequency

The CW pitch control sets the tone frequency used for sidetone monitoring and CW decode. In v0.9.2.1, the separate local sidetone controls (Local STn button, local volume slider, Follow pitch button, and local pitch slider) have been removed. The single **Sidetone** toggle and **Sidetone volume** slider now drive both the radio's DAX-fed monitor and the client-side low-latency sidetone generator in lockstep. Pitch and pan always follow the radio's `cw_pitch` and `mon_pan_cw` settings automatically.

## Before you start

- Connect to a FLEX-8600 radio. The Phone/CW applet requires an active radio connection.
- Set the active slice to a CW mode. The CW sub-panel is only visible when the active slice is in CW mode; the Phone sub-panel is shown otherwise.
- Open the Phone/CW applet by clicking the **P/CW** tray button in the right sidebar if it is not already visible.

## Steps

### Change the radio CW pitch

1. Locate **Pitch < / >** in the CW sub-panel. It is a spinbox with two arrow buttons.
2. Click **<** to decrease the pitch by 10 Hz, or **>** to increase it by 10 Hz.
3. The new pitch is sent to the radio immediately. Valid range: 100–6000 Hz, step 10 Hz. Default: 600 Hz.

The client-side sidetone generator always follows this pitch value automatically. There is no separate local pitch control.

### Enable or disable the sidetone

1. Click **Sidetone** in the CW sub-panel to toggle it on or off.
2. Both the radio's DAX-fed monitor and the client-side low-latency sidetone generator are enabled or disabled together by this single button.

### Adjust sidetone volume

1. Move the **Sidetone volume** slider to the desired level. Valid range: 0–100.
2. The slider sets both the radio monitor volume (`mon_gain_cw`) and the client-side sidetone generator volume simultaneously.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| **Pitch < / >** | 600 Hz | 100–6000 Hz (step 10) | — | Steps the radio CW sidetone/decode pitch by 10 Hz per click; sent to the FLEX-8600. The client-side sidetone pitch always follows this value automatically. |
| **Sidetone** | — | On / Off | — | Toggles both the radio's DAX-fed sidetone monitor and the client-side low-latency sidetone generator in lockstep. |
| **Sidetone volume** | — | 0–100 | — | Sets both the radio monitor volume (`mon_gain_cw`) and the client-side sidetone generator volume simultaneously. |
| **L / R pan (CW)** | 50 | 0–100 | — | Sets CW monitor stereo pan on the radio and applies constant-power pan to the client-side sidetone generator. Follows `mon_pan_cw` automatically. Double-click recenters to 50 (centre). |

## Tips

- The **Pitch < / >** control affects both the audible sidetone on the radio and the frequency used by the CW decoder. Adjust it to match your personal pitch preference. The client-side sidetone always tracks it automatically.
- Because pitch and pan follow the radio settings automatically, you only need to adjust **Pitch < / >** and **L / R pan (CW)** in one place — both the radio monitor and the local generator update together.
- The client-side sidetone generator operates at approximately 10 ms latency and works with paddle, straight key, and CWX-generated transmissions. If you are not hearing a sidetone at all, verify that **Sidetone** is enabled.

## Troubleshooting

- **No sidetone is audible** — Confirm **Sidetone** is enabled and **Sidetone volume** is above zero. Both the radio monitor and the client-side generator are controlled by these two controls.
- **Pitch change has no effect** — Confirm the active slice is in a CW mode. The CW sub-panel and its pitch control are only active in CW modes.
- **CW sub-panel is not visible** — The active slice is not in a CW mode. Switch the slice to CW; the applet switches automatically.

## Related

- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)