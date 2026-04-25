# Check which antenna and frequency each TX station is using

Open the multiFLEX Dashboard to see, at a glance, which TX antenna and transmit frequency every connected station is currently using.

## Before you start

- AetherSDR must be connected to the radio. The multiFLEX Dashboard requires an active radio connection.
- multiFLEX must be enabled on the radio. If it is not, the stations table will be empty.

## Steps

1. Click `Settings > multiFLEX...` to open the multiFLEX Dashboard.
2. Read the **Stations table**. Each row is one connected client. The columns are:

   | Column | What it shows |
   |---|---|
   | LOCAL PTT | A check mark if that station currently holds PTT authority. |
   | STATION | The program and station name for that client. Your own station is highlighted in blue. |
   | TX ANT | The transmit antenna that station has selected. Shows `----` if not yet reported. |
   | TX FREQ (MHz) | The transmit frequency in MHz, to three decimal places. Shows `----` if not yet reported. |

3. Click `Close` when you are done.

## Tips

- The table updates automatically whenever a station changes its transmit antenna or frequency. You do not need to reopen the dialog.
- Your own station's row is distinguished by blue text in the STATION column, making it easy to compare your settings against other stations.
- `TX ANT` and `TX FREQ (MHz)` values of `----` mean the radio has not yet reported that data for the station, not that the station is inactive.

## Related

- [Enable multiFLEX on the radio](enable-multiflex-on-the-radio.md)
- [See all stations connected to this FLEX](../../getting-started/setup/see-all-stations-connected-to-this-flex.md)
- [Grant or revoke local PTT](grant-or-revoke-local-ptt.md)
