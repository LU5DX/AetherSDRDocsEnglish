# SpotHub (formerly DX Cluster Dialog)

Central hub for connecting to DX spot sources — DX cluster, Reverse Beacon Network, WSJT-X, SpotCollector, POTA and FreeDV — and configuring how spots are displayed on the panadapter.

## Before you start

- Spot sources that use WebSocket (FreeDV) are available only in builds compiled with WebSocket support (`HAVE_WEBSOCKETS`). If the FreeDV tab is absent, your build does not include it.
- Spots appear on the panadapter only when the master spot overlay is enabled (see **Display** tab > **Spots:** toggle). If spots are not visible after connecting, verify that toggle is on.
- The dialog remembers its window geometry between sessions (saved to `DxClusterDialogGeometry`).

## Opening SpotHub

1. Open **Settings > SpotHub...**.

The dialog opens as a frameless, resizable window. Drag any edge to resize.

## Tabs overview

SpotHub has eight tabs, each corresponding to a spot source or display configuration:

- **Cluster** — DX cluster telnet connection, console and spot color
- **RBN** — Reverse Beacon Network telnet source with rate limiting
- **WSJT-X** — WSJT-X UDP listener with filters and color assignments
- **SpotCollector** — UDP listener for Ham Radio Deluxe SpotCollector broadcasts
- **POTA** — Polls `api.pota.app` for current activations
- **FreeDV** — WebSocket feed of FreeDV QSO reporter spots
- **Spot List** — Unified searchable table of all live spots
- **Display** — Panadapter spot visualization, Signal History and DXCC coloring

## Cluster tab

### Connection settings

| Control | Kind | Setting key | Behavior |
|---------|------|-------------|----------|
| **Server:** | Text field | `ClusterHost` | Hostname of DX cluster to connect to. |
| **Port:** | Spinbox (1-65535) | `ClusterPort` | Telnet port on DX cluster. |
| **Callsign:** | Text field | `ClusterCallsign` | Login callsign sent to cluster. |

### Connection controls

1. Fill in the connection settings above.
2. Click **Connect** to open the telnet session. The button label changes to **Disconnect** while connected; click it again to close.
3. Click **Auto-connect on startup** to have AetherSDR connect at launch. Setting: `ClusterAutoConnect`.

### Cluster console and commands

- **Cluster Console** — Read-only text field showing raw telnet traffic from the cluster.
- To send a command, type in the text field below the console and click **Send**.
- Click **Startup Commands…** to open an editor for commands that are sent automatically after every login. Enter one command per line — for example:
  ```
  SET/NAME YOUR_NAME
  SET/QTH YOUR_QTH
  ACCEPT/SPOT
  ```
  The commands are saved to `DxClusterStartupCommands` and are replayed each time the cluster connection re-establishes (not just on initial login). New in v26.5.2.1.

### Spot color

- **Spot Color:** — Opens a color picker for cluster spots. Setting: `ClusterSpotColor`.

## RBN tab

### Connection settings

| Control | Kind | Setting key | Behavior |
|---------|------|-------------|----------|
| **Server:** | Text field | `RbnHost` | RBN telnet hostname. |
| **Port:** | Spinbox (1-65535) | `RbnPort` | RBN telnet port. |
| **Callsign:** | Text field | `RbnCallsign` | Login callsign to RBN. |
| **Rate Limit:** | Spinbox | `RbnRateLimit` | Caps RBN spots per second. |

### Connection controls

1. Fill in the connection settings above.
2. Click **Connect** to open the telnet session. The button label changes to **Disconnect** while connected; click it again to close.
3. Click **Auto-connect on startup** to have AetherSDR connect at launch. Setting: `RbnAutoConnect`.

### RBN console and commands

- **RBN Console** — Read-only text field showing raw RBN traffic.
- To send a command, type in the text field below the console and click **Send**.
- Click **Startup Commands…** to open an editor for commands that are sent automatically after every login. Enter one command per line. The commands are saved to `RbnStartupCommands` and are replayed each time the RBN connection re-establishes. New in v26.5.2.1.

