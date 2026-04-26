# Enable Autostart for CAT with AetherSDR

Enabling autostart for CAT instructs AetherSDR to create virtual serial ports for CAT control each time the application launches, so external logging or contest software can connect without manual intervention.

## Before you start

- AetherSDR must be running on Linux or macOS. This feature creates virtual serial ports and is not available on Windows.
- Confirm that any software you intend to connect via CAT is not already holding the virtual ports open from a previous session.

## Steps

1. Click `Settings` in the menu bar.
2. Click `Autostart CAT with AetherSDR`.

The menu item is checkable. A check mark next to the label means autostart is enabled. Clicking the item again removes the check mark and disables autostart.

## What each control does

| Control | Description | Persisted key |
|---|---|---|
| `Autostart CAT with AetherSDR` | Checkable menu item. When checked, AetherSDR creates virtual serial ports for CAT control on every launch (Linux and macOS only). | `AutoStartCAT` |

## Tips

- The setting takes effect on the next launch of AetherSDR. Toggling it during a running session does not immediately start or stop CAT; restart the application to apply the change.
- If you also use rigctld for CAT control, see [Enable autostart for rigctld with AetherSDR](enable-autostart-for-rigctld-with-aethersdr.md) — running both simultaneously may cause port conflicts.

## Troubleshooting

- **Virtual serial ports do not appear after enabling autostart** — Verify you are running AetherSDR on Linux or macOS. This feature is not active on Windows. Also confirm you have restarted AetherSDR after enabling the setting.
- **CAT software cannot open the virtual port** — Another process may already hold the port open. Close any other CAT clients, then restart AetherSDR.

## Related

- [Enable autostart for rigctld with AetherSDR](enable-autostart-for-rigctld-with-aethersdr.md)
- [Enable autostart for TCI with AetherSDR](enable-autostart-for-tci-with-aethersdr.md)
- [Enable autostart for DAX with AetherSDR](enable-autostart-for-dax-with-aethersdr.md)
- [USB Cables](usb-cables.md)
