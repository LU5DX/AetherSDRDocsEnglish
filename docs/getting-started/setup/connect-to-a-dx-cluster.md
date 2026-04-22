# Connect to a DX cluster

AetherSDR's SpotHub dialog connects to a DX cluster via telnet and overlays the incoming spots on your panadapter. Use this page to enter your cluster server details, log in, and start seeing spots.

## Before you start

- Know the hostname and port of your preferred DX cluster (for example, `dxc.nc7j.com` on port `23`).
- Have your callsign ready — it is sent to the cluster as the login credential.

## Steps

1. Click `Settings > SpotHub...` to open the SpotHub dialog.
2. Click the **Cluster** tab.
3. In the **Server:** field, type the hostname of your DX cluster.
4. In the **Port:** field, set the telnet port (valid range: 1–65535).
5. In the **Callsign:** field, type your callsign.
6. Click **Connect**. The button label changes to **Disconnect** when the session is established. Raw cluster traffic appears in the **Cluster Console** read-only area.
7. Optional: to send a command to the cluster, type it in the command line field next to **Send** and click **Send**.
8. Optional: to reconnect automatically the next time AetherSDR starts, enable **Auto-connect on startup**.

## What each control does

| Control | Behavior | Setting key | Default | Range |
|---|---|---|---|---|
| **Server:** | Hostname of the DX cluster telnet server. | `ClusterHost` | — | — |
| **Port:** | Telnet port on the cluster server. | `ClusterPort` | — | 1–65535 |
| **Callsign:** | Login callsign sent to the cluster on connect. | `ClusterCallsign` | — | — |
| **Connect / Disconnect** | Toggles the telnet connection. Label reflects current state. | — | Connect | — |
| **Auto-connect on startup** | Reconnects to the cluster automatically at launch. | `ClusterAutoConnect` | — | — |
| **Cluster Console** | Read-only display of raw telnet traffic from the cluster. | — | — | — |
| **Send** | Sends the typed command to the cluster. Active only while connected. | — | — | — |
| **Spot Color:** | Opens a color picker to set the panadapter color for cluster spots. | `ClusterSpotColor` | — | — |

## Tips

- Spots appear on the panadapter only when the master spot overlay is enabled. If you see no spots after connecting, open the **Display** tab and confirm **Spots:** is set to Enabled (the default).
- Double-click any row in the **Spot List** tab to tune the active VFO to that spot's frequency. See [Tune to a spot by double-clicking the spot list](../../features/dx-cluster/tune-to-a-spot-by-double-clicking-the-spot-list.md).

## Troubleshooting

- **Button stays on "Connect" and the console shows "Error: ..."** — The hostname or port is wrong, or the cluster server is unreachable. Verify the server address and port, check your network connection, and try again.
- **No spots appear on the panadapter after connecting** — Confirm the **Spots:** toggle on the **Display** tab is Enabled. Also confirm the band of the incoming spots matches the panadapter's current frequency range.
- **Cluster Console is empty after connect** — Some clusters require you to send a command (such as your callsign again or `SET/DX`) before they stream spots. Type the command in the command line field and click **Send**.

## Related

- [SpotHub overview](../../features/dx-cluster/overview.md)
- [Connect to the Reverse Beacon Network](connect-to-the-reverse-beacon-network.md)
- [Tune to a spot by double-clicking the spot list](../../features/dx-cluster/tune-to-a-spot-by-double-clicking-the-spot-list.md)
- [Pick colors for each spot source](../../features/dx-cluster/pick-colors-for-each-spot-source.md)
- [Tune spot density, position, font size and lifetime](../../features/dx-cluster/tune-spot-density-position-font-size-and-lifetime.md)
- [Enable DXCC coloring from an ADIF log](../../features/dx-cluster/enable-dxcc-coloring-from-an-adif-log.md)
- [Clear all spots from the panadapter](../../features/dx-cluster/clear-all-spots-from-the-panadapter.md)
