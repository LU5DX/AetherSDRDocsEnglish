# Make the local sidetone pitch follow the radio's CW pitch, or set it manually with the slider

The local sidetone generator in AetherSDR can derive its pitch automatically from the radio's CW pitch setting, or you can override it with a fixed frequency using the pitch slider. Use this page to switch between the two modes and dial in the pitch you want.

## Before you start

- AetherSDR must be connected to the radio.
- The active slice must be in a CW mode — the Phone/CW applet only shows CW controls when CW is active.
- Local STn must be enabled. If it is not, enable it first (see [Enable the low-latency local CW sidetone (Local STn) for fast paddle / straight-key / CWX work](enable-the-low-latency-local-cw-sidetone-local-stn-for-fast-paddle-straight-key-cwx-work.md)).

## Steps

### To make the pitch follow the radio's CW pitch (default)

1. Open the Phone/CW applet by clicking the **P/CW** tray button in the right sidebar.
2. Locate the **Follow (local pitch)** button in the CW sub-panel.
3. Click **Follow (local pitch)** so it is checked (active). The local sidetone pitch will now track the radio's **Pitch < / >** setting automatically.

The **Local sidetone pitch** slider is disabled while **Follow (local pitch)** is on.

### To set the pitch manually

1. Open the Phone/CW applet by clicking the **P/CW** tray button in the right sidebar.
2. Click **Follow (local pitch)** to uncheck it. The **Local sidetone pitch** slider becomes enabled.
3. Drag the **Local sidetone pitch** slider to the desired frequency. The value range is 100–2000 Hz; the default is 600 Hz.

## What each control does

| Control | Default | Valid range | Persisted setting |
|---|---|---|---|
| **Follow (local pitch)** | On | On / Off | `CwLocalSidetonePitchFollow` |
| **Local sidetone pitch** | 600 Hz | 100–2000 Hz | `CwLocalSidetonePitchHz` |

**Follow (local pitch):** When on, the local sidetone pitch mirrors the radio's CW pitch (set via **Pitch < / >**). When off, the manual **Local sidetone pitch** slider takes effect.

**Local sidetone pitch:** Sets the local sidetone tone frequency in Hz. Only active when **Follow (local pitch)** is off. The underlying generator clamps values to the range 100–4000 Hz internally, but the slider exposes 100–2000 Hz.

## Tips

- The radio's CW pitch is adjusted with the **Pitch < / >** spinbox in the same CW sub-panel (range 100–6000 Hz, step 10 Hz). When **Follow (local pitch)** is on, the local sidetone tracks that value automatically — you do not need to update the pitch slider separately.
- The local sidetone runs at approximately 10 ms latency, independent of the radio's DAX-fed monitor. The pitch setting here does not affect the radio's sidetone, only the client-side generator.

## Troubleshooting

- **Local sidetone pitch slider is greyed out** — **Follow (local pitch)** is on. Click **Follow (local pitch)** to uncheck it before adjusting the slider.
- **Local sidetone pitch does not change when the radio CW pitch changes** — **Follow (local pitch)** is off. Click **Follow (local pitch)** to enable automatic tracking.
- **No local sidetone sound at all** — **Local STn** is off. Enable it; see [Enable the low-latency local CW sidetone (Local STn) for fast paddle / straight-key / CWX work](enable-the-low-latency-local-cw-sidetone-local-stn-for-fast-paddle-straight-key-cwx-work.md).

## Related

- [Change CW pitch / sidetone frequency](change-cw-pitch-sidetone-frequency.md)
- [Enable the low-latency local CW sidetone (Local STn) for fast paddle / straight-key / CWX work](enable-the-low-latency-local-cw-sidetone-local-stn-for-fast-paddle-straight-key-cwx-work.md)
- [Set the local sidetone volume independently of the radio monitor](set-the-local-sidetone-volume-independently-of-the-radio-monitor.md)
- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)
