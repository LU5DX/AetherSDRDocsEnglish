# SpotHub (DX Cluster Dialog)

The SpotHub dialog is the central hub for connecting to DX spot sources — DX cluster, Reverse Beacon Network, WSJT-X, SpotCollector, POTA and FreeDV — and configuring how spots are displayed on the panadapter.

## Opening SpotHub

1. Click **Settings > SpotHub...** in the main menu.
2. The SpotHub dialog opens with tabs for each spot source and a **Display** tab for visualization settings.

---

## Spot Sources

### Cluster (Tab)

Connect to a traditional DX cluster via telnet.

| Control | Setting key | Behavior |
|---------|-------------|----------|
| **Server:** | `ClusterHost` | Hostname of DX cluster to connect to. |
| **Port:** | `ClusterPort` | Telnet port on DX cluster. Range: 1–65535. |
| **Callsign:** | `ClusterCallsign` | Login callsign sent to cluster. |
| **Connect / Disconnect** | — | Toggles telnet connection to the cluster. |
| **Auto-connect on startup** | `ClusterAutoConnect` | Auto-connects cluster on launch. |
| **Cluster Console** | — | Read-only telnet console of raw cluster traffic. |
| **Send** | — | Sends a typed command to the cluster. |
| **Spot Color:** | `ClusterSpotColor` | Opens a color picker for cluster spots. |

### RBN (Tab)

Connect to the Reverse Beacon Network telnet source with rate limiting.

| Control | Setting key | Behavior |
|---------|-------------|----------|
| **Server:** | `RbnHost` | RBN telnet hostname. |
| **Port:** | `RbnPort` | RBN telnet port. Range: 1–65535. |
| **Callsign:** | `RbnCallsign` | Login callsign to RBN. |
| **Rate Limit:** | `RbnRateLimit` | Caps RBN spots per second. |
| **Connect / Disconnect (RBN)** | — | Toggles RBN connection. |
| **Auto-connect on startup (RBN)** | `RbnAutoConnect` | Starts RBN automatically. |
| **RBN Console** | — | Read-only console of RBN traffic. |
| **Send (RBN)** | — | Sends command to RBN. |
| **Spot Color: (RBN)** | `RbnSpotColor` | Color picker for RBN spots. |

### WSJT-X (Tab)

Listen for WSJT-X UDP broadcasts with filters and colors.

| Control | Setting key | Behavior |
|---------|-------------|----------|
| **Address:** | `WsjtxAddress` | UDP bind address for WSJT-X messages. |
| **Port:** | `WsjtxPort` | UDP port for WSJT-X. Range: 1–65535. |
| **Start / Stop** | — | Starts or stops UDP listener. |
| **Auto-start on startup (WSJT-X)** | `WsjtxAutoStart` | Auto-starts listener on launch. |
| **CQ** | `WsjtxFilterCQ` | Show only CQ calls from WSJT-X. |
| **CQ POTA** | `WsjtxFilterPOTA` | Show CQ POTA calls. |
| **Calling Me** | `WsjtxFilterCallingMe` | Show only decodes addressed to your callsign. |
| **CQ color** | `WsjtxColorCQ` | Color picker for CQ spots. |
| **POTA color** | `WsjtxColorPOTA` | Color picker for POTA spots. |
| **Calling Me color** | `WsjtxColorCallingMe` | Color picker for Calling Me spots. |
| **Default color** | `WsjtxColorDefault` | Color picker for other WSJT-X spots. |
| **WSJT-X Decodes** | — | Console of decoded transmissions. |
| **Spot Life:** | `WsjtxSpotLife` | Seconds WSJT-X spots remain on panadapter. |

### SpotCollector (Tab)

Listen for Ham Radio Deluxe SpotCollector UDP broadcasts.

| Control | Setting key | Behavior |
|---------|-------------|----------|
| **UDP Port:** | `SpotCollectorPort` | UDP port SpotCollector broadcasts on. Range: 1–65535. |
| **Start / Stop (SpotCollector)** | — | Starts or stops UDP listener. |
| **Auto-start on startup (SpotCollector)** | `SpotCollectorAutoStart` | Auto-starts listener on launch. |
| **SpotCollector Spots** | — | Console of received SpotCollector spots. |

