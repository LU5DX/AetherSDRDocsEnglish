# Reconnect to a radio with fewer slices without stale tabs

When you switch from a radio with more slices (for example, a FLEX-6700 with up to 8) to one with fewer, the RX Controls applet rebuilds its slice tab buttons from scratch on every connection so no leftover A–H tabs remain visible.

## Before you start

- Close your current radio connection before connecting to the smaller radio.
- The RX Controls applet must be visible in the Applet Panel (right sidebar). If it is not, click the **RX** tray button on the right sidebar to show it.

## Steps

1. Connect to the replacement radio using your normal connection method.
2. Observe the **Slice tabs (A..H)** row in the RX Controls applet — it now shows only the tabs supported by the newly connected radio. Any tabs from the previous session are gone.

> If the new radio has only one slice, the slice tab row is hidden entirely.

## What each control does

| Control | Behavior | Notes |
|---|---|---|
| **Slice tabs (A..H)** | Selects which slice the RX applet is bound to. Buttons are torn down and rebuilt on every connection (`clearSliceButtons()`), so tabs from a previous higher-slice radio never linger. The row is hidden when the radio supports only one slice. |  |
| **Slice badge** | Displays the letter (A–H) of the currently bound slice, coloured by slice identity. |  |
| **🔓 / 🔒** | Toggles tune-lock on the active slice. A locked slice ignores incoming frequency changes. |  |
| **ANT1 (RX antenna)** | Selects the receive antenna from the radio's antenna list. |  |
| **ANT1 (TX antenna)** | Selects the transmit antenna; RX-only ports (prefixed `RX`) are filtered out. |  |
| **Mode combo** | Sets the slice mode (USB, LSB, CW, AM, SAM, FM, NFM, DFM, DIGU, DIGL, RTTY; RADE if built with `HAVE_RADE`). |  |
| **Frequency label** | Displays the current VFO frequency. Click to enter edit mode. |  |
| **Frequency edit** | Type a frequency in MHz and press Enter to tune. Escape cancels and restores the previous frequency. |  |
| **TX (badge)** | Click to designate this slice as the TX slice. |  |
## Tips

- If you reconnect repeatedly between radios of different sizes, the tab row always reflects the current radio — no manual cleanup is needed.
- Slice tab click handlers are guarded against duplicate connections across reconnects, so rapid reconnection cycles do not cause double-firing events.
- The **L / R pan** slider resets to centre (50) with a double-click if audio positioning shifts unexpectedly after switching slices.

## Related

- [rx-controls-overview.md](rx-controls-overview.md)
- [connect-to-radio.md](connect-to-radio.md)
<!-- docmesh:llm version=v0.9.5.1 date=2026-05-04 -->
