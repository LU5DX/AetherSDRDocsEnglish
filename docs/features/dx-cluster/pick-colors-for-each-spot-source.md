# Pick colors for each spot source

Each spot source in SpotHub has its own color setting so you can tell at a glance where a spot came from on the panadapter. This page explains how to set the spot color for each source.

## Before you start

- Open AetherSDR with at least one spot source configured. Colors take effect immediately on any spots already displayed.
- The panadapter spot overlay must be active (`IsSpotsEnabled` set to Enabled) for colors to be visible. See [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md) if you need to enable it first.

## Steps

1. Go to `Settings > SpotHub...` to open the SpotHub dialog.
2. To set the **DX cluster** spot color, click the **Cluster** tab, then click **Spot Color:**. Choose a color in the color picker and confirm. The selection is saved to `ClusterSpotColor`.
3. To set the **RBN** spot color, click the **RBN** tab, then click **Spot Color:**. Choose a color and confirm. Saved to `RbnSpotColor`.
4. To set **WSJT-X** spot colors, click the **WSJT-X** tab. There are four separate color pickers, one for each category:
   - Click the color button next to **CQ** to set the CQ call color. Saved to `WsjtxColorCQ`.
   - Click the color button next to **CQ POTA** to set the POTA call color. Saved to `WsjtxColorPOTA`.
   - Click the color button next to **Calling Me** to set the color for decodes addressed to your callsign. Saved to `WsjtxColorCallingMe`.
   - Click the color button next to **Default** to set the fallback color for all other WSJT-X spots. Saved to `WsjtxColorDefault`.
5. To set the **POTA** spot color, click the **POTA** tab, then click **Spot Color:**. Choose a color and confirm. Saved to `PotaSpotColor`.
6. To set the **FreeDV** spot color, click the **FreeDV** tab, then click **Spot Color:**. Choose a color and confirm. Saved to `FreeDvSpotColor`.

## What each control does

| Control | Tab | Persisted setting | Description |
|---|---|---|---|
| **Spot Color:** | Cluster | `ClusterSpotColor` | Color applied to all spots received from the DX cluster telnet source. |
| **Spot Color:** | RBN | `RbnSpotColor` | Color applied to all spots received from the Reverse Beacon Network. |
| CQ color button | WSJT-X | `WsjtxColorCQ` | Color for WSJT-X decodes that are CQ calls. |
| POTA color button | WSJT-X | `WsjtxColorPOTA` | Color for WSJT-X decodes that are CQ POTA calls. |
| Calling Me color button | WSJT-X | `WsjtxColorCallingMe` | Color for WSJT-X decodes addressed to your callsign. |
| Default color button | WSJT-X | `WsjtxColorDefault` | Fallback color for WSJT-X decodes that do not match any active filter. |
| **Spot Color:** | POTA | `PotaSpotColor` | Color applied to all spots from POTA activations polling. |
| **Spot Color:** | FreeDV | `FreeDvSpotColor` | Color applied to all spots from the FreeDV QSO reporter WebSocket. |

## Tips

- The **FreeDV** tab is only present in builds that include WebSocket support. If the tab is absent, your build does not include it.
- If you want all spots to share a single color regardless of source, enable **Override Colors:** on the **Display** tab instead. That setting (`IsSpotsOverrideColorsEnabled`) overrides every per-source color.
- The WSJT-X Default color applies only to spots that do not match an enabled filter (CQ, CQ POTA, or Calling Me). If no filters are checked, the Default color is used for all WSJT-X spots.

## Related

- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
- [Start WSJT-X UDP listener and filter for CQ, POTA or calls to me](start-wsjt-x-udp-listener-and-filter-for-cq-pota-or-calls-to-me.md)
- [Enable DXCC coloring from an ADIF log](enable-dxcc-coloring-from-an-adif-log.md)
- [Poll POTA activations](poll-pota-activations.md)
- [Enable FreeDV QSO reporter WebSocket](enable-freedv-qso-reporter-websocket.md)
- [Connect to a DX cluster](../../getting-started/setup/connect-to-a-dx-cluster.md)
- [Connect to the Reverse Beacon Network](../../getting-started/setup/connect-to-the-reverse-beacon-network.md)
