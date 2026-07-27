# Connect to the Reverse Beacon Network

The Reverse Beacon Network (RBN) provides automated CW, RTTY, and digital skimmer spots. This page shows how to configure and connect AetherSDR's RBN telnet feed so that RBN spots appear on your panadapter.

## Before you start

- Know the RBN telnet server hostname and port (the public server is `telnet.reversebeacon.net`, port `7000` for CW skimmers).
- Know the callsign you will use to log in to the RBN.
- Spots will only appear on the panadapter if the master spot overlay is enabled (`IsSpotsEnabled` defaults to Enabled).

## Steps

1. Open `Settings > SpotHub...`.
2. Click the **RBN** tab.
3. In the **Server:** field, enter the RBN telnet hostname (e.g., `telnet.reversebeacon.net`). This persists as `RbnHost`.
4. Set **Port:** to the telnet port for the skimmer feed you want. Valid range: 1–65535. This persists as `RbnPort`.
5. In the **Callsign:** field, enter your callsign. This persists as `RbnCallsign`.
6. If the RBN feed produces more spots than you need, set **Rate Limit:** to cap the number of spots processed per second. This persists as `RbnRateLimit`.
7. Click **Connect**. The button label changes to **Disconnect** when the session is established, and the **RBN Console** shows incoming traffic.
8. To have AetherSDR connect to the RBN automatically on every launch, enable **Auto-connect on startup**. This persists as `RbnAutoConnect`.

## What each control does

