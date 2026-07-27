# Connect to a DX cluster

AetherSDR's SpotHub dialog lets you connect to a telnet DX cluster, the Reverse Beacon Network, WSJT-X, SpotCollector, POTA, and FreeDV, and configure how incoming spots display as overlays on the panadapter.

## Before you start

- Know the hostname (or IP address) and telnet port of your chosen DX cluster (for example, `dxc.k0xm.net` on port `7373`).
- Know the callsign you will use to log in to the cluster.

## Opening SpotHub

1. Open `Settings > SpotHub...`.

## Cluster tab

### Connecting to a DX cluster

1. Click the **Cluster** tab.
2. In the **Server:** field, type the cluster hostname or IP address. This saves to `ClusterHost`.
3. In the **Port:** field, set the telnet port (1–65535). This saves to `ClusterPort`.
4. In the **Callsign:** field, type your callsign. This saves to `ClusterCallsign`.
5. Click **Connect**.
   - The status indicator changes to **Connected** and the button label changes to **Disconnect**.
   - Incoming cluster traffic appears in the **Cluster Console** read-only display.
6. To reconnect automatically every time AetherSDR starts, enable **Auto-connect on startup**. This saves to `ClusterAutoConnect`.

### Setting startup commands for the DX cluster

You can configure a list of commands that are sent automatically after every login to the DX cluster (for example, `SET/NAME`, `SET/QTH`, `ACCEPT/SPOT`).

1. Click **Startup Commands…**.
2. In the dialog, enter one command per line.
3. Click **OK** to save. The commands are stored in the `DxClusterStartupCommands` setting and are replayed by the client after every successful login.

### What each control does on the Cluster tab

| Control | Description | Setting key |
|---|---|---|
| **Server:** | Hostname or IP address of the DX cluster telnet server. | `ClusterHost` |
| **Port:** | Telnet port. Valid range: 1–65535. | `ClusterPort` |
| **Callsign:** | Login callsign sent to the cluster on connect. | `ClusterCallsign` |
| **Connect / Disconnect** | Toggles the telnet connection. Label shows current action. | — |
| **Auto-connect on startup** | Connects to the cluster automatically when AetherSDR launches. | `ClusterAutoConnect` |
| **Startup Commands…** | Opens a dialog to edit commands sent automatically after every login. One command per line. New in v26.5.2.1. | `DxClusterStartupCommands` |
| **Cluster Console** | Read-only display of raw telnet traffic from the cluster. | — |
| **Send** (command line) | Sends a typed command to the cluster while connected. | — |
| **Spot Color:** | Opens a color picker for cluster spot overlays on the panadapter. | `ClusterSpotColor` |

## RBN tab

### Connecting to the Reverse Beacon Network

1. Click the **RBN** tab.
2. In the **Server:** field, type the RBN telnet hostname. This saves to `RbnHost`.
3. In the **Port:** field, set the RBN telnet port (1–65535). This saves to `RbnPort`.
4. In the **Callsign:** field, type your login callsign. This saves to `RbnCallsign`.
5. Set the **Rate Limit:** to cap the number of RBN spots processed per second. This saves to `RbnRateLimit`.
6. Click **Connect**.
7. To reconnect automatically on launch, enable **Auto-connect on startup**. This saves to `RbnAutoConnect`.

### Setting startup commands for the RBN

You can configure a list of commands that are sent automatically after every login to the RBN (for example, `SET/NAME`, `SET/QTH`, `ACCEPT/SPOT`).

1. Click **Startup Commands…**.
2. In the dialog, enter one command per line.
3. Click **OK** to save. The commands are stored in the `RbnStartupCommands` setting and are replayed by the RBN client after every successful login.

### What each control does on the RBN tab