### Spot color

- **Spot Color:** — Opens a color picker for RBN spots. Setting: `RbnSpotColor`.

## WSJT-X tab

### Listener settings

| Control | Kind | Setting key | Behavior |
|---------|------|-------------|----------|
| **Address:** | Text field | `WsjtxAddress` | UDP bind address for WSJT-X messages. |
| **Port:** | Spinbox (1-65535) | `WsjtxPort` | UDP port for WSJT-X. |

### Connection controls

1. Set the address and port to match WSJT-X's Reporting settings.
2. Click **Start** to begin listening for WSJT-X UDP broadcasts. The button label changes to **Stop** while listening.
3. Click **Auto-start on startup** to have AetherSDR start listening at launch. Setting: `WsjtxAutoStart`.

### Filters

Check any of the following checkboxes to restrict which WSJT-X decodes appear:

| Control | Setting key | Behavior |
|---------|-------------|----------|
| **CQ** | `WsjtxFilterCQ` | Show only CQ calls. |
| **CQ POTA** | `WsjtxFilterPOTA` | Show only CQ POTA calls. |
| **Calling Me** | `WsjtxFilterCallingMe` | Show only decodes addressed to your callsign. |

### Color settings

Click each color swatch to open a color picker for that category:

| Control | Setting key | Behavior |
|---------|-------------|----------|
| **CQ color** | `WsjtxColorCQ` | Color for CQ spots. |
| **POTA color** | `WsjtxColorPOTA` | Color for CQ POTA spots. |
| **Calling Me color** | `WsjtxColorCallingMe` | Color for decodes addressed to your callsign. |
| **Default color** | `WsjtxColorDefault` | Color for all other WSJT-X spots. |

### Decode console and spot life

- **WSJT-X Decodes** — Read-only text field showing decoded transmissions.
- **Spot Life:** — Spinbox controlling how many seconds WSJT-X spots remain on the panadapter. Setting: `WsjtxSpotLife`.

## SpotCollector tab

### Listener settings

| Control | Kind | Setting key | Behavior |
|---------|------|-------------|----------|
| **UDP Port:** | Spinbox (1-65535) | `SpotCollectorPort` | UDP port SpotCollector broadcasts on. |

### Connection controls

1. Set the port to match your SpotCollector broadcast port.
2. Click **Start** to begin listening. The button label changes to **Stop** while listening.
3. Click **Auto-start on startup** to have AetherSDR start listening at launch. Setting: `SpotCollectorAutoStart`.

### Spot console

- **SpotCollector Spots** — Read-only text field showing received spots.

## POTA tab

### Connection settings

| Control | Kind | Setting key | Behavior |
|---------|------|-------------|----------|
| **Server:** | Indicator | None | Fixed endpoint: `api.pota.app (HTTP polling)`. |
| **Poll Interval:** | Spinbox | `PotaPollInterval` | Seconds between POTA polls. |

### Connection controls

1. Click **Start** to begin polling for current activations. The button label changes to **Stop** while polling.
2. Click **Auto-start on startup** to have AetherSDR start polling at launch. Setting: `PotaAutoStart`.

### Activations console and color

- **POTA Activations** — Read-only text field showing activation feed.
- **Spot Color:** — Opens a color picker for POTA spots. Setting: `PotaSpotColor`.

## FreeDV tab

### Connection settings

| Control | Kind | Setting key | Behavior |
|---------|------|-------------|----------|
| **Server:** | Indicator | None | Fixed endpoint: `qso.freedv.org (WebSocket)`. |

### Connection controls

1. Click **Start** to connect to the FreeDV WebSocket. The status indicator changes to **Connected** when the WebSocket handshake succeeds.
2. Click **Auto-start on startup** to have AetherSDR connect at launch. Setting: `FreeDvAutoStart`.

### Spots console and color

- **FreeDV Spots** — Read-only text field showing incoming FreeDV activity.
- **Spot Color:** — Opens a color picker for FreeDV spots. Setting: `FreeDvSpotColor`.

