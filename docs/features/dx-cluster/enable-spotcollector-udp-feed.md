# Enable SpotCollector UDP feed

AetherSDR can receive DX spots broadcast by Ham Radio Deluxe's SpotCollector over UDP and display them on the panadapter. This page explains how to start the listener, set the correct port, and configure it to start automatically.

## Before you start

- SpotCollector must be installed, configured, and running on the same machine or local network, and set to broadcast spots via UDP.
- Note the UDP port SpotCollector is broadcasting on — you will need to enter it in AetherSDR.

## Steps

1. Open `Settings > SpotHub...`.
2. Click the **SpotCollector** tab.
3. Set **UDP Port:** to the port SpotCollector is broadcasting on. Valid range: 1–65535. This value is saved as `SpotCollectorPort`.
4. Click **Start**.
5. Confirm the status indicator changes to **Listening**. Incoming spots will appear in the **SpotCollector Spots** console as they arrive.
6. To have the listener start automatically every time AetherSDR launches, enable **Auto-start on startup**. This is saved as `SpotCollectorAutoStart`.

## What each control does

| Control | Description | Setting key |
|---|---|---|
| **UDP Port:** | UDP port AetherSDR listens on for SpotCollector broadcasts. Valid range: 1–65535. | `SpotCollectorPort` |
| **Start / Stop** | Starts or stops the UDP listener. | — |
| **Auto-start on startup** | Starts the listener automatically on launch. | `SpotCollectorAutoStart` |
| **SpotCollector Spots** | Read-only console showing spots received from SpotCollector. | — |

## Tips

- Spots received from SpotCollector appear alongside spots from other sources in the **Spot List** tab. The **Source** column identifies them.
- If the panadapter spot overlay is not visible, check that **Spots:** is set to **Enabled** on the **Display** tab.

## Troubleshooting

- **Status stays Stopped / no spots appear** — Verify that SpotCollector is actively broadcasting and that the UDP port in AetherSDR matches the port configured in SpotCollector. Check that no firewall is blocking UDP traffic on that port.
- **Listener starts but the panadapter shows no spots** — Confirm that the master spot overlay is on: open the **Display** tab and check that **Spots:** is **Enabled**.

## Related

- [SpotHub overview](overview.md)
- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
- [Pick colors for each spot source](pick-colors-for-each-spot-source.md)
- [Tune to a spot by double-clicking the spot list](tune-to-a-spot-by-double-clicking-the-spot-list.md)
- [Clear all spots from the panadapter](clear-all-spots-from-the-panadapter.md)
