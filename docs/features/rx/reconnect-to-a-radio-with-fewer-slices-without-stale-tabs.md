# Reconnect to a radio with fewer slices without stale tabs

When you switch from a radio with more slices (for example, a FLEX-6700 with up to 8 slices) to one with fewer, the RX Controls applet rebuilds its slice tab buttons from scratch on every connection so no stale A–H tabs remain from the previous radio.

## Before you start

- You must have already connected to one radio and are about to connect to a different radio that has fewer slices.

## Steps

1. Disconnect from the current radio using your normal disconnect control.
2. Connect to the radio with fewer slices. The **Slice tabs (A..H)** row in the RX Controls applet is automatically torn down and rebuilt to match the new radio's slice count — only the tabs valid for the new radio appear.

> If the new radio has only one slice, the slice tab row is hidden entirely.

## What each control does

| Control | Behavior |
|---|---|
| **Slice tabs (A..H)** | Selects which slice the RX applet is bound to. Buttons are fully torn down and rebuilt on each connection (`clearSliceButtons()`), so tabs from a previous higher-slice radio never linger. Row is hidden if the radio exposes only one slice. |
| **Slice badge** | Displays the letter (A–H) of the currently bound slice, coloured by slice identity. |
| **🔓 / 🔒** | Toggles tune-lock on the active slice. A locked slice ignores incoming frequency changes. |
| **ANT1 (RX antenna)** | Opens a menu of available RX antennas; selecting one calls `setRxAntenna` on the slice. |
| **ANT1 (TX antenna)** | Opens a menu of TX-capable antennas (RX-only ports beginning with "RX" are filtered out); selecting one calls `setTxAntenna`. |
| **2.7K (filter width)** | Read-only indicator showing the current filter bandwidth. Updates when a filter preset is applied. |
| **QSK** | Lights amber when CW full break-in is active. Read-only; controlled from the CW applet. |
| **TX (badge)** | Click to designate this slice as the TX slice. |
| **Mode combo** | Sets the slice mode (USB, LSB, CW, AM, SAM, FM, NFM, DFM, DIGU, DIGL, RTTY; RADE if built with `HAVE_RADE`). Reshapes filter and step presets for the new mode. |
| **Frequency label** | Displays the current VFO frequency with dotted grouping. Click to enter edit mode. |
| **Frequency edit** | Type a frequency in MHz and press Enter to tune and re-centre. Escape cancels the entry and restores the previous frequency. Accepts up to 450 MHz on an XVTR antenna. |
| **STEP** | `<` / `>` or mousewheel cycles through per-mode step sizes. |
| **Filter width presets** | Click to apply a preset filter width; right-click to save the current width as a preset. Hidden in FM/NFM/DFM modes. |
| **Filter passband widget** | Drag the lo or hi edge to adjust the filter passband. |
| **Tone mode (FM)** | Selects CTCSS tone mode (Off or CTCSS TX). Visible only in FM family modes. |
| **CTCSS tone value** | Selects the CTCSS tone frequency (67.0–254.1 Hz). Enabled only when Tone mode is set to CTCSS TX. |
| **Offset (FM)** | Sets the FM repeater offset frequency in MHz (0.0–100.0, step 0.1). |
| **− (offset down)** | Sets repeater offset direction to down (TX below RX). |
| **Simplex** | Sets repeater offset to simplex (TX = RX). Default state. |
| **+ (offset up)** | Sets repeater offset direction to up (TX above RX). |
| **REV** | Inverts the TX offset sign to work a reversed repeater pair. |
| **🔊 / 🔇 (mute)** | Mutes the slice audio output. Default is unmuted. |
| **AF gain** | Adjusts slice audio output gain (0–100, default 70). |
| **L / R pan** | Pans slice audio between left (0) and right (100). Double-click resets to centre (50). |
| **SQL** | Enables squelch at the current slider level. |
| **Squelch level** | Sets the squelch threshold (0–100, default 20). Takes effect only when SQL is on. |
| **AGC mode** | Sets the slice AGC mode (Off, Slow, Med, Fast). Hidden in FM family modes. |
| **AGC threshold** | Sets the AGC threshold, or the AGC off-level when AGC mode is Off (0–100, default 65). |
| **RIT** | Toggles Receive Incremental Tuning on/off. |
| **RIT 0** | Zeroes the RIT offset. |
| **RIT offset** | Adjusts the RIT offset in 10 Hz steps via `<` / `>` or mousewheel. |
| **XIT** | Toggles Transmit Incremental Tuning on/off. |
| **XIT 0** | Zeroes the XIT offset. |
| **XIT offset** | Adjusts the XIT offset in 10 Hz steps via `<` / `>` or mousewheel. |

## Tips

- If a tab for a slice letter you expect is missing after reconnecting, the new radio's hardware slice limit is lower than the previous one — this is correct behaviour, not a bug.
- The duplicate-handler guard (`m_sliceButtonClicksConnected`) ensures that clicking a slice tab does not fire multiple times across reconnects even if you connect and disconnect repeatedly in the same session.

## Related

- [rx-controls-overview.md](rx-controls-overview.md)
- [connect-to-radio.md](connect-to-radio.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
