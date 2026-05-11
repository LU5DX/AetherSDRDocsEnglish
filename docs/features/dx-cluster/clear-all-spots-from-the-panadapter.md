# Clear all spots from the panadapter

Remove every spot currently shown on the panadapter in one action. Use this when the display is cluttered and you want to start fresh without disconnecting any spot sources.

## Before you start

- At least one spot source (DX cluster, RBN, WSJT-X, SpotCollector, POTA, or FreeDV) must have delivered spots, otherwise there is nothing to clear.
- Spots continue arriving from any connected or running source immediately after clearing, so sources remain active.

## Steps

1. Open `Settings > SpotHub...`.
2. Click the `Display` tab.
3. Click `Clear All Spots`.

All spots are removed from the panadapter and the spot list instantly. Connected sources are not disconnected and will continue delivering new spots.

## Tips
- To remove spots band by band rather than all at once, use the `Spot List` tab. Check or uncheck individual bands under `Bands:` to hide spots for a specific band without discarding them permanently.
- To clear only the spot list table, go to the `Spot List` tab and click `Clear`. This empties the table display but the effect on the panadapter overlay follows the same live spot data.
- If spots reappear immediately and you want a clean slate for longer, reduce `Spot Lifetime:` on the `Display` tab (`DxClusterSpotLifetimeSec`) or disconnect the relevant source before clearing.
- `Auto:` is now enabled by default. When you double-click a spot that includes mode information (e.g. CW, FT8, RTTY), the slice mode switches automatically unless you disable this toggle.

## Auto: default change

As of v0.9.5.1, `Auto:` (`SpotAutoSwitchMode`) defaults to **Enabled**. In previous versions it defaulted to Disabled. If you have not previously saved this setting, AetherSDR will now automatically switch the radio mode when you click a spot on the panadapter. To turn this off, open the `Display` tab and click `Auto:` to set it to Disabled.

## Spot Lines

As of v0.9.7, the `Display` tab includes a `Spot Lines:` toggle (setting key `IsSpotsLinesEnabled`). When enabled, AetherSDR draws a vertical line from the spectrum up to each spot label so the exact frequency is easy to read. The toggle defaults to **Enabled**.

Disable `Spot Lines:` during contests or when the band is busy to reduce visual clutter on the panadapter.

### Steps

1. Open `Settings > SpotHub...` and click the `Display` tab.
2. Click `Spot Lines:` to toggle between **Enabled** and **Disabled**.

The change takes effect immediately on the panadapter without restarting any spot source.

## Tuning to a spot by double-clicking the spot list

Double-clicking a row in the spot table on the `Spot List` tab tunes the active slice to the spot frequency. As of v0.9.7, AetherSDR also reads any mode information embedded in the spot comment and forwards it alongside the frequency. If a recognizable mode (such as CW, FT8, or SSB) is found in the comment, and `Auto:` is enabled on the `Display` tab, the slice mode switches to match the spot automatically.

No additional configuration is required. The behavior activates whenever you double-click a spot row.

## SpotHub window and frameless mode

As of v26.5.1, the SpotHub dialog uses a frameless window title bar. This provides a cleaner appearance consistent with other AetherSDR windows. The window supports 8-axis edge resize when frameless mode is active.

Frameless mode is controlled globally by the `FramelessWindow` setting (default: `True`). When enabled, the window shows a custom title bar with window controls. When disabled, the window uses the standard OS title bar.

### Steps to toggle frameless mode

1. Open `Settings > AetherSDR Settings...`.
2. Navigate to the `Appearance` or `General` section.
3. Toggle `Frameless Window` as desired.

The SpotHub window respects the global setting and updates automatically.

## Signal History and QRM markers

As of v26.5.1, the Display tab includes two new toggles for Signal History visualization:

- **Signals** (`SHistoryMarkersEnabled`): Shows gold markers on the panadapter for detected voice-width signals. This toggle is the same as `View > Signal History Markers`.
- **QRM** (`SHistoryQrmEnabled`): Shows red markers for persistent narrow carriers and wideband interference. This toggle is the same as `View > QRM History Markers`.

Both toggles default to **Disabled**.

### Steps

1. Open `Settings > SpotHub...` and click the `Display` tab.
2. Click `Signals:` or `QRM:` to toggle each marker type on or off.

Markers appear and disappear immediately on the panadapter.

### Signal History tunables

Below the marker toggles, the Signal History section provides adjustment controls:

| Control | Setting Key | Default | Range | Behavior |
|---------|-------------|---------|-------|----------|
| Marker Lifetime: | `SHistoryLifetimeS` | 60 | 15-300 sec | How long an inactive Signal History marker persists before being removed. |
| QRM Gate: | `SHistoryQrmGateS` | 6 | 3-30 sec | How long a narrow carrier or wideband signal must persist before being classified as QRM. |
| Edge Threshold: | `SHistorySoftEdgeDb` | 3.0 | 1.0-10.0 dB | Threshold above noise floor for the slope edge walk that refines the S-History carrier-side edge. Lower = closer to carrier but more noise-sensitive. |

