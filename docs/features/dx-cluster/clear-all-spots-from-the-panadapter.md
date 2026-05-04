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
- If spots reappear immediately and you want a clean slate for longer, reduce `Spot Lifetime:` on the `Display` tab (`SpotsLifetime`) or disconnect the relevant source before clearing.

## Auto Mode default change

As of v0.9.5.1, `Auto Mode:` (`SpotAutoSwitchMode`) defaults to **Enabled**. In previous versions it defaulted to Disabled. If you have not previously saved this setting, AetherSDR will now automatically switch the radio mode when you click a spot on the panadapter. To turn this off, open the `Display` tab and click `Auto Mode:` to set it to Disabled.

## FreeDV Reporter reporting

The FreeDV tab includes a **Station Reporting** section that lets AetherSDR broadcast your activity to the public FreeDV Reporter map at `qso.freedv.org` whenever the RADE modem is active.

### Enabling reporting

1. Open `Settings > SpotHub...` and click the `FreeDV` tab.
2. In the **Station Reporting** group, fill in your callsign and grid square (see fields below).
3. Check `Enable FreeDV Reporter reporting when RADE is active`.

If either the callsign or the grid square is blank when you check the box, AetherSDR will display a warning and leave reporting disabled. Both fields must contain a value before reporting can be turned on. This guard prevents blank or placeholder data from appearing on the shared public map.

The setting is saved as `FreeDvAutoReport`.

### Station Reporting fields

| Field          | Setting key              | Description                                                                                                                                                                               |
|----------------|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Callsign:`    | `FreeDvMyCallsign`       | Callsign reported to the FreeDV Reporter map. The field is read-only when `Use radio` is checked.                                                                                         |
| `Use radio`    | `FreeDvUseRadioCallsign` | Pre-fills the callsign from the radio's configured callsign and locks the field. Defaults to enabled. When the callsign is later changed in Radio Setup, the field updates automatically. |
| `Grid Square:` | `FreeDvMyGrid`           | Maidenhead grid square (up to 6 characters) reported to the map. The field is read-only when `Use GPS` is checked.                                                                        |
| `Use GPS`      | `FreeDvUseGpsGrid`       | Pre-fills the grid from the radio's GPS module and locks the field. Only shown on radio models that have GPS hardware. Defaults to enabled.                                               |
| `Station Msg:` | `FreeDvMyMessage`        | Optional free-text message shown beside your callsign on the public map.                                                                                                                  |
### How AetherSDR resolves the callsign and grid

When you enable reporting, AetherSDR determines the effective callsign and grid square in this order:

1. **Callsign** — uses the radio's configured callsign if `Use radio` is checked and the radio has a non-empty callsign; otherwise uses the value typed in the `Callsign:` field.
2. **Grid square** — uses the radio's GPS grid if `Use GPS` is checked, GPS hardware is present, and the GPS has a fix; otherwise uses the value typed in the `Grid Square:` field.

If either resolved value is empty, enabling the checkbox is blocked and a warning dialog is shown.

## Related

- [SpotHub overview](overview.md)
- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
- [Tune to a spot by double-clicking the spot list](tune-to-a-spot-by-double-clicking-the-spot-list.md)