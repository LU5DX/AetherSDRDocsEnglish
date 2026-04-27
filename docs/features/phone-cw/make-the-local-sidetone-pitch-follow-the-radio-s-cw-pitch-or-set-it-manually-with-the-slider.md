# Make the local sidetone pitch follow the radio's CW pitch, or set it manually with the slider

Control whether the client-side local CW sidetone uses the radio's current CW pitch automatically, or plays at a fixed frequency you choose with a slider. This is useful when you want the local sidetone to stay in sync with the radio's decode pitch, or when you prefer a specific pitch regardless of what the radio is set to.

## Before you start

- The active slice must be in a CW mode so that the CW sub-panel is visible in the Phone/CW applet.
- Local STn must be enabled. If it is not, click Local STn in the Phone/CW applet to turn it on. See [Enable the low-latency local CW sidetone (Local STn) for fast paddle / straight-key / CWX work](enable-the-low-latency-local-cw-sidetone-local-stn-for-fast-paddle-straight-key-cwx-work.md).

## Steps

### To make the pitch follow the radio's CW pitch

1. Open the Phone/CW applet by clicking the **P/CW** tray button in the right sidebar.
2. Confirm that **Follow (local pitch)** is checked (lit). This is the default state.
3. No further action is needed. The local sidetone pitch now tracks whatever value is set in the **Pitch < / >** spinbox.

### To set the pitch manually

1. Open the Phone/CW applet by clicking the **P/CW** tray button in the right sidebar.
2. Click **Follow (local pitch)** to turn it off. The **Local sidetone pitch** slider becomes enabled.
3. Drag the **Local sidetone pitch** slider to the frequency you want. The valid range is 100–2000 Hz; the default is 600 Hz.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| **Follow (local pitch)** | On | On / Off | `CwLocalSidetonePitchFollow` | When on, local sidetone pitch tracks the radio's CW pitch. When off, the manual slider is enabled. |
| **Local sidetone pitch** | 600 Hz | 100–2000 Hz | `CwLocalSidetonePitchHz` | Sets the local sidetone frequency in Hz. Only adjustable when Follow (local pitch) is off. |

## Tips

- The radio's CW pitch is set with the **Pitch < / >** spinbox, which steps in 10 Hz increments over 100–6000 Hz. If you use Follow (local pitch), the local sidetone will reflect changes to that spinbox immediately.
- The local sidetone generator clamps its tone to 100–4000 Hz internally, so values above 4000 Hz set via the radio pitch will be clamped when Follow is on.

## Troubleshooting

- **Local sidetone pitch slider is grayed out and cannot be moved** — Follow (local pitch) is on. Click **Follow (local pitch)** to turn it off, which enables the slider.
- **Pitch does not change when you move the radio Pitch < / > spinbox** — Follow (local pitch) may be off. Click **Follow (local pitch)** to turn it on.

## Related

- [Enable the low-latency local CW sidetone (Local STn) for fast paddle / straight-key / CWX work](enable-the-low-latency-local-cw-sidetone-local-stn-for-fast-paddle-straight-key-cwx-work.md)
- [Set the local sidetone volume independently of the radio monitor](set-the-local-sidetone-volume-independently-of-the-radio-monitor.md)
- [Change CW pitch / sidetone frequency](change-cw-pitch-sidetone-frequency.md)
- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)
