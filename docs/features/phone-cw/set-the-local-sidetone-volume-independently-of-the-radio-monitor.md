# Set the local sidetone volume independently of the radio monitor

The local sidetone in AetherSDR is generated client-side by AudioEngine, with approximately 10 ms latency, making it independent of the radio's DAX-fed monitor. This page explains how to adjust its volume without affecting the radio's sidetone or monitor level.

## Before you start

- AetherSDR must be connected to the radio.
- The active slice must be in a CW mode. The Phone/CW applet automatically switches to the CW sub-panel when a CW mode is selected.
- Local sidetone must be enabled. Click the `P/CW` tray button in the right sidebar to open the Phone/CW applet, then enable Local STn. See [Enable the low-latency local CW sidetone (Local STn) for fast paddle / straight-key / CWX work](enable-the-low-latency-local-cw-sidetone-local-stn-for-fast-paddle-straight-key-cwx-work.md) if you have not done this yet.

## Steps

1. Click the `P/CW` tray button in the right sidebar to open the Phone/CW applet.
2. Confirm the CW sub-panel is visible. If the active slice is in a CW mode, the panel switches to CW controls automatically.
3. Locate the Local STn toggle button. Confirm it is active (enabled).
4. Drag the Local sidetone volume slider left or right to set the desired level. The range is 0–100, with a default of 50.

## What each control does

| Control | Default | Valid range | Persisted setting key |
|---|---|---|---|
| Local STn | Off | On / Off | `CwLocalSidetoneEnabled` |
| Local sidetone volume | 50 | 0–100 | `CwLocalSidetoneVolume` |
| Follow (local pitch) | On | On / Off | `CwLocalSidetonePitchFollow` |
| Local sidetone pitch | 600 | 100–2000 Hz | `CwLocalSidetonePitchHz` |

**Local STn** — Enables or disables the client-side low-latency sidetone generator. When off, no local audio is produced regardless of the volume slider position.

**Local sidetone volume** — Sets the volume of the local sidetone only. It has no effect on the radio's Sidetone volume slider or the MON monitor level.

**Follow (local pitch)** — When on, the local sidetone pitch tracks the radio's CW pitch setting. When off, the Local sidetone pitch slider becomes active for manual control.

**Local sidetone pitch** — Sets the local sidetone tone frequency in Hz. Only adjustable when Follow is off.

## Tips

- The Local sidetone volume slider and the Sidetone volume slider are fully independent. Adjust each separately to balance the local (~10 ms latency) and radio monitor audio.
- Local STn works for paddle, straight key, and CWX-generated transmissions.

## Related

- [Enable the low-latency local CW sidetone (Local STn) for fast paddle / straight-key / CWX work](enable-the-low-latency-local-cw-sidetone-local-stn-for-fast-paddle-straight-key-cwx-work.md)
- [Make the local sidetone pitch follow the radio's CW pitch, or set it manually with the slider](make-the-local-sidetone-pitch-follow-the-radio-s-cw-pitch-or-set-it-manually-with-the-slider.md)
- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)
- [Change CW pitch / sidetone frequency](change-cw-pitch-sidetone-frequency.md)
