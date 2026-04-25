# Connect to the Reverse Beacon Network

The Reverse Beacon Network (RBN) provides automated CW, RTTY, and digital skimmer spots. This page shows how to configure and connect AetherSDR's RBN telnet feed so that RBN spots appear on your panadapter.

## Before you start

- Know the RBN telnet server hostname and port (the public server is `telnet.reversebeacon.net`, port `7000` for CW skimmers).
- Know the callsign you will use to log in to the RBN.
- Spots will only appear on the panadapter if the master spot overlay is enabled (`IsSpotsEnabled` defaults to Enabled).

## Steps

1. Open `Settings > SpotHub...`.
2. Click the **RBN** tab.
3. In the **Server:** field, enter the RBN telnet hostname (e.g., `telnet.reversebeacon.net`). This persists as `RbnHost`.
4. Set **Port:** to the telnet port for the skimmer feed you want. Valid range: 1–65535. This persists as `RbnPort`.
5. In the **Callsign:** field, enter your callsign. This persists as `RbnCallsign`.
6. If the RBN feed produces more spots than you need, set **Rate Limit:** to cap the number of spots processed per second. This persists as `RbnRateLimit`.
7. Click **Connect**. The button label changes to **Disconnect** when the session is established, and the **RBN Console** shows incoming traffic.
8. To have AetherSDR connect to the RBN automatically on every launch, enable **Auto-connect on startup**. This persists as `RbnAutoConnect`.

## What each control does

| Control | Behavior | Setting key | Default / Range |
|---|---|---|---|
| **Server:** | RBN telnet hostname | `RbnHost` | — |
| **Port:** | RBN telnet port | `RbnPort` | 1–65535 |
| **Callsign:** | Login callsign sent to RBN | `RbnCallsign` | — |
| **Rate Limit:** | Maximum RBN spots accepted per second | `RbnRateLimit` | — |
| **Connect / Disconnect** | Toggles the RBN telnet session | — | Starts as Connect |
| **Auto-connect on startup** | Connects to RBN automatically on launch | `RbnAutoConnect` | — |
| **RBN Console** | Read-only display of raw RBN traffic | — | — |
| **Send** | Sends a typed command to the RBN session | — | — |
| **Spot Color:** | Opens a color picker for RBN spots on the panadapter | `RbnSpotColor` | — |

## Tips

- The **RBN Console** is read-only and shows raw telnet lines as they arrive. Use the **Send** command line below it to issue filter commands directly to the RBN server (e.g., `set/skimmer` or band-filter commands supported by the RBN).
- If the panadapter becomes cluttered during a contest, lower **Rate Limit:** to reduce spot density without disconnecting.
- To change how spots look on the panadapter — size, position, lifetime, and stacking — see [Tune spot density, position, font size and lifetime](../../features/dx-cluster/tune-spot-density-position-font-size-and-lifetime.md).
- RBN spots use the color set by **Spot Color:** on the RBN tab. To override all spot source colors with a single color, use the **Override Colors:** toggle on the **Display** tab.

## Troubleshooting

- **Connect button returns to Connect immediately with an error in the console** — The hostname or port is wrong, or the RBN server is unreachable. Verify `RbnHost` and `RbnPort` and check your network connection.
- **No spots appear on the panadapter after connecting** — Confirm that **Spots:** on the **Display** tab is set to Enabled (`IsSpotsEnabled`). Also check that the band you are monitoring is not hidden in the **Spot List** tab band filter checkboxes.
- **Panadapter is flooded with spots** — Reduce **Rate Limit:** to a lower value to cap incoming spot rate.

## Related

- [Connect to a DX cluster](connect-to-a-dx-cluster.md)
- [Tune spot density, position, font size and lifetime](../../features/dx-cluster/tune-spot-density-position-font-size-and-lifetime.md)
- [Pick colors for each spot source](../../features/dx-cluster/pick-colors-for-each-spot-source.md)
- [Tune to a spot by double-clicking the spot list](../../features/dx-cluster/tune-to-a-spot-by-double-clicking-the-spot-list.md)
- [SpotHub overview](../../features/dx-cluster/overview.md)
