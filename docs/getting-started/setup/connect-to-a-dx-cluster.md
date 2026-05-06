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
| **Auto Mode:** | Automatically switches the slice mode when clicking a spot that includes mode information (e.g. CW, FT8, RTTY). Enabled by default. | `SpotsAutoMode` |
| **Spot Lines:** | Draws vertical lines from the spectrum up to each spot label. Disable during contests to reduce visual clutter. New in v0.9.7. | `IsSpotsLinesEnabled` |
| **Enable FreeDV Reporter reporting when RADE is active** | Enables station-reporting to the public FreeDV Reporter map (qso.freedv.org) whenever the RADE modem is active. Requires a valid callsign and grid square; the checkbox refuses to enable and shows a warning if either field is blank or unresolvable. | `FreeDvAutoReport` |
| **Callsign:** (FreeDV Reporter) | Callsign to report to the FreeDV Reporter map. Read-only when **Use radio** is checked. Automatically updated if the radio's configured callsign changes while **Use radio** is checked. | `FreeDvMyCallsign` |
| **Use radio** (callsign) | Pre-fills the callsign field from the radio's configured callsign and locks the field read-only. Enabled by default. | `FreeDvUseRadioCallsign` |
| **Grid Square:** (FreeDV Reporter) | Maidenhead grid square to report (up to six characters). Read-only when **Use GPS** is checked. | `FreeDvMyGrid` |
| **Use GPS** (grid) | Pre-fills the grid field from the radio's GPS module and locks the field read-only. Only shown on radio models that have GPS hardware. | `FreeDvUseGpsGrid` |
| **Station Msg:** (FreeDV Reporter) | Optional free-text message shown beside the callsign on the public FreeDV Reporter map. | `FreeDvMyMessage` |
| **Total Spots:** | Live readout of how many spots are currently tracked across all sources. Updated whenever spots are added or cleared. Resets to 0 when **Clear All Spots** is pressed. | — |

## Tuning to a spot by double-clicking

Double-clicking a row in the **Spot List** tab tunes the active slice to the spot's frequency. As of v0.9.7, AetherSDR also forwards mode information extracted from the spot comment, so the slice switches to the appropriate mode (for example, CW or SSB) to match the spot rather than only changing frequency.

## FreeDV Reporter reporting

The **Station Reporting** group on the **FreeDV** tab lets AetherSDR broadcast your station's activity to the public FreeDV Reporter map at qso.freedv.org while the RADE modem is active.

### Requirements

- The FreeDV tab and all reporting controls are only present in builds compiled with `HAVE_WEBSOCKETS`. On Windows, the **Enable FreeDV Reporter reporting when RADE is active** checkbox additionally requires `HAVE_RADE`.
- Both a callsign and a grid square must be resolvable before reporting can be enabled. If either is blank when you check **Enable FreeDV Reporter reporting when RADE is active**, AetherSDR shows a warning dialog and leaves the checkbox unchecked.

### Setting up reporting

1. Open `Settings > SpotHub...` and click the **FreeDV** tab.
2. In the **Station Reporting** group, confirm or enter your callsign:
   - If **Use radio** is checked (default), the **Callsign:** field is filled automatically from the radio's configured callsign and is read-only. Uncheck **Use radio** to type a different callsign.
3. Confirm or enter your grid square:
   - If **Use GPS** is checked (default, GPS-capable radios only), the **Grid Square:** field is filled from the radio's GPS and is read-only. Uncheck **Use GPS** to type a grid square manually.
4. Optionally, enter a short message in **Station Msg:** to appear beside your callsign on the map.
5. Check **Enable FreeDV Reporter reporting when RADE is active**.
   - If both callsign and grid square are present, reporting is enabled and saved to `FreeDvAutoReport`.
   - If either is missing, a warning dialog appears and the checkbox remains unchecked. Fill in the missing field and try again.

### Reporting controls

