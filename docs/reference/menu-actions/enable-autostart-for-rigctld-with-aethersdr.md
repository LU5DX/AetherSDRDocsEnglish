# Enable Autostart for rigctld with AetherSDR

When this setting is enabled, AetherSDR automatically spawns a rigctld CAT server each time the application starts. This lets external logging, contest, and digital mode software connect to your radio via the standard rigctld interface without requiring manual startup steps.

## Before you start

- AetherSDR must be installed and able to reach your FLEX-8600 radio.
- rigctld must be installed and accessible on your system PATH.

## Steps

1. Click **Settings** in the menu bar.
2. Click **Autostart rigctld with AetherSDR**.

The menu item toggles on or off each time you click it. A check mark next to the label indicates it is enabled. The setting persists across sessions via the `AutoStartRigctld` AppSettings key.

## What each control does

| Control | Description | Persisted key |
|---|---|---|
| Autostart rigctld with AetherSDR | Checkable menu item. When checked, AetherSDR spawns rigctld at startup. When unchecked, rigctld is not started automatically. | `AutoStartRigctld` |

## Tips

- To disable autostart, click **Settings > Autostart rigctld with AetherSDR** again to remove the check mark.
- If you only need virtual serial port CAT control rather than rigctld, see [Enable autostart for CAT with AetherSDR](enable-autostart-for-cat-with-aethersdr.md).

## Troubleshooting

- **rigctld does not start on launch** — Confirm that rigctld is installed and available on your system PATH. If the binary cannot be found, AetherSDR cannot spawn it regardless of this setting.
- **External software cannot connect to rigctld** — Verify that the port rigctld listens on is not blocked by a firewall and matches the port configured in your external software. See your rigctld documentation for port configuration.

## Related

- [Enable autostart for CAT with AetherSDR](enable-autostart-for-cat-with-aethersdr.md)
- [Enable autostart for TCI with AetherSDR](enable-autostart-for-tci-with-aethersdr.md)
- [Enable autostart for DAX with AetherSDR](enable-autostart-for-dax-with-aethersdr.md)
- [Getting Started](getting-started.md)
