# Reset slice tabs after switching to a radio with fewer slices

When you connect to a radio that supports fewer slices than your previous radio, the Main Window may show stale slice tabs from the prior session. This page explains how to clear those leftover tabs so the tab strip reflects only the slices the current radio provides.

## Before you start

- Ensure the new radio connection is established and AetherSDR shows it as active in the Main Window.

## Steps

1. Disconnect from the current radio using the connection control in the Main Window toolbar, then reconnect to the same radio. The Main Window detects the slice count on reconnect and resets the tab strip to match the slices available on that radio.

If stale tabs remain after reconnecting, restart AetherSDR. The application rebuilds the slice tab strip from scratch on launch using the connected radio's slice count.

## Tips

- If you switch between radios frequently, always disconnect cleanly before switching so the Main Window can reconcile the slice count correctly on the next connection.
- Stale tabs do not affect audio or tuning on active slices, but selecting one may produce no output because no slice backs it.

## Related

- [main-window.md](main-window.md)
- [slice-panadapter-layout.md](slice-panadapter-layout.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
