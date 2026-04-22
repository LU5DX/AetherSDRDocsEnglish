# See all stations connected to this FLEX

The multiFLEX Dashboard shows every client currently sharing your FLEX-8600 and what each one is doing. Use it to confirm who is connected, which antenna they are using, and what frequency they are transmitting on.

## Before you start

- AetherSDR must be connected to the radio. The multiFLEX Dashboard requires an active radio connection.
- multiFLEX must be enabled on the radio. If the dashboard shows no stations, check that multiFLEX is active (see [Enable multiFLEX on the radio](../../features/multi-flex/enable-multiflex-on-the-radio.md)).

## Steps

1. Click `Settings > multiFLEX...`.
2. The **multiFLEX Dashboard** opens and immediately populates the **Stations table** with all connected clients.
3. Read the table. Each row is one client. The columns are **LOCAL PTT**, **STATION**, **TX ANT**, and **TX FREQ (MHz)**. Your own station is highlighted in blue.
4. Click `Close` when finished.

## What each control does

| Control | What it does |
|---|---|
| `Enabled` / `Disabled` button | Toggles multiFLEX on or off for the radio. The button label reflects the current state. |
| **Stations table** | Lists every connected multiFLEX client. Columns: **LOCAL PTT** (checkmark if that station holds PTT), **STATION** (program and station name), **TX ANT** (transmit antenna), **TX FREQ (MHz)** (transmit frequency). Displays `----` when a value is not available. |
| `Enable` (PTT) | Requests local PTT authority for your station. Appears only when another client is connected and your station does not currently hold PTT. |
| `Close` | Closes the dialog. |

## Tips

- The table updates automatically as clients connect, disconnect, or change state. You do not need to reopen the dialog to see changes.
- Your own station's row is shown in a distinct color so you can locate it quickly in a crowded list.
- The `Enable` (PTT) button is hidden when your station already holds PTT or when you are the only connected client.

## Related

- [multiFLEX Dashboard overview](../../features/multi-flex/overview.md)
- [Enable multiFLEX on the radio](../../features/multi-flex/enable-multiflex-on-the-radio.md)
- [Grant or revoke local PTT](../../features/multi-flex/grant-or-revoke-local-ptt.md)
- [Check which antenna and frequency each TX station is using](../../features/multi-flex/check-which-antenna-and-frequency-each-tx-station-is-using.md)