### Station Reporting

The **Station Reporting** group at the bottom of the FreeDV tab lets you broadcast your activity to the public FreeDV Reporter map at `qso.freedv.org` whenever the RADE modem is active.

#### Requirements before enabling

- A valid callsign must be present in the **Callsign:** field (or sourced from the radio).
- A valid Maidenhead grid square must be present in the **Grid Square:** field (or sourced from the radio's GPS).

If either value is blank when you check **Enable FreeDV Reporter reporting when RADE is active**, AetherSDR shows a warning and leaves the checkbox unchecked. This prevents blank or placeholder values from being broadcast to the shared public map.

#### Setup steps

1. In the **Station Reporting** group, review the **Callsign:** field.
   - If **Use radio** is checked (the default), the field is pre-filled with the callsign configured in your radio and is read-only. Changes to the radio's callsign in Radio Setup are reflected automatically.
   - Uncheck **Use radio** to enter a callsign manually. The entered value is saved to `FreeDvMyCallsign` and converted to upper case on save.
2. Review the **Grid Square:** field.
   - If your radio has GPS hardware and **Use GPS** is checked (the default on GPS-capable models), the field is pre-filled from the radio's GPS fix and is read-only. The **Use GPS** checkbox is hidden on radio models without GPS hardware.
   - Uncheck **Use GPS** (or if the checkbox is not present) to enter a grid square manually. The value is saved to `FreeDvMyGrid` and converted to upper case on save.
3. Optionally fill in **Station Msg:** with a short free-text note. This message appears beside your callsign on the public FreeDV Reporter map and is saved to `FreeDvMyMessage`.
4. Check **Enable FreeDV Reporter reporting when RADE is active**. AetherSDR validates callsign and grid before accepting the change, then saves `FreeDvAutoReport` = `True` and emits the reporting-enabled signal.

#### Station Reporting controls

| Control | Kind | Behavior |
|---------|------|----------|
| **Callsign:** | Text field | Callsign to report. Read-only when **Use radio** is checked. Saved to `FreeDvMyCallsign`. |
| **Use radio** | Checkbox | Pre-fills callsign from the radio's configured callsign. Saved to `FreeDvUseRadioCallsign`. |
| **Grid Square:** | Text field | Maidenhead grid square to report. Read-only when **Use GPS** is checked. Saved to `FreeDvMyGrid`. |
| **Use GPS** | Checkbox | Pre-fills grid from the radio's GPS module. Shown only on GPS-capable models. Saved to `FreeDvUseGpsGrid`. |
| **Station Msg:** | Text field | Optional message shown beside your callsign on the public map. Saved to `FreeDvMyMessage`. |
| **Enable FreeDV Reporter reporting when RADE is active** | Checkbox | Enables reporting to the public map. Saved to `FreeDvAutoReport`. |

## Spot List tab

The unified spot table shows all active spots from every connected source.

### Filtering by band

A row of checkboxes at the top lets you show or hide spots on specific bands (160m, 80m, 60m, 40m, 30m, 20m, 17m, 15m, 12m, 10m, 6m, 2m, etc.). Uncheck a band to remove its spots from the table.

The band checkboxes use a flow layout that wraps to a new row when the dialog is narrowed, keeping each checkbox readable instead of compressing labels.

### Clearing spots

Click **Clear** to empty the current spot list.

### Spot table

The main table is sortable by clicking column headers. Columns:

- **Time** — When the spot was received
- **Freq** — Frequency in MHz
- **DX Call** — The spotted callsign
- **Comment** — Spot comment (may include mode, name, etc.)
- **Spotter** — Who spotted the DX station
- **Band** — Band (e.g., 20m)
- **Mode** — Mode if included in the spot
- **Source** — Which source provided this spot (Cluster, RBN, WSJT-X, SpotCollector, POTA, FreeDV)

### Column visibility

Right-click any column header to open the column visibility menu. AetherSDR keeps the menu open