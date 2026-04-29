# CW sidetone pitch, volume, and enable in v0.9.2.1

In v0.9.2.1 the separate **Local STn**, **Local sidetone volume**, **Follow (local pitch)**, and **Local sidetone pitch** controls have been removed. The client-side low-latency CW sidetone (CwSidetoneGenerator, ~10 ms latency) is now controlled entirely by the same **Sidetone** toggle and **Sidetone volume** slider that control the radio's DAX-fed monitor. Pitch and pan are always taken automatically from the radio's `cw_pitch` and `mon_pan_cw` settings; there is no manual override.

If you were previously using the separate local sidetone controls, see [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md) for the current workflow.

## Before you start

- The active slice must be in a CW mode so that the CW sub-panel is visible in the Phone/CW applet.

## Steps

### To enable the CW sidetone (both radio monitor and local generator)

1. Open the Phone/CW applet by clicking the **P/CW** tray button in the right sidebar.
2. Click **Sidetone** to turn it on. Both the radio's DAX-fed monitor and the client-side CwSidetoneGenerator start simultaneously.

### To disable the CW sidetone

1. Click **Sidetone** again. Both the radio monitor and the local generator stop.

### To adjust sidetone volume

1. Drag the **Sidetone volume** slider (0–100). The same value is applied to the radio's `mon_gain_cw` setting and to the local sidetone generator volume simultaneously.

### To adjust sidetone pitch

1. Use the **Pitch < / >** spinbox to step the pitch in 10 Hz increments (100–6000 Hz). The local sidetone generator follows this value automatically; there is no separate local pitch control.

### To adjust sidetone stereo pan

1. Drag the **L / R pan (CW)** slider (0–100, default 50 = centre). The same pan value is sent to the radio (`mon_pan_cw`) and applied as constant-power pan to the local sidetone generator.
2. Double-click the slider to return it to centre (50).

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| **Sidetone** | — | On / Off | — | Toggles both the radio's DAX-fed CW monitor and the client-side CwSidetoneGenerator in lockstep. |
| **Sidetone volume** | — | 0–100 | — | Sets `mon_gain_cw` on the radio and the local sidetone generator volume simultaneously. |
| **Pitch < / >** | 600 Hz | 100–6000 Hz (step 10) | — | Sets the CW sidetone/decode pitch on the radio; local generator always follows. |
| **L / R pan (CW)** | 50 | 0–100 | — | Sets `mon_pan_cw` on the radio and applies constant-power pan to the local generator. Double-click recenters to 50. |

## Tips

- Because pitch and pan are always derived from the radio's `cw_pitch` and `mon_pan_cw` settings, the local sidetone and the radio monitor are always in agreement — no manual synchronization is needed.
- The local CwSidetoneGenerator has approximately 10 ms latency, which makes it suitable for high-speed paddle work where the radio's round-trip DAX latency is noticeable.
- There are no longer any `CwLocalSidetoneEnabled`, `CwLocalSidetoneVolume`, `CwLocalSidetonePitchFollow`, or `CwLocalSidetonePitchHz` settings. If you have scripts or configuration files that reference these keys, they can be removed.

## Troubleshooting

- **No sidetone heard even though Sidetone is on** — Check that your audio output device is selected correctly in AetherSDR's audio settings. Also confirm that **Sidetone volume** is above 0.
- **Sidetone pitch does not match what you expect** — The pitch is controlled solely by the **Pitch < / >** spinbox. Adjust it there; the local generator will follow immediately.
- **Pan has no effect** — Confirm your audio output is configured for stereo. Mono output devices will not reflect pan changes.

## Related

- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)
- [Change CW pitch / sidetone frequency](change-cw-pitch-sidetone-frequency.md)
- [Set CW speed and break-in delay](set-cw-speed-and-break-in-delay.md)