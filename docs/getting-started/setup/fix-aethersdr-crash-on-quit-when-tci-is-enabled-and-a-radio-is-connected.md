# TCI Server (TCI Applet)

AetherSDR can run an Expert-style TCI WebSocket server so third-party logging, digital-mode, and SDR software (Log4OM, SunSDR tools, etc.) can read and control the radio over the TCI protocol. TCI TX audio is received over the WebSocket and fed into a dedicated dax_tx stream slot that is independent of the Windows SmartSDR DAX2 audio device path, so TCI TX works on all platforms including Windows and Linux without PipeWire.

## Before you start

- A FLEX-8600 radio is connected and visible in the application.
- The TCI applet is visible. If it is not, click the `TCI` tray button on the right sidebar to show it.

## Steps

1. Open the TCI applet by clicking the `TCI` tray button on the right sidebar if it is not already visible.
2. In the `Port` field, enter a port value between 1024 and 65535. The default is `50001`. If the field is blank or out of range, type `50001` and press Enter — the field snaps to `50001` automatically for out-of-range values.
3. Click `Enable` to start the TCI server. The button text changes to `Enabled` when the server is running. If `Settings > Autostart TCI with AetherSDR` was enabled, the button starts as `Enabled` and the server starts automatically.
4. Confirm the status indicator next to `Enable` shows `:<port> (0 clients)` rather than `(port in use)`. If it shows `(port in use)`, see Troubleshooting below.
5. Configure your third-party software to connect to the TCI server at `localhost:<port>`.

## What each control does

