# Connect to the Reverse Beacon Network

The Reverse Beacon Network (RBN) automatically spots CW, RTTY, and digital signals heard by a worldwide network of skimmer stations. This page explains how to connect AetherSDR to the RBN telnet feed so that RBN spots appear on your panadapter.

## Before you start

- Know your callsign — it is used as the login credential for the RBN telnet server.
- Know the RBN telnet server hostname and port. The standard public server is `rbn.telegraphy.de` on port `7000`, but confirm with [reversebeacon.net](https://www.reversebeacon.net) if the address has changed.
- Spot display on the panadapter requires the master spot overlay to be enabled (see the Display tab, `IsSpotsEnabled`).

## Steps

1. Click `Settings > SpotHub...` to open the SpotHub dialog.
2. Click the **RBN** tab.
3. In the **Server:** field, enter the RBN telnet hostname (persisted as `RbnHost`).
4. In the **Port:** spinbox, enter the telnet port in the range 1–65535 (persisted as `RbnPort`).
5. In the **Callsign:** field, enter your callsign (persisted as `RbnCallsign`).
6. If you want to limit how many spots per second are processed, set **Rate Limit:** to your preferred value (persisted as `RbnRateLimit`).
7. Click **Connect**. The button label changes to **Disconnect** and the console area below shows `--- Connected ---` followed by incoming RBN traffic in the **RBN Console**.
8. To connect automatically every time AetherSDR starts, click **Auto-connect on startup** so it is active (persisted as `RbnAutoConnect`).
9. To choose a display color for RBN spots on the panadapter, click **Spot Color:** and select a color from the picker (persisted as `RbnSpotColor`).

## What each control does

| Control | Behavior | Setting key | Valid range / default |
|---|---|---|---|
| **Server:** | Hostname of the RBN telnet server. | `RbnHost` | Any hostname |
| **Port:** | Telnet port on the RBN server. | `RbnPort` | 1–65535 |
| **Callsign:** | Login callsign sent to the RBN on connect. | `RbnCallsign` | Your callsign |
| **Rate Limit:** | Maximum RBN spots processed per second. | `RbnRateLimit` | See spinbox range |
| **Connect / Disconnect** | Toggles the telnet connection to the RBN. | — | Default label: Connect |
| **Auto-connect on startup** | Connects to the RBN automatically when AetherSDR launches. | `RbnAutoConnect` | — |
| **RBN Console** | Read-only display of raw incoming RBN telnet traffic. | — | — |
| **Send** | Sends a typed command to the RBN session. | — | — |
| **Spot Color:** | Opens a color picker for RBN spots shown on the panadapter. | `RbnSpotColor` | — |

## Tips

- The **Rate Limit:** control is useful on a busy contest weekend when the RBN can produce hundreds of spots per second. Lowering it prevents the spot list and panadapter from being overwhelmed.
- You can type RBN telnet commands (for example, `set/skimmer` or `set/dx`) into the command line below the console and click **Send** to send them to the server.
- RBN spots appear alongside DX cluster spots in the **Spot List** tab. Use the band checkboxes there to filter by band. Double-click any row to tune directly to that frequency.

## Troubleshooting

- **Button stays on "Connect" and console shows an error** — The hostname or port is incorrect, or a firewall is blocking outbound telnet. Verify the server address and port, and check that your network allows outbound TCP on the configured port.
- **Spots appear in the console but not on the panadapter** — The master spot overlay may be disabled. Open the **Display** tab in SpotHub and confirm that **Spots:** is enabled (`IsSpotsEnabled`). Also confirm that a radio slice is open and visible.
- **"Auto-connect on startup" does not reconnect after a network dropout** — Auto-connect fires only at application launch. If the session drops mid-session, click **Connect** manually to reconnect.

## Related

- [SpotHub overview](../../features/dx-cluster/overview.md)
- [Connect to a DX cluster](connect-to-a-dx-cluster.md)
- [Tune spot density, position, font size and lifetime](../../features/dx-cluster/tune-spot-density-position-font-size-and-lifetime.md)
- [Pick colors for each spot source](../../features/dx-cluster/pick-colors-for-each-spot-source.md)
- [Tune to a spot by double-clicking the spot list](../../features/dx-cluster/tune-to-a-spot-by-double-clicking-the-spot-list.md)
- [Enable DXCC coloring from an ADIF log](../../features/dx-cluster/enable-dxcc-coloring-from-an-adif-log.md)
