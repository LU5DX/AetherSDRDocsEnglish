# Pick colors for each spot source

AetherSDR can display spots from multiple sources simultaneously. Assigning a distinct color to each source lets you tell them apart at a glance on the panadapter.

## Before you start

- Open `Settings > SpotHub...` to reach the SpotHub dialog.
- At least one spot source should be configured so you can see the result. Colors take effect immediately; no radio connection is required.

## Steps

### DX Cluster spots

1. Click `Settings > SpotHub...`.
2. Click the **Cluster** tab.
3. Click **Spot Color:**.
4. Choose a color in the color picker that opens and confirm.

The chosen color is saved to `ClusterSpotColor`.

### Reverse Beacon Network spots

1. Click `Settings > SpotHub...`.
2. Click the **RBN** tab.
3. Click **Spot Color:** (RBN).
4. Choose a color and confirm.

The chosen color is saved to `RbnSpotColor`.

### WSJT-X spots

WSJT-X spots support four separate colors, one per decode category.

1. Click `Settings > SpotHub...`.
2. Click the **WSJT-X** tab.
3. Click the color button for each category you want to change:

   | Button | Applies to | Setting key |
   |---|---|---|
   | CQ color | CQ calls | `WsjtxColorCQ` |
   | POTA color | CQ POTA calls | `WsjtxColorPOTA` |
   | Calling Me color | Decodes addressed to your callsign | `WsjtxColorCallingMe` |
   | Default color | All other WSJT-X decodes | `WsjtxColorDefault` |

4. Choose a color and confirm for each button you click.

### POTA spots

1. Click `Settings > SpotHub...`.
2. Click the **POTA** tab.
3. Click **Spot Color:** (POTA).
4. Choose a color and confirm.

The chosen color is saved to `PotaSpotColor`.

### FreeDV spots

1. Click `Settings > SpotHub...`.
2. Click the **FreeDV** tab.
3. Click **Spot Color:** (FreeDV).
4. Choose a color and confirm.

The chosen color is saved to `FreeDvSpotColor`.

## What each control does

| Control | Tab | What it sets | Setting key |
|---|---|---|---|
| Spot Color: | Cluster | Color for DX cluster spots on the panadapter | `ClusterSpotColor` |
| Spot Color: (RBN) | RBN | Color for RBN spots on the panadapter | `RbnSpotColor` |
| CQ color | WSJT-X | Color for CQ decode spots | `WsjtxColorCQ` |
| POTA color | WSJT-X | Color for CQ POTA decode spots | `WsjtxColorPOTA` |
| Calling Me color | WSJT-X | Color for decodes addressed to your callsign | `WsjtxColorCallingMe` |
| Default color | WSJT-X | Color for all other WSJT-X decodes | `WsjtxColorDefault` |
| Spot Color: (POTA) | POTA | Color for POTA activation spots | `PotaSpotColor` |
| Spot Color: (FreeDV) | FreeDV | Color for FreeDV QSO reporter spots | `FreeDvSpotColor` |

## Tips

- The **Display** tab has an **Override Colors:** toggle (`IsSpotsOverrideColorsEnabled`) that forces a single text color for all spots regardless of source. If your per-source colors appear to have no effect, check that this override is not active.
- If you want the panadapter background behind spot labels to be uniform as well, see the **Override Background** controls on the **Display** tab.

## Related

- [SpotHub overview](overview.md)
- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
- [Start WSJT-X UDP listener and filter for CQ, POTA or calls to me](start-wsjt-x-udp-listener-and-filter-for-cq-pota-or-calls-to-me.md)
- [Poll POTA activations](poll-pota-activations.md)
- [Enable FreeDV QSO reporter WebSocket](enable-freedv-qso-reporter-websocket.md)
- [Enable DXCC coloring from an ADIF log](enable-dxcc-coloring-from-an-adif-log.md)