| Control                        | Default                                                                                                                     | Valid range                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Port` field                   | `50001`                                                                                                                     | 1024–65535                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `Enable` toggle                | Off (or On if autostart is configured)                                                                                      | On / Off. Button text shows `Enabled` or `Disabled`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| RX1 gain+meter                 | 0.5                                                                                                                         | 0.0–1.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| RX2 gain+meter                 | 0.5                                                                                                                         | 0.0–1.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| RX3 gain+meter                 | 0.5                                                                                                                         | 0.0–1.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| RX4 gain+meter                 | 0.5                                                                                                                         | 0.0–1.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| RX5 gain+meter                 | 0.5                                                                                                                         | 0.0–1.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| RX6 gain+meter                 | 0.5                                                                                                                         | 0.0–1.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| RX7 gain+meter                 | 0.5                                                                                                                         | 0.0–1.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| RX8 gain+meter                 | 0.5                                                                                                                         | 0.0–1.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| TX gain+meter                  | Drags set the TCI TX gain and emit tciTxGainChanged. Right-click opens TX overflow-mode picker (Clip / NaNGuard / Measure). | TciServer::setTxGain persists TciTxGain internally; UI mirrors the stored value. TCI TX audio is always allowed regardless of platform or hosted-DAX availability (evaluateDaxTxPolicy now unconditionally allows DaxTxRequestReason::TciTxAudio, v0.9.5.1, #2276). Right-click menu lets users choose how out-of-range (>1.0) samples from digital-mode clients are handled: Clip (saturating ±1.0, legacy default), NaNGuard (pass-through, only zero NaN/Inf), or Measure (true bypass with clip counting). Default is Clip so existing users see no behavior change (#3065). |
| TX overflow mode (right-click) | Clip (0)                                                                                                                    | Clip (0), NaNGuard (1), Measure (2)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

### Enable toggle details

The `Enable` button is a toggle that starts or stops the TCI server. The button text changes to `Enabled` when the server is running and to `Disabled` when stopped. If `Settings > Autostart TCI with AetherSDR` is enabled, the button initializes as `Enabled` and the server starts automatically on application launch. If the port bind fails, the button snaps back to `Disabled` and the status shows `(port in use)` in red.

### RX gain+meter details

Each RX channel (1–8) has a combined meter and slider. Drag the slider to set the TCI RX gain for that channel. The gain value is persisted separately per channel as `TciRxGain1` through `TciRxGain8`. Each slider has an accessible name ("TCI RX 1 gain", "TCI RX 2 gain", etc.) for screen reader compatibility.

The number of visible RX rows is bounded by the radio's slice capacity. On radios with fewer than 8 slices, RX rows above the slice count are hidden. This mirrors the behavior of the DAX applet. The TCI receiver (trx) index is not capped at 4; it is a positional slice index bounded by the slice count (up to 8 on a FLEX-6700). DAX channels 5–8 have TCI representation.

### TX gain+meter details

Drags set the TCI TX gain and emit `tciTxGainChanged`. TCI TX audio is always allowed regardless of platform or hosted-DAX availability.

Right-click the TX gain meter/slider to open the TX overflow-mode context menu. This lets you choose how out-of-range (>1.0) samples from digital-mode clients are handled:

- **Clip (saturating ±1.0)** — Hard-clamp overshoots to ±1.0. This is the legacy default; it protects downstream int16 conversion but introduces harmonics on overshoot.
- **NaN guard (zero NaN/Inf only)** — Pass samples through bit-exact; only zero pathological NaN/Inf values. Preserves digital-mode tone fidelity. Out-of-range float values reach the radio.
- **Measure only (true bypass)** — Never mutate samples. Count overshoots for telemetry only. The downstream int16 conversion still clamps in the radio-native DAX route.

The selected mode is persisted as `TciTxOverflowMode` (0/1/2). Default is `Clip` so existing users see no behavior change.

### Slice assignment labels

The RX1–RX8 and TX rows show a label indicating which slice currently drives that channel. The label shows `—` when no slice is assigned, or `Slice <letter>` when a slice is active. These labels share the DAX channel mapping.

### Server status indicator

The status label next to `Enable` shows the server state and connected client count:

- `(stopped)` — Server is not running.
- `:<port> (N clients)` — Server is running on the specified port with N connected clients.
- `(port in use)` — Server failed to start because another process is bound to the port.

The label is styled using the application theme. In earlier versions the label used a hard-coded color; in v26.6.1 the color is derived from the theme's `background.3` color for consistent appearance across light and dark themes.

## Tips

- If you use `Settings > Autostart TCI with AetherSDR`, the TCI server starts automatically on each launch. The button text shows `Enabled` in this case.
- The crash on quit that affected v0.9.6 and earlier was fixed in v0.9.7. The fix ensures the TCI server is torn down after the audio thread stops but while the radio model is still alive, preventing a use-after-free.
- Starting with v26.5.2.1, the slice assignment labels (RX1–RX8 status and TX status) can render rich text. If a slice letter contains HTML characters (such as an ampersand or angle brackets), the label displays correctly instead of showing raw markup.
- Starting with v26.5.1, three TCI v2.0 commands (volume, drive, rx_volume) are supported with bidirectional state sync.
- Starting with v26.5.3, panadapter spectrum forwarding and tx_gain / ALC are exposed.
- The Port field, Enable toggle, and status indicator have accessible names and descriptions for screen reader compatibility. The Port field is labeled "TCI port" and the Enable button is labeled "TCI server enable".

## Troubleshooting

- **Status shows `(port in use)` after clicking `Enable`** — Another process is already bound to that port. Enter a different port number in the `Port` field and press Enter, then click `Enable` again. The button snaps back to `Disabled` and the status turns red.
- **Application crashes on quit** — Confirm you are running v0.9.7 or later. Check `Help > About` for the version string. If the version is correct and crashes persist, disable `Enable` before quitting to isolate whether TCI is still involved.
- **`Enable` snaps back to off immediately** — The port bind failed. The status label turns red and shows `(port in use)`. Change the port value and try again.
- **Slice assignment label shows raw HTML** — This indicates you are running a version earlier than v26.5.2.1. Upgrade to the latest version to ensure proper rendering of slice identifiers.
- **RX5–RX8 rows are hidden** — The radio's slice capacity is less than 8. Rows above the slice count are hidden to reflect the radio's actual capabilities. This is expected behavior; the DAX applet behaves the same way.

## Related

- [TCI Server overview](../../features/tci/overview.md)
- [Enable the TCI server for Log4OM / SunSDR clients](../../features/tci/enable-the-tci-server-for-log4om-sunsdr-clients.md)
- [Autostart TCI on launch](../../features/tci/autostart-tci-on-launch.md)
- [Change the TCI port](../../features/tci/change-the-tci-port.md)
- [See how many TCI clients are connected](see-how-many-tci-clients-are-connected.md)