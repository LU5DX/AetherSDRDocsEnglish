# Change Network MTU for VPN/Remote Setups

The Network MTU setting controls the maximum packet size the radio sends over the network. Lowering it prevents fragmentation when you connect through a VPN or other tunnel that reduces the available path MTU.

## Before you start

- AetherSDR must be connected to the radio. The Network tab is not accessible when disconnected.
- Know the MTU of your VPN tunnel or network path. Common VPN MTUs are 1400–1450 bytes; a standard Ethernet path is 1500 bytes.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Network** tab.
3. Locate the **Network MTU:** spinbox.
4. Set the value to match your network path MTU.
5. Click **Apply** to push the new MTU to the radio.

## What each control does

| Control | Description | Default |
|---|---|---|
| **Network MTU:** | Outgoing packet size in bytes. Lower this when operating over a VPN or any link with a reduced MTU. | — |
| **Apply** | Sends the current Network tab configuration, including the MTU value, to the radio. | — |
| TX Follows Active Slice | TX follows the active slice. Mutually exclusive with Active Slice Follows TX. Disabled automatically during Split operation. | — |
| Active Slice Follows TX | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with TX Follows Active Slice. | — |
| Voice / CW / Digital filter sharpness sliders | Sets filter sharpness (0=lowest latency to 3=sharpest) per mode; slider is disabled when Auto is enabled. Commands sent as `radio filter_sharpness <mode> level=<N>`. | — |
| Auto (Voice / CW / Digital) | Enables automatic filter-level selection for that mode; disables the manual sharpness slider. Commands sent as `radio filter_sharpness <mode> auto_level=1`. | — |
| Connect / Disconnect (TGXL) | Opens/closes direct TCP connection to the TGXL on port 9010. Saves IP and port to `TGXL_ManualIp` and `TGXL_ManualPort` on connect so AetherSDR auto-reconnects on startup. Required to recover TUNE on firmware 4.2+. When connected, the TUNE button sends the native `autotune` command directly to the TGXL instead of the radio-side path broken in firmware 4.2. The TGXL drives radio PTT via its hardware interlock cable; no client-side keying is needed. If the IP field is empty and the radio has discovered the TGXL, the discovered IP is pre-filled. | — |
| Connect / Disconnect (PGXL) | Opens/closes direct TCP connection to the Power Genius XL (default port 9008). Saves IP and port to `PGXL_ManualIp` and `PGXL_ManualPort`. | — |
| Connect / Disconnect (Antenna Genius) | Opens/closes connection to the Antenna Genius (default port 9007). Saves IP and port to `AG_ManualIp` and `AG_ManualPort`. | — |

## Frequency calibration (RX tab)

In v0.9.2.1 the RX tab frequency calibration controls are available regardless of whether a GPSDO is installed. Previously, the **Cal Frequency (MHz):**, **Start**, and **Freq Offset (ppb):** controls were hidden when a GPSDO was detected. Now all calibration fields are always shown; a status label at the top of the group indicates whether a GPSDO is present (green text) or not (amber text).

### Calibration procedure

1. Open `Settings > Radio Setup...`.
2. Click the **RX** tab.
3. Enter a known-accurate reference frequency in the **Cal Frequency (MHz):** field.
4. Click **Start**.
   - The button label changes to **Busy** and is disabled while the calibration sweep runs.
   - A status label beside the button updates as the sweep progresses.
   - The radio first resets the frequency error to 0 ppb (`radio set freq_error_ppb=0`), then begins the PLL calibration sequence.
5. When calibration completes the button re-enables and the status label shows the result.
6. If you prefer to set the offset manually, enter a value directly in **Freq Offset (ppb):** without clicking **Start**.

### Calibration status messages

| Message | Meaning |
|---|---|
| Starting… | The sweep command has been sent to the radio. |
| Busy | PLL calibration is in progress. |
| Enter cal frequency | The **Cal Frequency (MHz):** field was empty when **Start** was clicked. Enter a value and try again. |

### Notes

- Clicking **Start** with an empty **Cal Frequency (MHz):** field shows an amber "Enter cal frequency" warning and does not send any commands.
- The calibration sequence logs the cal frequency and run ID to the debug protocol log (`lcProtocol`). You can view this in the AetherSDR log viewer if diagnostic logging is enabled.
- If the Radio Setup dialog is closed while a calibration is running, the in-flight callback is discarded safely; no partial state is applied.

## Tips

- If you are unsure what MTU to use, start at 1400 bytes and increase until you see packet loss or audio dropouts, then step back down by 10–20 bytes.
- The **Audio Buffer:** setting (found on the **Audio** tab) can help absorb jitter on VPN links independently of the MTU setting. See [Turn on audio boost or enlarge the audio buffer for remote operation](turn-on-audio-boost-or-enlarge-the-audio-buffer-for-remote-operation.md).

## Troubleshooting

- **Apply has no visible effect** — Confirm the radio is still connected. If the connection dropped, reconnect via `Settings > Connect to Radio...` and repeat the steps.
- **Audio breaks up after changing MTU** — The new value may still be too large for the path. Lower **Network MTU:** by another 20–50 bytes and click **Apply** again.
- **Start button stays disabled after calibration** — If the dialog was closed and reopened during a sweep, click **Start** again with the desired cal frequency. The previous run was discarded cleanly.

## Related

- [Switch the radio between DHCP and static IP](switch-the-radio-between-dhcp-and-static-ip.md)
- [Turn on audio boost or enlarge the audio buffer for remote operation](turn-on-audio-boost-or-enlarge-the-audio-buffer-for-remote-operation.md)
- [Pick Opus vs uncompressed audio for SmartLink](pick-opus-vs-uncompressed-audio-for-smartlink.md)