| Control | Description | Setting key |
|---|---|---|
| **Server:** | RBN telnet hostname. | `RbnHost` |
| **Port:** | RBN telnet port. Valid range: 1–65535. | `RbnPort` |
| **Callsign:** | Login callsign to RBN. | `RbnCallsign` |
| **Rate Limit:** | Caps RBN spots per second. | `RbnRateLimit` |
| **Connect / Disconnect** | Toggles RBN connection. | — |
| **Auto-connect on startup** | Starts RBN automatically on launch. | `RbnAutoConnect` |
| **Startup Commands…** | Opens a dialog to edit commands sent automatically after every login to the RBN. One command per line. New in v26.5.2.1. | `RbnStartupCommands` |
| **RBN Console** | Read-only console of RBN traffic. | — |
| **Send** | Sends command to RBN. | — |
| **Spot Color:** | Color picker for RBN spots. | `RbnSpotColor` |

## WSJT-X tab

### Listening for WSJT-X spots

1. Click the **WSJT-X** tab.
2. In the **Address:** field, enter the UDP bind address for WSJT-X messages. This saves to `WsjtxAddress`.
3. In the **Port:** field, set the UDP port. This saves to `WsjtxPort`.
4. Click **Start** to begin listening. The status changes to **Listening**.
5. To auto-start on launch, enable **Auto-start on startup**. This saves to `WsjtxAutoStart`.

### Filtering WSJT-X decodes

Use the checkboxes to filter which decodes appear as spots:

- **CQ** — Show only CQ calls. Saves to `WsjtxFilterCQ`.
- **CQ POTA** — Show CQ POTA calls. Saves to `WsjtxFilterPOTA`.
- **Calling Me** — Show only decodes addressed to your callsign. Saves to `WsjtxFilterCallingMe`.

### Customizing WSJT-X spot colors

Click any color swatch to open a color picker:

- **CQ color** — Saves to `WsjtxColorCQ`.
- **POTA color** — Saves to `WsjtxColorPOTA`.
- **Calling Me color** — Saves to `WsjtxColorCallingMe`.
- **Default color** — Saves to `WsjtxColorDefault`.

### What each control does on the WSJT-X tab

| Control | Description | Setting key |
|---|---|---|
| **Address:** | UDP bind address for WSJT-X messages. | `WsjtxAddress` |
| **Port:** | UDP port for WSJT-X. Valid range: 1–65535. | `WsjtxPort` |
| **Start / Stop** | Starts or stops UDP listener. | — |
| **Auto-start on startup** | Auto-starts listener on launch. | `WsjtxAutoStart` |
| **CQ** | Show only CQ calls from WSJT-X. | `WsjtxFilterCQ` |
| **CQ POTA** | Show CQ POTA calls. | `WsjtxFilterPOTA` |
| **Calling Me** | Show only decodes addressed to your callsign. | `WsjtxFilterCallingMe` |
| **CQ color** | Color picker for CQ spots. | `WsjtxColorCQ` |
| **POTA color** | Color picker for POTA spots. | `WsjtxColorPOTA` |
| **Calling Me color** | Color picker for Calling Me spots. | `WsjtxColorCallingMe` |
| **Default color** | Color picker for other WSJT-X spots. | `WsjtxColorDefault` |
| **WSJT-X Decodes** | Console of decoded transmissions. | — |
| **Spot Life:** | Seconds WSJT-X spots remain on panadapter. | `WsjtxSpotLife` |

## SpotCollector tab

### Listening for SpotCollector broadcasts

1. Click the **SpotCollector** tab.
2. In the **UDP Port:** field, set the port SpotCollector broadcasts on. This saves to `SpotCollectorPort`.
3. Click **Start** to begin listening. The status changes to **Listening**.
4. To auto-start on launch, enable **Auto-start on startup**. This saves to `SpotCollectorAutoStart`.

### What each control does on the SpotCollector tab

