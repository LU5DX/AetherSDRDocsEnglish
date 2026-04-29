# Pick Opus vs Uncompressed Audio for SmartLink

Select the audio codec AetherSDR uses over SmartLink or LAN connections. Opus reduces bandwidth at the cost of a small amount of compression; uncompressed PCM preserves full fidelity when bandwidth allows. Auto lets the radio choose.

## Before you start

- AetherSDR must be connected to the radio. The Audio tab is not accessible without an active connection.
- Open `Settings > Radio Setup...` and click the **Audio** tab.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Audio** tab.
3. Under **Audio Compression (SmartLink):**, click **Auto**, **Uncompressed**, or **Opus** to select the codec.
   - **Auto** — the radio negotiates the codec automatically (default).
   - **Uncompressed** — sends raw PCM audio; uses more bandwidth.
   - **Opus** — sends Opus-encoded audio; lower bandwidth, slight compression.
4. Close the dialog. The setting takes effect immediately and is saved.

## What each control does

| Control | Default | Valid values |
|---|---|---|
| **Audio Compression (SmartLink):** Auto / Uncompressed / Opus | Auto | Auto, Uncompressed, Opus |
| **Audio Boost:** | — | Enabled / Disabled |
| **Audio Buffer:** | 200 ms | 50–1000 ms |
| **Recording:** Radio Side / Client Side | Radio Side | Radio Side, Client Side |
| **Save to:** | — | Folder path |
| **Auto-record on TX** | — | Checked / Unchecked |
| **Idle timeout:** | 120 sec | 10–3600 sec |
| **TX Follows Active Slice** | False | TX follows the active slice. Mutually exclusive with **Active Slice Follows TX**. Disabled automatically during Split operation. |
| **Active Slice Follows TX** | False | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with **TX Follows Active Slice**. |
| **Voice / CW / Digital filter sharpness sliders** | — | 0–3. Sets filter sharpness (0 = lowest latency to 3 = sharpest) per mode. Slider is disabled when Auto is enabled. Commands sent as `radio filter_sharpness <mode> level=<N>`. |
| **Auto (Voice / CW / Digital)** | — | Enabled / Disabled. Enables automatic filter-level selection for that mode; disables the manual sharpness slider. Commands sent as `radio filter_sharpness <mode> auto_level=1`. |
| **Connect / Disconnect (TGXL)** | Connect | Opens/closes direct TCP connection to the TGXL on port 9010. Saves IP and port to `TGXL_ManualIp` and `TGXL_ManualPort` on connect so AetherSDR auto-reconnects on startup. Required to recover TUNE on firmware 4.2+. When connected, the TUNE button sends the native `autotune` command directly to the TGXL instead of the radio-side path broken in firmware 4.2. The TGXL drives radio PTT via its hardware interlock cable; no client-side keying is needed. If the IP field is empty and the radio has discovered the TGXL, the discovered IP is pre-filled. |
| **Connect / Disconnect (PGXL)** | Connect | Opens/closes direct TCP connection to the Power Genius XL (default port 9008). Saves IP and port to `PGXL_ManualIp` and `PGXL_ManualPort`. |
| **Connect / Disconnect (Antenna Genius)** | Connect | Opens/closes connection to the Antenna Genius (default port 9007). Saves IP and port to `AG_ManualIp` and `AG_ManualPort`. |
| **Cal Frequency (MHz):** | — | Frequency used for manual calibration. Available regardless of whether a GPSDO is installed. If the field is empty when you click **Start**, a warning appears and calibration does not begin. |
| **Start** | — | Sets the calibration frequency, resets `freq_error_ppb` to 0, then starts the radio PLL calibration sweep. The button is disabled and labelled **Busy** while calibration is running. |
| **Freq Offset (ppb):** | — | Manual frequency offset in parts per billion. |

## RX tab — frequency calibration changes in v0.9.2.1

In previous versions, the **Cal Frequency (MHz):** field and **Start** button were only shown when no GPSDO was installed. From v0.9.2.1, those controls are always visible on the **RX** tab. The status banner at the top of the group still indicates whether a GPSDO is present (green text) or not (amber text).

When you click **Start**:

1. AetherSDR validates that the **Cal Frequency (MHz):** field is not empty. If it is empty, a warning message appears next to the button and calibration does not proceed.
2. The frequency offset is reset to 0 (`radio set freq_error_ppb=0`) and the calibration frequency is sent to the radio (`radio set cal_freq=<value>`).
3. The radio PLL calibration sweep begins (`radio pll_start`).
4. The **Start** button is disabled and shows **Busy** for the duration of the sweep.
5. A status label next to the button updates as the sweep progresses and shows the result when complete.

## Tips

- On a fast local LAN, **Uncompressed** avoids any codec artefacts and is the better choice for critical listening or digital mode decoding.
- On a slow or congested link (VPN, cellular SmartLink), **Opus** reduces audio dropouts. Pair it with a larger **Audio Buffer:** value (50–1000 ms) to absorb jitter.
- If audio sounds thin or quiet over SmartLink, try enabling **Audio Boost:** alongside Opus.
- If a GPSDO is installed, frequency calibration is rarely needed, but the controls are still available if you want to verify or manually trim the offset.

## Troubleshooting

- **Audio Compression buttons are greyed out or missing** — the Audio tab only builds after you click it, and only when a radio is connected. Verify the connection, then click the Audio tab again.
- **Audio quality is poor even with Uncompressed selected** — check network bandwidth and latency. Consider increasing **Audio Buffer:** to reduce underruns. See [Turn on audio boost or enlarge the audio buffer for remote operation](turn-on-audio-boost-or-enlarge-the-audio-buffer-for-remote-operation.md).
- **Start button shows "Busy" and does not return** — if the PLL sweep does not complete, close and reopen the Radio Setup dialog to reset the button state, then try again.
- **"Enter cal frequency" warning appears when clicking Start** — type a valid frequency (in MHz) into the **Cal Frequency (MHz):** field before clicking **Start**.

## Related

- [Turn on audio boost or enlarge the audio buffer for remote operation](turn-on-audio-boost-or-enlarge-the-audio-buffer-for-remote-operation.md)
- [Choose PC input/output audio devices](choose-pc-input-output-audio-devices.md)
- [Enable auto-record on TX and pick a save folder](enable-auto-record-on-tx-and-pick-a-save-folder.md)
- [Change network MTU for VPN/remote setups](change-network-mtu-for-vpn-remote-setups.md)