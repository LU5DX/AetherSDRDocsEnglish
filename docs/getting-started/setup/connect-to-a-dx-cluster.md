# Connect to a DX cluster

AetherSDR's SpotHub dialog lets you connect to a DX cluster via telnet and display incoming spots on the panadapter. Use this page to make that first connection and optionally reconnect automatically on every launch.

## Before you start

- Know the hostname and port of the DX cluster you want to use (for example, `dxc.k0xm.net`, port `23`).
- Have your callsign ready to use as the login credential.

## Steps

1. Open `Settings > SpotHub...`.
2. Click the **Cluster** tab.
3. In the **Server:** field, enter the cluster hostname.
4. In the **Port:** field, enter the telnet port (valid range: 1–65535).
5. In the **Callsign:** field, enter the callsign you want to log in with.
6. Click **Connect**.
7. Watch the **Cluster Console** area for the cluster's login banner and spot traffic to confirm the connection is live.
8. To type a command to the cluster, enter it in the command line field beneath the console and click **Send**.

## What each control does

| Control | Behavior | Setting key |
|---|---|---|
| **Server:** | Hostname of the DX cluster to connect to. | `ClusterHost` |
| **Port:** | Telnet port on the DX cluster. Valid range: 1–65535. | `ClusterPort` |
| **Callsign:** | Login callsign sent to the cluster at connect time. | `ClusterCallsign` |
| **Connect / Disconnect** | Toggles the telnet connection. Label switches to "Disconnect" while connected. | — |
| **Auto-connect on startup** | When enabled, AetherSDR connects to the cluster automatically at launch. | `ClusterAutoConnect` |
| **Cluster Console** | Read-only display of raw telnet traffic from the cluster. | — |
| **Send** | Sends the typed command to the cluster. Only active while connected. | — |
| **Spot Color:** | Opens a color picker to set the color used for cluster spots on the panadapter. | `ClusterSpotColor` |

## Tips

- Spots from the cluster appear in the unified **Spot List** tab alongside spots from other sources. The **Source** column identifies them as "Cluster".
- Double-click any row in the spot table to tune the radio to that frequency. See [Tune to a spot by double-clicking the spot list](../../features/dx-cluster/tune-to-a-spot-by-double-clicking-the-spot-list.md).
- The master spot overlay on the panadapter must be enabled. Go to the **Display** tab and confirm **Spots:** is set to Enabled (the default). If spots are not visible, check that control first.
- Per-source spot colors can be changed at any time without disconnecting.

## Troubleshooting

- **"Disconnect" button appears but no spots arrive** — The cluster may require a specific login command after the banner. Type the appropriate command (for example, `SET/SKIMMER` or `SET/DX`) in the command line and click **Send**.
- **Status shows an error in red** — The hostname or port is unreachable. Verify the **Server:** and **Port:** values and confirm your network path to the cluster host.
- **Spots appear in the Spot List but not on the panadapter** — Open the **Display** tab and confirm **Spots:** is Enabled. Also verify the radio is tuned to a band that has active spots.

## Related

- [SpotHub overview](../../features/dx-cluster/overview.md)
- [Connect to the Reverse Beacon Network](connect-to-the-reverse-beacon-network.md)
- [Tune to a spot by double-clicking the spot list](../../features/dx-cluster/tune-to-a-spot-by-double-clicking-the-spot-list.md)
- [Pick colors for each spot source](../../features/dx-cluster/pick-colors-for-each-spot-source.md)
- [Tune spot density, position, font size and lifetime](../../features/dx-cluster/tune-spot-density-position-font-size-and-lifetime.md)
- [Enable DXCC coloring from an ADIF log](../../features/dx-cluster/enable-dxcc-coloring-from-an-adif-log.md)
- [Start WSJT-X UDP listener and filter for CQ, POTA or calls to me](../../features/dx-cluster/start-wsjt-x-udp-listener-and-filter-for-cq-pota-or-calls-to-me.md)
