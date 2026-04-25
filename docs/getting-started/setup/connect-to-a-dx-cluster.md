# Connect to a DX cluster

AetherSDR's SpotHub dialog lets you connect to a telnet DX cluster and show incoming spots as overlays on the panadapter. Use this page to make your first connection and optionally reconnect automatically on every launch.

## Before you start

- Know the hostname (or IP address) and telnet port of your chosen DX cluster (for example, `dxc.k0xm.net` on port `7373`).
- Know the callsign you will use to log in to the cluster.

## Steps

1. Open `Settings > SpotHub...`.
2. Click the **Cluster** tab.
3. In the **Server:** field, type the cluster hostname or IP address. This saves to `ClusterHost`.
4. In the **Port:** field, set the telnet port (1–65535). This saves to `ClusterPort`.
5. In the **Callsign:** field, type your callsign. This saves to `ClusterCallsign`.
6. Click **Connect**.
   - The status indicator changes to **Connected** and the button label changes to **Disconnect**.
   - Incoming cluster traffic appears in the **Cluster Console** read-only display.
7. To reconnect automatically every time AetherSDR starts, enable **Auto-connect on startup**. This saves to `ClusterAutoConnect`.

## What each control does

| Control | Description | Setting key |
|---|---|---|
| **Server:** | Hostname or IP address of the DX cluster telnet server. | `ClusterHost` |
| **Port:** | Telnet port. Valid range: 1–65535. | `ClusterPort` |
| **Callsign:** | Login callsign sent to the cluster on connect. | `ClusterCallsign` |
| **Connect / Disconnect** | Toggles the telnet connection. Label shows current action. | — |
| **Auto-connect on startup** | Connects to the cluster automatically when AetherSDR launches. | `ClusterAutoConnect` |
| **Cluster Console** | Read-only display of raw telnet traffic from the cluster. | — |
| **Send** (command line) | Sends a typed command to the cluster while connected. | — |
| **Spot Color:** | Opens a color picker for cluster spot overlays on the panadapter. | `ClusterSpotColor` |

## Tips

- While connected, type a cluster command in the field next to **Send** and click **Send** to interact with the cluster directly (for example, `set/dx` or `sh/dx 20`).
- Spot overlays appear on the panadapter only when the master **Spots:** toggle on the **Display** tab is enabled (default: Enabled, saved to `IsSpotsEnabled`).
- To review recent cluster traffic from before you opened SpotHub, scroll up in the **Cluster Console** — AetherSDR loads up to the last 500 lines from the cluster log file when the dialog opens.

## Troubleshooting

- **Status shows "Error: ..."** — The hostname or port is wrong, or the cluster server is unreachable. Verify the address and port, then click **Connect** again.
- **Cluster Console is empty after connecting** — Some clusters require you to send your callsign as the first command. Type your callsign in the command field and click **Send**.
- **Spots do not appear on the panadapter** — Open the **Display** tab and confirm **Spots:** is enabled.

## Related

- [SpotHub overview](../../features/dx-cluster/overview.md)
- [Connect to the Reverse Beacon Network](connect-to-the-reverse-beacon-network.md)
- [Tune to a spot by double-clicking the spot list](../../features/dx-cluster/tune-to-a-spot-by-double-clicking-the-spot-list.md)
- [Pick colors for each spot source](../../features/dx-cluster/pick-colors-for-each-spot-source.md)
- [Tune spot density, position, font size and lifetime](../../features/dx-cluster/tune-spot-density-position-font-size-and-lifetime.md)
- [Enable DXCC coloring from an ADIF log](../../features/dx-cluster/enable-dxcc-coloring-from-an-adif-log.md)
- [Clear all spots from the panadapter](../../features/dx-cluster/clear-all-spots-from-the-panadapter.md)