| Control | Description | Setting key |
|---|---|---|
| **Enable FreeDV Reporter reporting when RADE is active** | Master switch for public map reporting. Blocked if callsign or grid square is blank. | `FreeDvAutoReport` |
| **Callsign:** | Callsign sent to the FreeDV Reporter map. | `FreeDvMyCallsign` |
| **Use radio** | Copies the callsign from the radio and locks the field read-only. | `FreeDvUseRadioCallsign` |
| **Grid Square:** | Maidenhead locator sent to the FreeDV Reporter map. | `FreeDvMyGrid` |
| **Use GPS** | Copies the grid from the radio's GPS and locks the field read-only. Visible only on GPS-capable radio models. | `FreeDvUseGpsGrid` |
| **Station Msg:** | Optional free-text status line shown on the public map. | `FreeDvMyMessage` |

## Display tab: Auto Mode default changed

As of v0.9.5.1, the **Auto Mode:** toggle defaults to **Enabled**. In previous releases the default was **Disabled**. `SpotsAutoMode` is saved as `True` unless you have previously set it otherwise. If you preferred the old behavior, open the **Display** tab and disable **Auto Mode:**.

## Display tab: Spot Lines (new in v0.9.7)

The **Spot Lines:** toggle on the **Display** tab controls whether AetherSDR draws a vertical line from the spectrum baseline up to each spot label on the panadapter. The toggle defaults to **Enabled** and saves to `IsSpotsLinesEnabled`.

Disable **Spot Lines:** during contests or when the panadapter is heavily populated with spots to reduce visual clutter.

## Tips

- While connected, type a cluster command in the field next to **Send** and click **Send** to interact with the cluster directly (for example, `set/dx` or `sh/dx 20`).
- Spot overlays appear on the panadapter only when the master **Spots:** toggle on the **Display** tab is enabled (default: Enabled, saved to `IsSpotsEnabled`).
- To review recent cluster traffic from before you opened SpotHub, scroll up in the **Cluster Console** — AetherSDR loads up to the last 500 lines from the cluster log file when the dialog opens.
- If your radio's callsign changes in Radio Setup while **Use radio** is checked, the **Callsign:** field in the FreeDV Reporter section updates automatically.
- **Auto Mode** defaults to Enabled. When you double-click a spot that carries mode information (e.g. CW, FT8, RTTY), AetherSDR automatically switches the slice to that mode. As of v0.9.7, mode information is parsed from the spot comment using a shared resolver, so mode detection is consistent across all spot sources.
- Disable **Spot Lines:** on the **Display** tab during contests to reduce panadapter clutter while keeping spot labels visible.

## Troubleshooting

- **Status shows "Error: ..."** — The hostname or port is wrong, or the cluster server is unreachable. Verify the address and port, then click **Connect** again.
- **Cluster Console is empty after connecting** — Some clusters require you to send your callsign as the first command. Type your callsign in the command field and click **Send**.
- **Spots do not appear on the panadapter** — Open the **Display** tab and confirm **Spots:** is enabled.
- **Double-clicking a spot does not switch mode** — Confirm **Auto Mode:** is enabled on the **Display** tab. Mode switching requires that the spot comment contains a recognizable mode token (e.g. CW, FT8, SSB).
- **Enable FreeDV Reporter reporting when RADE is active checkbox cannot be checked** — A warning dialog will explain that the callsign or grid square is missing. Fill in both fields (or enable **Use radio** / **Use GPS** so they populate automatically) and try again.
- **FreeDV tab is not visible** — Your build of AetherSDR was compiled without WebSocket support (`HAVE_WEBSOCKETS`). Contact your package provider for a build that includes FreeDV features.

## Related

- [SpotHub overview](../../features/dx-cluster/overview.md)
- [Connect to the Reverse Beacon Network](connect-to-the-reverse-beacon-network.md)
- [Tune to a spot by double-clicking the spot list](../../features/dx-cluster/tune-to-a-spot-by-double-clicking-the-spot-list.md)
- [Pick colors for each spot source](../../features/dx-cluster/pick-colors-for-each-spot-source.md)
- [Tune spot density, position, font size and lifetime](../../features/dx-cluster/tune-spot-density-position-font-size-and-lifetime.md)
- [Enable DXCC coloring from an ADIF log](../../features/dx-cluster/enable-dxcc-coloring-from-an-adif-log.md)
- [Clear all spots from the panadapter](../../features/dx-cluster/clear-all-spots-from-the-panadapter.md)
<!-- docmesh:llm version=V0.9.7 date=2026-05-03 -->