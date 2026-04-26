# Enable iambic paddle keying

Iambic paddle keying lets you use a dual-paddle key with the FLEX-8600's built-in iambic keyer. This page explains how to turn on the iambic mode from AetherSDR's Phone/CW applet.

## Before you start

- The radio must be connected. The Phone/CW applet is not available without an active radio connection.
- The active slice must be in a CW mode. The CW sub-panel only appears when the slice mode is CW; in voice modes the applet shows the Phone controls instead.
- Your paddle must be physically connected to the radio's KEY jack.

## Steps

1. Click the **P/CW** tray button on the right sidebar to open the Phone/CW applet. If the applet is already visible, skip this step.
2. Confirm the CW sub-panel is showing. If you see mic and processor controls instead, switch the active slice to a CW mode first.
3. Click **Iambic** to toggle it on. The button highlights when iambic mode is active.

## What each control does

| Control | Description | Default | Range | Setting key |
|---|---|---|---|---|
| **Iambic** | Toggles the iambic paddle keyer on the radio. | — | On / Off | — |
| **Speed (CW)** | Sets the keying speed. | — | 5–100 WPM | — |
| **Delay (CW)** | Sets the CW break-in delay. | — | 0–2000 ms (step 10) | — |
| **Breakin** | Toggles full break-in (QSK). | — | On / Off | — |
| **Pitch < / >** | Steps the CW sidetone and decode pitch by 10 Hz. | 600 Hz | 100–6000 Hz | — |
| **Sidetone** | Toggles the radio's CW sidetone monitor. | — | On / Off | — |
| **Sidetone volume** | Sets the radio CW monitor volume. | — | 0–100 | — |
| **Local STn** | Toggles a client-side low-latency CW sidetone (~10 ms latency). | Off | On / Off | `CwLocalSidetoneEnabled` |
| **Local sidetone volume** | Sets the local sidetone volume independently of the radio monitor. | 50 | 0–100 | `CwLocalSidetoneVolume` |
| **Follow (local pitch)** | When on, the local sidetone pitch tracks the radio CW pitch. When off, the manual pitch slider is enabled. | On | On / Off | `CwLocalSidetonePitchFollow` |
| **Local sidetone pitch** | Manual pitch for the local sidetone in Hz; only active when Follow is off. | 600 Hz | 100–2000 Hz | `CwLocalSidetonePitchHz` |

## Tips

- For the fastest audible feedback while paddling, enable **Local STn** in addition to or instead of **Sidetone**. The local sidetone is generated client-side at approximately 10 ms latency, compared to the DAX-fed radio monitor which carries more audio pipeline delay.
- If you want the local sidetone pitch to match what the radio decodes, leave **Follow (local pitch)** on. Turn it off only if you want to set a different pitch for your ear.

## Troubleshooting

- **CW sub-panel is not visible** — The active slice is not in CW mode. Change the slice mode to CW; the applet switches automatically.
- **Iambic button is visible but paddle does not key** — Verify the paddle is connected to the radio's KEY jack and that the radio firmware recognizes the connection. AetherSDR only sets the keyer mode; the physical connection is handled by the radio.

## Related

- [Enable the low-latency local CW sidetone (Local STn) for fast paddle / straight-key / CWX work](enable-the-low-latency-local-cw-sidetone-local-stn-for-fast-paddle-straight-key-cwx-work.md)
- [Set CW keying speed in WPM](set-cw-keying-speed-in-wpm.md)
- [Set CW break-in delay](set-cw-break-in-delay.md)
- [Change CW pitch / sidetone frequency](change-cw-pitch-sidetone-frequency.md)
- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)
- [Make the local sidetone pitch follow the radio's CW pitch, or set it manually with the slider](make-the-local-sidetone-pitch-follow-the-radio-s-cw-pitch-or-set-it-manually-with-the-slider.md)
