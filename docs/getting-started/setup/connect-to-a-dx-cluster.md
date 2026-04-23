# Connect to a DX cluster

Open the SpotHub dialog and enter your cluster's hostname, port, and callsign so that DX spots appear as overlays on the panadapter.

## Before you start

- Know the hostname (or IP address) and telnet port of the DX cluster you want to use (for example, `dxc.k0xm.net`, port `23`).
- Have your callsign ready — the cluster uses it for login.

## Steps

1. Click `Settings > SpotHub...` to open the SpotHub dialog.
2. Click the **Cluster** tab.
3. In the **Server:** field, type the cluster hostname or IP address. This value is saved as `ClusterHost`.
4. In the **Port:** field, set the telnet port (valid range: 1–65535). This value is saved as `ClusterPort`.
5. In the **Callsign:** field, type your callsign. This value is saved as `ClusterCallsign`.
6. Click **Connect**. The button label changes to **Disconnect** when the session is established, and the **Cluster Console** shows `--- Connected ---`.
7. To connect automatically every time AetherSDR starts, click **Auto-connect on startup** so it is enabled. This value is saved as `ClusterAutoConnect`.

## What each control does

| Control | Behavior | Setting key | Default | Valid range |
|---|---|---|---|---|
| **Server:** | Hostname of the DX cluster. | `ClusterHost` | — | Any hostname or IP |
| **Port:** | Telnet port on the cluster. | `ClusterPort` | — | 1–65535 |
| **Callsign:** | Login callsign sent to the cluster on connect. | `ClusterCallsign` | — | — |
| **Connect / Disconnect** | Toggles the telnet connection. | — | Connect | — |
| **Auto-connect on startup** | Reconnects to this cluster each time AetherSDR launches. | `ClusterAutoConnect` | — | — |
| **Cluster Console** | Read-only display of raw cluster traffic. | — | — | — |
| **Send** (command line) | Sends a typed command to the connected cluster. | — | — | — |
| **Spot Color:** | Opens a color picker for cluster-sourced spots on the panadapter. | `ClusterSpotColor` | — | — |

## Tips

- The **Cluster Console** shows raw telnet output, including login prompts. If the cluster requires a password, type it in the command field and click **Send**.
- To tune directly to a spotted frequency, switch to the **Spot List** tab and double-click the row.
- Spot overlays on the panadapter are controlled globally by the **Spots:** toggle on the **Display** tab (`IsSpotsEnabled`, default: Enabled). If spots are not visible after connecting, check that toggle.

## Troubleshooting

- **Button stays as "Connect" after clicking** — The cluster hostname or port is incorrect, or the server is unreachable from your network. Check the **Cluster Console** for an error line and verify the hostname and port.
- **No spots appear on the panadapter despite being connected** — Confirm that **Spots:** on the **Display** tab is enabled. Also verify that the band of the incoming spots is not hidden via the **Bands:** checkboxes on the **Spot List** tab.
- **"Error: …" shown in the console** — The cluster rejected the connection or dropped it. This is often a login issue; watch the **Cluster Console** for the cluster's login prompt and send your callsign manually with **Send** to confirm the credentials.

## Related

- [SpotHub overview](../../features/dx-cluster/overview.md)
- [Connect to the Reverse Beacon Network](connect-to-the-reverse-beacon-network.md)
- [Tune to a spot by double-clicking the spot list](../../features/dx-cluster/tune-to-a-spot-by-double-clicking-the-spot-list.md)
- [Tune spot density, position, font size and lifetime](../../features/dx-cluster/tune-spot-density-position-font-size-and-lifetime.md)
- [Enable DXCC coloring from an ADIF log](../../features/dx-cluster/enable-dxcc-coloring-from-an-adif-log.md)
- [Pick colors for each spot source](../../features/dx-cluster/pick-colors-for-each-spot-source.md)
- [Clear all spots from the panadapter](../../features/dx-cluster/clear-all-spots-from-the-panadapter.md)
