# Enable FreeDV QSO Reporter WebSocket

Connect AetherSDR to the FreeDV QSO reporter at `qso.freedv.org` to receive FreeDV activity spots on the panadapter.

## Before you start

- AetherSDR must have been built with WebSocket support (`HAVE_WEBSOCKETS`). If the FreeDV tab is absent from SpotHub, your build does not include this feature.
- Spot overlay must be active for spots to appear on the panadapter. See [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md) for display settings.

## Steps

1. Open `Settings > SpotHub...`.
2. Click the **FreeDV** tab.
3. Note that the **Server:** indicator shows `qso.freedv.org (WebSocket)`. The endpoint is fixed and cannot be changed.
4. Click **Start**. The status indicator changes to **Connected** when the WebSocket is established.
5. Incoming activity appears in the **FreeDV Spots** console.
6. To change the color of FreeDV spots on the panadapter, click **Spot Color:** and choose a color from the picker. This is saved as `FreeDvSpotColor`.
7. To connect automatically every time AetherSDR starts, enable **Auto-start on startup**. This is saved as `FreeDvAutoStart`.

## What each control does

| Control | Kind | Behavior | Setting key |
|---|---|---|---|
| **Server:** | Indicator | Shows the fixed endpoint `qso.freedv.org (WebSocket)`. Not editable. | — |
| **Start / Stop** | Button | Connects or disconnects the FreeDV WebSocket. | — |
| **Auto-start on startup** | Toggle button | Starts the FreeDV WebSocket automatically when AetherSDR launches. | `FreeDvAutoStart` |
| **FreeDV Spots** | Text field | Read-only console of received FreeDV activity. | — |
| **Spot Color:** | Button | Opens a color picker to set the panadapter spot color for FreeDV spots. | `FreeDvSpotColor` |

## Troubleshooting

- **FreeDV tab is not visible** — The tab is only present in builds compiled with WebSocket support. Check with your package provider or build configuration.
- **Status stays Disconnected after clicking Start** — Check your internet connection. The client connects to `qso.freedv.org` over WebSocket; a firewall or proxy may be blocking outbound WebSocket traffic.
- **Spots appear in the console but not on the panadapter** — Confirm the master spot overlay is enabled. Open `Settings > SpotHub...`, go to the **Display** tab, and verify **Spots:** is set to **Enabled** (`IsSpotsEnabled`).

## Related

- [SpotHub overview](overview.md)
- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
- [Pick colors for each spot source](pick-colors-for-each-spot-source.md)
- [Tune to a spot by double-clicking the spot list](tune-to-a-spot-by-double-clicking-the-spot-list.md)
- [Poll POTA activations](poll-pota-activations.md)
