# Fix AetherSDR crash on quit when TCI is enabled and a radio is connected

AetherSDR v0.9.6 and earlier could crash on exit when the TCI server was running and a radio was connected. Version 0.9.7 fixes this. If you are still seeing a crash on quit, the steps below confirm you are running the corrected version and guide you through a clean TCI configuration.

## Before you start

- You are running AetherSDR v0.9.7 or later. Earlier builds contain the use-after-free defect that caused the crash; upgrading is the only complete fix.
- A FLEX-8600 radio is connected and visible in the application.
- The TCI applet is visible. If it is not, click the `TCI` tray button on the right sidebar to show it.

## Steps

1. Quit AetherSDR using `File > Quit` or the keyboard shortcut `Ctrl+Q`.
2. If the application crashes at this point, confirm your installed version is v0.9.7 or later. If it is not, upgrade before continuing.
3. After upgrading, reopen AetherSDR and connect to your radio.
4. Open the TCI applet by clicking the `TCI` tray button on the right sidebar if it is not already visible.
5. In the `Port` field, confirm the port value is between 1024 and 65535. The default is `50001`. If the field is blank or out of range, type `50001` and press Enter — the field snaps to `50001` automatically for out-of-range values.
6. Click `Enable` to start the TCI server.
7. Confirm the status indicator next to `Enable` shows `:<port> (0 clients)` rather than `(port in use)`. If it shows `(port in use)`, see Troubleshooting below.
8. Use the radio normally, then quit with `File > Quit`. The application should exit cleanly.

## What each control does

| Control                        | Default                                                                                                                     | Valid range                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Port` field                   | `50001`                                                                                                                     | 1024–65535                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `Enable` toggle                | Off                                                                                                                         | On / Off                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| RX1 gain+meter                 | 0.5                                                                                                                         | 0.0–1.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| RX2 gain+meter                 | 0.5                                                                                                                         | 0.0–1.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| RX3 gain+meter                 | 0.5                                                                                                                         | 0.0–1.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| RX4 gain+meter                 | 0.5                                                                                                                         | 0.0–1.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| TX gain+meter                  | Drags set the TCI TX gain and emit tciTxGainChanged. Right-click opens TX overflow-mode picker (Clip / NaNGuard / Measure). | TciServer::setTxGain persists `TciTxGain` internally; UI mirrors the stored value. TCI TX audio is always allowed regardless of platform or hosted-DAX availability (evaluateDaxTxPolicy now unconditionally allows DaxTxRequestReason::TciTxAudio, v0.9.5.1, #2276). Right-click menu lets users choose how out-of-range (>1.0) samples from digital-mode clients are handled: Clip (saturating ±1.0, legacy default), NaNGuard (pass-through, only zero NaN/Inf), or Measure (true bypass with clip counting). Default is Clip so existing users see no behavior change (#3065). |
| TX overflow mode (right-click) | Clip (0)                                                                                                                    | Clip (0), NaNGuard (1), Measure (2)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

Out-of-range values entered in the `Port` field snap to `50001`. If `Enable` is toggled on and the bind fails, the button snaps back to off and the status shows `(port in use)`.
### TX gain+meter details

Drags set the TCI TX gain and emit `tciTxGainChanged`. TCI TX audio is always allowed regardless of platform or hosted-DAX availability.

Right-click the TX gain meter/slider to open the TX overflow-mode context menu. This lets you choose how out-of-range (>1.0) samples from digital-mode clients are handled:

- **Clip (saturating ±1.0)** — Hard-clamp overshoots to ±1.0. This is the legacy default; it protects downstream int16 conversion but introduces harmonics on overshoot.
- **NaN guard (zero NaN/Inf only)** — Pass samples through bit-exact; only zero pathological NaN/Inf values. Preserves digital-mode tone fidelity. Out-of-range float values reach the radio.
- **Measure only (true bypass)** — Never mutate samples. Count overshoots for telemetry only. The downstream int16 conversion still clamps in the radio-native DAX route.

The selected mode is persisted as `TciTxOverflowMode` (0/1/2). Default is `Clip` so existing users see no behavior change.

### Slice assignment labels

The RX1–RX4 and TX rows show a label indicating which slice currently drives that channel. The label shows `—` when no slice is assigned, or `Slice <letter>` when a slice is active. These labels share the DAX channel mapping.

### Server status indicator

The status label next to `Enable` shows the server state and connected client count:

- `(stopped)` — Server is not running.
- `:<port> (N clients)` — Server is running on the specified port with N connected clients.
- `(port in use)` — Server failed to start because another process is bound to the port.

The label is styled using the application theme. In earlier versions the label used a hard-coded color; in v26.6.1 the color is derived from the theme's `background.3` color for consistent appearance across light and dark themes.

## Tips

- If you use `Settings > Autostart TCI with AetherSDR`, the TCI server starts automatically on each launch. This setting was present before v0.9.7 and is safe to use after upgrading.
- The crash in earlier versions occurred because the TCI server was torn down after the radio model had already been released. In v0.9.7 the teardown order was corrected: the TCI server is shut down while the radio model is still alive. No configuration change on your part triggers or avoids this — upgrading to v0.9.7 is the fix.
- Starting with v26.5.2.1, the slice assignment labels (RX1–RX4 status and TX status) can render rich text. If a slice letter contains HTML characters (such as an ampersand or angle brackets), the label displays correctly instead of showing raw markup. This improves compatibility with third-party software that may send unusual slice identifiers.

## Troubleshooting

- **Status shows `(port in use)` after clicking `Enable`** — Another process is already bound to that port. Enter a different port number in the `Port` field and press Enter, then click `Enable` again.
- **Application still crashes on quit after upgrading** — Confirm you are running v0.9.7 or later. Check `Help > About` for the version string. If the version is correct and crashes persist, disable `Enable` before quitting to isolate whether TCI is still involved.
- **`Enable` snaps back to off immediately** — The port bind failed. The status label turns red and shows `(port in use)`. Change the port value and try again.
- **Slice assignment label shows raw HTML** — This indicates you are running a version earlier than v26.5.2.1. Upgrade to the latest version to ensure proper rendering of slice identifiers.

## Related

- [TCI Server overview](../../features/tci/overview.md)
- [Enable the TCI server for Log4OM / SunSDR clients](../../features/tci/enable-the-tci-server-for-log4om-sunsdr-clients.md)
- [Autostart TCI on launch](../../features/tci/autostart-tci-on-launch.md)
- [Change the TCI port](../../features/tci/change-the-tci-port.md)
- [See how many TCI clients are connected](see-how-many-tci-clients-are-connected.md)