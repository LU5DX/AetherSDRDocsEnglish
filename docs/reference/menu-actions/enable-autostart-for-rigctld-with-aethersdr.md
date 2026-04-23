# Enable autostart for rigctld with AetherSDR

When this setting is enabled, AetherSDR automatically spawns a rigctld CAT server each time the application starts. This lets logging programs and other external software use the Hamlib rigctld interface without requiring you to start it manually.

## Before you start

- AetherSDR must be installed and able to connect to your Flex radio.
- rigctld must be installed and accessible on your system PATH.

## Steps

1. Click `Settings` in the menu bar.
2. Click `Autostart rigctld with AetherSDR`.

The menu item is a checkable toggle. A check mark next to the label indicates the setting is active. The preference is saved to `AutoStartRigctld` and persists across restarts.

To disable autostart, repeat the same steps. The check mark will be removed and rigctld will no longer be spawned on launch.

## Tips

- If you also use virtual serial ports for CAT control, see [Enable autostart for CAT with AetherSDR](enable-autostart-for-cat-with-aethersdr.md) — the two features serve different use cases and can be used independently or together.
- Changes take effect on the next application launch. Toggling the setting does not start or stop a currently running rigctld process.

## Troubleshooting

- **rigctld does not start on launch** — Confirm that rigctld is installed and available on your system PATH. AetherSDR does not bundle rigctld; it must be installed separately (typically via your distribution's Hamlib package).
- **Check mark disappears after restart** — Verify that AetherSDR has write access to its settings storage. If the application cannot persist settings, `AutoStartRigctld` will revert to its default unchecked state.

## Related

- [Enable autostart for CAT with AetherSDR](enable-autostart-for-cat-with-aethersdr.md)
- [Enable autostart for TCI with AetherSDR](enable-autostart-for-tci-with-aethersdr.md)
- [Enable autostart for DAX with AetherSDR](enable-autostart-for-dax-with-aethersdr.md)
- [Getting Started](getting-started.md)