### POTA (Tab)

Poll api.pota.app for current Parks on the Air activations.

| Control | Setting key | Behavior |
|---------|-------------|----------|
| **Server:** | — | Fixed endpoint: api.pota.app (HTTP polling). |
| **Poll Interval:** | `PotaPollInterval` | Seconds between POTA polls. |
| **Start / Stop (POTA)** | — | Starts or stops POTA polling. |
| **Auto-start on startup (POTA)** | `PotaAutoStart` | Auto-starts POTA on launch. |
| **POTA Activations** | — | Console of activation feed. |
| **Spot Color: (POTA)** | `PotaSpotColor` | Color picker for POTA spots. |

### FreeDV (Tab)

Connect to the FreeDV QSO reporter WebSocket feed.

| Control | Setting key | Behavior |
|---------|-------------|----------|
| **Server:** | — | Fixed endpoint: qso.freedv.org (WebSocket). |
| **Start / Stop (FreeDV)** | — | Connects or disconnects the FreeDV WebSocket. |
| **Auto-start on startup (FreeDV)** | `FreeDvAutoStart` | Auto-starts FreeDV on launch. |
| **FreeDV Spots** | — | Console of FreeDV activity. |
| **Spot Color: (FreeDV)** | `FreeDvSpotColor` | Color picker for FreeDV spots. |

### Spot List (Tab)

Unified searchable table of all live spots from all sources.

| Control | Behavior |
|---------|----------|
| **Bands:** | Per-band checkboxes toggle visibility in table. Checkboxes are arranged in a flow layout that wraps to new rows when the dialog is narrow, keeping labels readable. |
| **Clear** | Empties current spot list. |
| **Spot table** | Sortable table of spots. Double-click a row to tune to that frequency. Columns: Time, Freq, DX Call, Comment, Spotter, Band, Mode, Source. Right-click the header row to show or hide columns — checkable actions toggle column visibility without closing the menu, letting you adjust multiple columns in one pass. |

---

## Display (Tab)

Configure how spots appear on the panadapter.

### Master Toggles

| Control | Setting key | Default | Behavior |
|---------|-------------|---------|----------|
| **Spots:** | `IsSpotsEnabled` | Enabled | Master toggle for DX spot overlay. |
| **Memories:** | `IsMemorySpotsEnabled` | Disabled | Toggles memory-channel overlay on panadapter. |
| **Auto:** | `SpotAutoSwitchMode` | Enabled | Automatically switch slice mode when clicking a spot that includes mode info (e.g. CW, FT8, RTTY). |
| **Signals (Signal History)** | `SHistoryMarkersEnabled` | Disabled | Gold markers for detected voice-width signals on the panadapter. |
| **QRM (Signal History)** | `SHistoryQrmEnabled` | Disabled | Red markers for persistent carriers and wideband interference. |

### Clear and Position Controls

| Control | Setting key | Range | Behavior |
|---------|-------------|-------|----------|
| **Clear All** | — | — | Clears all DX spots, memory feed, Signal History markers and QRM markers from the spectrum. |
| **Levels:** | `SpotsMaxLevel` | 1–10 (default: 3) | Number of vertical stacking rows for spots. |
| **Position:** | `SpotsStartingHeightPercentage` | 0–100 (default: 50) | Vertical position on panadapter. |
| **Font Size:** | `SpotFontSize` | 8–32 (default: 16) | Spot text size. |
| **Spot Lifetime:** | `DxClusterSpotLifetimeSec` | 10 sec – 24 hrs | Seconds before a spot fades away. Non-linear steps. |

### Color Overrides

