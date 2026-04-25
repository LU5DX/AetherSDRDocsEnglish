# Pick colors for each spot source

AetherSDR can display spots from up to six sources simultaneously. Assigning a distinct color to each source makes it easy to tell them apart on the panadapter at a glance.

## Before you start

- Open SpotHub: `Settings > SpotHub...`
- At least one spot source should be configured so you can see the effect of your color choice.

## Steps

### DX Cluster spot color

1. In SpotHub, click the **Cluster** tab.
2. Click the **Spot Color:** button.
3. Choose a color in the color picker that opens and confirm your selection.
4. The new color is saved to `ClusterSpotColor` and applied immediately to cluster spots on the panadapter.

### RBN spot color

1. Click the **RBN** tab.
2. Click the **Spot Color:** button.
3. Choose a color and confirm.
4. Saved to `RbnSpotColor`.

### WSJT-X spot colors

WSJT-X supports four separate colors, one per decode category.

1. Click the **WSJT-X** tab.
2. Click the color button for each category you want to change:
   - **CQ color** — spots decoded as CQ calls. Saved to `WsjtxColorCQ`.
   - **POTA color** — spots decoded as CQ POTA calls. Saved to `WsjtxColorPOTA`.
   - **Calling Me color** — decodes addressed to your callsign. Saved to `WsjtxColorCallingMe`.
   - **Default color** — all other WSJT-X decodes. Saved to `WsjtxColorDefault`.
3. Confirm each color in the color picker before moving to the next.

### POTA spot color

1. Click the **POTA** tab.
2. Click the **Spot Color:** button.
3. Choose a color and confirm.
4. Saved to `PotaSpotColor`.

### FreeDV spot color

1. Click the **FreeDV** tab.
2. Click the **Spot Color:** button.
3. Choose a color and confirm.
4. Saved to `FreeDvSpotColor`.

> **Note:** The FreeDV tab is present only if AetherSDR was built with WebSocket support.

### SpotCollector

SpotCollector does not have a dedicated spot-color picker in SpotHub. See the Display tab options below if you need a uniform override for all sources.

## What each control does

| Control | Tab | Saved setting | Purpose |
|---|---|---|---|
| **Spot Color:** | Cluster | `ClusterSpotColor` | Color for all spots received from the DX cluster telnet feed. |
| **Spot Color:** | RBN | `RbnSpotColor` | Color for all spots received from the Reverse Beacon Network. |
| **CQ color** | WSJT-X | `WsjtxColorCQ` | Color for WSJT-X decodes that are CQ calls. |
| **POTA color** | WSJT-X | `WsjtxColorPOTA` | Color for WSJT-X decodes that are CQ POTA calls. |
| **Calling Me color** | WSJT-X | `WsjtxColorCallingMe` | Color for WSJT-X decodes addressed to your callsign. |
| **Default color** | WSJT-X | `WsjtxColorDefault` | Color for all other WSJT-X decodes. |
| **Spot Color:** | POTA | `PotaSpotColor` | Color for spots received from the POTA activation feed. |
| **Spot Color:** | FreeDV | `FreeDvSpotColor` | Color for spots received from the FreeDV QSO reporter. |

## Tips

- If all per-source colors are too subtle to distinguish, use **Override Colors:** on the **Display** tab to force a single text color across every source, saved to `IsSpotsOverrideColorsEnabled` and `SpotsOverrideColor`.
- DXCC coloring (enabled with **DXCC Coloring** on the **Display** tab) can override per-source colors to indicate worked, confirmed, or needed status. If your spot colors are not appearing as set, check whether `DxccColoringEnabled` is active.

## Related

- [SpotHub overview](overview.md)
- [Start WSJT-X UDP listener and filter for CQ, POTA or calls to me](start-wsjt-x-udp-listener-and-filter-for-cq-pota-or-calls-to-me.md)
- [Poll POTA activations](poll-pota-activations.md)
- [Enable FreeDV QSO reporter WebSocket](enable-freedv-qso-reporter-websocket.md)
- [Enable DXCC coloring from an ADIF log](enable-dxcc-coloring-from-an-adif-log.md)
- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
