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

| Control                     | Behavior                                                                                                                                                               | Setting key           |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| **Server:**                 | RBN telnet hostname                                                                                                                                                    | `RbnHost`             |
| **Port:**                   | RBN telnet port                                                                                                                                                        | `RbnPort`             |
| **Callsign:**               | Login callsign sent to RBN                                                                                                                                             | `RbnCallsign`         |
| **Rate Limit:**             | Maximum RBN spots accepted per second                                                                                                                                  | `RbnRateLimit`        |
| **Connect / Disconnect**    | Toggles the RBN telnet session                                                                                                                                         | —                     |
| **Auto-connect on startup** | Connects to RBN automatically on launch                                                                                                                                | `RbnAutoConnect`      |
| **RBN Console**             | Read-only display of raw RBN traffic                                                                                                                                   | —                     |
| **Send**                    | Sends a typed command to the RBN session                                                                                                                               | —                     |
| **Spot Color:**             | Opens a color picker for RBN spots on the panadapter                                                                                                                   | `RbnSpotColor`        |
| **Spot Lines:**             | Draws vertical lines from the spectrum up to each spot label. Disable during contests to reduce visual clutter.                                                        | `IsSpotsLinesEnabled` |
| Total Spots:                | Live readout of how many spots are currently tracked across all sources. Updated whenever spots are added or cleared. Resets to 0 when **Clear All Spots** is pressed. | —                     |
## Double-clicking a spot now forwards mode hints

Starting in v0.9.7, double-clicking a row in the **Spot List** tab tunes the receiver to the spot frequency and also switches the receiver mode to match the spot. For example, double-clicking a CW spot switches the receiver to CW, and double-clicking an FT8 spot switches it to the appropriate digital mode, rather than only changing the frequency. The mode is resolved from the spot comment by the `SpotModeResolver` logic shared across all spot sources.

## Spot Lines

The **Display** tab now includes a **Spot Lines:** toggle (new in v0.9.7). When **Enabled** (the default), AetherSDR draws a short vertical line from the spectrum trace up to each spot label on the panadapter, making it easier to see exactly which frequency a spot corresponds to. Set it to **Disabled** during contests or other high-spot-density operating sessions to reduce visual clutter. This persists as `IsSpotsLinesEnabled`.

## FreeDV Reporter station reporting

The **FreeDV** tab contains a **Station Reporting** section that lets AetherSDR broadcast your station's activity to the public FreeDV Reporter map at `qso.freedv.org` whenever the RADE modem is active. This feature is build-gated by `HAVE_WEBSOCKETS`; on Windows it also requires the `HAVE_RADE` inner guard.

### Controls

| Control | Behavior | Setting key |
|---|---|---|
| **Enable FreeDV Reporter reporting when RADE is active** | Enables station reporting to the public FreeDV Reporter map whenever the RADE modem is active. The checkbox refuses to enable if either the callsign or grid square field resolves to an empty value. | `FreeDvAutoReport` |
| **Callsign:** | Callsign reported to the FreeDV Reporter map. Becomes read-only when **Use radio** is checked. | `FreeDvMyCallsign` |
| **Use radio** | Pre-fills the callsign field from the radio's configured callsign and locks the field read-only. When the radio's callsign changes (for example, in Radio Setup), the field updates automatically. | `FreeDvUseRadioCallsign` |
| **Grid Square:** | Maidenhead grid square reported. Becomes read-only when **Use GPS** is checked. | `FreeDvMyGrid` |
| **Use GPS** | Pre-fills the grid field from the radio's GPS module and locks the field read-only. Only shown on radio models that have GPS hardware. | `FreeDvUseGpsGrid` |
| **Station Msg:** | Optional free-text message shown beside the callsign on the public FreeDV Reporter map. | `FreeDvMyMessage` |

### Enabling station reporting

1. Click the **FreeDV** tab inside `Settings > SpotHub...`.
2. In the **Station Reporting** group, enter or confirm your **Callsign:**. Check **Use radio** to pull it from the radio automatically.
3. Enter or confirm your **Grid Square:**. On radios with GPS hardware, check **Use GPS** to populate it automatically.
4. Optionally fill in **Station Msg:** with a short free-text note.
5. Check **Enable FreeDV Reporter reporting when RADE is active**.
   - If either the callsign or grid square resolves to an empty value, a warning dialog appears and the checkbox reverts to unchecked. Fill in the missing field and try again.
   - When enabled, the setting persists as `FreeDvAutoReport`.

> **Note:** The FreeDV Reporter map is a public, community-shared resource. AetherSDR blocks enabling this feature if the callsign or grid square is blank to prevent placeholder values such as `N0CALL` or `AA00` from appearing on the map.

## Auto Mode default change

In v0.9.5.1 the **Auto Mode:** toggle on the **Display** tab defaults to **Enabled** for new installations. The setting persists as `SpotAutoSwitchMode`. Existing installations where the value has been saved explicitly are not affected.

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
- **FreeDV Reporter checkbox reverts to unchecked immediately** — A callsign or grid square value could not be resolved. Enter values in the **Callsign:** and **Grid Square:** fields, or enable **Use radio** and **Use GPS** so AetherSDR can read them from the radio.
- **Auto Mode: is now Enabled after upgrading** — v0.9.5.1 changed the default for `SpotAutoSwitchMode` from `False` to `True`. If you prefer the previous behavior, open `Settings > SpotHub...`, click the **Display** tab, and click **Auto Mode:** to set it to **Disabled**.

## Related

- [Connect to a DX cluster](connect-to-a-dx-cluster.md)
- [Tune spot density, position, font size and lifetime](../../features/dx-cluster/tune-spot-density-position-font-size-and-lifetime.md)
- [Pick colors for each spot source](../../features/dx-cluster/pick-colors-for-each-spot-source.md)
- [Tune to a spot by double-clicking the spot list](../../features/dx-cluster/tune-to-a-spot-by-double-clicking-the-spot-list.md)
- [SpotHub overview](../../features/dx-cluster/overview.md)