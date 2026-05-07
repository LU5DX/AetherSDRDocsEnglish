# Pick colors for each spot source

AetherSDR can display spots from up to six sources simultaneously. Assigning a distinct color to each source makes it easy to tell them apart on the panadapter at a glance.

## Before you start

- Open SpotHub: `Settings > SpotHub...`
- At least one spot source should be configured so you can see the effect of your color choice.

## Steps

### DX Cluster spot color
1. In SpotHub, click the **Cluster** tab.
2. Click the **Spot Color:** button.
3. Choose a color in the color picker that opens and confirm your selection.
4. The new color is saved to `ClusterSpotColor` and applied immediately to cluster spots on the panadapter.

### RBN spot color

1. Click the **RBN** tab.
2. Click the **Spot Color:** button.
3. Choose a color and confirm.
4. Saved to `RbnSpotColor`.

### WSJT-X spot colors

WSJT-X supports four separate colors, one per decode category.

1. Click the **WSJT-X** tab.
2. Click the color button for each category you want to change:
   - **CQ color** — spots decoded as CQ calls. Saved to `WsjtxColorCQ`.
   - **POTA color** — spots decoded as CQ POTA calls. Saved to `WsjtxColorPOTA`.
   - **Calling Me color** — decodes addressed to your callsign. Saved to `WsjtxColorCallingMe`.
   - **Default color** — all other WSJT-X decodes. Saved to `WsjtxColorDefault`.
3. Confirm each color in the color picker before moving to the next.

### POTA spot color

1. Click the **POTA** tab.
2. Click the **Spot Color:** button.
3. Choose a color and confirm.
4. Saved to `PotaSpotColor`.

### FreeDV spot color

1. Click the **FreeDV** tab.
2. Click the **Spot Color:** button.
3. Choose a color and confirm.
4. Saved to `FreeDvSpotColor`.

> **Note:** The FreeDV tab is present only if AetherSDR was built with WebSocket support.

### SpotCollector

SpotCollector does not have a dedicated spot-color picker in SpotHub. See the Display tab options below if you need a uniform override for all sources.

## What each control does
| Control                                                  | Tab                        | Saved setting                                                                                                                                                          |
|----------------------------------------------------------|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Spot Color:**                                          | Cluster                    | `ClusterSpotColor`                                                                                                                                                     |
| **Spot Color:**                                          | RBN                        | `RbnSpotColor`                                                                                                                                                         |
| **CQ color**                                             | WSJT-X                     | `WsjtxColorCQ`                                                                                                                                                         |
| **POTA color**                                           | WSJT-X                     | `WsjtxColorPOTA`                                                                                                                                                       |
| **Calling Me color**                                     | WSJT-X                     | `WsjtxColorCallingMe`                                                                                                                                                  |
| **Default color**                                        | WSJT-X                     | `WsjtxColorDefault`                                                                                                                                                    |
| **Spot Color:**                                          | POTA                       | `PotaSpotColor`                                                                                                                                                        |
| **Spot Color:**                                          | FreeDV                     | `FreeDvSpotColor`                                                                                                                                                      |
| **Enable FreeDV Reporter reporting when RADE is active** | FreeDV                     | `FreeDvAutoReport`                                                                                                                                                     |
| **Callsign:**                                            | FreeDV — Station Reporting | `FreeDvMyCallsign`                                                                                                                                                     |
| **Use radio (callsign)**                                 | FreeDV — Station Reporting | `FreeDvUseRadioCallsign`                                                                                                                                               |
| **Grid Square:**                                         | FreeDV — Station Reporting | `FreeDvMyGrid`                                                                                                                                                         |
| **Use GPS (grid)**                                       | FreeDV — Station Reporting | `FreeDvUseGpsGrid`                                                                                                                                                     |
| **Station Msg:**                                         | FreeDV — Station Reporting | `FreeDvMyMessage`                                                                                                                                                      |
| **Auto Mode:**                                           | Display                    | `SpotsAutoMode` — default changed to **Enabled** in v0.9.5.1                                                                                                           |
| **Spot Lines:**                                          | Display                    | `IsSpotsLinesEnabled` — new in v0.9.7                                                                                                                                  |
| Total spots count                                        | Status bar                 | Live readout of how many spots are currently tracked across all sources. Updated whenever spots are added or cleared. Resets to 0 when **Clear All Spots** is pressed. |
## FreeDV Reporter — Station Reporting