| Control                                                       | Behavior                                                                                                                                                               | Setting key                                                                                                        |
|---------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| **Server:**                                                   | RBN telnet hostname                                                                                                                                                    | `RbnHost`                                                                                                          |
| **Port:**                                                     | RBN telnet port                                                                                                                                                        | `RbnPort`                                                                                                          |
| **Callsign:**                                                 | Login callsign sent to RBN                                                                                                                                             | `RbnCallsign`                                                                                                      |
| **Rate Limit:**                                               | Maximum RBN spots accepted per second                                                                                                                                  | `RbnRateLimit`                                                                                                     |
| **Connect / Disconnect**                                      | Toggles the RBN telnet session                                                                                                                                         | —                                                                                                                  |
| **Auto-connect on startup**                                   | Connects to RBN automatically on launch                                                                                                                                | `RbnAutoConnect`                                                                                                   |
| **RBN Console**                                               | Read-only display of raw RBN traffic                                                                                                                                   | —                                                                                                                  |
| **Send**                                                      | Sends a typed command to the RBN session                                                                                                                               | —                                                                                                                  |
| **Spot Color:**                                               | Opens a color picker for RBN spots on the panadapter                                                                                                                   | `RbnSpotColor`                                                                                                     |
| **Spot Lines:**                                               | Draws vertical lines from the spectrum up to each spot label. Disable during contests to reduce visual clutter.                                                        | `IsSpotsLinesEnabled`                                                                                              |
| Total Spots:                                                  | Live readout of how many spots are currently tracked across all sources. Updated whenever spots are added or cleared. Resets to 0 when **Clear All Spots** is pressed. | —                                                                                                                  |
| Auto:                                                         | Automatically switch slice mode when clicking a spot that includes mode info (e.g. CW, FT8, RTTY).                                                                     | `SpotAutoSwitchMode`                                                                                               |
| Signals (Signal History)                                      | Gold markers for detected voice-width signals on the panadapter.                                                                                                       | `SHistoryMarkersEnabled`                                                                                           |
| QRM (Signal History)                                          | Red markers for persistent carriers and wideband interference.                                                                                                         | `SHistoryQrmEnabled`                                                                                               |
| Clear All                                                     | Clears all DX spots, memory feed, Signal History markers and QRM markers from the spectrum.                                                                            | —                                                                                                                  |
| Override Colors:                                              | Forces a single text color for all spots. Button is always labelled **Enabled** and changes to checked/ unchecked state.                                               | `IsSpotsOverrideColorsEnabled`                                                                                     |
| Spot text color picker                                        | Opens QColorDialog to pick spot text color.                                                                                                                            | `SpotsOverrideColor`                                                                                               |
| Override Background: Enabled                                  | Enables custom spot background color.                                                                                                                                  | `IsSpotsOverrideBackgroundColorsEnabled`                                                                           |
| Override Background: Auto                                     | Auto-picks background color for contrast.                                                                                                                              | `IsSpotsOverrideToAutoBackgroundColorEnabled`                                                                      |
| Spot background color picker                                  | Opens QColorDialog for spot background color.                                                                                                                          | `SpotsOverrideBgColor`                                                                                             |
| Background Opacity:                                           | Opacity of spot background color (0-100).                                                                                                                              | `SpotsBackgroundOpacity`                                                                                           |
| DXCC Coloring (section)                                       | Section header for DXCC coloring controls in the left column below the divider.                                                                                        | —                                                                                                                  |
| DXCC Colors:                                                  | Colors spots by worked/confirmed/needed DXCC status. Button is always labelled **Enabled**.                                                                            | `IsDxccColoringEnabled`                                                                                            |
| Log File (ADIF):                                              | Loads an ADIF log file to drive DXCC coloring. Auto-watches the file for changes after selection.                                                                      | `DxccAdifFilePath`                                                                                                 |
| Imported: (DXCC stats)                                        | Shows QSO count and entity count when a log is loaded.                                                                                                                 | —                                                                                                                  |
| DXCC Color swatches (New DXCC / New Band / New Mode / Worked) | Opens a color picker for each DXCC status category.                                                                                                                    | `DxccColorNewEntity`, `DxccColorNewBand`, `DxccColorNewMode`, `DxccColorWorked`                                    |
| Signal History (section)                                      | Section header for Signal History tunables in the right column below the divider.                                                                                      | —                                                                                                                  |
| Marker Lifetime:                                              | How long an inactive Signal History marker persists before being removed (15-300 sec).                                                                                 | `SHistoryLifetimeS`                                                                                                |
| QRM Gate:                                                     | How long a narrow carrier or wideband signal must persist before being classified as QRM (3-30 sec).                                                                   | `SHistoryQrmGateS`                                                                                                 |
| Edge Threshold:                                               | Threshold above noise floor for the slope edge walk that refines the S-History carrier-side edge (1.0-10.0 dB).                                                        | `SHistorySoftEdgeDb`                                                                                               |
| Signal History color swatches (Signals / QRM)                 | Opens a color picker for the voice signal markers (gold) and QRM markers (red).                                                                                        | `SHistoryColorSignals`, `SHistoryColorQrm`                                                                         |
| Snap to Step:                                                 | Rounds S-History click-to-tune to the nearest multiple of the active slice's step size, hiding the small carrier offset. Button is always labelled **Enabled**.        | `SHistorySnapToStep`                                                                                               |
| Bands:                                                        | Per-band checkboxes to toggle spot visibility in the Spot List table. Wrapped in a flow layout to remain readable when SpotHub is narrow.                              | —                                                                                                                  |
| Clear                                                         | Empties the current spot list.                                                                                                                                         | —                                                                                                                  |
| Spot table                                                    | Sortable table of spots. Double-click row to tune. Columns: Time, Freq, DX Call, Comment, Spotter, Band, Mode, Source.                                                  | —                                                                                                                  |

## Double-clicking a spot now forwards mode hints

Starting in v0.9.7, double-clicking a row in the **Spot List** tab tunes the receiver to the spot frequency and also switches the receiver mode to match the spot. For example, double-clicking a CW spot switches the receiver to CW, and double-clicking an FT8 spot switches it to the appropriate digital mode, rather than only changing the frequency. The mode is resolved from the spot comment by the `SpotModeResolver` logic shared across all spot sources.

## Spot Lines

The **Display** tab now includes a **Spot Lines:** toggle (new in v0.9.7). When **Enabled** (the default), AetherSDR draws a short vertical line from the spectrum trace up to each spot label on the panadapter, making it easier to see exactly which frequency a spot corresponds to. Set it to **Disabled** during contests or other high-spot-density operating sessions to reduce visual clutter. This persists as `IsSpotsLinesEnabled`.

## Toggle button labels simplified

