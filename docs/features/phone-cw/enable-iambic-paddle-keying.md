# Enable iambic paddle keying

This page explains how to turn on the iambic paddle keyer for the active CW slice. Use this when operating with a squeeze paddle and you want the radio's built-in iambic keyer to handle dit/dah generation.

## Before you start

- AetherSDR must be connected to the radio. The Phone/CW applet requires an active radio connection.
- The active slice must be in a CW mode. The Phone/CW applet shows CW controls only when the active slice is in CW mode; it shows Phone controls otherwise.

## Steps

1. Locate the **P/CW** tray button on the right sidebar and confirm the Phone/CW applet is visible. If it is not visible, click the **P/CW** tray button to show it.
2. Confirm the applet is displaying the CW panel. If Phone controls (mic gain, PROC, MON) are showing instead, switch the active slice to a CW mode first.
3. Click **Iambic** to toggle the iambic paddle keyer on. The button activates and the radio enables iambic keying.

To disable iambic keying, click **Iambic** again.

## What each control does

| Control | Kind | Default | Valid range | Persisted key |
|---|---|---|---|---|
| Iambic | Toggle button | — | On / Off | — |

**Iambic** — Toggles the iambic paddle keyer on the radio. When active, the radio interprets squeeze-paddle input as iambic keying. When off, the radio uses straight-key or bug behavior depending on your paddle wiring.

## Related

- [Set CW keying speed in WPM](set-cw-keying-speed-in-wpm.md)
- [Set CW break-in delay](set-cw-break-in-delay.md)
- [Change CW pitch / sidetone frequency](change-cw-pitch-sidetone-frequency.md)
- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)
