# Connect to the Reverse Beacon Network

The Reverse Beacon Network (RBN) provides automated CW, RTTY, and digital spot reports from skimmer stations worldwide. This page explains how to configure AetherSDR's RBN connection so those spots appear on your panadapter.

## Before you start

- AetherSDR is installed and running.
- You know the RBN telnet hostname and port you want to use (the public RBN server is `telnet.reversebeacon.net`).
- You have a callsign to use as your login.

## Steps

1. Click `Settings > SpotHub...` to open the SpotHub dialog.
2. Click the **RBN** tab.
3. In the **Server:** field, enter the RBN telnet hostname.
4. In the **Port:** spinbox, enter the telnet port. Valid range: 1–65535.
5. In the **Callsign:** field, enter the callsign you want to log in with.
6. In the **Rate Limit:** spinbox, set the maximum number of spots per second you want to receive.
7. Click **Connect**. The RBN Console area will show incoming raw telnet traffic when the connection is established.
8. To have AetherSDR connect to RBN automatically each time it starts, click **Auto-connect on startup** so it is active.

## What each control does

| Control | Description | Setting key |
|---|---|---|
| **Server:** | RBN telnet hostname | `RbnHost` |
| **Port:** | RBN telnet port (1–65535) | `RbnPort` |
| **Callsign:** | Login callsign sent to RBN | `RbnCallsign` |
| **Rate Limit:** | Maximum RBN spots per second delivered to the panadapter | `RbnRateLimit` |
| **Connect / Disconnect** | Toggles the telnet connection to RBN | — |
| **Auto-connect on startup** | Connects to RBN automatically when AetherSDR launches | `RbnAutoConnect` |
| **RBN Console** | Read-only display of raw RBN telnet traffic | — |
| **Send** | Sends a typed command to the RBN server | — |
| **Spot Color:** | Opens a color picker to set the panadapter color for RBN spots | `RbnSpotColor` |

## Tips

- RBN can produce a very high spot rate during contests. Set **Rate Limit:** to a lower value if the panadapter becomes cluttered or sluggish.
- Spot display on the panadapter requires the master spot overlay to be active. In the **Display** tab, verify that **Spots:** is set to Enabled (default).
- Double-click any RBN spot row in the **Spot List** tab to tune the radio directly to that frequency.

## Troubleshooting

- **RBN Console shows no traffic after clicking Connect** — Verify the hostname and port. The RBN Console will show a connection error message if the server is unreachable. Check your firewall permits outbound TCP on the port you configured.
- **Spots appear in the Spot List tab but not on the panadapter** — Open `Settings > SpotHub...`, click the **Display** tab, and confirm **Spots:** is Enabled.
- **Too many spots overwhelming the display** — Lower the **Rate Limit:** value, or adjust **Spot Lifetime:** and **Levels:** on the **Display** tab to reduce clutter.

## Related

- [SpotHub overview](../../features/dx-cluster/overview.md)
- [Connect to a DX cluster](connect-to-a-dx-cluster.md)
- [Tune spot density, position, font size and lifetime](../../features/dx-cluster/tune-spot-density-position-font-size-and-lifetime.md)
- [Tune to a spot by double-clicking the spot list](../../features/dx-cluster/tune-to-a-spot-by-double-clicking-the-spot-list.md)
- [Pick colors for each spot source](../../features/dx-cluster/pick-colors-for-each-spot-source.md)
- [Clear all spots from the panadapter](../../features/dx-cluster/clear-all-spots-from-the-panadapter.md)
