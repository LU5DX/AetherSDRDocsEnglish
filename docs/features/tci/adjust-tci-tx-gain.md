# Adjust TCI TX gain

Set the output gain that the TCI server applies to the transmit audio stream before sending it to connected clients (Log4OM, SunSDR tools, and similar).

## Before you start

- AetherSDR must be connected to the radio. The TCI applet requires an active radio connection.
- The TCI server must be visible. If the applet panel is not showing the TCI section, click the **TCI** tray button on the right sidebar to reveal it.

## Steps

1. Click the **TCI** tray button on the right sidebar to open the TCI Server applet.
2. Locate the **TX:** row. The slice indicator to the right of the label shows which slice currently drives the TX channel (for example, `Slice A`), or `—` if no TX slice is assigned.
3. Drag the **TX gain+meter** slider left to reduce gain or right to increase gain. The valid range is `0.0` to `1.0`; the default is `0.5`.
4. Release the slider. The new value is saved immediately to `TciTxGain` and takes effect in the running server.

## What each control does

| Control       | Default                                              | Valid range                                                                                                                                                                                                                                                         |
|---------------|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TX gain+meter | Drags set the TCI TX gain and emit tciTxGainChanged. | TciServer::setTxGain persists TciTxGain internally; UI mirrors the stored value. TCI TX audio is always allowed regardless of platform or hosted-DAX availability (evaluateDaxTxPolicy now unconditionally allows DaxTxRequestReason::TciTxAudio, v0.9.5.1, #2276). |

The **TX gain+meter** is a combined meter and slider. The meter portion reflects the live TX audio level from the active TX slice. The slider position sets the gain applied to that audio before it is sent to TCI clients.

The slice label next to **TX:** (for example, `Slice A` or `—`) is read-only. It shows which slice is currently assigned as the TX slice and updates automatically when the TX slice changes. Starting in v26.5.2.1, the slice label uses rich text formatting so that slice letters rendered as HTML display correctly (#2606).

## Tips

- If no slice label appears next to **TX:** (it shows `—`), no TX slice is assigned. Assign a TX slice on the radio before adjusting TX gain.
- The gain value persists across restarts. AetherSDR reads `TciTxGain` on launch and sets the slider to the stored value.

## Related

- [Adjust TCI RX gain per channel](adjust-tci-rx-gain-per-channel.md)
- [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md)
- [TCI Server overview](overview.md)