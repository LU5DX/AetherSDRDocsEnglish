# Connect to the Reverse Beacon Network

This page explains how to configure AetherSDR to receive spots from the Reverse Beacon Network (RBN) and display them on the panadapter. The RBN provides automated CW, RTTY, and digital skimmer spots useful for contest and DX operating.

## Before you start

- Know the RBN telnet hostname and port you want to use (the public server is `rbn.ad3w.com`, typically on port `7000`).
- Have your callsign ready — it is used as the login credential to the RBN server.

## Steps

1. Open `Settings > SpotHub...`.
2. Click the **RBN** tab.
3. In the **Server:** field, enter the RBN telnet hostname (for example, `rbn.ad3w.com`). This value is saved as `RbnHost`.
4. In the **Port:** field, enter the telnet port (valid range: 1–65535). This value is saved as `RbnPort`.
5. In the **Callsign:** field, enter your callsign. This value is saved as `RbnCallsign`.
6. If the RBN feed produces more spots than you need, set **Rate Limit:** to the maximum number of spots per second to accept. This value is saved as `RbnRateLimit`.
7. Click **Connect**. The button label changes to **Disconnect** when the session is established. Raw RBN traffic appears in the **RBN Console** area.
8. To have AetherSDR connect to the RBN automatically each time it starts, enable **Auto-connect on startup**. This saves to `RbnAutoConnect`.
9. To change the color used for RBN spots on the panadapter, click **Spot Color:** and choose a color from the picker. This saves to `RbnSpotColor`.

## What each control does

| Control | Behavior | Setting key | Default | Valid range |
|---|---|---|---|---|
| **Server:** | RBN telnet hostname | `RbnHost` | — | Any hostname or IP |
| **Port:** | RBN telnet port | `RbnPort` | — | 1–65535 |
| **Callsign:** | Login callsign sent to RBN | `RbnCallsign` | — | — |
| **Rate Limit:** | Maximum spots accepted per second | `RbnRateLimit` | — | — |
| **Connect / Disconnect** | Toggles the telnet connection | — | Connect | — |
| **Auto-connect on startup** | Connects to RBN automatically at launch | `RbnAutoConnect` | — | — |
| **RBN Console** | Read-only display of raw RBN telnet traffic | — | — | — |
| **Send** | Sends a typed command to the RBN server | — | — | — |
| **Spot Color:** | Opens color picker for RBN spots on the panadapter | `RbnSpotColor` | — | — |

## Tips

- RBN spot volume is high, especially during contests. Use **Rate Limit:** to prevent the panadapter from becoming cluttered.
- The **RBN Console** shows raw telnet output. If login fails, the error message appears there.
- Spots from all active sources (Cluster, RBN, WSJT-X, etc.) are combined in the **Spot List** tab and can be sorted by band, frequency, mode, or source.
- Double-click any row in the spot table to tune the radio to that frequency. See [Tune to a spot by double-clicking the spot list](../../features/dx-cluster/tune-to-a-spot-by-double-clicking-the-spot-list.md).

## Troubleshooting

- **RBN Console shows "--- Disconnected ---" immediately after connecting** — The server may have rejected the login. Verify the callsign in **Callsign:** is correct and that the hostname and port are reachable from your network.
- **Spots appear but the panadapter shows nothing** — Check that **Spots:** is enabled on the **Display** tab (master toggle, saved as `IsSpotsEnabled`). Also confirm the band of the incoming spots matches the panadapter's current view.
- **Too many spots slow down the display** — Lower **Rate Limit:** to reduce throughput, or use the band checkboxes on the **Spot List** tab to hide bands you are not working.

## Related

- [Connect to a DX cluster](connect-to-a-dx-cluster.md)
- [SpotHub overview](../../features/dx-cluster/overview.md)
- [Tune spot density, position, font size and lifetime](../../features/dx-cluster/tune-spot-density-position-font-size-and-lifetime.md)
- [Tune to a spot by double-clicking the spot list](../../features/dx-cluster/tune-to-a-spot-by-double-clicking-the-spot-list.md)
- [Pick colors for each spot source](../../features/dx-cluster/pick-colors-for-each-spot-source.md)
- [Enable DXCC coloring from an ADIF log](../../features/dx-cluster/enable-dxcc-coloring-from-an-adif-log.md)
- [Clear all spots from the panadapter](../../features/dx-cluster/clear-all-spots-from-the-panadapter.md)
