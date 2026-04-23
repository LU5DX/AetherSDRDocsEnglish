# Enable SpotCollector UDP feed

AetherSDR can receive DX spots broadcast by Ham Radio Deluxe's SpotCollector over UDP and display them on the panadapter. Use this page to start the listener and optionally enable it on every launch.

## Before you start

- Ham Radio Deluxe with SpotCollector must be running and configured to broadcast UDP spot data.
- Know which UDP port SpotCollector is broadcasting on and confirm it matches what you set in AetherSDR.

## Steps

1. Open `Settings > SpotHub...`.
2. Click the **SpotCollector** tab.
3. Set **UDP Port:** to the port SpotCollector is broadcasting on. Valid range: 1–65535. This value is saved as `SpotCollectorPort`.
4. Click **Start**. The status indicator changes to **Listening** when the UDP socket is bound successfully.
5. Verify incoming data appears in the **SpotCollector Spots** console.
6. To start the listener automatically on every launch, enable **Auto-start on startup**. This saves as `SpotCollectorAutoStart`.

## What each control does

| Control | Behavior | Setting key | Valid range |
|---|---|---|---|
| **UDP Port:** | UDP port AetherSDR listens on for SpotCollector broadcasts. | `SpotCollectorPort` | 1–65535 |
| **Start / Stop** | Starts or stops the UDP listener. | — | — |
| **Auto-start on startup** | Starts the listener automatically when AetherSDR launches. | `SpotCollectorAutoStart` | — |
| **SpotCollector Spots** | Read-only console showing received spot data. | — | — |

## Tips

- Spots received from SpotCollector appear in the unified spot list on the **Spot List** tab alongside spots from other sources. The **Source** column identifies them.
- If the panadapter spot overlay is not visible, check that **Spots:** is set to **Enabled** on the **Display** tab.

## Troubleshooting

- **Status stays at Stopped after clicking Start** — Another application may already be bound to the same UDP port. Change **UDP Port:** to a free port and update SpotCollector to match.
- **SpotCollector Spots console is empty** — Confirm SpotCollector is running and set to broadcast on the same UDP port. Check that no firewall is blocking local UDP traffic on that port.
- **Spots do not appear on the panadapter** — Open the **Display** tab and confirm **Spots:** is **Enabled**.

## Related

- [SpotHub overview](overview.md)
- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
- [Tune to a spot by double-clicking the spot list](tune-to-a-spot-by-double-clicking-the-spot-list.md)
- [Pick colors for each spot source](pick-colors-for-each-spot-source.md)
