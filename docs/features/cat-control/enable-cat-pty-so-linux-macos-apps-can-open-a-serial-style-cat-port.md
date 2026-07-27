# Enable CAT PTY so Linux/macOS apps can open a serial-style CAT port

CAT PTY creates four virtual serial port symlinks that logging and contest software can open as if they were physical serial devices. Use this feature on Linux or macOS when your external application expects a serial port path rather than a TCP connection.

## Before you start

- AetherSDR must be connected to the radio. The CAT Control applet requires an active radio connection.
- The PTY feature is available on Linux and macOS only.
- Open the CAT Control applet by clicking the **CAT** tray button on the right sidebar. The applet is hidden by default.

## Steps

1. Click the **CAT** tray button on the right sidebar to open the CAT Control applet.
2. Click **Enable TTY**.

   The button turns green when active. AetherSDR creates four symlinks:

   - Linux: `$XDG_RUNTIME_DIR/aethersdr/cat-A` through `cat-D`
   - macOS: `~/Library/Caches/AetherSDR/cat-A` through `cat-D`

3. In your external application, set the serial port path to the symlink for the channel you want to control — for example, on Linux: `$XDG_RUNTIME_DIR/aethersdr/cat-A` for channel A.
4. Each channel row in the applet updates to show the active PTY path once the symlink is running.

## What each control does

| Control              | Default     | Valid range |
|----------------------|-------------|-------------|
| **Enable TTY**       | Off         | On / Off    |
| **Enable TCP**       | Off         | On / Off    |
| **Base**             | `4532`      | 1024–65535  |
| A/B/C/D channel rows | `(stopped)` | —           |

Each channel row shows a per-port enable checkbox with a high-contrast indicator. The checkbox shows a filled accent color when checked, making the on/off state readable at a glance.

## Tips

- Each channel (A, B, C, D) maps to one radio slice. Point your logging software at the symlink that corresponds to the slice you want it to control.
- To have AetherSDR start the PTY symlinks automatically at launch, enable `Settings > Autostart CAT with AetherSDR`.
- You can run **Enable TTY** and **Enable TCP** independently. Enabling one does not require enabling the other.
- In v26.5.3, the PTY symlink location moved from `/tmp` to per-user runtime directories for security hardening (GHSA-qxhr-cwrc-pvrm). Symlinks are created atomically to prevent TOCTOU race conditions.
- In v26.7.4, the **Enable CAT** button label updates dynamically to show "Enabled" or "Disabled" text, reflecting the current state.

## Troubleshooting

- **Enable TTY has no effect or symlinks do not appear** — PTY support requires Linux or macOS. The feature is not available on Windows.
- **External application cannot open the port** — Confirm the application is using the correct path. On Linux, run `echo $XDG_RUNTIME_DIR/aethersdr/cat-A` to resolve the full path. On macOS, use `~/Library/Caches/AetherSDR/cat-A`. Check that **Enable TTY** is still active (button should be green) and that AetherSDR remains connected to the radio.
- **Symlink path shown in the row does not match `/tmp/AetherSDR-CAT-A`** — Starting with v26.5.3, symlinks are no longer created in `/tmp`. The path shown updates to the actual PTY device path under the per-user runtime directory. Use whatever path is displayed in the channel row.
- **Symlink path shows instead of a running path** — The path shown updates to `RigctlPty::defaultSymlinkPath(i)` format when the server is stopped, matching the per-user location scheme.
- **Per-port enable checkbox is hard to see** — In v26.7.4, the checkbox indicator received a high-contrast border and filled accent color for better visibility against the dark applet background.

## Related

- Enable CAT TCP so N1MM, Log4OM, WSJT-X can control the radio
- [Autostart CAT servers with AetherSDR](autostart-cat-servers-with-aethersdr.md)
- [CAT Control overview](overview.md)
- [Check how many external clients are connected to each channel](../../getting-started/setup/check-how-many-external-clients-are-connected-to-each-channel.md)