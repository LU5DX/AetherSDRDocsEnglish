# TCI Server Overview

The TCI Server applet runs a WebSocket server that speaks the Expert Electronics TCI protocol, letting third-party logging, digital-mode, and SDR applications — such as Log4OM and SunSDR tools — read and control the radio over a local network connection. Open the applet to start the server, set the port, and adjust audio gain for each RX and TX channel.

## Before you start

- AetherSDR must be connected to the radio. The TCI applet requires an active radio connection.
- This feature is only present in builds compiled with WebSocket support (`HAVE_WEBSOCKETS`). If the TCI tray button is absent, your build does not include TCI.

## How it works

The TCI applet is hidden by default. Toggle it open with the **TCI** tray button on the right sidebar.

When you click **Enable**, AetherSDR binds a WebSocket server on the configured port (default `50001`). Any TCI-compatible client that connects to `ws://<your-host>:<port>` can then query and command the radio using the TCI protocol. The applet displays the current server state and connected client count in the status area next to the **Enable** button.

RX audio for channels 1–4 follows the same DAX channel assignments as the DAX applet. The slice letter shown beside each RX and TX row — for example, `Slice A` — reflects whichever slice is currently assigned to that DAX channel. If no slice is assigned, the indicator shows `—`.

Gain levels set in the applet apply to the TCI audio stream and are independent of the radio's RF gain controls.

## What each control does

| Control                        | What it does                                                                                                                                                                      | Default                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RX1–RX4 gain+meter             | Combined level meter and gain slider for each TCI RX channel. Drag to set the output gain for that channel's audio stream.                                                        | 0.5                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| TX gain+meter                  | Drags set the TCI TX gain and emit tciTxGainChanged. Right-click opens TX overflow-mode picker (Clip / NaNGuard / Measure).                                                       | TciServer::setTxGain persists TciTxGain internally; UI mirrors the stored value. TCI TX audio is always allowed regardless of platform or hosted-DAX availability (evaluateDaxTxPolicy now unconditionally allows DaxTxRequestReason::TciTxAudio, v0.9.5.1, #2276). Right-click menu lets users choose how out-of-range (>1.0) samples from digital-mode clients are handled: Clip (saturating ±1.0, legacy default), NaNGuard (pass-through, only zero NaN/Inf), or Measure (true bypass with clip counting). Default is Clip so existing users see no behavior change (#3065). |
| RX/TX slice-assignment labels  | Read-only indicators showing which slice drives each row (`Slice A`, `Slice B`, etc., or `—` if unassigned). Uses rich text formatting so slice letters render correctly (#2606). | `—`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Port                           | WebSocket port the server listens on. Changing the value while the server is running restarts it on the new port. Values outside the valid range snap back to `50001`.            | `50001`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Enable                         | Starts or stops the TCI server. If the port is already in use, the button snaps back to off and the status shows `(port in use)` in red.                                          | Off                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Server status                  | Displays `(stopped)`, `:<port> (<N> clients)`, or `(port in use)`. Turns red on a bind failure.                                                                                   | `(stopped)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| TX overflow mode (right-click) | Right-click the TX gain meter/slider to open a context menu selecting the TX overflow handling mode. Emits tciTxOverflowModeChanged.                                              | New in v26.5.3. Clip clamps overshoots to ±1.0 with harmonic distortion; NaNGuard preserves bit-exact digital tones by only zeroing NaN/Inf; Measure counts overshoots for telemetry without mutation. Persisted as `TciTxOverflowMode` (0/1/2).                                                                                                                                                                                                                                                                                                                                  |

### TX overflow mode details

Right-click the **TX gain+meter** control to open a context menu with three options:

| Mode        | Behavior                                                                                                                                                                                                |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Clip (0)    | Hard-clamp overshoots to ±1.0. Defensive default; introduces harmonics on overshoot but protects downstream int16 conversion.                                                                          |
| NaNGuard (1)| Pass samples through bit-exact; only zero pathological NaN/Inf values. Preserves digital-mode tone fidelity; out-of-range floats reach the radio.                                                       |
| Measure (2) | Never mutate samples. Count overshoots for telemetry; the downstream int16 conversion still clamps in the radio-native DAX route.                                                                       |

The setting is persisted as `TciTxOverflowMode` and defaults to `0` (Clip) so existing users see no behavior change.

## Tips

- To start the TCI server automatically every time AetherSDR launches, enable `Settings > Autostart TCI with AetherSDR`. This sets the `AutoStartTCI` preference.
- The client count shown in the server status updates live as clients connect and disconnect. See [See how many TCI clients are connected](../../getting-started/setup/see-how-many-tci-clients-are-connected.md) for details.

## Troubleshooting

- **Status shows `(port in use)` and Enable snaps off** — Another process is already bound to that port. Change the port in the Port field to a free port in the range 1024–65535 and click Enable again. See [Change the TCI port](change-the-tci-port.md).
- **TCI tray button is missing** — This build of AetherSDR was compiled without WebSocket support. TCI is unavailable.
- **Slice labels show `—` for all channels** — No slices have a DAX channel assigned. Assign a DAX channel to a slice through the radio setup to populate the RX and TX labels.

## Related

- [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md)
- [Change the TCI port](change-the-tci-port.md)
- [Adjust TCI RX gain per channel](adjust-tci-rx-gain-per-channel.md)
- [Adjust TCI TX gain](adjust-tci-tx-gain.md)
- [Autostart TCI on launch](autostart-tci-on-launch.md)
- [See how many TCI clients are connected](../../getting-started/setup/see-how-many-tci-clients-are-connected.md)