v0.9.3 adds a **Station Reporting** group inside the **FreeDV** tab. When enabled, AetherSDR broadcasts your station's activity to the public FreeDV Reporter map at qso.freedv.org whenever the RADE modem is active.

> **Note:** Station Reporting is present only if AetherSDR was built with WebSocket support (`HAVE_WEBSOCKETS`). On Windows builds it additionally requires `HAVE_RADE`.

### Enable reporting

1. Click the **FreeDV** tab in SpotHub.
2. In the **Station Reporting** group, fill in a valid callsign and grid square (see below) before enabling the checkbox.
3. Check **Enable FreeDV Reporter reporting when RADE is active**.
   - If either the callsign or grid square field is blank when you check the box, a warning dialog appears and the checkbox reverts to unchecked. Fill both fields first, then try again.
4. The setting is saved to `FreeDvAutoReport`.

### Callsign field

- The **Callsign:** field (`FreeDvMyCallsign`) sets the callsign reported to the public map.
- When **Use radio** is checked (default), the field is pre-filled from the radio's configured callsign and locked read-only. The field updates automatically if you change the callsign in Radio Setup.
- Uncheck **Use radio** to type a callsign manually. The value is saved to `FreeDvMyCallsign` and uppercased on exit.
- **Use radio** is saved to `FreeDvUseRadioCallsign`.

### Grid Square field

- The **Grid Square:** field (`FreeDvMyGrid`) sets the Maidenhead locator reported to the public map.
- On radio models with GPS hardware, a **Use GPS** checkbox appears. When checked (default), the field is pre-filled from the radio's GPS module and locked read-only.
- Uncheck **Use GPS** to type a grid square manually. The value is saved to `FreeDvMyGrid` and uppercased on exit.
- **Use GPS** is saved to `FreeDvUseGpsGrid`. The checkbox is hidden on radio models that have no GPS hardware.

### Station message

- The optional **Station Msg:** field (`FreeDvMyMessage`) accepts free text that appears beside your callsign on the public FreeDV Reporter map. Leave it blank if you have nothing to add.

## Auto Mode default changed in v0.9.5.1

The **Auto Mode:** toggle on the **Display** tab now defaults to **Enabled** for new installations. If you are upgrading from an earlier version and `SpotsAutoMode` was not previously set, AetherSDR will treat it as enabled after the update. To disable it, open the **Display** tab and click **Auto Mode:** until it shows **Disabled**.

## Spot Lines (new in v0.9.7)

The **Spot Lines:** toggle on the **Display** tab controls whether vertical lines are drawn from the spectrum baseline up to each spot label on the panadapter. The setting is saved to `IsSpotsLinesEnabled` and defaults to **Enabled**.

To turn off spot lines:

1. Open SpotHub: `Settings > SpotHub...`
2. Click the **Display** tab.
3. Click **Spot Lines:** until it shows **Disabled**.

Disabling spot lines reduces visual clutter during contests or when spot density is high.

## Tuning from the Spot List (updated in v0.9.7)

Double-clicking a row in the **Spot List** tab tunes the active receiver to that spot's frequency. Starting with v0.9.7, AetherSDR also passes the spot's mode hint to the receiver, so the mode (for example CW or SSB) switches automatically to match the spot rather than only changing frequency.

## Tips

- If all per-source colors are too subtle to distinguish, use **Override Colors:** on the **Display** tab to force a single text color across every source, saved to `IsSpotsOverrideColorsEnabled`.
- DXCC coloring (enabled with **DXCC Coloring** on the **Display** tab) can override per-source colors to indicate worked, confirmed, or needed status. If your spot colors are not appearing as set, check whether `DxccColoringEnabled` is active.

## Related

- [SpotHub overview](overview.md)
- [Start WSJT-X UDP listener and filter for CQ, POTA or calls to me](start-wsjt-x-udp-listener-and-filter-for-cq-pota-or-calls-to-me.md)
- [Poll POTA activations](poll-pota-activations.md)
- [Enable FreeDV QSO reporter WebSocket](enable-freedv-qso-reporter-websocket.md)
- [Enable DXCC coloring from an ADIF log](enable-dxcc-coloring-from-an-adif-log.md)
- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
<!-- docmesh:llm version=v0.9.7 date=2026-05-03 -->