| Control | Description | Setting key |
|---|---|---|
| **UDP Port:** | UDP port SpotCollector broadcasts on. Valid range: 1–65535. | `SpotCollectorPort` |
| **Start / Stop** | Starts or stops UDP listener. | — |
| **Auto-start on startup** | Auto-starts listener on launch. | `SpotCollectorAutoStart` |
| **SpotCollector Spots** | Console of received SpotCollector spots. | — |

## POTA tab

### Polling POTA activations

1. Click the **POTA** tab.
2. Set **Poll Interval:** to the seconds between polls. This saves to `PotaPollInterval`.
3. Click **Start** to begin polling. The status changes to **Polling**.
4. To auto-start on launch, enable **Auto-start on startup**. This saves to `PotaAutoStart`.

### What each control does on the POTA tab

| Control | Description | Setting key |
|---|---|---|
| **Server:** | Fixed endpoint: `api.pota.app` (HTTP polling). | — |
| **Poll Interval:** | Seconds between POTA polls. | `PotaPollInterval` |
| **Start / Stop** | Starts or stops POTA polling. | — |
| **Auto-start on startup** | Auto-starts POTA on launch. | `PotaAutoStart` |
| **POTA Activations** | Console of activation feed. | — |
| **Spot Color:** | Color picker for POTA spots. | `PotaSpotColor` |

## FreeDV tab

### Connecting to FreeDV

> **Note:** The FreeDV tab is only present in builds compiled with WebSocket support (`HAVE_WEBSOCKETS`).

1. Click the **FreeDV** tab.
2. Click **Start** to connect to the FreeDV WebSocket feed. The status changes to **Connected**.
3. To auto-start on launch, enable **Auto-start on startup**. This saves to `FreeDvAutoStart`.

### What each control does on the FreeDV tab

| Control | Description | Setting key |
|---|---|---|
| **Server:** | Fixed endpoint: `qso.freedv.org` (WebSocket). | — |
| **Start / Stop** | Connects or disconnects the FreeDV WebSocket. | — |
| **Auto-start on startup** | Auto-starts FreeDV on launch. | `FreeDvAutoStart` |
| **FreeDV Spots** | Console of FreeDV activity. | — |
| **Spot Color:** | Color picker for FreeDV spots. | `FreeDvSpotColor` |

## Spot List tab

### Viewing and filtering spots

1. Click the **Spot List** tab.
2. Use the band checkboxes to toggle visibility of spots on each band (160m, 80m, 60m, 40m, 30m, 20m, 17m, 15m, 12m, 10m, 6m, 2m, etc.). The checkboxes use a flow layout that wraps to additional lines when the dialog is too narrow to display them all in one row.
3. Click **Clear** to empty the current spot list.

### Tuning to a spot

Double-click a row in the spot table to tune the active slice to the spot's frequency. As of v0.9.7, AetherSDR also forwards mode information extracted from the spot comment, so the slice switches to the appropriate mode (for example, CW or SSB) to match the spot rather than only changing frequency.

### Customizing table columns

Right-click the table header to open a column visibility menu. The menu stays open while you toggle checkable columns, so you can show or hide multiple columns (for example, Spotter, Band, Mode) in a single pass without the menu closing after each toggle.

### What each control does on the Spot List tab

| Control | Description | Setting key |
|---|---|---|
| **Bands:** | Per-band checkboxes toggle visibility in table. The checkboxes wrap to additional rows when the dialog is narrow. | — |
| **Clear** | Empties current spot list. | — |
| **Spot table** | Sortable table of spots. Columns: Time, Freq, DX Call, Comment, Spotter, Band, Mode, Source. Right-click header to show/hide columns without the menu closing between toggles. | — |

## Display tab

### Configuring spot overlay appearance

The **Display** tab controls how spots are visualized on the panadapter.

#### Master toggles

| Control | Description | Setting key |
|---|---|---|
| **Spots:** | Master toggle for DX spot overlay on the panadapter. Default: Enabled. | `IsSpotsEnabled` |
| **Memories:** | Toggles