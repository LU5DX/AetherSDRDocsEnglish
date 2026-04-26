# Set the local sidetone volume independently of the radio monitor

The local sidetone in AetherSDR is generated client-side with approximately 10 ms latency, separate from the radio's DAX-fed monitor. This page shows how to adjust its volume without affecting the radio sidetone gain.

## Before you start

- AetherSDR must be connected to the radio.
- The active slice must be in a CW mode. The Phone/CW applet automatically switches to the CW sub-panel when CW mode is active.
- Local STn must be enabled. If it is not, enable it first — see [Enable the low-latency local CW sidetone (Local STn) for fast paddle / straight-key / CWX work](enable-the-low-latency-local-cw-sidetone-local-stn-for-fast-paddle-straight-key-cwx-work.md).

## Steps

1. Open the Phone/CW applet by clicking the **P/CW** tray button in the right sidebar. The CW sub-panel is shown automatically when the active slice is in CW mode.
2. Locate the **Local sidetone volume** slider in the CW sub-panel.
3. Drag the slider to the desired level. The valid range is 0–100; the default is 50.

The setting is saved immediately as `CwLocalSidetoneVolume` and takes effect without restarting.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| **Local STn** | Off | On / Off | `CwLocalSidetoneEnabled` | Enables or disables the client-side low-latency sidetone. Volume has no effect while this is off. |
| **Local sidetone volume** | 50 | 0–100 | `CwLocalSidetoneVolume` | Sets the volume of the local sidetone only. Does not affect the radio's sidetone gain or the **Sidetone volume** slider. |
| **Sidetone volume** | — | 0–100 | — | Sets the radio CW monitor volume via the DAX-fed path. Adjusted independently of local sidetone volume. |

## Tips

- The **Local sidetone volume** slider and the **Sidetone volume** slider are completely independent. You can silence the radio monitor (set **Sidetone volume** to 0 or disable **Sidetone**) and rely solely on the local sidetone for lower latency feedback.
- The local sidetone works for paddle, straight key, and CWX-generated transmissions.

## Related

- [Enable the low-latency local CW sidetone (Local STn) for fast paddle / straight-key / CWX work](enable-the-low-latency-local-cw-sidetone-local-stn-for-fast-paddle-straight-key-cwx-work.md)
- [Make the local sidetone pitch follow the radio's CW pitch, or set it manually with the slider](make-the-local-sidetone-pitch-follow-the-radio-s-cw-pitch-or-set-it-manually-with-the-slider.md)
- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)
- [Change CW pitch / sidetone frequency](change-cw-pitch-sidetone-frequency.md)