### Signal History colors

Two color pickers are available in the Signal History section:

- **Signals** (`SHistoryColorSignals`, default `#FFC800`): Gold color for voice signal markers.
- **QRM** (`SHistoryColorQrm`, default `#FF0000`): Red color for QRM markers.

Click each color swatch to open a color picker and select a custom color.

### Snap to Step

`Snap to Step:` (`SHistorySnapToStep`) rounds the S-History click-to-tune frequency to the nearest multiple of the active slice's step size. This hides the small carrier offset that may appear when clicking on a Signal History marker. Default: **Disabled**.

## Clear All button

The `Clear All` button on the Display tab clears all DX spots, memory feed, Signal History markers, and QRM markers from the spectrum simultaneously. This is useful when the display is cluttered and you want a completely fresh view without restarting any spot sources.

## DXCC Coloring

As of v26.5.1, the Display tab includes a DXCC Coloring section in the left column below the divider.

### Enabling DXCC Coloring

1. Open `Settings > SpotHub...` and click the `Display` tab.
2. In the DXCC Coloring section, click `DXCC Colors:` (`IsDxccColoringEnabled`) to enable or disable spot coloring by DXCC status.

When enabled, spots are colored according to whether the DXCC entity is new, worked on a new band, worked on a new mode, or already worked completely.

### Loading an ADIF log

To drive DXCC coloring, load an ADIF log file:

1. Click `Log File (ADIF):` (`DxccAdifFilePath`).
2. Select an ADIF file from your system.
3. AetherSDR automatically watches the file for changes and reloads it when modified. No separate toggle for auto-reload is needed.

After loading, the `Imported:` indicator shows the number of QSOs and entities, for example: `1200 QSOs / 85 entities`.

### DXCC Color swatches

Four color pickers are available for each DXCC status category:

| Status | Setting Key | Description |
|--------|-------------|-------------|
| New DXCC | `DxccColorNewEntity` | Color for entities not yet worked. |
| New Band | `DxccColorNewBand` | Color for entities worked on other bands but not this one. |
| New Mode | `DxccColorNewMode` | Color for entities worked on other modes but not this one. |
| Worked | `DxccColorWorked` | Color for entities fully worked. |

Click each color swatch to open a color picker and select a custom color. These replace the previous fixed DXCC color scheme.

## FreeDV Reporter reporting

The FreeDV tab includes a **Station Reporting** section that lets AetherSDR broadcast your activity to the public FreeDV Reporter map at `qso.freedv.org` whenever the RADE modem is active.

### Enabling reporting

1. Open `Settings > SpotHub...` and click the `FreeDV` tab.
2. In the **Station Reporting** group, fill in your callsign and grid square (see fields below).
3. Check `Enable FreeDV Reporter reporting when RADE is active`.

If either the callsign or the grid square is blank when you check the box, AetherSDR will display a warning and leave reporting disabled. Both fields must contain a value before reporting can be turned on. This guard prevents blank or placeholder data from appearing on the shared public map.

The setting is saved as `FreeDvAutoReport`.

### Station Reporting fields

| Field | Setting key | Description |
|-------|-------------|-------------|
| `Callsign:` | `FreeDvMyCallsign` | Callsign reported to the FreeDV Reporter map. The field is read-only when `Use radio` is checked. |
| `Use radio` | `FreeDvUseRadioCallsign` | Pre-fills the callsign from the radio's configured callsign and locks the field. Defaults to enabled. When the callsign is later changed in Radio Setup, the field updates automatically. |
| `Grid Square:` | `FreeDvMyGrid` | Maidenhead grid square (up to 6 characters) reported to the map. The field is read-only when `Use GPS` is checked. |
| `Use GPS` | `FreeDvUseGpsGrid` | Pre-fills the grid from the radio's GPS module and locks the field. Only shown on radio models that have GPS hardware. Defaults to enabled. |
| `Station Msg:` | `FreeDvMyMessage` | Optional free-text message shown beside your callsign on the public map. |

### How AetherSDR resolves the callsign and grid

When you enable reporting, AetherSDR determines the effective callsign and grid square in this order:

1. **Callsign** — uses the radio's configured callsign if `Use radio` is checked and the radio has a non-empty callsign; otherwise uses the value typed in the `Callsign:` field.
2. **Grid square** — uses the radio's GPS grid if `Use GPS` is checked, GPS hardware is present, and the GPS has a fix; otherwise uses the value typed in the `Grid Square:` field.

If either resolved value is empty, enabling the checkbox is blocked and a warning dialog is shown.

## Related

- [SpotHub overview](overview.md)
- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
- [Tune to a spot by double-clicking the spot list](tune-to-a-spot-by-double-clicking-the-spot-list.md)