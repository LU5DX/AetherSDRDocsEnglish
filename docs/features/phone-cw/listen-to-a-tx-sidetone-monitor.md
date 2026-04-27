# Listen to a TX sidetone monitor

AetherSDR provides two separate sidetone monitor paths: a radio-side monitor (available in both Phone and CW modes) and a client-side local sidetone for CW (with approximately 10 ms latency). This page covers both so you can hear your own transmitted audio while operating.

## Before you start

- Connect to a FLEX-8600 radio. The Phone/CW applet requires an active radio connection.
- Open the Applet Panel. If it is not visible, click View > Applet Panel.

## Steps

### Phone mode: enable the sideband monitor

1. Click the P/CW tray button on the right sidebar to open the Phone/CW applet.
2. Confirm the applet is showing the Phone panel (the active slice must be in a voice mode such as SSB or AM).
3. Click MON to enable the TX sideband monitor. The button highlights when active.
4. Adjust the Monitor volume slider to set the playback level (0–100).

### CW mode: enable the radio sidetone monitor

1. Switch the active slice to a CW mode. The applet automatically shows the CW panel.
2. Click Sidetone to enable the radio's DAX-fed CW monitor. The button highlights when active.
3. Adjust the Sidetone volume slider to set the level (0–100).

### CW mode: enable the local low-latency sidetone

1. In the CW panel, click Local STn to enable the client-side sidetone generator. The button highlights when active.
2. Adjust the Local sidetone volume slider to set the level (0–100; default 50).
3. To control pitch:
   - Leave Follow on (default) to have the local sidetone pitch track the radio's CW pitch setting automatically.
   - Click Follow to turn it off, then use the Local sidetone pitch slider to set a manual pitch (100–2000 Hz; default 600 Hz).

## What each control does

| Control | What it does | Default | Range | Setting key |
|---|---|---|---|---|
| MON | Enables the TX sideband monitor (Phone panel). | — | On / Off | — |
| Monitor volume | Sets sideband monitor playback level. | — | 0–100 | — |
| Sidetone | Enables the radio's DAX-fed CW monitor (CW panel). | — | On / Off | — |
| Sidetone volume | Sets the radio CW monitor playback level. | — | 0–100 | — |
| Local STn | Enables the client-side low-latency CW sidetone (~10 ms). | Off | On / Off | `CwLocalSidetoneEnabled` |
| Local sidetone volume | Sets the local sidetone playback level, independent of the radio monitor. | 50 | 0–100 | `CwLocalSidetoneVolume` |
| Follow | When on, local sidetone pitch tracks the radio CW pitch. When off, the manual pitch slider is enabled. | On | On / Off | `CwLocalSidetonePitchFollow` |
| Local sidetone pitch | Manual local sidetone pitch override (only active when Follow is off). | 600 Hz | 100–2000 Hz | `CwLocalSidetonePitchHz` |

## Tips

- The radio sidetone (Sidetone button, CW panel) is routed through DAX and has higher latency than the local sidetone. If you notice an echo or lag while keying, use Local STn instead.
- Local STn works with paddle keying, straight key, and CWX-generated transmissions, so it is usable regardless of how you key the radio.
- The two CW monitor paths (Sidetone and Local STn) are independent. You can run both simultaneously or use only one.
- The MON button and the Sidetone button are separate controls on separate panels. MON applies to voice modes; Sidetone applies to CW mode.

## Troubleshooting

- **MON or Sidetone button has no effect** — Confirm the radio is connected and the active slice mode matches the panel being shown (Phone vs. CW). The applet switches panels automatically based on the active slice mode.
- **Local STn produces no audio** — Check that your system audio output is configured correctly. The local sidetone is generated client-side by AetherSDR; it does not depend on the radio's audio routing.
- **Local sidetone pitch does not change when you move the Local sidetone pitch slider** — Confirm that Follow is off. While Follow is on, the pitch slider is disabled and pitch is controlled by the radio's CW pitch setting.

## Related

- [Enable the low-latency local CW sidetone (Local STn) for fast paddle / straight-key / CWX work](enable-the-low-latency-local-cw-sidetone-local-stn-for-fast-paddle-straight-key-cwx-work.md)
- [Set the local sidetone volume independently of the radio monitor](set-the-local-sidetone-volume-independently-of-the-radio-monitor.md)
- [Make the local sidetone pitch follow the radio's CW pitch, or set it manually with the slider](make-the-local-sidetone-pitch-follow-the-radio-s-cw-pitch-or-set-it-manually-with-the-slider.md)
- [Change CW pitch / sidetone frequency](change-cw-pitch-sidetone-frequency.md)
