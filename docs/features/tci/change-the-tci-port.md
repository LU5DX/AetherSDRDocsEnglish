# Change the TCI port

The TCI server listens on a configurable port. Change the port when the default conflicts with another application or when your logging or digital-mode software requires a specific port number.

## Before you start

- AetherSDR must be connected to the radio. The TCI applet requires an active radio connection.
- Open the TCI applet by clicking the **TCI** tray button on the right sidebar if it is not already visible.

## Steps

1. In the TCI applet, locate the **Port** field next to the "Port:" label at the bottom of the applet.
2. Click the **Port** field and type the new port number. Valid values are 1024–65535. The default is `50001`. Values outside this range snap back to `50001`.
3. Press **Enter** or move focus away from the field to confirm. The value is saved to `TciPort`.
4. If the server is currently running (Enable is toggled on), AetherSDR stops the server and restarts it on the new port automatically. No additional action is required.
5. If the server is not running, click **Enable** to start it on the new port.

## What each control does

| Control                        | Default                                                                                                                                | Valid range                                                                                                                                                                                                                                                                                                                       |
|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Port** field                 | `50001`                                                                                                                                | 1024–65535                                                                                                                                                                                                                                                                                                                        |
| **Enable / Disabled**          | Off (shows "Disabled")                                                                                                                 | "Disabled" / "Enabled"                                                                                                                                                                                                                                                                                                            |
| Server status indicator        | `(stopped)`                                                                                                                            | `(stopped)`, `:<port> (N clients)`, `(port in use)`                                                                                                                                                                                                                                                                               |
| **RX1** gain+meter             | 0.5                                                                                                                                    | 0.0–1.0 (combined slider/meter)                                                                                                                                                                                                                                                                                                   |
| **RX2** gain+meter             | 0.5                                                                                                                                    | 0.0–1.0 (combined slider/meter)                                                                                                                                                                                                                                                                                                   |
| **RX3** gain+meter             | 0.5                                                                                                                                    | 0.0–1.0 (combined slider/meter)                                                                                                                                                                                                                                                                                                   |
| **RX4** gain+meter             | 0.5                                                                                                                                    | 0.0–1.0 (combined slider/meter)                                                                                                                                                                                                                                                                                                   |
| **TX** gain+meter              | 0.5                                                                                                                                    | 0.0–1.0 (combined slider/meter)                                                                                                                                                                                                                                                                                                   |
| RX/TX slice-assignment labels  | —                                                                                                                                      | `—` or `Slice <letter>` (rich text)                                                                                                                                                                                                                                                                                               |
| TX overflow mode (right-click) | Right-click the TX gain meter/slider to open a context menu selecting the TX overflow handling mode. Emits `tciTxOverflowModeChanged`. | New in v26.5.3. Clip (0): clamps overshoots to ±1.0 with harmonic distortion; NaNGuard (1): preserves bit-exact digital tones by only zeroing NaN/Inf; Measure (2): counts overshoots for telemetry without mutation. Persisted as `TciTxOverflowMode` (0/1/2). Default is Clip so existing users see no behavior change (#3065). |

## Tips

- If you change the port while the server is enabled, the restart is immediate. Connected clients will be disconnected and must reconnect to the new port.
- If the status shows `(port in use)` after clicking Enable, choose a different port number and try again.
- RX and TX gain sliders control the TCI audio level for their respective channels. Drag to adjust; the value is persisted in `TciRxGain1`–`TciRxGain4` and `TciTxGain`.
- Each TCI RX gain slider has an accessible name of "TCI RX 1 gain", "TCI RX 2 gain", etc., and the TX gain slider has an accessible name of "TCI TX gain" for screen reader compatibility.
- The Enable button text changes to reflect the current state: "Disabled" when the server is stopped, "Enabled" when it is running. If `AutoStartTCI` is set to `True` in settings, the button starts as "Enabled" and the server starts automatically on launch.
- Slice-assignment labels show which slice drives each RX/TX row. The slice letter may appear in rich text format for improved display.
- Right-click the TX gain meter/slider to open the TX overflow-mode picker. Choose how out-of-range (>1.0) samples from digital-mode clients are handled:
  - **Clip (saturating ±1.0)** — Hard-clamp overshoots to ±1.0. Default that introduces harmonics on overshoot but protects downstream int16 conversion.
  - **NaN guard (zero NaN/Inf only)** — Pass samples through bit-exact; only zero pathological NaN/Inf values. Preserves digital-mode tone fidelity; out-of-range floats reach the radio.
  - **Measure only (true bypass)** — Never mutate samples. Count overshoots for telemetry; the downstream int16 conversion still clamps in the radio-native DAX route.

## Troubleshooting

- **Status shows `(port in use)` after enabling** — Another application is already bound to that port. Enter a different port number in the **Port** field and click Enable again.
- **Port field reverts to `50001`** — The value entered was outside the 1024–65535 range. Enter a value within the valid range.

## Related

- [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md)
- [Autostart TCI on launch](autostart-tci-on-launch.md)
- [TCI Server overview](overview.md)