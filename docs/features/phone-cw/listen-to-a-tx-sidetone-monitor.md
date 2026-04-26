# Listen to a TX sidetone monitor

The Phone/CW applet provides two independent ways to monitor your transmitted audio: a radio-side sideband monitor (Phone modes) and a radio-side CW sidetone monitor (CW mode). Use these to hear your own signal during transmission without relying on external audio paths.

## Before you start

- AetherSDR must be connected to the radio. The Phone/CW applet is only functional when a radio connection is active.
- The P/CW applet must be visible in the Applet Panel. If it is not, click the **P/CW** tray button on the right sidebar to open it.
- Confirm which mode the active slice is in. The applet automatically shows the Phone panel in voice modes and the CW panel in CW mode.

## Steps

### Phone modes (SSB, AM, FM)

1. Open the **P/CW** applet from the right sidebar.
2. Confirm the Phone panel is displayed (not the CW panel).
3. Click **MON** to enable the sideband monitor. The button lights when active.
4. Drag the **Monitor volume** slider to set the monitor level. Valid range: 0–100.

### CW mode

1. Open the **P/CW** applet from the right sidebar.
2. Confirm the CW panel is displayed. If the active slice is in a CW mode, the applet switches to it automatically.
3. Click **Sidetone** to enable the radio CW sidetone monitor. The button lights when active.
4. Drag the **Sidetone volume** slider to set the monitor level. Valid range: 0–100.

## What each control does

| Control | Kind | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|---|
| **MON** | Toggle button | — | On / Off | — | Enables the sideband monitor for Phone modes. |
| **Monitor volume** | Slider | — | 0–100 | — | Sets the sideband monitor volume. |
| **Sidetone** | Toggle button | — | On / Off | — | Enables the radio CW sidetone monitor. |
| **Sidetone volume** | Slider | — | 0–100 | — | Sets the CW monitor volume. |

## Tips

- The radio-side CW sidetone monitor routes audio through the radio's DAX path. If you need lower latency (approximately 10 ms) for paddle or straight-key work, use the **Local STn** client-side sidetone instead. See [Enable the low-latency local CW sidetone (Local STn) for fast paddle / straight-key / CWX work](enable-the-low-latency-local-cw-sidetone-local-stn-for-fast-paddle-straight-key-cwx-work.md).
- **MON** and **Sidetone** are separate controls on separate panels. Enabling one does not affect the other.

## Related

- [Enable the low-latency local CW sidetone (Local STn) for fast paddle / straight-key / CWX work](enable-the-low-latency-local-cw-sidetone-local-stn-for-fast-paddle-straight-key-cwx-work.md)
- [Change CW pitch / sidetone frequency](change-cw-pitch-sidetone-frequency.md)
- [Set the local sidetone volume independently of the radio monitor](set-the-local-sidetone-volume-independently-of-the-radio-monitor.md)
