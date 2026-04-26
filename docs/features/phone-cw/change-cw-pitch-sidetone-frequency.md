# Change CW pitch / sidetone frequency

This page explains how to adjust the CW pitch — the tone frequency used for sidetone and CW decode — both on the radio and for the client-side local sidetone. You would do this to match your preferred listening pitch or to align the local sidetone with a non-default radio pitch.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- The active slice must be in a CW mode. The Phone/CW applet automatically switches to CW controls when CW mode is active.
- Open the Phone/CW applet by clicking the **P/CW** tray button on the right sidebar, if it is not already visible.

## Steps

### Change the radio CW pitch

1. In the CW sub-panel, locate the **Pitch < / >** spinbox.
2. Click **<** to decrease the pitch by 10 Hz, or **>** to increase it by 10 Hz.
3. The valid range is 100–6000 Hz in steps of 10 Hz. The default is 600 Hz.

This pitch setting is sent to the radio and also controls CW decode.

### Change the local sidetone pitch

The local sidetone pitch can either follow the radio pitch automatically or be set to an independent value.

**To follow the radio pitch (default):**

1. Confirm that **Follow (local pitch)** is on (the button appears active). This is the default state.
2. The local sidetone pitch will track the radio **Pitch < / >** value automatically. No further action is needed.

**To set a manual local sidetone pitch:**

1. Click **Follow (local pitch)** to turn it off.
2. The **Local sidetone pitch** slider becomes enabled.
3. Drag the **Local sidetone pitch** slider to your desired frequency. The valid range is 100–2000 Hz. The default is 600 Hz.

## What each control does

| Control | Kind | Default | Valid range | Persisted setting |
|---|---|---|---|---|
| **Pitch < / >** | Spinbox | 600 Hz | 100–6000 Hz (step 10 Hz) | — |
| **Follow (local pitch)** | Toggle button | On | On / Off | `CwLocalSidetonePitchFollow` |
| **Local sidetone pitch** | Slider | 600 Hz | 100–2000 Hz | `CwLocalSidetonePitchHz` |

## Tips

- The **Local sidetone pitch** slider is disabled while **Follow (local pitch)** is on. Turn **Follow (local pitch)** off first to enable the slider.
- The local sidetone pitch is independent of the radio sidetone monitor. If you use the local sidetone (Local STn) for low-latency monitoring, set the pitch here rather than through the radio's sidetone path.
- The internal tone generator clamps the pitch to 100–4000 Hz regardless of what the slider displays above 4000 Hz.

## Related

- [Make the local sidetone pitch follow the radio's CW pitch, or set it manually with the slider](make-the-local-sidetone-pitch-follow-the-radio-s-cw-pitch-or-set-it-manually-with-the-slider.md)
- [Enable the low-latency local CW sidetone (Local STn) for fast paddle / straight-key / CWX work](enable-the-low-latency-local-cw-sidetone-local-stn-for-fast-paddle-straight-key-cwx-work.md)
- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)
- [Set the local sidetone volume independently of the radio monitor](set-the-local-sidetone-volume-independently-of-the-radio-monitor.md)