In v26.6.3, the **Override Colors:**, **DXCC Colors:**, **Spot Lines:**, and **Snap to Step:** toggle buttons on the **Display** tab no longer change their text between **Enabled** and **Disabled** when clicked. Instead, the button always displays its default label (e.g., **Enabled**) and uses its checked/unchecked visual state (depressed or raised) to indicate the current setting. This applies to:

- **Override Colors:** (setting `IsSpotsOverrideColorsEnabled`)
- **Spot Lines:** (setting `IsSpotsLinesEnabled`)
- **DXCC Colors:** (setting `IsDxccColoringEnabled`)
- **Snap to Step:** (setting `SHistorySnapToStep`)

All other toggle buttons throughout the SpotHub dialog continue to display text reflecting their on/off state.

## Theme-aware styling

Starting in v26.6.1, the SpotHub dialog uses theme-aware styling. The status labels and tab bar colors now respect the selected theme, using semantic color tokens such as `{{color.accent}}`, `{{color.text.label}}`, and `{{color.accent.danger}}` instead of hardcoded hex values. This means status indicators (Connected, Disconnected, Error) automatically adjust their colors when you change themes.

## Auto Mode default change

In v0.9.5.1 the **Auto Mode:** toggle on the **Display** tab defaults to **Enabled** for new installations. The setting persists as `SpotAutoSwitchMode`. Existing installations where the value has been saved explicitly are not affected.

## Spot List tab improvements (v26.7.4)

The **Spot List** tab uses a flow layout for its band filter checkboxes. This prevents the checkboxes from being compressed to illegibility when the SpotHub dialog is narrow. The checkboxes wrap to a new row when they run out of horizontal space, keeping the checked state readable.

The **Spot table** columns can be shown or hidden by right-clicking the table header and checking or unchecking column names. The menu stays open while you toggle multiple checkboxes, so you can adjust several columns in one pass instead of reopening the menu per column.

The minimum width of the SpotHub dialog has been lowered to 360 pixels, allowing the dialog to be sized narrower once columns are hidden in the Spot List table.

## Tips

- The **RBN Console** is read-only and shows raw telnet lines as they arrive. Use the **Send** command line below it to issue filter commands directly to the RBN server (e.g., `set/skimmer` or band-filter commands supported by the RBN).
- If the panadapter becomes cluttered during a contest, lower **Rate Limit:** to reduce spot density without disconnecting. You can also disable **Spot Lines:** on the **Display** tab to reduce visual clutter further.
- To change how spots look on the panadapter — size, position, lifetime, and stacking — see [Tune spot density, position, font size and lifetime](../../features/dx-cluster/tune-spot-density-position-font-size-and-lifetime.md).
- RBN spots use the color set by **Spot Color:** on the RBN tab. To override all spot source colors with a single color, use the **Override Colors:** toggle on the **Display** tab.

## Troubleshooting

- **Connect button returns to Connect immediately with an error in the console** — The hostname or port is wrong, or the RBN server is unreachable. Verify `RbnHost` and `RbnPort` and check your network connection.
- **No spots appear on the panadapter after connecting** — Confirm that **Spots:** on the **Display** tab is set to Enabled (`IsSpotsEnabled`). Also check that the band you are monitoring is not hidden in the **Spot List** tab band filter checkboxes.
- **Panadapter is flooded with spots** — Reduce **Rate Limit:** to a lower value to cap incoming spot rate. Alternatively, disable **Spot Lines:** (`IsSpotsLinesEnabled`) on the **Display** tab to make dense spot areas easier to read without reducing the number of spots shown.
- **Double-clicking a spot changes frequency but does not change mode** — The spot comment may not contain a recognizable mode token. Mode switching depends on the spot comment containing a known mode string (e.g., `CW`, `FT8`, `SSB`). If the spotter did not include a mode in the comment, only the frequency changes.
- **Toggle buttons do not show Enabled/Disabled text change** — This is expected behavior starting in v26.6.3. The **Override Colors:**, **Spot Lines:**, **DXCC Colors:**, and **Snap to Step:** buttons always display **Enabled** regardless of state. Their checked/unchecked visual state indicates whether the feature is active.