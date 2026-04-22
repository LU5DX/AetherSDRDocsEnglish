# Enable FreeDV QSO Reporter WebSocket

Connect AetherSDR to the FreeDV QSO reporter at `qso.freedv.org` to display FreeDV activity as spots on the panadapter.

## Before you start

- The FreeDV WebSocket source is only available in builds compiled with WebSocket support (`HAVE_WEBSOCKETS`). If the FreeDV tab is absent from SpotHub, your build does not include it.
- Spots appear on the panadapter only when the master spot overlay is enabled. See [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md) if spots are not visible.

## Steps

1. Open `Settings > SpotHub...`.
2. Click the **FreeDV** tab.
3. Confirm the **Server:** indicator shows `qso.freedv.org (WebSocket)`. The endpoint is fixed and cannot be edited.
4. Click **Start**. The status indicator changes to **Connected** when the WebSocket link is established.
5. Watch the **FreeDV Spots** console for incoming activity.
6. To change the color used for FreeDV spots on the panadapter, click **Spot Color:** and choose a color from the picker.
7. To connect automatically on every launch, enable **Auto-start on startup**.

## What each control does

| Control | Description | Setting key |
|---|---|---|
| **Server:** | Read-only indicator. Always `qso.freedv.org (WebSocket)`. | — |
| **Start / Stop** | Connects or disconnects the FreeDV WebSocket. | — |
| **Auto-start on startup** | Reconnects to the FreeDV WebSocket each time AetherSDR starts. | `FreeDvAutoStart` |
| **FreeDV Spots** | Read-only console showing raw FreeDV spot activity. | — |
| **Spot Color:** | Opens a color picker. The chosen color is used for FreeDV spots on the panadapter. | `FreeDvSpotColor` |

## Troubleshooting

- **FreeDV tab is missing** — Your AetherSDR build was compiled without WebSocket support. FreeDV and TCI WebSocket features require a `HAVE_WEBSOCKETS` build. Check with your package provider or build from source with WebSocket support enabled.
- **Status stays Disconnected after clicking Start** — Verify that AetherSDR has outbound internet access to `qso.freedv.org` on the WebSocket port. A firewall or proxy may be blocking the connection.
- **Spots appear in the FreeDV Spots console but not on the panadapter** — Confirm that **Spots:** is set to Enabled on the **Display** tab of SpotHub. See [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md).

## Related

- [Poll POTA activations](poll-pota-activations.md)
- [Start WSJT-X UDP listener and filter for CQ, POTA or calls to me](start-wsjt-x-udp-listener-and-filter-for-cq-pota-or-calls-to-me.md)
- [Pick colors for each spot source](pick-colors-for-each-spot-source.md)
- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
- [Tune to a spot by double-clicking the spot list](tune-to-a-spot-by-double-clicking-the-spot-list.md)
