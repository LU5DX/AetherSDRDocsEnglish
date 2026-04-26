# Enable the low-latency local CW sidetone (Local STn) for fast paddle / straight-key / CWX work

The Local STn feature generates a CW sidetone entirely on your computer with approximately 10 ms latency, independent of the radio's DAX-fed monitor. Use it when the round-trip delay of the radio's built-in sidetone is noticeable during fast paddle, straight-key, or CWX operation.

## Before you start

- Connect to a FLEX-8600 radio. The Phone/CW applet requires an active radio connection.
- Set the active slice to a CW mode. The CW sub-panel is only shown when the active slice is in CW mode; in voice modes the applet displays the Phone controls instead.
- Confirm your system audio output is configured and working — the local sidetone plays through your computer's audio output.

## Steps

1. Click the **P/CW** tray button in the right sidebar to open the Phone/CW applet.
2. Switch the active slice to a CW mode if you have not already done so. The applet automatically switches to the CW sub-panel.
3. Click **Local STn** to enable the local sidetone. The button activates and the client-side sidetone generator starts. The setting is persisted as `CwLocalSidetoneEnabled`.
4. Adjust the **Local sidetone volume** slider to a comfortable level. The default is 50; the range is 0–100. This is persisted as `CwLocalSidetoneVolume`.
5. By default, **Follow** is on, which means the local sidetone pitch tracks the radio's CW pitch setting automatically. If you want a fixed pitch instead, click **Follow** to turn it off, then set the **Local sidetone pitch** slider to the desired frequency.

## What each control does

| Control | Default | Range | Persisted key | Behavior |
|---|---|---|---|---|
| **Local STn** | Off | On / Off | `CwLocalSidetoneEnabled` | Enables the client-side low-latency CW sidetone (~10 ms latency). Works for paddle, straight key, and CWX-generated transmissions. Independent of the radio's DAX-fed monitor. |
| **Local sidetone volume** | 50 | 0–100 | `CwLocalSidetoneVolume` | Sets the volume of the local sidetone. Has no effect on the radio sidetone gain. |
| **Follow** | On | On / Off | `CwLocalSidetonePitchFollow` | When on, the local sidetone pitch follows the radio's CW pitch. When off, the **Local sidetone pitch** slider is enabled for manual control. |
| **Local sidetone pitch** | 600 Hz | 100–2000 Hz | `CwLocalSidetonePitchHz` | Sets the local sidetone tone frequency in Hz. Only active when **Follow** is off. |

## Tips

- The local sidetone works for CWX text transmissions as well as paddle and straight-key keying. You do not need to change any CWX settings to get sidetone feedback during CWX sends.
- The radio's **Sidetone** button and **Sidetone volume** slider control the DAX-fed monitor path and are separate from Local STn. You can run both simultaneously or use either one alone.
- If **Follow** is on, changing the radio CW pitch via the **Pitch < / >** spinbox (100–6000 Hz, step 10) will also update the local sidetone pitch automatically.
- `CwLocalSidetoneEnabled` is persisted as `True` or `False` and is restored on the next application launch, so Local STn remains on across sessions once enabled.

## Troubleshooting

- **No sound from the local sidetone when keying** — Confirm **Local STn** is active (button checked), the **Local sidetone volume** slider is above 0, and your system audio output is functioning. The local sidetone plays through the computer's audio output, not through the radio's speaker.
- **Local sidetone pitch does not match what you hear on receive** — Check that **Follow** is on. If it is off, the **Local sidetone pitch** slider controls the pitch independently of the radio CW pitch setting. Turn **Follow** on to re-link them.
- **CW sub-panel is not visible** — The applet only shows CW controls when the active slice is in a CW mode. Switch the slice mode to CW and the panel will appear automatically.

## Related

- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)
- [Make the local sidetone pitch follow the radio's CW pitch, or set it manually with the slider](make-the-local-sidetone-pitch-follow-the-radio-s-cw-pitch-or-set-it-manually-with-the-slider.md)
- [Set the local sidetone volume independently of the radio monitor](set-the-local-sidetone-volume-independently-of-the-radio-monitor.md)
- [Change CW pitch / sidetone frequency](change-cw-pitch-sidetone-frequency.md)
- [Enable iambic paddle keying](enable-iambic-paddle-keying.md)
