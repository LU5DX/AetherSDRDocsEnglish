# Clear all spots and signal-history markers from the panadapter

Remove every DX spot, memory marker, Signal History voice marker, and QRM interference marker from the spectrum display in one action.

## Before you start

- Open the SpotHub dialog: `Settings > SpotHub...`

## Steps

1. Click the **Display** tab.
2. Click **Clear All**.

All spots from every source (DX cluster, RBN, WSJT-X, SpotCollector, POTA, FreeDV), memory-channel overlays, and Signal History markers (both gold voice markers and red QRM markers) disappear from the panadapter.

## Tips

- **Clear All** is a non-destructive action — it only removes current marker overlays from the spectrum. Connected spot sources (cluster, RBN, etc.) continue running and will repopulate the panadapter as new spots arrive.
- To stop spots reappearing, toggle the master **Spots:** toggle button to "Disabled" on the **Display** tab, or disconnect each source on its respective tab.

## Related

- [Toggle Signal History voice markers on the panadapter](toggle-signal-history-voice-markers-on-the-panadapter.md)
- [Toggle QRM markers to see persistent carriers and interference](toggle-qrm-markers-to-see-persistent-carriers-and-interference.md)
- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
- [Start WSJT-X UDP listener and filter for CQ, POTA or calls to me](start-wsjt-x-udp-listener-and-filter-for-cq-pota-or-calls-to-me.md)
- [Connect to a DX cluster](../../getting-started/setup/connect-to-a-dx-cluster.md)