| Control | Setting key | Default | Behavior |
|---------|-------------|---------|----------|
| **Override Colors:** | `IsSpotsOverrideColorsEnabled` | — | Forces a single text color for all spots. |
| **Spot text color picker** | `SpotsOverrideColor` | #FFFF00 | Opens color picker to choose spot text color. |
| **Override Background: Enabled** | `IsSpotsOverrideBackgroundColorsEnabled` | Enabled | Enables custom spot background color. |
| **Override Background: Auto** | `IsSpotsOverrideToAutoBackgroundColorEnabled` | Enabled | Auto-picks background color for contrast. |
| **Spot background color picker** | `SpotsOverrideBgColor` | #000000 | Opens color picker for spot background color. |
| **Background Opacity:** | `SpotsBackgroundOpacity` | 0–100 (default: 48) | Opacity of spot background color. |
| **Spot Lines:** | `IsSpotsLinesEnabled` | Enabled | Draws vertical lines from the spectrum up to each spot label. Disable during contests to reduce visual clutter. |

### Status Indicators

| Indicator | Behavior |
|-----------|----------|
| **Total Spots:** | Live count of spots currently tracked across all sources. |

### DXCC Coloring (Section)

| Control | Setting key | Behavior |
|---------|-------------|----------|
| **DXCC Colors:** | `IsDxccColoringEnabled` | Colors spots by worked/confirmed/needed DXCC status. |
| **Log File (ADIF):** | `DxccAdifFilePath` | Loads an ADIF log file to drive DXCC coloring. Auto-watches the file for changes after selection. |
| **Imported:** | — | Shows QSO count and entity count when a log is loaded. Format: `<N> QSOs / <M> entities`. |
| **New DXCC color** | `DxccColorNewEntity` | Color picker for unworked entities. |
| **New Band color** | `DxccColorNewBand` | Color picker for new band contacts. |
| **New Mode color** | `DxccColorNewMode` | Color picker for new mode contacts. |
| **Worked color** | `DxccColorWorked` | Color picker for already worked entities. |

### Signal History (Section)

| Control | Setting key | Default | Range | Behavior |
|---------|-------------|---------|-------|----------|
| **Marker Lifetime:** | `SHistoryLifetimeS` | 60 | 15–300 s | How long an inactive Signal History marker persists before being removed. Double-click knob to reset to 60 s. |
| **QRM Gate:** | `SHistoryQrmGateS` | 6 | 3–30 s | How long a narrow carrier or wideband signal must persist before being classified as QRM. Double-click knob to reset to 6 s. |
| **Edge Threshold:** | `SHistorySoftEdgeDb` | 3.0 | 1.0–10.0 dB | Threshold above noise floor for the slope edge walk that refines the S-History carrier-side edge. Double-click knob to reset to 3.0 dB. |
| **Signals color** | `SHistoryColorSignals` | #FFC800 | — | Opens color picker for gold voice signal markers. |
| **QRM color** | `SHistoryColorQrm` | #FF0000 | — | Opens color picker for red QRM markers. |
| **Snap to Step:** | `SHistorySnapToStep` | Disabled | — | Rounds S-History click-to-tune to the nearest multiple of the active slice's step size, hiding the small carrier offset. |

---

## Visual Feedback

- Status labels for each source show current connection state: Disconnected, Connected, Stopped, Listening, or Polling.
- The SpotHub dialog uses theme-aware colors: accent color when connected, label color when disconnected, and danger color on error.
- Toggle buttons display their default text ("Enabled" or "Disabled") — toggle state is indicated by the button's pressed state and background styling, not by the label text.

## Tips

- QRM markers are independent from Signal History voice markers. Enable one, both, or neither.
- Use the **QRM Gate** slider to ignore brief transmissions and only mark signals that persist long enough to be interference.
- Double-click any slider knob in the Signal History section to instantly reset it to its factory default value.
- The **Spot List** tab uses a flow layout for band checkboxes, so they wrap to new rows when the dialog is narrow instead of being compressed.
- Right-click the spot table header to show or hide columns — the column visibility menu stays open while you toggle multiple checkboxes.
- Click the **Time** column header in the Spot List table to restore newest-first ordering after sorting by another column.

## Related

- [Toggle Signal History voice markers on the panadapter](toggle-signal-history-voice-markers-on-the-panadapter)
- [Adjust S-History marker lifetime, QRM gate and edge threshold](adjust-s-history-marker-lifetime-qrm-gate-and-edge-threshold)
- [Pick custom colors for