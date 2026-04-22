# Pick colors for each spot source

AetherSDR can display spots from several independent sources on the panadapter. This page explains how to assign a distinct color to each source so you can tell them apart at a glance.

## Before you start

- Open AetherSDR.
- At least one spot source (DX cluster, RBN, WSJT-X, POTA, FreeDV) should already be configured. Colors can be set before or after a source is connected.

## Steps

1. Click `Settings > SpotHub...` to open the SpotHub dialog.
2. To set the color for **DX cluster spots**, click the **Cluster** tab, then click **Spot Color:**. Choose a color from the color picker and confirm.
3. To set the color for **RBN spots**, click the **RBN** tab, then click **Spot Color:**. Choose a color and confirm.
4. To set colors for **WSJT-X spots**, click the **WSJT-X** tab. Four color pickers are available:
   - Click **CQ color** to set the color for CQ spots. Saved as `WsjtxColorCQ`.
   - Click **POTA color** to set the color for CQ POTA spots. Saved as `WsjtxColorPOTA`.
   - Click **Calling Me color** to set the color for decodes addressed to your callsign. Saved as `WsjtxColorCallingMe`.
   - Click **Default color** to set the color for all other WSJT-X spots. Saved as `WsjtxColorDefault`.
5. To set the color for **POTA spots**, click the **POTA** tab, then click **Spot Color:**. Choose a color and confirm.
6. To set the color for **FreeDV spots**, click the **FreeDV** tab, then click **Spot Color:**. Choose a color and confirm.

## What each control does

| Control | Tab | Description | Setting key |
|---|---|---|---|
| Spot Color: | Cluster | Color applied to all spots from the DX cluster telnet source. | `ClusterSpotColor` |
| Spot Color: | RBN | Color applied to all spots from the Reverse Beacon Network. | `RbnSpotColor` |
| CQ color | WSJT-X | Color for WSJT-X spots matching the CQ filter. | `WsjtxColorCQ` |
| POTA color | WSJT-X | Color for WSJT-X spots matching the CQ POTA filter. | `WsjtxColorPOTA` |
| Calling Me color | WSJT-X | Color for WSJT-X decodes addressed to your callsign. | `WsjtxColorCallingMe` |
| Default color | WSJT-X | Color for all other WSJT-X spots not matched by a filter. | `WsjtxColorDefault` |
| Spot Color: | POTA | Color applied to all spots from the POTA activation feed. | `PotaSpotColor` |
| Spot Color: | FreeDV | Color applied to all spots from the FreeDV QSO reporter. | `FreeDvSpotColor` |

## Tips

- The **Display** tab provides global overrides. If **Override Colors:** is enabled, the single override color replaces all per-source colors on the panadapter. Disable it to restore per-source colors.
- The FreeDV tab is only present in builds with WebSocket support.
- WSJT-X provides four distinct colors because the same UDP feed can carry CQ calls, POTA activations, and contacts directed at your callsign simultaneously. Assigning different colors lets you prioritize at a glance.

## Related

- [Start WSJT-X UDP listener and filter for CQ, POTA or calls to me](start-wsjt-x-udp-listener-and-filter-for-cq-pota-or-calls-to-me.md)
- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
- [Enable DXCC coloring from an ADIF log](enable-dxcc-coloring-from-an-adif-log.md)
- [SpotHub overview](overview.md)
