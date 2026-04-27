# Enable the low-latency local CW sidetone (Local STn) for fast paddle / straight-key / CWX work

The local CW sidetone generates a client-side audio tone at approximately 10 ms latency, independent of the radio's DAX-fed monitor. Use it when the radio's sidetone path introduces too much delay for comfortable paddle, straight-key, or CWX operation.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- The active slice must be in a CW mode. The Phone/CW applet automatically switches to its CW sub-panel when a CW slice is active.
- The Phone/CW applet must be visible in the Applet Panel. If it is not, click the **P/CW** tray button on the right sidebar.

## Steps

1. Open the Phone/CW applet by clicking the **P/CW** tray button on the right sidebar. The CW sub-panel appears automatically when the active slice is in CW mode.
2. Click **Local STn** to enable the local sidetone. The button becomes active when enabled. This persists as `CwLocalSidetoneEnabled`.
3. Adjust the **Local sidetone volume** slider to a comfortable listening level (0–100, default 50). This persists as `CwLocalSidetoneVolume`.
4. Choose a pitch option:
   - Leave **Follow (local pitch)** enabled (default) so the local sidetone pitch tracks the radio's CW pitch setting automatically. This persists as `CwLocalSidetonePitchFollow`.
   - Or click **Follow (local pitch)** to turn it off, then drag the **Local sidetone pitch** slider to your preferred frequency (100–2000 Hz, default 600 Hz). This persists as `CwLocalSidetonePitchHz`.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| **Local STn** | Off | On / Off | `CwLocalSidetoneEnabled` | Enables the client-side low-latency CW sidetone (~10 ms). Works for paddle, straight key, and CWX transmissions. Independent of the radio's DAX-fed monitor. |
| **Local sidetone volume** | 50 | 0–100 | `CwLocalSidetoneVolume` | Sets the local sidetone playback volume. Independent of the radio sidetone gain. |
| **Follow (local pitch)** | On | On / Off | `CwLocalSidetonePitchFollow` | When on, the local sidetone pitch follows the radio's CW pitch setting. When off, the manual pitch slider is active. |
| **Local sidetone pitch** | 600 Hz | 100–2000 Hz | `CwLocalSidetonePitchHz` | Manual pitch override for the local sidetone. Only adjustable when **Follow (local pitch)** is off. |

## Tips

- The local sidetone works for CWX-generated text as well as paddle and straight-key input — you do not need a separate configuration for CWX.
- The radio's **Sidetone** button and **Sidetone volume** slider control the DAX-fed radio monitor and are separate from **Local STn**. You can run both simultaneously or use either one alone.
- If you use **Follow (local pitch)**, changing the radio pitch with the **Pitch < / >** spinbox (100–6000 Hz, step 10) will automatically update the local sidetone pitch as well.

## Troubleshooting

- **Local STn button is not visible** — The CW sub-panel only appears when the active slice is in a CW mode. Switch the slice mode to CW, and the applet will update automatically.
- **No audio from local sidetone despite Local STn being enabled** — Check that your system audio output device is configured and not muted. The local sidetone plays through the client system's audio, not the radio's speaker output.
- **Local sidetone pitch does not change when you move the slider** — Confirm that **Follow (local pitch)** is off. The pitch slider is only active when Follow is disabled.

## Related

- [Change CW pitch / sidetone frequency](change-cw-pitch-sidetone-frequency.md)
- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)
- [Make the local sidetone pitch follow the radio's CW pitch, or set it manually with the slider](make-the-local-sidetone-pitch-follow-the-radio-s-cw-pitch-or-set-it-manually-with-the-slider.md)
- [Set the local sidetone volume independently of the radio monitor](set-the-local-sidetone-volume-independently-of-the-radio-monitor.md)
- [Enable iambic paddle keying](enable-iambic-paddle-keying.md)
