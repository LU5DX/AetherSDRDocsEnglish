# TCI Server applet

The TCI Server applet runs an Expert-style TCI WebSocket server so third-party logging, digital-mode, and SDR software (Log4OM, SunSDR tools, etc.) can read and control the radio over the TCI protocol. TCI TX audio is received over the WebSocket and fed into a dedicated dax_tx stream slot that is independent of the Windows SmartSDR DAX2 audio device path, so TCI TX works on all platforms including Windows and Linux without PipeWire (v0.9.5.1, #2276).

In v0.9.7, a crash-on-quit was fixed: TciServer is now explicitly torn down in `~MainWindow()` after the audio thread stops but while RadioModel is still alive, preventing a use-after-free via `releaseDaxForTci()`. A belt-and-braces `QPointer<RadioModel>` was added so existing null-guards catch any future regression automatically.

In v26.5.1 three TCI v2.0 commands (volume, drive, rx_volume) were added to the dispatch table with bidirectional state sync (#1764, #2463). In v26.5.3 panadapter spectrum forwarding (#2841) and tx_gain / ALC (#2950) are exposed; right-click the TX slider to pick TX overflow handling (Clip / NaNGuard / Measure) for bit-exact digital-mode tone fidelity (#3065).

## Before you start

- AetherSDR must be connected to the radio. The TCI applet requires an active radio connection.
- The TCI server must be visible. If the applet panel is not showing the TCI section, click the **TCI** tray button on the right sidebar to reveal it.

## Steps

1. Click the **TCI** tray button on the right sidebar to open the TCI Server applet.

## What each control does

| Control                        | Default                                                                                                                     | Valid range                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Setting key                 |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|
| RX1..RX8 gain+meter            | 0.5                                                                                                                         | 0.0–1.0 (one slider per channel)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `TciRxGain1`..`TciRxGain8` |
| TX gain+meter                  | Drags set the TCI TX gain and emit tciTxGainChanged. Right-click opens TX overflow-mode picker (Clip / NaNGuard / Measure). | TciServer::setTxGain persists TciTxGain internally; UI mirrors the stored value. TCI TX audio is always allowed regardless of platform or hosted-DAX availability (evaluateDaxTxPolicy now unconditionally allows DaxTxRequestReason::TciTxAudio, v0.9.5.1, #2276). Right-click menu lets users choose how out-of-range (>1.0) samples from digital-mode clients are handled: Clip (saturating ±1.0, legacy default), NaNGuard (pass-through, only zero NaN/Inf), or Measure (true bypass with clip counting). Default is Clip so existing users see no behavior change (#3065). | `TciTxGain`                 |
| TX overflow mode (right-click) | Clip (0)                                                                                                                    | Clip (0), NaNGuard (1), Measure (2)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `TciTxOverflowMode`         |
| Port                           | 50001                                                                                                                       | 1024–65535 (out-of-range values snap to 50001)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `TciPort`                   |
| Enable                         | off                                                                                                                         | —                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | —                           |

### RX gain+meter sliders (RX1..RX8)

Each RX row has a combined meter and slider for channels RX1 through RX8. The meter portion reflects the live receive audio level from the assigned slice. The slider position sets the TCI RX gain for the channel and emits `tciRxGainChanged` when dragged. Each channel has its own setting key (`TciRxGain1` through `TciRxGain8`); the default for each is 0.5 with a valid range of 0.0–1.0.

The number of visible RX rows matches the radio's slice capacity (up to 8 on a FLEX-6700). Rows above the radio's maximum slice count are hidden automatically. On radios with fewer slices (for example, a FLEX-6600 with 4 slices), only the corresponding number of RX rows are shown.

### TX gain+meter slider

The **TX gain+meter** is a combined meter and slider. The meter portion reflects the live TX audio level from the active TX slice. The slider position sets the gain applied to that audio before it is sent to TCI clients.

The **TX gain+meter** slider has an accessible name "TCI TX gain" set in v26.6.3, improving screen reader compatibility.

#### Adjust TX gain

1. Locate the **TX:** row. The slice indicator to the right of the label shows which slice currently drives the TX channel (for example, `Slice A`), or `—` if no TX slice is assigned.
2. Drag the **TX gain+meter** slider left to reduce gain or right to increase gain. The valid range is `0.0` to `1.0`; the default is `0.5`.
3. Release the slider. The new value is saved immediately to `TciTxGain` and takes effect in the running server.

#### Choose TX overflow handling mode

1. Right-click the **TX gain+meter** slider to open the context menu.
2. Select one of the following modes:
   - **Clip (saturating ±1.0)** — Hard-clamp overshoots to ±1.0. Defensive default; introduces harmonics on overshoot but protects downstream int16 conversion.
   - **NaN guard (zero NaN/Inf only)** — Pass samples through bit-exact; only zero pathological NaN/Inf values. Preserves digital-mode tone fidelity; out-of-range floats reach the radio.
   - **Measure only (true bypass)** — Never mutate samples. Count overshoots for telemetry; the downstream int16 conversion still clamps in the radio-native DAX route.
3. The selection is saved immediately to `TciTxOverflowMode` and takes effect in the running server.

### Port field

The **Port** field sets the TCP port on which the TCI server listens. The default is 50001. Valid values are 1024–65535; out-of-range values snap back to 50001. Changing the port restarts the server if it is currently enabled.

### Enable button

The **Enable** button toggles the TCI server on or off. Clicking it starts or stops the server and emits `tciToggled`. If the server fails to bind to the configured port, the button snaps back to off and the status shows "(port in use)".

In v26.7.4, the button text changes dynamically:

- **Disabled** (off state) — The TCI server is stopped. The label uses the text "Disabled" when unchecked.
- **Enabled** (on state) — The TCI server is running. The label uses the text "Enabled" when checked.

The button starts in the state determined by `AutoStartTCI`. If `AutoStartTCI` is set to `True`, the button initializes as checked with the text "Enabled". If `AutoStartTCI` is `False` (the default), the button initializes as unchecked with the text "Disabled".

When clicked, the button toggles and its text updates immediately to match the new state. If the server fails to start (for example, because the port is in use), the button snaps back to the unchecked state and displays "Disabled" with the status label showing "(port in use)" in red.

The Enable button has an accessible name "TCI server enable" and accessible description "Start or stop the TCI server" (v26.7.4).

### Slice assignment labels

The RX rows and TX row each show a read-only slice assignment label to the right of the control. This label shows which slice currently drives that channel (for example, `Slice A`) or `—` if no slice is assigned. The labels share the same slice-to-DAX-channel mapping as the DAX applet and update automatically when slice assignments change.

The TCI receiver (trx) index is not capped at 4: trx is a positional slice index bounded by `slices.size()` (up to 8 on a FLEX-6700), so DAX channels 5–8 have TCI representation.

## Server status indicator

The TCI Server applet shows a status label next to the Enable button. This label displays one of three states:

| State                         | Meaning                                                                                   |
|-------------------------------|-------------------------------------------------------------------------------------------|
| `(stopped)`                   | Server is not running. The label uses the theme color `{{color.background.3}}` for text.  |
| `:<port> (N clients)`         | Server is running on the specified port with the given number of connected clients.       |
| `(port in use)`               | Server could not start because the port is already in use. The label turns red.           |

In v26.6.1, the status label styling was updated to use the theme color `{{color.background.3}}` instead of a hardcoded color, ensuring proper appearance with all AetherSDR themes.

## Tips

- If no slice label appears next to **TX:** (it shows `—`), no TX slice is assigned. Assign a TX slice on the radio before adjusting TX gain.
- The gain value persists across restarts. AetherSDR reads `TciTxGain` on launch and sets the slider to the stored value.
- Use **NaN guard** or **Measure only** when running digital modes that require bit-exact tone fidelity. The **Clip** mode may introduce harmonic distortion on overshoots.
- The **Measure only** mode is a true bypass and only counts overshoots for telemetry without modifying the audio stream.
- The Enable button text ("Enabled"/"Disabled") provides clear visual feedback about the server state, complementing the status label.

## Related

- [Adjust TCI RX gain per channel](adjust-tci-rx-gain-per-channel.md)
- [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md)
- [TCI Server overview](overview.md)